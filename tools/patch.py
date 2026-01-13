import yaml
from collections import defaultdict
from pathlib import PurePath
import re

"""
Parse results and patch stats file with test results
NOTE: This function is deprecated and no longer updates stats files.
Test status is now managed only through CI/CD workflows.
"""
def patch(article_path: str, results: dict, link: str):
    # This function is deprecated - test status no longer tracked in stats files
    print("Warning: patch() is deprecated. Test status is no longer tracked in stats_current_test_info.yml")
    return

    article_path_pure = PurePath(re.sub(r"^.*?content/", "", article_path))
    article_path_parts = list(article_path_pure.parts)
    if "learning-paths" in article_path_parts:
        content_type, sw_category, content_title, *others = article_path_parts
        article_path = PurePath(article_path, "_index.md")
    elif "install-guides" in article_path_parts:
        # In case the install guide is in a subdirectory
        if len(article_path_parts) > 3:
            content_type, subdirectory, content_title, *others = article_path_parts
        else:
            content_type, content_title, *others = article_path_parts
        # Remove ".md" from the content title if it exists
        content_title = content_title[:-3] if content_title.endswith(".md") else content_title
        sw_category = content_type
    else:
        raise SystemExit("Unknown content path, pass learning paths or install guides only")

    test_images = results.keys()
    results_values = defaultdict(lambda: "failed")
    results_values[0] = "passed"

    content_data = data["sw_categories"][sw_category][content_title]

    # Create 'tests_and_status' if it doesn't exist
    if "tests_and_status" not in content_data or not isinstance(content_data["tests_and_status"], list):
        content_data["tests_and_status"] = [{} for _ in range(len(test_images))]

    # If 'tests_and_status' exists but is too short, extend it
    if len(content_data["tests_and_status"]) < len(test_images):
        additional_entries = [{} for _ in range(len(test_images) - len(content_data["tests_and_status"]))]
        content_data["tests_and_status"].extend(additional_entries)

    # Now safe to index
    for i, image in enumerate(test_images):
        idx = min(i, len(content_data["tests_and_status"]) - 1)
        content_data["tests_and_status"][idx][image] = results_values[results[image]]

    if link:
        data["sw_categories"][sw_category][content_title]["test_link"] = link


    with open(stats_file, mode='w') as f:
        yaml.dump(data, f)
        f.close()