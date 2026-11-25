"""Cattura e confronto dei concorrenti (o dei riferimenti).

Uso: scripts/py.sh cattura_concorrenti.py <url1> <url2> ... --out <cartella> [--etichetta concorrenti]
     scripts/py.sh cattura_concorrenti.py --file urls.txt --out <cartella>

Per ogni sito: prima schermata su computer e telefono, le prime tre schermate, colori misurati,
font, titolo d'apertura, menu e il punteggio dei segnali IA (stesso metro di controllo_slop.py).
Scrive <etichetta>.md (tabella da leggere), <etichetta>.json e due fogli di confronto.
"""
import argparse
import os
import sys

from playwright.sync_api import sync_playwright

sys.path.insert(0, os.path.dirname(__file__))
import comune as C  # noqa: E402
import controllo_slop as S  # noqa: E402


def punteggio_rapido(pg):
    r = pg.evaluate(S.JS, [S.BANALI, S.FONT_DEFAULT])
    p, nomi = 100, []
    for sid, occ in r["T"].items():
        if sid in S.SEGNALI and occ:
            peso = S.SEGNALI[sid][0]
            if sid == "etichette-sopra-titoli" and len(occ) == 1:
                peso = round(peso * 0.3)
            p -= peso
            nomi.append(sid)
    return max(0, p), nomi


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("urls", nargs="*")
    ap.add_argument("--file")
    ap.add_argument("--out", required=True)
    ap.add_argument("--etichetta", default="concorrenti")
    a = ap.parse_args()
    urls = list(a.urls)
    if a.file:
        urls += [l.strip() for l in open(a.file) if l.strip() and not l.startswith("#")]
    out = os.path.abspath(os.path.expanduser(a.out))
    cart = os.path.join(out, a.etichetta)
    os.makedirs(cart, exist_ok=True)

    righe, dati, fogli_c, fogli_m, nomi = [], [], [], [], []
    with sync_playwright() as p:
        b = p.chromium.launch(headless=True)
        for u in urls:
            url = C.url_da_argomento(u)
            n = C.nome_sicuro(url)
            try:
                ctx, pg, _ = C.apri(b, url)
                pg.screenshot(path=os.path.join(cart, f"{n}-computer.png"))
                C.scorri_tutta(pg, passo=900, pausa=80)
                tre = os.path.join(cart, f"{n}-tre-schermate.png")
                pg.screenshot(path=tre, full_page=True)
                from PIL import Image
                im = Image.open(tre)
                im.crop((0, 0, im.width, min(im.height, 2700))).save(tre)
                ex = C.estrai(pg)
                punt, segnali = punteggio_rapido(pg)
                ctx.close()
                ctx, pm, _ = C.apri(b, url, 390, 844, mobile=True, attesa=1500)
                pm.screenshot(path=os.path.join(cart, f"{n}-telefono.png"))
                ctx.close()
                pal = C.tavolozza_da_immagine(tre, colori=6)
                h1 = next((t["testo"] for t in ex["titoli"] if t["tag"] == "H1"), (ex["titoli"][0]["testo"] if ex["titoli"] else ""))
                font = C.font_principali(ex["font"], 3)
                d = {"url": url, "nome": n, "titolo": ex["titolo"], "h1": h1, "font": font,
                     "colori": [c["hex"] for c in pal], "menu": ex["nav"][:10], "parole": ex["parole"],
                     "punteggio_ia": punt, "segnali": segnali, "generator": ex["generator"]}
                dati.append(d)
                fogli_c.append(os.path.join(cart, f"{n}-computer.png"))
                fogli_m.append(os.path.join(cart, f"{n}-telefono.png"))
                nomi.append(f"{n} · IA {punt}/100")
                print(f"ok {n}: {punt}/100")
            except Exception as e:
                dati.append({"url": url, "nome": n, "errore": str(e)[:160]})
                print(f"errore {n}: {str(e)[:120]}")
        b.close()

    C.foglio(fogli_c, os.path.join(out, f"{a.etichetta}-computer.jpg"), colonne=2, larghezza=700, etichette=nomi)
    C.foglio(fogli_m, os.path.join(out, f"{a.etichetta}-telefono.jpg"), colonne=4, larghezza=300, etichette=nomi)
    C.scrivi_json(os.path.join(out, f"{a.etichetta}.json"), dati)
    righe = [f"# {a.etichetta.capitalize()}: confronto", "",
             "Punteggio IA: 100 = nessun segnale di default (stesso metro del controllo finale).", "",
             "| Sito | Titolo d'apertura | Font | Colori dominanti | IA | Segnali |", "|---|---|---|---|---|---|"]
    for d in dati:
        if "errore" in d:
            righe.append(f"| {d['url']} | errore: {d['errore']} | | | | |")
            continue
        righe.append(f"| [{d['nome']}]({d['url']}) | {d['h1'][:70]} | {', '.join(d['font'])} | {' '.join(d['colori'][:4])} | {d['punteggio_ia']} | {', '.join(d['segnali'][:6])} |")
    righe += ["", f"Fogli: `{a.etichetta}-computer.jpg`, `{a.etichetta}-telefono.jpg`; schermate singole in `{a.etichetta}/`.",
              "", "Da ricavare leggendo le schermate: cosa fanno TUTTI (la media del settore, da non copiare),",
              "cosa fa il migliore e perché, quale spazio resta libero per il cliente."]
    with open(os.path.join(out, f"{a.etichetta}.md"), "w") as f:
        f.write("\n".join(righe))
    print(f"fatto: {out}/{a.etichetta}.md")


if __name__ == "__main__":
    main()
