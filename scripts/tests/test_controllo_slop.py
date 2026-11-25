"""Test di controllo_slop.py. Uso: scripts/py.sh tests/test_controllo_slop.py

La regressione usa due pagine locali indicate da variabili d'ambiente (vedi locale.md):
DSI_PAGINA_PULITA (deve restare 100) e DSI_PAGINA_SLOP (deve restare ≤ 30). Se mancano, il test è saltato.
"""
import json
import os

from comune_test import FIX, cartella, esegui, lancia


def controlla(pagina, *extra):
    out = cartella()
    r = lancia("controllo_slop.py", pagina, "--out", out, *extra, timeout=400)
    assert r.returncode == 0, r.stderr[-800:]
    return json.load(open(os.path.join(out, "controllo.json")))


def test_seconda_ondata():
    d = controlla(os.path.join(FIX, "seconda-ondata.html"))
    ids = {s["id"] for s in d["segnali"]}
    attesi = {"crema-terracotta", "freccia-su-link", "puntini-mediani", "etichette-mono"}
    assert attesi <= ids, f"mancano {sorted(attesi - ids)}; trovati {sorted(ids)}"


def test_regressione():
    pulita, slop = os.environ.get("DSI_PAGINA_PULITA"), os.environ.get("DSI_PAGINA_SLOP")
    if not (pulita and slop and os.path.exists(pulita) and os.path.exists(slop)):
        print("        (saltato: DSI_PAGINA_PULITA o DSI_PAGINA_SLOP non impostate)")
        return
    a = controlla(pulita)
    assert a["punteggio"] == 100, f"pagina pulita: {a['punteggio']} {[s['id'] for s in a['segnali']]}"
    b = controlla(slop)
    assert b["punteggio"] <= 30, f"pagina slop: {b['punteggio']}"


def test_crema_oklch():
    """Crema e terracotta scritti in oklch() si riconoscono."""
    t = open(os.path.join(FIX, "seconda-ondata.html")).read()
    t = t.replace("#F4F1EA", "oklch(0.96 0.012 85)").replace("#D97757", "oklch(0.67 0.13 40)")
    out = cartella()
    p = os.path.join(out, "oklch.html")
    open(p, "w").write(t)
    ids = {x["id"] for x in controlla(p)["segnali"]}
    assert "crema-terracotta" in ids, sorted(ids)


def test_cooccorrenze():
    """Il rapporto conta i segnali per gruppo e dice se insieme fanno un aspetto da IA."""
    d = controlla(os.path.join(FIX, "seconda-ondata.html"))
    g = d["gruppi"]
    assert g["Dettagli"] >= 2 and g["Colore"] >= 1 and g["Tipografia"] >= 1, g
    assert "aspetto_ia" in d


if __name__ == "__main__":
    esegui([test_seconda_ondata, test_regressione, test_crema_oklch, test_cooccorrenze])
