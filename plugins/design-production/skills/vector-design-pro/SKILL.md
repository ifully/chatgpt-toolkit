---
name: vector-design-pro
description: Create professional, editable vector graphics for visual identities, diagrams, social templates, and typographic compositions; validate SVG structure and exports. Use for SVG logos, brand marks, vector illustration, layout systems, and scalable artwork.
---

# Vector Design Pro

## Inputs and decisions
1. Establish purpose, audience, medium, artboard, required copy, brand colors, typography, delivery formats and whether text must remain editable. Do not silently invent brand facts.
2. Build an explicit hierarchy, grid, alignment system, whitespace strategy and contrast checks before styling.
3. Use true vector primitives (`path`, `rect`, `circle`, `text`) and logical groups. Do not wrap a raster image inside SVG and call it vector artwork.
4. Respect copyright and source licenses. Never copy protected logos or fonts into the repo without authorization.

## Implementation
- For browser interactive SVG, use `@svgdotjs/svg.js`; for sophisticated geometry or paths, use `paper` / Paper.js. These are npm dependencies, not copied upstream repositories.
- For deterministic no-dependency export, adapt `tools/create-vector.mjs` and `templates/vector-base.svg`.
- Write a valid SVG with `xmlns`, `viewBox`, meaningful `<title>` and `<desc>`, no embedded base64/raster when a pure vector deliverable is requested.
- Text as editable `<text>` where appropriate; convert typography to outlines only in a separate print-ready variant and with licensing considered. Verify Turkish glyph coverage.
- Check color model before print production; SVG alone is not proof of a CMYK-ready file. EPS export requires a verified converter and visual cross-check, not just renaming a file.

## QA and delivery
1. Run `python tools/qa.py` from `plugins/design-production`.
2. Open/render exported vectors and inspect at 100% and reduced sizes; inspect letterspacing, overlaps and optical balance.
3. Verify all output formats in their target applications (e.g. Illustrator), including font availability.
4. Provide source SVG + optional EPS/PDF where conversion was actually verified, plus a preview image; describe any untested export.
5. Read `../design-quality-audit/SKILL.md` for the independent handoff checklist.
