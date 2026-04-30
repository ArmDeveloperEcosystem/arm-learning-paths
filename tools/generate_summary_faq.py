#!/usr/bin/env python3

"""
Generate summary and FAQ content for Learning Path _index.md files.

This script is intentionally template-driven for the first iteration so it can
run in CI without external AI dependencies. It:

- selects eligible Learning Paths using a front-matter flag or explicit paths
- generates a managed `generated_summary_faq` front-matter block
- updates `_index.md` files in place when requested
- writes a central run report with per-path change details

Managed front-matter contract:

    generate_summary_faq: true

    # START generated_summary_faq
    generated_summary_faq:
      template_version: summary-faq-v1
      generated_at: "2026-04-30T19:40:00Z"
      generator: template
      source_hash: "..."
      summary: >-
        ...
      faqs:
        - question: What will you accomplish in this Learning Path?
          answer: >-
            ...
    # END generated_summary_faq
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import os
import re
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Sequence

import yaml


REPO_ROOT = Path(__file__).resolve().parent.parent
LEARNING_PATH_ROOT = REPO_ROOT / "content" / "learning-paths"
DEFAULT_REPORT_PATH = REPO_ROOT / "reports" / "generated-summary-faq" / "latest-run.yml"

ENABLE_FLAG = "generate_summary_faq"
GENERATED_KEY = "generated_summary_faq"
MANAGED_START = "# START generated_summary_faq"
MANAGED_END = "# END generated_summary_faq"
TEMPLATE_VERSION = "summary-faq-v1"
DEFAULT_HISTORY_LIMIT = 20


class BlockString(str):
    """Marker type so YAML emits readable folded blocks for long prose."""


class ReadableDumper(yaml.SafeDumper):
    """YAML dumper that keeps generated prose readable in front matter/report files."""


def _block_string_presenter(dumper: yaml.SafeDumper, data: BlockString) -> yaml.nodes.ScalarNode:
    return dumper.represent_scalar("tag:yaml.org,2002:str", str(data), style=">")


def _string_presenter(dumper: yaml.SafeDumper, data: str) -> yaml.nodes.ScalarNode:
    if "\n" in data:
        return dumper.represent_scalar("tag:yaml.org,2002:str", data, style=">")
    return dumper.represent_scalar("tag:yaml.org,2002:str", data)


ReadableDumper.add_representer(BlockString, _block_string_presenter)
ReadableDumper.add_representer(str, _string_presenter)
ReadableDumper.ignore_aliases = lambda self, data: True


@dataclass
class MarkdownDocument:
    path: Path
    raw_text: str
    front_matter_text: str
    content: str
    metadata: Dict[str, Any]


@dataclass
class StepPage:
    path: Path
    title: str
    weight: int
    metadata: Dict[str, Any]
    content: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate summary/FAQ front matter for Learning Paths.")
    parser.add_argument(
        "--path-filter",
        default="",
        help="Optional comma/newline-separated list of Learning Path directories or _index.md files.",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=0,
        help="Maximum number of Learning Paths to process when no explicit path filter is provided. 0 means no limit.",
    )
    parser.add_argument(
        "--allow-unflagged",
        action="store_true",
        help=f"Process explicit or discovered Learning Paths even when `{ENABLE_FLAG}` is not true.",
    )
    parser.add_argument(
        "--write",
        action="store_true",
        help="Persist generated front-matter updates back to each _index.md file.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Compute results and print a summary without writing Learning Path files.",
    )
    parser.add_argument(
        "--report-file",
        default=str(DEFAULT_REPORT_PATH),
        help="Path to the central run report YAML file.",
    )
    parser.add_argument(
        "--no-write-report",
        action="store_true",
        help="Skip writing the central report file.",
    )
    parser.add_argument(
        "--history-limit",
        type=int,
        default=DEFAULT_HISTORY_LIMIT,
        help="Maximum number of historical run entries to retain in the central report file.",
    )
    parser.add_argument("--run-url", default="", help="Optional GitHub Actions run URL to store in the report.")
    parser.add_argument("--git-ref", default="", help="Optional Git ref or branch name to store in the report.")
    parser.add_argument("--git-sha", default="", help="Optional commit SHA to store in the report.")
    parser.add_argument("--actor", default="", help="Optional workflow actor to store in the report.")

    args = parser.parse_args()

    if args.write and args.dry_run:
        parser.error("Use either --write or --dry-run, not both.")
    if not args.write and not args.dry_run:
        args.dry_run = True

    return args


def read_markdown_document(path: Path, require_front_matter: bool = True) -> MarkdownDocument:
    raw_text = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\s*\n(.*?)\n---\s*\n?(.*)\Z", raw_text, re.DOTALL)
    if not match:
        if require_front_matter:
            raise ValueError(f"{path} does not contain valid YAML front matter.")
        return MarkdownDocument(
            path=path,
            raw_text=raw_text,
            front_matter_text="",
            content=raw_text,
            metadata={},
        )

    front_matter_text = match.group(1)
    content = match.group(2)
    metadata = yaml.safe_load(front_matter_text) or {}
    if not isinstance(metadata, dict):
        raise ValueError(f"{path} front matter did not parse as a mapping.")

    return MarkdownDocument(
        path=path,
        raw_text=raw_text,
        front_matter_text=front_matter_text,
        content=content,
        metadata=metadata,
    )


def fallback_title_from_content(content: str, path: Path) -> str:
    for line in content.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        heading_match = re.match(r"^#{1,6}\s+(.*)$", stripped)
        if heading_match:
            return compact_whitespace(heading_match.group(1))
    return compact_whitespace(path.stem.replace("-", " ").replace("_", " ").title())


def normalize_path_filter(path_filter: str) -> List[Path]:
    raw_items = [item.strip() for item in re.split(r"[\n,]+", path_filter) if item.strip()]
    resolved: List[Path] = []

    for item in raw_items:
        candidate = Path(item)
        if not candidate.is_absolute():
            candidate = (REPO_ROOT / candidate).resolve()

        if candidate.is_dir():
            candidate = candidate / "_index.md"

        if candidate.name != "_index.md" or not candidate.exists():
            raise FileNotFoundError(f"Could not resolve Learning Path index from '{item}'.")

        resolved.append(candidate)

    return resolved


def discover_learning_path_indexes() -> List[Path]:
    indexes = sorted(LEARNING_PATH_ROOT.glob("*/*/_index.md"))
    return [path for path in indexes if path.is_file()]


def has_enable_flag(doc: MarkdownDocument) -> bool:
    return bool(doc.metadata.get(ENABLE_FLAG))


def is_draft(doc: MarkdownDocument) -> bool:
    return bool(doc.metadata.get("draft", False))


def load_steps(index_path: Path) -> List[StepPage]:
    steps: List[StepPage] = []
    for md_path in index_path.parent.glob("*.md"):
        doc = read_markdown_document(md_path, require_front_matter=False)
        weight = doc.metadata.get("weight", 99999)
        if not isinstance(weight, int):
            try:
                weight = int(weight)
            except Exception:
                weight = 99999

        title = str(doc.metadata.get("title", "")).strip() or fallback_title_from_content(doc.content, md_path)
        steps.append(
            StepPage(
                path=md_path,
                title=title,
                weight=weight,
                metadata=doc.metadata,
                content=doc.content,
            )
        )

    steps.sort(key=lambda step: (step.weight, step.path.name))
    return steps


def compact_whitespace(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def ensure_sentence(value: str) -> str:
    cleaned = compact_whitespace(value)
    if not cleaned:
        return ""
    if cleaned[-1] not in ".!?":
        cleaned += "."
    return cleaned


def strip_markdown_links(text: str) -> str:
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    return compact_whitespace(text)


def normalize_audience(value: str) -> str:
    cleaned = compact_whitespace(value)
    patterns = [
        r"^This Learning Path is for\s+",
        r"^This learning path is for\s+",
        r"^This topic is for\s+",
        r"^This is an? [^.]*? topic for\s+",
        r"^This is for\s+",
    ]
    for pattern in patterns:
        cleaned = re.sub(pattern, "", cleaned, flags=re.IGNORECASE)
    return cleaned.rstrip(". ")


def normalize_objective_for_sentence(objective: str) -> str:
    cleaned = compact_whitespace(objective).rstrip(". ")
    if not cleaned:
        return ""
    return cleaned[0].lower() + cleaned[1:] if len(cleaned) > 1 else cleaned.lower()


def natural_join(items: Sequence[str], conjunction: str = "and") -> str:
    cleaned = [compact_whitespace(str(item)) for item in items if compact_whitespace(str(item))]
    if not cleaned:
        return ""
    if len(cleaned) == 1:
        return cleaned[0]
    if len(cleaned) == 2:
        return f"{cleaned[0]} {conjunction} {cleaned[1]}"
    return f"{', '.join(cleaned[:-1])}, {conjunction} {cleaned[-1]}"


def semicolon_join(items: Sequence[str]) -> str:
    cleaned = [compact_whitespace(str(item)) for item in items if compact_whitespace(str(item))]
    return "; ".join(cleaned)


def unique_strings(items: Iterable[Any]) -> List[str]:
    seen = set()
    ordered: List[str] = []
    for item in items:
        text = compact_whitespace(str(item))
        if text and text not in seen:
            ordered.append(text)
            seen.add(text)
    return ordered


def as_list(value: Any) -> List[Any]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def build_platform_sentence(metadata: Dict[str, Any]) -> str:
    tools = unique_strings(as_list(metadata.get("tools_software_languages")))
    operating_systems = unique_strings(as_list(metadata.get("operatingsystems")))
    arm_ips = [item for item in unique_strings(as_list(metadata.get("armips"))) if item.lower() != "all"]
    cloud_providers = unique_strings(as_list(metadata.get("cloud_service_providers")))

    parts: List[str] = []

    if tools:
        parts.append(f"tools and technologies such as {natural_join(tools[:5])}")
    if operating_systems:
        parts.append(f"{natural_join(operating_systems[:4])} environments")
    if arm_ips:
        parts.append(f"Arm platforms including {natural_join(arm_ips[:4])}")
    if cloud_providers:
        parts.append(f"cloud platforms such as {natural_join(cloud_providers[:4])}")

    if not parts:
        return ""

    return ensure_sentence(f"It focuses on {natural_join(parts, conjunction='and')}")


def build_step_sentence(steps: Sequence[StepPage]) -> str:
    visible_titles = [
        step.title
        for step in steps
        if step.path.name not in {"_index.md", "_next-steps.md", "_review.md", "_demo.md"}
        and not step.metadata.get("hide_from_navpane", False)
        and step.title
    ]
    if not visible_titles:
        return ""
    selected = visible_titles[:5]
    return ensure_sentence(f"The main steps cover {natural_join(selected)}")


def build_summary(metadata: Dict[str, Any], steps: Sequence[StepPage]) -> str:
    title = compact_whitespace(str(metadata.get("title", "This Learning Path")))
    description = ensure_sentence(str(metadata.get("description", "")).strip())
    audience = normalize_audience(str(metadata.get("who_is_this_for", "")).strip())
    objectives = [normalize_objective_for_sentence(item) for item in as_list(metadata.get("learning_objectives"))]
    objectives = [objective for objective in objectives if objective]

    sentences: List[str] = []

    if description:
        sentences.append(description)
    else:
        sentences.append(ensure_sentence(f"{title} walks you through an end-to-end Arm software workflow"))

    if audience:
        sentences.append(ensure_sentence(f"It is designed for {audience}"))

    if objectives:
        sentences.append(ensure_sentence(f"By the end, you will be able to {natural_join(objectives[:3])}"))

    platform_sentence = build_platform_sentence(metadata)
    if platform_sentence:
        sentences.append(platform_sentence)

    step_sentence = build_step_sentence(steps)
    if step_sentence:
        sentences.append(step_sentence)

    return " ".join(sentence for sentence in sentences if sentence)


def build_faqs(metadata: Dict[str, Any], steps: Sequence[StepPage]) -> List[Dict[str, str]]:
    description = ensure_sentence(str(metadata.get("description", "")).strip())
    audience_raw = ensure_sentence(str(metadata.get("who_is_this_for", "")).strip())
    prerequisites = [str(item).strip() for item in as_list(metadata.get("prerequisites")) if str(item).strip()]
    objectives = [normalize_objective_for_sentence(item) for item in as_list(metadata.get("learning_objectives"))]
    objectives = [objective for objective in objectives if objective]

    tools = unique_strings(as_list(metadata.get("tools_software_languages")))
    operating_systems = unique_strings(as_list(metadata.get("operatingsystems")))
    arm_ips = [item for item in unique_strings(as_list(metadata.get("armips"))) if item.lower() != "all"]
    cloud_providers = unique_strings(as_list(metadata.get("cloud_service_providers")))

    visible_titles = [
        step.title
        for step in steps
        if step.path.name not in {"_index.md", "_next-steps.md", "_review.md", "_demo.md"}
        and not step.metadata.get("hide_from_navpane", False)
        and step.title
    ]

    accomplishment_parts: List[str] = []
    if objectives:
        accomplishment_parts.append(ensure_sentence(f"You will {natural_join(objectives[:3])}"))
    if description:
        accomplishment_parts.append(description)

    prerequisites_answer = (
        ensure_sentence(f"Before you start, make sure you have the following: {semicolon_join(prerequisites)}")
        if prerequisites
        else "There are no explicit prerequisites listed for this Learning Path."
    )

    coverage_parts: List[str] = []
    if tools:
        coverage_parts.append(f"tools and languages including {natural_join(tools[:5])}")
    if operating_systems:
        coverage_parts.append(f"{natural_join(operating_systems[:4])} environments")
    if arm_ips:
        coverage_parts.append(f"Arm platforms such as {natural_join(arm_ips[:4])}")
    if cloud_providers:
        coverage_parts.append(f"cloud platforms such as {natural_join(cloud_providers[:4])}")

    structure_answer = (
        ensure_sentence(f"The Learning Path is organized around {natural_join(visible_titles[:5])}")
        if visible_titles
        else "The Learning Path follows the standard introduction, guided steps, and next steps structure."
    )

    faqs = [
        {
            "question": "What will you accomplish in this Learning Path?",
            "answer": " ".join(part for part in accomplishment_parts if part)
            or "You will work through an Arm-focused workflow and finish with a concrete outcome.",
        },
        {
            "question": "Who is this Learning Path for?",
            "answer": audience_raw or "This Learning Path is written for Arm software developers.",
        },
        {
            "question": "What do you need before you start?",
            "answer": prerequisites_answer,
        },
        {
            "question": "Which tools, languages, or platforms does it cover?",
            "answer": ensure_sentence(f"It covers {natural_join(coverage_parts, conjunction='and')}")
            if coverage_parts
            else "It focuses on the tools, platforms, and steps listed in the Learning Path itself.",
        },
        {
            "question": "How is the Learning Path structured?",
            "answer": structure_answer,
        },
    ]

    return faqs


def build_source_hash(metadata: Dict[str, Any], steps: Sequence[StepPage]) -> str:
    relevant = {
        "title": metadata.get("title"),
        "description": metadata.get("description"),
        "who_is_this_for": metadata.get("who_is_this_for"),
        "learning_objectives": metadata.get("learning_objectives"),
        "prerequisites": metadata.get("prerequisites"),
        "tools_software_languages": metadata.get("tools_software_languages"),
        "operatingsystems": metadata.get("operatingsystems"),
        "armips": metadata.get("armips"),
        "cloud_service_providers": metadata.get("cloud_service_providers"),
        "step_titles": [
            {
                "file": step.path.name,
                "title": step.title,
                "weight": step.weight,
                "hidden": bool(step.metadata.get("hide_from_navpane", False)),
            }
            for step in steps
        ],
    }
    payload = json.dumps(relevant, sort_keys=True, ensure_ascii=False)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def build_generated_block(metadata: Dict[str, Any], steps: Sequence[StepPage]) -> Dict[str, Any]:
    generated_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    summary = build_summary(metadata, steps)
    faqs = build_faqs(metadata, steps)

    wrapped_faqs = []
    for faq in faqs:
        wrapped_faqs.append(
            {
                "question": faq["question"],
                "answer": BlockString(faq["answer"]),
            }
        )

    return {
        "template_version": TEMPLATE_VERSION,
        "generated_at": generated_at,
        "generator": "template",
        "source_hash": build_source_hash(metadata, steps),
        "summary": BlockString(summary),
        "faqs": wrapped_faqs,
    }


def make_managed_yaml_block(generated_block: Dict[str, Any]) -> str:
    serializable = {GENERATED_KEY: copy.deepcopy(generated_block)}
    yaml_block = yaml.dump(
        serializable,
        Dumper=ReadableDumper,
        sort_keys=False,
        allow_unicode=True,
        width=92,
        default_flow_style=False,
    ).rstrip()

    lines = [MANAGED_START, yaml_block, MANAGED_END]
    return "\n".join(lines)


def insert_or_replace_managed_block(front_matter_text: str, generated_block: Dict[str, Any]) -> str:
    managed_block = make_managed_yaml_block(generated_block)
    marker_pattern = re.compile(
        rf"(?ms)^[ \t]*{re.escape(MANAGED_START)}\n.*?^[ \t]*{re.escape(MANAGED_END)}[ \t]*\n?"
    )

    if marker_pattern.search(front_matter_text):
        updated = marker_pattern.sub(managed_block + "\n", front_matter_text).rstrip()
        return updated

    insertion_patterns = [
        re.compile(r"(?m)^author:\s"),
        re.compile(r"(?m)^### Tags\s*$"),
        re.compile(r"(?m)^### FIXED, DO NOT MODIFY\s*$"),
    ]

    for pattern in insertion_patterns:
        match = pattern.search(front_matter_text)
        if match:
            insert_at = match.start()
            prefix = front_matter_text[:insert_at].rstrip()
            suffix = front_matter_text[insert_at:].lstrip("\n")
            parts = [part for part in [prefix, managed_block, suffix] if part]
            return "\n\n".join(parts).rstrip()

    return (front_matter_text.rstrip() + "\n\n" + managed_block).rstrip()


def rebuild_markdown(doc: MarkdownDocument, updated_front_matter_text: str) -> str:
    content = doc.content.lstrip("\n")
    return f"---\n{updated_front_matter_text.rstrip()}\n---\n\n{content}"


def classify_faq_changes(existing: Dict[str, Any], new: Dict[str, Any]) -> Dict[str, Any]:
    existing_faqs = existing.get("faqs") or []
    new_faqs = new.get("faqs") or []

    existing_by_question = {
        faq.get("question"): compact_whitespace(str(faq.get("answer", "")))
        for faq in existing_faqs
        if isinstance(faq, dict) and faq.get("question")
    }
    new_by_question = {
        faq.get("question"): compact_whitespace(str(faq.get("answer", "")))
        for faq in new_faqs
        if isinstance(faq, dict) and faq.get("question")
    }

    added_questions = [question for question in new_by_question if question not in existing_by_question]
    removed_questions = [question for question in existing_by_question if question not in new_by_question]
    updated_questions = [
        question
        for question in new_by_question
        if question in existing_by_question and new_by_question[question] != existing_by_question[question]
    ]

    return {
        "before_count": len(existing_by_question),
        "after_count": len(new_by_question),
        "added_questions": added_questions,
        "removed_questions": removed_questions,
        "updated_questions": updated_questions,
    }


def classify_change(existing: Dict[str, Any] | None, new: Dict[str, Any]) -> Dict[str, Any]:
    if existing is None:
        faq_changes = classify_faq_changes({}, new)
        return {
            "status": "added",
            "summary_changed": True,
            "faq_changed": bool(new.get("faqs")),
            "faq_changes": faq_changes,
        }

    existing_for_compare = copy.deepcopy(existing)
    new_for_compare = copy.deepcopy(new)

    existing_for_compare.pop("generated_at", None)
    new_for_compare.pop("generated_at", None)

    summary_changed = compact_whitespace(str(existing_for_compare.get("summary", ""))) != compact_whitespace(
        str(new_for_compare.get("summary", ""))
    )

    faq_changes = classify_faq_changes(existing_for_compare, new_for_compare)
    faq_changed = bool(
        faq_changes["added_questions"] or faq_changes["removed_questions"] or faq_changes["updated_questions"]
    )

    status = "updated" if existing_for_compare != new_for_compare else "unchanged"
    return {
        "status": status,
        "summary_changed": summary_changed,
        "faq_changed": faq_changed,
        "faq_changes": faq_changes,
    }


def report_path_for_output(path: Path) -> str:
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def build_run_report(
    args: argparse.Namespace,
    processed_paths: Sequence[Path],
    per_path_results: Sequence[Dict[str, Any]],
) -> Dict[str, Any]:
    totals = {
        "processed": len(processed_paths),
        "added": sum(1 for result in per_path_results if result["status"] == "added"),
        "updated": sum(1 for result in per_path_results if result["status"] == "updated"),
        "unchanged": sum(1 for result in per_path_results if result["status"] == "unchanged"),
        "skipped": sum(1 for result in per_path_results if result["status"] == "skipped"),
        "errors": sum(1 for result in per_path_results if result["status"] == "error"),
        "removed": 0,
    }

    return {
        "timestamp": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "mode": "write" if args.write else "dry-run",
        "require_enable_flag": not args.allow_unflagged,
        "path_filter": args.path_filter or "",
        "limit": args.limit,
        "run_url": args.run_url or "",
        "git_ref": args.git_ref or "",
        "git_sha": args.git_sha or "",
        "actor": args.actor or "",
        "template_version": TEMPLATE_VERSION,
        "totals": totals,
        "paths": per_path_results,
    }


def write_report(report_file: Path, run_report: Dict[str, Any], history_limit: int) -> None:
    report_file.parent.mkdir(parents=True, exist_ok=True)

    existing_history: List[Dict[str, Any]] = []
    if report_file.exists():
        try:
            current = yaml.safe_load(report_file.read_text(encoding="utf-8")) or {}
            existing_history = current.get("history", []) or []
        except Exception:
            existing_history = []

    history = [copy.deepcopy(run_report)] + existing_history
    history = history[:history_limit]

    payload = {
        "latest_run": copy.deepcopy(run_report),
        "history": history,
    }

    report_text = yaml.dump(
        payload,
        Dumper=ReadableDumper,
        sort_keys=False,
        allow_unicode=True,
        width=100,
        default_flow_style=False,
    )
    report_file.write_text(report_text, encoding="utf-8")


def print_result_summary(run_report: Dict[str, Any]) -> None:
    totals = run_report["totals"]
    print(
        "Processed {processed} Learning Paths: "
        "{added} added, {updated} updated, {unchanged} unchanged, {errors} errors.".format(**totals)
    )
    for result in run_report["paths"]:
        status = result["status"]
        print(f"- {status.upper():9s} {result['path']}")


def select_learning_paths(args: argparse.Namespace) -> List[Path]:
    explicit_paths = normalize_path_filter(args.path_filter) if args.path_filter else []
    selected = explicit_paths or discover_learning_path_indexes()
    filtered: List[Path] = []

    for index_path in selected:
        doc = read_markdown_document(index_path)
        if is_draft(doc):
            continue
        if not args.allow_unflagged and not has_enable_flag(doc):
            continue
        filtered.append(index_path)

    if not explicit_paths and args.limit > 0:
        filtered = filtered[: args.limit]

    return filtered


def process_learning_path(index_path: Path, args: argparse.Namespace) -> Dict[str, Any]:
    try:
        doc = read_markdown_document(index_path)
        steps = load_steps(index_path)
        existing_generated = doc.metadata.get(GENERATED_KEY)
        if existing_generated is not None and not isinstance(existing_generated, dict):
            raise ValueError(f"{GENERATED_KEY} in {index_path} must be a mapping when present.")

        new_generated = build_generated_block(doc.metadata, steps)
        change = classify_change(existing_generated, new_generated)

        updated_front_matter = insert_or_replace_managed_block(doc.front_matter_text, new_generated)
        updated_markdown = rebuild_markdown(doc, updated_front_matter)
        changed_on_disk = updated_markdown != doc.raw_text

        if args.write and changed_on_disk:
            index_path.write_text(updated_markdown, encoding="utf-8")

        preview_summary = compact_whitespace(strip_markdown_links(str(new_generated.get("summary", ""))))
        preview_summary = preview_summary[:200] + ("..." if len(preview_summary) > 200 else "")

        return {
            "path": report_path_for_output(index_path),
            "status": change["status"] if changed_on_disk else "unchanged",
            "changed_on_disk": changed_on_disk,
            "summary_changed": change["summary_changed"],
            "faq_changed": change["faq_changed"],
            "faq_changes": change["faq_changes"],
            "summary_preview": preview_summary,
            "source_hash": new_generated["source_hash"],
        }
    except Exception as exc:
        return {
            "path": report_path_for_output(index_path),
            "status": "error",
            "error": str(exc),
        }


def main() -> int:
    args = parse_args()
    selected_paths = select_learning_paths(args)

    if not selected_paths:
        print("No Learning Paths matched the current selection rules.")
        run_report = build_run_report(args, [], [])
        if not args.no_write_report:
            write_report(Path(args.report_file), run_report, args.history_limit)
            print(f"Wrote report to {report_path_for_output(Path(args.report_file))}")
        return 0

    results = [process_learning_path(path, args) for path in selected_paths]
    run_report = build_run_report(args, selected_paths, results)

    if not args.no_write_report:
        write_report(Path(args.report_file), run_report, args.history_limit)
        print(f"Wrote report to {report_path_for_output(Path(args.report_file))}")

    print_result_summary(run_report)

    if run_report["totals"]["errors"] > 0:
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
