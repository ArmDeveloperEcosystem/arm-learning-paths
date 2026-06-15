# Agent instructions

This repository contains Arm Learning Paths and install guides for learn.arm.com.

Use this file as a lightweight router for Codex, Copilot, and other coding agents. Do not treat it as the full style guide. Load only the guidance that matches the task.

## Repository map

- `content/learning-paths/` contains task-led, end-to-end tutorials.
- `content/install-guides/` contains installation and verification guides.
- `.github/instructions/` contains scoped content guidance.
- `.github/skills/` contains reusable reviewer workflows and task-specific capabilities.

## Source of truth

- Repository router: `AGENTS.md`
- General Arm content editing: `.github/skills/arm-content-editor/SKILL.md`
- Learning Paths: `.github/skills/arm-content-editor/references/learning-path-guidance.md`
- Install guides: `.github/skills/arm-content-editor/references/install-guide-guidance.md`
- Shared content quality: `.github/skills/arm-content-editor/references/content-quality.md`
- Metadata descriptions: `.github/skills/metadata-description-update/SKILL.md`
- Markdown components: `.github/skills/markdown-component-edit/SKILL.md`
- Accessible link text: `.github/skills/link-text-review/SKILL.md`
- Stale content risk scans: `.github/skills/stale-content-review/SKILL.md`
- Images, alt text, captions, and `#center` syntax: `.github/skills/audit-images/SKILL.md`
- Code samples, commands, outputs, and code fence integrity: `.github/skills/code-sample-review/SKILL.md`

Prefer the narrowest applicable file. Avoid loading every instruction file by default.

## Compatibility

- `.github/copilot-instructions.md` is a short compatibility pointer for Github Copilot. It is not the source of truth.
- `.github/instructions/*.instructions.md` files are compatibility pointers. Skill references are the source of truth.

## Reviewer workflows

Use skills for repeatable workflows such as image audits, metadata description updates, stale-content audits, or structured content-quality checks.

Current shared skills:

- `.github/skills/arm-content-editor/SKILL.md` for reviewing and editing Arm Learning Paths and install guides.
- `.github/skills/metadata-description-update/SKILL.md` for adding or improving front matter `description` fields for Learning Paths and install guides.
- `.github/skills/markdown-component-edit/SKILL.md` for adding or updating links, tables, notices, tab panes, code panes, and other structured Markdown components.
- `.github/skills/link-text-review/SKILL.md` for reviewing and improving accessible, descriptive Markdown link text.
- `.github/skills/stale-content-review/SKILL.md` for periodic maintenance scans that flag stale-content risk, screenshots, mutable dependencies, temporal wording, old dates, and version-sensitive content.
- `.github/skills/audit-images/SKILL.md` for auditing Markdown image references, deficient alt text, captions, alignment syntax, and before/after image quality counts.
- `.github/skills/code-sample-review/SKILL.md` for reviewing code samples, commands, command output, language tags, and code fence integrity.

Keep deterministic scans in scripts when possible, and keep long reference material out of always-loaded instructions.

When creating new skills, prefer a structured `SKILL.md` with concise sections such as description, prerequisites, trigger, workflow, validation rules, and error handling. Keep the workflow explicit enough to be repeatable without turning the skill into a full style guide.
