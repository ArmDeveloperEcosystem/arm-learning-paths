# concierge_agent.py
# A terminal-based AI agent that acts as a local concierge.
# It uses a local Gemma model served by Ollama for reasoning and external tools
# for web search and browsing.

import os
import requests
from bs4 import BeautifulSoup
import json
import smtplib
from email.message import EmailMessage
import concurrent.futures
import re
import math
import difflib
import hashlib
from collections import Counter, defaultdict
import time

# --- Configuration ---
# Read secrets and settings from environment variables.
# Get a free Serper API key from https://serper.dev
SERPER_API_KEY = os.environ.get("SERPER_API_KEY", "")

# Ollama configuration
OLLAMA_HOST = os.environ.get("OLLAMA_HOST", "http://localhost:11434")
OLLAMA_MODEL = os.environ.get("OLLAMA_MODEL", "gemma3:4b")  # Runs on modest hardware

# SMTP configuration for the optional email tool
SMTP_SERVER = os.environ.get("SMTP_SERVER")
SMTP_PORT = int(os.environ.get("SMTP_PORT", 587))  # Default to 587 for STARTTLS
SMTP_USERNAME = os.environ.get("SMTP_USERNAME")
SMTP_PASSWORD = os.environ.get("SMTP_PASSWORD")

ANSI_RESET = "\033[0m"
ANSI_CPU = "\033[36m"  # Cyan
ANSI_GPU = "\033[33m"  # Yellow
ANSI_GREEN = "\033[32m"
ANSI_YELLOW = "\033[33m"
ANSI_RED = "\033[31m"
ANSI_MAGENTA = "\033[35m"


def log_cpu(message: str) -> None:
    print(f"{ANSI_CPU}[CPU]{ANSI_RESET} {message}")


def log_gpu(message: str) -> None:
    print(f"{ANSI_GPU}[GPU]{ANSI_RESET} {message}")


def render_timeline(events: list, width: int = 60) -> str:
    """
    Render a timestamp-based timeline from event intervals.
    Each event is a tuple: (start_ts, end_ts, kind) where kind is
    "cpu", "gpu_preload", or "gpu_tokens".
    """
    if not events:
        return "No timeline data."
    start_ts = min(e[0] for e in events)
    end_ts = max(e[1] for e in events)
    total = max(end_ts - start_ts, 1e-6)
    step = total / width
    bar_chars = []
    for i in range(width):
        t0 = start_ts + i * step
        t1 = t0 + step
        active = None
        for ev_start, ev_end, kind in events:
            if ev_end <= t0 or ev_start >= t1:
                continue
            active = kind
            break
        if active == "cpu":
            bar_chars.append(f"{ANSI_GREEN}C")
        elif active == "gpu_preload":
            bar_chars.append(f"{ANSI_MAGENTA}P")
        elif active == "gpu_tokens":
            bar_chars.append(f"{ANSI_RED}G")
        else:
            bar_chars.append(f"{ANSI_RESET}.")
    bar = "".join(bar_chars) + ANSI_RESET
    legend = (
        f"{ANSI_GREEN}C=CPU (orchestration + web I/O){ANSI_RESET} "
        f"{ANSI_MAGENTA}P=GPU input token processing{ANSI_RESET} "
        f"{ANSI_RED}G=GPU token generation{ANSI_RESET} "
        f"{ANSI_RESET}.=idle"
    )
    return f"{bar}\n{legend}\nTotal: {total:.3f}s"


# --- Part 1: The agent's tools ---

def search_web(query: str) -> str:
    """Use the Serper.dev API to perform a web search."""
    log_cpu(f"Searching web: '{query}'")
    if not SERPER_API_KEY:
        return "Error: SERPER_API_KEY is not set. Cannot perform web search."

    payload = json.dumps({"q": query})
    headers = {'X-API-KEY': SERPER_API_KEY, 'Content-Type': 'application/json'}

    try:
        response = requests.post("https://google.serper.dev/search", headers=headers, data=payload)
        response.raise_for_status()
        results = response.json()

        if not results.get("organic"):
            return "No good search results found."

        output = "Search Results:\n"
        for item in results["organic"][:5]:  # Top 5 results
            output += f"- Title: {item.get('title', 'N/A')}\n"
            output += f"  Link: {item.get('link', 'N/A')}\n"
            output += f"  Snippet: {item.get('snippet', 'N/A')}\n\n"
        return output

    except requests.exceptions.RequestException as e:
        return f"Error during web search: {e}"


def browse_website(url: str) -> str:
    """Scrape and clean the text content of a given URL."""
    log_cpu(f"Browsing website: '{url}'")
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/108.0.0.0 Safari/537.36',
            'Accept-Language': 'en-US,en;q=0.9',
            'Connection': 'keep-alive',
        }
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')
        for script_or_style in soup(['script', 'style']):
            script_or_style.decompose()

        text = soup.get_text()
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = '\n'.join(chunk for chunk in chunks if chunk)

        if not text:
            return f"Error: No text content found at {url}"

        log_cpu(f"Successfully browsed {url}")
        return text[:8000]

    except requests.exceptions.RequestException as e:
        return f"Error browsing website {url}: {e}"


def send_email(to_address: str, subject: str, body: str) -> str:
    """Send an email using the configured SMTP settings."""
    log_cpu(f"Sending email to '{to_address}'")
    if not all([SMTP_SERVER, SMTP_PORT, SMTP_USERNAME, SMTP_PASSWORD]):
        return "Error: SMTP settings are not fully configured. Cannot send email."

    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = SMTP_USERNAME
    msg['To'] = to_address

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.send_message(msg)
        return f"Email sent successfully to {to_address}."
    except Exception as e:
        return f"Error sending email: {e}"


# --- Part 1.5: CPU orchestration and processing pipeline ---

def generate_search_queries(base_query: str, goal: str) -> list:
    """Generate multiple search query variants for broader web coverage."""
    log_cpu(f"Expanding base query '{base_query}' into multiple variants...")
    variants = [base_query, f"best {base_query}", f"{base_query} 2026"]
    seen = set()
    unique_variants = []
    for q in variants:
        if q not in seen:
            seen.add(q)
            unique_variants.append(q)
    log_cpu(f"Generated {len(unique_variants)} search variants: {unique_variants}")
    return unique_variants


def parallel_search(queries: list) -> str:
    """Orchestrate concurrent web searches across multiple query variants."""
    log_cpu(f"Dispatching {len(queries)} parallel search threads...")
    results_by_query = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=len(queries)) as executor:
        future_to_query = {executor.submit(search_web, q): q for q in queries}
        for future in concurrent.futures.as_completed(future_to_query):
            query = future_to_query[future]
            try:
                results_by_query[query] = future.result()
                log_cpu(f"Search thread complete for: '{query}'")
            except Exception as e:
                results_by_query[query] = f"Error: {e}"
    return merge_search_results(results_by_query)


def merge_search_results(results_by_query: dict) -> str:
    """Merge results from multiple searches, deduplicating by URL."""
    log_cpu("Merging search results and deduplicating URLs...")
    seen_urls = set()
    merged_output = "Aggregated Search Results:\n"
    for query, result_text in results_by_query.items():
        merged_output += f"\n[Query: '{query}']\n"
        current_url = None
        pending_lines = []
        for line in result_text.split('\n'):
            if line.strip().startswith('Link:'):
                current_url = line.strip().replace('Link:', '').strip()
                if current_url in seen_urls:
                    pending_lines = []
                    current_url = None
                    continue
                seen_urls.add(current_url)
            pending_lines.append(line)
            if line == '' and pending_lines:
                merged_output += '\n'.join(pending_lines) + '\n'
                pending_lines = []
        if pending_lines:
            merged_output += '\n'.join(pending_lines) + '\n'
    log_cpu(f"Merged {len(results_by_query)} result sets -> {len(seen_urls)} unique URLs")
    return merged_output


def parallel_browse(urls: list) -> list:
    """Orchestrate concurrent browsing of multiple URLs using a thread pool."""
    log_cpu(f"Dispatching {len(urls)} parallel browse threads...")
    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=min(len(urls), 10)) as executor:
        future_to_url = {executor.submit(browse_website, url): url for url in urls}
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:
                text = future.result()
                results.append((url, text))
                status = "OK" if not text.startswith("Error") else "FAILED"
                log_cpu(f"Browse thread [{status}]: {url}")
            except Exception as e:
                results.append((url, f"Error: {e}"))
                log_cpu(f"Browse thread [EXCEPTION]: {url}")
    return results


def compute_tfidf_score(text: str, query_terms: list) -> float:
    """Compute a TF-IDF relevance score for a document against query terms."""
    if not text or not query_terms:
        return 0.0
    words = re.findall(r'\b\w+\b', text.lower())
    if not words:
        return 0.0
    word_freq = Counter(words)
    total_words = len(words)
    score = 0.0
    for term in query_terms:
        tf = word_freq.get(term.lower(), 0) / total_words
        idf = math.log(1 + len(query_terms) / (1 + sum(1 for t in query_terms if t == term)))
        score += tf * idf
    return score


def rank_and_filter_content(scraped_pairs: list, goal: str) -> list:
    """Rank scraped pages by TF-IDF relevance to the user's goal."""
    log_cpu("Running TF-IDF ranking on scraped content...")
    stop_words = {'the', 'a', 'an', 'in', 'on', 'at', 'to', 'for', 'of', 'and', 'or', 'i', 'me',
                  'my', 'we', 'is', 'are', 'was', 'were', 'be', 'been', 'have', 'has', 'had',
                  'do', 'does', 'did', 'will', 'would', 'could', 'should'}
    query_terms = [w.lower() for w in re.findall(r'\b\w+\b', goal)
                   if w.lower() not in stop_words and len(w) > 2]
    ranked = []
    for url, text in scraped_pairs:
        if text.startswith("Error"):
            log_cpu(f"Skipping failed URL: {url}")
            continue
        score = compute_tfidf_score(text, query_terms)
        ranked.append((url, text, score))
        log_cpu(f"  TF-IDF score {score:.5f} -> {url[:60]}")
    ranked.sort(key=lambda x: x[2], reverse=True)
    if ranked:
        log_cpu(f"Top-ranked page: {ranked[0][0]} (score={ranked[0][2]:.5f})")
    return ranked


def extract_entities(text: str) -> dict:
    """Extract structured entities (phones, hours, prices, URLs) via regex."""
    log_cpu("Extracting named entities from aggregated content...")
    entities = {'phone_numbers': [], 'hours': [], 'prices': [], 'urls': []}
    phone_re = re.compile(r'\(?\d{3}\)?[\s.\-]?\d{3}[\s.\-]?\d{4}')
    hours_re = re.compile(
        r'(?:Mon|Tue|Wed|Thu|Fri|Sat|Sun)[a-z]*'
        r'(?:[\s\-\u2013]+(?:Mon|Tue|Wed|Thu|Fri|Sat|Sun)[a-z]*)?'
        r'[\s:]+\d{1,2}(?::\d{2})?\s*(?:am|pm)\s*[-\u2013]\s*\d{1,2}(?::\d{2})?\s*(?:am|pm)',
        re.IGNORECASE
    )
    price_re = re.compile(r'\$\d+(?:\.\d{2})?(?:\s*[-\u2013]\s*\$\d+(?:\.\d{2})?)?')
    url_re = re.compile(r'https?://[^\s<>"\']+')
    entities['phone_numbers'] = list(dict.fromkeys(phone_re.findall(text)))[:5]
    entities['hours'] = list(dict.fromkeys(hours_re.findall(text)))[:5]
    entities['prices'] = list(dict.fromkeys(price_re.findall(text)))[:5]
    entities['urls'] = list(dict.fromkeys(url_re.findall(text)))[:10]
    total = sum(len(v) for v in entities.values())
    log_cpu(f"Entity extraction complete: {total} entities")
    return entities


def deduplicate_sentences(texts: list, similarity_threshold: float = 0.82) -> str:
    """Remove near-duplicate sentences across all source texts."""
    log_cpu("Deduplicating sentences across all scraped sources...")
    all_sentences = []
    for text in texts:
        for sent in re.split(r'(?<=[.!?])\s+', text):
            sent = sent.strip()
            if len(sent) > 40:
                all_sentences.append(sent)
    unique_sentences = []
    for candidate in all_sentences:
        is_dup = False
        for existing in unique_sentences[-60:]:
            if difflib.SequenceMatcher(None, candidate[:180], existing[:180]).ratio() > similarity_threshold:
                is_dup = True
                break
        if not is_dup:
            unique_sentences.append(candidate)
    log_cpu(f"Deduplication: {len(all_sentences)} raw sentences -> {len(unique_sentences)} unique")
    return ' '.join(unique_sentences[:300])


def compute_content_fingerprints(texts: list) -> dict:
    """Generate shingle-based content fingerprints per document."""
    log_cpu("Computing content fingerprints using 5-word shingles...")
    fingerprints = {}
    for doc_id, text in enumerate(texts):
        words = text.lower().split()
        shingles = set()
        for i in range(len(words) - 4):
            shingle = ' '.join(words[i:i + 5])
            shingles.add(hashlib.md5(shingle.encode()).hexdigest())
        fingerprints[doc_id] = shingles
        log_cpu(f"  Doc {doc_id}: {len(shingles)} shingles generated")
    return fingerprints


def find_near_duplicates(fingerprints: dict, threshold: float = 0.25) -> list:
    """Compute pairwise Jaccard similarity to detect near-duplicate pages."""
    log_cpu("Computing pairwise Jaccard similarities for near-duplicate detection...")
    keys = list(fingerprints.keys())
    duplicates = []
    for i in range(len(keys)):
        for j in range(i + 1, len(keys)):
            s1, s2 = fingerprints[keys[i]], fingerprints[keys[j]]
            union = len(s1 | s2)
            if union == 0:
                continue
            jaccard = len(s1 & s2) / union
            if jaccard > threshold:
                duplicates.append((keys[i], keys[j], jaccard))
                log_cpu(f"  Near-duplicate: doc {keys[i]} <-> doc {keys[j]} (Jaccard={jaccard:.3f})")
    log_cpu(f"Near-duplicate detection complete: {len(duplicates)} pairs found")
    return duplicates


def build_keyword_index(texts: list) -> dict:
    """Build an inverted keyword index across all scraped documents."""
    log_cpu("Building inverted keyword index...")
    stop_words = {'the', 'a', 'an', 'in', 'on', 'at', 'to', 'for', 'of', 'and', 'or', 'is', 'are',
                  'was', 'were', 'be', 'been', 'have', 'has', 'had', 'do', 'does', 'did', 'will',
                  'would', 'could', 'should', 'may', 'might', 'this', 'that', 'with', 'from', 'by',
                  'as', 'it', 'its'}
    index = defaultdict(list)
    for doc_id, text in enumerate(texts):
        words = re.findall(r'\b[a-zA-Z]{3,}\b', text.lower())
        word_freq = Counter(w for w in words if w not in stop_words)
        for word, freq in word_freq.most_common(150):
            index[word].append((doc_id, freq))
    log_cpu(f"Keyword index complete: {len(index)} unique terms across {len(texts)} documents")
    return dict(index)


def format_entity_summary(entities: dict) -> str:
    """Format extracted entity data for inclusion in the summarization prompt."""
    parts = []
    if entities.get('phone_numbers'):
        parts.append(f"Phone Numbers: {', '.join(entities['phone_numbers'])}")
    if entities.get('hours'):
        parts.append(f"Hours of Operation: {', '.join(entities['hours'])}")
    if entities.get('prices'):
        parts.append(f"Prices/Costs: {', '.join(entities['prices'])}")
    if entities.get('urls'):
        parts.append(f"Key URLs: {', '.join(entities['urls'][:5])}")
    return '\n'.join(parts)


# --- Part 2: The agent's brain (Ollama interaction) ---

def call_gemma_ollama(prompt: str, output_format: str = "json", timing: dict = None,
                      label: str = "ollama", timeline_events: list = None) -> str:
    """Call the local Ollama API and return the model response."""
    log_gpu("Thinking with local Gemma model...")
    payload = {
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "stream": True,
        "keep_alive": -1,  # Keep model weights in GPU memory
    }
    if output_format == "json":
        payload["format"] = "json"

    try:
        start_ts = time.perf_counter()
        first_token_ts = None
        chunks = []
        with requests.post(f"{OLLAMA_HOST}/api/generate", json=payload, stream=True, timeout=60) as response:
            response.raise_for_status()
            for line in response.iter_lines(decode_unicode=True):
                if not line:
                    continue
                if first_token_ts is None:
                    first_token_ts = time.perf_counter()
                data = json.loads(line)
                chunk = data.get("response", "")
                if chunk:
                    chunks.append(chunk)
                if data.get("done"):
                    break
        end_ts = time.perf_counter()
        if timing is not None:
            total_s = end_ts - start_ts
            ttfb_s = (first_token_ts - start_ts) if first_token_ts else total_s
            timing["gpu_total_s"] += total_s
            timing["gpu_ttfb_s"] += ttfb_s
            log_gpu(f"Timing[{label}]: ttfb={ttfb_s:.3f}s total={total_s:.3f}s")
        if timeline_events is not None:
            if first_token_ts is None:
                first_token_ts = end_ts
            timeline_events.append((start_ts, first_token_ts, "gpu_preload"))
            timeline_events.append((first_token_ts, end_ts, "gpu_tokens"))
        return "".join(chunks) or "{}"

    except requests.exceptions.Timeout:
        return "Error: Ollama API request timed out."
    except requests.exceptions.RequestException as e:
        return f"Error calling Ollama API: {e}. Is Ollama running?"
    except (KeyError, IndexError) as e:
        return f"Error parsing Ollama response: {e}."


# --- Part 3: The agentic chain ---

def run_concierge_agent(goal: str, history: list) -> str:
    """Run the main agent logic with conversation history and multi-site browsing."""
    timing = {"cpu_s": 0.0, "gpu_total_s": 0.0, "gpu_ttfb_s": 0.0}
    timeline_events = []

    def time_cpu(label: str, fn, *args, **kwargs):
        start_ts = time.perf_counter()
        result = fn(*args, **kwargs)
        elapsed = time.perf_counter() - start_ts
        timing["cpu_s"] += elapsed
        timeline_events.append((start_ts, start_ts + elapsed, "cpu"))
        log_cpu(f"Timing[{label}]: {elapsed:.3f}s")
        return result

    print(f"\nGoal: {goal}\n")
    formatted_history = "\n".join(history)

    # 1. Decide what to search for
    prompt1 = f"""
You are a helpful concierge agent. Your task is to understand a user's request and
generate a concise, effective search query to find the information they need.

Conversation history:
---
{formatted_history}
---
User's latest request: "{goal}"

Based on the request, what is the best, simple search query for Google?
The query should be 3-5 words.
Respond with ONLY the search query itself.
"""
    search_query = call_gemma_ollama(
        prompt1, output_format="text", timing=timing,
        label="search_query", timeline_events=timeline_events,
    ).strip().replace('"', '')

    # 1.5: CPU expands the base query into multiple variants
    query_variants = time_cpu("generate_search_queries", generate_search_queries, search_query, goal)

    # 2. CPU orchestrates parallel web searches across all query variants
    search_results = time_cpu("parallel_search", parallel_search, query_variants)
    print(search_results)

    # 3. Choose which sites to browse
    search_results_for_url_prompt = search_results[:2500]
    prompt2 = f"""
You are a smart web navigator. Your task is to analyze Google search results and select
the most promising URLs to find the answer to a user's goal. Avoid generic homepages and
prefer specific articles, lists, or maps.

User's goal: "{goal}"

Search Results:
---
{search_results_for_url_prompt}
---

Which are the top 8-10 most promising and specific URLs to browse for details?
Respond with ONLY a list of URLs, one per line.
"""
    browse_urls_str = call_gemma_ollama(
        prompt2, output_format="text", timing=timing,
        label="select_urls", timeline_events=timeline_events,
    ).strip()
    browse_urls = [url.strip() for url in browse_urls_str.split('\n') if url.strip().startswith('http')]

    if not browse_urls:
        log_cpu("No URLs selected; summarizing from search snippets.")
        prompt_summarize_snippets = f"""
You are a helpful concierge agent. The web browser is not working, but you have search snippets.
User's goal: "{goal}"
Search Results:
---
{search_results}
---
Provide a summary based only on the search result snippets.
"""
        final_summary = call_gemma_ollama(
            prompt_summarize_snippets, output_format="text", timing=timing,
            label="summarize_snippets", timeline_events=timeline_events,
        )
        print("\n--- Here is your summary ---\n")
        print(final_summary)
        print("\n--------------------------\n")
        return final_summary

    # 4. CPU orchestrates parallel browsing of all selected URLs
    scraped_pairs = time_cpu("parallel_browse", parallel_browse, browse_urls)

    # 4.5: CPU ranks pages by TF-IDF relevance to the user's goal
    ranked_results = time_cpu("rank_and_filter_content", rank_and_filter_content, scraped_pairs, goal)

    if not ranked_results:
        log_cpu("All browsed pages failed - falling back to search snippets.")
        prompt_fallback = f"""
You are a helpful concierge agent. The websites could not be browsed, but you have snippets.
User's goal: "{goal}"
Search Results:
---
{search_results}
---
Provide the best answer you can based only on the search result snippets above.
"""
        final_summary = call_gemma_ollama(
            prompt_fallback, output_format="text", timing=timing,
            label="fallback_summary", timeline_events=timeline_events,
        )
        print("\n--- Here is your summary (from search snippets) ---\n")
        print(final_summary)
        print("\n--------------------------\n")
        return final_summary

    # 4.6: CPU deduplicates near-identical sentences across all sources
    all_texts = [text for _, text, _ in ranked_results]
    deduped_text = time_cpu("deduplicate_sentences", deduplicate_sentences, all_texts)

    # 4.7: CPU extracts structured entities (phones, hours, prices, URLs)
    entities = time_cpu("extract_entities", extract_entities, deduped_text)
    entity_summary = time_cpu("format_entity_summary", format_entity_summary, entities)

    # 4.8: CPU generates shingle fingerprints and detects near-duplicate pages
    fingerprints = time_cpu("compute_content_fingerprints", compute_content_fingerprints, all_texts)
    time_cpu("find_near_duplicates", find_near_duplicates, fingerprints)

    # 4.9: CPU builds an inverted keyword index for efficient term retrieval
    keyword_index = time_cpu("build_keyword_index", build_keyword_index, all_texts)
    log_cpu(f"Full orchestration pipeline complete - {len(keyword_index)} terms indexed")

    # Combine deduplicated content with CPU-extracted entities for the model
    aggregated_text = deduped_text[:2000]
    if entity_summary:
        aggregated_text = (
            f"[CPU-Extracted Entities]\n{entity_summary}\n\n"
            f"[Aggregated Web Content]\n{aggregated_text}"
        )

    # 5. Summarize everything for the user
    prompt3 = f"""
You are a meticulous and trustworthy concierge agent. Provide a clear, concise, and accurate
answer to the user's request by synthesizing information from multiple sources.

User's latest request: "{goal}"

You have gathered the following text from one or more websites:
---
{aggregated_text}
---

Before including any business or item, verify that it meets ALL the specific criteria from the
user's request. If you cannot find explicit confirmation, do not include it. Format your response
clearly. If listing places, use bullet points.
"""
    final_summary = call_gemma_ollama(
        prompt3, output_format="text", timing=timing,
        label="final_summary", timeline_events=timeline_events,
    )

    print("\n--- Here is your summary ---\n")
    print(final_summary)
    print("\n--------------------------\n")

    gpu_token_s = max(0.0, timing["gpu_total_s"] - timing["gpu_ttfb_s"])
    print("\n--- Processing Timeline ---")
    print(f"CPU operations:             {timing['cpu_s']:.3f}s")
    print(f"GPU input token processing: {timing['gpu_ttfb_s']:.3f}s")
    print(f"GPU token generation:       {gpu_token_s:.3f}s")
    print(f"GPU total:                  {timing['gpu_total_s']:.3f}s")
    print(render_timeline(timeline_events))
    print("---------------------------\n")

    return final_summary


# --- Part 4: The terminal interface ---

def main():
    """Run the terminal application loop."""
    if not SERPER_API_KEY:
        print("FATAL ERROR: SERPER_API_KEY environment variable not set.")
        print("Get a free key from https://serper.dev and export the variable.")
        return

    print("Hello! I am your local concierge agent.")
    print("Ask me anything - I research topics by browsing multiple websites in real time.")
    print("Make sure Ollama is running in the background.")
    print('Type "quit" or "exit" to end the session.')

    conversation_history = []

    while True:
        user_goal = input("\nWhat would you like to find?\n> ")
        if user_goal.lower() in ["quit", "exit"]:
            print("Goodbye!")
            break
        run_concierge_agent(user_goal, conversation_history)


if __name__ == "__main__":
    main()
