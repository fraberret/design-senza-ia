"""Aiuti per i test: lancia gli script della skill con lo stesso Python."""
import os
import subprocess
import sys
import tempfile

QUI = os.path.dirname(os.path.abspath(__file__))
SCRIPTS = os.path.dirname(QUI)
FIX = os.path.join(QUI, "fixtures")


def lancia(script, *argomenti, timeout=240):
    r = subprocess.run([sys.executable, os.path.join(SCRIPTS, script), *argomenti],
                       capture_output=True, text=True, timeout=timeout)
    return r


def cartella():
    return tempfile.mkdtemp(prefix="dsi-test-")


def esegui(test):
    """Esegue le funzioni test_* passate, stampa l'esito, esce con 1 se una fallisce."""
    falliti = 0
    for t in test:
        try:
            t()
            print(f"ok      {t.__name__}")
        except Exception as e:  # noqa: BLE001
            falliti += 1
            print(f"FALLITO {t.__name__}: {type(e).__name__}: {e}")
    print(f"{len(test) - falliti}/{len(test)} superati")
    sys.exit(1 if falliti else 0)
