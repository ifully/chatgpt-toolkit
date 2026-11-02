#!/usr/bin/env python3
"""Conservative static QA: catches obvious faults but not full visual/client bugs."""
from __future__ import annotations
import argparse
import re
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT/'out'
SVG_NS = '{http://www.w3.org/2000/svg}'
A_NS = '{http://schemas.openxmlformats.org/drawingml/2006/main}'
P_NS = '{http://schemas.openxmlformats.org/presentationml/2006/main}'


def svg_check(file: Path):
    errs,warns=[],[]
    try:
        doc=ET.parse(file).getroot()
        if doc.tag!=SVG_NS+'svg':errs.append('not SVG root')
        if not doc.attrib.get('viewBox'):errs.append('missing viewBox')
        if not any(x.tag in {SVG_NS+'path',SVG_NS+'rect',SVG_NS+'circle',SVG_NS+'polygon',SVG_NS+'line',SVG_NS+'ellipse'} for x in doc.iter()):
            errs.append('no true vector shape primitives')
        ids=[x.attrib['id'] for x in doc.iter() if 'id' in x.attrib]
        if len(ids)!=len(set(ids)): errs.append('duplicate SVG ids')
        for x in doc.iter():
            local=x.tag.split('}')[-1]
            if local in ('image','foreignObject'):warns.append(f'<{local}> may embed raster/nonvector content')
            if local=='script':errs.append('script in SVG')
            for attr,val in x.attrib.items():
                if attr.lower().endswith('href') and re.match(r'(https?:|data:)',val,re.I):
                    errs.append('external or embedded content reference')
    except (OSError, ET.ParseError) as e:errs.append(f'SVG parsing failed: {e}')
    return errs,warns


def pptx_check(file: Path):
    errs,warns=[],[]
    try:
        with zipfile.ZipFile(file) as z:
            bad=z.testzip()
            if bad: errs.append('invalid ZIP member: '+bad)
            if '[Content_Types].xml' not in z.namelist():errs.append('missing OOXML content types')
            pres=ET.fromstring(z.read('ppt/presentation.xml'))
            sz=pres.find(P_NS+'sldSz')
            if sz is None:errs.append('missing slide dimensions')
            else:
                w,h=int(sz.attrib['cx']),int(sz.attrib['cy'])
                if min(w,h)<=0:errs.append('nonpositive presentation dimensions')
            slides=sorted([n for n in z.namelist() if re.fullmatch(r'ppt/slides/slide\d+\.xml',n)])
            if not slides:errs.append('presentation has no slides')
            for name in slides:
                doc=ET.fromstring(z.read(name))
                for xf in doc.iter(A_NS+'xfrm'):
                    off=xf.find(A_NS+'off'); ext=xf.find(A_NS+'ext')
                    if off is None or ext is None or sz is None:continue
                    x,y=int(off.attrib['x']),int(off.attrib['y'])
                    dx,dy=int(ext.attrib['cx']),int(ext.attrib['cy'])
                    if min(dx,dy)<0:errs.append(f'{name}: negative shape extent')
                    if x<0 or y<0 or x+dx>w+2000 or y+dy>h+2000:
                        warns.append(f'{name}: drawing extends beyond slide bounds (review intentional bleed)')
    except (OSError,ET.ParseError,KeyError,zipfile.BadZipFile,ValueError) as e:
        errs.append(f'PPTX parsing failed: {e}')
    warns.append('PowerPoint rendering, fonts and text clipping require manual visual review')
    return errs,sorted(set(warns))


def mjml_check(file: Path):
    errs,warns=[],[]
    try:
        doc=ET.parse(file).getroot()
        if doc.tag!='mjml':errs.append('missing mjml root')
        if not list(doc.iter('mj-body')):errs.append('missing mj-body')
        for x in doc.iter('mj-body'):
            for x in x.iter():
                if x.tag=='mj-image' and not x.get('alt'):errs.append('mj-image lacks alt')
                if x.tag=='mj-button' and not x.get('href'):warns.append('mj-button has no target')
                if x.tag=='mj-button' and x.get('href','').startswith('http://'):warns.append('insecure CTA link')
        blob=file.read_text(encoding='utf8').lower()
        if 'unsubscribe' not in blob and 'abonelikten ayrıl' not in blob:
            warns.append('unsubscribe handling not found')
        if 'example.org' in blob or '{{' in blob:
            warns.append('template contains placeholders; not ready to send')
    except (OSError,ET.ParseError) as e:errs.append(f'MJML parsing failed: {e}')
    return errs,warns


def html_check(file: Path):
    errs,warns=[],[]
    data=file.read_text(encoding='utf8')
    for tag in re.findall(r'<img\b[^>]*>',data,re.I|re.S):
        if not re.search(r'\balt\s*=',tag,re.I):errs.append('HTML <img> missing alt')
    if re.search(r'href\s*=\s*["\']\s*["\']',data,re.I):errs.append('empty anchor target')
    if 'example.org' in data:warns.append('placeholder URLs remain in HTML')
    if 'abonelikten ayrıl' not in data.lower() and 'unsubscribe' not in data.lower():warns.append('no obvious unsubscribe text')
    return errs,warns


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--strict',action='store_true',help='Fail on warnings (demo placeholders trigger failure)');args=ap.parse_args()
    targets=[('SVG template',ROOT/'templates/vector-base.svg',svg_check),('MJML template',ROOT/'templates/newsletter.mjml',mjml_check)]
    for file,fn in [(OUT/'sample-vector.svg',svg_check),(OUT/'sample-presentation.pptx',pptx_check),(OUT/'newsletter.html',html_check)]:
        if file.exists():targets.append((file.name,file,fn))
    errors=warnings=0
    for name,p,fn in targets:
        ee,ww=fn(p);errors+=len(ee);warnings+=len(ww)
        print(f'[{"FAIL" if ee else "OK"}] {name}: {p.relative_to(ROOT)}')
        for v in ee:print('  ERROR:',v)
        for v in ww:print('  WARN:',v)
    print(f'QA summary: {errors} errors / {warnings} warnings. Static checks do not establish visual quality or email-client compatibility.')
    return 1 if errors or (args.strict and warnings) else 0
if __name__=='__main__':sys.exit(main())
