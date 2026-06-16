---
name: link-text-review
description: Review and improve accessible Markdown link text in Arm Learning Paths and install guides. Use when asked to find vague links, fix link text such as here or click here, verify internal links, improve screen-reader clarity, or make links descriptive and task-focused.
---

# Link text review

Use this skill to review or improve Markdown link text so links are descriptive, accessible, and useful out of context.

This skill focuses on anchor text and link clarity. For tables, notices, tab panes, and other structural Markdown components, use `.github/skills/markdown-component-edit/SKILL.md`.

## Prerequisites

- Work from the repository root.
- Read `AGENTS.md` only if you need repository routing context.
- Read `.github/skills/arm-content-editor/references/writing-style.md` only when changing prose around links.
- For Learning Paths, read `.github/skills/arm-content-editor/references/learning-path-guidance.md` when link placement or `further_reading` is involved.

## Workflow

1. Identify the target file, directory, section, or selected text.
2. Read surrounding context before changing link text.
3. Find vague anchors such as `here`, `click here`, `this page`, `read more`, `link`, bare URLs, or repeated generic text.
4. Verify internal links before editing when practical.
5. Rewrite anchor text to describe the destination, action, or resource.
6. Preserve the URL unless it is broken or the user asks to change it.
7. Keep anchor text concise and natural in the sentence.
8. Re-open or search changed lines to verify the Markdown link syntax is valid.
9. Report changed links and any links not verified.

## Quality rules

- Link text should make sense without nearby words when possible.
- Prefer destination-specific anchors such as `Docker install guide`, `Arm Developer resources`, or `Google Cloud firewall rules`.
- Avoid anchors that only describe the mechanic, such as `click here`, `this link`, or `website`.
- Avoid overlong anchors that wrap a whole sentence.
- Follow `.github/skills/arm-content-editor/references/writing-style.md` for URL path format.
- Don't change product names, tool names, URLs, or technical meaning to satisfy prose preferences.
- Don't add speculative links. Verify internal targets or state when verification was not possible.

## Examples

Poor:

```md
See [here](/install-guides/docker/) for setup.
```

Better:

```md
See the [Docker install guide](/install-guides/docker/) for setup.
```

Poor:

```md
A list of all AWS instance types can be [viewed here](https://aws.amazon.com/ec2/instance-types/).
```

Better:

```md
See the [Amazon EC2 instance types](https://aws.amazon.com/ec2/instance-types/) for a complete list.
```
