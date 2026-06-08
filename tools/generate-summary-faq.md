# Generate Summary/FAQ Tool

Use `tools/generate-summary-faq` to generate AI-assisted summary and FAQ content for Learning Path `_index.md` files.

The tool always uses the configured LLM endpoint. There is no template or offline generation mode.

## Prerequisites

Set your Arm OpenAI proxy key before running:

```bash
export OPENAI_API_KEY="..."
```

Optional endpoint configuration:

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
testing against the Arm proxy. If you want to force certificate verification,
use:

```bash
tools/generate-summary-faq --all --dry-run --verify-tls
```

You can also make the bypass explicit:

```bash
export OPENAI_INSECURE_SKIP_VERIFY="true"
```

## Common Runs

Default full generation for all opted-in Learning Paths:

```bash
./generate-summary-faq
```

The shortcut above is equivalent to:

```bash
tools/generate-summary-faq --all --write
```

Dry-run one category:

```bash
tools/generate-summary-faq --category automotive
```

Write generated content for one category:

```bash
tools/generate-summary-faq --category servers-and-cloud-computing --write
```

Write generated content for all eligible Learning Paths:

```bash
tools/generate-summary-faq --all --write
```

Process a single Learning Path:

```bash
tools/generate-summary-faq \
  --path content/learning-paths/servers-and-cloud-computing/nginx_tune \
  --write
```

List available categories:

```bash
tools/generate-summary-faq --list-categories
```

## Including or Excluding Learning Paths

By default, the generator only processes Learning Paths with this front-matter flag:

```yaml
generate_summary_faq: true
```

Set it to `false` to leave a Learning Path out of generated summary/FAQ runs:

```yaml
generate_summary_faq: false
```

After a successful write run, the tool resets `generate_summary_faq` to `false`
for every processed Learning Path. This keeps future runs from reprocessing
content unless a contributor intentionally opts the path in again.

The `rerun_summary` and `rerun_faqs` fields are separate controls. For a
Learning Path that already has generated summary/FAQ content, both fields can
stay `false`; the tool will report the path as unchanged and will not send that
Learning Path to the LLM again.

Set one or both rerun flags to force regeneration for an existing generated
section. After a successful write run, the tool resets both rerun flags to
`false`:

```yaml
rerun_summary: true
rerun_faqs: true
```

New Learning Paths scaffolded from `archetypes/learning-path/_index.md` start
with:

```yaml
generate_summary_faq: true
rerun_summary: false
rerun_faqs: false
```

If you create a Learning Path by copying an existing folder, confirm these
three fields manually in the copied `_index.md`.

The LLM is called only when at least one section needs work:

```text
generated_summary_faq is missing
summary is missing
FAQs are missing
rerun_summary is true
rerun_faqs is true
existing generated content used a non-AI generator
```

## Output

Each run writes three local artifacts under:

```text
reports/generated-summary-faq/
```

The files are:

```text
<run-name>.txt  progress log and terminal-style output
<run-name>.yml  structured report with latest run and retained history
<run-name>.md   local Markdown report with tables for review
```

When you run all Learning Paths, the tool still treats that as one parent run,
but it splits the actual work by top-level category to reduce timeout/context
risk. In that case, the artifacts are grouped in one run directory:

```text
reports/generated-summary-faq/<run-name>/
run.txt          aggregate progress log for the whole run
run.yml          aggregate structured report for the whole run
run.md           aggregate Markdown report for the whole run
automotive.yml   per-category structured report
automotive.md    per-category Markdown report
...
```

Use the aggregate `run.md` first. It links to the per-category Markdown reports
when you need the deeper breakdown.

Each run also refreshes these stable report snapshots:

```text
reports/generated-summary-faq/latest-run.yml
reports/generated-summary-faq/latest-run.md
```

Those snapshots point at the most recent local run data, so you do not have to
guess which timestamped folder was produced last. The per-command terminal log
remains in the run folder as `run.txt`.

Use `--run-name` to make output filenames predictable:

```bash
tools/generate-summary-faq \
  --category servers-and-cloud-computing \
  --run-name servers-and-cloud-computing \
  --write
```

That creates:

```text
reports/generated-summary-faq/servers-and-cloud-computing.txt
reports/generated-summary-faq/servers-and-cloud-computing.yml
reports/generated-summary-faq/servers-and-cloud-computing.md
```

For all Learning Paths:

```bash
tools/generate-summary-faq \
  --all \
  --run-name all-learning-paths-test \
  --write
```

That creates:

```text
reports/generated-summary-faq/all-learning-paths-test/run.txt
reports/generated-summary-faq/all-learning-paths-test/run.yml
reports/generated-summary-faq/all-learning-paths-test/run.md
```

Open the `.md` file locally to review the table-style run overview:

```bash
open reports/generated-summary-faq/servers-and-cloud-computing.md
```

The Markdown report is intentionally plain Markdown, so it can also be copied into a page or wired into a local Hugo-only report page later.

For example, to write the Markdown report somewhere else:

```bash
tools/generate-summary-faq \
  --category automotive \
  --markdown-report /tmp/automotive-summary-faq-report.md
```

## Timeout Tuning

For larger categories or occasional read timeouts, use smaller prompts and more retries:

```bash
tools/generate-summary-faq \
  --category servers-and-cloud-computing \
  --timeout 180 \
  --retries 3 \
  --step-limit 5 \
  --excerpt-chars 600 \
  --write
```
