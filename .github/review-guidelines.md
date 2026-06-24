# Maintenance review guidance

Use `.github/skills/stale-content-review/SKILL.md` for stale-content risk scans and maintenance triage.

The skill includes:

- A periodic scan workflow for Learning Paths and install guides.
- A deterministic script for finding likely stale-content signals.
- Reference guidance for interpreting temporal wording, screenshots, mutable dependencies, external links, old dates, and version-sensitive content.

For one-off manual reviews, run:

```bash
python3 .github/skills/stale-content-review/scripts/stale_content_scan.py <content-path>
```

No content changes are required unless explicitly requested.
