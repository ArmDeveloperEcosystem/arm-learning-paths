#!/usr/bin/env python3

"""
External Link Checker for Hugo Website
Extracts and validates all external links from markdown files.
"""

import argparse
import glob
import re
import sys
import time
from collections import defaultdict
from pathlib import Path
from urllib.parse import urlparse
from threading import Lock
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

# Configuration
TIMEOUT = 10  # seconds
MAX_WORKERS = 10  # parallel requests
USER_AGENT = 'Mozilla/5.0 (compatible; LinkChecker/1.0)'
MAX_RETRIES = 3
RETRY_DELAY = 2  # seconds

# Domain-specific rate limits (delay in seconds)
DOMAIN_RATE_LIMITS = {
    'github.com': 1.0,
    'api.github.com': 2.0,
    'raw.githubusercontent.com': 1.0,
    'docs.github.com': 1.0,
    'stackoverflow.com': 0.5,
    'twitter.com': 1.0,
    'x.com': 1.0,
}
DEFAULT_RATE_LIMIT = 0.3

# Track last request time per domain
domain_last_request = {}
domain_locks = defaultdict(Lock)

# Patterns to extract links
MARKDOWN_LINK_PATTERN = r'\[([^\]]+)\]\(([^)]+)\)'
HTML_LINK_PATTERN = r'<a\s+(?:[^>]*?\s+)?href="([^"]*)"'
URL_PATTERN = r'https?://[^\s<>"{}|\\^`\[\]]+'


def is_external_link(url):
    """Check if URL is external (not internal path or anchor)."""
    if not url or url.startswith(('#', '/', 'mailto:', 'tel:')):
        return False
    parsed = urlparse(url)
    return parsed.scheme in ('http', 'https')


def extract_links_from_file(filepath):
    """Extract all external links from a markdown file."""
    links = set()
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Extract markdown links [text](url)
        for match in re.finditer(MARKDOWN_LINK_PATTERN, content):
            url = match.group(2)
            if is_external_link(url):
                links.add(url)
        
        # Extract HTML links <a href="url">
        for match in re.finditer(HTML_LINK_PATTERN, content):
            url = match.group(1)
            if is_external_link(url):
                links.add(url)
                
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
    
    return links


def get_domain_delay(url):
    """Get the appropriate delay for a domain."""
    try:
        domain = urlparse(url).netloc.lower()
        # Check for exact match
        if domain in DOMAIN_RATE_LIMITS:
            return DOMAIN_RATE_LIMITS[domain]
        # Check for subdomain matches (e.g., docs.github.com matches github.com)
        for rate_domain, delay in DOMAIN_RATE_LIMITS.items():
            if domain.endswith('.' + rate_domain) or domain == rate_domain:
                return delay
        return DEFAULT_RATE_LIMIT
    except:
        return DEFAULT_RATE_LIMIT


def rate_limit_wait(url):
    """Enforce per-domain rate limiting."""
    try:
        domain = urlparse(url).netloc.lower()
        lock = domain_locks[domain]
        
        with lock:
            now = time.time()
            last_request = domain_last_request.get(domain, 0)
            delay = get_domain_delay(url)
            time_since_last = now - last_request
            
            if time_since_last < delay:
                sleep_time = delay - time_since_last
                time.sleep(sleep_time)
            
            domain_last_request[domain] = time.time()
    except:
        pass  # If anything fails, just proceed


def check_link(url, session, timeout=TIMEOUT, max_retries=MAX_RETRIES):
    """Check if a URL is reachable with retries and rate limiting."""
    rate_limit_wait(url)
    
    for attempt in range(max_retries):
        try:
            response = session.head(url, timeout=timeout, allow_redirects=True)
            # Some servers don't support HEAD, try GET
            if response.status_code == 405 or response.status_code == 404:
                rate_limit_wait(url)  # Additional delay before GET
                response = session.get(url, timeout=timeout, allow_redirects=True, stream=True)
                # Don't download the full content, just check headers
                response.close()
            
            # Handle rate limiting
            if response.status_code == 429:
                retry_after = int(response.headers.get('Retry-After', RETRY_DELAY * (attempt + 1)))
                if attempt < max_retries - 1:
                    time.sleep(min(retry_after, 60))  # Cap at 60 seconds
                    continue
                return {
                    'url': url,
                    'status_code': 429,
                    'ok': False,
                    'error': 'Rate limited (429)',
                    'final_url': None
                }
            
            return {
                'url': url,
                'status_code': response.status_code,
                'ok': response.ok,
                'error': None,
                'final_url': response.url
            }
            
        except requests.exceptions.Timeout:
            if attempt < max_retries - 1:
                time.sleep(RETRY_DELAY * (attempt + 1))
                continue
            return {'url': url, 'status_code': None, 'ok': False, 'error': 'Timeout', 'final_url': None}
        except requests.exceptions.SSLError as e:
            # Don't retry SSL errors
            return {'url': url, 'status_code': None, 'ok': False, 'error': f'SSL Error: {str(e)[:100]}', 'final_url': None}
        except requests.exceptions.ConnectionError as e:
            if attempt < max_retries - 1:
                time.sleep(RETRY_DELAY * (attempt + 1))
                continue
            return {'url': url, 'status_code': None, 'ok': False, 'error': f'Connection Error: {str(e)[:100]}', 'final_url': None}
        except requests.exceptions.RequestException as e:
            if attempt < max_retries - 1:
                time.sleep(RETRY_DELAY * (attempt + 1))
                continue
            return {'url': url, 'status_code': None, 'ok': False, 'error': str(e)[:100], 'final_url': None}
        except Exception as e:
            return {'url': url, 'status_code': None, 'ok': False, 'error': f'Unexpected: {str(e)[:100]}', 'final_url': None}
    
    return {'url': url, 'status_code': None, 'ok': False, 'error': 'Max retries exceeded', 'final_url': None}


def main():
    parser = argparse.ArgumentParser(
        description='Check external links in Hugo markdown files',
        epilog='Note: GitHub links are automatically rate-limited to 1s between requests'
    )
    parser.add_argument('--content-dir', default='content', help='Content directory (default: content)')
    parser.add_argument('--output', default='external_links_report.txt', help='Output report file')
    parser.add_argument('--list-only', action='store_true', help='Only list links without checking')
    parser.add_argument('--max-workers', type=int, default=5, help='Maximum parallel workers (default: 5, lower = safer)')
    parser.add_argument('--timeout', type=int, default=TIMEOUT, help=f'Request timeout in seconds (default: {TIMEOUT})')
    parser.add_argument('--retries', type=int, default=MAX_RETRIES, help=f'Max retries per link (default: {MAX_RETRIES})')
    args = parser.parse_args()

    print(f"Scanning markdown files in {args.content_dir}...")
    
    # Find all markdown files
    md_files = list(Path(args.content_dir).rglob('*.md'))
    print(f"Found {len(md_files)} markdown files")
    
    # Extract all links
    print("Extracting external links...")
    link_to_files = defaultdict(list)
    
    for filepath in md_files:
        links = extract_links_from_file(filepath)
        for link in links:
            link_to_files[link].append(str(filepath))
    
    unique_links = list(link_to_files.keys())
    print(f"Found {len(unique_links)} unique external links")
    
    if args.list_only:
        print("\nExternal links:")
        for link in sorted(unique_links):
            print(f"  {link}")
        return 0
    
    # Check links
    print(f"\nChecking links (timeout={args.timeout}s, workers={args.max_workers}, retries={args.retries})...")
    print("Rate limiting: GitHub (1.0s), StackOverflow (0.5s), Others (0.3s)")
    print("This may take several minutes...\n")
    
    session = requests.Session()
    session.headers.update({'User-Agent': USER_AGENT})
    
    results = []
    with ThreadPoolExecutor(max_workers=args.max_workers) as executor:
        future_to_url = {executor.submit(check_link, url, session, args.timeout, args.retries): url for url in unique_links}
        
        for i, future in enumerate(as_completed(future_to_url), 1):
            result = future.result()
            results.append(result)
            
            # Progress indicator
            status = "✓" if result['ok'] else "✗"
            domain = urlparse(result['url']).netloc
            print(f"[{i}/{len(unique_links)}] {status} [{domain}] {result['url'][:60]}")
    
    # Generate report
    print(f"\nGenerating report: {args.output}")
    
    broken_links = [r for r in results if not r['ok']]
    working_links = [r for r in results if r['ok']]
    
    with open(args.output, 'w', encoding='utf-8') as f:
        f.write("External Links Report\n")
        f.write("=" * 80 + "\n\n")
        f.write(f"Total unique links: {len(unique_links)}\n")
        f.write(f"Working links: {len(working_links)}\n")
        f.write(f"Broken links: {len(broken_links)}\n\n")
        
        if broken_links:
            f.write("\nBROKEN LINKS\n")
            f.write("-" * 80 + "\n\n")
            for result in sorted(broken_links, key=lambda x: x['url']):
                f.write(f"URL: {result['url']}\n")
                f.write(f"Status: {result['status_code'] or 'N/A'}\n")
                f.write(f"Error: {result['error'] or 'HTTP ' + str(result['status_code'])}\n")
                f.write(f"Found in:\n")
                for filepath in link_to_files[result['url']]:
                    f.write(f"  - {filepath}\n")
                f.write("\n")
        
        f.write("\nWORKING LINKS\n")
        f.write("-" * 80 + "\n\n")
        for result in sorted(working_links, key=lambda x: x['url']):
            f.write(f"✓ [{result['status_code']}] {result['url']}\n")
            if result['final_url'] != result['url']:
                f.write(f"  → Redirects to: {result['final_url']}\n")
    
    print(f"\nSummary:")
    print(f"  Total links: {len(unique_links)}")
    print(f"  Working: {len(working_links)}")
    print(f"  Broken: {len(broken_links)}")
    
    if broken_links:
        print(f"\n⚠ Found {len(broken_links)} broken links!")
        print(f"See {args.output} for details")
        return 1
    else:
        print("\n✓ All external links are working!")
        return 0


if __name__ == '__main__':
    sys.exit(main())
