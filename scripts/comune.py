"""Funzioni comuni: apertura pagine con Playwright, schermate, estrazione di colori, font e struttura.

Usato da analizza_sito.py, cattura_concorrenti.py e controllo_slop.py.
"""
import atexit
import json
import os
import re
from collections import Counter
from urllib.parse import urlparse

from PIL import Image, ImageDraw

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/131.0 Safari/537.36")
UA_MOBILE = ("Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 "
             "(KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1")

# banner dei cookie: nascosti con il CSS, mai accettati
_BANNER = ("[id*=cookie i],[class*=cookie i],[id*=consent i],[class*=consent i],[id*=iubenda i],"
           "[class*=iubenda i],#CybotCookiebotDialog,[class*=cmplz],[id*=gdpr i],[class*=gdpr i],"
           ".cky-consent-container,#onetrust-banner-sdk,#usercentrics-root,.cc-window,.cookie-pop")
# mai html, body o main: plugin come Cookie Notice mettono "cookies-not-set" sul body
NASCONDI_BANNER = ",".join(x + ":not(html):not(body):not(main)" for x in _BANNER.split(",")) + "{display:none!important}"


def prima_riga(e):
    """Prima riga del messaggio di un'eccezione, o il suo tipo se il messaggio è vuoto."""
    return (str(e).strip().splitlines() or [type(e).__name__])[0]


def url_da_argomento(x):
    """Accetta un URL o un file locale; restituisce un URL apribile."""
    if re.match(r"^https?://", x):
        return x
    p = os.path.abspath(os.path.expanduser(x))
    if os.path.exists(p):
        return "file://" + p
    return "https://" + x


def nome_sicuro(url):
    h = urlparse(url).netloc or os.path.basename(urlparse(url).path)
    return re.sub(r"[^a-zA-Z0-9.-]", "_", h.replace("www.", ""))[:60] or "pagina"


_BROWSER_SENZA_HTTP2 = []  # al massimo un browser per la riprova senza HTTP/2, riusato e chiuso alla fine


def chiudi_riprove():
    """Chiude il browser della riprova senza HTTP/2, se è stato aperto."""
    while _BROWSER_SENZA_HTTP2:
        try:
            _BROWSER_SENZA_HTTP2.pop().close()
        except Exception:
            pass


atexit.register(chiudi_riprove)


def apri(browser, url, larghezza=1440, altezza=900, mobile=False, attesa=2500, riprova_http2=True,
         richieste=None, javascript=True):
    """Apre la pagina in un contesto nuovo. Se il sito rifiuta HTTP/2 del browser automatico
    (ERR_HTTP2_PROTOCOL_ERROR), riprova con un browser lanciato con --disable-http2.
    richieste: lista in cui raccogliere gli URL richiesti dal caricamento in poi (senza clic).
    javascript: False per vedere la pagina come la vede chi non esegue JavaScript."""
    def contesto(b):
        c = b.new_context(
            user_agent=UA_MOBILE if mobile else UA,
            viewport={"width": larghezza, "height": altezza},
            is_mobile=mobile, has_touch=mobile, device_scale_factor=1, locale="it-IT",
            java_script_enabled=javascript,
        )
        p = c.new_page()
        if richieste is not None:
            p.on("request", lambda r: richieste.append({"url": r.url, "tipo": r.resource_type}))
        p.on("pageerror", lambda e: errori.append(str(e)[:200]))
        return c, p

    errori = []
    ctx, pg = contesto(browser)
    try:
        pg.goto(url, wait_until="domcontentloaded", timeout=60000)
    except Exception as e:
        if not (riprova_http2 and "ERR_HTTP2_PROTOCOL_ERROR" in str(e)):
            ctx.close()
            raise
        ctx.close()
        if not _BROWSER_SENZA_HTTP2:
            _BROWSER_SENZA_HTTP2.append(browser.browser_type.launch(args=["--disable-http2"]))
        ctx, pg = contesto(_BROWSER_SENZA_HTTP2[0])
        pg.goto(url, wait_until="domcontentloaded", timeout=60000)
    try:
        pg.wait_for_load_state("load", timeout=20000)
    except Exception:
        pass
    pg.wait_for_timeout(attesa)
    if javascript:  # add_style_tag usa JavaScript: con JavaScript spento si bloccherebbe
        try:
            pg.add_style_tag(content=NASCONDI_BANNER)
        except Exception:
            pass
    return ctx, pg, errori


def scorri_tutta(pg, passo=700, pausa=120):
    """Scorre la pagina con la rotella per far caricare immagini pigre e comparse."""
    h = pg.evaluate("document.documentElement.scrollHeight")
    y = 0
    while y < h and y < 40000:
        pg.mouse.wheel(0, passo)
        pg.wait_for_timeout(pausa)
        y += passo
        h = pg.evaluate("document.documentElement.scrollHeight")
    pg.wait_for_timeout(600)
    pg.evaluate("window.scrollTo(0,0)")
    pg.wait_for_timeout(300)


def schermata_intera(pg, percorso, max_altezza=16000):
    pg.screenshot(path=percorso, full_page=True)
    im = Image.open(percorso)
    if im.height > max_altezza:
        im.crop((0, 0, im.width, max_altezza)).save(percorso)
    return percorso


def tagli(percorso, uscita_prefisso, altezza_taglio=1800, larghezza_max=1100):
    """Taglia una schermata intera in pezzi leggibili (jpg), restituisce i percorsi."""
    im = Image.open(percorso).convert("RGB")
    out = []
    n = (im.height + altezza_taglio - 1) // altezza_taglio
    for i in range(n):
        c = im.crop((0, i * altezza_taglio, im.width, min(im.height, (i + 1) * altezza_taglio)))
        c.thumbnail((larghezza_max, 2000))
        p = f"{uscita_prefisso}-{i + 1:02d}.jpg"
        c.save(p, quality=80)
        out.append(p)
    return out


def foglio(immagini, percorso, colonne=2, larghezza=700, etichette=None):
    """Mette più immagini in un foglio di confronto."""
    ims = []
    for f in immagini:
        try:
            i = Image.open(f).convert("RGB")
            i = i.resize((larghezza, int(i.height * larghezza / i.width)))
            ims.append(i)
        except Exception:
            continue
    if not ims:
        return None
    h = max(i.height for i in ims) + 26
    righe = (len(ims) + colonne - 1) // colonne
    c = Image.new("RGB", (colonne * (larghezza + 10), righe * (h + 10)), "white")
    d = ImageDraw.Draw(c)
    for k, i in enumerate(ims):
        x, y = (k % colonne) * (larghezza + 10), (k // colonne) * (h + 10)
        c.paste(i, (x, y + 24))
        if etichette:
            d.text((x + 4, y + 6), str(etichette[k])[:90], fill="black")
    c.save(percorso, quality=82)
    return percorso


def tavolozza_da_immagine(percorso, colori=10, altezza_max=4000):
    """Colori dominanti misurati sui pixel (più affidabile del CSS)."""
    im = Image.open(percorso).convert("RGB")
    im = im.crop((0, 0, im.width, min(im.height, altezza_max)))
    im.thumbnail((400, 4000))
    q = im.quantize(colors=colori, method=Image.Quantize.MEDIANCUT)
    pal = q.getpalette()
    conti = sorted(q.getcolors(), reverse=True)
    tot = sum(c for c, _ in conti)
    out = []
    for c, idx in conti:
        r, g, b = pal[idx * 3: idx * 3 + 3]
        out.append({"hex": f"#{r:02x}{g:02x}{b:02x}", "quota": round(100 * c / tot, 1)})
    return out


JS_ESTRAI = r"""
() => {
  const vis = e => { const r = e.getBoundingClientRect(); const s = getComputedStyle(e);
    return r.width > 0 && r.height > 0 && s.visibility !== 'hidden' && s.display !== 'none' && parseFloat(s.opacity) > 0.05; };
  const testo = e => (e.innerText || '').replace(/\s+/g, ' ').trim();
  const font = {}; const pesi = {};
  document.querySelectorAll('h1,h2,h3,h4,p,li,a,button,span,label').forEach(e => {
    if (!vis(e) || !testo(e)) return; const s = getComputedStyle(e);
    const f = s.fontFamily.split(',')[0].replace(/["']/g, '').trim(); font[f] = (font[f] || 0) + 1;
    pesi[f + ' ' + s.fontWeight] = (pesi[f + ' ' + s.fontWeight] || 0) + 1; });
  const titoli = [...document.querySelectorAll('h1,h2,h3')].filter(vis).map(h => ({ tag: h.tagName, testo: testo(h).slice(0, 140),
    font: getComputedStyle(h).fontFamily.split(',')[0].replace(/["']/g, ''), size: parseFloat(getComputedStyle(h).fontSize),
    peso: getComputedStyle(h).fontWeight, colore: getComputedStyle(h).color })).slice(0, 60);
  const raggi = {}; document.querySelectorAll('div,section,article,a,button,img,figure,li').forEach(e => {
    if (!vis(e)) return; const s = getComputedStyle(e); const r = s.borderTopLeftRadius;
    if (r && r !== '0px' && (s.backgroundColor !== 'rgba(0, 0, 0, 0)' || s.borderTopWidth !== '0px' || e.tagName === 'IMG' || s.boxShadow !== 'none')) raggi[r] = (raggi[r] || 0) + 1; });
  const nav = [...document.querySelectorAll('nav a, header a')].filter(vis).map(a => testo(a)).filter(t => t && t.length < 40);
  const corpo = testo(document.body);
  const tel = [...new Set((corpo.match(/(?:\+39[\s.]?)?(?:0\d{1,3}|3\d{2})(?:[\s./-]?\d{2,4}){2,4}/g) || []).map(x => x.trim()).filter(x => { const n = x.replace(/\D/g, ''); return n.length >= 8 && n.length <= 12 && /[\s./-]/.test(x); }))].slice(0, 6);
  const email = [...new Set(corpo.match(/[\w.+-]+@[\w-]+\.[\w.]+/g) || [])].slice(0, 6);
  const indirizzi = [...new Set((corpo.match(/(?:Via|Viale|Piazza|Piazzale|Corso|Largo|Vicolo|Strada|Lungotevere)\s(?:[A-ZÀ-Üa-zà-ü'.]+\s?){1,6},?\s?\d{1,4}(?:[\/.]?[A-Za-z])?(?:\s?[-–,]\s?\d{5})?(?:\s[A-Z][a-zà-ü]+)?/g) || []).map(x => x.trim()))].slice(0, 6);
  const piva = (corpo.match(/(?:P\.?\s?IVA|Partita IVA)[^\d]{0,40}(\d{11})/i) || [])[1] || null;
  const link = [...document.querySelectorAll('a[href]')].map(a => a.href);
  const social = [...new Set(link.filter(h => /facebook|instagram|linkedin|youtube|tiktok|twitter|x\.com/i.test(h)))].slice(0, 12);
  const video = [...new Set([...document.querySelectorAll('iframe[src],a[href]')].map(e => e.src || e.href)
    .map(u => (u.match(/(?:youtube(?:-nocookie)?\.com\/(?:embed\/|watch\?v=)|youtu\.be\/)([\w-]{11})/) || [])[1]).filter(Boolean))];
  const immagini = [...document.images].filter(i => i.naturalWidth >= 200 && vis(i)).map(i => ({ src: i.currentSrc || i.src, w: i.naturalWidth, h: i.naturalHeight, alt: i.alt })).slice(0, 80);
  const svg = document.querySelectorAll('svg').length;
  const meta = n => (document.querySelector(`meta[name="${n}"]`) || {}).content || null;
  return { titolo: document.title, descrizione: meta('description'), generator: meta('generator'), lingua: document.documentElement.lang,
    titoli, font, pesi, raggi, nav: [...new Set(nav)].slice(0, 30), tel, email, indirizzi, piva, social, video, immagini, svg,
    parole: corpo.split(' ').length, testo: corpo.slice(0, 12000) };
}
"""


def estrai(pg):
    return pg.evaluate(JS_ESTRAI)


def scrivi_json(percorso, dati):
    with open(percorso, "w") as f:
        json.dump(dati, f, ensure_ascii=False, indent=1)


def font_principali(font_conti, n=4):
    return [f for f, _ in Counter(font_conti).most_common(n)]
