#!/usr/bin/env python3
"""Verify the company repository is internally consistent.

Checks, all against files in this checkout:

1. Every relative Markdown link and image target resolves to a real file.
2. Every product named in the README portfolio table also appears in
   docs/PORTFOLIO_REGISTER.md, and the register introduces no product the
   README omits.
3. No Markdown file links to a path outside the repository root.

Exit code 1 on any failure. Run from the repository root.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

LINK_RE = re.compile(r"!?\[([^\]]*)\]\(([^)\s]+)\)")
TABLE_ROW_RE = re.compile(r"^\|\s*\[?([^|\]]+?)\]?(?:\([^)]*\))?\s*\|", re.MULTILINE)

IGNORED_SCHEMES = ("http://", "https://", "mailto:", "#")
PRODUCT_TABLE_HEADER = "| Product |"


def markdown_files() -> list[Path]:
    return sorted(p for p in ROOT.rglob("*.md") if ".git" not in p.parts)


def check_links() -> list[str]:
    problems: list[str] = []
    for path in markdown_files():
        text = path.read_text(encoding="utf-8")
        for label, target in LINK_RE.findall(text):
            if target.startswith(IGNORED_SCHEMES):
                continue
            clean = target.split("#", 1)[0].strip()
            if not clean:
                continue
            resolved = (path.parent / clean).resolve()
            if ROOT.resolve() not in resolved.parents and resolved != ROOT.resolve():
                problems.append(f"{path.relative_to(ROOT)}: link '{label}' escapes the repository: {target}")
                continue
            if not resolved.exists():
                problems.append(f"{path.relative_to(ROOT)}: broken link '{label}' -> {target}")
    return problems


def table_products(path: Path) -> list[str]:
    """Product names from the first column of the portfolio-style table."""
    text = path.read_text(encoding="utf-8")
    names: list[str] = []
    in_table = False
    for line in text.splitlines():
        if line.startswith(PRODUCT_TABLE_HEADER):
            in_table = True
            continue
        if not in_table:
            continue
        if not line.startswith("|"):
            in_table = False
            continue
        if set(line.strip()) <= {"|", "-", ":", " "}:
            continue
        cell = line.split("|")[1].strip()
        match = re.match(r"\[([^\]]+)\]", cell) or re.match(r"([^|]+)", cell)
        if match:
            name = match.group(1).strip()
            if name and name.lower() != "product":
                names.append(name)
    return names


def check_portfolio() -> list[str]:
    readme = ROOT / "README.md"
    register = ROOT / "docs" / "PORTFOLIO_REGISTER.md"
    if not readme.exists() or not register.exists():
        return ["README.md or docs/PORTFOLIO_REGISTER.md is missing"]

    def key(name: str) -> str:
        return re.sub(r"[^a-z0-9]", "", name.lower())

    # The register carries a row for the company itself; the README portfolio
    # table deliberately lists products only.
    company_rows = {"vectolith"}
    readme_products = {key(n) for n in table_products(readme)} - company_rows
    register_products = {key(n) for n in table_products(register)} - company_rows

    problems: list[str] = []
    for missing in sorted(readme_products - register_products):
        problems.append(f"README lists a product the portfolio register does not: {missing}")
    for missing in sorted(register_products - readme_products):
        problems.append(f"PORTFOLIO_REGISTER lists a product the README does not: {missing}")
    if not register_products:
        problems.append("no products could be parsed from the portfolio register")
    if not readme_products:
        problems.append("no products could be parsed from the README portfolio table")
    return problems


def main() -> int:
    problems = check_links() + check_portfolio()
    if problems:
        print(f"{len(problems)} problem(s) found:\n")
        for problem in problems:
            print(f"  - {problem}")
        return 1
    files = len(markdown_files())
    print(f"OK: {files} Markdown files, all relative links resolve, portfolio tables agree.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
