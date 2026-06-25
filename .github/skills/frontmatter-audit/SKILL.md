---
name: frontmatter-audit
description: Audit YAML front matter and metadata for Arm Learning Paths and install guides. Use when checking required fields, fixed layout fields, duplicate weights, draft visibility metadata, closed-list metadata values, description presence or quality, YAML validity, and front matter consistency.
---

# Front matter audit

Use this skill to audit front matter and metadata without rewriting body content. It can report issues or make metadata-only edits when requested.

## Workflow

1. Identify whether the target is a Learning Path, single-page install guide, multi-page install guide, or mixed content directory.
2. Read the front matter and enough body context to understand the page task, platform, and outcome.
3. Check YAML validity and preserve front matter order when editing.
4. Check required and fixed fields for the content type.
5. Check metadata consistency across files in a content unit, including duplicate or missing `weight` values.
6. Check whether `description` is present and fit for purpose. If it is missing or weak, either report it or use `.github/skills/metadata-description-update/SKILL.md` when the user asked for edits.
7. After completing all checks, report findings by severity with file and line references when available.

## Learning Path checks

For a Learning Path directory:

- `_index.md` should use `weight: 1`.
- Public pages should have unique `weight` values within the directory.
- Every page except for `_next-steps.md` must include a description.
- `_index.md` must include `description`.
- Required `_index.md` fields include `title`, `description`, `weight`, `layout`, `minutes_to_complete`, `prerequisites`, `author`, `generate_summary_faq`, `rerun_summary`, `rerun_faqs`, `subjects`, `armips`, `tools_software_languages`, `skilllevels`, and `operatingsystems`.
- `layout` is usually `learningpathall`.
- `title` should be task-led and use an imperative structure: verb + technology/tool + outcome.
- `skilllevels` values are only `Introductory` or `Advanced`.
- `subjects` and `operatingsystems` must match the closed lists in `content/learning-paths/cross-platform/_example-learning-path/write-2-metadata/`.
- `armips` should use Arm IP families such as Neoverse, Cortex-A, or Cortex-M, not specific CPU models or Arm architecture versions.
- `author` can list multiple authors with YAML list syntax.
- `generate_summary_faq`, `rerun_summary`, and `rerun_faqs` values are only `true` and `false`.
- Skip `_next-steps.md` for description updates unless the user explicitly asks how to handle it.

## Install guide checks

For an install guide:

- Required fields include `title`, `minutes_to_complete`, `official_docs`, `author`, `weight`, and `layout`.
- Fixed fields should usually be `weight: 1`, `tool_install: true`, and `layout: installtoolsall`.
- Set `tool_install: false` only when the guide is intentionally hidden.
- Set `multi_install` and `multitool_install_part` based on whether the guide is multi-page.
- If `multi_install` is true, the first page should act as the series overview.
- Sub-pages in a multi-page guide should set `multitool_install_part: true`.
- Install guide descriptions should describe the tool, supported Arm platform or operating system context, and what the setup enables.

## Description quality checks

- The description should be one sentence.
- It should state what the reader will do, the main tool or platform, and the useful outcome.
- It should be concise, developer-focused, and suitable as a search snippet.
- It should not repeat the title verbatim.
- It should not use vague summaries, hype, keyword stuffing, unsupported claims, or invented capabilities.
- Quote the value only when needed for YAML syntax.

## Validation rules

- Preserve body content, Hugo shortcodes, links, commands, code blocks, and expected output unless the user explicitly asks for broader edits.
- Do not invent metadata values. Use nearby content, repository examples, or the closed-list metadata reference.
- If a closed-list value cannot be verified, state the limitation instead of guessing.
- For broad audits, report before editing unless the user explicitly requested changes.

## Response format

For audits, lead with metadata findings ordered by severity and include file and line references. Then add skipped files, assumptions, and a short summary.

For edits, summarize changed fields and note any metadata checks performed.
