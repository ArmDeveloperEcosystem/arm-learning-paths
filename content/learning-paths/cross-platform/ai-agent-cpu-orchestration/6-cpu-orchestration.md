---
title: Understand the CPU's role in the agentic workflow
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## How the CPU and GPU share the work

When people picture an AI agent, they usually picture an AI model generating text using just the GPU. In practice, the model is only one stage of an agentic workflow. 

The CPU and GPU work in tandem, each handling the part of the workload it does best: the GPU runs the model's reasoning, while the CPU does the broad, continuous work of orchestration that turns a single request into a useful answer.

## What the CPU does in an agentic workflow

Most agentic systems share the same shape, regardless of the task. Between model calls, the CPU is responsible for the work that surrounds inference:

- Orchestration – deciding what to do next, scheduling tasks, coordinating tools and services, and routing work between multiple AI agents and subagents.
- Tool calls and I/O – calling APIs, querying databases, reading files, and fetching web pages, often many at once.
- Data preparation – cleaning, filtering, ranking, deduplicating, and structuring raw data before it reaches the model.
- Memory and state – tracking conversation history, caching results, and managing context across steps.

These stages are mostly classical computing: concurrency, networking, parsing, and text processing. They run continuously throughout a query, while the GPU is used in focused bursts only when the model reasons. As agents call more tools and handle more data, this CPU-side work grows.

## Why this is a good fit for Arm

This kind of broad, concurrent orchestration and I/O is exactly the workload Arm CPUs handle efficiently. The same pattern scales across Arm platforms:

- On an Apple Silicon MacBook or an Arm Linux laptop, the Arm CPU runs orchestration and I/O while the integrated GPU accelerates the model, so the whole agent runs on one device with no cloud dependency.
- On an NVIDIA DGX Spark, the Arm Grace CPU coordinates the agentic workflow while the Blackwell GPU runs inference, mirroring how larger AI systems are built: CPUs orchestrate, GPUs accelerate.

The key takeaway is that an agent is an *orchestration system*, not just an inference system. The model is one important stage, but the CPU is what turns a single request into tool calls, data, and structured context, and that orchestration is a large part of the work.

## Update agent code to visualize the role of the CPU 

To see the effect of the CPU pipeline for yourself, try these changes and compare the timelines:

- Increase the number of query variants in `generate_search_queries()` and watch CPU search time grow.
- Reduce `max_workers` in `parallel_browse()` to `1` to disable parallel browsing, and see how much longer the CPU I/O stretch becomes.
- Switch to a larger model with `OLLAMA_MODEL=gemma3:27b` and compare how the GPU share changes relative to the CPU share.

Each experiment shifts the balance between CPU and GPU work and makes the orchestration pattern easier to see.

## What you've accomplished

You've now understood the CPU's orchestration role and why Arm platforms suit agentic workloads. 

You can use the workflows in the Learning Path to create your own AI agents on Arm. 
