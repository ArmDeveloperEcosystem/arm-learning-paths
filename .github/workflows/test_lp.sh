ALL_CHANGED_FILES=$1

# Skip non .md files
CHANGED_CONTENT=()
for file in ${ALL_CHANGED_FILES}; do
   echo "$file"
   if [[ $file == *.md ]]; then
      CHANGED_CONTENT+="$file"
   else
      echo "Not an .md file, skipping"
   fi
done

# Keep full paths for install guides,
# get parent directory for learning paths
CONTENT_PATHS=()
for file in ${CHANGED_CONTENT[@]}; do
   parentdir="$(dirname "$file")"
   if [[ $parentdir = */install-guides/* ]]; then
      CONTENT_PATHS+="$file"
   else
      CONTENT_PATHS+="$parentdir"
   fi
done

# Make sure each learning path is only tested once
CONTENT_PATHS_UNIQUE=($(echo "$CONTENT_PATHS" | sort -u))

# Install dependencies
pip install -r tools/requirements.txt

# Run the tests
for file in ${CONTENT_PATHS_UNIQUE}; do
   tools/maintenance.py -i ${file}
done
