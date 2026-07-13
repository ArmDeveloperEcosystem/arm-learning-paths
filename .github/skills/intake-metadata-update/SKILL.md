---
name: intake-metadata-update
description: Add or verify draft metadata for new Arm Learning Paths and install guides before or after merge to main, so unreviewed content does not publish publicly. Use when asked to mark new content as draft, prepare new content for review, hide new Learning Paths or install guides from publication, or check draft metadata.
---

# Update metadata during content intake

Use this skill when new Learning Path or install guide content needs to remain unpublished until technical and editorial review is complete.

Work from the repository root and preserve existing front matter values and order where possible. Don't edit anything else in the file. 

## Workflow

1. Identify the target content:
   - Learning Path directory: edit its `_index.md`.
   - Single-file install guide: edit metadata in that Markdown file.
   - Multi-page install guide or content bundle: edit the `_index.md` or main entry file.
2. Add or update this metadata:
  - For Learning Paths:

    ```yaml
    draft: true
    cascade:
        draft: true
    ```

  - For single-page install guides:

    ```yaml
    draft: true
    ```

## Response format

List the file(s) that were updated. 