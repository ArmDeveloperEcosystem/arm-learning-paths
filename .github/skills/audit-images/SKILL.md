---
name: audit-images
description: Audit and fix Markdown image alt text in Arm Learning Paths and install guides. Use when the user asks to review images, find deficient alt text, count faulty images, run project-level or path-level image audits, track before/after image quality, or update image alt text and captions against repository image guidance.
---

# Audit images

## Description

Audit Markdown image references in Arm Learning Paths and install guides, report deficient alt text and image syntax, and help fix alt text with useful instructional descriptions.

Use the script for repeatable inventory and counting. Use assistant judgment for semantic alt-text quality and final edits.

## Prerequisites

- Work from the repository root.
- Read `AGENTS.md` to locate shared guidance.
- Read `references/image-guidance.md` before editing image alt text.
- When auditing a Learning Path or install guide, also read the matching scoped content guidance.

## Trigger

Use this skill when the user asks to:

- Audit images or alt text.
- Find placeholder, vague, missing, malformed, or duplicated alt text.
- Count faulty images across the project or inside one Path/guide.
- Track image audit counts before and after fixes.
- Fix image alt text, captions, or `#center` syntax.

## Review levels

### Project-level review

Scan all Learning Paths and install guides unless the user gives a narrower scope.

Use project-level review to:

- Count total image references and faulty image references.
- Group faults by content unit and issue type.
- Identify high-priority directories or files for cleanup.
- Produce a before/after baseline for tracking progress.

Do not mass-edit the whole project unless the user explicitly asks. Prefer reporting the project-level inventory and then fixing one Path, guide, category, or batch.

### Path/guide-level review

Scan one Learning Path directory, install guide file, or install guide directory.

Use path/guide-level review to:

- List each faulty image with file, line, image path, current alt text, caption, and issue type.
- Inspect surrounding Markdown context before changing alt text.
- View local images when visual inspection is needed.
- Fix alt text and syntax in place.
- Re-run the audit and report before/after counts.

## Workflow

1. Identify whether the requested scope is project-level or path/guide-level.
2. Run `.github/skills/audit-images/scripts/audit_images.py` on that scope.
3. Record the baseline summary: total images, faulty images, content units affected, and issue counts.
4. For project-level requests, summarize the results and suggest prioritized cleanup batches unless the user asked for edits.
5. For path/guide-level edit requests, inspect the relevant Markdown context and image files.
6. Rewrite deficient alt text using `references/image-guidance.md`.
7. Preserve the repository image syntax, especially `![Descriptive alt text#center](image.png "Optional caption")`.
8. Re-run the audit on the same scope.
9. Report before/after counts, files changed, and any remaining issues.

## Validation rules

- Treat the script as a detector, not the final authority. It flags likely problems for review.
- Do not replace meaningful alt text only because it is long or short; judge whether it helps the learner complete the task.
- Do not use placeholders such as `alt-txt`, `alt-text`, `image`, `img1`, `screenshot`, `graph`, or `output`.
- Do not use captions as a substitute for alt text.
- Keep `#center` attached directly to the alt text with no space before it.
- Preserve valid local image paths and existing captions unless they are wrong, vague, or outdated.
- Avoid `Figure 1:` style captions unless the content uses explicit numbered cross-references.

## Error handling

- If the script reports a missing local image path, verify whether the path is site-root-relative, file-relative, or intentionally external before changing content.
- If an image cannot be inspected, fix only issues that can be resolved from surrounding Markdown context and state the limitation.
- If project-level results are too large to edit safely, report the inventory and recommend a smaller batch.
- If the audit script and visual/context review disagree, explain the judgment and leave a short note in the final response.

## Script usage

Run a project-level audit:

```bash
python3 .github/skills/audit-images/scripts/audit_images.py
```

Run a path-level audit:

```bash
python3 .github/skills/audit-images/scripts/audit_images.py content/learning-paths/servers-and-cloud-computing/example-path
```

Write JSON for tracking:

```bash
python3 .github/skills/audit-images/scripts/audit_images.py --format json --output image-audit.json
```
