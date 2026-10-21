#!/usr/bin/env python3
"""Search local, curated prompts. Standard library only; no network or remote code."""
import argparse
import json
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description="Search academic/dev prompts from prompts.json")
    parser.add_argument("query", nargs="?", default="", help="Text in ID/title/purpose/category")
    parser.add_argument("--id", help="Show full prompt by ID")
    args = parser.parse_args()
    data = json.loads((Path(__file__).parent / "prompts.json").read_text(encoding="utf-8"))
    prompts = data['prompts']
    if args.id:
        matches = [p for p in prompts if p['id'].lower() == args.id.lower()]
        if not matches:
            parser.error(f"Unknown prompt ID: {args.id}")
        print(json.dumps(matches[0], ensure_ascii=False, indent=2))
        return
    needle = args.query.casefold()
    matches = [p for p in prompts if needle in ' '.join([p['id'],p['title'],p['purpose'],p['category']]).casefold()]
    for p in matches:
        print(f"{p['id']}  {p['title']}  [{p['category']}]")
    print(f"{len(matches)} match(es)")

if __name__ == '__main__':
    main()
