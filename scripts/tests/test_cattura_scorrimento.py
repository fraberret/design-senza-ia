"""Test di cattura_scorrimento.py. Uso: scripts/py.sh tests/test_cattura_scorrimento.py"""
import hashlib
import os

from comune_test import FIX, cartella, esegui, lancia


def test_fotogrammi():
    out = cartella()
    r = lancia("cattura_scorrimento.py", os.path.join(FIX, "scorrimento.html"), "--out", out, "--fotogrammi", "6")
    assert r.returncode == 0, r.stderr[-500:]
    nomi = [f"f{i:02d}.png" for i in range(6)]
    for n in nomi:
        assert os.path.exists(os.path.join(out, n)), f"manca {n}"
    assert os.path.exists(os.path.join(out, "foglio.jpg")), "manca foglio.jpg"
    hash_ = {hashlib.md5(open(os.path.join(out, n), "rb").read()).hexdigest() for n in nomi}
    assert len(hash_) >= 4, f"solo {len(hash_)} fotogrammi diversi"


def test_errore_rete():
    out = cartella()
    r = lancia("cattura_scorrimento.py", "https://dominio-inesistente.invalid", "--out", out)
    assert r.returncode == 0, f"codice {r.returncode}: {r.stderr[-300:]}"
    assert os.path.exists(os.path.join(out, "errore.txt")), "manca errore.txt"


def test_webgpu_avviso():
    out = cartella()
    r = lancia("cattura_scorrimento.py", os.path.join(FIX, "webgpu.html"), "--out", out, "--fotogrammi", "2")
    assert r.returncode == 0, r.stderr[-300:]
    p = os.path.join(out, "errore.txt")
    assert os.path.exists(p), "manca errore.txt"
    assert "WebGPU" in open(p).read()


def test_webgpu_nominato():
    """Una pagina che parla di WebGPU ma funziona non produce l'avviso."""
    out = cartella()
    p = os.path.join(out, "articolo.html")
    open(p, "w").write("<!doctype html><html lang=it><body><h1>Novità</h1><p>" + "Testo dell'articolo. " * 40
                       + "Chrome supporta WebGPU da tempo.</p></body></html>")
    r = lancia("cattura_scorrimento.py", p, "--out", out, "--fotogrammi", "1")
    assert r.returncode == 0, r.stderr[-300:]
    assert not os.path.exists(os.path.join(out, "errore.txt"))


def test_errore_vecchio_cancellato():
    """Un errore.txt di un giro precedente sparisce dopo una cattura riuscita."""
    out = cartella()
    open(os.path.join(out, "errore.txt"), "w").write("vecchio")
    r = lancia("cattura_scorrimento.py", os.path.join(FIX, "scorrimento.html"), "--out", out, "--fotogrammi", "1")
    assert r.returncode == 0, r.stderr[-300:]
    assert not os.path.exists(os.path.join(out, "errore.txt"))


def test_casi_limite():
    """--fotogrammi 0 non va in crash; un messaggio d'errore vuoto non va in crash."""
    out = cartella()
    r = lancia("cattura_scorrimento.py", os.path.join(FIX, "scorrimento.html"), "--out", out, "--fotogrammi", "0")
    assert r.returncode == 0, r.stderr[-300:]
    import sys
    from comune_test import SCRIPTS
    sys.path.insert(0, SCRIPTS)
    import comune
    assert comune.prima_riga(Exception("")) == "Exception"


if __name__ == "__main__":
    esegui([test_fotogrammi, test_errore_rete, test_webgpu_avviso, test_webgpu_nominato, test_errore_vecchio_cancellato,
            test_casi_limite])
