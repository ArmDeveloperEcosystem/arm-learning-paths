#!/usr/bin/env python3
"""Snapshot and verify technical surfaces during editorial Markdown refactors."""

from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import sys


FENCE_RE = re.compile(r"^(`{3,}|~{3,})[^\n]*\n.*?^\1\s*$", re.MULTILINE | re.DOTALL)
SHORTCODE_RE = re.compile(r"{{[<%].*?[>%]}}", re.DOTALL)
INLINE_DEST_RE = re.compile(r"!?\[[^\]]*\]\(\s*(?:<([^>]+)>|([^\s)]+))")
REFERENCE_DEST_RE = re.compile(r"^\s*\[[^\]]+\]:\s*(?:<([^>]+)>|([^\s]+))", re.MULTILINE)


def digest(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def markdown_files(target: Path) -> list[Path]:
    if target.is_file():
        return [target] if target.suffix.lower() in {".md", ".mdx"} else []
    return sorted(
        path
        for path in target.rglob("*")
        if path.is_file() and path.suffix.lower() in {".md", ".mdx"}
    )


def normalized_counter(values: list[str]) -> dict[str, int]:
    return dict(sorted(Counter(values).items()))


def inspect_file(path: Path) -> dict[str, object]:
    content = path.read_text(encoding="utf-8")
    fences = []
    for match in FENCE_RE.finditer(content):
        lines = match.group(0).splitlines(keepends=True)
        body = "".join(lines[1:-1])
        fences.append(digest(body))
    shortcodes = [digest(match.group(0)) for match in SHORTCODE_RE.finditer(content)]
    destinations: list[str] = []
    for pattern in (INLINE_DEST_RE, REFERENCE_DEST_RE):
        for match in pattern.finditer(content):
            destinations.append(match.group(1) or match.group(2))
    return {
        "fenced_blocks": normalized_counter(fences),
        "link_and_image_destinations": normalized_counter(destinations),
        "hugo_shortcodes": normalized_counter(shortcodes),
    }


def snapshot(target: Path) -> dict[str, object]:
    resolved = target.resolve()
    files = markdown_files(resolved)
    if not files:
        raise ValueError(f"no Markdown files found under {target}")
    root = resolved if resolved.is_dir() else resolved.parent
    return {
        "schema_version": 2,
        "target": str(resolved),
        "files": {
            str(path.relative_to(root)): inspect_file(path)
            for path in files
        },
    }


def compare(expected: dict[str, object], actual: dict[str, object]) -> list[str]:
    differences: list[str] = []
    expected_files = expected.get("files", {})
    actual_files = actual.get("files", {})
    if not isinstance(expected_files, dict) or not isinstance(actual_files, dict):
        return ["invalid baseline or snapshot file structure"]

    for name in sorted(set(expected_files) - set(actual_files)):
        differences.append(f"removed Markdown file: {name}")
    for name in sorted(set(actual_files) - set(expected_files)):
        differences.append(f"added Markdown file: {name}")

    for name in sorted(set(expected_files) & set(actual_files)):
        before = expected_files[name]
        after = actual_files[name]
        if not isinstance(before, dict) or not isinstance(after, dict):
            differences.append(f"invalid protected-content record: {name}")
            continue
        for field in ("fenced_blocks", "link_and_image_destinations", "hugo_shortcodes"):
            if before.get(field) != after.get(field):
                differences.append(f"changed {field.replace('_', ' ')}: {name}")
    return differences


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Guard code blocks, destinations, and Hugo shortcodes during editorial refactors."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    snapshot_parser = subparsers.add_parser("snapshot")
    snapshot_parser.add_argument("target", type=Path)
    snapshot_parser.add_argument("--output", required=True, type=Path)

    verify_parser = subparsers.add_parser("verify")
    verify_parser.add_argument("target", type=Path)
    verify_parser.add_argument("--baseline", required=True, type=Path)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        current = snapshot(args.target)
        if args.command == "snapshot":
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(json.dumps(current, indent=2) + "\n", encoding="utf-8")
            print(f"Recorded editorial guard baseline for {len(current['files'])} Markdown file(s).")
            return 0

        baseline = json.loads(args.baseline.read_text(encoding="utf-8"))
        differences = compare(baseline, current)
        if differences:
            print("Editorial guard found protected-content differences:")
            for difference in differences:
                print(f"- {difference}")
            return 1
        print(f"Editorial guard passed for {len(current['files'])} Markdown file(s).")
        return 0
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(f"editorial_guard: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
