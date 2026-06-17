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
- Read `.github/skills/writing-style-review/SKILL.md` only when changing prose around links.
- For Learning Paths, read `.github/skills/learning-path-structure-review/SKILL.md` when link placement or `further_reading` is involved.

## Workflow

1. Identify the target file, directory, section, or selected text.
2. Read surrounding context before suggesting any changes.
3. After understanding the context of the URL, suggest concise and natural rewrites to the anchor text based on `Quality rules`. 
4. After the user accepts suggestions, make changes, then re-open or search changed lines to verify the Markdown link syntax is valid.
5. After you make changes, report changed links and any links not verified.

## Quality rules

- Link text should make sense without nearby words when possible.
- Prefer destination-specific anchors such as `Docker install guide`, `Arm Developer resources`, or `Google Cloud firewall rules`.
- Avoid anchors that only describe the mechanic, such as `here`, `click here`, `this page`, `read more`, `link`, or `website`, as well as bare URLs or repeated generic text.
- Avoid overlong anchors that wrap a whole sentence.
- Don't change product names, tool names, URLs, or technical meaning to satisfy prose preferences.
- Don't add speculative links. Verify internal targets or state when verification was not possible. Preserve the URL unless it's broken or the user asks for a change.

## Examples

Use these examples for both link format and link text guidance.

Poor:

```md
See [here](/install-guides/docker/) for setup.
```

Better:

```md
For setup instructions, see the [Docker install guide](/install-guides/docker/).
```

Poor:

```md
A list of all AWS instance types can be [viewed here](https://aws.amazon.com/ec2/instance-types/).
```

Better:

```md
For a complete list, see [Amazon EC2 instance types](https://aws.amazon.com/ec2/instance-types/).
```
