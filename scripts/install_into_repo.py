#!/usr/bin/env python3
"""Conservatively install the plugin into an existing repository, no destructive edits."""
from __future__ import annotations
import argparse
import json
import shutil
import sys
from pathlib import Path

SRC_ROOT=Path(__file__).resolve().parents[1]
PLUGIN_NAME='design-production'
ENTRY={'name':PLUGIN_NAME,'source':{'source':'local','path':'./plugins/design-production'},'policy':{'installation':'AVAILABLE'},'category':'Creativity'}


def main():
    parser=argparse.ArgumentParser(description='Safely copy Design Production plugin into an existing repo')
    parser.add_argument('repository',type=Path,help='Existing local checkout of the GitHub repository')
    parser.add_argument('--dry-run',action='store_true',help='Print changes without writing them')
    args=parser.parse_args()
    target=args.repository.expanduser().resolve()
    if not target.is_dir():print('ERROR: repository must be an existing directory',file=sys.stderr);return 2
    if target==SRC_ROOT or SRC_ROOT in target.parents:print('ERROR: target must not be inside the unpacked source',file=sys.stderr);return 2
    if not (target/'.git').exists():print('WARN: target has no .git folder; verify this is your intended repo checkout')
    src_plugin=SRC_ROOT/'plugins'/PLUGIN_NAME
    dst_plugin=target/'plugins'/PLUGIN_NAME
    if dst_plugin.exists():
        print(f'ABORT: target already exists: {dst_plugin}\nNo files were changed. Review/merge differences manually.',file=sys.stderr)
        return 3
    msrc=SRC_ROOT/'.agents/plugins/marketplace.json'
    mdst=target/'.agents/plugins/marketplace.json'
    try:
        if mdst.exists():
            market=json.loads(mdst.read_text(encoding='utf-8'))
            if not isinstance(market,dict) or not isinstance(market.get('plugins'),list):
                print('ABORT: existing marketplace JSON lacks a plugins array',file=sys.stderr);return 3
            if any(p.get('name')==PLUGIN_NAME for p in market['plugins']):
                print('ABORT: design-production already registered in marketplace',file=sys.stderr);return 3
        else:market=json.loads(msrc.read_text(encoding='utf-8'))
    except (ValueError,OSError) as exc:print(f'ABORT: cannot safely parse marketplace: {exc}',file=sys.stderr);return 3
    if mdst.exists():market['plugins'].append(ENTRY)
    # No overwrite of repo-level files; skip any existing file.
    optional={
        SRC_ROOT/'.github/workflows/design-production-qa.yml':target/'.github/workflows/design-production-qa.yml',
        SRC_ROOT/'AGENTS.md':target/'AGENTS.md',
        SRC_ROOT/'.gitignore':target/'.gitignore',
    }
    print(('DRY RUN' if args.dry_run else 'INSTALL')+f' into: {target}')
    print('  +',dst_plugin.relative_to(target))
    print('  '+('~' if mdst.exists() else '+'),mdst.relative_to(target),'(preserve existing plugins)')
    for src,dst in optional.items():
        print('  '+('SKIP existing' if dst.exists() else '+'),dst.relative_to(target))
    docs_src=SRC_ROOT/'docs'
    docs_dest=target/'docs/design-production'
    if docs_dest.exists():
        print('  SKIP existing',docs_dest.relative_to(target))
    else:print('  +',docs_dest.relative_to(target))
    if args.dry_run:
        print('Dry-run complete: no files changed.');return 0
    try:
        shutil.copytree(src_plugin,dst_plugin)
        mdst.parent.mkdir(parents=True,exist_ok=True)
        mdst.write_text(json.dumps(market,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
        for src,dst in optional.items():
            if not dst.exists():dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dst)
        if not docs_dest.exists():shutil.copytree(docs_src,docs_dest)
    except (OSError,shutil.Error) as exc:
        print('ERROR: copy failed; changes may be partial and should be reviewed:',exc,file=sys.stderr)
        return 1
    if (target/'AGENTS.md').exists() and (target/'AGENTS.md').read_bytes()!=(SRC_ROOT/'AGENTS.md').read_bytes():
        print('NOTICE: existing AGENTS.md preserved. Merge the skill routing instructions manually.')
    print('Installed. Review changes with `git status` before committing.')
    return 0

if __name__=='__main__':sys.exit(main())
