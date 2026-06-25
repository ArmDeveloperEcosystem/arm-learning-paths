---
title: Understand the agent and the CPU/GPU split
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What you'll build

In this Learning Path, you'll build and run a *local concierge agent*: a terminal application that answers research-style questions, such as finding restaurants, comparing products, or summarizing a topic, by searching the web, reading multiple pages, and writing a fact-checked summary.

Everything runs on your own Arm machine. The agent uses an LLM served locally by [Ollama](https://ollama.com/), so your prompts and the pages you browse never leave the device. The same code runs on an Apple silicon MacBook, an Arm Linux laptop, or an NVIDIA DGX Spark.


The agent is interesting not just because it runs locally, but because of *how the work is divided*. A common assumption is that an AI agent is "just the model." In practice, the model is only one stage in a longer pipeline, and most of the surrounding work runs on the CPU.

## The agentic loop

Each time you ask the agent a question, it runs through a chain of steps rather than a single model call:

```text
Your question
    -> Decide what to search for          (GPU: model reasoning)
    -> Expand into several search queries  (CPU: orchestration)
    -> Run web searches in parallel        (CPU: network I/O)
    -> Choose which pages to open          (GPU: model reasoning)
    -> Scrape those pages in parallel       (CPU: network I/O)
    -> Rank, deduplicate, extract data      (CPU: text processing)
    -> Write a fact-checked summary         (GPU: model reasoning)
```

The model is called several times, but between every model call the CPU does a large amount of orchestration: generating query variants, dispatching parallel network requests, merging and deduplicating results, scoring pages for relevance, and extracting structured data.

## Why the CPU matters in an agentic workflow

It's easy to focus only on token generation, because that's the visible "thinking" part. But in an agent, the CPU is responsible for turning a single user request into useful, structured context for the model:

| Stage | Runs on | Example work |
|---|---|---|
| Reasoning and summarization | GPU | Choosing search terms, selecting URLs, writing the final answer |
| Orchestration | CPU | Expanding queries, scheduling parallel tasks, merging results |
| Web I/O | CPU | Calling the search API, downloading and parsing web pages |
| Text processing | CPU | TF-IDF ranking, deduplication, entity extraction, indexing |

This division is a natural fit for Arm platforms. On an Apple silicon MacBook or an Arm Linux machine, the CPU handles all orchestration and I/O while the GPU accelerates the model. On an NVIDIA DGX Spark, the Arm CPU coordinates the workflow while the GPU runs inference. In every case, the model is only as good as the context the CPU prepares for it.

## How the agent shows you the split

The program is instrumented so you can see this division directly. As it runs, it prints:

- <code style="color:#00aaaa"><strong>[CPU]</strong></code> log lines for every orchestration and processing step
- <code style="color:#aaaa00"><strong>[GPU]</strong></code> log lines for every model call
- A timing breakdown of CPU time versus GPU input-token processing and token generation
- A text-based timeline that visualizes when the CPU and GPU are each active

By the end of this Learning Path, you'll be able to look at a single query and see exactly how much of the work happened on the CPU before and after the model produced its answer.

## What's next

In the next section, you'll set up your environment: create a Python virtual environment, install the required packages, and get a Serper API key for web search.
