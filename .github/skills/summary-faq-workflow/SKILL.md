---
name: summary-faq-workflow
description: Generate, style-review, and patch AI-assisted Learning Path summaries and FAQs for one path, a path subset, a category, or the repository. Use when summary/FAQ metadata needs generation followed by automatic editorial cleanup.
---

# Summary and FAQ workflow

Use this skill when a user asks to generate, review, or style-fix the
`generated_summary_faq` block in Learning Path `_index.md` files.

If subagents are available, use three roles:

- **Generator:** resolve scope, set the flags, and run `tools/generate-summary-faq`.
- **Reviewer:** read-only review of generated summaries and FAQs.
- **Fixer:** apply reviewer findings and validate the edited blocks.

If subagents are unavailable, perform the same phases in the current agent.

## Workflow

The following are the steps in greater detail:

1. Resolve the requested scope: one path, a comma-separated path list, one
   category, or all Learning Paths.
2. Run
   `tools/generate-summary-faq` depending on the scope if the request is to generate summaries and FAQs. The generator writes content in the
   current branch only when `--write` is supplied. If generation fails due to credential or network issues, echo the error message and exit. Don't try to manually generate summaries and FAQs.
3. After successful generation, review only the selected generated blocks against
   `.github/skills/writing-style-review/SKILL.md`, the mandatory style and factual checklist in this skill, and the source Learning Path pages. Follow the same step for reviewing previously generated summaries and faqs.
4. Using the mandatory checklist, apply style and factual corrections without asking for an approval step. Do not assume
   the generator followed the writing-style guidance.
5. Validate the selected paths by parsing front matter, checking the five-FAQ
   contract, and running `git diff --check`.
6. Return a patch-oriented summary listing changed files, style corrections,
   skipped paths, credential-refresh status, and validation results.

Run generation and fixing sequentially because all agents share the working
tree. 

## Scope commands

```bash
# Example for one Learning Path. Replace `--path` with `--category` or `--all`
# when needed, and pass the same target to both commands.
tools/set-summary-faq-flags \
  --path content/learning-paths/category/path \
  --all-true
tools/generate-summary-faq \
  --path content/learning-paths/category/path \
  --write
```

Pass generator options after the scope, such as `--run-name`, `--timeout`, or
`--retries`. For a dry run, use `--dry-run` on both commands and add
`--allow-unflagged` to the generator command.

When you get a request to generate a specific number of summaries and FAQs, or to generate them for a subset of a category, use bash scripts such as the following:

```bash
PATHS=$(for f in content/learning-paths/servers-and-cloud-computing/*/_index.md; do
  if ! rg -q '^draft:\s*true\b|^\s+draft:\s*true\b' "$f" &&
     ! rg -q '^generated_summary_faq:' "$f" &&
     rg -q '^generate_summary_faq:\s*true\b' "$f"; then
    dirname "$f"
  fi
done | sed -n '1,20p' | paste -sd, -)

tools/generate-summary-faq \
  --path "$PATHS" \
  --write \
  --run-name servers-and-cloud-computing-summary-faq-01
```
Update the URL and the number of summaries as necessary.


## Style and factual review

Apply `.github/skills/writing-style-review/SKILL.md` as the canonical source
for voice, readability, terminology, formatting, and list style. Keep the
technical meaning grounded in the Learning Path source pages.

In addition, check that summaries orient the reader without repeating metadata
or objectives, FAQs answer practical step-level questions, and factual claims
remain narrower than or equal to the source content. Make sure the first sentence in the summary sums the Learning Path up in one sentence, and the subsequent sentences summarize the sections sequentially. 

### Mandatory voice and format checklist

Review every sentence in each selected summary for direct second-person voice.
Use `you` or `your` when describing what the reader does, learns, configures,
or verifies. Do not accept passive or third-person language such as `This Learning Path`,
`Learners`, `the path`, `the implementation`, `the steps`, `the result`, or
`they` when those phrases describe the reader's work. Rewrite those sentences
to address the reader directly. To avoid sounding robotic, vary the phrases in length and phrasing without losing technical accuracy. Keep summaries about 50-60 words long whenever possible. 

FAQ answers must follow the same second-person
voice. FAQ questions may use first person when phrased from the reader's
perspective.

Make sure all UI and code elements are formatted correctly.

Run this deterministic check after editing. It must report zero matches for the
selected generated blocks; then perform the sentence-level review because a
clean scan does not prove that every sentence uses second person:

```bash
for f in <selected-_index.md-files>; do
  sed -n '/^  summary:/,/^  faqs:/p' "$f" |
    rg -n -i 'This Learning Path|Learners|\blearners\b|\bthe path\b|\bthe implementation\b|\bthe steps\b|\bthe result\b|\bthey\b' && exit 1
done
```

Edit only `generated_summary_faq.summary` and `generated_summary_faq.faqs`;
preserve the generated metadata, source hashes, timestamps, control flags, and
body content.

Do not invent commands, compatibility claims, performance results, tools, or
prerequisites. Always rely on the Learning Path for information. If the source is ambiguous, preserve the narrower claim and
report the uncertainty. 

## Validation

Parse the selected front matter and confirm that each generated block contains
one non-empty summary and exactly five question and answer pairs. Run:

```bash
git diff --check
```

Confirm that drafts skipped by the generator remain unchanged and that only
the requested Learning Path index files were edited.

## Resources

- `tools/generate-summary-faq` handles generation and reports.
