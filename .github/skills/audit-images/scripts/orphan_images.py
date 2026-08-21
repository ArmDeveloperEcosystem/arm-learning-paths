#!/usr/bin/env python3
"""Find broken image references and unreferenced tracked images.

The checker deliberately uses Git's tracked paths as the source of truth so
filename comparisons remain case-sensitive on every operating system.
"""

from __future__ import annotations

import argparse
import json
import posixpath
import re
import subprocess
import sys
import time
from collections import defaultdict
from dataclasses import asdict, dataclass
from pathlib import Path, PurePosixPath
from typing import Callable, Mapping, Sequence
from urllib.parse import quote, unquote, urlparse


DEFAULT_PATHS = ("content/learning-paths", "content/install-guides")
IMAGE_EXTENSIONS = {
    ".avif",
    ".bmp",
    ".gif",
    ".jpeg",
    ".jpg",
    ".png",
    ".svg",
    ".tif",
    ".tiff",
    ".webp",
}
GENERATED_BINARY_IMAGE_EXTENSIONS = IMAGE_EXTENSIONS - {".svg"}

MARKDOWN_LINK_START_RE = re.compile(r"(!?)\[([^\]]*)\]\(")
REFERENCE_DEFINITION_RE = re.compile(
    r"^\s*\[([^\]]+)\]:\s*(?:<([^>]+)>|(\S+))", re.MULTILINE
)
REFERENCE_IMAGE_RE = re.compile(r"!\[([^\]]*)\]\[([^\]]*)\]")
HTML_IMAGE_RE = re.compile(
    r"<img\b[^>]*?\b(?:src|data-src)\s*=\s*([\"'])(.*?)\1[^>]*>",
    re.IGNORECASE | re.DOTALL,
)
HUGO_IMAGE_RE = re.compile(
    r"\b(?:img_src|image|src)\s*=\s*([\"'])(.*?)\1", re.IGNORECASE
)
FRONT_MATTER_IMAGE_RE = re.compile(
    r"^\s*(?:cover|diagram|diagram_blowup|image|thumbnail)\s*:\s*"
    r"(?:[\"']([^\"']+)[\"']|(\S+))\s*$",
    re.IGNORECASE | re.MULTILINE,
)
LOCAL_IMAGE_TOKEN_RE = re.compile(
    r"(?<![A-Za-z0-9_.-])"
    r"((?:/|\./|\.\./)?[A-Za-z0-9_.-]+(?:/[A-Za-z0-9_.-]+)*"
    r"\.(?:avif|bmp|gif|jpe?g|png|svg|tiff?|webp))"
    r"(?:[?#][^\s\"'<>)]*)?",
    re.IGNORECASE,
)
GENERATED_IMAGE_TOKEN_RE = re.compile(
    r"(?P<target>"
    r"(?:(?:https?:)?//[^\s\"'<>]+?\.(?:avif|bmp|gif|jpe?g|png|svg|tiff?|webp)"
    r"|(?:/|\./|\.\./)?[A-Za-z0-9_.-]+(?:/[A-Za-z0-9_.-]+)*"
    r"\.(?:avif|bmp|gif|jpe?g|png|svg|tiff?|webp))"
    r"(?:[?#][^\s\"'<>)]*)?)",
    re.IGNORECASE,
)
FENCE_RE = re.compile(r"^\s*(`{3,}|~{3,})")
INLINE_CODE_RE = re.compile(r"(`+)(.+?)\1")
URL_SCHEME_RE = re.compile(r"^[A-Za-z][A-Za-z0-9+.-]*:")


@dataclass(frozen=True)
class Snapshot:
    files: dict[str, str]
    text: dict[str, str]
    scopes: tuple[str, ...] = DEFAULT_PATHS


@dataclass(frozen=True)
class Reference:
    source: str
    line: int
    target: str
    kind: str
    explicit: bool = True


@dataclass(frozen=True)
class Problem:
    kind: str
    path: str
    line: int = 0
    target: str = ""
    resolved: str = ""
    matches: tuple[str, ...] = ()
    replacement: str = ""
    detail: str = ""

    def identity(self) -> tuple:
        """Return a line-number-independent identity for problem deduplication."""
        if self.kind == "orphan":
            return (self.kind, self.path)
        return (
            self.kind,
            self.path,
            self.target,
            self.resolved,
            self.matches,
            self.replacement,
            self.detail,
        )


@dataclass(frozen=True)
class Change:
    kind: str
    path: str
    line: int = 0
    before: str = ""
    after: str = ""


@dataclass
class Analysis:
    tracked_images: int
    referenced_images: int
    orphan_images: list[str]
    safe_delete_images: list[str]
    needs_review_images: list[str]
    duplicate_orphans: dict[str, tuple[str, ...]]
    generated_site_checked: bool
    problems: list[Problem]

    def all_problems(self) -> list[Problem]:
        safe = set(self.safe_delete_images)
        orphan_problems: list[Problem] = []
        for path in self.orphan_images:
            matches = self.duplicate_orphans.get(path, ())
            if path not in safe:
                detail = "needs review because evidence is incomplete or ambiguous"
            elif matches:
                detail = (
                    "delete only this unreferenced path; byte-identical referenced "
                    "copies are kept"
                )
            else:
                detail = (
                    "not referenced in tracked source or the rendered site; "
                    "safe deletion proposal"
                )
            orphan_problems.append(
                Problem(
                    kind="orphan",
                    path=path,
                    matches=matches,
                    detail=detail,
                )
            )
        return sorted(
            self.problems + orphan_problems,
            key=problem_sort_key,
        )


def run_git(repo_root: Path, args: Sequence[str], *, text: bool = False) -> bytes | str:
    command = ["git", "-C", str(repo_root), *args]
    try:
        return subprocess.check_output(command, text=text)
    except subprocess.CalledProcessError as error:
        raise SystemExit(f"Git command failed: {' '.join(command)}") from error


def path_in_scopes(path: str, scopes: Sequence[str]) -> bool:
    return any(path == scope or path.startswith(scope.rstrip("/") + "/") for scope in scopes)


def is_image_path(path: str) -> bool:
    return PurePosixPath(path).suffix.lower() in IMAGE_EXTENSIONS


def is_probably_text(data: bytes) -> bool:
    return b"\0" not in data


def tracked_file_oids(repo_root: Path) -> dict[str, str]:
    """Return stage-zero tracked paths and blob IDs without reading file contents."""
    raw = run_git(repo_root, ["ls-files", "-s", "-z"])
    assert isinstance(raw, bytes)
    tracked: dict[str, str] = {}

    for record in raw.decode("utf-8").split("\0"):
        if not record:
            continue
        metadata, path = record.split("\t", 1)
        _mode, oid, stage = metadata.split()
        if stage != "0":
            continue
        tracked[path] = oid
    return tracked


def current_snapshot(repo_root: Path, scopes: Sequence[str]) -> Snapshot:
    tracked = tracked_file_oids(repo_root)
    files = {path: oid for path, oid in tracked.items() if path_in_scopes(path, scopes)}
    text_entries = [
        (path, oid) for path, oid in tracked.items() if not is_image_path(path)
    ]

    text_files: dict[str, str] = {}
    for path, oid in text_entries:
        file_path = repo_root / path
        try:
            data = file_path.read_bytes()
        except OSError:
            blob = run_git(repo_root, ["show", f":{path}"])
            assert isinstance(blob, bytes)
            data = blob
        if is_probably_text(data):
            text_files[path] = data.decode("utf-8", errors="replace")

    return Snapshot(files=files, text=text_files, scopes=tuple(scopes))


def mask_fenced_code(text: str) -> str:
    """Mask fenced code while preserving offsets and line numbers."""
    masked: list[str] = []
    active_marker = ""

    for line in text.splitlines(keepends=True):
        match = FENCE_RE.match(line)
        marker = match.group(1) if match else ""
        if not active_marker and marker:
            active_marker = marker
            masked.append(" " * (len(line) - line.count("\n")) + "\n" * line.count("\n"))
            continue
        if active_marker:
            masked.append(" " * (len(line) - line.count("\n")) + "\n" * line.count("\n"))
            if marker and marker[0] == active_marker[0] and len(marker) >= len(active_marker):
                active_marker = ""
            continue
        masked.append(line)

    joined = "".join(masked)
    return INLINE_CODE_RE.sub(lambda match: " " * len(match.group(0)), joined)


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def find_closing_parenthesis(text: str, start: int) -> int | None:
    depth = 1
    quote = ""
    escaped = False

    for index in range(start, len(text)):
        char = text[index]
        if escaped:
            escaped = False
            continue
        if char == "\\":
            escaped = True
            continue
        if quote:
            if char == quote:
                quote = ""
            continue
        if char in {'"', "'"}:
            quote = char
        elif char == "(":
            depth += 1
        elif char == ")":
            depth -= 1
            if depth == 0:
                return index
    return None


def parse_markdown_destination(value: str) -> tuple[str, str | None]:
    content = value.strip()
    if not content:
        return "", "missing image destination"

    if content.startswith("<"):
        closing = content.find(">")
        if closing < 0:
            return "", "unterminated angle-bracket destination"
        target = content[1:closing]
        remainder = content[closing + 1 :].strip()
    else:
        match = re.match(r"(?:\\.|\S)+", content)
        if not match:
            return "", "missing image destination"
        target = match.group(0)
        remainder = content[match.end() :].strip()

    if not remainder:
        return target, None

    valid_title = (
        len(remainder) >= 2
        and (
            (remainder[0] == remainder[-1] and remainder[0] in {'"', "'"})
            or (remainder[0] == "(" and remainder[-1] == ")")
        )
    )
    if not valid_title:
        return target, "invalid text after the image destination"
    return target, None


def extract_markdown_references(source: str, text: str) -> tuple[list[Reference], list[Problem]]:
    visible_text = mask_fenced_code(text)
    references: list[Reference] = []
    problems: list[Problem] = []

    for match in MARKDOWN_LINK_START_RE.finditer(visible_text):
        closing = find_closing_parenthesis(visible_text, match.end())
        source_line = line_number(visible_text, match.start())
        if closing is None:
            if match.group(1):
                line_end = visible_text.find("\n", match.end())
                if line_end < 0:
                    line_end = len(visible_text)
                probable_target, _error = parse_markdown_destination(
                    visible_text[match.end() : line_end]
                )
                problems.append(
                    Problem(
                        kind="malformed_markdown",
                        path=source,
                        line=source_line,
                        target=probable_target,
                        detail="image destination is not closed",
                    )
                )
            continue

        target, error = parse_markdown_destination(visible_text[match.end() : closing])
        target_is_image = bool(
            target and is_image_path(target.split("?", 1)[0].split("#", 1)[0])
        )
        if error and (match.group(1) or target_is_image):
            problems.append(
                Problem(
                    kind="malformed_markdown",
                    path=source,
                    line=source_line,
                    target=target,
                    detail=error,
                )
            )
        if target_is_image:
            references.append(
                Reference(
                    source=source,
                    line=source_line,
                    target=target,
                    kind="markdown_image" if match.group(1) else "markdown_link",
                )
            )

    definitions: dict[str, tuple[str, int]] = {}
    for match in REFERENCE_DEFINITION_RE.finditer(visible_text):
        target = match.group(2) or match.group(3) or ""
        definitions[match.group(1).strip().lower()] = (
            target,
            line_number(visible_text, match.start()),
        )
    for match in REFERENCE_IMAGE_RE.finditer(visible_text):
        label = (match.group(2) or match.group(1)).strip().lower()
        if label in definitions:
            target, _definition_line = definitions[label]
            references.append(
                Reference(
                    source=source,
                    line=line_number(visible_text, match.start()),
                    target=target,
                    kind="markdown_reference_image",
                )
            )

    for match in HTML_IMAGE_RE.finditer(visible_text):
        references.append(
            Reference(
                source=source,
                line=line_number(visible_text, match.start()),
                target=match.group(2),
                kind="html_image",
            )
        )

    for match in HUGO_IMAGE_RE.finditer(visible_text):
        references.append(
            Reference(
                source=source,
                line=line_number(visible_text, match.start()),
                target=match.group(2),
                kind="hugo_image",
            )
        )

    front_matter = extract_front_matter(text)
    if front_matter:
        for match in FRONT_MATTER_IMAGE_RE.finditer(front_matter):
            references.append(
                Reference(
                    source=source,
                    line=line_number(front_matter, match.start()) + 1,
                    target=match.group(1) or match.group(2),
                    kind="front_matter_image",
                )
            )

    return references, problems


def extract_front_matter(text: str) -> str:
    if not text.startswith("---"):
        return ""
    lines = text.splitlines(keepends=True)
    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            return "".join(lines[1:index])
    return ""


def extract_conservative_references(source: str, text: str) -> list[Reference]:
    """Reserve any exact local image path mentioned in tracked text.

    These references prevent unsafe deletion but do not produce missing-image
    findings because paths inside examples and commands may be generated later.
    """
    return [
        Reference(
            source=source,
            line=line_number(text, match.start()),
            target=match.group(1),
            kind="text_path",
            explicit=False,
        )
        for match in LOCAL_IMAGE_TOKEN_RE.finditer(text)
    ]


def normalize_target(source: str, target: str) -> str | None:
    value = target.strip().replace("\\ ", " ")
    if value.startswith("<") and value.endswith(">"):
        value = value[1:-1]
    parsed = urlparse(value)
    if parsed.scheme or value.startswith(("#", "$", "~")) or URL_SCHEME_RE.match(value):
        return None

    value = unquote(value.split("#", 1)[0].split("?", 1)[0])
    if not value or "\\" in value:
        return None

    if value.startswith("content/"):
        resolved = value
    elif value.startswith("/"):
        resolved = "content/" + value.lstrip("/")
    else:
        resolved = posixpath.join(posixpath.dirname(source), value)
    normalized = posixpath.normpath(resolved)
    if normalized == ".." or normalized.startswith("../"):
        return None
    return normalized


def suggested_missing_asset(source: str, resolved: str, assets: set[str]) -> str:
    """Return a unique nearby asset for an obviously mistyped reference.

    Suggestions stay inside the content unit containing the Markdown source.
    This repairs cases such as a wrong extension or an accidental site-root
    path without guessing between similarly named assets elsewhere.
    """
    source_directory = posixpath.dirname(source)
    nearby = [
        asset
        for asset in assets
        if asset.startswith(source_directory.rstrip("/") + "/")
    ]
    missing_name = PurePosixPath(resolved).name.casefold()
    same_name = [
        asset for asset in nearby if PurePosixPath(asset).name.casefold() == missing_name
    ]
    if len(same_name) == 1:
        return same_name[0]

    missing_stem = PurePosixPath(resolved).stem.casefold()
    same_stem = [
        asset for asset in nearby if PurePosixPath(asset).stem.casefold() == missing_stem
    ]
    return same_stem[0] if len(same_stem) == 1 else ""


def target_for_asset(
    source: str,
    original: str,
    asset: str,
    *,
    preserve_site_root: bool = False,
) -> str:
    """Format a tracked asset path for use from a source Markdown file."""
    suffix_match = re.search(r"[?#]", original)
    suffix = original[suffix_match.start() :] if suffix_match else ""
    original_path = original[: suffix_match.start()] if suffix_match else original

    if preserve_site_root and original_path.startswith("/") and asset.startswith("content/"):
        rendered = "/" + asset.removeprefix("content/")
    else:
        rendered = posixpath.relpath(asset, posixpath.dirname(source))
        if original_path.startswith(("./", "/")) and not rendered.startswith("."):
            rendered = "./" + rendered
    return rendered + suffix


MALFORMED_DUPLICATE_IMAGE_RE = re.compile(
    r"^(?P<indent>\s*)!\[(?P<alt>[^\]]+)\]\("
    r"(?P<target><[^>]+>|\S+)\s+"
    r"(?P<quote>[\"'])(?P<title>.*?)(?P=quote)"
    r"(?P<duplicated>.+)\]\((?P=target)\s+"
    r"(?P=quote)(?P=title)(?P=quote)\)(?P<trailing>\s*)$"
)


def repair_duplicated_image_line(line: str) -> str | None:
    """Repair the known duplicated-alt-text Markdown corruption pattern."""
    newline = "\n" if line.endswith("\n") else ""
    value = line[:-1] if newline else line
    match = MALFORMED_DUPLICATE_IMAGE_RE.fullmatch(value)
    if not match:
        return None
    quote = match.group("quote")
    return (
        f'{match.group("indent")}![{match.group("alt")}]'
        f'({match.group("target")} {quote}{match.group("title")}{quote})'
        f'{match.group("trailing")}{newline}'
    )


def normalize_generated_target(source: str, target: str) -> str | None:
    """Map an image URL in generated output back to a content repository path."""
    value = target.strip()
    parsed = urlparse(value if not value.startswith("//") else "https:" + value)
    if parsed.scheme:
        if parsed.scheme not in {"http", "https"}:
            return None
        value = parsed.path
    value = unquote(value.split("#", 1)[0].split("?", 1)[0])
    if not value or value.startswith("#"):
        return None
    if value.startswith("/"):
        public_path = value.lstrip("/")
    else:
        public_path = posixpath.join(posixpath.dirname(source), value)
    normalized = posixpath.normpath(public_path)
    if normalized == ".." or normalized.startswith("../"):
        return None
    return "content/" + normalized


def generated_site_references(
    site_root: Path,
    assets: set[str],
    progress: Callable[[str], None] | None = None,
) -> set[str]:
    """Return tracked content assets referenced by rendered site text."""
    if not site_root.is_dir():
        raise SystemExit(f"Generated site directory does not exist: {site_root}")

    by_casefold: dict[str, list[str]] = defaultdict(list)
    for asset in assets:
        by_casefold[asset.casefold()].append(asset)

    used: set[str] = set()
    found_html = False
    files_seen = 0
    text_files_scanned = 0
    for path in sorted(site_root.rglob("*")):
        if not path.is_file():
            continue
        files_seen += 1
        if progress and files_seen % 1000 == 0:
            progress(f"Examined {files_seen} rendered files...")
        if path.suffix.lower() == ".html":
            found_html = True
        if path.suffix.lower() in GENERATED_BINARY_IMAGE_EXTENSIONS:
            continue
        try:
            data = path.read_bytes()
        except OSError:
            continue
        if not is_probably_text(data):
            continue
        text_files_scanned += 1
        text = data.decode("utf-8", errors="replace")
        source = path.relative_to(site_root).as_posix()
        for match in GENERATED_IMAGE_TOKEN_RE.finditer(text):
            resolved = normalize_generated_target(source, match.group("target"))
            if not resolved:
                continue
            if resolved in assets:
                used.add(resolved)
            else:
                used.update(by_casefold.get(resolved.casefold(), []))
    if progress:
        progress(
            f"Rendered-site scan checked {text_files_scanned} text files "
            f"and skipped {files_seen - text_files_scanned} non-text files."
        )
    if not found_html:
        raise SystemExit(
            f"Generated site contains no HTML files; refusing confidence upgrade: {site_root}"
        )
    return used


def analyze(
    snapshot: Snapshot,
    generated_used: set[str] | None = None,
) -> Analysis:
    assets = {path for path in snapshot.files if is_image_path(path)}
    by_casefold: dict[str, list[str]] = defaultdict(list)
    for asset in assets:
        by_casefold[asset.casefold()].append(asset)

    used: set[str] = set()
    problems: list[Problem] = []
    seen_problems: set[tuple] = set()

    for source, text in snapshot.text.items():
        if path_in_scopes(source, snapshot.scopes):
            explicit_references, malformed = extract_markdown_references(source, text)
        else:
            explicit_references, malformed = [], []
        for problem in malformed:
            add_problem(problems, seen_problems, problem)

        references = explicit_references + extract_conservative_references(source, text)
        for reference in references:
            resolved = normalize_target(source, reference.target)
            if not resolved or not is_image_path(resolved):
                continue
            if not reference.explicit and not path_in_scopes(resolved, snapshot.scopes):
                continue
            if resolved in assets:
                used.add(resolved)
                continue

            case_matches = tuple(sorted(by_casefold.get(resolved.casefold(), [])))
            if case_matches:
                used.update(case_matches)
                if reference.explicit:
                    add_problem(
                        problems,
                        seen_problems,
                        Problem(
                            kind="case_mismatch",
                            path=source,
                            line=reference.line,
                            target=reference.target,
                            resolved=resolved,
                            matches=case_matches,
                        ),
                    )
                continue

            if reference.explicit:
                replacement = suggested_missing_asset(source, resolved, assets)
                add_problem(
                    problems,
                    seen_problems,
                    Problem(
                        kind="missing_image",
                        path=source,
                        line=reference.line,
                        target=reference.target,
                        resolved=resolved,
                        replacement=replacement,
                    ),
                )

    if generated_used is not None:
        used.update(generated_used & assets)

    orphan_images = sorted(assets - used)
    used_by_oid: dict[str, list[str]] = defaultdict(list)
    for path in used:
        used_by_oid[snapshot.files[path]].append(path)
    duplicate_orphans = {
        path: tuple(sorted(used_by_oid[snapshot.files[path]]))
        for path in orphan_images
        if snapshot.files[path] in used_by_oid
    }

    ambiguous_directories = {
        posixpath.dirname(problem.path).rstrip("/") + "/"
        for problem in problems
        if problem.kind == "missing_image" and not problem.replacement
    }
    ambiguous = {
        path
        for path in orphan_images
        if any(path.startswith(directory) for directory in ambiguous_directories)
    }
    ambiguous.update(
        problem.replacement
        for problem in problems
        if problem.kind == "missing_image" and problem.replacement in assets
    )
    if generated_used is None:
        safe_delete = set(duplicate_orphans) - ambiguous
    else:
        safe_delete = set(orphan_images) - ambiguous
    needs_review = set(orphan_images) - safe_delete

    return Analysis(
        tracked_images=len(assets),
        referenced_images=len(used),
        orphan_images=orphan_images,
        safe_delete_images=sorted(safe_delete),
        needs_review_images=sorted(needs_review),
        duplicate_orphans=duplicate_orphans,
        generated_site_checked=generated_used is not None,
        problems=sorted(problems, key=problem_sort_key),
    )


def apply_safe_reference_fixes(repo_root: Path, analysis: Analysis) -> list[Change]:
    """Apply only deterministic repairs and return the changes made."""
    by_source: dict[str, list[Problem]] = defaultdict(list)
    for problem in analysis.problems:
        if problem.kind in {"malformed_markdown", "case_mismatch", "missing_image"}:
            by_source[problem.path].append(problem)

    changes: list[Change] = []
    for source, problems in sorted(by_source.items()):
        source_path = repo_root / source
        lines = source_path.read_text(encoding="utf-8").splitlines(keepends=True)

        for problem in sorted(problems, key=lambda item: item.line, reverse=True):
            if problem.line < 1 or problem.line > len(lines):
                continue
            index = problem.line - 1
            original_line = lines[index]

            if problem.kind == "malformed_markdown":
                repaired = repair_duplicated_image_line(original_line)
                if repaired is None or repaired == original_line:
                    continue
                lines[index] = repaired
                changes.append(
                    Change(
                        kind="fixed_malformed_markdown",
                        path=source,
                        line=problem.line,
                        before=original_line.rstrip("\n"),
                        after=repaired.rstrip("\n"),
                    )
                )
                continue

            asset = ""
            preserve_site_root = False
            if problem.kind == "case_mismatch" and len(problem.matches) == 1:
                asset = problem.matches[0]
                preserve_site_root = True
            elif problem.kind == "missing_image" and problem.replacement:
                asset = problem.replacement
            if not asset:
                continue

            replacement_target = target_for_asset(
                source,
                problem.target,
                asset,
                preserve_site_root=preserve_site_root,
            )
            if original_line.count(problem.target) != 1:
                continue
            repaired = original_line.replace(problem.target, replacement_target, 1)
            if repaired == original_line:
                continue
            lines[index] = repaired
            changes.append(
                Change(
                    kind=(
                        "fixed_case_mismatch"
                        if problem.kind == "case_mismatch"
                        else "fixed_missing_reference"
                    ),
                    path=source,
                    line=problem.line,
                    before=problem.target,
                    after=replacement_target,
                )
            )

        source_path.write_text("".join(lines), encoding="utf-8")

    return sorted(changes, key=lambda change: (change.path, change.line, change.kind))


def delete_safe_images(
    repo_root: Path,
    paths: Sequence[str],
    tracked_paths: Sequence[str],
) -> list[Change]:
    """Remove safe candidates while preserving case-colliding worktree files."""
    if not paths:
        return []

    deleting = set(paths)
    tracked_by_casefold: dict[str, list[str]] = defaultdict(list)
    for path in tracked_paths:
        tracked_by_casefold[path.casefold()].append(path)

    index_only = [
        path
        for path in paths
        if any(
            other not in deleting
            for other in tracked_by_casefold.get(path.casefold(), [])
            if other != path
        )
    ]
    index_only_set = set(index_only)
    regular = [path for path in paths if path not in index_only_set]

    if regular:
        subprocess.check_call(["git", "-C", str(repo_root), "rm", "-q", "--", *regular])
    if index_only:
        subprocess.check_call(
            ["git", "-C", str(repo_root), "rm", "--cached", "-q", "--", *index_only]
        )

    return [
        Change(
            kind=(
                "removed_duplicate_index_entry"
                if path in index_only_set
                else "deleted_safe_orphan"
            ),
            path=path,
        )
        for path in paths
    ]


def add_problem(problems: list[Problem], seen: set[tuple], problem: Problem) -> None:
    occurrence = (problem.identity(), problem.line)
    if occurrence not in seen:
        seen.add(occurrence)
        problems.append(problem)


def problem_sort_key(problem: Problem) -> tuple:
    return (problem.kind, problem.path, problem.line, problem.target, problem.detail)


def needs_review_records(analysis: Analysis) -> list[dict[str, object]]:
    """Describe why each protected orphan needs human review."""
    records: list[dict[str, object]] = []
    missing = [problem for problem in analysis.problems if problem.kind == "missing_image"]

    for path in analysis.needs_review_images:
        related: list[dict[str, object]] = []
        for problem in missing:
            source_directory = posixpath.dirname(problem.path).rstrip("/") + "/"
            if problem.replacement == path:
                relationship = "unique nearby replacement"
            elif not problem.replacement and path.startswith(source_directory):
                relationship = "unresolved image in the same content directory"
            else:
                continue
            related.append(
                {
                    "source": problem.path,
                    "line": problem.line,
                    "target": problem.target,
                    "relationship": relationship,
                }
            )

        if any(item["relationship"] == "unique nearby replacement" for item in related):
            reason = "A missing image reference uniquely points to this nearby asset."
            recommendation = "Fix the related reference before considering deletion."
        elif related:
            reason = "An unresolved missing reference exists in the same content directory."
            recommendation = "Inspect the image and article to decide whether to link or delete it."
        elif not analysis.generated_site_checked:
            reason = "Rendered-site evidence is unavailable and this is not an exact duplicate."
            recommendation = "Run the full rendered audit before making a deletion decision."
        else:
            reason = "Available evidence is incomplete or ambiguous."
            recommendation = "Inspect the image and nearby content before changing it."

        records.append(
            {
                "path": path,
                "reason": reason,
                "recommendation": recommendation,
                "related_references": related,
            }
        )
    return records


def displayed_review_records(
    analysis: Analysis,
    records: Sequence[dict[str, object]],
) -> tuple[list[dict[str, object]], int]:
    """Separate actionable review details from candidates awaiting a full audit."""
    if analysis.generated_site_checked:
        return list(records), 0
    displayed = [record for record in records if record["related_references"]]
    return displayed, len(records) - len(displayed)


def analysis_json(
    analysis: Analysis,
    problems: Sequence[Problem],
    changes: Sequence[Change] = (),
    file_oids: Mapping[str, str] | None = None,
) -> str:
    safe_deletion_oids = {
        path: file_oids[path]
        for path in analysis.safe_delete_images
        if file_oids is not None and path in file_oids
    }
    return json.dumps(
        {
            "summary": {
                "tracked_images": analysis.tracked_images,
                "referenced_images": analysis.referenced_images,
                "orphan_images": len(analysis.orphan_images),
                "safe_delete_images": len(analysis.safe_delete_images),
                "needs_review_images": len(analysis.needs_review_images),
                "duplicate_orphans": len(analysis.duplicate_orphans),
                "generated_site_checked": analysis.generated_site_checked,
                "reported_problems": len(problems),
            },
            "safe_deletions": analysis.safe_delete_images,
            "safe_deletion_oids": safe_deletion_oids,
            "needs_review": needs_review_records(analysis),
            "problems": [asdict(problem) for problem in problems],
            "changes": [asdict(change) for change in changes],
        },
        indent=2,
        sort_keys=True,
    ) + "\n"


def cleanup_manifest_paths(
    baseline_path: Path,
    tracked_files: Mapping[str, str],
    scopes: Sequence[str],
) -> list[str]:
    """Validate and return rendered-safe paths whose image blobs are unchanged."""
    try:
        baseline = json.loads(baseline_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise SystemExit(f"Cannot read cleanup manifest {baseline_path}: {error}") from error
    if not isinstance(baseline, dict):
        raise SystemExit("Cleanup manifest must be a JSON object")

    errors: list[str] = []
    summary = baseline.get("summary")
    if not isinstance(summary, dict) or summary.get("generated_site_checked") is not True:
        errors.append("manifest was not produced by a rendered-site audit")

    raw_paths = baseline.get("safe_deletions")
    raw_oids = baseline.get("safe_deletion_oids")
    if not isinstance(raw_paths, list):
        errors.append("safe_deletions must be a list")
        raw_paths = []
    if not isinstance(raw_oids, dict):
        errors.append("safe_deletion_oids must be an object")
        raw_oids = {}

    paths: list[str] = []
    seen: set[str] = set()
    for raw_path in raw_paths:
        if not isinstance(raw_path, str):
            errors.append("safe_deletions contains a non-string path")
            continue
        path = PurePosixPath(raw_path)
        if path.is_absolute() or ".." in path.parts:
            errors.append(f"unsafe cleanup path: {raw_path}")
            continue
        normalized = path.as_posix()
        if normalized in seen:
            errors.append(f"duplicate cleanup path: {normalized}")
            continue
        seen.add(normalized)
        paths.append(normalized)

        if not path_in_scopes(normalized, scopes):
            errors.append(f"cleanup path is outside the requested scopes: {normalized}")
        if not is_image_path(normalized):
            errors.append(f"cleanup path is not a supported image: {normalized}")
        actual_oid = tracked_files.get(normalized)
        expected_oid = raw_oids.get(normalized)
        if actual_oid is None:
            errors.append(f"cleanup path is no longer tracked: {normalized}")
        elif not isinstance(expected_oid, str):
            errors.append(f"cleanup path has no audited blob ID: {normalized}")
        elif actual_oid != expected_oid:
            errors.append(f"cleanup path changed after the audit: {normalized}")

    extra_oids = sorted(set(raw_oids) - set(paths))
    if extra_oids:
        errors.append(
            "manifest contains blob IDs for paths outside safe_deletions: "
            + ", ".join(extra_oids)
        )
    if errors:
        raise SystemExit("Cleanup manifest validation failed:\n- " + "\n- ".join(errors))
    return paths


def verify_cleanup(
    repo_root: Path,
    baseline_path: Path,
    analysis: Analysis,
) -> list[str]:
    """Verify that a staged cleanup matches a rendered dry-run exactly."""
    try:
        baseline = json.loads(baseline_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        return [f"cannot read cleanup baseline {baseline_path}: {error}"]

    errors: list[str] = []
    if not baseline.get("summary", {}).get("generated_site_checked"):
        errors.append("cleanup baseline was not produced by a rendered-site audit")
    if not analysis.generated_site_checked:
        errors.append("post-deletion audit did not inspect a rendered site")

    expected = set(baseline.get("safe_deletions", []))
    raw = run_git(
        repo_root,
        [
            "diff",
            "--cached",
            "--name-only",
            "--diff-filter=D",
            "-z",
            "HEAD",
            "--",
            *DEFAULT_PATHS,
        ],
    )
    assert isinstance(raw, bytes)
    actual = {path for path in raw.decode("utf-8").split("\0") if path}

    missing = sorted(expected - actual)
    unexpected = sorted(actual - expected)
    if missing:
        errors.append("expected deletions are missing: " + ", ".join(missing))
    if unexpected:
        errors.append("unexpected deletions are staged: " + ", ".join(unexpected))

    before_non_orphans = {
        json.dumps(problem, sort_keys=True)
        for problem in baseline.get("problems", [])
        if problem.get("kind") != "orphan"
    }
    after_non_orphans = {
        json.dumps(asdict(problem), sort_keys=True)
        for problem in analysis.problems
        if problem.kind != "orphan"
    }
    introduced = sorted(after_non_orphans - before_non_orphans)
    if introduced:
        errors.append(
            f"cleanup introduced {len(introduced)} new non-orphan problem(s)"
        )
    if analysis.safe_delete_images:
        errors.append(
            f"cleanup left {len(analysis.safe_delete_images)} safe deletion(s) behind"
        )
    return errors


def analysis_text(
    analysis: Analysis,
    problems: Sequence[Problem],
    changes: Sequence[Change] = (),
) -> str:
    lines: list[str] = []
    if changes:
        lines.extend(["Applied changes", ""])
        for change in changes:
            location = change.path + (f":{change.line}" if change.line else "")
            message = f"- {change.kind}: {location}"
            if change.before or change.after:
                message += f" ({change.before} -> {change.after})"
            lines.append(message)
        lines.append("")

    lines.extend(
        [
            "Image integrity report",
            "",
            f"Tracked images: {analysis.tracked_images}",
            f"Referenced images: {analysis.referenced_images}",
            f"Current orphan candidates: {len(analysis.orphan_images)}",
            f"Safe automatic deletions: {len(analysis.safe_delete_images)}",
            f"Needs review: {len(analysis.needs_review_images)}",
            f"Exact duplicate orphans: {len(analysis.duplicate_orphans)}",
            "Generated site checked: "
            + ("yes" if analysis.generated_site_checked else "no"),
            f"All detected problems: {len(problems)}",
        ]
    )

    review_records = needs_review_records(analysis)
    displayed_records, awaiting_render = displayed_review_records(
        analysis,
        review_records,
    )
    if displayed_records:
        lines.extend(["", f"Current images needing review ({len(displayed_records)})"])
        for record in displayed_records:
            lines.append(f"- {record['path']}")
            lines.append(f"  Reason: {record['reason']}")
            for related in record["related_references"]:
                source = related["source"]
                line = related["line"]
                target = related["target"]
                relationship = related["relationship"]
                lines.append(
                    f"  Related reference: {source}:{line} -> {target} "
                    f"({relationship})"
                )
            lines.append(f"  Recommended action: {record['recommendation']}")
    if awaiting_render:
        lines.extend(
            [
                "",
                f"Awaiting full rendered classification: {awaiting_render}",
                "Run the full audit before reviewing these candidates individually.",
            ]
        )

    if not problems:
        lines.extend(["", "No actionable image-integrity problems found."])
        return "\n".join(lines) + "\n"

    grouped: dict[str, list[Problem]] = defaultdict(list)
    for problem in problems:
        grouped[problem.kind].append(problem)

    labels = {
        "case_mismatch": "Filename case mismatches",
        "malformed_markdown": "Malformed Markdown image references",
        "missing_image": "Missing referenced images",
        "orphan": "Unreferenced image candidates",
    }
    for kind in sorted(grouped):
        lines.extend(["", labels.get(kind, kind.replace("_", " ").title())])
        for problem in grouped[kind]:
            location = problem.path + (f":{problem.line}" if problem.line else "")
            message = location
            if problem.target:
                message += f" -> {problem.target}"
            if problem.matches:
                relationship = (
                    "referenced byte-identical copies kept"
                    if problem.kind == "orphan"
                    else "tracked as"
                )
                message += f" ({relationship} {', '.join(problem.matches)})"
            if problem.replacement:
                message += f" (safe replacement: {problem.replacement})"
            if problem.detail:
                message += f" ({problem.detail})"
            lines.append(f"- {message}")

    return "\n".join(lines) + "\n"


def github_file_link(
    repository_url: str,
    revision: str,
    path: str,
    line: int = 0,
) -> str:
    """Return a Markdown link to a repository file when GitHub context is available."""
    label = path + (f":{line}" if line else "")
    if not repository_url or not revision:
        return f"`{label}`"
    url = (
        f"{repository_url.rstrip('/')}/blob/{quote(revision, safe='')}/"
        f"{quote(path, safe='/')}"
    )
    if line:
        url += f"#L{line}"
    return f"[`{label}`]({url})"


def analysis_markdown(
    analysis: Analysis,
    problems: Sequence[Problem],
    changes: Sequence[Change] = (),
    repository_url: str = "",
    revision: str = "",
) -> str:
    """Return a GitHub-friendly report with clickable repository paths."""
    lines = [
        "### Audit report",
        "",
        "| Metric | Count |",
        "| --- | ---: |",
        f"| Tracked images | {analysis.tracked_images} |",
        f"| Referenced images | {analysis.referenced_images} |",
        f"| Current orphan candidates | {len(analysis.orphan_images)} |",
        f"| Safe automatic deletions | {len(analysis.safe_delete_images)} |",
        f"| Needs review | {len(analysis.needs_review_images)} |",
        f"| Exact duplicate orphans | {len(analysis.duplicate_orphans)} |",
        "| Generated site checked | "
        + ("yes" if analysis.generated_site_checked else "no")
        + " |",
        f"| All detected problems | {len(problems)} |",
    ]

    review_records = needs_review_records(analysis)
    displayed_records, awaiting_render = displayed_review_records(
        analysis,
        review_records,
    )
    if awaiting_render:
        lines.append(f"| Awaiting full rendered classification | {awaiting_render} |")
    if displayed_records:
        lines.extend(
            [
                "",
                f"### Current images needing review ({len(displayed_records)})",
                "",
            ]
        )
        for record in displayed_records:
            path = str(record["path"])
            lines.append(f"- {github_file_link(repository_url, revision, path)}")
            lines.append(f"  - **Why:** {record['reason']}")
            for related in record["related_references"]:
                source = str(related["source"])
                line = int(related["line"])
                target = related["target"]
                relationship = related["relationship"]
                source_link = github_file_link(
                    repository_url,
                    revision,
                    source,
                    line,
                )
                lines.append(
                    f"  - **Related reference:** {source_link} requests `{target}` "
                    f"({relationship})."
                )
            lines.append(f"  - **Recommended action:** {record['recommendation']}")
    if awaiting_render:
        lines.extend(
            [
                "",
                f"> **{awaiting_render} additional candidates** are awaiting rendered-site "
                "evidence. Run the full audit before reviewing them individually.",
            ]
        )

    if changes:
        lines.extend(["", "### Applied changes", ""])
        for change in changes:
            link = github_file_link(
                repository_url,
                revision,
                change.path,
                change.line,
            )
            lines.append(f"- `{change.kind}`: {link}")

    lines.extend(["", "### All detected problems", ""])
    if not problems:
        lines.append("No actionable image-integrity problems found.")
        return "\n".join(lines) + "\n"

    grouped: dict[str, list[Problem]] = defaultdict(list)
    for problem in problems:
        grouped[problem.kind].append(problem)
    labels = {
        "case_mismatch": "Filename case mismatches",
        "malformed_markdown": "Malformed Markdown image references",
        "missing_image": "Missing referenced images",
        "orphan": "Unreferenced image candidates",
    }
    for kind in sorted(grouped):
        lines.extend(["", f"#### {labels.get(kind, kind.replace('_', ' ').title())}", ""])
        for problem in grouped[kind]:
            link = github_file_link(
                repository_url,
                revision,
                problem.path,
                problem.line,
            )
            message = f"- {link}"
            if problem.target:
                message += f" requests `{problem.target}`"
            if problem.matches:
                relationship = (
                    "referenced byte-identical copies kept"
                    if kind == "orphan"
                    else "tracked as"
                )
                matches = ", ".join(f"`{match}`" for match in problem.matches)
                message += f" ({relationship} {matches})"
            if problem.replacement:
                message += f" (safe replacement: `{problem.replacement}`)"
            if problem.detail:
                message += f" — {problem.detail}"
            lines.append(message)
    return "\n".join(lines) + "\n"


def cleanup_changes_report(
    changes: Sequence[Change],
    output_format: str,
    repository_url: str = "",
    revision: str = "",
) -> str:
    """Return a report for a manifest application without rerunning the audit."""
    if output_format == "json":
        return json.dumps(
            {"changes": [asdict(change) for change in changes]},
            indent=2,
            sort_keys=True,
        ) + "\n"

    if output_format == "markdown":
        lines = ["### Applied cleanup manifest", ""]
        if not changes:
            lines.append("The verified manifest contained no safe deletions.")
        else:
            lines.append(f"Staged {len(changes)} verified image deletion(s).")
            lines.append("")
            for change in changes:
                link = github_file_link(
                    repository_url,
                    revision,
                    change.path,
                    change.line,
                )
                lines.append(f"- `{change.kind}`: {link}")
        return "\n".join(lines) + "\n"

    lines = ["Applied cleanup manifest", ""]
    if not changes:
        lines.append("No safe deletions were present.")
    else:
        lines.extend(f"- {change.kind}: {change.path}" for change in changes)
    return "\n".join(lines) + "\n"


def write_cli_output(repo_root: Path, raw_path: str, output: str) -> None:
    path = Path(raw_path)
    if not path.is_absolute():
        path = repo_root / path
    path.write_text(output, encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Report malformed, missing, case-mismatched, and unreferenced images."
    )
    parser.add_argument(
        "paths",
        nargs="*",
        default=list(DEFAULT_PATHS),
        help="Tracked content directories to inspect.",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Exit with status 1 when reported problems exist.",
    )
    parser.add_argument(
        "--fix-references",
        action="store_true",
        help=(
            "Repair deterministic malformed, case-mismatched, and nearby missing "
            "image references. Ambiguous references remain unchanged."
        ),
    )
    parser.add_argument(
        "--generated-site",
        metavar="DIRECTORY",
        help=(
            "Rendered Hugo output to scan as independent usage evidence. "
            "Relative paths are resolved from the repository root."
        ),
    )
    parser.add_argument(
        "--delete-safe",
        action="store_true",
        help=(
            "Remove only high-confidence orphan candidates. Without rendered-site "
            "evidence, only exact duplicates of referenced images qualify."
        ),
    )
    parser.add_argument(
        "--apply-cleanup",
        metavar="BASELINE_JSON",
        help=(
            "Stage only the safe deletions in a rendered JSON audit after verifying "
            "that every tracked image still has its audited Git blob ID."
        ),
    )
    parser.add_argument(
        "--verify-cleanup",
        metavar="BASELINE_JSON",
        help=(
            "Verify that staged image deletions exactly match the safe-deletion "
            "list from a rendered JSON report and introduce no new reference problems."
        ),
    )
    parser.add_argument(
        "--format",
        choices=("text", "json", "markdown"),
        default="text",
    )
    parser.add_argument(
        "--repository-url",
        default="",
        help="Repository URL used to make Markdown report paths clickable.",
    )
    parser.add_argument(
        "--revision",
        default="",
        help="Git revision used to make Markdown report paths clickable.",
    )
    parser.add_argument("--output", help="Write the report to this file.")
    parser.add_argument(
        "--json-output",
        help="Also write the current analysis as JSON without running a second audit.",
    )
    parser.add_argument("--repo-root", default=".")
    args = parser.parse_args()
    changing_modes = sum(
        bool(mode) for mode in (args.fix_references, args.delete_safe, args.apply_cleanup)
    )
    if changing_modes > 1:
        parser.error(
            "--fix-references, --delete-safe, and --apply-cleanup are mutually exclusive"
        )
    if args.verify_cleanup and changing_modes:
        parser.error("--verify-cleanup cannot be combined with file-changing modes")
    if args.apply_cleanup and args.generated_site:
        parser.error("--apply-cleanup uses rendered evidence from its JSON manifest")
    if args.apply_cleanup and args.json_output:
        parser.error("--json-output is not available with --apply-cleanup")
    return args


def find_repo_root(raw_root: str) -> Path:
    root = Path(raw_root).resolve()
    output = run_git(root, ["rev-parse", "--show-toplevel"], text=True)
    assert isinstance(output, str)
    return Path(output.strip()).resolve()


def main() -> int:
    args = parse_args()
    repo_root = find_repo_root(args.repo_root)
    scopes = tuple(PurePosixPath(path).as_posix().rstrip("/") for path in args.paths)

    def progress(message: str) -> None:
        print(f"[image-integrity] {message}", file=sys.stderr, flush=True)

    if args.apply_cleanup:
        baseline_path = Path(args.apply_cleanup)
        if not baseline_path.is_absolute():
            baseline_path = repo_root / baseline_path
        tracked_files = tracked_file_oids(repo_root)
        paths = cleanup_manifest_paths(
            baseline_path.resolve(),
            tracked_files,
            scopes,
        )
        progress(f"Applying {len(paths)} blob-verified deletion(s) from the manifest.")
        changes = delete_safe_images(repo_root, paths, tuple(tracked_files))
        output = cleanup_changes_report(
            changes,
            args.format,
            args.repository_url,
            args.revision,
        )
        if args.output:
            write_cli_output(repo_root, args.output, output)
        else:
            print(output, end="")
        return 0

    generated_site: Path | None = None
    if args.generated_site:
        generated_site = Path(args.generated_site)
        if not generated_site.is_absolute():
            generated_site = repo_root / generated_site
        generated_site = generated_site.resolve()

    scan_number = 0

    def analyze_current() -> tuple[Snapshot, Analysis]:
        nonlocal scan_number
        scan_number += 1
        started = time.monotonic()
        progress(f"Starting analysis pass {scan_number}.")
        snapshot = current_snapshot(repo_root, scopes)
        generated_used = None
        if generated_site is not None:
            assets = {path for path in snapshot.files if is_image_path(path)}
            generated_used = generated_site_references(
                generated_site,
                assets,
                progress,
            )
        result = analyze(snapshot, generated_used)
        progress(
            f"Analysis pass {scan_number} completed in "
            f"{time.monotonic() - started:.1f}s."
        )
        return snapshot, result

    current_snapshot_value, current = analyze_current()
    changes: list[Change] = []

    if args.fix_references:
        changes.extend(apply_safe_reference_fixes(repo_root, current))
        current_snapshot_value, current = analyze_current()

    if args.delete_safe:
        changes.extend(
            delete_safe_images(
                repo_root,
                current.safe_delete_images,
                tuple(current_snapshot_value.files),
            )
        )
        current_snapshot_value, current = analyze_current()

    reported = current.all_problems()
    verification_errors: list[str] = []
    if args.verify_cleanup:
        baseline_path = Path(args.verify_cleanup)
        if not baseline_path.is_absolute():
            baseline_path = repo_root / baseline_path
        verification_errors = verify_cleanup(
            repo_root,
            baseline_path.resolve(),
            current,
        )

    json_output = analysis_json(
        current,
        reported,
        changes,
        current_snapshot_value.files,
    )
    if args.format == "json":
        output = json_output
    elif args.format == "markdown":
        output = analysis_markdown(
            current,
            reported,
            changes,
            args.repository_url,
            args.revision,
        )
    else:
        output = analysis_text(current, reported, changes)

    if args.output:
        write_cli_output(repo_root, args.output, output)
    else:
        print(output, end="")
    if args.json_output:
        write_cli_output(repo_root, args.json_output, json_output)

    for error in verification_errors:
        print(f"Cleanup verification failed: {error}", file=sys.stderr)

    return 1 if verification_errors or (args.check and reported) else 0


if __name__ == "__main__":
    raise SystemExit(main())
