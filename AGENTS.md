# Agent instructions

This repository contains Arm Learning Paths and install guides for learn.arm.com.

Use this file as a lightweight router for Codex, Copilot, and other coding agents. Do not treat it as the full style guide. Load only the guidance that matches the task.

## Repository map

- `content/learning-paths/` contains task-led, end-to-end tutorials.
- `content/install-guides/` contains installation and verification guides.
- `.github/instructions/` contains scoped content guidance.
- `.github/skills/` contains reusable reviewer workflows and task-specific capabilities.

## Source of truth

- Repository-wide guidance: `.github/copilot-instructions.md`
- Learning Paths: `.github/instructions/learning-paths.instructions.md`
- Install guides: `.github/instructions/install-guides.instructions.md`
- Shared content quality: `.github/instructions/content-quality.instructions.md`
- Images, alt text, captions, and `#center` syntax: `.github/instructions/images.instructions.md`

Prefer the narrowest applicable file. Avoid loading every instruction file by default.

## Reviewer workflows

Use skills for repeatable workflows such as image audits, metadata description updates, stale-content audits, or structured content-quality checks.

Current shared skills:

- `.github/skills/arm-content-editor/SKILL.md` for reviewing and editing Arm Learning Paths and install guides.

Keep deterministic scans in scripts when possible, and keep long reference material out of always-loaded instructions.
