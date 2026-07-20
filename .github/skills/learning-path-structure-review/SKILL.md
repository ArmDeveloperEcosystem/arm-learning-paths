---
name: learning-path-structure-review
description: Review Arm Learning Paths for structural soundness, task ownership, scope discipline, progression, validation, further reading placement, recap sections, and performance-learning integrity. Use when asked to review, create, reorganize, or assess the structure of content under content/learning-paths.
---

# Learning Path structure review

Use this skill when a Learning Path needs a structural review. Focus on whether the content is organized to help a developer complete one clear task from preparation through validation.

## Workflow

1. Identify the Learning Path directory and read the relevant Markdown files together.
2. Summarize the developer task owned by LP in one sentence. If the task is unclear, too broad, or split across unrelated goals, flag it.
3. Check the required file shape:
   - The Learning Path has an `_index.md` file.
   - The Learning Path has an `_next-steps.md` file.
   - Additional resources and next steps live in `_index.md` `further_reading`, not in `_next-steps.md`.
   - `_next-steps.md` remains minimal and respects `FIXED, DO NOT MODIFY` template comments.
4. Review the instructional shape:
   - The title and opening of the Learning Path frame one developer task/job-to-be-done. 
   - The introduction gives context, user goal, and practical value.
   - Prerequisites are explicit and linked when useful.
   - Learning objectives are measurable, action-oriented, and limited to three or four bullets.
   - Sections progress logically through prepare, configure, use, and validate phases, with each section ideally focusing on one job-to-be-done. Flag nebulous sections with titles such as "working with x" or "managing y" that include multiple tasks that shouldn't be grouped together (e.g. creating and deleting a VM, or creating a VM and security group rules in the same section). 
   - Validation steps prove the learner reached the promised outcome.
   - The conclusion or next-step guidance names what the learner can do next.
5. Review `further_reading`:
   - Keep four to six essential resources.
   - Prefer direct relevance, Arm Learning Paths, required tools, foundation knowledge, and logical next steps.
   - Avoid link piles that pull readers away from the task.
6. Review recap and transition sections:
   - Include concise recap and forward-looking transition at major instructional boundaries. Do not treat a transition sentence alone as a recap. Note the absence of a transition as a finding. 
   - Use `what you've learned` for conceptual sections and `what you've accomplished` for task sections.
   - Avoid repeating earlier content verbatim.
7. If the Learning Path demonstrates Arm-specific performance features, apply the performance integrity checks.
8. Report findings by learner impact, with file and line references when available. Do not comment on content that is already structurally sound.

## Scope rules

- Learning Paths are not blog posts, reference articles, or install guides.
- A Learning Path should own one concrete developer task.
- Link to install guides for setup instead of duplicating install guide content.
- Preserve Hugo shortcodes, code fences, commands, links, front matter, and the author's technical intent when editing.
- Use repository search when structure, terminology, links, or task flow depends on related files.

## Performance integrity checks

For Learning Paths that demonstrate Arm-specific performance features, such as SME2, SVE2, I8MM, DotProd, or optimized microkernels:

- State the measurable improvement the learner will observe before deep architectural explanation.
- Show performance results before internal call stacks or microkernel details.
- Include toolchain or software version, device or platform, thread count, CPU affinity, runtime feature flags, and workload configuration when performance numbers are included.
- Label illustrative numbers clearly.
- Distinguish compile-time feature enablement, runtime feature activation, and automatic fallback behavior.
- Include a way to verify the accelerated path executed, such as logs, profiling output, kernel names, or hardware counters.
- Change only one meaningful benchmark variable at a time.
- Control thread count and CPU binding intentionally.
- Quantify percentage improvement explicitly.
- Connect observed improvement to the Arm architectural feature responsible for it.

## Response format

For reviews, lead with findings ordered by severity and include file and line references. Then add open questions or assumptions, followed by a short summary.

For edits, summarize the structural changes and note any checks performed.
