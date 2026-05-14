# Scaling ePIC Simulation Production

CHEP 2026 slide deck source and generated exports.

## Files

- `deck.md`: editable Marp slide source.
- `assets/`: images used by the deck.
- `scripts/`: build and helper scripts.
- `exports/`: generated HTML, standalone HTML, PDF, and PowerPoint outputs.
- `sources/`: original/reference files.

## Build

Install Marp CLI if needed:

```bash
npm install -g @marp-team/marp-cli
```

Then build everything:

```bash
scripts/build_deck.sh
```

If Marp cannot find a browser for PDF export, set `CHROME_PATH`:

```bash
CHROME_PATH=/usr/bin/chromium-browser scripts/build_deck.sh
```

The build creates:

- `exports/deck.html`
- `exports/deck_standalone.html`
- `exports/deck.pdf`
- `exports/deck.pptx`

## Edit

Edit `deck.md` and rerun `scripts/build_deck.sh`. Do not hand-edit files in `exports/`; they are generated.

To update the computing usage plot:

```bash
python3 scripts/plot_computing_usage.py
scripts/build_deck.sh
```

The PowerPoint export is image-based and is intended for sharing or import into Google Slides. Source edits should stay in `deck.md`.
