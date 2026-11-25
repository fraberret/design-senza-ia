#!/bin/zsh
# Lancia uno script della skill con un Python che ha Playwright e Pillow.
# Ordine: venv della skill, venv della skill seo, python3 di sistema.
# Uso: scripts/py.sh <script.py> [argomenti]
DIR="${0:A:h}"
for PY in "$DIR/../.venv/bin/python" "$HOME/.claude/skills/seo/.venv/bin/python" "$(command -v python3)"; do
  [[ -x "$PY" ]] || continue
  "$PY" -c "import playwright, PIL" 2>/dev/null || continue
  for B in "$DIR/../.venv/ms-playwright" "$HOME/.claude/skills/seo/ms-playwright" "$HOME/Library/Caches/ms-playwright"; do
    [[ -d "$B" ]] && export PLAYWRIGHT_BROWSERS_PATH="$B" && break
  done
  exec "$PY" "$DIR/$1" "${@:2}"
done
echo "Nessun Python con playwright e pillow. Installazione (chiedere prima all'utente):" >&2
echo "  python3 -m venv $DIR/../.venv && $DIR/../.venv/bin/pip install playwright pillow && PLAYWRIGHT_BROWSERS_PATH=$DIR/../.venv/ms-playwright $DIR/../.venv/bin/python -m playwright install chromium" >&2
exit 1
