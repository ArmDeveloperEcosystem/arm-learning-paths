---
name: refactor-learning-path-editorial
description: Audit and refactor an existing Arm Learning Path for editorial structure, front matter, discoverability, writing style, accessibility, images, links, Markdown presentation, and code-sample presentation without changing technical instructions. Use when modernizing older content under content/learning-paths, applying multiple editorial skills as one controlled workflow, or requesting an editorial-only Learning Path cleanup with review and verification gates.
---

# Refactor a Learning Path editorially

Refactor one Learning Path through independent review, a deduplicated findings ledger, sequential edits, and a cold verification pass. Preserve technical truth and defer technical review.

## Prerequisites

- Work from the repository root.
- Read every Markdown file in the selected Learning Path together.
- Read [references/finding-contract.md](references/finding-contract.md) before starting reviewer agents or recording findings.
- Record the initial `git status --short`. Preserve unrelated and pre-existing changes.

## Editorial boundary

Include:

- Task ownership, page organization, progression, introductions, objectives, recaps, transitions, validation framing, and further-reading placement.
- Front matter validity and editorial metadata, including titles and descriptions.
- SEO, GEO, AEO, headings, style, voice, readability, terminology, descriptive link text, image guidance, alt text, captions, and Markdown presentation.
- Explanatory prose around commands, code, and output; code-fence integrity and language tags.

Exclude:

- Technical accuracy, freshness, performance integrity, dependency drift, and version verification.
- Changes inside commands, code samples, configuration, expected output, URLs, or technical Hugo shortcodes.
- New claims about compatibility, performance, prerequisites, supported platforms, tools, or results.

Treat `armips`, `tools_software_languages`, `operatingsystems`, `platforms`, `subjects`, `skilllevels`, and `minutes_to_complete` as protected metadata. Reviewers may flag missing, invalid, or inconsistent values, but must mark the finding `needs-human-review` and must not invent or apply a replacement. Adding, removing, or changing a `further_reading` destination also requires human review; descriptive edits to existing resource titles do not.

If an editorial issue appears to require a technical change, record it as `deferred-technical` and leave the source unchanged. Do not use `stale-content-review`, technical mode from `code-sample-review`, or performance-integrity checks in this workflow.

## Workflow

### 1. Establish scope and baseline

1. Resolve exactly one Learning Path directory unless the user explicitly requests a batch.
2. Inventory all Markdown files and state the Learning Path's owned developer task in one sentence.
3. Create an editorial guard snapshot in a temporary location:

   ```bash
   python3 .github/skills/refactor-learning-path-editorial/scripts/editorial_guard.py snapshot <path> --output <temporary-json>
   ```

4. Run the image audit on the same path and record its baseline counts.
5. Treat file additions, deletions, renames, and page splits as `needs-human-review` unless explicitly requested.

### 2. Run independent editorial reviews

If subagents are available, start these project agents in parallel and wait for both:

- `lp_editorial_architecture_reviewer`
- `lp_editorial_presentation_reviewer`

Give each agent the exact directory, ask it to read all files in scope, and require the finding contract. Review agents must remain read-only.

If subagents are unavailable, perform the same two reviews sequentially in the current agent while keeping their findings separate.

The architecture reviewer applies:

- `.github/skills/learning-path-structure-review/SKILL.md`, excluding performance integrity.
- `.github/skills/frontmatter-audit/SKILL.md`.
- `.github/skills/metadata-description-update/SKILL.md` for description findings.
- `.github/skills/seo-geo-aeo-review/SKILL.md`.

The presentation reviewer applies:

- `.github/skills/writing-style-review/SKILL.md`.
- `.github/skills/link-text-review/SKILL.md`.
- `.github/skills/audit-images/SKILL.md` and its required image guidance.
- `.github/skills/code-sample-review/SKILL.md` in editorial mode only.
- `.github/skills/markdown-component-edit/SKILL.md` only for a component the user explicitly requested.

### 3. Build the findings ledger

Merge and deduplicate the reviewer results. Keep one ledger entry per distinct problem. Do not discard a finding silently.

For an explicit refactor request, mark low- and medium-risk editorial findings `accepted` when their correction preserves meaning. Mark these `needs-human-review`:

- File splits, merges, renames, or deletions.
- Reordering that could change the procedure.
- Changes to prerequisites or validation criteria.
- Changes to protected metadata or `further_reading` destinations.
- Ambiguous wording whose resolution requires domain knowledge.
- Any proposed change to protected technical content.

Report review coverage before editing. Every expected file and applicable skill must be accounted for.

### 4. Apply accepted fixes sequentially

Use `lp_editorial_fixer` when available. Give it only the accepted ledger, scope, and guard location. Do not ask it to rediscover or broaden the work.

Apply fixes in this order:

1. Learning Path structure and task framing.
2. Front matter and descriptions.
3. Headings, introductions, recaps, transitions, and validation framing.
4. Links, images, alt text, captions, and code-sample presentation.
5. Writing style and terminology.

After each category, inspect the diff and update every affected ledger entry to `fixed`, `unresolved`, or `deferred-technical`.

Do not generate or edit `generated_summary_faq` unless the user explicitly includes it. If included, run `.github/skills/summary-faq-workflow/SKILL.md` last, after the source pages are stable.

### 5. Verify independently

Run the guard against the final files:

```bash
python3 .github/skills/refactor-learning-path-editorial/scripts/editorial_guard.py verify <path> --baseline <temporary-json>
```

A guard failure is not automatically an error, but every reported difference must correspond to an explicitly accepted change. Restore accidental technical changes.

Then:

1. Re-run the image audit and compare counts.
2. Parse the edited front matter and check unique public page weights.
3. Check changed Markdown, shortcode pairs, links, and code fences.
4. Run `git diff --check`.
5. Confirm that only allowed files changed.
6. Use `lp_editorial_verifier` for a cold, read-only review when available. Give it the final files and scope, but not the original reviewers' reasoning. Ask it to apply the relevant skills and verify each ledger entry separately.

Do not declare completion while an accepted finding remains `found`, `accepted`, or `fixed` but unverified.

## Final response

Report:

- The one-sentence developer task.
- Changed files.
- Before-and-after counts by review category.
- Checks run and their results.
- Ledger entries still unresolved, `needs-human-review`, or `deferred-technical`.
- Confirmation that protected technical content was unchanged, or an itemized explanation of intentional guard differences.

## Error handling

- If reviewer results omit files or applicable skills, rerun only the missing coverage.
- If reviewers disagree, preserve both findings and let the coordinator resolve them from repository evidence.
- If the guard baseline is missing, recreate it before editing; do not reconstruct a pre-edit baseline afterward.
- If existing user changes overlap the target, preserve them and distinguish them from this workflow's diff.
- If completing an edit requires technical judgment, defer it instead of guessing.
