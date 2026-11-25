"""Test di controllo_tecnico.py. Uso: scripts/py.sh tests/test_controllo_tecnico.py"""
import json
import os

from comune_test import FIX, cartella, esegui, lancia


def controlla(pagina):
    out = cartella()
    r = lancia("controllo_tecnico.py", pagina, "--out", out)
    assert r.returncode == 0, r.stderr[-800:]
    assert os.path.exists(os.path.join(out, "tecnico.md")), "manca tecnico.md"
    return json.load(open(os.path.join(out, "tecnico.json")))


def con_esito(dati, esito):
    return {c["id"] for c in dati["controlli"] if c["esito"] == esito}


def test_pagina_buona():
    d = controlla(os.path.join(FIX, "pagina-buona.html"))
    assert d["errori"] == 0, [c for c in d["controlli"] if c["esito"] == "errore"]


def test_pagina_cattiva():
    d = controlla(os.path.join(FIX, "pagina-cattiva.html"))
    attesi = {"contrasto", "h1", "lang", "alt", "lcp-lazy", "terzi-al-caricamento", "movimento-ridotto", "bersagli"}
    assert con_esito(d, "errore") == attesi, sorted(con_esito(d, "errore") ^ attesi)


def test_testo_su_immagine():
    out = cartella()
    p = os.path.join(out, "pagina.html")
    open(p, "w").write(
        '<!doctype html><html lang="it"><head><meta charset="utf-8"><title>Prova</title></head>'
        '<body style="margin:0"><div style="height:600px;background:linear-gradient(#123,#c96)">'
        '<h1 style="color:#fff;margin:0;padding:40px">Titolo sopra un gradiente</h1></div></body></html>')
    d = controlla(p)
    c = {x["id"]: x["esito"] for x in d["controlli"]}
    assert c["contrasto"] == "a occhio", c["contrasto"]


def test_file_locale():
    d = controlla(os.path.join(FIX, "pagina-buona.html"))
    c = {x["id"]: x for x in d["controlli"]}
    assert c["terzi-al-caricamento"]["esito"] == "ok", c["terzi-al-caricamento"]


def pagina(corpo):
    out = cartella()
    p = os.path.join(out, "pagina.html")
    open(p, "w").write('<!doctype html><html lang="it"><head><meta charset="utf-8">'
                       '<meta name="viewport" content="width=device-width,initial-scale=1"><title>Prova</title>'
                       '<style>body{margin:0;font:17px/1.6 sans-serif;color:#111;background:#fff}'
                       '.sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);color:#fff}'
                       '.salta{position:absolute;left:-9999px}</style></head><body>' + corpo + '</body></html>')
    return controlla(p)


def test_testo_nascosto():
    """Testo solo per lettori di schermo (1×1 px) e link fuori schermo non contano."""
    d = pagina('<a class="salta" href="#c">Salta al contenuto</a><h1 id="c">Titolo</h1>'
               '<span class="sr">Solo per lettori di schermo</span><p>Testo normale.</p>')
    c = {x["id"]: x for x in d["controlli"]}
    assert c["contrasto"]["esito"] == "ok", c["contrasto"]
    assert c["bersagli"]["esito"] != "errore", c["bersagli"]


def test_bersaglio_isolato():
    """WCAG 2.5.8, eccezione della spaziatura: un link alto 22 px senza vicini non è un errore."""
    d = pagina('<h1>Titolo</h1><p style="margin:40px 0"><a href="#x" style="line-height:22px">Chiedi informazioni</a></p>')
    c = {x["id"]: x for x in d["controlli"]}
    assert c["bersagli"]["esito"] == "avviso", c["bersagli"]


def test_bersagli_vicini():
    """Due pulsanti da 18 px attaccati: errore."""
    d = pagina('<h1>Titolo</h1><p><button style="width:18px;height:18px;padding:0;border:0" aria-label="A">a</button>'
               '<button style="width:18px;height:18px;padding:0;border:0" aria-label="B">b</button></p>')
    c = {x["id"]: x for x in d["controlli"]}
    assert c["bersagli"]["esito"] == "errore", c["bersagli"]


if __name__ == "__main__":
    esegui([test_pagina_buona, test_pagina_cattiva, test_testo_su_immagine, test_file_locale,
            test_testo_nascosto, test_bersaglio_isolato, test_bersagli_vicini])
