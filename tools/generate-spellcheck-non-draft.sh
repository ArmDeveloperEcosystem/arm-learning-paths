#!/bin/bash
# Generate a spell check configuration that only includes non-draft files
# This script finds all markdown files EXCEPT those in draft Learning Paths

cd "$(dirname "$(dirname "${BASH_SOURCE[0]}")")" || exit 1

output_config=".spellcheck-non-draft.yml"

# Arrays to collect draft files
draft_lp_dirs=()
draft_install_guides=()
draft_lp_files=()

# Find draft Learning Path directories (those with cascade directive)
echo "Finding draft Learning Paths with cascade directive..."
draft_file_list=$(find content/learning-paths -type f -name "_index.md" -exec grep -l "^draft: true" {} \; 2>/dev/null)
while IFS= read -r file; do
  [ -z "$file" ] && continue
  # Only mark entire directory as draft if it has cascade directive
  if grep -q "^cascade:" "$file" 2>/dev/null; then
    dir=$(dirname "$file")
    draft_lp_dirs+=("$dir")
    echo "  - $dir/"
  fi
done <<< "$draft_file_list"
echo "Found ${#draft_lp_dirs[@]} draft Learning Path director(ies) with cascade"
echo ""

# Find draft install guides
echo "Finding draft install guides..."
while IFS= read -r file; do
  [ -z "$file" ] && continue
  if grep -q "^draft: true[[:space:]]*$" "$file" 2>/dev/null; then
    draft_install_guides+=("$file")
    echo "  - $file"
  fi
done < <(find content/install-guides -name "*.md" -type f | sort)
echo "Found ${#draft_install_guides[@]} draft install guide(s)"
echo ""

# Find individual draft Learning Path files (not in cascade directories)
echo "Finding individual draft Learning Path files..."
while IFS= read -r file; do
  [ -z "$file" ] && continue
  
  # Check if this file is in a cascade-draft directory
  in_draft_dir=0
  for draft_dir in "${draft_lp_dirs[@]}"; do
    if [[ "$file" == "$draft_dir"* ]]; then
      in_draft_dir=1
      break
    fi
  done
  
  # If not in draft directory, check if individually marked as draft
  if [ $in_draft_dir -eq 0 ] && grep -q "^draft: true[[:space:]]*$" "$file" 2>/dev/null; then
    draft_lp_files+=("$file")
    echo "  - $file"
  fi
done < <(find content/learning-paths -name "*.md" -type f | sort)
echo "Found ${#draft_lp_files[@]} individual draft Learning Path file(s)"
echo ""

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
  [ -z "$file" ] && continue
  # Check if this install guide is marked as draft (allowing trailing whitespace)
  if ! grep -q "^draft: true[[:space:]]*$" "$file" 2>/dev/null; then
    echo "  - '$file'" >> "$output_config"
    ((install_count++))
  fi
done < <(find content/install-guides -name "*.md" -type f | sort)
echo "Found $install_count non-draft install guide(s)"

# Collect and add non-draft learning path files
lp_count=0
while IFS= read -r file; do
  [ -z "$file" ] && continue
  # Check if this file is in a cascade-draft directory
  is_draft=0
  for draft_dir in "${draft_lp_dirs[@]}"; do
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
echo "Found $lp_count non-draft Learning Path source file(s)"

if [ ! -f "$output_config" ]; then
  echo "Error: Failed to create $output_config" >&2
  exit 1
fi

echo ""
echo "Generated spell check configuration: $output_config"
echo "  Install guides: $install_count"
echo "  Learning Path source files: $lp_count"
