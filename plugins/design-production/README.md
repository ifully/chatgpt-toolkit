# Design Production — Codex Plugin

Four locally-authored agent skills and production templates. This is a **custom integration**, not a copy of or an official distribution from OpenAI, SVG.js, Paper.js, PptxGenJS, MJML or Slidev.

## Skills
- `vector-design-pro`: true vectors, typographic/artboard discipline, SVG audit.
- `presentation-design-pro`: editable PowerPoint, Slidev as an optional web deck path.
- `newsletter-design-pro`: MJML HTML email, client tests and unsubscribe compliance.
- `design-quality-audit`: static QA plus required manual visual verification.

## Windows or macOS/Linux setup
```bash
cd plugins/design-production
npm install
npm run demo
```
Outputs are written to ignored `out/` directory. Build steps can be run individually:
```bash
npm run build:vector
npm run build:pptx
npm run build:email
npm run qa
```

**Important:** `npm install` downloads third-party dependencies; their GitHub ZIP snapshots are **not** embedded. Package versions reflect the uploaded archives and are not a guarantee of npm registry availability. Node >=22.12 is needed for the selected Slidev version. If upstream registry versions changed, review and update the manifest and lockfile in a controlled commit.

The sample includes placeholders, example copy, and nonproduction URLs. It is a *starter*, not ready-to-send branded content. The QA command cannot replace visual review or actual Gmail/Outlook/Apple Mail previews.
