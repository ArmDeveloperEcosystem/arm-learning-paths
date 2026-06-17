---
name: install-guide-structure-review
description: Review Arm install guides for structural soundness, installation-only scope, verification quality, OS-specific sections, troubleshooting, multi-page guide behavior, and version-note placement. Use when asked to review, create, reorganize, or assess content under content/install-guides.
---

# Install guide structure review

Use this skill when an install guide needs a structural review. Focus on whether the guide installs and verifies one tool on Arm platforms without drifting into applied workflows.

For metadata-only checks, use `.github/skills/frontmatter-audit/SKILL.md`. For command and output accuracy, use `.github/skills/code-sample-review/SKILL.md`.

## Workflow

1. Identify whether the target is a single-page guide, multi-page guide, or install guide directory.
2. State the installation target and supported Arm platform context in one sentence.
3. Check the required guide shape:
   - Overview: explains what the tool is and which Arm platforms are supported, such as `aarch64`, Windows on Arm, or macOS on Arm.
   - Install steps: grouped logically, with clear OS-specific sections when necessary.
   - Verification: includes at least one or two commands and expected output.
   - Troubleshooting: covers common failure cases and fixes when appropriate.
   - Optional uninstall steps stay secondary.
4. Check version handling:
   - Download and install examples use a specific version when practical.
   - A note before versioned commands tells readers they can use other versions.
   - The note links to a release or download page where readers can find the latest version.
5. Check scope boundaries:
   - No end-to-end workflows.
   - No performance benchmarking.
   - No deep architectural explanation.
   - No comparative marketing claims.
   - No duplicated Learning Path workflow content.
6. For multi-page guides, check that the first page acts as the overview and sub-pages behave as install parts.
7. Report findings by learner impact, with file and line references when available. Do not comment on content that is already structurally sound.

## Version note pattern

Use this pattern before commands that pin a downloadable tool version:

```md
{{% notice Note %}}
The following commands use <tool> version <version>. The same commands work with other versions. Replace the file used in these steps with the file for your version of choice. To find the latest version, see [Link to page with release info](URL).
{{% /notice %}}
```

## Validation rules

- Preserve front matter, Hugo shortcodes, code fences, command syntax, expected output, links, and the author's technical intent when editing.
- Use `.github/skills/frontmatter-audit/SKILL.md` for required front matter, fixed fields, and metadata validity.
- Use `.github/skills/code-sample-review/SKILL.md` when commands, outputs, language tags, or technical accuracy need a deeper pass.
- Verify internal links before changing them, or state when verification was not possible.

## Response format

For reviews, lead with findings ordered by severity and include file and line references. Then add open questions or assumptions, followed by a short summary.

For edits, summarize the structural changes and note any checks performed.
