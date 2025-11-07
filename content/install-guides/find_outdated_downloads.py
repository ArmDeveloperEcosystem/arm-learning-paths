#!/usr/bin/env python3
"""
Script to find download commands in markdown files that may contain outdated software versions.
Searches for wget, curl, and other download patterns with version numbers.
"""

import os
import re
import glob
from pathlib import Path

def extract_download_commands(file_path):
    """Extract download commands from a markdown file."""
    download_commands = []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return download_commands
    
    # Patterns to match download commands with potential version numbers
    patterns = [
        # wget commands with URLs containing version numbers
        r'wget\s+[^\s]*(?:https?://[^\s]*(?:\d+\.\d+[^\s]*|v\d+[^\s]*|release[^\s]*|download[^\s]*)[^\s]*)',
        # curl commands with URLs containing version numbers  
        r'curl\s+[^\n]*(?:https?://[^\s]*(?:\d+\.\d+[^\s]*|v\d+[^\s]*|release[^\s]*|download[^\s]*)[^\s]*)',
        # Direct download URLs in markdown links or code blocks
        r'https?://[^\s\)]*(?:download[^\s\)]*|release[^\s\)]*|archive[^\s\)]*|releases[^\s\)]*)[^\s\)]*(?:\d+\.\d+[^\s\)]*|v\d+[^\s\)]*)',
        # Package manager installs with specific versions
        r'(?:apt|yum|dnf|brew|pip|npm|cargo)\s+install[^\n]*(?:\d+\.\d+|\=\d+)',
        # GitHub releases pattern
        r'https?://github\.com/[^/]+/[^/]+/releases/download/[^\s\)]*',
        # Archive downloads with version numbers
        r'(?:wget|curl)[^\n]*\.(?:tar\.gz|tar\.bz2|zip|tgz)[^\n]*(?:\d+\.\d+|v\d+)',
        # Docker image pulls with specific tags
        r'docker\s+pull[^\n]*:\d+\.\d+',
        # Maven/Gradle dependencies with versions
        r'(?:implementation|compile|dependency)[^\n]*:\d+\.\d+',
    ]
    
    # Find all code blocks (both ``` and indented)
    code_blocks = []
    
    # Find fenced code blocks
    fenced_pattern = r'```[^\n]*\n(.*?)\n```'
    for match in re.finditer(fenced_pattern, content, re.DOTALL):
        code_blocks.append(match.group(1))
    
    # Find indented code blocks (4+ spaces or tabs)
    lines = content.split('\n')
    current_block = []
    for line in lines:
        if re.match(r'^(?:    |\t)', line):  # 4 spaces or tab
            current_block.append(line.strip())
        else:
            if current_block:
                code_blocks.append('\n'.join(current_block))
                current_block = []
    if current_block:
        code_blocks.append('\n'.join(current_block))
    
    # Search in code blocks and full content
    search_content = content + '\n' + '\n'.join(code_blocks)
    
    for pattern in patterns:
        matches = re.finditer(pattern, search_content, re.IGNORECASE | re.MULTILINE)
        for match in matches:
            command = match.group(0).strip()
            # Clean up the command (remove extra whitespace, limit length)
            command = ' '.join(command.split())
            if len(command) > 200:
                command = command[:200] + '...'
            
            # Skip if it's just a generic example or placeholder
            if not re.search(r'(?:example|placeholder|your-|<[^>]+>)', command, re.IGNORECASE):
                download_commands.append(command)
    
    # Remove duplicates while preserving order
    seen = set()
    unique_commands = []
    for cmd in download_commands:
        if cmd not in seen:
            seen.add(cmd)
            unique_commands.append(cmd)
    
    return unique_commands

def scan_directory(directory_path):
    """Scan directory for markdown files and extract download commands."""
    results = {}
    
    # Find all .md files recursively
    md_files = glob.glob(os.path.join(directory_path, '**/*.md'), recursive=True)
    
    for md_file in md_files:
        # Skip _index.md and other index files as they typically don't contain install commands
        if os.path.basename(md_file).startswith('_'):
            continue
            
        download_commands = extract_download_commands(md_file)
        if download_commands:
            # Store relative path for cleaner output
            rel_path = os.path.relpath(md_file, directory_path)
            results[rel_path] = download_commands
    
    return results

def write_results(results, output_file):
    """Write results to output file."""
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# Software Download Commands That May Need Version Updates\n\n")
        f.write("This file contains download commands found in markdown files that may contain outdated software versions.\n")
        f.write("Review each command to check if newer versions are available.\n\n")
        f.write(f"Total files with download commands: {len(results)}\n\n")
        
        for file_path, commands in sorted(results.items()):
            f.write(f"## {file_path}\n\n")
            for i, command in enumerate(commands, 1):
                f.write(f"{i}. ```\n{command}\n```\n\n")
            f.write("---\n\n")

def main():
    """Main function."""
    current_dir = os.getcwd()
    output_file = os.path.join(current_dir, 'outdated_software_downloads.md')
    
    print(f"Scanning directory: {current_dir}")
    print("Looking for download commands in .md files...")
    
    results = scan_directory(current_dir)
    
    if results:
        write_results(results, output_file)
        print(f"\nFound download commands in {len(results)} files.")
        print(f"Results written to: {output_file}")
        
        # Print summary
        total_commands = sum(len(commands) for commands in results.values())
        print(f"Total download commands found: {total_commands}")
        
        print("\nFiles with most download commands:")
        sorted_files = sorted(results.items(), key=lambda x: len(x[1]), reverse=True)
        for file_path, commands in sorted_files[:5]:
            print(f"  {file_path}: {len(commands)} commands")
    else:
        print("No download commands found in any markdown files.")

if __name__ == "__main__":
    main()
