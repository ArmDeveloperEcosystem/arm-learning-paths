#!/usr/bin/env python3

import sys
import yaml
import os
import re

ALLOWLIST_FILE = "tools/closed-filters-allow-list.yml"
REQUIRED_FIELDS = [
    "title", "minutes_to_complete", "who_is_this_for", "learning_objectives",
    "prerequisites", "author", "skilllevels", "subjects", "armips", "tools_software_languages",
    "operatingsystems", "further_reading", "weight", "layout", "learning_path_main_page"
]
VALID_SKILLLEVELS = {"Introductory", "Advanced"}

def load_allowlist():
    with open(ALLOWLIST_FILE, 'r') as f:
        data = yaml.safe_load(f)

    flat_subjects = set()
    for _, subjects in data.get('subjects', {}).items():
        flat_subjects.update(subjects)

    return {
        "subjects_by_category": data.get("subjects", {}),
        "flat_subjects": flat_subjects,
        "operatingsystems": set(data.get("operatingsystems", [])),
        "cloud_service_providers": set(data.get("cloud_service_providers", [])),
    }

def extract_frontmatter(path):
    with open(path, 'r') as f:
        content = f.read()
    if not content.startswith('---'):
        return None
    parts = list(yaml.safe_load_all(content))
    if len(parts) >= 2:
        return parts[0]
    return None

def get_category_from_path(path):
    match = re.match(r"content/learning-paths/([^/]+)/", path)
    return match.group(1) if match else None

import os

def is_valid_index_path(path):
    norm_path = os.path.normpath(path)
    parts = norm_path.split(os.sep)

    try:
        lp_index = parts.index("learning-paths")
        # Ensure path is: .../learning-paths/<category>/<learning-path>/_index.md
        return (
            parts[-1] == "_index.md" and
            len(parts) == lp_index + 4  # learning-paths + category + tutorial + _index.md
        )
    except ValueError:
        return False

def validate_file(path, allowlist):
    if not is_valid_index_path(path):
        print(f"Skipping {path} as it is not a learning path index file.")
        return

    data = extract_frontmatter(path)
    if not data:
        print(f"❌ Invalid or missing YAML frontmatter: {path}")
        return True

    errors = []
    # Check for required fields
    for field in REQUIRED_FIELDS:
        if field not in data:
            errors.append(f"Missing required field: {field}")

    # Validate skilllevels
    skill = data.get("skilllevels")
    if skill and skill not in VALID_SKILLLEVELS:
        errors.append(f"Invalid skilllevels: {skill}. Please choose from {', '.join(VALID_SKILLLEVELS)}")

    # Validate subjects
    subject = data.get("subjects")
    if subject and subject not in allowlist["flat_subjects"]:
        errors.append(f"Invalid subjects: {subject}.")

    # Validate OS if present
    osys = data.get("operatingsystems", [])
    if isinstance(osys, list):
        for os_entry in osys:
            if os_entry not in allowlist["operatingsystems"]:
                errors.append(f"Invalid operatingsystem: {os_entry}. Please choose from {', '.join(allowlist['operatingsystems'])}")

    # Validate subject/category mapping
    category = get_category_from_path(path)
    if category and subject:
        category_subjects = allowlist["subjects_by_category"].get(category)
        if category_subjects and subject not in category_subjects:
            errors.append(f"Subject '{subject}' not allowed for category '{category}'. Please choose from {', '.join(category_subjects)}")

    if errors:
        print(f"❌ Validation errors in {path}:")
        for e in errors:
            print(f"   - {e}")
        return True

    print(f"✅ {path} fields are verified.")
    return False

if __name__ == "__main__":
    files = sys.argv[1:]
    allowlist = load_allowlist()
    any_errors = False

    for f in files:
        if "content/" in f and f.endswith("_index.md") and os.path.exists(f):
            if validate_file(f, allowlist):
                any_errors = True



    if any_errors:
        sys.exit(1)