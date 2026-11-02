---
name: design-quality-audit
description: Independent quality review of vector SVG, editable PowerPoint, MJML/HTML newsletter and Slidev design deliverables; verify structure, usability, accessibility and truthful release claims. Use before releasing or uploading any design artifact.
---

# Design Quality Audit

## Gate A — structural
1. Verify filename, source deliverable, required size, correct Turkish characters, branding, approved content and all mandatory attachments.
2. Run `python tools/qa.py` in the plugin root and `python scripts/validate_repository.py` at the repository root.
3. Investigate errors; never suppress them merely to obtain a green status.

## Gate B — technical
- SVG: real vector primitives, coherent `viewBox`, no external scripts, no external raster references, font/embed policy, clean rendering.
- PPTX: valid OOXML package, consistent ratio, editable elements where required, no obvious out-of-slide coordinates, no orphaned media relationships, visual review for text clipping.
- Email: MJML compilation, valid HTML output, image alternatives, hyperlinks, unsubscribe destination, no placeholder content, mobile and major-client test evidence.
- Slidev: Markdown/Vue compilation, PDF export when requested, browser presentation checked at the target ratio.

## Gate C — visual / editorial
- Use a checklist for visual hierarchy, rhythm, spacing, typographic detail, semantic color and contrast, grammar, citations, affordance, and consistency with an approved visual system.
- Test screenshots and rendered deliverables at 100%, mobile/thumbnail and realistic projection/reading sizes.
- Accessibility checks include contrast and reading order, but automated tools cannot confirm aesthetic or user-task suitability.

## Handoff record
State: files delivered; source editability; build command; automated checks completed; manual checks completed; assumptions; remaining risks. If client-side rendering, app testing or any check was not performed, label it explicitly 'not verified'. Never describe a file as error-free solely on successful generation.
