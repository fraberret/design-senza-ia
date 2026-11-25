"""Controllo tecnico di una pagina: contrasti, telefono, SEO di base, velocità, privacy.

Uso: scripts/py.sh controllo_tecnico.py <url|file> --out <cartella>

Scrive <cartella>/tecnico.md (tabella leggibile) e tecnico.json, stampa "N errori · M avvisi".
Esiti: ok, avviso, errore, "a occhio" (non calcolabile: testo sopra immagini o gradienti).
Le soglie vengono da references/seo-accessibilita-velocita-legale.md e checklist-consegna.md.
I banner dei cookie si nascondono con il CSS, mai accettati: le richieste a terzi contano
dal caricamento in poi, senza alcun clic.
"""
import argparse
import json
import os
import re
import sys
from urllib.parse import urlparse

from playwright.sync_api import sync_playwright

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import comune as C  # noqa: E402

# domini che richiedono il consenso prima di essere chiamati (Garante, 2021-2022)
TERZI_VIETATI = ("fonts.googleapis.com", "fonts.gstatic.com", "youtube.com", "youtube-nocookie.com",
                 "ytimg.com", "google-analytics.com", "googletagmanager.com", "facebook.com",
                 "facebook.net", "maps.googleapis.com", "maps.gstatic.com", "doubleclick.net")

REGOLE = {
    "contrasto": "testo 4,5:1; testo grande (≥ 24 px o ≥ 18,66 px grassetto) 3:1 (WCAG 1.4.3)",
    "bersagli": "a 390 px: link e pulsanti ≥ 24×24 px o distanziati (WCAG 2.5.8), obiettivo 44×44; esclusi i link nel testo",
    "sbordamento": "nessuno scorrimento orizzontale a 360, 390 e 1440 px",
    "testi-piccoli": "a 390 px nessun testo sotto i 16 px (piccole note ammesse, da guardare)",
    "h1": "un solo H1",
    "lang": "attributo lang sull'elemento html",
    "title": "title tra 30 e 60 caratteri",
    "description": "meta description tra 70 e 160 caratteri",
    "canonical": "link rel=canonical presente",
    "og": "og:title, og:description, og:image",
    "jsonld": "dati strutturati JSON-LD leggibili",
    "alt": "ogni img ha l'attributo alt (vuoto se decorativa)",
    "dimensioni-img": "ogni img ha width e height (niente spostamenti, CLS ≤ 0,1)",
    "lcp-lazy": "l'immagine più grande della prima schermata non ha loading=lazy (LCP ≤ 2,5 s)",
    "terzi-al-caricamento": "nessuna richiesta a font, video, mappe o analisi di terzi prima del consenso",
    "font-formato": "font in WOFF2",
    "movimento-ridotto": "con animazioni o transizioni c'è @media (prefers-reduced-motion)",
    "senza-js": "con JavaScript spento resta almeno l'80% del testo",
    "piva": "P.IVA (11 cifre) in home",
    "tel": "i numeri di telefono sono link tel:",
}

JS_CONTRASTO = r"""
() => {
  const rgba = s => { const m = s.match(/rgba?\(([^)]+)\)/); if (!m) return [0,0,0,0];
    const p = m[1].split(/[\s,\/]+/).filter(Boolean).map(parseFloat); return [p[0],p[1],p[2],p.length>3?p[3]:1]; };
  const sopra = (a, b) => { const t = a[3] + b[3]*(1-a[3]); if (!t) return [255,255,255,1];
    return [0,1,2].map(i => (a[i]*a[3] + b[i]*b[3]*(1-a[3]))/t).concat([t]); };
  const lum = c => { const f = v => { v/=255; return v<=0.03928 ? v/12.92 : Math.pow((v+0.055)/1.055, 2.4); };
    return 0.2126*f(c[0]) + 0.7152*f(c[1]) + 0.0722*f(c[2]); };
  const rapporto = (a, b) => { const x = lum(a), y = lum(b); return (Math.max(x,y)+0.05)/(Math.min(x,y)+0.05); };
  const vis = e => { const r = e.getBoundingClientRect(); const s = getComputedStyle(e);
    if (r.width <= 2 || r.height <= 2 || r.right <= 0 || r.bottom <= -scrollY || r.left >= document.documentElement.scrollWidth) return false;
    if (/rect\(0(px)?,? 0(px)?,? 0(px)?,? 0(px)?\)/.test(s.clip) || /inset\(50%\)/.test(s.clipPath)) return false;
    return s.visibility !== 'hidden' && s.display !== 'none' && parseFloat(s.opacity) > 0.05; };
  const sfondo = e => { // risale i genitori: null se c'è un'immagine, un gradiente o un video sotto
    let strati = [];
    for (let n = e; n && n.nodeType === 1; n = n.parentElement) {
      const s = getComputedStyle(n);
      if (s.backgroundImage && s.backgroundImage !== 'none') return null;
      if (n !== e && (n.querySelector(':scope > video, :scope > img, :scope > picture, :scope > canvas'))) {
        const r = e.getBoundingClientRect();
        for (const m of n.querySelectorAll(':scope > video, :scope > img, :scope > picture, :scope > canvas')) {
          const q = m.getBoundingClientRect();
          if (m !== e && !m.contains(e) && q.left < r.right && q.right > r.left && q.top < r.bottom && q.bottom > r.top) return null;
        }
      }
      const c = rgba(s.backgroundColor); if (c[3] > 0) strati.push(c);
      if (c[3] >= 1) break;
    }
    let b = [255,255,255,1];
    for (let i = strati.length - 1; i >= 0; i--) b = sopra(strati[i], b);
    return b;
  };
  const out = { falliti: [], occhio: [], controllati: 0 };
  const tutti = document.body ? document.body.querySelectorAll('*') : [];
  for (const e of tutti) {
    if (['SCRIPT','STYLE','NOSCRIPT','SVG','svg','OPTION'].includes(e.tagName)) continue;
    const diretto = [...e.childNodes].some(n => n.nodeType === 3 && n.textContent.trim().length > 0);
    if (!diretto || !vis(e)) continue;
    const s = getComputedStyle(e);
    const px = parseFloat(s.fontSize), peso = parseInt(s.fontWeight) || 400;
    const grande = px >= 24 || (px >= 18.66 && peso >= 700);
    const minimo = grande ? 3 : 4.5;
    const testo = e.textContent.replace(/\s+/g,' ').trim().slice(0, 60);
    const b = sfondo(e);
    out.controllati++;
    if (!b) { out.occhio.push(testo); continue; }
    const t = sopra(rgba(s.color), b);
    const r = rapporto(t, b);
    if (r < minimo) out.falliti.push({ testo, rapporto: Math.round(r*100)/100, minimo, colore: s.color, px });
  }
  return out;
}
"""

JS_PAGINA = r"""
() => {
  const vis = e => { const r = e.getBoundingClientRect(); const s = getComputedStyle(e);
    return r.width > 0 && r.height > 0 && s.visibility !== 'hidden' && s.display !== 'none'; };
  const meta = (a, n) => { const m = document.querySelector(`meta[${a}="${n}"]`); return m ? m.content : null; };
  const ld = [...document.querySelectorAll('script[type="application/ld+json"]')].map(s => {
    try { const j = JSON.parse(s.textContent); const tipi = [];
      const giro = x => { if (Array.isArray(x)) x.forEach(giro); else if (x && typeof x === 'object') {
        if (x['@type']) tipi.push([].concat(x['@type']).join('/')); if (x['@graph']) giro(x['@graph']); } };
      giro(j); return { ok: true, tipi }; } catch (e) { return { ok: false, errore: String(e).slice(0, 120) }; } });
  const imgs = [...document.images];
  const alt = imgs.filter(i => !i.hasAttribute('alt')).map(i => (i.currentSrc || i.src).split('/').pop().slice(0, 60));
  const dim = imgs.filter(i => !(i.hasAttribute('width') && i.hasAttribute('height')) && vis(i))
    .map(i => (i.currentSrc || i.src).split('/').pop().slice(0, 60));
  const H = innerHeight;
  const prima = imgs.filter(i => { const r = i.getBoundingClientRect(); return vis(i) && r.top < H && r.bottom > 0; })
    .map(i => { const r = i.getBoundingClientRect(); return { src: (i.currentSrc || i.src).split('/').pop().slice(0, 60),
      area: r.width * r.height, lazy: i.getAttribute('loading') === 'lazy' }; })
    .sort((a, b) => b.area - a.area);
  let css = '';
  for (const sh of document.styleSheets) { try { for (const r of sh.cssRules) css += r.cssText + '\n'; } catch (e) {} }
  document.querySelectorAll('[style]').forEach(e => css += e.getAttribute('style') + '\n');
  const animazioni = /@keyframes|animation(-name)?\s*:\s*(?!none)[a-z]/i.test(css) ||
    /transition(-property)?\s*:\s*(?!none|all 0s)[^;]*\d*\.?\d+m?s/i.test(css);
  const ridotto = /prefers-reduced-motion/i.test(css);
  const corpo = (document.body && document.body.innerText) || '';
  const piva = /P\.?\s?IVA[^\d]{0,30}\d{11}|Partita IVA[^\d]{0,30}\d{11}/i.test(corpo);
  const tel = [...new Set((corpo.match(/(?:\+39[\s.]?)?(?:0\d{1,3}|3\d{2})(?:[\s./-]?\d{2,4}){2,4}/g) || [])
    .map(x => x.trim()).filter(x => { const n = x.replace(/\D/g, ''); return n.length >= 8 && n.length <= 13 && /[\s./-]/.test(x); }))];
  const telLink = document.querySelectorAll('a[href^="tel:"]').length;
  return { title: document.title || '', description: meta('name', 'description'), lang: document.documentElement.lang || '',
    canonical: !!document.querySelector('link[rel="canonical"]'),
    og: ['og:title', 'og:description', 'og:image'].filter(n => !meta('property', n)),
    h1: [...document.querySelectorAll('h1')].map(h => h.innerText.trim().slice(0, 60)),
    ld, alt, dim, prima: prima.slice(0, 3), animazioni, ridotto, piva, tel: tel.slice(0, 5), telLink,
    testo: corpo.replace(/\s+/g, ' ').trim().length };
}
"""

JS_TELEFONO = r"""
() => {
  const vis = e => { const r = e.getBoundingClientRect(); const s = getComputedStyle(e);
    if (r.width <= 2 || r.height <= 2 || r.right <= 0 || r.bottom <= -scrollY || r.left >= document.documentElement.scrollWidth) return false;
    if (/rect\(0(px)?,? 0(px)?,? 0(px)?,? 0(px)?\)/.test(s.clip) || /inset\(50%\)/.test(s.clipPath)) return false;
    return s.visibility !== 'hidden' && s.display !== 'none' && parseFloat(s.opacity) > 0.05; };
  const nelTesto = a => { // link dentro una frase: esenti da WCAG 2.5.8
    if (getComputedStyle(a).display !== 'inline') return false;
    const p = a.parentElement; if (!p) return false;
    const resto = [...p.childNodes].filter(n => n !== a).map(n => n.textContent).join('').trim();
    return resto.length > 0;
  };
  const bers = [...document.querySelectorAll('a[href], button, input:not([type=hidden]), select, textarea, [role=button]')]
    .filter(vis).filter(e => !(e.tagName === 'A' && nelTesto(e)))
    .map(e => { const r = e.getBoundingClientRect();
      return { testo: (e.innerText || e.getAttribute('aria-label') || e.value || e.tagName).trim().slice(0, 40),
               w: Math.round(r.width), h: Math.round(r.height), r: [r.left, r.top, r.right, r.bottom] }; });
  // WCAG 2.5.8, eccezione della spaziatura: un bersaglio sotto 24 px passa se il cerchio di 24 px
  // centrato su di lui non tocca altri bersagli né i cerchi degli altri bersagli piccoli
  const centro = x => [(x.r[0] + x.r[2]) / 2, (x.r[1] + x.r[3]) / 2];
  const dist = (c, q) => Math.hypot(Math.max(q[0] - c[0], 0, c[0] - q[2]), Math.max(q[1] - c[1], 0, c[1] - q[3]));
  const piccolo = x => x.w < 24 || x.h < 24;
  for (const x of bers) {
    if (!piccolo(x)) continue;
    const c = centro(x);
    x.vicino = bers.some(y => y !== x && (dist(c, y.r) < 12 || (piccolo(y) && Math.hypot(c[0] - centro(y)[0], c[1] - centro(y)[1]) < 24)));
  }
  bers.forEach(x => delete x.r);
  const piccoli = []; const visti = new Set();
  for (const e of document.body.querySelectorAll('*')) {
    const diretto = [...e.childNodes].some(n => n.nodeType === 3 && n.textContent.trim().length > 1);
    if (!diretto || !vis(e)) continue;
    const px = parseFloat(getComputedStyle(e).fontSize);
    if (px < 16) { const t = e.textContent.replace(/\s+/g, ' ').trim().slice(0, 40); if (!visti.has(t)) { visti.add(t); piccoli.push({ testo: t, px }); } }
  }
  return { bers, piccoli };
}
"""

SBORDA = "() => document.documentElement.scrollWidth - document.documentElement.clientWidth"


def dominio_base(h):
    h = (h or "").lower()
    return h[4:] if h.startswith("www.") else h


def stesso_sito(h, base):
    h = dominio_base(h)
    return bool(base) and (h == base or h.endswith("." + base) or base.endswith("." + h))


def valuta(url, js_on, js_off, tel_dati, sbordi, richieste):
    ctr = []

    def add(i, esito, dettaglio):
        ctr.append({"id": i, "esito": esito, "dettaglio": dettaglio})

    co = js_on["contrasto"]
    if co["falliti"]:
        ex = "; ".join(f'"{f["testo"][:40]}" {f["rapporto"]}:1 (min {f["minimo"]})' for f in co["falliti"][:4])
        add("contrasto", "errore", f'{len(co["falliti"])} testi sotto soglia: {ex}')
    elif co["occhio"]:
        add("contrasto", "a occhio", f'{len(co["occhio"])} testi sopra immagini, video o gradienti: '
            + "; ".join(f'"{t[:40]}"' for t in co["occhio"][:4]))
    else:
        add("contrasto", "ok", f'{co["controllati"]} testi controllati')

    b = tel_dati["bers"]
    sotto24 = [x for x in b if (x["w"] < 24 or x["h"] < 24) and x.get("vicino")]
    sotto44 = [x for x in b if x not in sotto24 and (x["w"] < 44 or x["h"] < 44)]
    if sotto24:
        add("bersagli", "errore", f"{len(sotto24)} sotto 24 px e troppo vicini ad altri: "
            + "; ".join(f'"{x["testo"]}" {x["w"]}×{x["h"]}' for x in sotto24[:5]))
    elif sotto44:
        add("bersagli", "avviso", f"{len(sotto44)} tra 24 e 44 px: " + "; ".join(f'"{x["testo"]}" {x["w"]}×{x["h"]}' for x in sotto44[:5]))
    else:
        add("bersagli", "ok", f"{len(b)} bersagli ≥ 44 px")

    fuori = {k: v for k, v in sbordi.items() if v > 1}
    add("sbordamento", "errore" if fuori else "ok",
        ", ".join(f"{k} px: {v} px in più" for k, v in fuori.items()) if fuori else "360, 390, 1440 senza scorrimento orizzontale")

    p = tel_dati["piccoli"]
    add("testi-piccoli", "avviso" if p else "ok",
        f"{len(p)} testi sotto 16 px: " + "; ".join(f'"{x["testo"]}" {x["px"]:g} px' for x in p[:5]) if p else "tutti ≥ 16 px")

    pg = js_on["pagina"]
    n = len(pg["h1"])
    add("h1", "ok" if n == 1 else "errore", f'{n} H1: ' + " | ".join(pg["h1"][:3]))
    add("lang", "ok" if pg["lang"] else "errore", f'lang="{pg["lang"]}"' if pg["lang"] else "manca lang su <html>")
    t = len(pg["title"])
    add("title", "ok" if 30 <= t <= 60 else "avviso", f'{t} caratteri: "{pg["title"][:70]}"')
    d = len(pg["description"] or "")
    add("description", "ok" if 70 <= d <= 160 else "avviso", f"{d} caratteri" if d else "manca")
    add("canonical", "ok" if pg["canonical"] else "avviso", "presente" if pg["canonical"] else "manca")
    add("og", "avviso" if pg["og"] else "ok", "mancano " + ", ".join(pg["og"]) if pg["og"] else "completi")
    ld = pg["ld"]
    if any(not x["ok"] for x in ld):
        add("jsonld", "errore", "JSON-LD non leggibile: " + "; ".join(x["errore"] for x in ld if not x["ok"]))
    elif not ld:
        add("jsonld", "avviso", "nessun dato strutturato")
    else:
        add("jsonld", "ok", "tipi: " + ", ".join(t for x in ld for t in x["tipi"]))
    add("alt", "errore" if pg["alt"] else "ok", "senza alt: " + ", ".join(pg["alt"][:5]) if pg["alt"] else "tutte con alt")
    add("dimensioni-img", "avviso" if pg["dim"] else "ok",
        "senza width/height: " + ", ".join(pg["dim"][:5]) if pg["dim"] else "tutte con width e height")
    pr = pg["prima"]
    if pr and pr[0]["lazy"]:
        add("lcp-lazy", "errore", f'{pr[0]["src"]} è la più grande della prima schermata e ha loading=lazy')
    else:
        add("lcp-lazy", "ok", f'immagine principale: {pr[0]["src"]}' if pr else "nessuna immagine nella prima schermata")

    base = dominio_base(urlparse(url).hostname)
    terzi = []
    for r in richieste:
        u = urlparse(r["url"])
        if u.scheme not in ("http", "https") or stesso_sito(u.hostname, base):
            continue
        terzi.append(r["url"])
    vietati = sorted({urlparse(x).hostname for x in terzi if any(dominio_base(urlparse(x).hostname).endswith(v) for v in TERZI_VIETATI)})
    altri = sorted({urlparse(x).hostname for x in terzi} - set(vietati))
    if vietati:
        add("terzi-al-caricamento", "errore", "prima del consenso: " + ", ".join(vietati) + (f" (altri: {', '.join(altri[:5])})" if altri else ""))
    elif altri:
        add("terzi-al-caricamento", "avviso", "domini esterni al caricamento, da verificare: " + ", ".join(altri[:8]))
    else:
        add("terzi-al-caricamento", "ok", "nessuna richiesta a terzi senza clic")

    font = sorted({r["url"].split("?")[0].split("/")[-1] for r in richieste
                   if (r["tipo"] == "font" or re.search(r"\.(ttf|otf|woff2?|eot)(\?|$)", r["url"]))
                   and not re.search(r"\.woff2(\?|$)", r["url"]) and not r["url"].startswith("data:")})
    add("font-formato", "avviso" if font else "ok", "non WOFF2: " + ", ".join(font[:5]) if font else "solo WOFF2 o nessun font scaricato")

    if pg["animazioni"] and not pg["ridotto"]:
        add("movimento-ridotto", "errore", "animazioni o transizioni senza @media (prefers-reduced-motion)")
    else:
        add("movimento-ridotto", "ok", "rispettato" if pg["animazioni"] else "nessuna animazione")

    con, senza = pg["testo"], js_off.get("testo", 0)
    quota = (senza / con) if con else 1
    add("senza-js", "ok" if quota >= 0.8 else "avviso", f"senza JavaScript resta il {round(100 * quota)}% del testo")
    add("piva", "ok" if pg["piva"] else "avviso", "presente" if pg["piva"] else "P.IVA con 11 cifre non trovata nel testo")
    if pg["tel"] and not pg["telLink"]:
        add("tel", "avviso", "numeri senza link tel: " + ", ".join(pg["tel"][:3]))
    else:
        add("tel", "ok", f'{pg["telLink"]} link tel:' if pg["telLink"] else "nessun numero nel testo")
    return ctr


def scrivi(out, url, ctr):
    e = sum(1 for c in ctr if c["esito"] == "errore")
    a = sum(1 for c in ctr if c["esito"] == "avviso")
    C.scrivi_json(os.path.join(out, "tecnico.json"), {"pagina": url, "errori": e, "avvisi": a, "controlli": ctr})
    righe = [f"# Controllo tecnico\n\nPagina: {url}\n\n**{e} errori · {a} avvisi**\n",
             "| Controllo | Esito | Dettaglio | Regola |", "|---|---|---|---|"]
    for c in ctr:
        det = c["dettaglio"].replace("|", "/")
        righe.append(f'| {c["id"]} | {c["esito"]} | {det} | {REGOLE[c["id"]]} |')
    righe.append("\n\"a occhio\": il contrasto non si calcola sopra immagini o gradienti; va guardato sulle schermate.")
    open(os.path.join(out, "tecnico.md"), "w").write("\n".join(righe) + "\n")
    return e, a


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pagina")
    ap.add_argument("--out", required=True)
    o = ap.parse_args()
    os.makedirs(o.out, exist_ok=True)
    url = C.url_da_argomento(o.pagina)
    richieste = []
    with sync_playwright() as p:
        b = p.chromium.launch()
        ctx, pg, _ = C.apri(b, url, richieste=richieste, attesa=1500)
        pagina = pg.evaluate(JS_PAGINA)  # prima dello scorrimento: la prima schermata vera
        C.scorri_tutta(pg)
        contrasto = pg.evaluate(JS_CONTRASTO)
        sbordi = {"1440": pg.evaluate(SBORDA)}
        ctx.close()
        tel = None
        for w in (390, 360):
            ctx, pm, _ = C.apri(b, url, w, 844, mobile=True, attesa=1000)
            C.scorri_tutta(pm)
            sbordi[str(w)] = pm.evaluate(SBORDA)
            if w == 390:
                tel = pm.evaluate(JS_TELEFONO)
            ctx.close()
        ctx, pn, _ = C.apri(b, url, javascript=False, attesa=500)
        senza = {"testo": len(re.sub(r"\s+", " ", pn.inner_text("body")).strip()) if pn.query_selector("body") else 0}
        ctx.close()
        b.close()
    ctr = valuta(url, {"contrasto": contrasto, "pagina": pagina}, senza, tel, sbordi, richieste)
    e, a = scrivi(o.out, url, ctr)
    print(f"{e} errori · {a} avvisi")
    print(os.path.join(o.out, "tecnico.md"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
