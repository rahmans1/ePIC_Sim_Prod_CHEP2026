# Scaling ePIC Simulation Production Slide Workflow

This directory contains the editable Marp source for the CHEP 2026 slide deck, the image assets used by the deck, helper scripts, prompts for AI-assisted editing, and generated exports.

## Directory Layout

- `deck.md`: source of truth for the slides. Edit this file first.
- `assets/`: all image assets used by the deck. Keep every deck image in this single folder.
- `scripts/`: helper scripts for generating plots and packaging outputs.
- `prompts/`: reusable prompts for AI-assisted deck revisions.
- `sources/`: original/reference input files, including the source PowerPoint.
- `exports/`: generated outputs such as PDF, PowerPoint, HTML, and standalone HTML.
- `MARP_WORKFLOW.md`: short legacy workflow note; this README is the detailed workflow.

## Prerequisites

Install Marp CLI:

```bash
npm install -g @marp-team/marp-cli
```

For PDF export, Marp needs a local browser engine. Install Chrome, Chromium, Edge, or Firefox. If Marp cannot find the browser automatically, set `CHROME_PATH`:

```bash
CHROME_PATH=/path/to/chrome scripts/build_deck.sh
```

The plotting helper needs Python packages:

```bash
python3 -m pip install matplotlib numpy
```

The PDF-to-PowerPoint helper needs Poppler's `pdftoppm` command:

```bash
sudo apt install poppler-utils
```

## Editing The Deck

1. Open `deck.md`.
2. Edit slide text, layout HTML, or references to files in `assets/`.
3. Keep `deck.md` as the source of truth. Do not manually edit generated files in `exports/`.
4. Keep image references relative to the project root, for example:

```html
<img src="assets/detector.jpg" alt="ePIC detector rendering">
```

5. Keep slide layouts simple when PowerPoint or Google Slides editing is required. Prefer editable Markdown/HTML text over screenshots of text.

## Adding Or Updating Image Assets

1. Put the image file directly in `assets/`.
2. Use concise lowercase names when adding new files, for example `workflow_diagram.png`.
3. Reference it from `deck.md` as `assets/workflow_diagram.png`.
4. Avoid adding nested folders under `assets/`; the directory is intentionally flat.
5. If an image comes from the original PowerPoint, keep the original PowerPoint in `sources/` and store the extracted image in `assets/`.

## Regenerating The Computing Usage Plot

The plot data and styling live in `scripts/plot_computing_usage.py`.

To regenerate the default plot:

```bash
python3 scripts/plot_computing_usage.py
```

This writes:

```text
assets/computing_usage.png
```

To generate a different file or DPI:

```bash
python3 scripts/plot_computing_usage.py --output assets/computing_usage_highres.png --dpi 300
```

After regenerating a plot, verify that `deck.md` points at the intended asset.

## Exporting Slides

Create the output directory if needed:

```bash
mkdir -p exports
```

Export PDF and derive PowerPoint from that PDF:

```bash
CHROME_PATH=/usr/bin/chromium-browser scripts/build_deck.sh
```

The build intentionally does not use Marp's direct PPTX export. Marp renders `exports/deck.pdf` with HTML enabled, then `scripts/pdf_to_pptx.py` converts each PDF page into a full-slide image in `exports/deck.pptx`.

Export to browser-based HTML:

```bash
marp deck.md --html -o exports/deck.html
perl -pi -e 's#(src|href)="assets/#$1="../assets/#g' exports/deck.html
```

The path rewrite is needed because `deck.md` is rendered from the project root, while `exports/deck.html` is opened from the `exports/` directory.

Export HTML, standalone HTML, PDF, and PDF-derived PowerPoint together:

```bash
CHROME_PATH=/usr/bin/chromium-browser scripts/build_deck.sh
```

If your browser is not installed at `/usr/bin/chromium-browser`, use the correct path or omit `CHROME_PATH` if Marp finds the browser automatically. Generated files should stay in `exports/`.

## Creating A Single-File HTML Deck

The normal HTML export references files in `assets/`. To create one self-contained HTML file with image data embedded:

```bash
python3 scripts/embed_html_assets.py exports/deck.html exports/deck_standalone.html
```

Use `exports/deck_standalone.html` when you need to send one file that contains the deck and image assets. External hyperlinks inside the deck remain normal hyperlinks.

## Importing Into Google Slides

1. Export PDF and the PDF-derived PowerPoint with:

```bash
CHROME_PATH=/usr/bin/chromium-browser scripts/build_deck.sh
```

2. Open Google Slides.
3. Choose `File -> Import slides`.
4. Upload `exports/deck.pptx`.
5. Select the slides to import.
6. Review the imported deck visually. The PowerPoint is image-based, so edits should happen in `deck.md` and then be regenerated.

## AI-Assisted Revisions

Use `prompts/deck-generation.md` when asking an AI assistant to revise the deck. The key rules are:

- Edit `deck.md`, not generated exports.
- Use `assets/` for all figures and screenshots.
- Preserve factual uncertainty by marking items as `[VERIFY]`.
- Keep the deck exportable with Marp.

## Recommended Full Workflow

1. Edit `deck.md`.
2. Add or update images in `assets/`.
3. Regenerate plots if needed:

```bash
python3 scripts/plot_computing_usage.py
```

4. Export HTML for quick review:

```bash
marp deck.md --html -o exports/deck.html
perl -pi -e 's#(src|href)="assets/#$1="../assets/#g' exports/deck.html
```

5. Open `exports/deck.html` in a browser and review every slide.
6. Export PDF and PowerPoint:

```bash
CHROME_PATH=/usr/bin/chromium-browser scripts/build_deck.sh
```

7. If needed, create the single-file HTML:

```bash
python3 scripts/embed_html_assets.py exports/deck.html exports/deck_standalone.html
```

8. Import `exports/deck.pptx` into Google Slides only after reviewing `exports/deck.pdf`.

## Troubleshooting

- `No suitable browser found`: install Chrome, Chromium, Edge, or Firefox, or set `CHROME_PATH`.
- Broken images in HTML: confirm the file exists directly in `assets/` and the `deck.md` path starts with `assets/`.
- Standalone HTML still has missing images: regenerate `exports/deck.html`, then rerun `scripts/embed_html_assets.py`.
- Broken or fuzzy PowerPoint slides: inspect `exports/deck.pdf` first. If the PDF is correct, increase the DPI in `scripts/build_deck.sh` for `scripts/pdf_to_pptx.py`.
- Plot script import errors: install dependencies with `python3 -m pip install matplotlib numpy`.

## Cleanup Rules

- Keep source files at the top level only when they are actively edited, such as `deck.md` and `README.md`.
- Keep all generated deck outputs in `exports/`.
- Keep all deck images in `assets/`.
- Keep original reference files in `sources/`.
- Do not edit generated files in `exports/` by hand; regenerate them from `deck.md`.
