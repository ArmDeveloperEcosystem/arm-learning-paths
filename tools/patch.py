import yaml
from collections import defaultdict
from pathlib import PurePath
import re

"""
Parse results and patch stats file with test results
"""
def patch(article_path: str, results: dict, link: str):
    stats_file = "data/stats_current_test_info.yml"

    with open(stats_file, mode='r') as f:
        data = yaml.safe_load(f)
        f.close()

    article_path_pure = PurePath(re.sub(r"^.*?content/", "", article_path))
    article_path_parts = list(article_path_pure.parts)
    if "learning-paths" in article_path_parts:
        content_type, sw_category, content_title = article_path_parts
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

    for image, i in zip(test_images, range(len(test_images))):
        if content_title not in data["sw_categories"][sw_category]:
            raise SystemExit(f"{content_title} does not exist in {stats_file}. Add it to update the stats report.")
        data["sw_categories"][sw_category][content_title]["tests_and_status"][i][image] = results_values[results[image]]

    if link:
        data["sw_categories"][sw_category][content_title]["test_link"] = link


    with open(stats_file, mode='w') as f:
        yaml.dump(data, f)
        f.close()