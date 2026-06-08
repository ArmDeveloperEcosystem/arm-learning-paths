---
name: intake-metadata-update
description: Add or verify draft metadata for new Arm Learning Paths and install guides before or after merge to main, so unreviewed content does not publish publicly. Use when asked to mark new content as draft, prepare new content for review, hide new Learning Paths or install guides from publication, or check draft metadata.
---

# Update metadata during content intake

Use this skill when new Learning Path or install guide content needs to remain unpublished until technical and editorial review is complete.

## Workflow

1. Work from the repository root.
2. Identify the target content:
   - Learning Path directory: edit its `_index.md`.
   - Single-file install guide: edit metadata in that Markdown file.
   - Multi-page install guide or content bundle: edit the `_index.md` or main entry file.
3. Preserve existing front matter order and values where possible.
4. Add or update this metadata in front matter for Learning Paths:

```yaml
draft: true
cascade:
    draft: true
```

5. Add or update this metadata in front matter for single-page install guides:

```yaml
draft: true
```