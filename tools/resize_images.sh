#!/bin/bash

set -e

#
# Tunables: Defaults
#
export dry_run=true   # if true, do not perform any file modifications
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
        echo "Usage: $0 <image1> <image2> ..."
        exit 1
    fi
}

#
# Function: process_env_tunables
# Purpose: pull/configure tunables from environment
#
process_env_tunables() {
    # Dry Run
    if [ -z "${DRY_RUN}" ]; then
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
# Function: process_images
# Purpose: process all images passed as arguments
#
process_images() {
    # loop through all image arguments
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
        echo "Checking $img..."
        width=$(identify -format "%w" "$img" 2>/dev/null || echo 0)

        # Get file size in KB (macOS stat is different)
        filesize=$(stat -f%z "$img" 2>/dev/null || echo 0)
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
                if [ "$kbsize" -ge 1500 ]; then           # ≥ 150KB
                    quality=80
                elif [ "$kbsize" -ge 500 ]; then          # 500–1500KB
                    quality=75
                else                                            # < 500KB
                    quality=95
                fi
                echo "Optimizing $img (${kbsize}KB, ${width}px), quality=$quality"
                # Resize and convert to WebP. If error occurs, capture it and exit.
                error=$(magick "$img" -resize 1280x\> -quality $quality -define webp:lossless=true "$webp_img" 2>&1)
                convert_status=$?
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

                img_name=$(basename "$img")             # create_device.png
                webp_name=$(basename "$webp_img")       # create_device.webp
                img_dir=$(dirname "$img")               # The directory of the image

                # Only scan markdown files in the same directory
                find "$img_dir" "$(dirname "$img_dir")" -name "*.md" 2>/dev/null | while read -r md_file; do
                    if grep -q "$img_name" "$md_file"; then
                        echo "Replacing $img_name → $webp_name in $md_file"
                        sed -i '' "s|($img_name|(${webp_name}|g" "$md_file"
                        sed -i '' "s|/$img_name|/${webp_name}|g" "$md_file"
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
}

#
# main() function
# Purpose: entry point for the script
#
main() {
    # confirm arguments
    confirm_args $*

    # pull/configure tunables from environment
    process_env_tunables $*

    # process all images passed as arguments
    process_images $*

    # we are done!
    echo "🎉 Optimization complete."
}

# Invoke main() with all script arguments
main $*
