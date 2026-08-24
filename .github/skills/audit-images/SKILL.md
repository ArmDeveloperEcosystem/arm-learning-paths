---
name: audit-images
description: Audit and fix Markdown image alt text in Arm Learning Paths and install guides. Use when the user asks to review images, find deficient alt text, count faulty images, run project-level or path-level image audits, track before/after image quality, or update image alt text and captions against repository image guidance.
---

# Audit images

## Description

Audit Markdown image references in Arm Learning Paths and install guides, report deficient alt text and image syntax, and help fix alt text with useful instructional descriptions.

Use the script for repeatable inventory and counting. Use assistant judgment for semantic alt-text quality and final edits.

## Prerequisites

- Work from the repository root.
- Read `AGENTS.md` to locate shared guidance.
- Read `references/image-guidance.md` before editing image alt text, captions, or image syntax.

## Trigger

Use this skill when the user asks to:

- Audit images or alt text.
- Find placeholder, vague, missing, malformed, or duplicated alt text.
- Count faulty images across the project or inside one Path/guide.
- Track image audit counts before and after fixes.
- Fix image alt text, captions, or `#center` syntax.

## Review levels

### Project-level review

Scan all Learning Paths and install guides unless the user gives a narrower scope.

Use project-level review to:

- Count total image references and faulty image references.
- Group faults by content unit and issue type.
- Identify high-priority directories or files for cleanup.
- Produce a before/after baseline for tracking progress.

Don't mass-edit the whole project unless the user explicitly asks. Prefer reporting the project-level inventory and then fixing one Path, guide, category, or batch.

### Path/guide-level review

Scan one Learning Path directory, install guide file, or install guide directory.

Use path/guide-level review to:

- List each faulty image with file, line, image path, current alt text, caption, and issue type.
- Inspect surrounding Markdown context before changing alt text.
- View local images when visual inspection is needed.
- Fix alt text and syntax in place.
- Re-run the audit and report before/after counts.

## Workflow

1. Identify whether the requested scope is project-level or path/guide-level.
2. Run `.github/skills/audit-images/scripts/audit_images.py` on that scope.
3. Record the baseline summary: total images, faulty images, content units affected, and issue counts.
4. Depending on the request level, do the following:
  - For project-level requests, summarize the results and suggest prioritized cleanup batches unless the user asked for edits.
  - For path/guide-level edit requests, inspect the relevant Markdown context and image files.
5. Suggest rewrites for deficient alt text using `references/image-guidance.md`.
6. After the reviewer accepts suggestions, rewrite text, then re-run the audit on the same scope.
7. Report before/after counts, files changed, and any remaining issues.

## Orphan and reference-integrity workflow

Use `scripts/orphan_images.py` when the task concerns unreferenced image files,
broken local image paths, filename case mismatches, or malformed Markdown image
destinations. This is separate from the alt-text audit so existing editorial
findings do not block image-integrity checks.

1. Run the checker in report mode before deleting anything.
2. Run `scripts/orphan_images.py --fix-references` to repair deterministic
   malformed, missing, and case-mismatched references. Review any ambiguous
   references that remain instead of guessing.
3. Render the site with Hugo and pass the output to `--generated-site`. The
   checker combines tracked source references, rendered references, exact Git
   blob matches, and unresolved-reference proximity to classify candidates.
4. Run `--delete-safe` to remove only high-confidence candidates. Without a
   rendered site, only byte-identical duplicates of referenced images qualify.
5. Review only the smaller `needs review` group. Do not maintain a repository-wide
   keep-list for historical candidates.
6. Re-run the checker and Hugo build after cleanup.

Case-colliding duplicate paths are removed from the Git index without deleting
the shared worktree file on case-insensitive systems. GitHub Actions never
writes deletions directly to the default branch. The Orphaned images cleanup
workflow performs one full, Hugo-rendered audit at 09:00 UTC on March 1
and September 1 and creates or updates a bot-owned cleanup PR when safe
candidates exist. Scheduled runs are restricted to the canonical Arm
repository; forks can still start manual runs. The workflow rebuilds Hugo and
verifies the staged deletion set before pushing that proposal branch. It writes
Markdown and JSON from one audit pass, then applies only manifest paths whose
Git blob IDs still match the audited snapshot. The PR is never auto-merged, and
`needs review` images remain untouched.

## Validation rules

- Treat the script as a detector, not the final authority. It flags likely problems for review.
- Use `references/image-guidance.md` as the source of truth for alt text, captions, placeholder text, `#center` syntax, and figure numbering.
- Don't replace meaningful alt text only because it is long or short; judge whether it helps the learner complete the task.
- Preserve valid local image paths and existing captions unless they are wrong, vague, or outdated.
- Preserve repository image syntax unless syntax cleanup is the target of the edit.

## Error handling

- If the script reports a missing local image path, verify whether the path is site-root-relative, file-relative, or intentionally external before changing content.
- If an image cannot be inspected, fix only issues that can be resolved from surrounding Markdown context and state the limitation.
- If project-level results are too large to edit safely, report the inventory and recommend a smaller batch.
- If the audit script and visual/context review disagree, explain the judgment and leave a short note in the final response.

## Script usage

Run a project-level audit:

```bash
python3 .github/skills/audit-images/scripts/audit_images.py
```

Run a path-level audit:

```bash
python3 .github/skills/audit-images/scripts/audit_images.py content/learning-paths/servers-and-cloud-computing/example-path
```

Write JSON for tracking:

```bash
python3 .github/skills/audit-images/scripts/audit_images.py --format json --output image-audit.json
```

Report image-integrity problems without changing files:

```bash
python3 .github/skills/audit-images/scripts/orphan_images.py
```

Fail when any current problems exist:

```bash
python3 .github/skills/audit-images/scripts/orphan_images.py --check
```

Apply deterministic reference repairs in bulk:

```bash
python3 .github/skills/audit-images/scripts/orphan_images.py --fix-references
```

Build the site and classify candidates with independent rendered evidence:

```bash
hugo --destination /tmp/arm-learning-paths-image-integrity
python3 .github/skills/audit-images/scripts/orphan_images.py \
  --generated-site /tmp/arm-learning-paths-image-integrity
```

Delete only candidates supported by the available confidence evidence:

```bash
python3 .github/skills/audit-images/scripts/orphan_images.py \
  --generated-site /tmp/arm-learning-paths-image-integrity \
  --delete-safe
```

Use the **Orphaned images cleanup** workflow's **Run workflow** control to start
the same full Hugo-backed audit without waiting for the six-month schedule.
Select **Create cleanup PR** to propose verified safe deletions, or leave it
clear for a report-only run. Scheduled canonical-repository runs automatically
create or update the proposal. Pushes and pull requests do not trigger this
workflow.
The repository's Actions settings must grant the workflow token read/write
access and allow GitHub Actions to create pull requests. If those permissions
are disabled, the audit report still completes before the proposal step fails.

Every workflow report lists the actionable `needs review` group even when those
images are historical. Markdown reports link each protected image and related
source line, explain why automatic deletion was blocked, and recommend the next
review action. The full audit uses both source references and the rendered Hugo
site to avoid treating images used by published pages as safe to delete.
The cleanup PR contains deletion-only content changes, links every proposed
deletion at the audited commit, and links the protected review group. Before
opening the PR, the workflow requires the staged deletions to exactly match the
JSON dry-run manifest, rebuilds the complete site, and rejects any newly
introduced non-orphan problem. Rendered-site scans skip copied raster images
before reading file contents while retaining text-based SVG reference checks.

For a manual Git cleanup, build Hugo first and let the checker stage only the
safe deletion set:

```bash
hugo --destination /tmp/arm-learning-paths-image-integrity
python3 .github/skills/audit-images/scripts/orphan_images.py \
  --generated-site /tmp/arm-learning-paths-image-integrity \
  --delete-safe
git diff --cached --name-status
git diff --cached --stat
```

Review the staged deletion list before committing. The automated workflow uses
the same `safe_delete_images` list and adds the post-deletion verification and
pull-request boundary.
