# Repository guidance

## Project overview

This project is a collection of Learning Paths and install guides for learn.arm.com. The content explains how to develop software on Arm for software developers targeting Arm platforms.

Assume the audience is made up of Arm software developers. Bias information toward Arm platforms. For Linux, assume systems are `aarch64` unless context says otherwise. Readers also use macOS and Windows on Arm systems.

## Highest priority rules

- Each Learning Path must own one clear developer task.
- Install guides are for installation and verification only.
- Every Learning Path `_index.md` must include a `description` field.
- Use task-led titles, introductions, and metadata.
- Do not use placeholder alt text such as `alt-txt`.
- Prefer Arm-native solutions and Arm-specific framing.
- Avoid hype, duplication, and vague summaries.

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

- Learning Paths are end-to-end tasks with prepare, configure, use, and validate stages. They must include `_index.md` and `_next-steps.md`.
- Install guides are for installation and verification only. They should not include applied workflows, benchmarks, or deep architectural explanation.
- Learning Paths can link to install guides for setup. Do not duplicate install-guide content inside Learning Paths.

## Reference examples

Use `content/learning-paths/cross-platform/_example-learning-path` when creating or checking Learning Path structure.
