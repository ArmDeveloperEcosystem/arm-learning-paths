# Repository guidance

## Project overview

This project is a collection of Learning Paths and install guides for learn.arm.com. The content explains how to develop software on Arm for software developers targeting Arm platforms.

Assume the audience is made up of Arm software developers. Bias information toward Arm platforms. For Linux, assume systems are `aarch64` unless context says otherwise. Readers also use macOS and Windows on Arm systems.

## Guidance boundaries

Use this file for repository-wide orientation only. For task-specific rules, load the narrowest relevant guidance:

- Learning Path structure and scope: `learning-path-guidance.md`
- Install guide structure and scope: `install-guide-guidance.md`
- Shared content quality: `content-quality.md`
- Metadata descriptions: `.github/skills/metadata-description-update/SKILL.md`
- SEO, GEO, AEO, and AI-agent discoverability: `.github/skills/seo-geo-aeo-review/SKILL.md`
- Images and alt text: `.github/skills/audit-images/SKILL.md`

## Project structure

Top-level directories:

- `/content`: Main directory containing Learning Paths and install guides as Markdown files.
- `/themes`: HTML templates and styling elements that render the final website.
- `/tools`: Python scripts for automated website integrity checking.
- `config.toml`: High-level Hugo configuration settings.

Content directories:

- `content/learning-paths/`: Core learning content organized by category.
- `content/install-guides/`: Tool installation guides with supporting subdirectories and shared images.

Special content directories:

- `content/migration/`: Migration guides and resources for `https://learn.arm.com/migration`.
- `content/lists/`: Content listing and organization files for `https://learn.arm.com/lists`.
- `content/stats/`: Website statistics and analytics for `https://learn.arm.com/stats`.

## Content type boundaries

- Learning Paths are end-to-end tasks with prepare, configure, use, and validate stages.
- Install guides are for installation and verification only.
- Learning Paths can link to install guides for setup. Do not duplicate install-guide content inside Learning Paths.

## Reference examples

Use `content/learning-paths/cross-platform/_example-learning-path` when creating or checking Learning Path structure.
