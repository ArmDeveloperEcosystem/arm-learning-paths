---
name: metadata-description-update
description: Add or improve SEO-friendly front matter description fields for Arm Learning Paths and install guides. Use when asked to add missing descriptions, update weak metadata descriptions, optimize search snippets, or ensure Learning Path pages and install guides have accurate description metadata.
---

# Metadata description update

Use this skill to add or improve `description` fields in front matter for Arm Learning Paths and install guides.

This skill is for search and discovery metadata. For draft visibility metadata, use `.github/skills/intake-metadata-update/SKILL.md`.

## Prerequisites

- Work from the repository root.
- Read `AGENTS.md` to locate shared guidance.
- Read `.github/skills/arm-content-editor/references/content-quality.md` for general project content quality guidance.
- For Learning Paths, read `.github/skills/arm-content-editor/references/learning-path-guidance.md`.
- For install guides, read `.github/skills/arm-content-editor/references/install-guide-guidance.md`.

## Scope rules

- Learning Path directory: update `_index.md` and each public content page in the directory. Skip `_next-steps.md`.
- Learning Path `_index.md`: describe the full Learning Path task, main tool or platform, and outcome.
- Learning Path content page: describe that page's specific action, context in the task flow, and outcome.
- Install guide file: describe the tool being installed, supported Arm platform or operating system context, and what the tool enables.
- Multi-page install guide directory: update the main entry page and public sub-pages that need descriptions.
- Preserve existing front matter order when practical. If adding a missing description, place it near `title`.
- Preserve body content, shortcodes, links, commands, code blocks, and expected output. Don't edit anything that isn't metadata.
- Skip `_next-steps.md` and any file without front matter unless the user explicitly asks how to handle it.

## Workflow

1. Identify whether the target is an install guide content page, a Learning Path `_index.md`, or a Learning Path content page.
2. Read the title, existing description, headings, introduction, task flow, code or command context, and validation or conclusion.
3. Add or revise the `description` field in front matter based on quality rules.
4. After editing, re-open or search the files to verify each changed target has one `description` field.
5. Report files changed and note any skipped files.

## Description quality rules

- Write one sentence.
- Keep it concise, developer-focused, and suitable for a search snippet.
- Use natural Arm-specific terms when relevant.
- State what the reader will do, the main tool or platform, and the useful outcome.
- Don't repeat the title verbatim.
- Don't use vague summaries such as `Learn about...` unless the page is genuinely conceptual.
- Don't use marketing language, hype, or keyword stuffing.
- Don't invent capabilities, performance claims, supported platforms, or tools not supported by the page.
- Use valid YAML. Quote the description only when needed for YAML syntax.

## Examples

Learning Path `_index.md`:

```yaml
description: Learn how to deploy a retrieval-augmented generation application on Google Axion with LlamaIndex, Ollama, and a browser-based chat interface.
```

Learning Path content page:

```yaml
description: Configure firewall rules for a Google Axion instance so the browser-based RAG application can accept HTTP traffic.
```

Install guide:

```yaml
description: Install the AWS Cloud Development Kit on Arm Linux and verify the setup so you can define and deploy cloud infrastructure with reusable code.
```
