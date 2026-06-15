---
name: stale-content-review
description: Scan Arm Learning Paths and install guides for stale-content risk. Use when the user asks to periodically flag content that may need maintenance, freshness review, dependency drift review, screenshot or UI review, latest or unpinned version review, or a report of likely stale pages.
---

# Stale content review

Use this skill to find Learning Paths and install guides that may need human maintenance review. This skill is report-only by default: flag risk, provide evidence, and leave fixes to the relevant owner unless the user explicitly asks for edits.

## Prerequisites

- Work from the repository root.
- Read `AGENTS.md` if routing or related skill selection is unclear.
- Read `references/staleness-signals.md` before interpreting scan results.

## Workflow

1. Identify the review scope. For periodic scans, default to `content/learning-paths` and `content/install-guides`.
2. Run `scripts/stale_content_scan.py` for a deterministic first pass.
3. Review the highest-scoring files and sample lines before drawing conclusions.
4. Summarize what each selected guide or page does, the dependencies or moving parts it relies on, and the review flags a human should consider.
5. Use related skills for focused follow-up:
   - `audit-images` for screenshot, image, alt text, and caption review.
   - `code-sample-review` for commands, package installs, outputs, and code fence integrity.
   - `arm-content-editor` for Arm terminology, product naming, and broader content judgment.
   - `link-text-review` for stale or vague external links that also need accessible anchor text.

## Validation rules

- Treat scan output as a triage queue, not proof that content is wrong.
- Do not invent replacement commands, versions, links, or product guidance.
- Do not open issues, move project cards, or edit content unless the user asks.
- Flag mutable dependencies, screenshots, UI flows, external services, unpinned versions, old dates, and version-specific instructions as review candidates.
- Be explicit when a flag is uncertain or only a heuristic signal.
- Keep periodic scan output lightweight enough for a reviewer to act on.
- Prefer questions and maintenance prompts over direct edits.

## Script usage

Run the default content scan:

```bash
python3 .github/skills/stale-content-review/scripts/stale_content_scan.py
```

The default broad scan reports files with score 20 or higher. Use `--min-score` to widen or narrow the queue.

Scan one Learning Path or install guide:

```bash
python3 .github/skills/stale-content-review/scripts/stale_content_scan.py content/install-guides/acfl.md
```

Write a Markdown report:

```bash
python3 .github/skills/stale-content-review/scripts/stale_content_scan.py --output stale-content-risk-report.md
```

Write JSON for later processing:

```bash
python3 .github/skills/stale-content-review/scripts/stale_content_scan.py --format json --output stale-content-risk-report.json
```

Include draft content when preparing unpublished material for review:

```bash
python3 .github/skills/stale-content-review/scripts/stale_content_scan.py --include-drafts
```

## Periodic workflow

`.github/workflows/stale-content-scan.yml` runs the broad scan every Monday at 10:00 UTC. It writes the first part of the report to the workflow summary and uploads the full Markdown report as `stale-content-risk-report`.

## Error handling

- If the scan returns too many candidates, increase `--min-score` or scan a narrower path.
- If a broad periodic scan returns too few candidates, lower `--min-score` to 15 or 12.
- If a file scores highly because of generated output or intentional version pinning, mark it as a lower-priority false positive in the review summary.
- If the workflow artifact is empty or unexpectedly small, rerun the script locally with the same path and threshold.
