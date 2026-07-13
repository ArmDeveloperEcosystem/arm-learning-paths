"""
Generate weekly stats for the Arm Learning Paths /stats page.

Reads content summary data from the roadmap repo for accurate category counts,
reads author metadata from local content directories, queries the GitHub API
for repo stats, and appends a new weekly entry to data/stats_weekly_data.yml.

Usage (in CI):
    python3 stats_data_generate.py --token $GITHUB_TOKEN

Usage (local, without GitHub stats):
    python3 stats_data_generate.py --no-github
"""

import os
import re
import csv
import yaml
import argparse
import requests
from pathlib import Path
from datetime import datetime


REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = REPO_ROOT / 'data' / 'stats_weekly_data.yml'
LP_DIR = REPO_ROOT / 'content' / 'learning-paths'
IG_DIR = REPO_ROOT / 'content' / 'install-guides'
CONTRIBUTORS_CSV = REPO_ROOT / 'assets' / 'contributors.csv'
GITHUB_API = 'https://api.github.com/repos/ArmDeveloperEcosystem/arm-learning-paths'
ROADMAP_RAW = 'https://raw.githubusercontent.com/ArmDeveloperEcosystem/roadmap/main/reports/content-count'


def urlize(s):
    return s.replace(' ', '-').lower()


def load_contributors_csv():
    authors = {}
    with open(CONTRIBUTORS_CSV, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row['author'].strip().lower()
            authors[name] = row['company'].strip()
    return authors


def read_metadata(md_path):
    lines = []
    in_meta = False
    with open(md_path, encoding='utf-8') as f:
        for line in f:
            if line.strip() == '---':
                if in_meta:
                    break
                in_meta = True
                continue
            if in_meta:
                lines.append(line)
    return yaml.safe_load(''.join(lines)) or {}


def fetch_content_summary():
    """Fetch the latest content_summary from the roadmap repo.

    File naming: content_summary_MM-01-YYYY.md where date is first of next month.
    Tries next month first, then current month, then previous months going back.
    """
    now = datetime.now()
    candidates = []

    # Try next month, current month, and previous months
    for offset in range(1, -6, -1):
        month = now.month + offset
        year = now.year
        while month > 12:
            month -= 12
            year += 1
        while month < 1:
            month += 12
            year -= 1
        candidates.append(f'{month:02d}-01-{year}')
        candidates.append(f'{month:02d}-1-{year}')

    for date_str in candidates:
        url = f'{ROADMAP_RAW}/content_summary_{date_str}.md'
        resp = requests.get(url)
        if resp.status_code == 200:
            print(f'Fetched content summary: content_summary_{date_str}.md')
            return resp.text

    print('ERROR: Could not fetch any content summary from roadmap repo.')
    return None


def parse_content_summary(md_text):
    """Parse content summary markdown for category totals and headline number."""
    result = {'total_published': 0, 'categories': {}, 'install_guides': 0}

    match = re.search(r'Total Published Content.*?\|\s*(\d+)\s*\|', md_text)
    if match:
        result['total_published'] = int(match.group(1))

    cat_pattern = re.compile(
        r'\|\s*(.+?)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|'
    )
    for m in cat_pattern.finditer(md_text):
        cat_name = m.group(1).strip().strip('|').strip()
        total = int(m.group(2))
        if not cat_name or cat_name.startswith('-'):
            continue
        result['categories'][cat_name] = total

    ig_match = re.search(r'Install Guides\s*\|\s*(\d+)\s*\|', md_text)
    if ig_match:
        result['install_guides'] = int(ig_match.group(1))

    return result


def discover_categories():
    return sorted([
        d.name for d in LP_DIR.iterdir()
        if d.is_dir() and d.name != '_example-learning-path'
    ])


def count_authors():
    """Count authors from all published content."""
    categories = discover_categories()
    authors = {}

    for cat in categories:
        cat_dir = LP_DIR / cat
        for item in cat_dir.iterdir():
            if not item.is_dir() or item.name.startswith('_'):
                continue
            index_file = item / '_index.md'
            if not index_file.exists():
                continue
            meta = read_metadata(index_file)
            if meta.get('draft', False):
                continue
            author_field = meta.get('author', '')
            if author_field:
                author_names = author_field if isinstance(author_field, list) else [author_field]
                for name in author_names:
                    key = urlize(name.strip())
                    if key:
                        authors[key] = authors.get(key, 0) + 1

    for item in IG_DIR.iterdir():
        if item.name.startswith('_') or item.name == '_images':
            continue
        if item.is_file() and item.suffix == '.md':
            meta = read_metadata(item)
            if not meta.get('draft', False):
                author_field = meta.get('author', '')
                if author_field:
                    for name in (author_field if isinstance(author_field, list) else [author_field]):
                        key = urlize(name.strip())
                        if key:
                            authors[key] = authors.get(key, 0) + 1
        elif item.is_dir():
            for sub in item.iterdir():
                if sub.name.startswith('_') or sub.suffix != '.md':
                    continue
                meta = read_metadata(sub)
                if not meta.get('draft', False):
                    author_field = meta.get('author', '')
                    if author_field:
                        for name in (author_field if isinstance(author_field, list) else [author_field]):
                            key = urlize(name.strip())
                            if key:
                                authors[key] = authors.get(key, 0) + 1

    return authors


def classify_contributions(authors_dict):
    csv_authors = load_contributors_csv()
    internal = 0
    external = 0
    for author_key, count in authors_dict.items():
        matched = False
        for csv_name, company in csv_authors.items():
            if urlize(csv_name) == author_key:
                if company.lower() == 'arm':
                    internal += count
                else:
                    external += count
                matched = True
                break
        if not matched:
            external += count
    return {'internal': internal, 'external': external}


def get_github_stats(token=None):
    headers = {'Accept': 'application/vnd.github.v3+json'}
    if token:
        headers['Authorization'] = f'token {token}'

    resp = requests.get(GITHUB_API, headers=headers)
    resp.raise_for_status()
    repo = resp.json()

    open_prs = 0
    pr_resp = requests.get(
        f'{GITHUB_API}/pulls', headers=headers,
        params={'state': 'open', 'per_page': 1}
    )
    if pr_resp.ok:
        if 'Link' in pr_resp.headers:
            match = re.search(r'page=(\d+)>; rel="last"', pr_resp.headers['Link'])
            if match:
                open_prs = int(match.group(1))
        else:
            open_prs = len(pr_resp.json())

    return {
        'stars': repo.get('stargazers_count', 0),
        'forks': repo.get('forks_count', 0),
        'open_prs': open_prs
    }


def build_entry(token=None, no_github=False):
    authors = count_authors()
    contributions = classify_contributions(authors)

    # Get content counts from roadmap repo
    summary_md = fetch_content_summary()
    if not summary_md:
        raise SystemExit('ERROR: No content summary available from roadmap repo. Cannot generate stats.')

    summary = parse_content_summary(summary_md)
    content = {
        'total': summary['total_published'],
        'install-guides': summary.get('install_guides', 0),
    }
    for cat_name, total in summary['categories'].items():
        content[urlize(cat_name)] = total

    entry = {
        'date': datetime.now().strftime('%Y-%m-%d'),
        'content': content,
        'individual_authors': dict(sorted(authors.items())),
        'contributions': contributions,
    }

    if not no_github:
        try:
            entry['github'] = get_github_stats(token)
        except Exception as e:
            print(f'WARNING: GitHub API call failed: {e}')
            entry['github'] = {'stars': 0, 'forks': 0, 'open_prs': 0}
    else:
        entry['github'] = {'stars': 0, 'forks': 0, 'open_prs': 0}

    return entry


def main():
    parser = argparse.ArgumentParser(description='Generate weekly stats for /stats page')
    parser.add_argument('-t', '--token', help='GitHub personal access token')
    parser.add_argument('--no-github', action='store_true', help='Skip GitHub API calls')
    args = parser.parse_args()

    if DATA_FILE.exists():
        existing = yaml.safe_load(DATA_FILE.read_text()) or []
    else:
        existing = []

    entry = build_entry(token=args.token, no_github=args.no_github)
    today = entry['date']

    for i, e in enumerate(existing):
        if e.get('date') == today:
            print(f'Entry for {today} already exists, updating.')
            existing[i] = entry
            break
    else:
        existing.append(entry)
        print(f'Appended new entry for {today}.')

    with open(DATA_FILE, 'w') as f:
        yaml.dump(existing, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    print(f'Total content: {entry["content"]["total"]}')
    print(f'Unique authors: {len(entry["individual_authors"])}')
    print(f'Written to: {DATA_FILE}')


if __name__ == '__main__':
    main()
