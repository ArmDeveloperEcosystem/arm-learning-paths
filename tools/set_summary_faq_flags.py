#!/usr/bin/env python3
"""Set generated summary/FAQ front-matter flags for Learning Paths."""

from __future__ import annotations

import argparse
import re
import subprocess
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
LEARNING_PATH_ROOT = REPO_ROOT / "content" / "learning-paths"
FLAGS = ("generate_summary_faq", "rerun_summary", "rerun_faqs")
FRONT_MATTER_PATTERN = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.DOTALL)


def parse_bool(value: str) -> bool:
    normalized = value.strip().lower()
    if normalized in {"true", "t", "yes", "y", "1"}:
        return True
    if normalized in {"false", "f", "no", "n", "0"}:
        return False
    raise argparse.ArgumentTypeError(f"Expected true or false, got {value!r}.")


def bool_text(value: bool) -> str:
    return "true" if value else "false"


def run_git_lines(args: list[str]) -> list[str]:
    result = subprocess.run(
        ["git", *args],
        cwd=REPO_ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return [line.strip() for line in result.stdout.splitlines() if line.strip()]


def learning_path_index_for_repo_path(repo_path: str) -> Path | None:
    try:
        relative_path = Path(repo_path).relative_to("content/learning-paths")
    except ValueError:
        return None

    if len(relative_path.parts) < 2:
        return None

    category, slug = relative_path.parts[:2]
    index_path = LEARNING_PATH_ROOT / category / slug / "_index.md"
    return index_path if index_path.exists() else None


def untracked_learning_path_files() -> list[str]:
    return run_git_lines(["ls-files", "--others", "--exclude-standard", "--", "content/learning-paths"])


def changed_learning_path_files(base_ref: str, diff_filter: str) -> list[str]:
    return run_git_lines(
        ["diff", "--name-only", f"--diff-filter={diff_filter}", base_ref, "--", "content/learning-paths"]
    )


def find_index_files_since(base_ref: str, diff_filter: str, include_untracked: bool) -> list[Path]:
    changed_files = changed_learning_path_files(base_ref, diff_filter)
    if include_untracked:
        changed_files.extend(untracked_learning_path_files())

    paths = {
        index_path
        for changed_file in changed_files
        if (index_path := learning_path_index_for_repo_path(changed_file)) is not None
    }
    return sorted(paths)


def find_index_files(args: argparse.Namespace) -> list[Path]:
    if args.all:
        return sorted(LEARNING_PATH_ROOT.glob("*/*/_index.md"))

    if args.category:
        category_dir = LEARNING_PATH_ROOT / args.category
        if not category_dir.is_dir():
            raise SystemExit(f"Category not found: {args.category}")
        return sorted(category_dir.glob("*/_index.md"))

    if args.new_since:
        return find_index_files_since(args.new_since, "A", include_untracked=True)

    if args.changed_since:
        return find_index_files_since(args.changed_since, "ACMR", include_untracked=True)

    paths: list[Path] = []
    for raw_path in args.path.split(","):
        path = Path(raw_path.strip())
        if not path:
            continue
        if not path.is_absolute():
            path = REPO_ROOT / path
        if path.is_dir():
            path = path / "_index.md"
        if not path.exists():
            raise SystemExit(f"Path not found: {path.relative_to(REPO_ROOT)}")
        if path.name != "_index.md":
            raise SystemExit(f"Path is not a Learning Path _index.md file: {path.relative_to(REPO_ROOT)}")
        paths.append(path)
    return sorted(set(paths))


def replacement_flags(args: argparse.Namespace) -> dict[str, bool]:
    values = {
        "generate_summary_faq": args.generate_summary_faq,
        "rerun_summary": args.rerun_summary,
        "rerun_faqs": args.rerun_faqs,
    }

    if args.all_true:
        values = {flag: True for flag in FLAGS}
    elif args.all_false:
        values = {flag: False for flag in FLAGS}

    selected = {flag: value for flag, value in values.items() if value is not None}
    if not selected:
        raise SystemExit("Choose --all-true, --all-false, or at least one individual flag value.")
    return selected


def set_front_matter_flag(front_matter: str, flag: str, value: bool) -> tuple[str, bool]:
    line_pattern = re.compile(rf"^#?[ \t]*{re.escape(flag)}[ \t]*:[ \t]*(?:true|false)[ \t]*$", re.MULTILINE)
    replacement = f"{flag}: {bool_text(value)}"

    if line_pattern.search(front_matter):
        updated = line_pattern.sub(replacement, front_matter, count=1)
        return updated, updated != front_matter

    lines = front_matter.splitlines()
    insert_at = 0
    for index, line in enumerate(lines):
        if re.match(r"^(title|description|minutes_to_complete|who_is_this_for|learning_objectives|prerequisites|author|reviewers|test_maintenance|test_images|weight|layout|draft|hidden|tags|skilllevels|subjects|armips|tools_software_languages|operatingsystems|cloud_service_providers|ci_cd|learning_path_main_image|main_image|additional_search_terms|ignore_connection_issues|generate_summary_faq|rerun_summary|rerun_faqs)\s*:", line):
            insert_at = index + 1
    lines.insert(insert_at, replacement)
    return "\n".join(lines), True


def update_file(path: Path, values: dict[str, bool], dry_run: bool) -> bool:
    text = path.read_text(encoding="utf-8")
    match = FRONT_MATTER_PATTERN.match(text)
    if not match:
        raise SystemExit(f"Missing YAML front matter: {path.relative_to(REPO_ROOT)}")

    front_matter = match.group(1)
    changed = False
    for flag, value in values.items():
        front_matter, flag_changed = set_front_matter_flag(front_matter, flag, value)
        changed = changed or flag_changed

    if changed and not dry_run:
        updated_text = f"---\n{front_matter}\n---\n{text[match.end():]}"
        path.write_text(updated_text, encoding="utf-8")

    return changed


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Set generated summary/FAQ control flags in Learning Path _index.md files."
    )
    target = parser.add_mutually_exclusive_group(required=True)
    target.add_argument("--all", action="store_true", help="Update all Learning Paths.")
    target.add_argument("--category", help="Update one top-level Learning Path category.")
    target.add_argument("--path", help="Update one path, _index.md file, or comma-separated path list.")
    target.add_argument("--new-since", metavar="REF", help="Update Learning Paths added since a git ref.")
    target.add_argument("--changed-since", metavar="REF", help="Update Learning Paths changed since a git ref.")

    preset = parser.add_mutually_exclusive_group()
    preset.add_argument("--all-true", action="store_true", help="Set generate/rerun flags to true.")
    preset.add_argument("--all-false", action="store_true", help="Set generate/rerun flags to false.")

    parser.add_argument("--generate-summary-faq", type=parse_bool, help="Set generate_summary_faq.")
    parser.add_argument("--rerun-summary", type=parse_bool, help="Set rerun_summary.")
    parser.add_argument("--rerun-faqs", type=parse_bool, help="Set rerun_faqs.")
    parser.add_argument("--dry-run", action="store_true", help="Show what would change without editing files.")

    args = parser.parse_args()
    values = replacement_flags(args)
    paths = find_index_files(args)
    changed = 0

    for path in paths:
        did_change = update_file(path, values, args.dry_run)
        changed += int(did_change)
        status = "would update" if args.dry_run and did_change else "updated" if did_change else "unchanged"
        print(f"{status:12} {path.relative_to(REPO_ROOT)}")

    print(
        f"\nProcessed {len(paths)} Learning Paths: {changed} "
        f"{'would change' if args.dry_run else 'changed'}, {len(paths) - changed} unchanged."
    )
    print("Set values: " + ", ".join(f"{flag}={bool_text(value)}" for flag, value in values.items()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
