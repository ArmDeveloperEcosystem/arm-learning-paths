# Generated Summary/FAQ Reports

This folder stores local reports and logs created by:

```bash
./generate-summary-faq
```

For a category or single-path run, expect files such as:

```text
<run-name>.txt  terminal-style progress log
<run-name>.yml  structured report data
<run-name>.md   Markdown report for human review
```

For an all-path run, the tool creates a timestamped folder:

```text
<run-name>/
  run.txt          aggregate progress log for the whole command
  run.yml          aggregate structured report for the whole command
  run.md           aggregate Markdown report for human review
  automotive.yml   per-category structured report
  automotive.md    per-category Markdown report
  ...
```

The tool also refreshes:

```text
latest-run.yml
latest-run.md
```

These point to the most recent local run. Future generation branches can include
the relevant reports and logs in a pull request when they are useful for review
or backtracking.
