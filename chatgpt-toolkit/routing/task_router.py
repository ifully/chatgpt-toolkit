#!/usr/bin/env python3
"""Yerel araç kataloğundan güvenli, deterministik görev yönlendirmesi.

Yalnızca Python standart kütüphanesini kullanır. Haricî komut çalıştırmaz,
paket kurmaz, ağ isteği yapmaz veya seçilen depoların kodlarını yürütmez.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path
import re
import shutil
import sys
import unicodedata


ROOT = Path(__file__).resolve().parent.parent
CATALOG = ROOT / "tools.json"
RULES = ROOT / "routing" / "rules.json"
TURKISH = str.maketrans({"ı": "i", "İ": "i", "ğ": "g", "Ğ": "g", "ü": "u", "Ü": "u", "ş": "s", "Ş": "s", "ö": "o", "Ö": "o", "ç": "c", "Ç": "c"})

# İzinli ve denetlenebilir *pasif* yoklamalar: kurulum/çalıştırma yapmaz.
PYTHON_IMPORTS = {
    "AutoResearch/autora": "autora",
    "angr/angr": "angr",
    "docling-project/docling": "docling",
    "pandas-dev/pandas": "pandas",
    "pola-rs/polars": "polars",
    "duckdb/duckdb": "duckdb",
    "scipy/scipy": "scipy",
    "plotly/plotly.py": "plotly",
    "psychopy/psychopy": "psychopy",
    "treeverse/dvc": "dvc",
    "snakemake/snakemake": "snakemake",
    "PaddlePaddle/PaddleOCR": "paddleocr",
    "scikit-learn/scikit-learn": "sklearn",
}
CLI_BINARIES = {
    "NationalSecurityAgency/ghidra": "ghidraRun",
    "rizinorg/rizin": "rizin",
    "quarto-dev/quarto-cli": "quarto",
    "jgm/pandoc": "pandoc",
    "typst/typst": "typst",
    "colmap/colmap": "colmap",
    "blender/blender": "blender",
    "visioncortex/vtracer": "vtracer",
    "fonttools/fontbakery": "fontbakery",
    "GoogleChrome/lighthouse": "lighthouse",
    "semgrep/semgrep": "semgrep",
    "gitleaks/gitleaks": "gitleaks",
    "aquasecurity/trivy": "trivy",
    "PyCQA/bandit": "bandit",
    "openai/evals": "oaieval",
    "promptfoo/promptfoo": "promptfoo",
}


def normalize(text: str) -> str:
    """Türkçe harfleri ASCII'ye eşleyip harf/rakam dizilerine indirger."""
    folded = text.translate(TURKISH).casefold()
    ascii_text = unicodedata.normalize("NFKD", folded)
    ascii_text = "".join(c for c in ascii_text if not unicodedata.combining(c))
    return " ".join(re.findall(r"[a-z0-9]+", ascii_text))


def trigger_matches(query_tokens: list[str], trigger: str) -> bool:
    """Kelime başlangıcı ve ardışık kelime eşleşmesi; keyfî alt dize değil."""
    parts = normalize(trigger).split()
    if not parts or len(parts) > len(query_tokens):
        return False
    for start in range(len(query_tokens) - len(parts) + 1):
        if all(query_tokens[start + offset].startswith(part) for offset, part in enumerate(parts)):
            return True
    return False


def load_data() -> tuple[dict, list[dict]]:
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    rules_data = json.loads(RULES.read_text(encoding="utf-8"))
    tools = catalog.get("tools", [])
    rules = rules_data.get("rules", [])
    repos = {tool["repo"] for tool in tools}
    if len(repos) != len(tools):
        raise ValueError("Araç kataloğunda yinelenen repo var.")
    if len({rule["id"] for rule in rules}) != len(rules):
        raise ValueError("Yönlendirme kurallarında yinelenen ID var.")
    for rule in rules:
        missing = set(rule["repos"]) - repos
        if missing:
            raise ValueError(f"{rule['id']}: katalogda bulunmayan repo: {sorted(missing)}")
        if not rule.get("triggers") or not rule.get("validation"):
            raise ValueError(f"{rule['id']}: tetikleyici veya doğrulama ölçütü eksik.")
    return catalog, rules


def passive_probe(tool: dict) -> dict:
    """Salt-okuma görünürlük kontrolü; kurulumu veya çalışmayı kanıtlamaz."""
    repo = tool["repo"]
    if repo in PYTHON_IMPORTS:
        module = PYTHON_IMPORTS[repo]
        try:
            found = importlib.util.find_spec(module) is not None
        except (ImportError, ValueError, AttributeError):
            found = False
        return {
            "type": "python-module-discovery",
            "target": module,
            "status": "visible-in-current-python" if found else "not-found-in-current-python",
            "limitation": "Import/çalıştırma, bağımlılıklar, sürüm ve yetki doğrulanmadı.",
        }
    if repo in CLI_BINARIES:
        binary = CLI_BINARIES[repo]
        found = shutil.which(binary) is not None
        return {
            "type": "executable-path-discovery",
            "target": binary,
            "status": "visible-on-path" if found else "not-found-on-path",
            "limitation": "Komut çalıştırılmadı; işlev ve sürüm doğrulanmadı.",
        }
    return {
        "type": "not-checked",
        "status": "unknown",
        "limitation": "Salt-okuma güvenilir bir yoklama tanımlı değil; kurulu/bağlı varsayılmaz.",
    }


def route(query: str, *, limit: int = 6, max_rules: int = 3, probe: bool = False) -> dict:
    catalog, rules = load_data()
    words = normalize(query).split()
    scored = []
    for rule in rules:
        matched = [trigger for trigger in rule["triggers"] if trigger_matches(words, trigger)]
        if not matched:
            continue
        primary = max(2 * len(normalize(t).split()) + len(normalize(t)) / 50 for t in matched)
        score = round(primary + 0.25 * (len(matched) - 1), 3)
        scored.append((score, rule, matched))
    scored.sort(key=lambda item: (-item[0], item[1]["id"]))
    choices = scored[:max_rules]
    by_repo = {tool["repo"]: tool for tool in catalog["tools"]}

    # Birden çok niyet varsa ilk kural tüm kontenjanı doldurmasın.
    max_depth = max((len(rule["repos"]) for _, rule, _ in choices), default=0)
    selected = []
    seen = set()
    for depth in range(max_depth):
        for score, rule, _ in choices:
            if len(selected) >= limit:
                break
            if depth >= len(rule["repos"]):
                continue
            repo = rule["repos"][depth]
            if repo in seen:
                continue
            seen.add(repo)
            tool = by_repo[repo]
            entry = {
                "repo": repo,
                "url": tool["url"],
                "name": tool["name"],
                "execution_mode": tool["execution_mode"],
                "purpose_tr": tool["purpose_tr"],
                "recommended_by": rule["id"],
                "runtime_status": "not-verified",
            }
            if probe:
                entry["environment_probe"] = passive_probe(tool)
            selected.append(entry)
        if len(selected) >= limit:
            break

    matched_rules = [
        {"id": rule["id"], "label_tr": rule["label_tr"], "score": score,
         "matched_triggers": matched}
        for score, rule, matched in choices
    ]
    return {
        "query": query,
        "catalog_total": len(catalog["tools"]),
        "matched_rules": matched_rules,
        "recommendations": selected,
        "validation": list(dict.fromkeys(item for _, rule, _ in choices for item in rule["validation"])),
        "cautions": list(dict.fromkeys(item for _, rule, _ in choices for item in rule["cautions"])),
        "limitations": [
            "Bu sonuç yalnızca katalog bazlı öneridir; depolar yüklenmez veya çalıştırılmaz.",
            "--probe kullanılsa bile görünürlük kontrolü çalışabilirlik, sürüm veya izin doğrulaması değildir.",
            "Bilinmeyen görev ifadelerinde manuel seçim ve kaynak denetimi gerekir.",
        ],
    }


def format_text(result: dict) -> str:
    lines = [f"Görev: {result['query']}", f"Katalog: {result['catalog_total']} kayıt"]
    if not result["matched_rules"]:
        lines.extend(["Eşleşen yönlendirme kuralı bulunamadı.",
                      "Görevi yeniden ifade edin veya tools.json ve categories/ rehberlerini inceleyin."])
        return "\n".join(lines)
    lines.append("Eşleşen alanlar: " + "; ".join(
        item["label_tr"] for item in result["matched_rules"]
    ))
    lines.append("\nÖnerilen kaynaklar (kurulu/etkin oldukları doğrulanmadı):")
    for idx, entry in enumerate(result["recommendations"], 1):
        lines.append(f"{idx}. {entry['repo']} — {entry['execution_mode']}")
        lines.append(f"   {entry['url']}")
        if "environment_probe" in entry:
            p = entry["environment_probe"]
            lines.append(f"   Pasif ortam kontrolü: {p['status']} ({p['type']})")
    lines.append("\nÇıktı doğrulama:")
    lines.extend(f"- {item}" for item in result["validation"])
    lines.append("\nDikkat:")
    lines.extend(f"- {item}" for item in result["cautions"] + result["limitations"])
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query", help="Türkçe/İngilizce görev ifadesi")
    parser.add_argument("--limit", type=int, default=6, help="En fazla kaç repo önerilsin (1-15)")
    parser.add_argument("--max-rules", type=int, default=3, help="En fazla kaç görev alanı (1-5)")
    parser.add_argument("--probe", action="store_true", help="Yalnızca pasif Python/PATH görünürlük kontrolü")
    parser.add_argument("--json", action="store_true", help="Makine tarafından okunabilir JSON çıktısı")
    args = parser.parse_args(argv)
    if not 1 <= args.limit <= 15 or not 1 <= args.max_rules <= 5:
        parser.error("--limit 1-15, --max-rules 1-5 arasında olmalı.")
    try:
        result = route(args.query, limit=args.limit, max_rules=args.max_rules, probe=args.probe)
    except (ValueError, OSError, json.JSONDecodeError, KeyError) as exc:
        print(f"Katalog/yönlendirme hatası: {exc}", file=sys.stderr)
        return 2
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(format_text(result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
