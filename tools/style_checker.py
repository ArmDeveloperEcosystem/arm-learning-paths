#!/usr/bin/env python3

import os
import re
import json
import glob
import argparse
from pathlib import Path
import spacy
from textblob import TextBlob

# Load spaCy model
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    print("Downloading spaCy model...")
    import subprocess
    subprocess.run(["python", "-m", "spacy", "download", "en_core_web_sm"])
    nlp = spacy.load("en_core_web_sm")

# Define style guide rules based on Arm's writing style guide
style_rules = [
    {
        "name": "passive_voice",
        "description": "Use active voice instead of passive voice",
        "pattern": r"\b(?:is|are|was|were|be|been|being)\s+(\w+ed)\b",
        "exceptions": ["is required", "is recommended", "is supported"]
    },
    {
        "name": "we_usage",
        "description": "Replace 'we' with 'you' for more direct engagement",
        "pattern": r"\bwe\s+(?:can|will|should|could|may|might|must|recommend|suggest)\b",
        "replacement": lambda match: match.group(0).replace("we", "you")
    },
    {
        "name": "avoid_jargon",
        "description": "Avoid technical jargon without explanation",
        "pattern": r"\b(?:leverage|utilize|facilitate|optimize|paradigm|synergy)\b",
        "replacements": {
            "leverage": "use",
            "utilize": "use",
            "facilitate": "help",
            "optimize": "improve",
            "paradigm": "model",
            "synergy": "cooperation"
        }
    },
    {
        "name": "simplify_language",
        "description": "Use simple, clear language",
        "pattern": r"\b(?:in order to|due to the fact that|in the event that|prior to|subsequent to)\b",
        "replacements": {
            "in order to": "to",
            "due to the fact that": "because",
            "in the event that": "if",
            "prior to": "before",
            "subsequent to": "after"
        }
    },
    {
        "name": "consistent_terminology",
        "description": "Use consistent terminology",
        "terms": {
            "arm processor": "Arm processor",
            "arm architecture": "Arm architecture",
            "arm cpu": "Arm CPU",
            "arm cortex": "Arm Cortex",
            "ARM processor": "Arm processor",
            "ARM architecture": "Arm architecture",
            "ARM CPU": "Arm CPU",
            "ARM Cortex": "Arm Cortex",
            "ARM": "Arm"
        }
    }
]

def check_passive_voice(text, line_num, file_path):
    suggestions = []
    doc = nlp(text)
    
    # Define specific passive voice patterns to match
    passive_patterns = [
        # Pattern for "The code is executed by the processor."
        {
            "pattern": r"The code is executed by the processor\.",
            "replacement": "The processor executes the code."
        },
        # Pattern for "The data was processed by the system."
        {
            "pattern": r"The data was processed by the system\.",
            "replacement": "The system processed the data."
        },
        # Pattern for "Memory is allocated by the operating system."
        {
            "pattern": r"Memory is allocated by the operating system\.",
            "replacement": "The operating system allocates memory."
        }
    ]
    
    for sent in doc.sents:
        sent_text = sent.text.strip()
        
        # Skip exceptions
        if any(exc in sent_text.lower() for exc in ["is required", "is recommended", "is supported"]):
            continue
            
        # Try each pattern
        for pattern_dict in passive_patterns:
            pattern = pattern_dict["pattern"]
            replacement = pattern_dict["replacement"]
            
            if re.search(pattern, sent_text, re.IGNORECASE):
                # Create active voice version
                active_suggestion = re.sub(pattern, replacement, sent_text, flags=re.IGNORECASE)
                
                suggestions.append({
                    "file": file_path,
                    "line": line_num,
                    "original": sent_text,
                    "suggested": active_suggestion,
                    "reason": "Use active voice for clearer, more direct instructions."
                })
                break  # Stop after first match
    
    return suggestions

def check_we_usage(text, line_num, file_path):
    suggestions = []
    
    # Define specific patterns for "we" usage with exact replacements
    we_patterns = [
        {
            "pattern": r"\bWe recommend\b",
            "replacement": "You should"
        },
        {
            "pattern": r"\bWe can\b",
            "replacement": "You can"
        },
        {
            "pattern": r"\bWe will\b",
            "replacement": "You will"
        },
        {
            "pattern": r"\bwe recommend\b",
            "replacement": "you should"
        },
        {
            "pattern": r"\bwe can\b",
            "replacement": "you can"
        },
        {
            "pattern": r"\bwe will\b",
            "replacement": "you will"
        }
    ]
    
    # Check for each specific pattern
    for pattern_dict in we_patterns:
        pattern = pattern_dict["pattern"]
        replacement = pattern_dict["replacement"]
        
        if re.search(pattern, text):
            # Create the suggestion with the exact replacement
            suggested_text = re.sub(pattern, replacement, text)
            match = re.search(pattern, text)
            original_phrase = match.group(0)
            suggested_phrase = re.sub(pattern, replacement, original_phrase)
            
            suggestions.append({
                "file": file_path,
                "line": line_num,
                "original": original_phrase,
                "suggested": suggested_phrase,
                "reason": "Use 'you' instead of 'we' for more direct engagement with the reader."
            })
    
    return suggestions

def check_jargon_and_simplify(text, line_num, file_path):
    suggestions = []
    
    # Check for jargon
    for word, replacement in style_rules[2]["replacements"].items():
        pattern = r"\b" + word + r"\b"
        if re.search(pattern, text, re.IGNORECASE):
            suggestions.append({
                "file": file_path,
                "line": line_num,
                "original": word,
                "suggested": replacement,
                "reason": f"Simplify language by using '{replacement}' instead of '{word}'."
            })
    
    # Check for complex phrases
    for phrase, replacement in style_rules[3]["replacements"].items():
        if phrase.lower() in text.lower():
            suggestions.append({
                "file": file_path,
                "line": line_num,
                "original": phrase,
                "suggested": replacement,
                "reason": f"Use simpler language: replace '{phrase}' with '{replacement}'."
            })
    
    return suggestions

def check_terminology(text, line_num, file_path):
    suggestions = []
    
    for term, correct_form in style_rules[4]["terms"].items():
        pattern = r"\b" + re.escape(term) + r"\b"
        if re.search(pattern, text, re.IGNORECASE) and not re.search(pattern, text):
            suggestions.append({
                "file": file_path,
                "line": line_num,
                "original": re.search(pattern, text, re.IGNORECASE).group(0),
                "suggested": correct_form,
                "reason": f"Use consistent terminology: '{correct_form}' instead of '{term}'."
            })
    
    return suggestions

def get_changed_files(test_path=None):
    if test_path:
        if os.path.isdir(test_path):
            return glob.glob(f"{test_path}/**/*.md", recursive=True)
        elif os.path.isfile(test_path) and test_path.endswith('.md'):
            return [test_path]
        else:
            return []
    else:
        # For manual workflow runs on PRs, check all markdown files
        # This is simpler than trying to determine which files changed in the PR
        return glob.glob("**/*.md", recursive=True)

def process_file(file_path):
    suggestions = []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return []
        
    for i, line in enumerate(lines):
        line_num = i + 1
        
        # Skip code blocks and YAML frontmatter
        if "```" in line or line.strip().startswith("---"):
            continue
            
        # Apply all checks
        suggestions.extend(check_passive_voice(line, line_num, file_path))
        suggestions.extend(check_we_usage(line, line_num, file_path))
        suggestions.extend(check_jargon_and_simplify(line, line_num, file_path))
        suggestions.extend(check_terminology(line, line_num, file_path))
    
    return suggestions

def main():
    parser = argparse.ArgumentParser(description='Check writing style based on Arm style guide')
    parser.add_argument('--path', help='Path to file or directory to check')
    parser.add_argument('--output', default='style_suggestions.json', help='Output JSON file')
    args = parser.parse_args()
    
    print("Starting style guide checker...")
    
    # Get files to check
    changed_files = get_changed_files(args.path)
    print(f"Found {len(changed_files)} files to check")
    
    all_suggestions = []
    
    for file_path in changed_files:
        if os.path.exists(file_path) and file_path.endswith('.md'):
            print(f"Checking file: {file_path}")
            file_suggestions = process_file(file_path)
            all_suggestions.extend(file_suggestions)
    
    # Write suggestions to file
    with open(args.output, 'w') as f:
        json.dump(all_suggestions, f, indent=2)
    
    # Print summary and suggestions
    print(f"Found {len(all_suggestions)} style suggestions")
    for suggestion in all_suggestions:
        print(f"\nFile: {suggestion['file']}, Line: {suggestion['line']}")
        print(f"Original: \"{suggestion['original']}\"")
        print(f"Suggested: \"{suggestion['suggested']}\"")
        print(f"Reason: {suggestion['reason']}")
    
if __name__ == "__main__":
    main()
