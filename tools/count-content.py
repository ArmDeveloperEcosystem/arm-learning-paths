#!/usr/bin/env python3
"""
Script to count learning paths in each category and install guides.
Excludes learning paths marked as draft: true.
Accounts for cross-platform learning paths shared between multiple categories.
Writes results to a markdown file.
"""

import os
import sys
import re
import yaml
import argparse
from collections import defaultdict
from datetime import datetime

def extract_front_matter(file_path):
    """Extract YAML front matter from a markdown file."""
    try:
        with open(file_path, 'r') as f:
            content = f.read()
            # Look for front matter between --- markers
            match = re.search(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
            if match:
                front_matter_text = match.group(1)
                try:
                    # Parse the YAML front matter
                    return yaml.safe_load(front_matter_text)
                except Exception as e:
                    print(f"Error parsing YAML in {file_path}: {e}", file=sys.stderr)
            return {}
    except Exception as e:
        print(f"Error reading {file_path}: {e}", file=sys.stderr)
        return {}

def is_draft(index_file_path):
    """
    Check if a learning path is marked as draft.
    Only considers the _index.md file for determining if the entire Learning Path is a draft.
    """
    # Only check files named _index.md
    if not index_file_path.endswith('/_index.md'):
        return False
        
    front_matter = extract_front_matter(index_file_path)
    return front_matter.get('draft', False) is True

def get_shared_categories(index_file_path):
    """Get the categories this learning path is shared with."""
    front_matter = extract_front_matter(index_file_path)
    if front_matter.get('shared_path', False) and 'shared_between' in front_matter:
        return front_matter['shared_between']
    return []

def is_learning_path(directory):
    """Check if a directory is a learning path by looking for _index.md file."""
    index_file = os.path.join(directory, "_index.md")
    return os.path.isfile(index_file)

def count_learning_paths(base_dir, debug_category=None):
    """Count learning paths in each category, excluding drafts."""
    # Direct counts (learning paths directly in each category)
    direct_counts = defaultdict(int)
    # Shared counts (learning paths shared from cross-platform)
    shared_counts = defaultdict(int)
    # Draft counts
    drafts_by_category = defaultdict(int)
    # Store draft paths for debugging
    draft_paths = []
    
    # For detailed debugging
    debug_info = {
        'direct_paths': defaultdict(list),
        'shared_paths': defaultdict(list),
        'draft_paths': defaultdict(list),
        'all_dirs': defaultdict(list)
    }
    
    # Count learning paths by category
    learning_paths_dir = os.path.join(base_dir, "content", "learning-paths")
    if os.path.exists(learning_paths_dir):
        # First, process all categories except cross-platform
        for category in os.listdir(learning_paths_dir):
            category_path = os.path.join(learning_paths_dir, category)
            if os.path.isdir(category_path) and category != "cross-platform":
                # Count direct learning paths in this category
                for item in os.listdir(category_path):
                    item_path = os.path.join(category_path, item)
                    if os.path.isdir(item_path):
                        debug_info['all_dirs'][category].append(item)
                        
                        if is_learning_path(item_path):
                            index_file = os.path.join(item_path, "_index.md")
                            if is_draft(index_file):
                                drafts_by_category[category] += 1
                                draft_paths.append(f"{category}/{item}")
                                debug_info['draft_paths'][category].append(item)
                            else:
                                direct_counts[category] += 1
                                debug_info['direct_paths'][category].append(item)
                        else:
                            print(f"Warning: Directory {item_path} does not have an _index.md file")
        
        # Now process cross-platform learning paths
        cross_platform_path = os.path.join(learning_paths_dir, "cross-platform")
        if os.path.exists(cross_platform_path):
            for item in os.listdir(cross_platform_path):
                item_path = os.path.join(cross_platform_path, item)
                if os.path.isdir(item_path):
                    debug_info['all_dirs']["cross-platform"].append(item)
                    
                    if is_learning_path(item_path):
                        index_file = os.path.join(item_path, "_index.md")
                        
                        # Skip if it's a draft
                        if is_draft(index_file):
                            drafts_by_category["cross-platform"] += 1
                            draft_paths.append(f"cross-platform/{item}")
                            debug_info['draft_paths']["cross-platform"].append(item)
                            continue
                        
                        # Count it in cross-platform
                        direct_counts["cross-platform"] += 1
                        debug_info['direct_paths']["cross-platform"].append(item)
                        
                        # Check if it's shared with other categories
                        shared_categories = get_shared_categories(index_file)
                        for shared_category in shared_categories:
                            shared_counts[shared_category] += 1
                            debug_info['shared_paths'][shared_category].append(item)
                    else:
                        print(f"Warning: Directory {item_path} does not have an _index.md file")
    
    # Combine direct and shared counts
    total_counts = defaultdict(int)
    for category in set(list(direct_counts.keys()) + list(shared_counts.keys())):
        total_counts[category] = direct_counts[category] + shared_counts[category]
    
    # Print detailed debug info for the specified category
    if debug_category:
        print(f"\nDetailed information for category: {debug_category}")
        
        print(f"\nAll directories ({len(debug_info['all_dirs'].get(debug_category, []))}):")
        for path in sorted(debug_info['all_dirs'].get(debug_category, [])):
            print(f"  - {path}")
        
        print(f"\nDirect Learning Paths ({len(debug_info['direct_paths'].get(debug_category, []))}):")
        for path in sorted(debug_info['direct_paths'].get(debug_category, [])):
            print(f"  - {path}")
        
        print(f"\nShared Learning Paths from cross-platform ({len(debug_info['shared_paths'].get(debug_category, []))}):")
        for path in sorted(debug_info['shared_paths'].get(debug_category, [])):
            print(f"  - {path}")
        
        print(f"\nDraft Learning Paths ({len(debug_info['draft_paths'].get(debug_category, []))}):")
        for path in sorted(debug_info['draft_paths'].get(debug_category, [])):
            print(f"  - {path}")
            
        # Check if any draft paths have draft: true in their _index.md
        for path in sorted(debug_info['draft_paths'].get(debug_category, [])):
            full_path = os.path.join(learning_paths_dir, debug_category, path, "_index.md")
            if os.path.exists(full_path):
                with open(full_path, 'r') as f:
                    content = f.read()
                    print(f"\nChecking draft status for {path}:")
                    print(f"  Has 'draft: true': {'draft: true' in content}")
                    # Extract a snippet around the draft declaration
                    match = re.search(r'(.*draft:.*)', content)
                    if match:
                        print(f"  Draft line: {match.group(1).strip()}")
        
        # Find directories that are not counted as learning paths
        not_learning_paths = set(debug_info['all_dirs'].get(debug_category, [])) - \
                            set(debug_info['direct_paths'].get(debug_category, [])) - \
                            set(debug_info['draft_paths'].get(debug_category, []))
        
        if not_learning_paths:
            print(f"\nDirectories not counted as Learning Paths ({len(not_learning_paths)}):")
            for path in sorted(not_learning_paths):
                full_path = os.path.join(learning_paths_dir, debug_category, path)
                print(f"  - {path} (Has _index.md: {os.path.exists(os.path.join(full_path, '_index.md'))})")
    
    return total_counts, direct_counts, shared_counts, drafts_by_category, draft_paths, debug_info

def count_install_guides(base_dir):
    """
    Count install guides:
    - Each .md file directly in the install-guides directory (excluding _index.md) counts as 1 guide
    - Each subdirectory counts as 1 guide (regardless of how many .md files it contains)
    """
    install_guides_count = 0
    install_guides_dir = os.path.join(base_dir, "content", "install-guides")
    
    if not os.path.exists(install_guides_dir):
        return 0
    
    for item in os.listdir(install_guides_dir):
        item_path = os.path.join(install_guides_dir, item)
        
        # Count .md files directly in the install-guides directory
        if os.path.isfile(item_path) and item.endswith('.md') and item != '_index.md':
            install_guides_count += 1
        
        # Count each subdirectory as 1 guide (except _images)
        elif os.path.isdir(item_path) and item != '_images':
            install_guides_count += 1
    
    return install_guides_count

def write_markdown_report(total_counts, direct_counts, shared_counts, drafts_by_category, install_guides_count, output_file):
    """Write the results to a markdown file."""
    today = datetime.now().strftime("%B %d, %Y")
    
    # Calculate totals
    unique_learning_paths = sum(direct_counts.values())
    total_with_shared = sum(total_counts.values())
    total_drafts = sum(drafts_by_category.values())
    
    with open(output_file, 'w') as f:
        f.write(f"# Arm Learning Paths Content Summary\n\n")
        f.write(f"This document provides a summary of the content available in the Arm Learning Paths repository as of {today}.\n\n")
        
        # Learning Paths by Category table
        f.write("## Learning Paths by Category\n\n")
        f.write("The table below shows the breakdown of Learning Paths by category, including both direct and shared content:\n\n")
        f.write("| Category | Total | Published | Direct | Shared | Drafts |\n")
        f.write("|----------|-------|-----------|--------|--------|--------|\n")
        
        for category, count in sorted(total_counts.items()):
            # Special case for IoT to ensure correct capitalization
            if category == "iot":
                category_name = "IoT"
            else:
                category_name = category.replace('-', ' ').title()
            
            # Calculate published count (total minus drafts)
            published_count = count - drafts_by_category[category]
            
            f.write(f"| {category_name} | {count} | {published_count} | {direct_counts[category]} | {shared_counts[category]} | {drafts_by_category[category]} |\n")
        
        # Install Guides table
        f.write("\n## Install Guides\n\n")
        f.write("| Content Type | Count |\n")
        f.write("|--------------|-------|\n")
        f.write(f"| Install Guides | {install_guides_count} |\n")
        
        # Summary Totals table
        f.write("\n## Summary Totals\n\n")
        f.write("| Metric | Count |\n")
        f.write("|--------|-------|\n")
        f.write(f"| Total Learning Paths (unique) | {unique_learning_paths} |\n")
        f.write(f"| Total Learning Paths (including shared) | {total_with_shared} |\n")
        f.write(f"| Total Learning Paths (drafts) | {total_drafts} |\n")
        f.write(f"| Total Published Content (unique Learning Paths + Install Guides) | {unique_learning_paths + install_guides_count} |\n")
        
        # Notes section
        f.write("\n## Notes\n\n")
        f.write("- **Direct**: Learning Paths that are directly in the category's directory\n")
        f.write("- **Shared**: Learning Paths from the cross-platform directory that are shared with this category\n")
        f.write("- **Drafts**: Learning Paths marked with `draft: true` that are not published\n")
        f.write("- The \"Total Learning Paths (unique)\" counts each Learning Path once, regardless of how many categories it appears in\n")
        f.write("- The \"Total Learning Paths (including shared)\" counts Learning Paths in each category they appear in\n")

def main():
    import argparse
    
    # Set up command line arguments
    parser = argparse.ArgumentParser(description='Count learning paths and install guides in the repository.')
    parser.add_argument('--debug', dest='debug_category', 
                        help='Enable debug output for a specific category')
    args = parser.parse_args()
    
    base_dir = os.getcwd()  # Assuming script is run from the project root
    output_file = os.path.join(base_dir, "content_summary.md")
    
    # Use debug_category from command line arguments if provided
    debug_category = args.debug_category
    
    total_counts, direct_counts, shared_counts, drafts_by_category, draft_paths, debug_info = count_learning_paths(base_dir, debug_category)
    install_guides_count = count_install_guides(base_dir)
    
    # Write results to markdown file
    write_markdown_report(total_counts, direct_counts, shared_counts, drafts_by_category, 
                         install_guides_count, output_file)
    
    print(f"\nContent summary written to {output_file}")
    
    # Also print a brief summary to the console
    unique_learning_paths = sum(direct_counts.values())
    total_with_shared = sum(total_counts.values())
    total_drafts = sum(drafts_by_category.values())
    
    print("\nBrief Summary:")
    print(f"- Learning Paths (unique): {unique_learning_paths}")
    print(f"- Learning Paths (with shared): {total_with_shared}")
    print(f"- Install Guides: {install_guides_count}")
    print(f"- Total Published Content: {unique_learning_paths + install_guides_count}")
    print(f"- Draft Learning Paths: {total_drafts}")
    
    # Print draft paths for debugging
    if draft_paths:
        print("\nDraft Learning Paths:")
        for path in sorted(draft_paths):
            print(f"- {path}")

if __name__ == "__main__":
    main()
