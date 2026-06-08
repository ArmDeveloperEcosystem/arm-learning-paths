---
name: code-sample-review
description: Review and improve code samples, commands, command output, and fenced code blocks in Arm Learning Paths and install guides. Use when checking editorial formatting, technical accuracy, runnable commands, output lead-ins, code fence integrity, language tags, or token-heavy and unexplained code or output blocks.
---

# Code sample review

Use this skill to review or edit code samples, commands, command output, and fenced code blocks in Arm Learning Paths and install guides.

This skill can support either editorial review or technical review. Match the depth of review to the user's request and do not invent commands, outputs, workflows, package names, benchmark numbers, or validation results.

## Prerequisites

- Work from the repository root.
- Read `AGENTS.md` to locate shared guidance.
- Read `references/code-sample-guidance.md` before reviewing or editing code samples.
- When the review depends on content type, also read the matching Learning Path or install guide guidance.

## Modes

### Editorial mode

Use when the user asks to review or fix code sample presentation, readability, formatting, or consistency.

Check for:

- Explanatory prose before each code block
- Correct and consistent language tags
- Standard output lead-ins
- Closed code fences
- Oversized, duplicated, or unexplained output blocks
- Consistent terminology around commands, files, UI labels, and outputs

### Technical mode

Use when the user asks whether commands, examples, or outputs are accurate, runnable, safe, or technically complete.

Check for:

- Commands that match the stated operating system, shell, tool, and Arm platform
- Plausible package names, file paths, flags, versions, and environment variables
- Output blocks that correspond to the preceding command
- Validation steps that prove the intended outcome
- Learning Path code that supports the stated task
- Install guide commands that stay within install and verification scope

## Workflow

1. Identify the review scope and whether the request is editorial, technical, or mixed.
2. Load only the content-type guidance needed for the target files.
3. Inspect surrounding prose before judging a code block; code samples should be evaluated in context.
4. For review requests, report issues by file and line when possible, ordered by learner impact.
5. For edit requests, report issues and suggest focused changes that preserve technical intent and existing repository patterns.
6. Do not modify commands or output unless the correction is supported by context, documentation, or an executable check.
7. After the reviewer accepts suggestions, re-scan edited areas for code fence integrity, language tags, and output lead-ins.
8. Report what changed and note any technical assumptions or checks not performed.

## Validation rules

- Preserve front matter, Hugo shortcodes, Markdown structure, command syntax, and expected output unless they are the target of the edit.
- Do not rewrite meaningful code solely for style.
- Do not replace tool-native terms, casing, flags, package names, or architecture strings with prose preferences.
- Do not treat long code or output as a problem by itself; flag it only when it reduces learning value or obscures the task.
- Keep edits scoped to code sample quality unless the user asks for broader content review.
