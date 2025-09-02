#!/usr/bin/env python3
"""
Enhanced style checker for Arm Learning Paths content.
This script checks markdown files against writing style guidelines from a JSON file
and uses spaCy for passive voice detection.
"""

import argparse
import json
import os
import re
import sys
import re

# Import spaCy if available
try:
    import spacy
    SPACY_AVAILABLE = True
    # Try to load the English model
    try:
        nlp = spacy.load("en_core_web_sm")
    except:
        print("Warning: spaCy model 'en_core_web_sm' not found. Attempting to download it.")
        try:
            from spacy.cli import download
            download("en_core_web_sm")
            nlp = spacy.load("en_core_web_sm")
            print("Successfully downloaded and loaded spaCy model.")
        except Exception as e:
            print(f"Error: Could not download spaCy model. Passive voice detection will be limited. Details: {e}")
            raise SystemExit("Exiting due to missing spaCy model.")
        try:
            from spacy.cli import download
            download("en_core_web_sm")
            nlp = spacy.load("en_core_web_sm")
            print("Successfully downloaded and loaded spaCy model.")
        except:
            print("Error: Could not download spaCy model. Passive voice detection will be limited.")
            SPACY_AVAILABLE = False
except ImportError:
    print("Warning: spaCy not installed. Using basic passive voice detection.")
    SPACY_AVAILABLE = False

def load_style_rules(rules_file):
    """Load style rules from a JSON file."""
    try:
        with open(rules_file, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading style rules: {e}")
        return []

def is_in_code_block(lines, line_index):
    """Check if the line is within a code block."""
    code_block_count = 0
    for i in range(line_index):
        if re.match(r'^```', lines[i]):
            code_block_count += 1

    return code_block_count % 2 == 1  # Odd count means inside a code block

def is_in_yaml_frontmatter(lines, line_index):
    """Check if the line is within YAML frontmatter."""
    if line_index == 0 and lines[0].strip() == '---':
        return True

    frontmatter_markers = 0
    for i in range(line_index):
        if lines[i].strip() == '---':
            frontmatter_markers += 1

    # If we've seen an odd number of markers, we're in frontmatter
    return frontmatter_markers % 2 == 1

def should_capitalize_replacement(original, start_index, replacement):
    """Determine if the replacement should be capitalized based on its position."""
    should_capitalize = False
    if start_index == 0 or (start_index >= 2 and original[start_index-2:start_index] == '. '):
        if replacement and replacement[0].islower():
            return replacement[0].upper() + replacement[1:]
        should_capitalize = True
    return replacement, should_capitalize

def detect_passive_voice_with_spacy(text):
    """
    Detect passive voice using spaCy's dependency parsing.
    Returns a list of (passive_text, suggested_active) tuples.

    Note: If spaCy is not available (`SPACY_AVAILABLE` is False), this function will return an empty list.
    """
    if not SPACY_AVAILABLE:
        return []

    doc = nlp(text)
    passive_constructions = []

    for token in doc:
        # Look for passive auxiliary verbs
        if token.dep_ == "auxpass":
            # Find the main verb
            verb = token.head

            # Find the subject (usually nsubjpass)
            subject = None
            for child in verb.children:
                if child.dep_ == "nsubjpass":
                    subject = child
                    break

            # Find the agent (usually introduced by "by")
            agent = None
            for child in verb.children:
                if child.dep_ == "agent":
                    for agent_child in child.children:
                        if agent_child.dep_ == "pobj":
                            agent = agent_child
                            break
                    break

            # If we have both subject and agent, we can suggest an active voice alternative
            if subject and agent:
                # Extract the spans of text
                passive_span = doc[max(0, subject.i - 1):min(len(doc), verb.i + 2)]
                if agent.i > verb.i:
                    passive_span = doc[max(0, subject.i - 1):min(len(doc), agent.i + 1)]

                # Create active voice suggestion
                # Capitalize if at start of sentence
                active_suggestion, should_capitalize = should_capitalize_replacement(text, passive_span.start_char, active_suggestion)
                if should_capitalize:
                    active_suggestion = active_suggestion[0].upper() + active_suggestion[1:]

                passive_constructions.append((passive_span.text, active_suggestion))

    return passive_constructions

def fix_passive_voice(line):
    """
    Fix passive voice constructions by swapping subject and object.
    This is a more sophisticated approach than simple pattern replacement.
    """
    # Common passive voice patterns with specific replacements
    passive_patterns = [
        (r'The data is processed by the system', r'The system processes the data'),
        (r'The code is handled by the compiler', r'The compiler handles the code'),
        (r'The configuration was managed by the user', r'The user managed the configuration'),
        (r'The documentation was created by the team', r'The team created the documentation'),
        (r'The results are generated by the algorithm', r'The algorithm generates the results'),
        (r'The API is provided by the service', r'The service provides the API')
    ]

    # Try each specific pattern first
    for pattern, replacement in passive_patterns:
        if re.search(pattern, line, re.IGNORECASE):
            return re.sub(pattern, replacement, line, flags=re.IGNORECASE)

    # Generic patterns as fallback
    generic_patterns = [
        # Present tense passive
        (r'(\w+) is (\w+ed) by (\w+)', r'\3 \2s \1'),
        (r'(\w+) are (\w+ed) by (\w+)', r'\3 \2 \1'),
        # Past tense passive
        (r'(\w+) was (\w+ed) by (\w+)', r'\3 \2 \1'),
        (r'(\w+) were (\w+ed) by (\w+)', r'\3 \2 \1')
    ]

    for pattern, replacement in generic_patterns:
        if re.search(pattern, line):
            return re.sub(pattern, replacement, line)

    return line

def check_style(content, file_path, style_rules):
    """Check content against style rules and return suggestions."""
    suggestions = []
    lines = content.split("\n")

    # First, check for passive voice using spaCy if available
    if SPACY_AVAILABLE:
        # Process each paragraph separately to maintain context
        paragraphs = []
        current_paragraph = []

        for i, line in enumerate(lines):
            # Skip code blocks, YAML frontmatter, headings, and links
            if (is_in_code_block(lines, i) or
                is_in_yaml_frontmatter(lines, i) or
                re.match(r'^#+\s', line) or
                re.search(r'^\s*\[.*\]:\s*', line)):
                # End the current paragraph if any
                if current_paragraph:
                    paragraphs.append((current_paragraph[0], " ".join(current_paragraph[1])))
                    current_paragraph = []
                continue

            # Skip empty lines - they end paragraphs
            if not line.strip():
                if current_paragraph:
                    paragraphs.append((current_paragraph[0], " ".join(current_paragraph[1])))
                    current_paragraph = []
                continue

            # Add line to current paragraph
            if not current_paragraph:
                current_paragraph = [i, [line]]
            else:
                current_paragraph[1].append(line)

        # Add the last paragraph if any
        if current_paragraph:
            paragraphs.append((current_paragraph[0], " ".join(current_paragraph[1])))

        # Check each paragraph for passive voice
        for start_line, paragraph_text in paragraphs:
            passive_constructions = detect_passive_voice_with_spacy(paragraph_text)

            for passive_text, active_suggestion in passive_constructions:
                # Find which line contains this passive construction
                for j, line in enumerate(lines[start_line:start_line + 10]):  # Look at next 10 lines max
                    if passive_text in line:
                        line_index = start_line + j
                        suggestions.append({
                            "file": file_path,
                            "line": line_index + 1,  # 1-based line numbers
                            "original": line,
                            "suggested": line.replace(passive_text, active_suggestion),
                            "reason": "Convert passive voice to active voice for clarity and directness (detected by spaCy)."
                        })
                        break

    # Then check each line against style rules
    for i, line in enumerate(lines):
        # Skip code blocks and YAML frontmatter
        if is_in_code_block(lines, i) or is_in_yaml_frontmatter(lines, i):
            continue

        # Skip headings (lines starting with #)
        if re.match(r'^#+\s', line):
            continue

        # Skip links and image references
        if re.search(r'^\s*\[.*\]:\s*', line):
            continue

        # If we already have a suggestion for this line, skip further checks
        if any(sugg["line"] == i + 1 for sugg in suggestions):
            continue

        # Check against other style rules
        for rule in style_rules:
            matches = list(re.finditer(rule["pattern"], line, re.IGNORECASE))
            for match in matches:
                # Create a suggestion
                original = line

                # Get the matched text
                # Determine if replacement should be capitalized
                replacement, should_capitalize = should_capitalize_replacement(line, match.start(), rule["replacement"])
                if replacement and should_capitalize:
                    replacement = replacement[0].upper() + replacement[1:]

                # Apply the replacement
                suggested = line[:match.start()] + replacement + line[match.end():]

                if original != suggested:
                    suggestions.append({
                        "file": file_path,
                        "line": i + 1,
                        "original": original,
                        "suggested": suggested,
                        "reason": rule["reason"],
                    })
                    # Only one suggestion per line to avoid conflicts
                    break

    return suggestions

def save_suggestions_to_file(suggestions, output_file="data/style_suggestions.json"):
    """Save suggestions to a JSON file."""
    with open(output_file, "w") as f:
        json.dump(suggestions, f, indent=2)
    print(f"Saved suggestions to {output_file}")

def print_suggestions(suggestions):
    """Print suggestions in a readable format."""
    if not suggestions:
        print("No style issues found.")
        return

    print(f"\nFound {len(suggestions)} style issues:")
    print("=" * 80)

    for i, sugg in enumerate(suggestions, 1):
        print(f"Issue {i}: File: {sugg['file']}, Line: {sugg['line']}, Reason: {sugg['reason']}")
        print(f"Original: {sugg['original']} -> Suggested: {sugg['suggested']}")
        print("-" * 80)


def load_suggestions(suggestions_path):
    with open(suggestions_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def load_file_lines(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.readlines()

def save_file_lines(file_path, lines):
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(lines)

def interactive_review(suggestions):
    grouped_suggestions = {}

    # Group suggestions by file
    for s in suggestions:
        grouped_suggestions.setdefault(s['file'], []).append(s)

    for file_path, file_suggestions in grouped_suggestions.items():
        if not os.path.exists(file_path):
            print(f"\n❌ File not found: {file_path} — skipping.")
            continue

        print(f"\n🔍 Reviewing suggestions for: {file_path}")
        lines = load_file_lines(file_path)

        modified = False

        for suggestion in file_suggestions:
            line_num = suggestion['line']
            original_line = suggestion['original'].strip()
            suggested_line = suggestion['suggested'].strip()
            reason = suggestion.get('reason', 'No reason provided.')

            print(f"\nLine {line_num}:")
            print(f"🔸 Original:  {original_line}")
            print(f"✅ Suggested: {suggested_line}")
            print(f"Reason:    {reason}")
            choice = input("Apply change? [y/n/q] (q = quit): ").strip().lower()

            if choice == 'y':
                index = line_num - 1
                if lines[index].strip() == original_line:
                    lines[index] = lines[index].replace(original_line, suggested_line)
                    print("✔ Change applied.")
                    modified = True
                else:
                    print("⚠ Original line mismatch. Skipped to prevent overwriting unintended content.")
            elif choice == 'q':
                print("Exiting early.")
                return
            else:
                print("Skipped.")

        if modified:
            save_file_lines(file_path, lines)
            print(f"💾 Changes saved to: {file_path}")
        else:
            print("No changes made.")


def main():
    parser = argparse.ArgumentParser(description="Check markdown files for style issues")
    parser.add_argument("--file", help="Path to a specific markdown file to check")
    parser.add_argument("--dir", help="Directory containing markdown files to check")
    parser.add_argument("--rules", default="tools/style_rules.json", help="JSON file containing style rules")
    parser.add_argument("--output", default="data/style_suggestions.json", help="Output file for suggestions")
    parser.add_argument("--install-spacy", action="store_true", help="Install spaCy and download the English model")
    args = parser.parse_args()

    # Install spaCy if requested
    if args.install_spacy:
        print("Installing spaCy and downloading the English model...")
        import subprocess
        subprocess.call([sys.executable, "-m", "pip", "install", "spacy"])
        subprocess.call([sys.executable, "-m", "spacy", "download", "en_core_web_sm"])
        print("Installation complete. Please run the script again without --install-spacy.")
        sys.exit(0)

    if not args.file and not args.dir:
        print("Error: Please provide either --file or --dir argument")
        sys.exit(1)

    # Load style rules
    style_rules = load_style_rules(args.rules)
    if not style_rules:
        print("Error: No style rules loaded. Check the rules file.")
        sys.exit(1)

    print(f"Loaded {len(style_rules)} style rules from {args.rules}")

    all_suggestions = []

    # Check a specific file
    if args.file:
        if not os.path.isfile(args.file):
            print(f"Error: File not found: {args.file}")
            sys.exit(1)

        if not args.file.endswith((".md", ".mdx")):
            print(f"Warning: {args.file} is not a markdown file. Checking anyway.")

        with open(args.file, "r", encoding="utf-8") as f:
            content = f.read()

        suggestions = check_style(content, args.file, style_rules)
        all_suggestions.extend(suggestions)
        print(f"Checked {args.file}: Found {len(suggestions)} style issues")

    # Check all markdown files in a directory
    if args.dir:
        if not os.path.isdir(args.dir):
            print(f"Error: Directory not found: {args.dir}")
            sys.exit(1)

        for root, _, files in os.walk(args.dir):
            for file in files:
                if file.endswith((".md", ".mdx")):
                    file_path = os.path.join(root, file)
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read()

                    suggestions = check_style(content, file_path, style_rules)
                    all_suggestions.extend(suggestions)
                    print(f"Checked {file_path}: Found {len(suggestions)} style issues")

    save_suggestions_to_file(all_suggestions, args.output)
    interactive_review(all_suggestions)

if __name__ == "__main__":
    main()
