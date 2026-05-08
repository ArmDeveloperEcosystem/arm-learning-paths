#!/usr/bin/env python3

"""
Generate summary and FAQ content for Learning Path _index.md files.

This script is intentionally template-driven so it can run in CI without
external AI dependencies. It:

- selects eligible Learning Paths using a front-matter flag or explicit paths
- manages a `generated_summary_faq` front-matter block
- supports one-shot `rerun_summary` / `rerun_faqs` controls
- auto-repairs missing generated summary/FAQ sections
- reports section-level changes, drift, and reasons in a central YAML file

Managed front-matter contract:

    generate_summary_faq: true
    rerun_summary: false
    rerun_faqs: false

    # START generated_summary_faq
    generated_summary_faq:
      template_version: summary-faq-v2
      generated_at: "2026-05-06T19:40:00Z"
      generator: template
      source_hash: "..."
      summary_generated_at: "2026-05-06T19:40:00Z"
      summary_source_hash: "..."
      faq_generated_at: "2026-05-06T19:40:00Z"
      faq_source_hash: "..."
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
RERUN_SUMMARY_FLAG = "rerun_summary"
RERUN_FAQS_FLAG = "rerun_faqs"

GENERATED_KEY = "generated_summary_faq"
MANAGED_START = "# START generated_summary_faq"
MANAGED_END = "# END generated_summary_faq"

TEMPLATE_VERSION = "summary-faq-v2"
DEFAULT_HISTORY_LIMIT = 20

SUMMARY_SOURCE_HASH_KEY = "summary_source_hash"
SUMMARY_GENERATED_AT_KEY = "summary_generated_at"
FAQ_SOURCE_HASH_KEY = "faq_source_hash"
FAQ_GENERATED_AT_KEY = "faq_generated_at"

SUMMARY_ACTIONS = (
    "created",
    "repaired_missing",
    "rerun_requested",
    "drift_detected_preserved",
    "unchanged",
)
FAQ_ACTIONS = SUMMARY_ACTIONS
REASON_ORDER = (
    "initial_generation",
    "missing_summary",
    "missing_faqs",
    "rerun_summary",
    "rerun_faqs",
    "summary_drift_detected",
    "faq_drift_detected",
    "rerun_flags_reset",
)
CHANGE_ACTIONS = {"created", "repaired_missing", "rerun_requested"}


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


def current_timestamp() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


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


def as_bool(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        return value.strip().lower() in {"1", "true", "yes", "on"}
    return bool(value)


def has_enable_flag(doc: MarkdownDocument) -> bool:
    return as_bool(doc.metadata.get(ENABLE_FLAG))


def is_draft(doc: MarkdownDocument) -> bool:
    return as_bool(doc.metadata.get("draft", False))


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


def preview_text(value: str, limit: int = 200) -> str:
    preview = compact_whitespace(strip_markdown_links(str(value or "")))
    if len(preview) > limit:
        preview = preview[:limit] + "..."
    return preview


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
        and not as_bool(step.metadata.get("hide_from_navpane", False))
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
        and not as_bool(step.metadata.get("hide_from_navpane", False))
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


def extract_existing_summary(existing_generated: Dict[str, Any] | None) -> str:
    if not isinstance(existing_generated, dict):
        return ""
    value = existing_generated.get("summary", "")
    if value is None:
        return ""
    return str(value).strip()


def extract_existing_faqs(existing_generated: Dict[str, Any] | None) -> List[Dict[str, str]]:
    if not isinstance(existing_generated, dict):
        return []

    raw_faqs = existing_generated.get("faqs")
    if not isinstance(raw_faqs, list):
        return []

    normalized: List[Dict[str, str]] = []
    for raw_faq in raw_faqs:
        if not isinstance(raw_faq, dict):
            continue
        question = str(raw_faq.get("question", "")).strip()
        answer = str(raw_faq.get("answer", "")).strip()
        if question and answer:
            normalized.append({"question": question, "answer": answer})
    return normalized


def summaries_differ(existing: str, new: str) -> bool:
    return compact_whitespace(existing) != compact_whitespace(new)


def faq_mapping(faqs: Sequence[Dict[str, Any]]) -> Dict[str, str]:
    mapping: Dict[str, str] = {}
    for faq in faqs:
        if not isinstance(faq, dict):
            continue
        question = compact_whitespace(str(faq.get("question", "")))
        answer = compact_whitespace(str(faq.get("answer", "")))
        if question:
            mapping[question] = answer
    return mapping


def classify_faq_changes(existing_faqs: Sequence[Dict[str, Any]], new_faqs: Sequence[Dict[str, Any]]) -> Dict[str, Any]:
    existing_by_question = faq_mapping(existing_faqs)
    new_by_question = faq_mapping(new_faqs)

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


def faq_differences_exist(change_details: Dict[str, Any]) -> bool:
    return bool(
        change_details["added_questions"]
        or change_details["removed_questions"]
        or change_details["updated_questions"]
        or change_details["before_count"] != change_details["after_count"]
    )


def get_existing_section_source_hash(existing_generated: Dict[str, Any] | None, section: str) -> str:
    if not isinstance(existing_generated, dict):
        return ""

    key = SUMMARY_SOURCE_HASH_KEY if section == "summary" else FAQ_SOURCE_HASH_KEY
    value = compact_whitespace(str(existing_generated.get(key, "")))
    if value:
        return value

    return compact_whitespace(str(existing_generated.get("source_hash", "")))


def get_existing_section_generated_at(existing_generated: Dict[str, Any] | None, section: str) -> str:
    if not isinstance(existing_generated, dict):
        return ""

    key = SUMMARY_GENERATED_AT_KEY if section == "summary" else FAQ_GENERATED_AT_KEY
    value = compact_whitespace(str(existing_generated.get(key, "")))
    if value:
        return value

    return compact_whitespace(str(existing_generated.get("generated_at", "")))


def normalize_faqs_for_output(faqs: Sequence[Dict[str, Any]]) -> List[Dict[str, Any]]:
    wrapped_faqs: List[Dict[str, Any]] = []
    for faq in faqs:
        question = str(faq.get("question", "")).strip()
        answer = str(faq.get("answer", "")).strip()
        if not question or not answer:
            continue
        wrapped_faqs.append({"question": question, "answer": BlockString(answer)})
    return wrapped_faqs


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


def replace_top_level_scalar_line(front_matter_text: str, key: str, new_value: str) -> str:
    pattern = re.compile(rf"(?m)^{re.escape(key)}:\s*.*$")
    if not pattern.search(front_matter_text):
        return front_matter_text
    return pattern.sub(f"{key}: {new_value}", front_matter_text, count=1)


def rebuild_markdown(doc: MarkdownDocument, updated_front_matter_text: str) -> str:
    content = doc.content.lstrip("\n")
    return f"---\n{updated_front_matter_text.rstrip()}\n---\n\n{content}"


def report_path_for_output(path: Path) -> str:
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def build_section_output_metadata(
    existing_generated: Dict[str, Any] | None,
    current_source_hash: str,
    generated_at: str,
    section: str,
    action: str,
    section_matches_current: bool,
) -> Dict[str, str]:
    existing_source_hash = get_existing_section_source_hash(existing_generated, section)
    existing_generated_at = get_existing_section_generated_at(existing_generated, section)

    if action in CHANGE_ACTIONS:
        return {
            "source_hash": current_source_hash,
            "generated_at": generated_at,
        }

    if existing_source_hash:
        source_hash = existing_source_hash
    elif section_matches_current:
        source_hash = current_source_hash
    else:
        source_hash = ""

    if existing_generated_at:
        section_generated_at = existing_generated_at
    elif section_matches_current:
        section_generated_at = generated_at
    else:
        section_generated_at = ""

    return {
        "source_hash": source_hash,
        "generated_at": section_generated_at,
    }


def build_updated_generated_block(
    existing_generated: Dict[str, Any] | None,
    summary_after: str,
    faqs_after: Sequence[Dict[str, Any]],
    desired_summary: str,
    desired_faqs: Sequence[Dict[str, Any]],
    current_source_hash: str,
    generated_at: str,
    summary_action: str,
    faq_action: str,
) -> Dict[str, Any]:
    summary_matches_current = not summaries_differ(summary_after, desired_summary)
    faqs_match_current = not faq_differences_exist(classify_faq_changes(faqs_after, desired_faqs))

    summary_meta = build_section_output_metadata(
        existing_generated=existing_generated,
        current_source_hash=current_source_hash,
        generated_at=generated_at,
        section="summary",
        action=summary_action,
        section_matches_current=summary_matches_current,
    )
    faq_meta = build_section_output_metadata(
        existing_generated=existing_generated,
        current_source_hash=current_source_hash,
        generated_at=generated_at,
        section="faqs",
        action=faq_action,
        section_matches_current=faqs_match_current,
    )

    if summary_matches_current and faqs_match_current:
        top_level_source_hash = current_source_hash
    else:
        top_level_source_hash = compact_whitespace(str((existing_generated or {}).get("source_hash", ""))) or current_source_hash

    return {
        "template_version": TEMPLATE_VERSION,
        "generated_at": generated_at,
        "generator": "template",
        "source_hash": top_level_source_hash,
        SUMMARY_GENERATED_AT_KEY: summary_meta["generated_at"],
        SUMMARY_SOURCE_HASH_KEY: summary_meta["source_hash"],
        FAQ_GENERATED_AT_KEY: faq_meta["generated_at"],
        FAQ_SOURCE_HASH_KEY: faq_meta["source_hash"],
        "summary": BlockString(summary_after),
        "faqs": normalize_faqs_for_output(faqs_after),
    }


def build_result_status(
    existing_generated: Dict[str, Any] | None,
    changed_on_disk: bool,
    summary_drift_detected: bool,
    faq_drift_detected: bool,
) -> str:
    if existing_generated is None and changed_on_disk:
        return "added"
    if changed_on_disk:
        return "updated"
    if summary_drift_detected or faq_drift_detected:
        return "drift_detected"
    return "unchanged"


def zeroed_action_counts(actions: Sequence[str]) -> Dict[str, int]:
    return {action: 0 for action in actions}


def build_run_report(
    args: argparse.Namespace,
    processed_paths: Sequence[Path],
    per_path_results: Sequence[Dict[str, Any]],
) -> Dict[str, Any]:
    totals = {
        "processed": len(processed_paths),
        "added": 0,
        "updated": 0,
        "unchanged": 0,
        "drift_detected": 0,
        "paths_with_drift": 0,
        "skipped": 0,
        "errors": 0,
        "removed": 0,
        "summary_changed": 0,
        "faq_changed": 0,
        "rerun_flags_reset": 0,
    }
    section_totals = {
        "summary": zeroed_action_counts(SUMMARY_ACTIONS),
        "faqs": zeroed_action_counts(FAQ_ACTIONS),
    }
    reason_totals = {reason: 0 for reason in REASON_ORDER}

    for result in per_path_results:
        status = result.get("status", "error")
        totals_key = "errors" if status == "error" else status
        if totals_key in totals:
            totals[totals_key] += 1

        summary_result = result.get("summary", {})
        if summary_result.get("changed"):
            totals["summary_changed"] += 1
        summary_action = summary_result.get("action")
        if summary_action in section_totals["summary"]:
            section_totals["summary"][summary_action] += 1

        faq_result = result.get("faqs", {})
        if faq_result.get("changed"):
            totals["faq_changed"] += 1
        faq_action = faq_result.get("action")
        if faq_action in section_totals["faqs"]:
            section_totals["faqs"][faq_action] += 1

        if summary_result.get("drift_detected") or faq_result.get("drift_detected"):
            totals["paths_with_drift"] += 1

        rerun_flags_reset = result.get("rerun_flags_reset", [])
        if rerun_flags_reset:
            totals["rerun_flags_reset"] += 1

        for reason in result.get("change_reasons", []):
            if reason not in reason_totals:
                reason_totals[reason] = 0
            reason_totals[reason] += 1

    return {
        "timestamp": current_timestamp(),
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
        "section_totals": section_totals,
        "reason_totals": reason_totals,
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
        "{added} added, {updated} updated, {drift_detected} drift detected, "
        "{paths_with_drift} paths with drift, "
        "{unchanged} unchanged, {errors} errors.".format(**totals)
    )

    summary_actions = run_report["section_totals"]["summary"]
    faq_actions = run_report["section_totals"]["faqs"]
    print(
        "Summary actions: "
        f"{summary_actions['created']} created, "
        f"{summary_actions['repaired_missing']} repaired_missing, "
        f"{summary_actions['rerun_requested']} rerun_requested, "
        f"{summary_actions['drift_detected_preserved']} drift_detected_preserved."
    )
    print(
        "FAQ actions: "
        f"{faq_actions['created']} created, "
        f"{faq_actions['repaired_missing']} repaired_missing, "
        f"{faq_actions['rerun_requested']} rerun_requested, "
        f"{faq_actions['drift_detected_preserved']} drift_detected_preserved."
    )

    for result in run_report["paths"]:
        status = result["status"]
        summary_action = result.get("summary", {}).get("action", "")
        faq_action = result.get("faqs", {}).get("action", "")
        reasons = ", ".join(result.get("change_reasons", [])) or "none"
        print(f"- {status.upper():14s} {result['path']} | summary={summary_action} | faqs={faq_action} | reasons={reasons}")


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

        rerun_summary_requested = as_bool(doc.metadata.get(RERUN_SUMMARY_FLAG))
        rerun_faqs_requested = as_bool(doc.metadata.get(RERUN_FAQS_FLAG))

        generated_at = current_timestamp()
        current_source_hash = build_source_hash(doc.metadata, steps)
        desired_summary = build_summary(doc.metadata, steps)
        desired_faqs = build_faqs(doc.metadata, steps)

        existing_summary = extract_existing_summary(existing_generated)
        existing_faqs = extract_existing_faqs(existing_generated)

        summary_missing_before = existing_generated is not None and not compact_whitespace(existing_summary)
        faqs_missing_before = existing_generated is not None and not existing_faqs

        change_reasons: List[str] = []
        if existing_generated is None:
            change_reasons.append("initial_generation")

        if summary_missing_before:
            change_reasons.append("missing_summary")
        if faqs_missing_before:
            change_reasons.append("missing_faqs")

        if rerun_summary_requested:
            change_reasons.append("rerun_summary")
        if rerun_faqs_requested:
            change_reasons.append("rerun_faqs")

        if existing_generated is None:
            summary_action = "created"
            summary_after = desired_summary
        elif summary_missing_before:
            summary_action = "repaired_missing"
            summary_after = desired_summary
        elif rerun_summary_requested:
            summary_action = "rerun_requested"
            summary_after = desired_summary
        else:
            summary_after = existing_summary
            if summaries_differ(existing_summary, desired_summary):
                summary_action = "drift_detected_preserved"
                change_reasons.append("summary_drift_detected")
            else:
                summary_action = "unchanged"

        if existing_generated is None:
            faq_action = "created"
            faqs_after = desired_faqs
        elif faqs_missing_before:
            faq_action = "repaired_missing"
            faqs_after = desired_faqs
        elif rerun_faqs_requested:
            faq_action = "rerun_requested"
            faqs_after = desired_faqs
        else:
            faqs_after = existing_faqs
            if faq_differences_exist(classify_faq_changes(existing_faqs, desired_faqs)):
                faq_action = "drift_detected_preserved"
                change_reasons.append("faq_drift_detected")
            else:
                faq_action = "unchanged"

        summary_changed = summaries_differ(existing_summary, summary_after)
        faq_change_details = classify_faq_changes(existing_faqs, faqs_after)
        faq_changed = faq_differences_exist(faq_change_details)

        summary_drift_detected = summary_action == "drift_detected_preserved"
        faq_generated_diff = classify_faq_changes(existing_faqs, desired_faqs)
        faq_drift_detected = faq_action == "drift_detected_preserved"

        managed_block_updated = existing_generated is None or summary_action in CHANGE_ACTIONS or faq_action in CHANGE_ACTIONS
        rerun_flags_reset = []
        if rerun_summary_requested:
            rerun_flags_reset.append(RERUN_SUMMARY_FLAG)
        if rerun_faqs_requested:
            rerun_flags_reset.append(RERUN_FAQS_FLAG)
        if rerun_flags_reset:
            change_reasons.append("rerun_flags_reset")

        updated_front_matter = doc.front_matter_text
        summary_source_hash_after = get_existing_section_source_hash(existing_generated, "summary")
        summary_generated_at_after = get_existing_section_generated_at(existing_generated, "summary")
        faq_source_hash_after = get_existing_section_source_hash(existing_generated, "faqs")
        faq_generated_at_after = get_existing_section_generated_at(existing_generated, "faqs")
        template_version_after = compact_whitespace(str((existing_generated or {}).get("template_version", "")))

        if managed_block_updated:
            updated_generated = build_updated_generated_block(
                existing_generated=existing_generated,
                summary_after=summary_after,
                faqs_after=faqs_after,
                desired_summary=desired_summary,
                desired_faqs=desired_faqs,
                current_source_hash=current_source_hash,
                generated_at=generated_at,
                summary_action=summary_action,
                faq_action=faq_action,
            )
            updated_front_matter = insert_or_replace_managed_block(updated_front_matter, updated_generated)
            summary_source_hash_after = compact_whitespace(str(updated_generated.get(SUMMARY_SOURCE_HASH_KEY, "")))
            summary_generated_at_after = compact_whitespace(str(updated_generated.get(SUMMARY_GENERATED_AT_KEY, "")))
            faq_source_hash_after = compact_whitespace(str(updated_generated.get(FAQ_SOURCE_HASH_KEY, "")))
            faq_generated_at_after = compact_whitespace(str(updated_generated.get(FAQ_GENERATED_AT_KEY, "")))
            template_version_after = compact_whitespace(str(updated_generated.get("template_version", "")))

        if rerun_summary_requested:
            updated_front_matter = replace_top_level_scalar_line(updated_front_matter, RERUN_SUMMARY_FLAG, "false")
        if rerun_faqs_requested:
            updated_front_matter = replace_top_level_scalar_line(updated_front_matter, RERUN_FAQS_FLAG, "false")

        updated_markdown = rebuild_markdown(doc, updated_front_matter)
        changed_on_disk = updated_markdown != doc.raw_text

        if args.write and changed_on_disk:
            index_path.write_text(updated_markdown, encoding="utf-8")

        result_status = build_result_status(
            existing_generated=existing_generated,
            changed_on_disk=changed_on_disk,
            summary_drift_detected=summary_drift_detected,
            faq_drift_detected=faq_drift_detected,
        )

        return {
            "path": report_path_for_output(index_path),
            "status": result_status,
            "changed_on_disk": changed_on_disk,
            "managed_block_updated": managed_block_updated,
            "rerun_flags_reset": rerun_flags_reset,
            "change_reasons": change_reasons,
            "template_version_before": compact_whitespace(str((existing_generated or {}).get("template_version", ""))),
            "template_version_after": template_version_after,
            "summary": {
                "action": summary_action,
                "missing_before": summary_missing_before,
                "rerun_requested": rerun_summary_requested,
                "changed": summary_changed,
                "drift_detected": summary_drift_detected,
                "source_hash_before": get_existing_section_source_hash(existing_generated, "summary"),
                "source_hash_after": summary_source_hash_after,
                "current_source_hash": current_source_hash,
                "generated_at_before": get_existing_section_generated_at(existing_generated, "summary"),
                "generated_at_after": summary_generated_at_after,
                "preview_before": preview_text(existing_summary),
                "preview_after": preview_text(summary_after),
                "preview_generated": preview_text(desired_summary),
            },
            "faqs": {
                "action": faq_action,
                "missing_before": faqs_missing_before,
                "rerun_requested": rerun_faqs_requested,
                "changed": faq_changed,
                "drift_detected": faq_drift_detected,
                "source_hash_before": get_existing_section_source_hash(existing_generated, "faqs"),
                "source_hash_after": faq_source_hash_after,
                "current_source_hash": current_source_hash,
                "generated_at_before": get_existing_section_generated_at(existing_generated, "faqs"),
                "generated_at_after": faq_generated_at_after,
                "before_count": len(existing_faqs),
                "after_count": len(faqs_after),
                "generated_count": len(desired_faqs),
                "change_details": faq_change_details,
                "generated_diff": faq_generated_diff,
            },
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
