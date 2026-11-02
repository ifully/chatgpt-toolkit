#!/usr/bin/env python3
"""Repository architecture validation, independent of npm and network."""
from pathlib import Path
import json
import re
import sys
from xml.etree import ElementTree as ET

HERE = Path(__file__).resolve()
ROOT = HERE.parents[3] if HERE.parent.name == 'tools' else HERE.parents[1]
PLUGIN = ROOT / 'plugins' / 'design-production'
SKILLS = ('vector-design-pro','presentation-design-pro','newsletter-design-pro','design-quality-audit')

def main():
    errors=[]
    def get_json(p):
        try:return json.loads(p.read_text(encoding='utf-8'))
        except (OSError, ValueError) as exc:
            errors.append(f'{p.relative_to(ROOT)}: {exc}')
            return None
    manifest=get_json(PLUGIN/'.codex-plugin/plugin.json')
    marketplace=get_json(ROOT/'.agents/plugins/marketplace.json')
    package=get_json(PLUGIN/'package.json')
    get_json(PLUGIN/'config/design-tokens.json')
    provenance=ROOT/'docs/source-manifest.json'
    if not provenance.exists(): provenance=ROOT/'docs/design-production/source-manifest.json'
    if provenance.exists(): get_json(provenance)
    if manifest:
        if manifest.get('name')!='design-production':errors.append('plugin manifest name mismatch')
        if manifest.get('skills')!='./skills/':errors.append('plugin skill location mismatch')
    if marketplace:
        entries=[e for e in marketplace.get('plugins',[]) if e.get('name')=='design-production']
        if len(entries)!=1:errors.append(f'expect exactly one marketplace plugin entry, found {len(entries)}')
        elif entries[0].get('source',{}).get('path')!='./plugins/design-production':errors.append('marketplace path mismatch')
    if package:
        for dep in ('@svgdotjs/svg.js','paper','pptxgenjs','mjml','@slidev/cli'):
            if dep not in package.get('dependencies',{}):errors.append('missing dependency '+dep)
    for name in SKILLS:
        p=PLUGIN/'skills'/name/'SKILL.md'
        if not p.exists():errors.append('missing skill '+name);continue
        s=p.read_text(encoding='utf-8')
        if not re.search(r'^---\s*\nname:\s*'+re.escape(name)+r'\s*\n',s): errors.append(f'{name}: invalid frontmatter name')
        if not re.search(r'^description:\s*\S',s,re.M):errors.append(f'{name}: missing description')
        if 'design-quality-audit' not in s and name!='design-quality-audit': errors.append(f'{name}: QA linkage missing')
    for filename in ['tools/create-vector.mjs','tools/create-presentation.mjs','tools/render-newsletter.mjs','tools/qa.py','templates/newsletter.mjml','templates/vector-base.svg','templates/slides.md']:
        if not (PLUGIN/filename).is_file():errors.append('missing '+filename)
    if not errors:
        try:ET.parse(PLUGIN/'templates/vector-base.svg')
        except ET.ParseError as exc:errors.append('invalid SVG template: '+str(exc))
    print(f'Repository validation: {"PASS" if not errors else "FAIL"}. Skills: {len(SKILLS)}; errors: {len(errors)}')
    for error in errors:print('ERROR',error)
    return 1 if errors else 0

if __name__=='__main__':sys.exit(main())
