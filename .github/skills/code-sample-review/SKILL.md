---
name: code-sample-review
description: Review and improve code samples, commands, command output, and fenced code blocks in Arm Learning Paths and install guides. Use when checking editorial formatting, technical accuracy, runnable commands, output lead-ins, code fence integrity, language tags, or token-heavy and unexplained code or output blocks.
---

# Code sample review

Use this skill to review or edit code samples, commands, command output, and fenced code blocks in Arm Learning Paths and install guides.

This skill can support either editorial review or technical review. Match the depth of review to the user's request and don't invent commands, outputs, workflows, package names, benchmark numbers, or validation results.

## Prerequisites

- Work from the repository root.
- Read `AGENTS.md` to locate shared guidance.
- Read `references/code-sample-guidance.md` before reviewing or editing code samples.

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
2. Inspect surrounding prose before judging a code block; code samples should be evaluated in context. If you've previously read the page, use context and don't re-read it unless there's a change since the last read. 
3. Depending on the type of review, suggest fixes as follows:
  - For review requests, report issues by file and line when possible, ordered by learner impact.
  - For edit requests, report issues and suggest focused changes that preserve technical intent and existing repository patterns.
4. After the reviewer accepts suggestions, make changes, then re-scan edited areas for code fence integrity, language tags, and output lead-ins.
5. Report what changed and note any technical assumptions or checks not performed.

## Validation rules

- Preserve front matter, Hugo shortcodes, Markdown structure, command syntax, and expected output unless they are the target of the edit.
- Don't rewrite meaningful code solely for style.
- Don't replace tool-native terms, casing, flags, package names, or architecture strings with prose preferences.
- Don't treat long code or output as a problem by itself; flag it only when it reduces learning value or obscures the task.
- Keep edits scoped to code sample quality unless the user asks for broader content review.
- Don't modify commands or output unless the reviewer accepts the suggestions.
- Don't hallucinate corrections that aren't supported by context, documentation, or an executable check.
