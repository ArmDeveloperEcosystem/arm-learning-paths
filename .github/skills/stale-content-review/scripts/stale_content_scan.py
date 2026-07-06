#!/usr/bin/env python3
"""Scan Arm Learning Path content for stale-content risk signals."""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path


DEFAULT_PATHS = ["content/learning-paths", "content/install-guides"]

RULES = [
    {
        "id": "temporal-language",
        "score": 2,
        "allow_code": False,
        "reason": "Temporal wording may need freshness review.",
        "pattern": re.compile(
            r"\b(currently|current support|currently supports?|latest|recently|newly|"
            r"at the time of writing|as of|today)\b",
            re.IGNORECASE,
        ),
    },
    {
        "id": "preview-or-beta",
        "score": 3,
        "allow_code": True,
        "reason": "Preview, beta, nightly, or experimental content often changes quickly.",
        "pattern": re.compile(r"\b(preview|beta|nightly|experimental|deprecated)\b", re.IGNORECASE),
    },
    {
        "id": "mutable-download",
        "score": 4,
        "allow_code": True,
        "reason": "Install scripts, release downloads, or raw URLs can change without this content changing.",
        "pattern": re.compile(
            r"\b(curl|wget|Invoke-WebRequest|iwr)\b.*\b(latest|releases?|download|raw|install\.sh|script)\b|"
            r"\b(latest|releases?|download|raw|install\.sh|script)\b.*\b(curl|wget|Invoke-WebRequest|iwr)\b",
            re.IGNORECASE,
        ),
    },
    {
        "id": "floating-container-tag",
        "score": 3,
        "allow_code": True,
        "reason": "Container tags that point to latest can drift over time.",
        "pattern": re.compile(r"\b[\w./-]+:latest\b", re.IGNORECASE),
    },
    {
        "id": "unpinned-package-install",
        "score": 2,
        "allow_code": True,
        "reason": "Unpinned package installs may change as package repositories change.",
        "pattern": re.compile(
            r"\b(pip3?\s+install|python3?\s+-m\s+pip\s+install|npm\s+(?:install|i)|"
            r"apt(?:-get)?\s+install|dnf\s+install|yum\s+install|brew\s+install|"
            r"go\s+install|cargo\s+install)\b",
            re.IGNORECASE,
        ),
    },
    {
        "id": "version-specific-dependency",
        "score": 2,
        "allow_code": False,
        "reason": "Version-specific dependency claims may need periodic verification.",
        "pattern": re.compile(
            r"\b(Ubuntu|Debian|Fedora|RHEL|Rocky Linux|Amazon Linux|macOS|Windows|"
            r"Python|Node(?:\.js)?|npm|Java|JDK|Go|Rust|LLVM|GCC|CUDA|PyTorch|"
            r"TensorFlow|Kubernetes|Docker|Terraform|OpenSSL|CMake)\s+"
            r"(?:version\s*)?v?\d+(?:\.\d+){0,2}\b",
            re.IGNORECASE,
        ),
    },
    {
        "id": "external-moving-link",
        "score": 2,
        "allow_code": True,
        "reason": "External release, download, docs, pricing, or support URLs may need checking.",
        "pattern": re.compile(
            r"https?://docs\.[^\s)\]\"]+|"
            r"https?://[^\s)\]\"]*(?:latest|releases?|download|documentation|pricing|support|docs[./_-])[^\s)\]\"]*",
            re.IGNORECASE,
        ),
    },
]

IMAGE_RE = re.compile(r"!\[([^\]]*)\]\(([^)\s]+)(?:\s+\"([^\"]*)\")?\)")
DATE_RE = re.compile(r"\b(20\d{2})[-/](\d{1,2})[-/](\d{1,2})\b")
FENCE_RE = re.compile(r"^\s*(```|~~~)")

UI_IMAGE_WORDS = re.compile(
    r"\b(screenshot|screen shot|console|portal|dashboard|ui|ide|visual studio|vs code|"
    r"browser|dialog|menu|form|button|tab|settings|wizard|page|preview|extension)\b",
    re.IGNORECASE,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Scan content for stale-maintenance risk signals.")
    parser.add_argument("paths", nargs="*", default=DEFAULT_PATHS, help="Files or directories to scan.")
    parser.add_argument("--format", choices=["markdown", "json", "csv"], default="markdown")
    parser.add_argument("--output", help="Write the report to this file.")
    parser.add_argument(
        "--min-score",
        type=int,
        default=None,
        help="Only report files with this score or higher. Defaults to 20 for a full content scan and 4 for explicit paths.",
    )
    parser.add_argument(
        "--max-findings-per-file",
        type=int,
        default=12,
        help="Maximum sample findings to print for each file in Markdown output.",
    )
    parser.add_argument(
        "--old-date-months",
        type=int,
        default=18,
        help="Flag explicit YYYY-MM-DD or YYYY/MM/DD dates older than this many months.",
    )
    parser.add_argument("--include-drafts", action="store_true", help="Include files with draft: true.")
    return parser.parse_args()


def iter_markdown_files(paths: list[str]) -> list[Path]:
    files: set[Path] = set()
    for raw in paths:
        path = Path(raw)
        if path.is_file() and path.suffix == ".md":
            files.add(path)
        elif path.is_dir():
            for candidate in path.rglob("*.md"):
                if ".git" not in candidate.parts:
                    files.add(candidate)
    return sorted(files)


def parse_front_matter(lines: list[str]) -> dict[str, str]:
    if not lines or lines[0].strip() != "---":
        return {}

    front_matter: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            break
        match = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)\s*$", line)
        if match:
            front_matter[match.group(1)] = match.group(2).strip().strip("'\"")
    return front_matter


def is_draft(front_matter: dict[str, str]) -> bool:
    return front_matter.get("draft", "").lower() == "true"


def content_unit(path: Path) -> str:
    parts = path.parts
    if len(parts) >= 4 and parts[0] == "content" and parts[1] == "learning-paths":
        return "/".join(parts[:4])
    if len(parts) >= 3 and parts[0] == "content" and parts[1] == "install-guides":
        if path.name == "_index.md" and len(parts) >= 4:
            return "/".join(parts[:3])
        if len(parts) >= 4:
            return "/".join(parts[:3])
        return str(path.with_suffix(""))
    return str(path.parent)


def excerpt(line: str) -> str:
    text = " ".join(line.strip().split())
    if len(text) > 160:
        return text[:157] + "..."
    return text


def add_finding(findings: list[dict], line: int, category: str, score: int, reason: str, text: str) -> None:
    findings.append(
        {
            "line": line,
            "category": category,
            "score": score,
            "reason": reason,
            "excerpt": excerpt(text),
        }
    )


def month_delta(start: dt.date, end: dt.date) -> int:
    return (end.year - start.year) * 12 + (end.month - start.month)


def scan_file(path: Path, today: dt.date, old_date_months: int, include_drafts: bool) -> dict | None:
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        text = path.read_text(encoding="utf-8", errors="replace")

    lines = text.splitlines()
    front_matter = parse_front_matter(lines)
    if is_draft(front_matter) and not include_drafts:
        return {"path": str(path), "skipped": "draft"}

    findings: list[dict] = []
    image_count = 0
    ui_image_count = 0
    in_fence = False

    for line_number, line in enumerate(lines, start=1):
        if FENCE_RE.match(line):
            in_fence = not in_fence

        for rule in RULES:
            if in_fence and not rule["allow_code"]:
                continue
            if rule["pattern"].search(line):
                add_finding(findings, line_number, rule["id"], rule["score"], rule["reason"], line)

        for match in DATE_RE.finditer(line):
            year, month, day = map(int, match.groups())
            try:
                found_date = dt.date(year, month, day)
            except ValueError:
                continue
            if month_delta(found_date, today) >= old_date_months:
                add_finding(
                    findings,
                    line_number,
                    "old-explicit-date",
                    2,
                    "Explicit dates older than the threshold may need freshness review.",
                    line,
                )
                break

        for match in IMAGE_RE.finditer(line):
            image_count += 1
            alt, image_path, title = match.groups()
            image_text = " ".join(part or "" for part in (alt, image_path, title))
            if UI_IMAGE_WORDS.search(image_text):
                ui_image_count += 1
                add_finding(
                    findings,
                    line_number,
                    "screenshot-or-ui-image",
                    5,
                    "Screenshot or UI image may need visual freshness review.",
                    line,
                )

    if image_count >= 4:
        add_finding(
            findings,
            0,
            "image-heavy-page",
            2,
            "Image-heavy pages can become stale when UI, output, or diagrams change.",
            f"{image_count} Markdown image references found.",
        )

    if not findings:
        return None

    by_category: dict[str, list[dict]] = defaultdict(list)
    for finding in findings:
        by_category[finding["category"]].append(finding)

    score = 0
    for category_findings in by_category.values():
        score += max(finding["score"] for finding in category_findings)
        score += min(len(category_findings) - 1, 4)

    return {
        "path": str(path),
        "unit": content_unit(path),
        "score": score,
        "finding_count": len(findings),
        "image_count": image_count,
        "ui_image_count": ui_image_count,
        "categories": dict(Counter(finding["category"] for finding in findings)),
        "findings": findings,
    }


def resolve_min_score(args: argparse.Namespace) -> int:
    if args.min_score is not None:
        return args.min_score
    if args.paths == DEFAULT_PATHS:
        return 20
    return 4


def scan(paths: list[str], args: argparse.Namespace) -> tuple[list[dict], dict]:
    today = dt.date.today()
    candidates = iter_markdown_files(paths)
    min_score = resolve_min_score(args)
    records = []
    skipped = Counter()

    for path in candidates:
        result = scan_file(path, today, args.old_date_months, args.include_drafts)
        if not result:
            continue
        if result.get("skipped"):
            skipped[result["skipped"]] += 1
            continue
        if result["score"] >= min_score:
            records.append(result)

    records.sort(key=lambda item: (-item["score"], item["path"]))
    summary = {
        "generated": today.isoformat(),
        "scanned_files": len(candidates),
        "reported_files": len(records),
        "skipped": dict(skipped),
        "min_score": min_score,
        "paths": paths,
    }
    return records, summary


def category_summary(record: dict) -> str:
    parts = [f"{category} ({count})" for category, count in record["categories"].items()]
    return ", ".join(parts)


def escape_cell(value: object) -> str:
    return str(value).replace("|", "\\|")


def format_markdown(records: list[dict], summary: dict, max_findings_per_file: int) -> str:
    lines = [
        "# Stale Content Risk Scan",
        "",
        f"Generated: {summary['generated']}",
        f"Scanned files: {summary['scanned_files']}",
        f"Reported files: {summary['reported_files']} with score >= {summary['min_score']}",
    ]
    if summary["skipped"]:
        skipped = ", ".join(f"{key}: {value}" for key, value in summary["skipped"].items())
        lines.append(f"Skipped files: {skipped}")
    lines.extend(["", "## Top candidates", ""])

    if not records:
        lines.append("No files met the reporting threshold.")
        return "\n".join(lines) + "\n"

    lines.extend(
        [
            "| Score | File | Unit | Flags |",
            "| ---: | --- | --- | --- |",
        ]
    )
    for record in records[:50]:
        lines.append(
            f"| {record['score']} | `{escape_cell(record['path'])}` | "
            f"`{escape_cell(record['unit'])}` | {escape_cell(category_summary(record))} |"
        )

    lines.extend(["", "## Details", ""])
    for record in records:
        lines.extend(
            [
                f"### `{record['path']}`",
                "",
                f"- Score: {record['score']}",
                f"- Unit: `{record['unit']}`",
                f"- Flags: {category_summary(record)}",
            ]
        )
        if record["image_count"]:
            lines.append(f"- Images: {record['image_count']} total, {record['ui_image_count']} UI/screenshot-like")
        lines.append("")

        for finding in record["findings"][:max_findings_per_file]:
            line_label = "file" if finding["line"] == 0 else f"line {finding['line']}"
            lines.append(
                f"- {line_label} [{finding['category']}]: {finding['reason']} "
                f"`{finding['excerpt']}`"
            )
        remaining = len(record["findings"]) - max_findings_per_file
        if remaining > 0:
            lines.append(f"- {remaining} more findings omitted from this sample.")
        lines.append("")

    return "\n".join(lines)


def write_csv(records: list[dict], stream) -> None:
    writer = csv.DictWriter(
        stream,
        fieldnames=["score", "path", "unit", "finding_count", "image_count", "ui_image_count", "categories"],
    )
    writer.writeheader()
    for record in records:
        writer.writerow(
            {
                "score": record["score"],
                "path": record["path"],
                "unit": record["unit"],
                "finding_count": record["finding_count"],
                "image_count": record["image_count"],
                "ui_image_count": record["ui_image_count"],
                "categories": category_summary(record),
            }
        )


def main() -> int:
    args = parse_args()
    records, summary = scan(args.paths, args)

    if args.format == "json":
        output = json.dumps({"summary": summary, "records": records}, indent=2)
    elif args.format == "csv":
        if args.output:
            with Path(args.output).open("w", encoding="utf-8", newline="") as stream:
                write_csv(records, stream)
            return 0
        write_csv(records, sys.stdout)
        return 0
    else:
        output = format_markdown(records, summary, args.max_findings_per_file)

    if args.output:
        Path(args.output).write_text(output, encoding="utf-8")
    else:
        print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
