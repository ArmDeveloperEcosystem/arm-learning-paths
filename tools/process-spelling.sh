#!/bin/bash

# Extract just the misspelled words from the output of the spellcheck tool

# Set the input file path
input_file="spellcheck-output.txt"

# Sort and remove duplicates, saving the result to a temporary file
tmp_file=$(mktemp)
grep -v '^>' "$input_file" | grep -v '^\s*$' | awk 'NF==1' | grep '^[a-zA-Z0-9]' | sort -u > "$tmp_file"

# Move the temporary file content back to the original file (overwrite)
mv "$tmp_file" "$input_file"

echo "New spelling issues to check are now available in '$input_file'"

echo -e "\nWords to check:"
cat $input_file
