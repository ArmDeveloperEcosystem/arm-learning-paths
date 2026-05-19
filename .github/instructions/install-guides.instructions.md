---
applyTo: "content/install-guides/**/*.md"
---

### Install guide requirements

Install guides focus on installing and verifying one tool on Arm platforms. They do not teach workflows or applied usage.

#### Front matter requirements

Install guides must include:
- `title`
- `minutes_to_complete`
- `official_docs`
- `author`
- `weight: 1`
- `layout: installtoolsall`

#### Fixed fields for install guides

- `weight: 1` (always)
- `tool_install: true` (set to false only if intentionally hidden)
- `layout: installtoolsall` (always)
- `multi_install` and `multitool_install_part` (set based on whether the install guide is multi-page)

Do not modify fixed template fields.

If `multi_install` is set to true, the first page must act as an overview for the series. Sub-pages must set `multitool_install_part: true`.

#### Required content structure

Install guides should include:

1. Overview
   - What the tool is
   - Supported Arm platforms (aarch64, Windows on Arm, macOS on Arm where applicable)

2. Install steps
   - Clear OS-specific sections when necessary
   - Commands grouped logically
   - Explanation before each code block

3. Verify installation
   - One or two commands
   - Expected output shown

4. Troubleshooting
   - Common failure cases
   - Clear fixes

Optional:
- Uninstall instructions

#### Scope boundaries

Install guides must not include:
- End-to-end workflows
- Performance benchmarking
- Deep architectural explanation
- Comparative marketing claims

Learning Paths may link to install guides for setup steps. Install guides should not duplicate workflow content.

#### Tool versions

When providing commands for downloading or installing software, use a specific version in the example. This ensures that the instructions are accurate and verifiable. However, also include a note before the commands that tells readers the same commands work with other versions. Provide a link to where the latest version can be found. The note can be formatted as follows:

{{% notice Note %}}
The following commands use <tool> version <version>. The same commands work with other versions. Replace the file used in these steps with the file for your version of choice. To find the latest version, see [Link to page with release info](URL).
{{% /notice %}}

### Install Guide metadata description requirements

Every Install Guide's front matter must include a `description` field.

- Write one sentence
- Describe the tool being installed and what it can be used for (why it matters) 
- Keep it concise, developer-focused, and suitable for use as a search snippet
- Do not use vague summaries or marketing language
- A slightly richer one-sentence summary is acceptable when it helps clarify the workflow or outcome

Good example:

```yaml
description: Learn how to install Arm Compiler for Linux (ACfL) on Arm Linux (aarch64) to access the armclang C/C++ compiler, armflang Fortran compiler, and Arm Performance Libraries for HPC development.
```

Avoid:
- Generic summaries that could apply to any page
- Marketing phrases such as `powerful`, `cutting-edge`, or `game-changing`

### Metadata optimization workflow

When adding or revising `description` fields:

- Use metadata descriptions to clarify which platform or tool, and what outcome
- Treat the description as a search snippet, not a generic summary

### Recap section 

For Install Guides, include a short recap paragraph and forward-looking transition at the end of each major instructional section or module

Example recap pattern for Learning Paths:

```md
## Next steps

In this section:
- Briefly summarize what the user has learned or completed
- Suggest and link to a couple relevant Learning Paths (if they exist)

Keep this concise and encouraging. Do not repeat earlier content verbatim.
```
This helps learners feel a sense of progress.
