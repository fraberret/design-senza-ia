"""Fotogrammi dello scorrimento di una pagina, per studiare siti con movimento.

Uso: scripts/py.sh cattura_scorrimento.py <url|file> --out <cartella> [--fotogrammi 12] [--webgpu]

Scorre con la rotella a passi (900 px per fotogramma), aspetta ~1 s perché le animazioni si
assestino e salva f00.png … fNN.png a 1440×900 più foglio.jpg (4 colonne). I banner dei cookie
si nascondono con il CSS, mai accettati. Con un errore di rete scrive errore.txt ed esce con 0,
così un elenco di siti non si ferma. --webgpu apre un browser visibile con WebGPU attivo (per
siti come bizar.ro); senza, se la pagina dice di richiedere WebGPU, lo scrive in errore.txt.
"""
import argparse
import os
import re
import sys

from PIL import Image
from playwright.sync_api import sync_playwright

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import comune  # noqa: E402

ARGS_WEBGPU = ["--disable-http2", "--enable-unsafe-webgpu", "--enable-features=Vulkan,WebGPU", "--use-angle=metal"]


def foglio_4(fotogrammi, percorso, colonne=4, w=480):
    ims = [Image.open(f).convert("RGB") for f in fotogrammi]
    ims = [i.resize((w, int(i.height * w / i.width))) for i in ims]
    h = max(i.height for i in ims)
    righe = (len(ims) + colonne - 1) // colonne
    c = Image.new("RGB", (colonne * (w + 10), righe * (h + 10)), "white")
    for k, i in enumerate(ims):
        c.paste(i, ((k % colonne) * (w + 10), (k // colonne) * (h + 10)))
    c.save(percorso, quality=82)


def main():
    a = argparse.ArgumentParser()
    a.add_argument("pagina")
    a.add_argument("--out", required=True)
    a.add_argument("--fotogrammi", type=int, default=12)
    a.add_argument("--webgpu", action="store_true")
    o = a.parse_args()
    os.makedirs(o.out, exist_ok=True)
    url = comune.url_da_argomento(o.pagina)
    errore_txt = os.path.join(o.out, "errore.txt")
    if os.path.exists(errore_txt):  # resto di un giro precedente
        os.remove(errore_txt)
    avvisi = []
    fotogrammi = []

    with sync_playwright() as p:
        if o.webgpu:
            b = p.chromium.launch(headless=False, args=ARGS_WEBGPU)
        else:
            b = p.chromium.launch()
        try:
            ctx, pg, _ = comune.apri(b, url, attesa=3000)
        except Exception as e:  # rete, DNS, HTTP/2 anche dopo la riprova
            msg = comune.prima_riga(e)
            open(errore_txt, "w").write(
                f"{url}\nerrore: {msg}\n"
                + ("" if o.webgpu else "Il sito può rifiutare il browser automatico: in quel caso si cattura a mano dal browser.\n"))
            print(f"errore: {msg}")
            b.close()
            comune.chiudi_riprove()
            return 0
        corpo = pg.evaluate("(document.body && document.body.innerText) || ''")
        # avviso solo se la pagina dice di aver bisogno di WebGPU, non se lo nomina e basta
        if not o.webgpu and len(corpo) < 600 and re.search(
                r"(needs?|requires?|require|richiede|serve)\s+WebGPU|WebGPU\s+(is\s+)?(not\s+(supported|available)|non\s+(è\s+)?support)",
                corpo, re.I):
            avvisi.append("La pagina sembra richiedere WebGPU: rilanciare con --webgpu (browser visibile).")
        try:
            for i in range(o.fotogrammi):
                f = os.path.join(o.out, f"f{i:02d}.png")
                pg.screenshot(path=f)
                fotogrammi.append(f)
                for _ in range(6):
                    pg.mouse.wheel(0, 150)
                    pg.wait_for_timeout(120)
                pg.wait_for_timeout(900)
        except Exception as e:  # pagina che si chiude o si blocca a metà: si tiene quello che c'è
            avvisi.append(f"cattura interrotta al fotogramma {len(fotogrammi)}: {comune.prima_riga(e)}")
        ctx.close()
        b.close()
    comune.chiudi_riprove()

    if fotogrammi:
        foglio_4(fotogrammi, os.path.join(o.out, "foglio.jpg"))
    if avvisi:
        open(errore_txt, "w").write(f"{url}\n" + "\n".join(avvisi) + "\n")
        print("\n".join(avvisi))
    print(o.out)
    return 0

if __name__ == "__main__":
    sys.exit(main())
