# Editorial finding contract

Use this schema for every reviewer result and for the combined ledger.

```yaml
reviewer: lp_editorial_architecture_reviewer
scope: content/learning-paths/category/path
owned_task: Configure a tool on Arm Linux and verify the requested outcome.
coverage:
  expected_files: 5
  files_read: 5
  skills_required:
    - learning-path-structure-review
  skills_completed:
    - learning-path-structure-review
findings:
  - id: ARCH-001
    severity: high
    category: validation-framing
    file: 03-run.md
    line: 42
    evidence: The page ends after starting the service and does not explain how the existing output demonstrates success.
    proposed_action: Explain what the existing output proves without changing the command or output.
    risk: medium
    status: found
limitations: []
```

## Required values

Use these severities:

- `high`: Blocks task comprehension, creates a misleading promise, or prevents the reader from knowing whether they succeeded.
- `medium`: Causes confusion, weak navigation, inconsistent metadata, or a material accessibility problem.
- `low`: Local style, wording, formatting, or presentation issue.

Use these risk values:

- `low`: Mechanical editorial correction that cannot reasonably change technical meaning.
- `medium`: Contextual rewrite or reorganization that needs careful diff inspection.
- `high`: Could affect procedure, prerequisites, validation criteria, or technical meaning.

Use these statuses:

- `found`
- `accepted`
- `needs-human-review`
- `fixed`
- `verified`
- `unresolved`
- `deferred-technical`
- `rejected`

## Completeness rules

- Include every Markdown file in the expected and read counts, including `_index.md` and `_next-steps.md`.
- Report a required skill as completed even when it produces zero findings.
- Give file and line evidence for each finding when possible.
- Do not report content that is already sound.
- Do not combine unrelated problems into one finding.
- Do not silently omit uncertain issues; use `needs-human-review` or `deferred-technical`.
