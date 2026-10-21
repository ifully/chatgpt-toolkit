"""Search OpenAlex with PyAlex, export metadata to CSV and audit metadata to JSON.

No network activity in --dry-run mode. Requires OPENALEX_API_KEY for live use.
"""
from __future__ import annotations
import argparse
import csv
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

FIELDS = [
    "openalex_id", "doi", "title", "year", "publication_date", "authors",
    "venue", "cited_by_count", "open_access", "abstract", "search_query",
]


def parser():
    p = argparse.ArgumentParser(description="PyAlex bibliographic search with audit logging")
    p.add_argument("--query", required=True, help="Literal OpenAlex search text")
    p.add_argument("--from-year", type=int, default=2020)
    p.add_argument("--to-year", type=int, default=datetime.now(timezone.utc).year)
    p.add_argument("--max-records", type=int, default=50)
    p.add_argument("--per-page", type=int, default=50)
    p.add_argument("--output", default="openalex_results.csv")
    p.add_argument("--dry-run", action="store_true", help="Only validate and print plan; no network")
    return p


def validate(args):
    if not args.query.strip():
        raise ValueError("--query must not be empty")
    if not (1900 <= args.from_year <= args.to_year <= 2200):
        raise ValueError("year range is invalid")
    if not (1 <= args.per_page <= 200):
        raise ValueError("--per-page must be 1..200")
    if not (1 <= args.max_records <= 500):
        raise ValueError("--max-records must be 1..500")


def normalize(work, query):
    authors = "; ".join(
        x.get("author", {}).get("display_name", "")
        for x in (work.get("authorships") or [])
        if isinstance(x, dict)
    )
    place = work.get("primary_location") or {}
    source = place.get("source") or {}
    oa = work.get("open_access") or {}
    return {
        "openalex_id": work.get("id", ""),
        "doi": work.get("doi") or "",
        "title": work.get("title") or "",
        "year": work.get("publication_year") or "",
        "publication_date": work.get("publication_date") or "",
        "authors": authors,
        "venue": source.get("display_name") or "",
        "cited_by_count": work.get("cited_by_count") or 0,
        "open_access": oa.get("is_oa", ""),
        "abstract": work.get("abstract") or "",
        "search_query": query,
    }


def main(argv=None):
    args = parser().parse_args(argv)
    try:
        validate(args)
    except ValueError as exc:
        parser().error(str(exc))
    plan = {
        "query": args.query.strip(),
        "from_year": args.from_year,
        "to_year": args.to_year,
        "max_records": args.max_records,
        "per_page": args.per_page,
        "output": args.output,
        "method": "OpenAlex Works().search + date filters, PyAlex paginate",
    }
    if args.dry_run:
        print(json.dumps({"dry_run": True, "plan": plan}, indent=2, ensure_ascii=False))
        return 0
    key = os.environ.get("OPENALEX_API_KEY")
    if not key:
        print("Missing OPENALEX_API_KEY: configure a private environment variable (do not commit it).", file=sys.stderr)
        return 2
    try:
        import pyalex
        from pyalex import Works
    except ImportError:
        print("PyAlex is not installed. In a trusted environment: python -m pip install pyalex", file=sys.stderr)
        return 3
    pyalex.config.api_key = key
    builder = (Works().search(args.query.strip()).filter(
        from_publication_date=f"{args.from_year}-01-01",
        to_publication_date=f"{args.to_year}-12-31",
    ))
    # The output is exploratory bibliographic metadata, not a validated citation list.
    rows = []
    try:
        for page in builder.paginate(per_page=args.per_page, n_max=args.max_records):
            for work in page:
                if len(rows) >= args.max_records:
                    break
                rows.append(normalize(work, args.query.strip()))
            if len(rows) >= args.max_records:
                break
    except Exception as exc:
        print(f"OpenAlex request failed ({type(exc).__name__}): {exc}", file=sys.stderr)
        return 4
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)
    audit = {
        **plan,
        "retrieved_at_utc": datetime.now(timezone.utc).isoformat(),
        "record_count": len(rows),
        "pyalex_version": getattr(pyalex, "__version__", "unknown"),
        "notes": "Metadata are not verified primary sources. Check DOI, publisher, journal and relevance separately.",
    }
    out.with_suffix(out.suffix + ".audit.json").write_text(
        json.dumps(audit, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"Saved {len(rows)} records to {out} and audit metadata beside it.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
