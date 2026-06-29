---
name: seo-geo-aeo-review
description: Review and improve Arm Learning Paths and install guides for SEO, GEO, AEO, search snippets, AI-agent selection, and answer-engine readiness. Use when asked to optimize discoverability, search intent, AI-readable structure, page titles, headings, summaries, or content selection signals beyond only front matter descriptions.
---

# SEO, GEO, and AEO review

Use this skill when Arm Learning Paths or install guides need a focused discoverability review that goes beyond editing a single `description` field.

This skill covers:

- SEO: search snippets, titles, headings, metadata, and natural keyword usage.
- GEO: generative-engine selection signals, including authority, task coverage, and citation-ready structure.
- AEO: direct answer readiness for developer questions and AI-generated summaries.

For focused front matter `description` edits only, use `.github/skills/metadata-description-update/SKILL.md`.

## Prerequisites

- Work from the repository root.
- Read `AGENTS.md` only if you need repository routing context.
- Review `.github/skills/seo-geo-aeo-review/references/learning-paths-discoverability.md` only if you're reviewing a Learning Path.

## Workflow

1. Identify the target content type and target developer intent. 
2. Read the title, front matter description, headings, introduction, prerequisites, main task flow, validation, conclusion, and further reading. If you've previously read a page, use context and don't re-read it unless there's a change since the last read. 
3. State the page's owned task in one sentence. If the task is unclear or too broad, flag it.
4. Review SEO signals:
   - The title is task-led and includes the main technology, platform, or tool.
   - The `description` is one concise sentence that states the task, context, and outcome.
   - Headings expose the workflow and use natural developer search terms.
   - Keywords are specific and natural, not repeated for ranking.
5. Review GEO signals:
   - The page has clear Arm-specific authority and avoids generic advice that could apply anywhere.
   - Prerequisites, assumptions, and target platform are explicit.
   - Steps progress from preparation to configuration, usage, and validation.
   - The page avoids contradictions, duplicated instructions, and unsupported claims.
6. Review AEO signals:
   - The opening content answers what the reader will do and why it matters.
   - Sections are scannable and can be safely summarized out of context.
   - Validation steps prove the learner reached the promised outcome.
   - Troubleshooting, next steps, or further reading answer likely follow-up questions.
7. Provide suggestions based on findings in the format specified under `Response format`.
8. Make focused edits only when a reviewer requests you to implement changes that you suggested. When making edits, preserve technical meaning, front matter structure, Hugo shortcodes, links, commands, and code blocks.
9. After making updates, re-open changed sections and verify front matter, Markdown syntax, and internal links when practical.

## Review rules

- Optimize for selection and usefulness, not ranking alone.
- For Learning Paths, prefer verb-led titles such as `Install`, `Deploy`, `Configure`, `Analyze`, `Optimize`, or `Verify`. Install guides are named after the tool being installed and don't feature a verb because install is implied.
- Preserve content-type boundaries: install guides cover installation and verification; Learning Paths cover applied end-to-end tasks.
- Use Arm-specific terminology naturally when it is supported by the content.
- Don't add speculative keywords, unsupported performance claims, or marketing language.
- Don't overfit content to AI agents at the expense of human readability.

## Response format

For reviews, lead with findings ordered by severity and include file and line references when available. Then add open questions or assumptions, followed by a short summary.

For edits, summarize the changed SEO/GEO/AEO signals and note any checks performed.
