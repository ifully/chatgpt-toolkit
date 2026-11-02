---
name: presentation-design-pro
description: Design professional editable PowerPoint presentations and optional Slidev decks; enforce structure, slide consistency, text fit, typography, and visual inspection. Use for academic, business, conference or visual storytelling slide decks.
---

# Presentation Design Pro

## Visual and editorial contract
- Define audience, narrative objective, aspect ratio, slide count, language, brand tokens and anticipated projection size.
- One clear claim per slide when possible. Distinguish evidence, interpretation and recommendation. Cite verifiable statistics and charts.
- Establish title/body scales, grid, consistent alignment, accessible contrast, clear slide numbering and non-decorative imagery.
- Never synthesize unverifiable statistics or falsely imply graph causality. Ensure Turkish diacritics render correctly.

## Editable PPTX
- Use PptxGenJS for real native text, shapes, charts and tables. Do not make every slide a screenshot.
- Starter: `node tools/create-presentation.mjs` generates `out/sample-presentation.pptx`.
- Always run package integrity checks and render every slide to an image for manual review in PowerPoint/LibreOffice when available.
- Text boxes and rotations need visual checks; OOXML geometry tests alone cannot prove lack of text clipping.

## Slidev alternative
- Slidev is a separate Markdown/Vue presentation path; use `templates/slides.md` with `npx slidev templates/slides.md` once dependencies are installed.
- A Slidev deck is not automatically a native editable PowerPoint file. Choose it for browser-based/interactive decks, not where native PPTX editing is mandatory.

## Final audit
- Check full-size and thumbnail renders, slide boundaries, cropped charts, slide reading order, footnotes, title consistency, and contrast.
- Run `python tools/qa.py`; report visual inspection and app compatibility separately.
- Follow `../design-quality-audit/SKILL.md` before final delivery.
