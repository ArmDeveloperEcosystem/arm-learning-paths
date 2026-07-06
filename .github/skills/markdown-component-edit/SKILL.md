---
name: markdown-component-edit
description: Add or update structured Markdown and Hugo components in Arm Learning Paths and install guides. Use when asked to turn selected text into a link, table, notice, tab pane, code pane, shortcode block, or other repo-specific Markdown component while preserving surrounding content.
---

# Markdown component edit

Use this skill to make focused structural edits to Markdown and Hugo components in Arm Learning Paths and install guides.

This skill is best when the user highlights text, names a section, or asks for a specific component. It shouldn't decide that content needs a component during broad editorial review unless the user asks.

## Prerequisites

- Work from the repository root.
- Read `AGENTS.md` to locate shared guidance.
- Read `references/component-patterns.md` before adding or changing notices, tables, tabs, or other structured components.
- Use `.github/skills/code-sample-review/SKILL.md` for code panes, command examples, command output, language tags, or code fence integrity.

## Workflow

1. Use the user's highlighted, selected, or explicitly named text as the edit target. If the target is ambiguous, ask for the exact text, file, or section before editing. If you've previously read the page, use context and don't re-read it unless there's a change since the last read. 
2. Inspect nearby Markdown so the new component fits the surrounding flow.
3. Verify internal links before adding or changing them when practical.
4. Use `component rules` and the `component-patterns` reference and do one of the following:
  - If the target isn't a good fit for the provided component, push back with justification. Rely on component rules. 
  - If it's a good fit, or if the reviewer voluntarily requests an unusual update, make the update.
4. After making an update, re-open or search the edited area to verify shortcode pairs, table rows, links, and code fences are well formed.
5. Report the component added or changed and note any links or syntax that could not be verified.

## Component rules

- Notices are for notes, warnings, tips, troubleshooting, platform-specific context, or important constraints.
- Tables are for comparison, lookup, short structured reference, or option summaries. Avoid tables for sequential instructions.
- Tab panes are for mutually exclusive alternatives such as operating systems, shells, package managers, or platform-specific code.
- Links should use descriptive anchor text. Use the link text review skill for broader cleanup.
- Don't convert content into a component if a plain paragraph or list is clearer. Keep the component small and purposeful
- Preserve front matter, shortcodes, code fences, commands, expected output, and existing file structure.
- Use local examples before adding unfamiliar Hugo shortcode syntax.
