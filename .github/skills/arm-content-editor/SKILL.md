---
name: arm-content-editor
description: Review and edit Arm Learning Paths and install guides. Use when auditing or improving content quality, metadata descriptions, SEO/GEO/AEO discoverability, Arm-specific framing, install guide versus Learning Path scope, Markdown image alt text, stale or token-heavy content, and focused reviewer feedback.
---

# Arm content editor

Use this skill as a second-pass reviewer for Arm Learning Paths and install guides. Focus on high-impact issues a human reviewer might miss.

Targets are usually selected or referenced Learning Path or install guide files. If the request names a directory, review the files in that content unit together so metadata, terminology, headings, links, and task flow stay consistent.

## Load guidance

Use `AGENTS.md` as the router. Load only the narrowest guidance needed.

For routine second-pass review, start with only the target's content-type guidance:
- Learning Path: `references/learning-path-guidance.md`
- Install guide: `references/install-guide-guidance.md`
- Mixed or unclear scope: `references/repository-guidance.md`

Add general guidance only when the review scope calls for it:
- Prose/style/accessibility: `references/writing-style.md`
- Shared quality/discoverability: `references/content-quality.md`

Add focused guidance only when the task or content requires it:
- Metadata descriptions: `.github/skills/metadata-description-update/SKILL.md`
- SEO/GEO/AEO: `.github/skills/seo-geo-aeo-review/SKILL.md`
- Links: `.github/skills/link-text-review/SKILL.md`
- Images: `.github/skills/audit-images/SKILL.md`
- Code samples: `.github/skills/code-sample-review/SKILL.md`
- Staleness: `.github/skills/stale-content-review/SKILL.md`
- Markdown components: `.github/skills/markdown-component-edit/SKILL.md`

Do not load all guidance files for routine review.

## Review workflow

1. Identify whether the target is a Learning Path or an install guide.
2. Depending on what type of content it is, load the minimum guidance and review against those guidelines.
3. If the initial review finds a likely issue covered by a focused skill, load only that skill before making the finding.
4. Suggest updates in the format specified under `Response format`. Don't comment on content that is already clear, correct, and fit for purpose.
5. When the reviewer accepts all or part of your submissions and asks you to proceed, go ahead and make updates.

Don't recommend splitting content only because a file is long. Prefer semantic boundaries based on headings, task transitions, or conceptual changes.

## Editing workflow

- Make focused edits that preserve the author's intent. 
- Preserve front matter, Hugo shortcodes, code fences, command syntax, file structure, and existing technical flow.
- Prefer Arm-native framing and flag x86 assumptions.
- Preserve content-type boundaries: install guides stay limited to installation and verification, while Learning Paths own one concrete developer task.
- Keep tone natural and developer-focused. Avoid hype, generic praise, and unnecessary rewrites.
- Verify internal links before changing them, or state when link verification was not possible.
- Prioritize learner-blocking issues, incorrect technical guidance, scope drift, missing metadata, broken links, weak Arm framing, image issues, and unclear validation steps.
- Classify substantial files as prose-heavy, mixed, or code-heavy before judging length or density.
- Use repository search when cross-file consistency, links, terminology, or metadata depends on surrounding content.

## Response format

For review requests, lead with findings in an ordered list by severity and type. Include file and line references when available. Then add open questions, followed by a brief summary.

After the reviewer asks to implement suggested fixes, summarize the key changes and note any checks or verification performed.
