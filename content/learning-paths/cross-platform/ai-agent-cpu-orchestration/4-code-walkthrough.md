---
title: Understand the concierge agent code
description: Review the concierge agent code to see where web search, page scraping, Ollama model calls, and CPU orchestration happen in the workflow.
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## How the code is organized

The `concierge_agent.py` script you downloaded earlier is organized into four parts. You'll understand what runs on the CPU, what runs on the GPU, and how the agent chains them together.

| Part | Responsibility | Runs on |
|---|---|---|
| Tools | Web search, page scraping, optional email | CPU |
| The brain | Calls the local Gemma model through Ollama | GPU |
| Orchestration pipeline | Query expansion, parallelism, ranking, deduplication, extraction | CPU |
| The agentic chain | Ties everything together into one query workflow | CPU + GPU |

### The tools

The tools are the agent's connection to the outside world. `search_web()` calls the Serper API and returns the top five results. `browse_website()` downloads a page and strips it down to clean text. Both run entirely on the CPU and both log their activity with `log_cpu()`:

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

### The brain

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

Two details are worth noting:

- `keep_alive: -1` tells Ollama to keep the model resident in memory between calls. The agent calls the model several times per query, so this avoids reloading the weights each time.
- The function records timing as it streams. The time until the *first* token arrives is the model's input-token processing (prefill); the time spent streaming the rest is token generation. Separating these two values is what lets the agent show you the GPU breakdown later.

Because every model call goes through this one function, the agent only ever uses the GPU in clearly marked places.

### The CPU orchestration pipeline

Between the model calls, the CPU prepares the context. Each of the following stages runs entirely on the CPU:

| Stage | Function | What it does |
|---|---|---|
| Expand queries | `generate_search_queries()` | Turns one query into several variants |
| Search in parallel | `parallel_search()` | Runs all searches concurrently |
| Browse in parallel | `parallel_browse()` | Fetches up to ten websites at once |
| Rank by relevance | `rank_and_filter_content()` | Scores pages with TF-IDF |
| Deduplicate | `deduplicate_sentences()`, `find_near_duplicates()` | Removes repeated sentences and near-duplicate pages |
| Extract data | `extract_entities()` | Pulls out phone numbers, hours, and prices |
| Build index | `build_keyword_index()` | Indexes the most frequent terms |

### The agentic chain

`run_concierge_agent()` ties the pipeline together. When you read the function from top to bottom, you can see how CPU and GPU steps alternate:

1. GPU – `call_gemma_ollama()` turns your question into a search query.
2. CPU – `generate_search_queries()` and `parallel_search()` expand and run the searches.
3. GPU – the model selects which URLs to open.
4. CPU – `parallel_browse()`, `rank_and_filter_content()`, `deduplicate_sentences()`, `extract_entities()`, and the indexing stages prepare the context.
5. GPU – the model writes the final, fact-checked summary.

## What you've learned and what's next

You've now learned about the structure of the agent code and what functions work on the CPU and the GPU respectively. 

Next, you'll run the agent and watch the CPU and GPU work in real time.
