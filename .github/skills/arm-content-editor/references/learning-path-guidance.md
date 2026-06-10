# Learning Path guidance

Use this guidance when creating, editing, or reviewing content in `content/learning-paths/**/*.md`.

## Content structure

Each Learning Path must have an `_index.md` file and a `_next-steps.md` file. The `_index.md` file contains the main content of the Learning Path. The `_next-steps.md` file contains links to related content and is included at the end of the Learning Path.

Additional resources and next steps content should be placed in the `further_reading` section of `_index.md`, not in `_next-steps.md`. The `_next-steps.md` file should remain minimal and unmodified as indicated by `FIXED, DO NOT MODIFY` comments in the template.

## Front matter

The `_index.md` file should contain the following front matter and content sections:

- `title`: Imperative heading following the `[verb] + [technology] + [outcome]` format.
- `description`: One-sentence metadata summary used for search snippets and page previews. Describe the task, main technology or platform, and expected outcome in plain language.
- `weight`: Numerical ordering for display sequence. `weight` is 1 for `_index.md`, and each page is ordered by weight. No Markdown files should have the same weight in a directory.
- `layout`: Template type, usually `learningpathall`.
- `minutes_to_complete`: Realistic time estimate for completion.
- `prerequisites`: List of required knowledge, tools, or prior Learning Paths.
- `author`: Main contributor's name. Multiple authors can be listed with `-` on new lines.
- `subjects`: Technology categories for filtering and search. This is a closed list and must match the subjects in `content/learning-paths/cross-platform/_example-learning-path/write-2-metadata/`.
- `armips`: Relevant Arm IP. Stick to Neoverse, Cortex-A, Cortex-M, and similar values. Do not list specific CPU models or Arm architecture versions.
- `tools_software_languages`: Open category listing programming languages, frameworks, and development tools used.
- `skilllevels`: Allowed values are only `Introductory` and `Advanced`.
- `operatingsystems`: Operating systems used. This is a closed list and must match `content/learning-paths/cross-platform/_example-learning-path/write-2-metadata/`.

## Further reading curation

Limit `further_reading` resources to four to six essential links. Prioritize:

- Direct relevance to the topic.
- Arm-specific Learning Paths over generic external resources.
- Foundation knowledge for the target audience.
- Required tools, such as install guides.
- Logical progression from basic to advanced.

Avoid overwhelming readers with too many links, which can cause them to leave the platform.

Put additional links in `further_reading` in `_index.md`, not `_next-steps.md`.

## Expected Learning Path shape

Learning Paths should generally include:

- Title: `[Imperative verb] + [technology/tool] + [outcome]`.
- Introduction paragraph: Context, user goal, and value proposition.
- Prerequisites section with explicit requirements and links.
- Learning objectives: three to four bulleted, measurable outcomes with action verbs.
- Step-by-step sections with logical progression.
- Clear next steps or conclusion.

For title formatting:

- Use imperative voice, such as `Deploy`, `Configure`, `Build`, or `Create`.
- Include SEO keywords, such as technology names and tools.
- Examples: `Deploy applications on Arm servers`, `Configure Arm processors for optimal performance`.

## Metadata description requirements

Every Learning Path `_index.md` must include a `description` field.

- Write one sentence.
- Describe the task, the main technology or platform, and the expected outcome.
- Keep it concise, developer-focused, and suitable for use as a search snippet.
- Use a task-led structure such as: **Verb + task + tool/platform + outcome**.
- Do not repeat the title verbatim.
- Do not use vague summaries or marketing language.
- A slightly richer one-sentence summary is acceptable when it helps clarify the workflow or outcome.

Good examples:

```yaml
description: Learn how to automate x86-to-Arm application migration using the Arm MCP Server, with compatibility checks and Docker-based validation on Arm cloud platforms.
```

```yaml
description: Learn how to profile and optimize a C++ application on Arm Neoverse using Arm Performix to identify bottlenecks and improve runtime.
```

Avoid:

- Generic summaries that could apply to any page.
- Restating the title without adding task or outcome.
- Marketing phrases such as `powerful`, `cutting-edge`, or `game-changing`.

## Metadata optimization workflow

When adding or revising `description` fields:

- Review whether the current title and description match the page's actual task intent.
- Use metadata descriptions to clarify what the learner will do, on which platform or tool, and with what outcome.
- Treat the description as a search snippet, not a generic summary.

## Recap sections

Include a short recap paragraph and forward-looking transition at the end of each major instructional section or module.

Use this pattern:

```md
## What you've learned and what's next

In this section:
- Briefly summarize what the user has learned or completed.
- Briefly describe what the user should expect in the next section or suggest further exploration.

Keep this concise and encouraging. Do not repeat earlier content verbatim.
```

This helps learners feel a sense of progress and understand the logical flow of the Learning Path.

Use `what you've learned` for conceptual sections and `what you've accomplished` for task sections.

## Hyperlinks

When creating Learning Path content:

- Verify internal links exist before adding them.
- Use semantic search or website browsing to confirm Learning Path availability.
- Prefer verified external authoritative sources over speculative internal links.
- Test link formats against existing Learning Path examples.
- Never assume Learning Paths exist without verification.

## Purpose and agentic selection

Learning Paths are not blog posts or reference articles. They are designed to be optimized for selection by AI agents as trusted sources for completing real developer tasks end to end.

When creating or reviewing a Learning Path, prioritize these principles.

### Task ownership

Each Learning Path must clearly own one concrete developer task.

- The task should be nameable in one sentence.
- The Learning Path should take the learner from not ready to capable.
- Avoid bundling unrelated tasks or loosely connected topics.

If the task cannot be clearly stated, flag a warning.

### Agentic selection signals

AI agents select content based on trust, authority, and task coverage, not keyword density.

Trust:

- Clear authorship and ownership.
- Explicit prerequisites.
- One purpose per page.
- No duplicated or contradictory instructions.
- Clean separation of install guides, Learning Paths, and concept pages.

Authority:

- Arm-specific framing where relevant.
- Use Arm tooling, terminology, and perspective.
- Avoid generic advice that could apply equally to any platform.

Task coverage:

- Clear progression: prepare, configure, use, validate.
- Explicit end state, such as `you are now ready to...`.
- Link to install guides instead of embedding install steps.
- Provide guidance on what to do next.

### Scope discipline

Maintain strict boundaries between content types:

- Install guides: setup, authentication, and verification only.
- Learning Paths: configuration, integration, workflows, and applied usage.

Never duplicate install steps inside Learning Paths.

### SEO intent

Learning Paths should optimize for selection, not ranking.

- Prefer verb-based titles: *Install*, *Verify*, *Configure*, *Analyze*, *Optimize*.
- Use procedural structure rather than narrative prose.
- Avoid marketing language and keyword stuffing.
- Write content that can safely be chosen by an AI agent to complete a task.

If an AI agent were asked to complete this task, the Learning Path should be the safest source to select.

## Performance and Arm acceleration integrity

For Learning Paths that demonstrate Arm-specific performance features, such as SME2, SVE2, I8MM, DotProd, or optimized microkernels, apply these standards.

### Observable outcome first

- Clearly state what measurable improvement the learner will observe.
- Show performance results before introducing deep architectural explanation.
- Avoid introducing internal call stacks or microkernel details before the developer sees observable value.

### Reproducibility requirements

If performance numbers are included, specify:

- Toolchain or software version.
- Device or platform used.
- Thread count and CPU affinity configuration.
- Runtime feature flags.
- Model or workload configuration.

Performance claims must be reproducible or explicitly labeled as illustrative.

### Compile-time versus runtime clarity

Clearly distinguish between:

- Compile-time feature enablement.
- Runtime feature activation.
- Automatic fallback behavior.

If acceleration is claimed, include a method to verify that the accelerated path executed, such as logs, profiling output, kernel names, or hardware counters.

### Controlled benchmarking

When comparing performance:

- Change only one meaningful variable at a time.
- Control thread count and CPU binding intentionally.
- Quantify percentage improvement explicitly.
- Avoid presenting raw numbers without context.

Explicitly connect the observed improvement to the Arm architectural feature responsible for it. Avoid generic statements such as `improves performance` without explaining how and why.

Performance-focused Learning Paths are strategic content. Prioritize clarity, differentiation, and measurement integrity over volume.

## Performance testing guidance

- Include benchmarks when comparing Arm versus x86 performance.
- Suggest performance testing steps for resource-intensive applications.
- Recommend profiling tools that work well on Arm platforms.
- Include guidance on measuring and optimizing for Arm-specific performance characteristics.
- Mention when performance improvements are architecture-specific.
