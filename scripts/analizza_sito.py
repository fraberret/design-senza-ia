"""Analisi del sito da rifare.

Uso: scripts/py.sh analizza_sito.py <url> --out <cartella> [--pagine 6] [--no-immagini]

Produce in <cartella>:
  analisi.json            tutti i dati estratti
  analisi.md              sintesi leggibile (da leggere per prima)
  schermate/              home intera su computer (in pezzi) e telefono, prima schermata delle pagine interne
  materiale/              immagini del sito (>= 300 px), favicon, copertine dei video YouTube
  testi/                  testo di ogni pagina visitata, per l'inventario dei contenuti
"""
import argparse
import os
import re
import sys
import urllib.request
from urllib.parse import urljoin, urlparse

from playwright.sync_api import sync_playwright

sys.path.insert(0, os.path.dirname(__file__))
import comune as C  # noqa: E402


def scarica(url, dest):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": C.UA})
        with urllib.request.urlopen(req, timeout=25) as r:
            dati = r.read()
        if len(dati) < 2000:
            return False
        with open(dest, "wb") as f:
            f.write(dati)
        return True
    except Exception:
        return False


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("url")
    ap.add_argument("--out", required=True)
    ap.add_argument("--pagine", type=int, default=6, help="pagine interne del menu da visitare")
    ap.add_argument("--no-immagini", action="store_true")
    a = ap.parse_args()

    url = C.url_da_argomento(a.url)
    out = os.path.abspath(os.path.expanduser(a.out))
    for d in ("schermate", "materiale", "testi"):
        os.makedirs(os.path.join(out, d), exist_ok=True)

    risultato = {"url": url}
    with sync_playwright() as p:
        b = p.chromium.launch(headless=True)

        # home su computer
        ctx, pg, errori = C.apri(b, url)
        C.scorri_tutta(pg)
        dati = C.estrai(pg)
        intera = C.schermata_intera(pg, os.path.join(out, "schermate", "home-computer-intera.png"))
        pezzi = C.tagli(intera, os.path.join(out, "schermate", "home-computer"))
        pg.screenshot(path=os.path.join(out, "schermate", "home-computer-prima.png"))
        altezza = pg.evaluate("document.documentElement.scrollHeight")
        link_interni = pg.evaluate("""(h) => [...document.querySelectorAll('nav a[href], header a[href]')]
            .map(a => ({t: (a.innerText||'').trim(), u: a.href})).filter(x => x.t && x.u.includes(h) && !x.u.includes('#'))""",
                                   urlparse(url).netloc)
        ctx.close()

        # home su telefono
        ctx, pgm, _ = C.apri(b, url, 390, 844, mobile=True)
        C.scorri_tutta(pgm)
        pgm.screenshot(path=os.path.join(out, "schermate", "home-telefono-prima.png"))
        mob = C.schermata_intera(pgm, os.path.join(out, "schermate", "home-telefono-intera.png"))
        C.tagli(mob, os.path.join(out, "schermate", "home-telefono"), altezza_taglio=2600, larghezza_max=420)
        ctx.close()

        # pagine interne del menu
        visti, interne = set([url.rstrip("/")]), []
        for l in link_interni:
            u = l["u"].split("#")[0].rstrip("/")
            if u in visti or len(interne) >= a.pagine or re.search(r"\.(pdf|jpg|png|zip)$", u, re.I):
                continue
            visti.add(u)
            try:
                c2, p2, _ = C.apri(b, u, attesa=1500)
                d2 = C.estrai(p2)
                nome = C.nome_sicuro(u) + "-" + re.sub(r"\W+", "-", l["t"].lower())[:30]
                p2.screenshot(path=os.path.join(out, "schermate", f"pagina-{len(interne) + 1:02d}.png"))
                with open(os.path.join(out, "testi", f"{len(interne) + 1:02d}-{nome}.txt"), "w") as f:
                    f.write(f"{l['t']}\n{u}\n\n" + d2["testo"])
                interne.append({"voce": l["t"], "url": u, "titolo": d2["titolo"],
                                "titoli": [t["testo"] for t in d2["titoli"]][:12], "parole": d2["parole"]})
                c2.close()
            except Exception as e:
                interne.append({"voce": l["t"], "url": u, "errore": str(e)[:120]})
        b.close()

    with open(os.path.join(out, "testi", "00-home.txt"), "w") as f:
        f.write(dati["testo"])

    tavolozza = C.tavolozza_da_immagine(intera)

    # materiale: immagini grandi, favicon, copertine video
    scaricate = []
    if not a.no_immagini:
        imgs = sorted(dati["immagini"], key=lambda i: -(i["w"] * i["h"]))
        for i, im in enumerate(imgs[:30]):
            ext = os.path.splitext(urlparse(im["src"]).path)[1][:5] or ".jpg"
            dest = os.path.join(out, "materiale", f"img-{i + 1:02d}{ext}")
            if im["w"] >= 300 and scarica(im["src"], dest):
                scaricate.append({"file": os.path.basename(dest), **im})
        scarica(urljoin(url, "/favicon.ico"), os.path.join(out, "materiale", "favicon.ico"))
        for v in dati["video"]:
            if not scarica(f"https://i.ytimg.com/vi/{v}/maxresdefault.jpg", os.path.join(out, "materiale", f"video-{v}.jpg")):
                scarica(f"https://i.ytimg.com/vi/{v}/hqdefault.jpg", os.path.join(out, "materiale", f"video-{v}.jpg"))

    risultato.update({"dati": {k: v for k, v in dati.items() if k != "testo"}, "tavolozza": tavolozza,
                      "altezza_home": altezza, "errori_js": errori, "pagine_interne": interne,
                      "immagini_scaricate": scaricate, "pezzi_schermata": [os.path.basename(x) for x in pezzi]})
    C.scrivi_json(os.path.join(out, "analisi.json"), risultato)

    # sintesi leggibile
    d = dati
    font = sorted(d["font"].items(), key=lambda x: -x[1])[:6]
    raggi = sorted(d["raggi"].items(), key=lambda x: -x[1])[:6]
    r = [f"# Analisi di {url}", "",
         f"- **Titolo:** {d['titolo']}", f"- **Descrizione:** {d['descrizione']}",
         f"- **CMS/generatore:** {d['generator'] or 'non dichiarato'} · lingua `{d['lingua']}` · {d['parole']} parole in home · altezza {altezza}px",
         f"- **Menu:** {', '.join(d['nav'][:20])}", "",
         "## Contatti trovati",
         f"- Telefoni: {', '.join(d['tel']) or '-'}", f"- Email: {', '.join(d['email']) or '-'}",
         f"- Indirizzi: {', '.join(d['indirizzi']) or '-'}", f"- P.IVA: {d['piva'] or '-'}",
         f"- Social: {', '.join(d['social']) or '-'}", f"- Video YouTube: {', '.join(d['video']) or '-'}", "",
         "## Struttura dei titoli (home)"] + [f"- {t['tag']} ({t['font']} {t['size']:.0f}px/{t['peso']}): {t['testo']}" for t in d["titoli"][:40]] + [
         "", "## Colori misurati sui pixel (quota della pagina)"] + [f"- `{c['hex']}` {c['quota']}%" for c in tavolozza] + [
         "", "## Font usati (elementi di testo)"] + [f"- {f}: {n}" for f, n in font] + [
         "", "## Arrotondamenti più frequenti"] + [f"- {k}: {n}" for k, n in raggi] + [
         "", f"## Immagini: {len(d['immagini'])} visibili ≥ 200 px, {len(scaricate)} scaricate in materiale/; SVG in pagina: {d['svg']}",
         "", "## Pagine interne visitate"] + [f"- **{x['voce']}** ({x.get('parole', '?')} parole) {x['url']}: " + "; ".join(x.get("titoli", [])[:5]) for x in interne] + [
         "", f"Errori JavaScript: {len(errori)}", "",
         "Schermate in `schermate/` (home-computer-NN.jpg in ordine), testi in `testi/`."]
    with open(os.path.join(out, "analisi.md"), "w") as f:
        f.write("\n".join(r))
    print(f"fatto: {out}/analisi.md · {len(pezzi)} pezzi di schermata · {len(interne)} pagine interne · {len(scaricate)} immagini")


if __name__ == "__main__":
    main()
