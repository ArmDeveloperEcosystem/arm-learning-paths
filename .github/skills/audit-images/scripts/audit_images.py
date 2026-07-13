#!/usr/bin/env python3
"""Audit Markdown image alt text in Arm Learning Paths and install guides."""

from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable
from urllib.parse import unquote, urlparse


IMAGE_RE = re.compile(r"!\[([^\]]*)\]\(([^)\n]+)\)")
PLACEHOLDER_RE = re.compile(r"\b(alt[- ]?txt|alt[- ]?text|example image|placeholder)\b", re.IGNORECASE)
VAGUE_ALT_RE = re.compile(
    r"^(img\d*|image\d*|screenshot\d*|screen shot|graph|chart|diagram|figure|photo|"
    r"output\d*|aws\d*|gcloud\d*|pulumi|remote|connect|role|buildspec|artifacts)$",
    re.IGNORECASE,
)
ALIGNMENT_RE = re.compile(r"#(center|left|right)\b")
URL_RE = re.compile(r"^[a-z][a-z0-9+.-]*://", re.IGNORECASE)


@dataclass
class Finding:
    file: str
    line: int
    unit: str
    image: str
    alt: str
    caption: str
    issues: list[str]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Audit Markdown image alt text in Arm Learning Paths and install guides."
    )
    parser.add_argument(
        "paths",
        nargs="*",
        default=["content/learning-paths", "content/install-guides"],
        help="Markdown files or directories to scan.",
    )
    parser.add_argument(
        "--format",
        choices=["markdown", "json", "csv"],
        default="markdown",
        help="Output format.",
    )
    parser.add_argument("--output", help="Write output to this file.")
    parser.add_argument(
        "--include-ok",
        action="store_true",
        help="Include image references with no detected issues in detailed output.",
    )
    parser.add_argument(
        "--max-alt-words",
        type=int,
        default=45,
        help="Flag alt text longer than this many words.",
    )
    parser.add_argument(
        "--repo-root",
        default=".",
        help="Repository root used for resolving local image paths.",
    )
    return parser.parse_args()


def markdown_files(paths: Iterable[str], repo_root: Path) -> list[Path]:
    files: list[Path] = []
    for raw_path in paths:
        path = (repo_root / raw_path).resolve()
        if path.is_file() and path.suffix == ".md":
            files.append(path)
        elif path.is_dir():
            files.extend(sorted(path.rglob("*.md")))
    return sorted(dict.fromkeys(files))


def split_target(raw_target: str) -> tuple[str, str]:
    target = raw_target.strip()
    caption = ""

    title_match = re.search(r'\s+"([^"]*)"\s*$', target)
    if title_match:
        caption = title_match.group(1).strip()
        target = target[: title_match.start()].strip()

    return target, caption


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def normalize_alt(alt: str) -> str:
    return ALIGNMENT_RE.sub("", alt).strip()


def word_count(text: str) -> int:
    return len(re.findall(r"[A-Za-z0-9]+(?:[-'][A-Za-z0-9]+)?", text))


def is_placeholder_or_vague(alt: str) -> bool:
    normalized = re.sub(r"[^A-Za-z0-9 -]+", "", alt).strip()
    normalized = re.sub(r"\s+", " ", normalized)
    return bool(PLACEHOLDER_RE.search(alt) or VAGUE_ALT_RE.match(normalized))


def is_url_or_anchor(target: str) -> bool:
    return bool(URL_RE.match(target)) or target.startswith("#")


def strip_url_bits(target: str) -> str:
    parsed = urlparse(target)
    if parsed.scheme:
        return target
    return unquote(target.split("#", 1)[0].split("?", 1)[0])


def resolve_local_image(target: str, md_file: Path, repo_root: Path) -> Path | None:
    if is_url_or_anchor(target):
        return None

    clean_target = strip_url_bits(target)
    if not clean_target:
        return None

    if clean_target.startswith("/"):
        site_path = clean_target.lstrip("/")
        if site_path.startswith(("learning-paths/", "install-guides/")):
            return repo_root / "content" / site_path
        return repo_root / site_path

    return md_file.parent / clean_target


def content_unit(md_file: Path, repo_root: Path) -> str:
    rel = md_file.relative_to(repo_root).as_posix()
    parts = rel.split("/")

    if parts[:2] == ["content", "learning-paths"] and len(parts) >= 4:
        return "/".join(parts[:4])

    if parts[:2] == ["content", "install-guides"]:
        return rel

    return str(Path(rel).parent)


def detect_issues(
    alt: str,
    caption: str,
    target: str,
    md_file: Path,
    repo_root: Path,
    max_alt_words: int,
) -> list[str]:
    issues: list[str] = []
    normalized = normalize_alt(alt)
    normalized_words = word_count(normalized)

    if not alt.strip():
        issues.append("missing_alt")

    if alt.strip().startswith(('"', "'")) or alt.strip().endswith(('"', "'")):
        issues.append("quoted_alt")

    if re.search(r"\s+#(center|left|right)\b", alt):
        issues.append("alignment_not_attached")

    if "#center" not in alt:
        issues.append("missing_center_alignment")

    if is_placeholder_or_vague(normalized):
        issues.append("placeholder_or_vague_alt")

    if normalized and normalized_words < 4:
        issues.append("too_short_alt")

    if normalized_words > max_alt_words:
        issues.append("overlong_alt")

    if caption and re.match(r"Figure\s+\d+\s*:", caption, re.IGNORECASE):
        issues.append("figure_number_caption")

    if caption and normalized_words <= 2 and word_count(caption) >= 4:
        issues.append("caption_substitutes_for_alt")

    local_image = resolve_local_image(target, md_file, repo_root)
    if local_image is not None and not local_image.exists():
        issues.append("missing_local_image")

    return issues


def audit_file(md_file: Path, repo_root: Path, max_alt_words: int) -> list[Finding]:
    text = md_file.read_text(encoding="utf-8")
    unit = content_unit(md_file, repo_root)
    findings: list[Finding] = []

    for match in IMAGE_RE.finditer(text):
        raw_alt = match.group(1)
        target, caption = split_target(match.group(2))
        issues = detect_issues(raw_alt, caption, target, md_file, repo_root, max_alt_words)
        findings.append(
            Finding(
                file=md_file.relative_to(repo_root).as_posix(),
                line=line_number(text, match.start()),
                unit=unit,
                image=target,
                alt=raw_alt,
                caption=caption,
                issues=issues,
            )
        )

    duplicate_counts = Counter(
        normalize_alt(item.alt).lower()
        for item in findings
        if normalize_alt(item.alt) and not is_placeholder_or_vague(normalize_alt(item.alt))
    )
    for item in findings:
        normalized = normalize_alt(item.alt).lower()
        if normalized and duplicate_counts[normalized] > 1:
            item.issues.append("duplicate_alt_in_file")

    return findings


def summarize(findings: list[Finding], files_scanned: int) -> dict:
    faulty = [item for item in findings if item.issues]
    issue_counts = Counter(issue for item in faulty for issue in item.issues)
    unit_counts: dict[str, Counter] = defaultdict(Counter)

    for item in findings:
        unit_counts[item.unit]["total"] += 1
        if item.issues:
            unit_counts[item.unit]["faulty"] += 1

    units = [
        {"unit": unit, "total": counts["total"], "faulty": counts["faulty"]}
        for unit, counts in sorted(unit_counts.items())
    ]
    units.sort(key=lambda row: (-row["faulty"], row["unit"]))

    return {
        "files_scanned": files_scanned,
        "images_found": len(findings),
        "faulty_images": len(faulty),
        "issue_counts": dict(sorted(issue_counts.items())),
        "units": units,
    }


def markdown_output(findings: list[Finding], summary: dict, include_ok: bool) -> str:
    rows = [item for item in findings if include_ok or item.issues]
    lines = [
        "# Image audit",
        "",
        f"- Markdown files scanned: {summary['files_scanned']}",
        f"- Images found: {summary['images_found']}",
        f"- Faulty images: {summary['faulty_images']}",
        "",
        "## Issue counts",
        "",
    ]

    if summary["issue_counts"]:
        for issue, count in summary["issue_counts"].items():
            lines.append(f"- `{issue}`: {count}")
    else:
        lines.append("- No issues detected")

    lines.extend(["", "## Content units", ""])
    lines.append("| Unit | Faulty | Total |")
    lines.append("|---|---:|---:|")
    for row in summary["units"]:
        if row["faulty"] or include_ok:
            lines.append(f"| `{row['unit']}` | {row['faulty']} | {row['total']} |")

    lines.extend(["", "## Findings", ""])
    if not rows:
        lines.append("No findings to report.")
        return "\n".join(lines) + "\n"

    lines.append("| File | Line | Image | Alt text | Caption | Issues |")
    lines.append("|---|---:|---|---|---|---|")
    for item in rows:
        issues = ", ".join(f"`{issue}`" for issue in item.issues) or "OK"
        lines.append(
            "| "
            f"`{item.file}` | {item.line} | `{item.image}` | "
            f"{escape_table(item.alt)} | {escape_table(item.caption)} | {issues} |"
        )

    return "\n".join(lines) + "\n"


def escape_table(value: str) -> str:
    escaped = value.replace("|", r"\|").replace("\n", " ")
    return escaped if escaped else ""


def json_output(findings: list[Finding], summary: dict, include_ok: bool) -> str:
    rows = [item for item in findings if include_ok or item.issues]
    return json.dumps(
        {"summary": summary, "findings": [asdict(item) for item in rows]},
        indent=2,
        sort_keys=True,
    ) + "\n"


def csv_output(findings: list[Finding], include_ok: bool) -> str:
    from io import StringIO

    rows = [item for item in findings if include_ok or item.issues]
    output = StringIO()
    writer = csv.writer(output)
    writer.writerow(["file", "line", "unit", "image", "alt", "caption", "issues"])
    for item in rows:
        writer.writerow(
            [item.file, item.line, item.unit, item.image, item.alt, item.caption, ";".join(item.issues)]
        )
    return output.getvalue()


def main() -> int:
    args = parse_args()
    repo_root = Path(args.repo_root).resolve()
    files = markdown_files(args.paths, repo_root)
    findings: list[Finding] = []

    for md_file in files:
        findings.extend(audit_file(md_file, repo_root, args.max_alt_words))

    summary = summarize(findings, len(files))

    if args.format == "json":
        output = json_output(findings, summary, args.include_ok)
    elif args.format == "csv":
        output = csv_output(findings, args.include_ok)
    else:
        output = markdown_output(findings, summary, args.include_ok)

    if args.output:
        Path(args.output).write_text(output, encoding="utf-8")
    else:
        print(output, end="")

    return 1 if summary["faulty_images"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
