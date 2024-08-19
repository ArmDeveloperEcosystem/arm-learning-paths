ALL_CHANGED_FILES=$@

echo "All changed files: ${ALL_CHANGED_FILES}"

# Skip non .md files
CHANGED_CONTENT=()
for file in ${ALL_CHANGED_FILES[*]}; do
   if echo "$file" | grep -q ".md"; then
      CHANGED_CONTENT+=("$file")
   else
      echo "Not an .md file, skipping"
   fi
done
echo "Changed content: ${CHANGED_CONTENT[*]}"

# Keep full paths for install guides,
# get parent directory for learning paths
CONTENT_PATHS=()
for file in ${CHANGED_CONTENT[*]}; do
   parentdir="$(dirname "$file")"
   if echo "$parentdir" | grep -q "install-guides"; then
      CONTENT_PATHS+=("$file")
   else
      CONTENT_PATHS+=("$parentdir")
   fi
done

# Make sure each learning path is only tested once
echo "Content paths: ${CONTENT_PATHS[*]}"
CONTENT_PATHS_UNIQUE=($(printf "%s\n" "${CONTENT_PATHS[@]}" | sort -u))
echo "Unique content paths: ${CONTENT_PATHS_UNIQUE[*]}"

# Install dependencies
pip install -r tools/requirements.txt

# Run the tests
for file in ${CONTENT_PATHS_UNIQUE[*]}; do
   tools/maintenance.py -i ${file}
done
