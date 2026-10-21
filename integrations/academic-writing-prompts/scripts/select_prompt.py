#!/usr/bin/env python3
"""Stdlib-only helper: list or display academic prompt text; no network or API calls."""
from pathlib import Path
import argparse,json
p=argparse.ArgumentParser(description='Select an academic writing prompt from the catalog')
p.add_argument('--id',help='Prompt ID such as AWL-03 or AWQ-01')
p.add_argument('--list',action='store_true',help='Show known IDs')
a=p.parse_args()
data=json.loads((Path(__file__).resolve().parent.parent/'prompts.json').read_text(encoding='utf-8'))
entries=data['prompts']
if a.list or not a.id:
 for x in entries: print(x['id'],x['title_tr'],sep=' | ')
else:
 match=next((x for x in entries if x['id']==a.id),None)
 if match is None: p.error('Unknown ID: '+a.id)
 print(match['prompt_tr'])
