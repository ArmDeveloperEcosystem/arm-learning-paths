---
applyTo: "content/learning-paths/**/*.md"
---

### Content structure

Each Learning Path must have an `_index.md` file and a `_next-steps.md` file. The `_index.md` file contains the main content of the Learning Path. The `_next-steps.md` file contains links to related content and is included at the end of the Learning Path.

Additional resources and `next steps` content should be placed in the `further_reading` section of `_index.md`, not in `_next-steps.md`. The `_next-steps.md` file should remain minimal and unmodified as indicated by `FIXED, DO NOT MODIFY` comments in the template.

The `_index.md` file should contain the following front matter and content sections.

### Front matter (YAML format)

- `title`: Imperative heading following the [verb] + [technology] + [outcome] format
- `description`: One-sentence metadata summary used for search snippets and page previews. Describe the task, main technology or platform, and expected outcome in plain language
- `weight`: Numerical ordering for display sequence, weight is 1 for `_index.md` and each page is ordered by weight, no markdown files should have the same weight in a directory
- `layout`: Template type (usually "learningpathall")
- `minutes_to_complete`: Realistic time estimate for completion
- `prerequisites`: List of required knowledge, tools, or prior learning paths
- `author`: Main contributor's name, multiple authors can be listed separated using `-` on new lines
- `subjects`: Technology categories for filtering and search, this is a closed list and must match one of the subjects listed on https://learn.arm.com/learning-paths/cross-platform/_example-learning-path/write-2-metadata/
- `armips`: Relevant Arm IP, stick to Neoverse, Cortex-A, Cortex-M, etc. Don't list specific CPU models or Arm architecture versions
- `tools_software_languages`: Open category listing Programming languages, frameworks, and development tools used
- `skilllevels`: Skill levels allowed are only Introductory and Advanced
- `operatingsystems`: Operating systems used, must match the closed list on https://learn.arm.com/learning-paths/cross-platform/_example-learning-path/write-2-metadata/

### Further reading curation

Limit `further_reading` resources to four to six essential links. Prioritize:

- Direct relevance to the topic
- Arm-specific Learning Paths over generic external resources
- Foundation knowledge for the target audience
- Required tools (install guides)
- Logical progression from basic to advanced

Avoid overwhelming readers with too many links, which can cause them to leave the platform.

All Learning Paths should generally include:

- Title: [Imperative verb] + [technology/tool] + [outcome]
- Introduction paragraph: Context + user goal + value proposition
- Prerequisites section with explicit requirements and links
- Learning objectives: three to four bulleted, measurable outcomes with action verbs
- Step-by-step sections with logical progression
- Clear next steps or conclusion

For title formatting:

- Must use imperative voice (`Deploy`, `Configure`, `Build`, `Create`)
- Must include SEO keywords (technology names, tools)
- Examples: `Deploy applications on Arm servers`, `Configure Arm processors for optimal performance`

The term "Learning Path" should always be capitalized.

### Learning Path metadata description requirements

Every Learning Path `_index.md` must include a `description` field.

- Write one sentence
- Describe the task, the main technology or platform, and the expected outcome
- Keep it concise, developer-focused, and suitable for use as a search snippet
- Use a task-led structure such as: **Verb + task + tool/platform + outcome**
- Do not repeat the title verbatim
- Do not use vague summaries or marketing language
- A slightly richer one-sentence summary is acceptable when it helps clarify the workflow or outcome

Good example:

```yaml
description: Learn how to automate x86-to-Arm application migration using the Arm MCP Server, with compatibility checks and Docker-based validation on Arm cloud platforms.
```

Also good:

```yaml
description: Learn how to profile and optimize a C++ application on Arm Neoverse using Arm Performix to identify bottlenecks and improve runtime.
```

Avoid:
- Generic summaries that could apply to any page
- Restating the title without adding task or outcome
- Marketing phrases such as `powerful`, `cutting-edge`, or `game-changing`

### Metadata optimization workflow

When adding or revising `description` fields:

- Review whether the current title and description match the page's actual task intent
- Use metadata descriptions to clarify what the learner will do, on which platform or tool, and with what outcome
- Treat the description as a search snippet, not a generic summary

### Recap section 

For Learning Paths, include a short recap paragraph and forward-looking transition at the end of each major instructional section or module

Example recap pattern for Learning Paths:

```md
## What you've learned and what's next

In this section:
- Briefly summarize what the user has learned or completed
- Briefly describe what the user should expect in the next section or suggest further exploration

Keep this concise and encouraging. Do not repeat earlier content verbatim.
```

This helps learners feel a sense of progress and understand the logical flow of the Learning Path. 

The recap for the last section of the Learning Path might not include a forward-looking transition and might recap the whole Path.

Use 'what you've learned' for conceptual sections and 'what you've accomplished' for task sections. 

### Hyperlink guidelines

When creating Learning Path content:
- Verify internal links exist before adding them
- Use semantic search or website browsing to confirm Learning Path availability
- Prefer verified external authoritative sources over speculative internal links
- Test link formats against existing Learning Path examples
- Never assume Learning Paths exist without verification

Put additional links in `further_reading` in `_index.md`, not `_next-steps.md`