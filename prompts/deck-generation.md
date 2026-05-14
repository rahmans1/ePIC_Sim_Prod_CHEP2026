# AI Prompt for Updating the MARP Deck

Use `deck.md` as the editable source of truth and use `sources/Scaling ePIC Simulation Production.pptx` only as the reference/base deck.

Goal: produce a CHEP 2026 presentation about scaling ePIC simulation production that can be exported with Marp for presentation and imported into Google Slides as rendered slide images.

Constraints:

- Keep the output in MARP-compatible Markdown.
- Preserve the 8-slide narrative unless asked to expand it.
- Keep slide text concise and presentation-ready.
- Prefer Markdown text in `deck.md` so the source remains editable. The generated PowerPoint is image-based.
- Use files in `assets/` for figures, workflow diagrams, screenshots, maps, and plots.
- Keep layouts simple so PowerPoint and Google Slides import remains usable.
- Avoid complex CSS, absolute positioning, and deeply nested HTML.
- Use ASCII characters unless a scientific symbol is required.
- Do not invent results, resource totals, dates, or infrastructure status. Mark uncertain updates as `[VERIFY]`.

Recommended structure:

1. Title
2. ePIC and EIC context
3. Simulation production resource evolution
4. PanDA WMS / iDDS transition
5. Rucio data management
6. Physics Configuration System
7. Simulation payload optimizations
8. Summary

Editing instruction:

When revising, return the complete updated `deck.md` or a clear patch. Keep the deck exportable with:

```bash
CHROME_PATH=/usr/bin/chromium-browser scripts/build_deck.sh
```
