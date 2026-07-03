---
name: draft-learning-path
description: "Toggle draft mode on a Learning Path _index.md. Use when: marking a learning path as draft, hiding a learning path from publication, adding draft: true to front matter, unpublishing or disabling a learning path, removing draft, publishing a learning path, taking a learning path out of draft."
---

# Draft Learning Path

Sets `draft: true` and `cascade: draft: true` in the front matter of a Learning Path `_index.md` file so the page and all its child pages are excluded from the published site.

For new content intake where the goal is to prevent unreviewed content from publishing, use `.github/skills/intake-metadata-update/SKILL.md` instead.

## Draft block to insert

The following YAML must be added to the front matter, after the `title:` field. Leave a blank line between `title:` and the draft block for readability:

```yaml
title: Your Learning Path Title

draft: true
cascade:
    draft: true
```

## Workflow

1. **Identify the target file**
   - If the user specifies a path, use that.
   - Otherwise, use the currently open or most recently edited `_index.md` file in the workspace.
   - Confirm the file is a Learning Path `_index.md` (contains Hugo front matter between `---` markers).

2. **Read the file**
   - Read the file to inspect the existing front matter.

3. **Apply the draft block**
   - If `draft: true` and `cascade:` with `draft: true` already exist, inform the user it is already in draft mode and stop.
   - If a `draft:` field exists but no `cascade:` block, replace the existing `draft:` line with the full draft block above.
   - If no `draft:` field exists, insert the draft block after the `title:` field, with a blank line between them.

4. **Confirm**
   - Report the file path and confirm the draft block has been set.
   - Remind the user that Hugo will exclude this file and all child pages from the built site until the draft block is removed.

## Undraft workflow

If the user asks to publish, undraft, or remove draft mode:

1. **Identify the target file** (same as above).
2. **Read the file** to locate the draft block.
3. **Remove the draft block**
   - Remove the `draft: true` line.
   - Remove the `cascade:` block (`cascade:` and its indented `draft: true` child line).
   - Remove any blank line that was added between `title:` and the draft block, restoring the original spacing.
   - If no draft block exists, inform the user the file is already published and stop.
4. **Confirm**
   - Report the file path and confirm draft mode has been removed.
   - Remind the user the Learning Path will now appear on the published site.
