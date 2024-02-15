#!/bin/bash

# Define the file names
infile="outdated_files.csv"
outfile="oldest-quarter.csv"

if [ ! -f "$infile" ]; then
    echo "Missing input file: $infile"
    echo "Run 'python3 tools/maintenance.py -r 1' first to generate $infile"
    exit 1
fi

# Get the total number of lines in the file
total_lines=$(wc -l < $infile)

# Calculate the number of lines to be selected
lines_to_select=$((total_lines / 4))

# Sort the file by date and select the oldest lines
oldest_lines=$(sort -t, -k2 -n -r $infile| head -n $lines_to_select)

# Print the oldest lines
echo "$oldest_lines" > $outfile

old_count=$(wc -l < $outfile)

echo "There are $old_count items to review in $outfile"

