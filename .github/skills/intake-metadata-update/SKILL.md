---
name: intake-metadata-update
description: Mark Arm Learning Paths or install guides as draft, or suggest content-based Learning Path tags and install guide search terms during metadata intake.
---

# Update metadata during content intake

Use this skill to update draft metadata or suggest content-based metadata values.

Scenarios include:

- Updating the index when new Learning Path or install guide content needs to remain unpublished
- Suggesting tags based on the content of a Learning Path
- Suggesting search terms based on the content of an install guide

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
3. For Learning Path tag suggestions, read the Learning Path and check its existing metadata and relevant repository examples before suggesting values for:
   - `tools_software_languages`
   - `operatingsystems`
   - `armips`

   Use the repository's allowed values where a field has a closed list. Base each suggestion on the content; if a field has no supported value, say so instead of guessing. Treat these fields as protected metadata: propose values for human review, and don't apply them unless the user explicitly approves the values.
4. For install guide search-term suggestions, read the guide and its existing `additional_search_terms`, then suggest only terms supported by the content. Check relevant repository examples for spelling and style.

## Response format

If you set content to draft, list the files updated. For tag or search-term suggestions, list proposed values and a brief content-based rationale for each; identify any fields for which you can't support a suggestion.
