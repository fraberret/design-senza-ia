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


def esiti(d):
    return {x["id"]: x for x in d["controlli"]}


def test_oklch():
    """I colori in oklch() si leggono: #333 su un fondo oklch scuro non passa, il bianco sì."""
    d = pagina('<div style="background:oklch(0.25 0.05 250);padding:30px"><h1 style="color:#fff">Titolo chiaro</h1>'
               '<p style="color:#333">Testo scuro su fondo scuro, illeggibile.</p></div>')
    c = esiti(d)["contrasto"]
    assert c["esito"] == "errore", c
    assert "Titolo chiaro" not in c["dettaglio"], c


def test_foto_in_elemento_fratello():
    """Testo sopra un video o una foto messi in un elemento fratello (sfondi di Elementor): a occhio, mai ok."""
    d = pagina('<div style="position:relative;height:500px"><div style="position:absolute;inset:0">'
               '<img src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///ywAAAAAAQABAAACAUwAOw==" '
               'style="width:100%;height:100%" alt=""></div>'
               '<h1 style="position:relative;color:#222;padding:40px;margin:0">Titolo sopra la foto</h1></div>')
    assert esiti(d)["contrasto"]["esito"] == "a occhio", esiti(d)["contrasto"]


def test_errore_rete():
    """Un sito che non risponde: rapporto con l'errore e uscita 0, come cattura_scorrimento."""
    out = cartella()
    r = lancia("controllo_tecnico.py", "https://dominio-inesistente.invalid", "--out", out)
    assert r.returncode == 0, r.stderr[-400:]
    d = json.load(open(os.path.join(out, "tecnico.json")))
    assert d.get("errore"), d
    assert os.path.exists(os.path.join(out, "tecnico.md"))


def test_h1_nascosto():
    """Un H1 con display:none (versione solo telefono di Elementor) non conta."""
    d = pagina('<h1>Titolo vero</h1><h1 style="display:none">Titolo solo telefono</h1><p>Testo.</p>')
    assert esiti(d)["h1"]["esito"] == "ok", esiti(d)["h1"]


def test_classe_cookie_sul_body():
    """<body class="cookies-not-set"> (plugin Cookie Notice) non deve nascondere la pagina."""
    out = cartella()
    p = os.path.join(out, "pagina.html")
    open(p, "w").write('<!doctype html><html lang="it"><head><meta charset="utf-8"><title>Prova</title></head>'
                       '<body class="cookies-not-set"><h1>Titolo</h1><p style="color:#bbb">Testo grigio chiaro.</p></body></html>')
    c = esiti(controlla(p))["contrasto"]
    assert c["esito"] == "errore", c


def test_banner_cookie():
    """Il banner si nasconde senza clic: il suo testo non conta e i terzi caricati al clic non partono."""
    d = pagina('<h1>Titolo</h1><p>Testo.</p><div id="cookie-banner" style="background:#fff;color:#ccc">'
               'Usiamo i cookie <button onclick="var i=new Image();i.src=\'https://www.youtube.com/x.png\'">Accetta</button></div>')
    c = esiti(d)
    assert c["contrasto"]["esito"] == "ok", c["contrasto"]
    assert c["terzi-al-caricamento"]["esito"] == "ok", c["terzi-al-caricamento"]


def test_contrasto_senza_testi():
    """Zero testi controllati non è un superamento."""
    d = pagina('<img src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///ywAAAAAAQABAAACAUwAOw==" width="200" height="200" alt="x">')
    assert esiti(d)["contrasto"]["esito"] != "ok", esiti(d)["contrasto"]


def test_animazione_css_esterno():
    """Un'animazione infinita in un foglio di stile separato, senza prefers-reduced-motion: errore."""
    d = controlla(os.path.join(FIX, "css-esterno", "pagina.html"))
    assert esiti(d)["movimento-ridotto"]["esito"] == "errore", esiti(d)["movimento-ridotto"]


def test_transizioni_di_colore():
    """Le transizioni solo di colore restano ammesse con prefers-reduced-motion: niente errore."""
    d = pagina('<style>a{transition:color .2s, background-color .2s}.t{display:block;transition:filter .15s}</style><a class="t" href="#y">Tasto</a><h1>Titolo</h1><p><a href="#x">Un link</a></p>')
    assert esiti(d)["movimento-ridotto"]["esito"] == "ok", esiti(d)["movimento-ridotto"]


if __name__ == "__main__":
    esegui([test_pagina_buona, test_pagina_cattiva, test_testo_su_immagine, test_file_locale,
            test_testo_nascosto, test_bersaglio_isolato, test_bersagli_vicini,
            test_oklch, test_foto_in_elemento_fratello, test_errore_rete, test_h1_nascosto,
            test_classe_cookie_sul_body, test_banner_cookie, test_contrasto_senza_testi, test_animazione_css_esterno,
            test_transizioni_di_colore])
