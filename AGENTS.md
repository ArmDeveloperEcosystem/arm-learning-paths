# Agent instructions

This repository contains Arm Learning Paths and install guides for learn.arm.com.

Use this file as a lightweight router for Codex, Copilot, and other coding agents. Do not treat it as the full style guide. Load only the guidance that matches the task.

## Repository map

- `content/learning-paths/` contains task-led, end-to-end tutorials.
- `content/install-guides/` contains installation and verification guides.
- `.github/skills/` contains reusable reviewer workflows and task-specific capabilities.

## Compatibility

- `.github/copilot-instructions.md` is a short compatibility pointer for Github Copilot. It is not the source of truth.

## Reviewer workflows

Use skills for repeatable workflows such as image audits, metadata description updates, stale-content audits, or structured content-quality checks.

Current shared skills:

- Learning Path structure review: `.github/skills/learning-path-structure-review/SKILL.md`
- Install guide structure review: `.github/skills/install-guide-structure-review/SKILL.md`
- Writing style and voice review: `.github/skills/writing-style-review/SKILL.md`
- Front matter and metadata audits: `.github/skills/frontmatter-audit/SKILL.md`
- Metadata descriptions: `.github/skills/metadata-description-update/SKILL.md`
- SEO, GEO, AEO, and AI-agent discoverability: `.github/skills/seo-geo-aeo-review/SKILL.md`
- Markdown components: `.github/skills/markdown-component-edit/SKILL.md`
- Accessible link text: `.github/skills/link-text-review/SKILL.md`
- Stale content risk scans: `.github/skills/stale-content-review/SKILL.md`
- Images, alt text, captions, and `#center` syntax: `.github/skills/audit-images/SKILL.md`
- Code samples, commands, outputs, and code fence integrity: `.github/skills/code-sample-review/SKILL.md`

Keep deterministic scans in scripts when possible, and keep long reference material out of always-loaded instructions. 

Prefer the narrowest applicable file. Avoid loading every instruction file by default.

When creating new skills, prefer a structured `SKILL.md` with concise sections such as description, prerequisites, trigger, workflow, validation rules, and error handling. Keep the workflow explicit enough to be repeatable without turning the skill into a full style guide.
