# Generate Summary/FAQ Tool

Use this tool to generate AI-assisted summary and FAQ content for Arm Learning
Path `_index.md` files. The generated content is stored in each Learning Path
front matter under `generated_summary_faq` and is intended as a reviewed draft,
not as automatically approved content.

The generator always uses the configured LLM endpoint. There is no offline or
template-only generation mode.

## What This Tool Does

The tool can:

- Generate a summary paragraph and five FAQ entries for selected Learning Paths.
- Store generated content in the matching Learning Path `_index.md`.
- Reset control flags after a successful write run so paths are not regenerated accidentally.
- Produce local `.txt`, `.yml`, and `.md` reports for each run.
- Process all Learning Paths, one category, one path, newly added paths, or edited paths.

The generated block is labeled AI-assisted in the rendered Learning Path page.
Generated text should still be reviewed by a human contributor before it is
treated as final site content.

## One-Time Setup

Set the Arm OpenAI proxy key in your shell before running the generator:

```bash
export OPENAI_API_KEY="..."
```

The wrapper defaults to the Arm proxy endpoint and `gpt-5`, but you can override
them if needed:

```bash
export OPENAI_BASE_URL="https://openai-api-proxy.geo.arm.com/api/providers/openai/v1/responses/"
export OPENAI_MODEL="gpt-5"
```

If Python cannot verify the company TLS certificate locally, prefer a CA bundle:

```bash
export OPENAI_CA_BUNDLE="/path/to/arm-ca-bundle.pem"
```

For local convenience, `tools/generate-summary-faq` automatically bypasses TLS
verification when no CA bundle is configured. This is intended only for local
testing against the Arm proxy. To force certificate verification, use:

```bash
tools/generate-summary-faq --all --dry-run --verify-tls
```

## Quick Start

Run all currently opted-in Learning Paths and write the generated content:

```bash
./generate-summary-faq
```

That shortcut is equivalent to:

```bash
tools/generate-summary-faq --all --write
```

Run a dry run first if you only want reports and no file edits:

```bash
tools/generate-summary-faq --all --dry-run
```

Run one category:

```bash
tools/generate-summary-faq --category laptops-and-desktops --write
```

Run one Learning Path:

```bash
tools/generate-summary-faq \
  --path content/learning-paths/laptops-and-desktops/wsl2 \
  --write
```

List available categories:

```bash
tools/generate-summary-faq --list-categories
```

## Control Flags

Each Learning Path uses three front-matter fields:

```yaml
author: Example Author

generate_summary_faq: true
rerun_summary: false
rerun_faqs: false

### Tags
```

Use the fields this way:

- `generate_summary_faq: true` opts the Learning Path into the next generator run.
- `generate_summary_faq: false` leaves the Learning Path out of normal generator runs.
- `rerun_summary: true` forces the summary to be regenerated.
- `rerun_faqs: true` forces the FAQs to be regenerated.

After a successful write run, the generator resets all three fields to `false`
for processed Learning Paths. This prevents repeated LLM calls unless a
contributor intentionally opts the path in again.

New Learning Paths scaffolded from `archetypes/learning-path/_index.md` should
place the fields after `author` and before `### Tags`:

```yaml
author: PLACEHOLDER NAME

generate_summary_faq: true
rerun_summary: false
rerun_faqs: false

### Tags
```

If you create a Learning Path by copying an existing folder, confirm these
fields manually in the copied `_index.md`.

## Set Flags

Use `set-summary-faq-flags` to prepare paths for generation without editing
front matter by hand.

Set all Learning Paths to regenerate both sections:

```bash
./set-summary-faq-flags --all --all-true
```

Reset all Learning Paths back to inactive:

```bash
./set-summary-faq-flags --all --all-false
```

Set one category to regenerate both sections:

```bash
./set-summary-faq-flags --category laptops-and-desktops --all-true
```

Set one Learning Path to regenerate both sections:

```bash
./set-summary-faq-flags \
  --path content/learning-paths/laptops-and-desktops/wsl2 \
  --all-true
```

Regenerate only FAQs for a category:

```bash
tools/set-summary-faq-flags \
  --category servers-and-cloud-computing \
  --generate-summary-faq true \
  --rerun-summary false \
  --rerun-faqs true
```

Regenerate only the summary for a category:

```bash
tools/set-summary-faq-flags \
  --category laptops-and-desktops \
  --generate-summary-faq true \
  --rerun-summary true \
  --rerun-faqs false
```

## New Or Edited Learning Paths

Most day-to-day use should be branch based. If your feature branch adds new
Learning Paths, compare it against the latest `origin/main`:

```bash
git fetch origin main
git checkout your-feature-branch
./set-summary-faq-flags --new-since origin/main --all-true
./generate-summary-faq
```

If your feature branch edits existing Learning Paths, use `--changed-since`:

```bash
git fetch origin main
git checkout your-feature-branch
./set-summary-faq-flags --changed-since origin/main --all-true
./generate-summary-faq
```

`--new-since` finds Learning Paths that exist on your branch but not on
`origin/main`. `--changed-since` finds Learning Paths changed on your branch
since `origin/main`, including newly added paths.

## When The LLM Is Called

The LLM is called only when at least one section needs work:

```text
generated_summary_faq is missing
summary is missing
FAQs are missing
rerun_summary is true
rerun_faqs is true
existing generated content used a non-AI generator
```

If a Learning Path already has generated content and both rerun flags are
`false`, the tool preserves the existing content and does not send that path to
the LLM.

Draft Learning Paths are skipped.

## Reports And Logs

Each run writes local artifacts under:

```text
reports/generated-summary-faq/
```

For a category or path run, the files are:

```text
<run-name>.txt  progress log and terminal-style output
<run-name>.yml  structured report with run details
<run-name>.md   Markdown report with review tables
```

For an all-path run, the tool creates one run directory:

```text
reports/generated-summary-faq/<run-name>/
run.txt          aggregate progress log for the whole command
run.yml          aggregate structured report for the whole command
run.md           aggregate Markdown report for the whole command
automotive.yml   per-category structured report
automotive.md    per-category Markdown report
...
```

Start with the aggregate `run.md`. It links to the per-category Markdown reports
when you need a deeper breakdown.

Each run also refreshes:

```text
reports/generated-summary-faq/latest-run.yml
reports/generated-summary-faq/latest-run.md
```

These files point to the most recent local run, so you do not have to guess
which timestamped folder was produced last.

Open a Markdown report locally:

```bash
open reports/generated-summary-faq/latest-run.md
```

Use `--run-name` to make report filenames predictable:

```bash
tools/generate-summary-faq \
  --category servers-and-cloud-computing \
  --run-name servers-and-cloud-computing \
  --write
```

## Timeout Tuning

For larger categories or occasional read timeouts, use smaller prompts and more
retries:

```bash
tools/generate-summary-faq \
  --category servers-and-cloud-computing \
  --timeout 180 \
  --retries 3 \
  --step-limit 5 \
  --excerpt-chars 600 \
  --write
```

## Recommended PR Flow

For a normal PR that adds or edits Learning Paths:

1. Update your branch from main.
2. Set flags for new or changed Learning Paths with `set-summary-faq-flags`.
3. Run `./generate-summary-faq`.
4. Review the generated `_index.md` changes and the Markdown report.
5. Edit or remove generated content if human review finds issues.
6. Run the site locally and confirm the generated block renders correctly.

For the initial bulk rollout, keep generated summary/FAQ content out of the PR.
The PR should include the tool, prompts, rendering, and default flags. The first
fresh generation can happen after the PR lands on main.
