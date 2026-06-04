#!/usr/bin/env python3

"""
Generate summary and FAQ content for Learning Path _index.md files.

This script uses an OpenAI-compatible endpoint to generate AI-assisted content.

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
      template_version: summary-faq-v3
      generated_at: "2026-05-06T19:40:00Z"
      generator: ai
      ai_assisted: true
      ai_review_required: true
      model: "..."
      prompt_template: summary-faq-v3
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
import os
import re
import ssl
import sys
import time
import urllib.error
import urllib.request
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Sequence

import yaml


REPO_ROOT = Path(__file__).resolve().parent.parent
LEARNING_PATH_ROOT = REPO_ROOT / "content" / "learning-paths"
DEFAULT_REPORT_PATH = REPO_ROOT / "reports" / "generated-summary-faq" / "latest-run.yml"
DEFAULT_PROMPT_DIR = REPO_ROOT / "tools" / "prompts"
DEFAULT_OPENAI_BASE_URL = "https://openai-api-proxy.geo.arm.com/api/providers/openai/v1/responses/"
DEFAULT_OPENAI_MODEL = "gpt-4.1-mini"
DEFAULT_OPENAI_TIMEOUT = 120
DEFAULT_OPENAI_RETRIES = 2
DEFAULT_PROMPT_STEP_LIMIT = 8
DEFAULT_PROMPT_EXCERPT_CHARS = 900

ENABLE_FLAG = "generate_summary_faq"
RERUN_SUMMARY_FLAG = "rerun_summary"
RERUN_FAQS_FLAG = "rerun_faqs"

GENERATED_KEY = "generated_summary_faq"
MANAGED_START = "# START generated_summary_faq"
MANAGED_END = "# END generated_summary_faq"

TEMPLATE_VERSION = "summary-faq-v3"
PROMPT_TEMPLATE_VERSION = "summary-faq-v3"
DEFAULT_HISTORY_LIMIT = 20

SUMMARY_SOURCE_HASH_KEY = "summary_source_hash"
SUMMARY_GENERATED_AT_KEY = "summary_generated_at"
FAQ_SOURCE_HASH_KEY = "faq_source_hash"
FAQ_GENERATED_AT_KEY = "faq_generated_at"

SUMMARY_ACTIONS = (
    "created",
    "repaired_missing",
    "rerun_requested",
    "generator_changed",
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
    "generator_changed",
    "summary_drift_detected",
    "faq_drift_detected",
    "rerun_flags_reset",
)
CHANGE_ACTIONS = {"created", "repaired_missing", "rerun_requested", "generator_changed"}


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
        "--category",
        default="",
        help="Optional top-level Learning Path category slug, for example servers-and-cloud-computing.",
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
        "--openai-base-url",
        default=os.getenv("OPENAI_BASE_URL", DEFAULT_OPENAI_BASE_URL),
        help="OpenAI-compatible Responses endpoint URL. Defaults to Arm's OpenAI proxy.",
    )
    parser.add_argument(
        "--openai-model",
        default=os.getenv("OPENAI_MODEL", DEFAULT_OPENAI_MODEL),
        help="Model or deployment name exposed by the configured OpenAI-compatible endpoint.",
    )
    parser.add_argument(
        "--openai-timeout",
        type=int,
        default=int(os.getenv("OPENAI_TIMEOUT", DEFAULT_OPENAI_TIMEOUT)),
        help="Seconds to wait for each AI endpoint response before retrying.",
    )
    parser.add_argument(
        "--openai-retries",
        type=int,
        default=int(os.getenv("OPENAI_RETRIES", DEFAULT_OPENAI_RETRIES)),
        help="Number of retries for transient AI endpoint timeout/network errors.",
    )
    parser.add_argument(
        "--openai-ca-bundle",
        default=os.getenv("OPENAI_CA_BUNDLE", os.getenv("SSL_CERT_FILE", "")),
        help="Optional CA bundle file for the OpenAI-compatible endpoint.",
    )
    parser.add_argument(
        "--openai-insecure-skip-verify",
        action="store_true",
        default=as_bool(os.getenv("OPENAI_INSECURE_SKIP_VERIFY", "")),
        help="Skip TLS certificate verification for local endpoint testing only.",
    )
    parser.add_argument(
        "--prompt-dir",
        default=str(DEFAULT_PROMPT_DIR),
        help="Directory containing summary/FAQ system and user prompt templates.",
    )
    parser.add_argument(
        "--prompt-step-limit",
        type=int,
        default=int(os.getenv("SUMMARY_FAQ_PROMPT_STEP_LIMIT", DEFAULT_PROMPT_STEP_LIMIT)),
        help="Maximum number of Learning Path step excerpts included in each AI prompt.",
    )
    parser.add_argument(
        "--prompt-excerpt-chars",
        type=int,
        default=int(os.getenv("SUMMARY_FAQ_PROMPT_EXCERPT_CHARS", DEFAULT_PROMPT_EXCERPT_CHARS)),
        help="Maximum characters included from each step excerpt in each AI prompt.",
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
        "--markdown-report-file",
        default="",
        help="Optional Markdown report file with tables for local review.",
    )
    parser.add_argument(
        "--log-file",
        default="",
        help="Optional text file that captures progress, errors, and summary output for this run.",
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
    parser.add_argument(
        "--quiet-progress",
        action="store_true",
        help="Hide per-Learning Path progress output.",
    )

    args = parser.parse_args()

    if args.write and args.dry_run:
        parser.error("Use either --write or --dry-run, not both.")
    if args.path_filter and args.category:
        parser.error("Use either --path-filter or --category, not both.")
    if not args.write and not args.dry_run:
        args.dry_run = True

    return args


def append_log_line(log_file: str, message: str) -> None:
    if not log_file:
        return

    path = Path(log_file)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as log:
        log.write(message + "\n")


def emit(args: argparse.Namespace, message: str, flush: bool = False) -> None:
    print(message, flush=flush)
    append_log_line(args.log_file, message)


def initialize_log(args: argparse.Namespace) -> None:
    if not args.log_file:
        return

    path = Path(args.log_file)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "\n".join(
            [
                "Generate summary/FAQ local run",
                f"timestamp: {current_timestamp()}",
                f"mode: {'write' if args.write else 'dry-run'}",
                f"openai_base_url: {args.openai_base_url}",
                f"openai_model: {args.openai_model}",
                f"category: {args.category or ''}",
                f"path_filter: {args.path_filter or ''}",
                "",
            ]
        ),
        encoding="utf-8",
    )


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


def discover_category_indexes(category: str) -> List[Path]:
    category_slug = category.strip().strip("/")
    if not category_slug:
        return []

    category_path = LEARNING_PATH_ROOT / category_slug
    if not category_path.is_dir():
        raise FileNotFoundError(f"Could not resolve Learning Path category from '{category}'.")

    indexes = sorted(category_path.glob("*/_index.md"))
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


def strip_markdown_links(text: str) -> str:
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    return compact_whitespace(text)


def preview_text(value: str, limit: int = 200) -> str:
    preview = compact_whitespace(strip_markdown_links(str(value or "")))
    if len(preview) > limit:
        preview = preview[:limit] + "..."
    return preview


def prompt_metadata(metadata: Dict[str, Any]) -> Dict[str, Any]:
    keys = (
        "title",
        "description",
        "who_is_this_for",
        "learning_objectives",
        "prerequisites",
        "skilllevels",
        "subjects",
        "tools_software_languages",
        "operatingsystems",
        "armips",
        "cloud_service_providers",
        "minutes_to_complete",
    )
    return {key: metadata.get(key) for key in keys if metadata.get(key) not in (None, "", [])}


def prompt_steps(
    steps: Sequence[StepPage],
    step_limit: int = DEFAULT_PROMPT_STEP_LIMIT,
    excerpt_chars: int = DEFAULT_PROMPT_EXCERPT_CHARS,
) -> List[Dict[str, Any]]:
    prompt_pages: List[Dict[str, Any]] = []
    safe_step_limit = max(1, step_limit)
    safe_excerpt_chars = max(200, excerpt_chars)

    for step in steps:
        if step.path.name in {"_index.md", "_next-steps.md", "_review.md", "_demo.md"}:
            continue
        if as_bool(step.metadata.get("hide_from_navpane", False)):
            continue

        excerpt = compact_whitespace(strip_markdown_links(step.content))
        prompt_pages.append(
            {
                "file": step.path.name,
                "title": step.title,
                "weight": step.weight,
                "excerpt": excerpt[:safe_excerpt_chars],
            }
        )

    return prompt_pages[:safe_step_limit]


def build_learning_path_prompt_context(
    metadata: Dict[str, Any],
    steps: Sequence[StepPage],
    args: argparse.Namespace,
) -> Dict[str, Any]:
    return {
        "metadata": prompt_metadata(metadata),
        "steps": prompt_steps(
            steps,
            step_limit=args.prompt_step_limit,
            excerpt_chars=args.prompt_excerpt_chars,
        ),
        "output_requirements": {
            "summary": "One concise paragraph, approximately 70-120 words.",
            "faqs": "Exactly 5 FAQs. Each answer should be 1-3 sentences.",
            "voice": "Clear, specific, technically accurate, and aligned with Arm developer education content.",
            "review": "Output will be reviewed by human contributors before publication.",
        },
    }


def read_prompt_template(prompt_dir: Path, filename: str) -> str:
    path = prompt_dir / filename
    if not path.exists():
        raise FileNotFoundError(f"Prompt template not found: {path}")
    return path.read_text(encoding="utf-8").strip()


def render_user_prompt(template: str, context: Dict[str, Any]) -> str:
    context_json = json.dumps(context, ensure_ascii=False, indent=2, sort_keys=True)
    return template.replace("{{ learning_path_context }}", context_json)


def extract_json_object(text: str) -> Dict[str, Any]:
    cleaned = text.strip()
    fenced_match = re.search(r"```(?:json)?\s*(.*?)\s*```", cleaned, re.DOTALL)
    if fenced_match:
        cleaned = fenced_match.group(1).strip()

    try:
        payload = json.loads(cleaned)
    except json.JSONDecodeError:
        start = cleaned.find("{")
        end = cleaned.rfind("}")
        if start == -1 or end == -1 or end <= start:
            raise
        payload = json.loads(cleaned[start : end + 1])

    if not isinstance(payload, dict):
        raise ValueError("AI response must be a JSON object.")
    return payload


def validate_ai_summary_faq(payload: Dict[str, Any]) -> Dict[str, Any]:
    summary = compact_whitespace(str(payload.get("summary", "")))
    raw_faqs = payload.get("faqs")

    if not summary:
        raise ValueError("AI response did not include a non-empty summary.")
    if not isinstance(raw_faqs, list) or not raw_faqs:
        raise ValueError("AI response did not include a non-empty faqs list.")

    faqs: List[Dict[str, str]] = []
    for raw_faq in raw_faqs:
        if not isinstance(raw_faq, dict):
            continue
        question = compact_whitespace(str(raw_faq.get("question", "")))
        answer = compact_whitespace(str(raw_faq.get("answer", "")))
        if question and answer:
            faqs.append({"question": question, "answer": answer})

    if len(faqs) != 5:
        raise ValueError(f"AI response must include exactly 5 valid FAQs; received {len(faqs)}.")

    return {
        "summary": summary,
        "faqs": faqs,
    }


def extract_response_text(response_payload: Dict[str, Any]) -> str:
    output_text = response_payload.get("output_text")
    if isinstance(output_text, str) and output_text.strip():
        return output_text

    output = response_payload.get("output")
    if isinstance(output, list):
        chunks: List[str] = []
        for item in output:
            if not isinstance(item, dict):
                continue
            content = item.get("content")
            if not isinstance(content, list):
                continue
            for content_item in content:
                if not isinstance(content_item, dict):
                    continue
                text = content_item.get("text")
                if isinstance(text, str):
                    chunks.append(text)
        if chunks:
            return "\n".join(chunks)

    choices = response_payload.get("choices")
    if isinstance(choices, list) and choices:
        message = choices[0].get("message") if isinstance(choices[0], dict) else None
        if isinstance(message, dict) and isinstance(message.get("content"), str):
            return message["content"]

    raise ValueError("Could not find text output in AI response.")


def build_ssl_context(ca_bundle: str = "", insecure_skip_verify: bool = False) -> ssl.SSLContext:
    if insecure_skip_verify:
        return ssl._create_unverified_context()
    if ca_bundle:
        return ssl.create_default_context(cafile=ca_bundle)
    return ssl.create_default_context()


def post_responses_request(
    endpoint: str,
    api_key: str,
    payload: Dict[str, Any],
    ca_bundle: str = "",
    insecure_skip_verify: bool = False,
    timeout: int = DEFAULT_OPENAI_TIMEOUT,
    retries: int = DEFAULT_OPENAI_RETRIES,
) -> Dict[str, Any]:
    request = urllib.request.Request(
        endpoint,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )

    ssl_context = build_ssl_context(ca_bundle=ca_bundle, insecure_skip_verify=insecure_skip_verify)
    max_attempts = max(1, retries + 1)
    last_error: Exception | None = None

    for attempt in range(1, max_attempts + 1):
        try:
            with urllib.request.urlopen(request, timeout=timeout, context=ssl_context) as response:
                body = response.read().decode("utf-8")
            break
        except urllib.error.HTTPError as exc:
            error_body = exc.read().decode("utf-8", errors="replace")
            if exc.code not in {408, 429, 500, 502, 503, 504} or attempt == max_attempts:
                raise RuntimeError(f"AI endpoint returned HTTP {exc.code}: {error_body}") from exc
            last_error = RuntimeError(f"AI endpoint returned HTTP {exc.code}: {error_body}")
        except TimeoutError as exc:
            if attempt == max_attempts:
                raise RuntimeError(f"AI endpoint timed out after {timeout} seconds.") from exc
            last_error = exc
        except urllib.error.URLError as exc:
            reason = str(exc.reason)
            if "CERTIFICATE_VERIFY_FAILED" in reason:
                raise RuntimeError(
                    "Could not verify the AI endpoint TLS certificate. "
                    "Set OPENAI_CA_BUNDLE to your Arm corporate CA bundle, or use "
                    "OPENAI_INSECURE_SKIP_VERIFY=true for local testing only. "
                    f"Original error: {reason}"
                ) from exc
            if attempt == max_attempts:
                raise RuntimeError(f"Could not reach AI endpoint: {exc.reason}") from exc
            last_error = exc

        sleep_seconds = min(20, 2 ** (attempt - 1))
        time.sleep(sleep_seconds)
    else:
        raise RuntimeError(f"AI endpoint failed after {max_attempts} attempts: {last_error}")

    try:
        parsed = json.loads(body)
    except json.JSONDecodeError as exc:
        raise ValueError(f"AI endpoint returned non-JSON response: {body[:500]}") from exc

    if not isinstance(parsed, dict):
        raise ValueError("AI endpoint response must be a JSON object.")

    return parsed


def generate_ai_summary_faq(metadata: Dict[str, Any], steps: Sequence[StepPage], args: argparse.Namespace) -> Dict[str, Any]:
    api_key = os.getenv("OPENAI_API_KEY", "").strip()
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY is required for AI-assisted summary/FAQ generation.")

    prompt_dir = Path(args.prompt_dir)
    system_prompt = read_prompt_template(prompt_dir, "summary_faq_system.md")
    user_template = read_prompt_template(prompt_dir, "summary_faq_user.md")
    user_prompt = render_user_prompt(
        user_template,
        build_learning_path_prompt_context(metadata, steps, args),
    )

    prompt_input = (
        f"{system_prompt}\n\n"
        "Use the following Learning Path context to produce the required JSON response.\n\n"
        f"{user_prompt}"
    )

    response_payload = post_responses_request(
        endpoint=args.openai_base_url,
        api_key=api_key,
        payload={
            "model": args.openai_model,
            "input": prompt_input,
        },
        ca_bundle=args.openai_ca_bundle,
        insecure_skip_verify=args.openai_insecure_skip_verify,
        timeout=args.openai_timeout,
        retries=args.openai_retries,
    )

    content = extract_response_text(response_payload)
    return validate_ai_summary_faq(extract_json_object(content))


def build_desired_summary_faq(
    metadata: Dict[str, Any],
    steps: Sequence[StepPage],
    args: argparse.Namespace,
) -> Dict[str, Any]:
    return generate_ai_summary_faq(metadata, steps, args)


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
    model: str,
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
        "generator": "ai",
        "ai_assisted": True,
        "ai_review_required": True,
        "model": model,
        "prompt_template": PROMPT_TEMPLATE_VERSION,
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
        "ai_requests": 0,
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

        if result.get("ai_requested"):
            totals["ai_requests"] += 1

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
        "category": args.category or "",
        "limit": args.limit,
        "run_url": args.run_url or "",
        "git_ref": args.git_ref or "",
        "git_sha": args.git_sha or "",
        "actor": args.actor or "",
        "template_version": TEMPLATE_VERSION,
        "openai_base_url": args.openai_base_url,
        "openai_model": args.openai_model,
        "prompt_template": PROMPT_TEMPLATE_VERSION,
        "markdown_report_file": args.markdown_report_file or "",
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


def markdown_escape(value: Any) -> str:
    text = str(value if value is not None else "")
    return text.replace("|", "\\|").replace("\n", "<br>")


def markdown_metric_row(label: str, value: Any) -> str:
    return f"| {markdown_escape(label)} | {markdown_escape(value)} |"


def render_markdown_report(run_report: Dict[str, Any]) -> str:
    totals = run_report.get("totals", {})
    section_totals = run_report.get("section_totals", {})
    reason_totals = run_report.get("reason_totals", {})
    paths = run_report.get("paths", [])

    lines: List[str] = [
        "# Generate Summary/FAQ Report",
        "",
        f"Generated at: `{markdown_escape(run_report.get('timestamp', ''))}`",
        "",
        "| Field | Value |",
        "| --- | --- |",
        markdown_metric_row("Mode", run_report.get("mode", "")),
        markdown_metric_row("Require enable flag", run_report.get("require_enable_flag", "")),
        markdown_metric_row("Category", run_report.get("category", "") or "all"),
        markdown_metric_row("Path filter", run_report.get("path_filter", "") or "none"),
        markdown_metric_row("Limit", run_report.get("limit", 0)),
        markdown_metric_row("Model", run_report.get("openai_model", "")),
        markdown_metric_row("Prompt template", run_report.get("prompt_template", "")),
        "",
        "## Run Overview",
        "",
        "| Metric | Count |",
        "| --- | ---: |",
        markdown_metric_row("Processed", totals.get("processed", 0)),
        markdown_metric_row("Added", totals.get("added", 0)),
        markdown_metric_row("Updated", totals.get("updated", 0)),
        markdown_metric_row("Drift detected", totals.get("drift_detected", 0)),
        markdown_metric_row("Paths with drift", totals.get("paths_with_drift", 0)),
        markdown_metric_row("Skipped", totals.get("skipped", 0)),
        markdown_metric_row("Unchanged", totals.get("unchanged", 0)),
        markdown_metric_row("Errors", totals.get("errors", 0)),
        markdown_metric_row("AI requests", totals.get("ai_requests", 0)),
        markdown_metric_row("Summary changed", totals.get("summary_changed", 0)),
        markdown_metric_row("FAQs changed", totals.get("faq_changed", 0)),
        markdown_metric_row("Rerun flags reset", totals.get("rerun_flags_reset", 0)),
        "",
    ]

    for section_name, title in (("summary", "Summary Actions"), ("faqs", "FAQ Actions")):
        actions = section_totals.get(section_name, {})
        lines.extend(
            [
                f"## {title}",
                "",
                "| Action | Count |",
                "| --- | ---: |",
            ]
        )
        for action in SUMMARY_ACTIONS:
            lines.append(markdown_metric_row(action, actions.get(action, 0)))
        lines.append("")

    nonzero_reasons = [(reason, count) for reason, count in reason_totals.items() if count]
    if nonzero_reasons:
        lines.extend(["## Change Reasons", "", "| Reason | Count |", "| --- | ---: |"])
        for reason, count in nonzero_reasons:
            lines.append(markdown_metric_row(reason, count))
        lines.append("")

    interesting_paths = [
        entry
        for entry in paths
        if entry.get("status") != "unchanged" or entry.get("change_reasons") or entry.get("status") == "error"
    ]

    if interesting_paths:
        lines.extend(
            [
                "## Path Details",
                "",
                "| Path | Status | Summary | FAQs | Reasons | Notes |",
                "| --- | --- | --- | --- | --- | --- |",
            ]
        )
        for entry in interesting_paths:
            summary = entry.get("summary", {})
            faqs = entry.get("faqs", {})
            reasons = ", ".join(entry.get("change_reasons", [])) or "none"
            notes = ""
            if entry.get("status") == "error":
                notes = entry.get("error", "")
            elif entry.get("status") == "skipped":
                notes = entry.get("skip_reason", "")
            elif faqs:
                notes = f"FAQs {faqs.get('before_count', 0)} -> {faqs.get('after_count', 0)}"

            lines.append(
                "| `{path}` | {status} | {summary_action} | {faq_action} | {reasons} | {notes} |".format(
                    path=markdown_escape(entry.get("path", "")),
                    status=markdown_escape(entry.get("status", "")),
                    summary_action=markdown_escape(summary.get("action", "")),
                    faq_action=markdown_escape(faqs.get("action", "")),
                    reasons=markdown_escape(reasons),
                    notes=markdown_escape(notes),
                )
            )
        lines.append("")
    else:
        lines.extend(["## Path Details", "", "All processed Learning Paths were unchanged.", ""])

    changed_previews = [
        entry
        for entry in interesting_paths
        if entry.get("summary", {}).get("changed") or entry.get("faqs", {}).get("changed")
    ]
    if changed_previews:
        lines.extend(
            [
                "## Changed Content Preview",
                "",
                "| Path | Summary Preview | FAQ Change Details |",
                "| --- | --- | --- |",
            ]
        )
        for entry in changed_previews:
            summary = entry.get("summary", {})
            faqs = entry.get("faqs", {})
            details = faqs.get("change_details", {})
            faq_details = (
                f"before={details.get('before_count', 0)}, "
                f"after={details.get('after_count', 0)}, "
                f"added={len(details.get('added_questions', []))}, "
                f"removed={len(details.get('removed_questions', []))}, "
                f"updated={len(details.get('updated_questions', []))}"
            )
            lines.append(
                "| `{path}` | {summary_preview} | {faq_details} |".format(
                    path=markdown_escape(entry.get("path", "")),
                    summary_preview=markdown_escape(summary.get("preview_after", "")),
                    faq_details=markdown_escape(faq_details),
                )
            )
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def write_markdown_report(markdown_report_file: Path, run_report: Dict[str, Any]) -> None:
    markdown_report_file.parent.mkdir(parents=True, exist_ok=True)
    markdown_report_file.write_text(render_markdown_report(run_report), encoding="utf-8")


def print_result_summary(args: argparse.Namespace, run_report: Dict[str, Any]) -> None:
    totals = run_report["totals"]
    emit(
        args,
        "Processed {processed} Learning Paths: "
        "{added} added, {updated} updated, {drift_detected} drift detected, "
        "{paths_with_drift} paths with drift, "
        "{skipped} skipped, {unchanged} unchanged, {errors} errors, {ai_requests} AI requests.".format(**totals)
    )

    summary_actions = run_report["section_totals"]["summary"]
    faq_actions = run_report["section_totals"]["faqs"]
    emit(
        args,
        "Summary actions: "
        f"{summary_actions['created']} created, "
        f"{summary_actions['repaired_missing']} repaired_missing, "
        f"{summary_actions['rerun_requested']} rerun_requested, "
        f"{summary_actions['generator_changed']} generator_changed, "
        f"{summary_actions['drift_detected_preserved']} drift_detected_preserved."
    )
    emit(
        args,
        "FAQ actions: "
        f"{faq_actions['created']} created, "
        f"{faq_actions['repaired_missing']} repaired_missing, "
        f"{faq_actions['rerun_requested']} rerun_requested, "
        f"{faq_actions['generator_changed']} generator_changed, "
        f"{faq_actions['drift_detected_preserved']} drift_detected_preserved."
    )

    for result in run_report["paths"]:
        status = result["status"]
        summary_action = result.get("summary", {}).get("action", "")
        faq_action = result.get("faqs", {}).get("action", "")
        reasons = ", ".join(result.get("change_reasons", [])) or "none"
        line = f"- {status.upper():14s} {result['path']} | summary={summary_action} | faqs={faq_action} | reasons={reasons}"
        if status == "error":
            line += f" | error={result.get('error', 'Unknown error')}"
        if status == "skipped":
            line += f" | skip_reason={result.get('skip_reason', 'unknown')}"
        emit(args, line)


def candidate_learning_paths(args: argparse.Namespace) -> tuple[List[Path], bool]:
    explicit_paths = normalize_path_filter(args.path_filter) if args.path_filter else []
    if explicit_paths:
        return explicit_paths, True
    elif args.category:
        return discover_category_indexes(args.category), False
    return discover_learning_path_indexes(), False


def skipped_result(index_path: Path, reason: str) -> Dict[str, Any]:
    return {
        "path": report_path_for_output(index_path),
        "status": "skipped",
        "skip_reason": reason,
        "change_reasons": [reason],
        "ai_requested": False,
        "summary": {"action": "skipped"},
        "faqs": {"action": "skipped"},
    }


def selection_plan(args: argparse.Namespace) -> tuple[List[Path], List[Path], Dict[Path, Dict[str, Any]]]:
    candidates, explicit = candidate_learning_paths(args)
    selected: List[Path] = []
    skipped: Dict[Path, Dict[str, Any]] = {}

    for index_path in candidates:
        doc = read_markdown_document(index_path)
        if is_draft(doc):
            skipped[index_path] = skipped_result(index_path, "draft")
            continue
        if not args.allow_unflagged and not has_enable_flag(doc):
            skipped[index_path] = skipped_result(index_path, f"{ENABLE_FLAG}_false")
            continue
        selected.append(index_path)

    if not explicit and args.limit > 0 and len(selected) > args.limit:
        limited = set(selected[: args.limit])
        for index_path in selected[args.limit :]:
            skipped[index_path] = skipped_result(index_path, "limit")
        selected = [path for path in selected if path in limited]

    return candidates, selected, skipped


def select_learning_paths(args: argparse.Namespace) -> List[Path]:
    _, selected, _ = selection_plan(args)
    return selected


def process_learning_path(index_path: Path, args: argparse.Namespace) -> Dict[str, Any]:
    ai_requested = False
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

        existing_summary = extract_existing_summary(existing_generated)
        existing_faqs = extract_existing_faqs(existing_generated)
        existing_generator = compact_whitespace(str((existing_generated or {}).get("generator", "")))
        generator_changed = bool(existing_generated is not None and existing_generator != "ai")

        summary_missing_before = existing_generated is not None and not compact_whitespace(existing_summary)
        faqs_missing_before = existing_generated is not None and not existing_faqs
        summary_needs_generation = bool(
            existing_generated is None
            or generator_changed
            or summary_missing_before
            or rerun_summary_requested
        )
        faqs_needs_generation = bool(
            existing_generated is None
            or generator_changed
            or faqs_missing_before
            or rerun_faqs_requested
        )
        ai_requested = summary_needs_generation or faqs_needs_generation

        if ai_requested:
            desired_content = build_desired_summary_faq(doc.metadata, steps, args)
            desired_summary = desired_content["summary"]
            desired_faqs = desired_content["faqs"]
        else:
            desired_summary = existing_summary
            desired_faqs = existing_faqs

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
        if generator_changed:
            change_reasons.append("generator_changed")

        if existing_generated is None:
            summary_action = "created"
            summary_after = desired_summary
        elif generator_changed:
            summary_action = "generator_changed"
            summary_after = desired_summary
        elif summary_missing_before:
            summary_action = "repaired_missing"
            summary_after = desired_summary
        elif rerun_summary_requested:
            summary_action = "rerun_requested"
            summary_after = desired_summary
        else:
            summary_action = "unchanged"
            summary_after = existing_summary

        if existing_generated is None:
            faq_action = "created"
            faqs_after = desired_faqs
        elif generator_changed:
            faq_action = "generator_changed"
            faqs_after = desired_faqs
        elif faqs_missing_before:
            faq_action = "repaired_missing"
            faqs_after = desired_faqs
        elif rerun_faqs_requested:
            faq_action = "rerun_requested"
            faqs_after = desired_faqs
        else:
            faq_action = "unchanged"
            faqs_after = existing_faqs

        summary_changed = summaries_differ(existing_summary, summary_after)
        faq_change_details = classify_faq_changes(existing_faqs, faqs_after)
        faq_changed = faq_differences_exist(faq_change_details)

        summary_drift_detected = summary_action == "drift_detected_preserved"
        faq_generated_diff = classify_faq_changes(existing_faqs, desired_faqs) if ai_requested else {}
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
                model=args.openai_model,
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
            "ai_requested": ai_requested,
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
            "ai_requested": ai_requested,
            "error": str(exc),
        }


def main() -> int:
    args = parse_args()
    initialize_log(args)
    candidate_paths, selected_paths, skipped_results = selection_plan(args)

    if not args.quiet_progress:
        emit(
            args,
            "Selection summary: "
            f"{len(selected_paths)} selected, {len(skipped_results)} skipped, "
            f"{len(candidate_paths)} candidates.",
            flush=True,
        )

    if not selected_paths:
        emit(args, "No Learning Paths matched the current selection rules.")
        run_report = build_run_report(args, [], list(skipped_results.values()))
        if not args.no_write_report:
            write_report(Path(args.report_file), run_report, args.history_limit)
            emit(args, f"Wrote report to {report_path_for_output(Path(args.report_file))}")
        if args.markdown_report_file:
            write_markdown_report(Path(args.markdown_report_file), run_report)
            emit(args, f"Wrote Markdown report to {report_path_for_output(Path(args.markdown_report_file))}")
        return 0

    results = []
    selected_set = set(selected_paths)
    total_paths = len(candidate_paths)
    for index, path in enumerate(candidate_paths, start=1):
        if path in skipped_results:
            result = skipped_results[path]
            results.append(result)
            if not args.quiet_progress:
                emit(
                    args,
                    f"[{index}/{total_paths}] Skipping {report_path_for_output(path)} "
                    f"({result.get('skip_reason', 'unknown')})",
                    flush=True,
                )
            continue

        if path not in selected_set:
            continue

        if not args.quiet_progress:
            emit(args, f"[{index}/{total_paths}] Processing {report_path_for_output(path)}", flush=True)
        result = process_learning_path(path, args)
        results.append(result)
        if not args.quiet_progress and result.get("status") == "error":
            emit(args, f"[{index}/{total_paths}] ERROR {result.get('error', 'Unknown error')}", flush=True)

    run_report = build_run_report(args, selected_paths, results)

    if not args.no_write_report:
        write_report(Path(args.report_file), run_report, args.history_limit)
        emit(args, f"Wrote report to {report_path_for_output(Path(args.report_file))}")

    if args.markdown_report_file:
        write_markdown_report(Path(args.markdown_report_file), run_report)
        emit(args, f"Wrote Markdown report to {report_path_for_output(Path(args.markdown_report_file))}")

    print_result_summary(args, run_report)

    if run_report["totals"]["errors"] > 0:
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
