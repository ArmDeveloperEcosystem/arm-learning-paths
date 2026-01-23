#!/bin/bash
# Generate a spell check configuration that only includes non-draft files
# This script finds all markdown files EXCEPT those in draft Learning Paths

cd "$(dirname "$(dirname "${BASH_SOURCE[0]}")")" || exit 1

output_config=".spellcheck-non-draft.yml"

# Find all draft directories first
echo "Finding draft Learning Paths..."
draft_file_list=$(find content/learning-paths -type f -name "_index.md" -exec grep -l "^draft: true$" {} \; 2>/dev/null)
draft_dirs=()
while IFS= read -r file; do
  # Only mark entire directory as draft if it has cascade directive
  if grep -q "^cascade:" "$file" 2>/dev/null; then
    dir=$(dirname "$file")
    draft_dirs+=("$dir")
  fi
done <<< "$draft_file_list"

echo "Found ${#draft_dirs[@]} draft Learning Path(s) with cascade"
[[ ${#draft_dirs[@]} -gt 0 ]] && printf 'Draft dirs: %s\n' "${draft_dirs[@]}"

# Write base config template
cat > "$output_config" << 'EOF'
matrix:
- name: Markdown
  expect_match: false
  apsell:
    mode: en
  dictionary:
    wordlists:
    - .wordlist.txt
    output: wordlist.dic
    encoding: utf-8
  pipeline:
  - pyspelling.filters.markdown:
      markdown_extensions:
      - markdown.extensions.extra:
  - pyspelling.filters.html:
      comments: false
      attributes:
      - alt
      ignores:
      - ':matches(code, pre)'
      - 'code'
      - 'pre'
      - 'blockquote'
  sources:
EOF

echo "Building sources list (excluding drafts)..."

# Collect and add install guide files (excluding drafts)
install_count=0
while IFS= read -r file; do
  # Check if this install guide is marked as draft (allowing trailing whitespace)
  if ! grep -q "^draft: true[[:space:]]*$" "$file" 2>/dev/null; then
    echo "  - '$file'" >> "$output_config"
    ((install_count++))
  fi
done < <(find content/install-guides -name "*.md" -type f | sort)
echo "Found $install_count non-draft install guide file(s)"

# Collect and add non-draft learning path files
lp_count=0
while IFS= read -r file; do
  # Check if this file is in a cascade-draft directory
  is_draft=0
  for draft_dir in "${draft_dirs[@]}"; do
    if [[ "$file" == "$draft_dir"* ]]; then
      is_draft=1
      break
    fi
  done
  
  # Also check if this individual file is marked as draft (allowing trailing whitespace)
  if [ $is_draft -eq 0 ] && grep -q "^draft: true[[:space:]]*$" "$file" 2>/dev/null; then
    is_draft=1
  fi
  
  if [ $is_draft -eq 0 ]; then
    echo "  - '$file'" >> "$output_config"
    ((lp_count++))
  fi
done < <(find content/learning-paths -name "*.md" -type f | sort)
echo "Found $lp_count non-draft learning path file(s)"

if [ ! -f "$output_config" ]; then
  echo "Error: Failed to create $output_config" >&2
  exit 1
fi

file_count=$(grep -c "- '" "$output_config" 2>/dev/null || echo 0)
echo ""
echo "Generated spell check configuration: $output_config"
echo "  Install guides: $install_count"
echo "  Learning paths (non-draft): $lp_count"
echo "  Total sources: $file_count files"
echo "  File size: $(wc -c < "$output_config") bytes"
