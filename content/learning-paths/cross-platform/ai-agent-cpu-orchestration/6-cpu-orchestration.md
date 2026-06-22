---
title: Understand the CPU's role in the agentic workflow
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## The CPU does most of the work

When people picture an AI agent, they usually picture the model generating text. The timeline from the previous section tells a different story: for a typical research query, the CPU is active far longer than the GPU. The model is fast and focused; the CPU does the broad, continuous work of turning one question into a useful answer.

This section steps back from the code to explain *why* that happens and why it matters on Arm platforms.

## Where the CPU time goes

Every stage between the model calls runs on the CPU. Grouped by purpose, the CPU is responsible for:

| Category | What the CPU does | Functions involved |
|---|---|---|
| Orchestration | Expands one query into variants, schedules parallel tasks, coordinates the workflow | `generate_search_queries`, `parallel_search`, `parallel_browse` |
| Web I/O | Calls the search API, downloads pages, parses HTML into clean text | `search_web`, `browse_website` |
| Relevance | Scores and sorts pages so the best content reaches the model | `compute_tfidf_score`, `rank_and_filter_content` |
| Cleanup | Removes duplicate sentences and near-duplicate pages | `deduplicate_sentences`, `compute_content_fingerprints`, `find_near_duplicates` |
| Structuring | Extracts entities and builds a keyword index | `extract_entities`, `build_keyword_index` |

Only after all of this does the model receive a compact, deduplicated, fact-rich prompt. The quality of the final answer depends heavily on this preparation.

## Why this matters: garbage in, garbage out

A model can only reason about the context it's given. If the agent fed every raw page directly to the model, three problems would follow:

- **Cost and latency** – long, repetitive prompts take much longer for the model to read (the input-token processing time you saw in the breakdown).
- **Lower quality** – boilerplate and duplicated text crowd out the facts that actually answer the question.
- **Hallucination risk** – without extracted, verified entities, the model is more likely to guess.

The CPU pipeline addresses all three. Parallel I/O keeps latency down, deduplication and ranking keep the prompt focused, and entity extraction gives the model concrete facts to ground its answer.

## Why this is a good fit for Arm

The CPU work in this agent, coordinating parallel tasks, handling network I/O, and running classical text processing, is exactly the kind of broad, concurrent workload that Arm CPUs handle efficiently.

- On an **Apple silicon MacBook** or an **Arm Linux laptop**, the same Arm CPU runs all orchestration and I/O while the integrated GPU accelerates the model. The whole agent runs on one device with no cloud dependency.
- On an **NVIDIA DGX Spark**, the Arm Grace CPU coordinates the agentic workflow while the Blackwell GPU runs inference. The division of labor in this small agent mirrors how larger AI systems are built: CPUs orchestrate, GPUs accelerate.

The key takeaway is that an agent is an *orchestration system*, not just an inference system. The model is one important stage, but the CPU is what turns a single question into searches, reading, ranking, and structured facts, and that orchestration is where most of the work happens.

## Experiment

To see the effect of the CPU pipeline for yourself, try these changes and compare the timelines:

- Increase the number of query variants in `generate_search_queries()` and watch CPU search time grow.
- Reduce `max_workers` in `parallel_browse()` to `1` to disable parallel browsing, and see how much longer the CPU I/O stretch becomes.
- Switch to a larger model with `OLLAMA_MODEL=gemma3:27b` and compare how the GPU share changes relative to the CPU share.

Each experiment shifts the balance between CPU and GPU work and makes the orchestration pattern easier to see.

## What you've accomplished

You've built and run a local AI concierge agent end to end on Arm hardware, and you've seen how the work divides between the CPU and the GPU. Specifically, you've:

- Set up a Python environment and served a Gemma model locally with Ollama
- Run an agentic workflow that searches, browses, ranks, deduplicates, and extracts data before each model call
- Read the timing breakdown and timeline to measure how much of each query runs on the CPU
- Connected the CPU's orchestration role to why Arm platforms suit agentic workloads

The main idea to carry forward is that an AI agent is an orchestration system: the model reasons in short bursts, while the CPU does the broad, continuous work that turns one question into a grounded answer.
