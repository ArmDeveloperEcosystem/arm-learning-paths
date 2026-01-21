# Run by test-lp.yml GitHub Action
ALL_CHANGED_FILES=$@

# Install dependencies and run tests,
# if we found tests to run
echo "All changed content paths:       ${ALL_CHANGED_FILES}"
# Keep full paths for install guides,
# get parent directory for learning paths
CONTENT_PATHS=()
for file in ${ALL_CHANGED_FILES[*]}; do
   parentdir="$(dirname "$file")"
   if echo "$parentdir" | grep -q "install-guides"; then
      CONTENT_PATHS+=("$file")
   else
      CONTENT_PATHS+=("$parentdir")
   fi
done
# Make sure each learning path is only tested once
CONTENT_PATHS_UNIQUE=($(printf "%s\n" "${CONTENT_PATHS[@]}" | sort -u))
echo "Unique content paths:         ${CONTENT_PATHS_UNIQUE[*]}"
# Run the tests
for file in ${CONTENT_PATHS_UNIQUE[*]}; do
   tools/maintenance.py -i ${file}
done
