#!/bin/bash
set -e

# Check if arguments provided
if [ $# -eq 0 ]; then
    echo "No images provided as arguments"
    echo "Usage: $0 <image1> <image2> ..."
    exit 1
fi

echo "🔍 Processing $# image(s)..."
dry_run=false

# Process each image argument
for img in "$@"; do
    # Skip if file doesn't exist
    [ -f "$img" ] || {
        echo "⚠️ File not found: $img"
        continue
    }

    # Skip if not an image file
    if [[ ! "$img" =~ \.(png|jpg|jpeg)$ ]]; then
        if [[ "$img" == *.webp ]]; then
            echo "Skipping $img (already .webp)"
            continue
        fi
        echo "Skipping non-image file: $img"
        continue
    fi

    # Get width using ImageMagick
    width=$(identify -format "%w" "$img" 2>/dev/null || echo 0)

    # Get file size in KB (macOS stat is different)
    filesize=$(stat -c%s "$img" 2>/dev/null || echo 0)
    kbsize=$((filesize / 1024))

    # Define new filename
    base="${img%.*}"
    ext="${img##*.}"
    webp_img="${base}.webp"

    # Resize + convert if needed
    if [ "$kbsize" -gt 200 ] && [ "$width" -gt 1600 ]; then
        if [ "$dry_run" = "true" ]; then
            echo "DRY RUN: Would resize $img → $webp_img"
            echo "DRY RUN: Would remove $img"
            echo "DRY RUN: Would update markdown references"
        else
            echo "Optimizing $img (${kbsize}KB, ${width}px)"
            
                convert "$img" -resize 1280x\> -quality 85 "$webp_img"
                rm "$img"

            img_name=$(basename "$img")             # create_device.png
            webp_name=$(basename "$webp_img")       # create_device.webp
            img_dir=$(dirname "$img")               # ./avh_balena

            # Only scan markdown files in the same directory
            find "$img_dir" "$(dirname "$img_dir")" -name "*.md" 2>/dev/null | while read -r md_file; do
                if grep -q "$img_name" "$md_file"; then
                    echo "Replacing $img_name → $webp_name in $md_file"
                    sed -i '' "s|$img_name|$webp_name|g" "$md_file"
                fi
            done
        fi

    else
        if [ "$dry_run" = "true" ]; then
            echo "DRY RUN: Would skip $img (size: ${kbsize}KB, width: ${width}px)"
        else
            echo "Skipping $img since it's small enough: (${kbsize}KB, ${width}px)"
        fi
    fi
done

echo "🎉 Optimization complete."