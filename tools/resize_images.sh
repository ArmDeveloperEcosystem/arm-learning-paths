#!/bin/bash

set -e

#
# Tunables: Defaults
#
export dry_run=false   # if true, do not perform any file modifications
export quality=85     # quality for webp conversion (1-100)
export max_width=1600 # maximum width before resizing
export target_width=1280 # target width for resizing      
export max_size_kb=200 # maximum file size in KB before resizing

#
# Function: confirm_args
# Purpose: confirm that at least one image argument is provided
#
confirm_args() {
    if [ $# -eq 0 ]; then
        echo "No images provided as arguments"
        echo "Usage: $0 <image-or-directory> ..."
        exit 1
    fi
}

#
# Function: process_env_tunables
# Purpose: pull/configure tunables from environment
#
process_env_tunables() {
    # Dry Run
    if [ -n "${DRY_RUN}" ]; then
        export dry_run=${DRY_RUN}
    fi

    # Quality
    if [ -n "${QUALITY}" ]; then
        export quality=${QUALITY}
    fi
    # Max Width
    if [ -n "${MAX_WIDTH}" ]; then
        export max_width=${MAX_WIDTH}
    fi
    # Target Width
    if [ -n "${TARGET_WIDTH}" ]; then
        export target_width=${TARGET_WIDTH}
    fi
    # Max Size KB
    if [ -n "${MAX_SIZE_KB}" ]; then
        export max_size_kb=${MAX_SIZE_KB}
    fi    
}

#
# Function: find_markdown_root
# Purpose: find the nearest content root containing an _index.md file
#
find_markdown_root() {
    local search_dir="$1"

    while [ "$search_dir" != "/" ]; do
        if [ -f "$search_dir/_index.md" ]; then
            echo "$search_dir"
            return
        fi
        search_dir=$(dirname "$search_dir")
    done

    # Preserve the previous behavior for images outside a content directory.
    dirname "$1"
}

#
# Function: process_image
# Purpose: process one image
#
process_image() {
        local img="$1"

        # Skip if not an image file
        if [[ ! "$img" =~ \.(png|PNG|jpg|JPG|jpeg|JPEG)$ ]]; then
            if [[ "$img" == *.webp ]]; then
                echo "Skipping $img (already .webp)"
                return
            fi
            echo "Skipping non-image file: $img"
            return
        fi

        # Get width using ImageMagick
        echo "Checking $img..."
        width=$(identify -format "%w" "$img" 2>/dev/null || echo 0)

        # Get file size in KB (handle both macOS and Linux)
        if [[ "$OSTYPE" == "darwin"* ]]; then
            filesize=$(stat -f%z "$img" 2>/dev/null || echo 0)
        else
            filesize=$(stat -c%s "$img" 2>/dev/null || echo 0)
        fi
        kbsize=$((filesize / 1024))

        # Define new filename
        base="${img%.*}"
        ext="${img##*.}"
        webp_img="${base}.webp"

        # image stats
        echo "Image: $img | Size: ${kbsize}KB | Width: ${width}px"

        # Resize + convert if needed
        if [ "$kbsize" -gt ${max_size_kb} ] && [ "$width" -gt ${max_width} ]; then
            if [ "$dry_run" = "true" ]; then
                echo "DRY RUN: Would resize $img → $webp_img"
                echo "DRY RUN: Would remove $img"
                echo "DRY RUN: Would update markdown references"
            else
                # Set quality dynamically based on file size
                if [ "$kbsize" -ge 1500 ]; then           # ≥ 1500KB
                    quality=80
                elif [ "$kbsize" -ge 500 ]; then          # 500–1500KB
                    quality=75
                else                                            # < 500KB
                    quality=95
                fi
                echo "Optimizing $img (${kbsize}KB, ${width}px), quality=$quality"
                # Resize and convert to WebP. If error occurs, capture it and exit.
                # Try 'magick' first (newer ImageMagick), fall back to 'convert' (older/traditional)
                if command -v magick &> /dev/null; then
                    error=$(magick "$img" -resize ${target_width}x\> -quality $quality -define webp:lossless=true "$webp_img" 2>&1)
                    convert_status=$?
                elif command -v convert &> /dev/null; then
                    error=$(convert "$img" -resize ${target_width}x\> -quality $quality -define webp:lossless=true "$webp_img" 2>&1)
                    convert_status=$?
                else
                    echo "⚠️ Neither 'magick' nor 'convert' command found. Please install ImageMagick."
                    exit 1
                fi
                if [ $convert_status -ne 0 ]; then
                    echo "⚠️ Error converting $img to WebP format."
                    if [ -z "${error}" ]; then
                        error="Unknown error"
                    fi
                    echo "Error details: $error"
                    echo "⚠️ Exiting script."
                    exit 1
                else
                    echo "Created $webp_img.... removing $img..."
                    rm "$img"
                fi

                img_dir=$(dirname "$img")               # The directory of the image
                markdown_root=$(find_markdown_root "$img_dir")
                relative_img="${img#"$markdown_root"/}"
                relative_webp="${webp_img#"$markdown_root"/}"

                # Escape paths before using them in a sed expression. Matching the
                # relative path avoids changing a same-named image in another
                # nested directory.
                sed_img=$(printf '%s\n' "$relative_img" | sed 's/[][\\.^$*|]/\\&/g')
                sed_webp=$(printf '%s\n' "$relative_webp" | sed 's/[\\&|]/\\&/g')

                # Scan the Learning Path or Install Guide containing the image. This
                # reaches Markdown files above nested directories such as
                # images/streamline/ without touching unrelated content.
                find "$markdown_root" -type f -name "*.md" -print0 2>/dev/null | while IFS= read -r -d '' md_file; do
                    if grep -Fq "$relative_img" "$md_file"; then
                        echo "Replacing $relative_img → $relative_webp in $md_file"
                        # Handle sed differences between macOS and Linux
                        if [[ "$OSTYPE" == "darwin"* ]]; then
                            sed -i '' "s|$sed_img|$sed_webp|g" "$md_file"
                        else
                            sed -i "s|$sed_img|$sed_webp|g" "$md_file"
                        fi
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
}

#
# Function: process_images
# Purpose: process image files and recursively process image directories
#
process_images() {
    local input

    for input in "$@"; do
        if [ -d "$input" ]; then
            while IFS= read -r -d '' img; do
                process_image "$img"
            done < <(find "$input" -type f \( \
                -iname "*.png" -o \
                -iname "*.jpg" -o \
                -iname "*.jpeg" -o \
                -iname "*.webp" \
            \) -print0)
        elif [ -f "$input" ]; then
            process_image "$input"
        else
            echo "⚠️ File or directory not found: $input"
        fi
    done
}

#
# main() function
# Purpose: entry point for the script
#
main() {
    # confirm arguments
    confirm_args "$@"

    # pull/configure tunables from environment
    process_env_tunables "$@"

    # process all images passed as arguments
    process_images "$@"

    # we are done!
    echo "🎉 Optimization complete."
}

# Invoke main() with all script arguments
main "$@"
