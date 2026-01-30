#!/usr/bin/env python3

"""
Headless Browser Link Checker
Re-tests broken links using a real browser to distinguish false positives from actual broken links.
Uses Playwright for headless browser automation.
"""

import argparse
import re
import sys
import time
from pathlib import Path
from urllib.parse import urlparse

try:
    from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeout
except ImportError:
    print("Error: Playwright not installed.")
    print("Install with: pip install playwright && playwright install chromium")
    sys.exit(1)


# URLs to skip (known to be examples/documentation only)
SKIP_PATTERNS = [
    r'^http://localhost',
    r'^https?://.*\.local',
    r'^http://.*\.sock',
    r'^http://example\.',
    r'^https?://your-',
]


def should_skip_url(url):
    """Check if URL should be skipped (localhost, examples, etc.)."""
    for pattern in SKIP_PATTERNS:
        if re.match(pattern, url, re.IGNORECASE):
            return True
    return False


def parse_broken_links_report(report_file):
    """Extract broken links from the report file."""
    broken_links = []
    
    try:
        with open(report_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Parse the broken links section
        broken_section = re.search(r'BROKEN LINKS\n-+\n\n(.*?)\n\nWORKING LINKS', content, re.DOTALL)
        if not broken_section:
            print("Could not find BROKEN LINKS section in report")
            return []
        
        # Extract URL blocks
        url_blocks = re.finditer(
            r'URL: (https?://[^\s]+)\nStatus: ([^\n]*)\nError: ([^\n]*)\nFound in:\n((?:  - [^\n]+\n)+)',
            broken_section.group(1)
        )
        
        for match in url_blocks:
            url = match.group(1)
            status = match.group(2)
            error = match.group(3)
            files = [line.strip()[2:] for line in match.group(4).strip().split('\n')]
            
            broken_links.append({
                'url': url,
                'status': status,
                'error': error,
                'files': files
            })
    
    except Exception as e:
        print(f"Error parsing report: {e}")
        return []
    
    return broken_links


def check_url_in_browser(page, url, timeout=15000):
    """Check if URL loads in headless browser."""
    try:
        # Navigate to URL
        response = page.goto(url, wait_until='domcontentloaded', timeout=timeout)
        
        if response is None:
            return {
                'url': url,
                'works': False,
                'status_code': None,
                'error': 'No response received',
                'title': None
            }
        
        status_code = response.status
        
        # Get page title
        try:
            title = page.title()
        except:
            title = None
        
        # Check for common error patterns in content
        content_lower = page.content().lower()
        is_error_page = any(pattern in content_lower for pattern in [
            '404', 'not found', 'page not found',
            '403', 'forbidden', 'access denied',
            'error', 'oops', 'something went wrong'
        ])
        
        # Consider it working if status is OK and it's not an obvious error page
        works = (200 <= status_code < 400) and (not is_error_page or status_code == 200)
        
        return {
            'url': url,
            'works': works,
            'status_code': status_code,
            'error': None if works else f'Status {status_code}' + (' (Error page detected)' if is_error_page else ''),
            'title': title
        }
        
    except PlaywrightTimeout:
        return {
            'url': url,
            'works': False,
            'status_code': None,
            'error': 'Timeout in browser',
            'title': None
        }
    except Exception as e:
        return {
            'url': url,
            'works': False,
            'status_code': None,
            'error': f'Browser error: {str(e)[:100]}',
            'title': None
        }


def main():
    parser = argparse.ArgumentParser(
        description='Re-check broken links using headless browser',
        epilog='Requires: pip install playwright && playwright install chromium'
    )
    parser.add_argument('--report', default='external_links_report.txt',
                        help='Input report file (default: external_links_report.txt)')
    parser.add_argument('--output', default='browser_check_report.txt',
                        help='Output report file (default: browser_check_report.txt)')
    parser.add_argument('--timeout', type=int, default=15,
                        help='Page load timeout in seconds (default: 15)')
    parser.add_argument('--delay', type=float, default=1.0,
                        help='Delay between requests in seconds (default: 1.0)')
    parser.add_argument('--filter', choices=['403', '404', 'timeout', 'all'], default='all',
                        help='Filter which errors to recheck (default: all)')
    parser.add_argument('--headless', action='store_true', default=True,
                        help='Run browser in headless mode (default: True)')
    args = parser.parse_args()
    
    print(f"Reading broken links from: {args.report}")
    broken_links = parse_broken_links_report(args.report)
    
    if not broken_links:
        print("No broken links found in report")
        return 1
    
    print(f"Found {len(broken_links)} broken links in report")
    
    # Filter links based on criteria
    filtered_links = []
    for link in broken_links:
        # Skip localhost and example URLs
        if should_skip_url(link['url']):
            continue
        
        # Filter by error type if specified
        if args.filter != 'all':
            if args.filter == '403' and link['status'] != '403':
                continue
            elif args.filter == '404' and link['status'] != '404':
                continue
            elif args.filter == 'timeout' and 'Timeout' not in link['error']:
                continue
        
        filtered_links.append(link)
    
    print(f"Testing {len(filtered_links)} links in headless browser (skipped {len(broken_links) - len(filtered_links)} localhost/examples)")
    print("This may take several minutes...\n")
    
    # Launch browser
    results = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=args.headless)
        context = browser.new_context(
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        )
        page = context.new_page()
        
        for i, link in enumerate(filtered_links, 1):
            print(f"[{i}/{len(filtered_links)}] Testing: {link['url'][:70]}")
            
            result = check_url_in_browser(page, link['url'], timeout=args.timeout * 1000)
            result['original_status'] = link['status']
            result['original_error'] = link['error']
            result['files'] = link['files']
            results.append(result)
            
            status_icon = "✓" if result['works'] else "✗"
            print(f"             {status_icon} {result['status_code'] or 'N/A'} - {result['error'] or 'OK'}")
            
            time.sleep(args.delay)
        
        browser.close()
    
    # Generate report
    print(f"\nGenerating report: {args.output}")
    
    false_positives = [r for r in results if r['works']]
    still_broken = [r for r in results if not r['works']]
    
    with open(args.output, 'w', encoding='utf-8') as f:
        f.write("Browser-Based Link Check Report\n")
        f.write("=" * 80 + "\n\n")
        f.write(f"Links tested: {len(results)}\n")
        f.write(f"Working in browser (false positives): {len(false_positives)}\n")
        f.write(f"Still broken: {len(still_broken)}\n\n")
        
        if false_positives:
            f.write("\nFALSE POSITIVES - Working in browser\n")
            f.write("-" * 80 + "\n")
            f.write("These links work in a browser but failed automated checking.\n")
            f.write("They likely use bot detection or require JavaScript.\n\n")
            
            for result in sorted(false_positives, key=lambda x: x['url']):
                f.write(f"URL: {result['url']}\n")
                f.write(f"Original error: {result['original_error']}\n")
                f.write(f"Browser status: {result['status_code']} - {result['title'] or 'No title'}\n")
                f.write(f"Found in:\n")
                for filepath in result['files']:
                    f.write(f"  - {filepath}\n")
                f.write("\n")
        
        if still_broken:
            f.write("\nSTILL BROKEN - Need fixing\n")
            f.write("-" * 80 + "\n")
            f.write("These links don't work even in a real browser.\n\n")
            
            for result in sorted(still_broken, key=lambda x: x['url']):
                f.write(f"URL: {result['url']}\n")
                f.write(f"Original error: {result['original_error']}\n")
                f.write(f"Browser error: {result['error']}\n")
                f.write(f"Status code: {result['status_code'] or 'N/A'}\n")
                f.write(f"Found in:\n")
                for filepath in result['files']:
                    f.write(f"  - {filepath}\n")
                f.write("\n")
    
    print(f"\nSummary:")
    print(f"  Total tested: {len(results)}")
    print(f"  False positives (work in browser): {len(false_positives)}")
    print(f"  Still broken (need fixing): {len(still_broken)}")
    
    if still_broken:
        print(f"\n⚠ Found {len(still_broken)} links that need fixing!")
    
    print(f"\nFull report: {args.output}")
    return 0


if __name__ == '__main__':
    sys.exit(main())
