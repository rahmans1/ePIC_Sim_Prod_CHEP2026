#!/usr/bin/env bash
set -euo pipefail

mkdir -p exports

marp deck.md --html -o exports/deck.html
perl -pi -e 's#(src|href)="assets/#$1="../assets/#g' exports/deck.html

python3 scripts/embed_html_assets.py exports/deck.html exports/deck_standalone.html

marp deck.md --pdf --html --allow-local-files -o exports/deck.pdf
python3 scripts/pdf_to_pptx.py exports/deck.pdf exports/deck.pptx --title "Scaling ePIC Simulation Production"
