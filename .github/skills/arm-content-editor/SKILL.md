---
name: arm-content-editor
description: Review and edit Arm Learning Paths and install guides. Use when auditing or improving content quality, metadata descriptions, Arm-specific framing, install guide versus Learning Path scope, Markdown image alt text, stale or token-heavy content, and focused reviewer feedback.
---

# Arm content editor

Use this skill to review or edit Arm Learning Paths and install guides with focused, high-signal feedback and minimal necessary changes.

Targets are usually selected or referenced Learning Path or install guide files. If the request names a directory, review the files in that content unit together so metadata, terminology, headings, links, and task flow stay consistent.

## Load guidance

Start with `AGENTS.md` at the repository root to identify the right source files.

Read only the guidance needed for the task:

- Repository structure and content model: `references/repository-guidance.md`
- Writing style, headings, links, terminology, and prose cleanup: `references/writing-style.md`
- Shared content quality and discoverability: `references/content-quality.md`
- Learning Paths: `references/learning-path-guidance.md`
- Install guides: `references/install-guide-guidance.md`
- Metadata descriptions: `.github/skills/metadata-description-update/SKILL.md`
- Markdown components: `.github/skills/markdown-component-edit/SKILL.md`
- Accessible link text: `.github/skills/link-text-review/SKILL.md`
- Stale content risk scans: `.github/skills/stale-content-review/SKILL.md`
- Images, alt text, captions, and `#center` syntax: `.github/skills/audit-images/SKILL.md`
- Code samples, commands, outputs, and code fence integrity: `.github/skills/code-sample-review/SKILL.md`

## Review workflow

1. Identify whether the target is a Learning Path, install guide, or mixed content.
2. Load the matching scoped guidance.
3. Use repository search when cross-file consistency, links, terminology, or metadata depends on surrounding content.
4. Review by exception. Do not comment on content that is already clear, correct, and fit for purpose.
5. Prioritize learner-blocking issues, incorrect technical guidance, scope drift, missing metadata, broken links, weak Arm framing, image issues, and unclear validation steps.
6. Classify substantial files as prose-heavy, mixed, or code-heavy before judging length or density.
7. Use the metadata description skill for focused `description` field updates.
8. Use the Markdown component skill for focused links, tables, notices, tab panes, and component syntax edits.
9. Use the link text review skill for focused accessible anchor text cleanup.
10. Use the stale content review skill for periodic maintenance scans and freshness triage.
11. Use the code sample review skill for command accuracy, output formatting, code fence integrity, and token-heavy code or output blocks.

Do not recommend splitting content only because a file is long. Prefer semantic boundaries based on headings, task transitions, or conceptual changes.

## Editing workflow

- Make focused edits that preserve the author's intent.
- Preserve front matter, Hugo shortcodes, code fences, command syntax, file structure, and existing technical flow.
- Prefer Arm-native framing and flag x86 assumptions.
- Preserve content-type boundaries: install guides stay limited to installation and verification, while Learning Paths own one concrete developer task.
- Keep tone natural and developer-focused. Avoid hype, generic praise, and unnecessary rewrites.
- Verify internal links before changing them, or state when link verification was not possible.

## Response format

For review requests, lead with findings ordered by severity and include file and line references when available. Then add open questions, followed by a brief summary.

For edit requests, summarize the key changes and note any checks or verification performed.
