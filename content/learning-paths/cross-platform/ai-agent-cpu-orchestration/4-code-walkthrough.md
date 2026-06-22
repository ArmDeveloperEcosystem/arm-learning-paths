---
title: Walk through the agent code
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## How the code is organized

The `concierge_agent.py` script you downloaded earlier is organized into four parts. This section walks through the important pieces so you understand what runs on the CPU, what runs on the GPU, and how the agent chains them together.

| Part | Responsibility | Runs on |
|---|---|---|
| Part 1: Tools | Web search, page scraping, optional email | CPU |
| Part 1.5: Orchestration pipeline | Query expansion, parallelism, ranking, deduplication, extraction | CPU |
| Part 2: The brain | Calls the local Gemma model through Ollama | GPU |
| Part 3: The agentic chain | Ties everything together into one query workflow | CPU + GPU |

## Part 1: The tools

The tools are the agent's connection to the outside world. `search_web()` calls the Serper API and returns the top five results; `browse_website()` downloads a page and strips it down to clean text. Both run entirely on the CPU and both log their activity with `log_cpu()`:

```python
def search_web(query: str) -> str:
    """Use the Serper.dev API to perform a web search."""
    log_cpu(f"Searching web: '{query}'")
    ...

def browse_website(url: str) -> str:
    """Scrape and clean the text content of a given URL."""
    log_cpu(f"Browsing website: '{url}'")
    ...
    return text[:8000]
```

`browse_website()` uses BeautifulSoup to remove `<script>` and `<style>` tags, collapse whitespace, and cap the result at 8,000 characters so a single large page can't dominate the pipeline.

## Part 2: The brain

A single function, `call_gemma_ollama()`, is the only place the model is used. It sends a prompt to the local Ollama API and streams the response back token by token:

```python
def call_gemma_ollama(prompt, output_format="json", timing=None,
                      label="ollama", timeline_events=None):
    log_gpu("Thinking with local Gemma model...")
    payload = {
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "stream": True,
        "keep_alive": -1,  # Keep model weights in GPU memory
    }
    ...
```

Two details are worth highlighting:

- `keep_alive: -1` tells Ollama to keep the model resident in memory between calls. The agent calls the model several times per query, so this avoids reloading the weights each time.
- The function records timing as it streams. The time until the *first* token arrives is the model's input-token processing (prefill); the time spent streaming the rest is token generation. Separating these two values is what lets the agent show you the GPU breakdown later.

Because every model call goes through this one function, the agent only ever uses the GPU in clearly marked places. Everything else is CPU work.

## Part 1.5: The CPU orchestration pipeline

This is the heart of the Learning Path. Between the model calls, the CPU transforms a single user request into rich, structured context. Each function below is a distinct CPU stage.

### Expand one query into several

A single search query rarely covers a topic well, so the CPU expands it into variants before searching:

```python
def generate_search_queries(base_query: str, goal: str) -> list:
    variants = [base_query, f"best {base_query}", f"{base_query} 2026"]
    ...
```

### Search and browse in parallel

Network requests are slow, so the CPU runs them concurrently with a thread pool instead of one at a time. The same pattern is used for searching and for browsing:

```python
def parallel_browse(urls: list) -> list:
    log_cpu(f"Dispatching {len(urls)} parallel browse threads...")
    with concurrent.futures.ThreadPoolExecutor(max_workers=min(len(urls), 10)) as executor:
        future_to_url = {executor.submit(browse_website, url): url for url in urls}
        ...
```

This is a good example of orchestration: the CPU coordinates up to ten simultaneous downloads, then collects the results as each thread finishes.

### Rank pages by relevance

Not every page the agent opens is useful. The CPU scores each page against the user's goal using TF-IDF (term frequency–inverse document frequency) and sorts them so the most relevant content reaches the model first:

```python
def rank_and_filter_content(scraped_pairs: list, goal: str) -> list:
    log_cpu("Running TF-IDF ranking on scraped content...")
    ...
    ranked.sort(key=lambda x: x[2], reverse=True)
    return ranked
```

### Deduplicate and extract structured data

Web pages repeat each other and bury the useful facts in boilerplate. Several CPU stages clean this up:

- `deduplicate_sentences()` removes near-duplicate sentences across sources using sequence matching.
- `compute_content_fingerprints()` and `find_near_duplicates()` use 5-word shingles and Jaccard similarity to detect near-duplicate pages.
- `extract_entities()` pulls structured data, such as phone numbers, opening hours, and prices, out of the text with regular expressions.
- `build_keyword_index()` builds an inverted index of the most frequent terms.

The extracted entities are handed to the model as a clearly labeled block, so the model starts from facts the CPU already verified:

```python
aggregated_text = (
    f"[CPU-Extracted Entities]\n{entity_summary}\n\n"
    f"[Aggregated Web Content]\n{aggregated_text}"
)
```

## Part 3: The agentic chain

`run_concierge_agent()` ties the pipeline together. Reading it top to bottom shows how CPU and GPU steps alternate:

1. **GPU** – `call_gemma_ollama()` turns your question into a search query.
2. **CPU** – `generate_search_queries()` and `parallel_search()` expand and run the searches.
3. **GPU** – the model selects which URLs to open.
4. **CPU** – `parallel_browse()`, `rank_and_filter_content()`, `deduplicate_sentences()`, `extract_entities()`, and the indexing stages prepare the context.
5. **GPU** – the model writes the final, fact-checked summary.

A small helper, `time_cpu()`, wraps each CPU stage to measure how long it takes and record it on the timeline:

```python
def time_cpu(label: str, fn, *args, **kwargs):
    start_ts = time.perf_counter()
    result = fn(*args, **kwargs)
    elapsed = time.perf_counter() - start_ts
    timing["cpu_s"] += elapsed
    timeline_events.append((start_ts, start_ts + elapsed, "cpu"))
    log_cpu(f"Timing[{label}]: {elapsed:.3f}s")
    return result
```

The matching GPU timing is captured inside `call_gemma_ollama()`. Together they produce the timeline and the timing breakdown you'll see when you run the agent in the next section.

{{% notice Note %}}
The script also contains an `send_email()` tool and commented-out email steps. They're disabled by default so the workflow stays focused on research. You can re-enable them later by configuring the `SMTP_*` environment variables and uncommenting the email steps.
{{% /notice %}}

Now that you understand the structure, you'll run the agent and watch the CPU and GPU work in real time.
