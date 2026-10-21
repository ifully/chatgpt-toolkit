#!/usr/bin/env python3
"""Validate the local JSON prompt catalog without network access."""
from pathlib import Path
import json,sys
p=Path(__file__).resolve().parent.parent/'prompts.json'
d=json.loads(p.read_text(encoding='utf-8')); assert isinstance(d['prompts'],list)
ids=[]
for i,e in enumerate(d['prompts']):
 for key in ['id','category','title_tr','required_inputs','prompt_tr','expected_outputs','quality_checks','origin']:
  assert key in e and e[key], f'Entry {i} missing {key}'
 assert e['origin']=='original-adaptation'
 assert e['id'].startswith(('AWL-','AWR-','AWW-','AWQ-','AWP-'))
 assert 'DOĞRULANMADI' in e['prompt_tr']
 ids.append(e['id'])
assert len(set(ids))==len(ids), 'Duplicate IDs'
print(f'PASS: {len(ids)} original prompts, no duplicate IDs')
