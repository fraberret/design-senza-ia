"""Test di comune.py. Uso: scripts/py.sh tests/test_comune.py"""
import sys

from comune_test import SCRIPTS, esegui

sys.path.insert(0, SCRIPTS)
import comune  # noqa: E402


class Pagina:
    def __init__(self, rifiuta):
        self.rifiuta = rifiuta
    def on(self, *a): pass
    def goto(self, *a, **k):
        if self.rifiuta:
            raise RuntimeError("net::ERR_HTTP2_PROTOCOL_ERROR")
    def wait_for_load_state(self, *a, **k): pass
    def wait_for_timeout(self, *a): pass
    def add_style_tag(self, **k): pass


class Contesto:
    def __init__(self, rifiuta):
        self.rifiuta = rifiuta
    def new_page(self): return Pagina(self.rifiuta)
    def close(self): pass


class Browser:
    lanci = 0
    def __init__(self, rifiuta):
        self.rifiuta = rifiuta
        self.browser_type = self
        self.chiuso = False
    def new_context(self, **k): return Contesto(self.rifiuta)
    def launch(self, **k):
        Browser.lanci += 1
        return Browser(False)
    def close(self): self.chiuso = True


def test_riprova_http2_un_solo_browser():
    """Più aperture di un sito che rifiuta HTTP/2 riusano lo stesso browser senza HTTP/2, e chiudi() lo chiude."""
    Browser.lanci = 0
    b = Browser(True)
    for _ in range(4):
        comune.apri(b, "https://esempio.it", attesa=0)
    assert Browser.lanci == 1, f"lanciati {Browser.lanci} browser"
    riprova = comune._BROWSER_SENZA_HTTP2[0]
    comune.chiudi_riprove()
    assert riprova.chiuso and not comune._BROWSER_SENZA_HTTP2


if __name__ == "__main__":
    esegui([test_riprova_http2_un_solo_browser])
