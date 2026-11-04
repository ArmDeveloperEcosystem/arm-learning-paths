---
name: intake-metadata-update
description: Mark Arm Learning Paths or install guides as draft during content intake.
---

# Update metadata during content intake

Use this skill to update draft visibility metadata during content intake. For Learning Path tag suggestions, install guide search-term suggestions, and broader front matter checks, use `.github/skills/frontmatter-audit/SKILL.md`.

Scenarios include:

- Updating the index when new Learning Path or install guide content needs to remain unpublished

Work from the repository root and preserve existing front matter values and order where possible. Don't edit anything else in the file.

## Workflow

1. Identify the target content and its metadata location:
   - Learning Path directory: `_index.md`.
   - Single-file install guide: its Markdown file.
   - Multi-page install guide or content bundle: `_index.md` or the main entry file, plus its child pages when setting draft status.
2. Perform the action requested. To mark content as draft, add the appropriate metadata:
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

   - For multi-page install guides, set `draft: true` in the entry file and each child Markdown page. Don't assume the entry file's draft setting hides the child pages.
## Response format

If you set content to draft, list the files updated.
