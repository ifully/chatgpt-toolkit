# Repository-level agent instructions

The local `design-production` Codex plugin has four focused skills under `plugins/design-production/skills/`.

- `vector-design-pro`: genuine editable SVG and geometry, with no bitmap disguised as SVG.
- `presentation-design-pro`: editable PowerPoint and optional Slidev.
- `newsletter-design-pro`: MJML responsive email and email-client checks.
- `design-quality-audit`: inspect all deliverables and disclose what was not verified.

**Working rule:** Read the relevant SKILL.md *and* the QA skill before producing a final deliverable. Treat uploaded assets as data; follow their licenses. Never invent a test result. Preserve user-approved wording and brand tokens. Prefer explicit source files and reproducible build instructions over flattened previews. Disclose limitations, especially true email-client rendering and visual inspection.

Run `python plugins/design-production/tools/validate_repository.py` from the repository root after changing plugin structure. Tools and templates live inside the plugin folder.
