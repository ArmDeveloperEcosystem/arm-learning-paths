---
title: Review the Deployment Across Arm Platforms
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Compare Arm Deployment Architectures

You built a local-first household assistant with memory, document RAG, browser search, and scheduled notifications. You ran it with vLLM on NVIDIA DGX Spark, then moved it to llama.cpp on Radxa Orion O6.

The following comparison shows what stayed the same across the two Arm-based implementations and what changed with the local generation backend:

| Layer | NVIDIA DGX Spark | Radxa Orion O6 |
|---|---|---|
| Reference runtime services | Same services | Same services |
| User interface | Telegram | Telegram |
| Skills | Memory, RAG, search, weather, cron | Same skills |
| Vector memory | Qdrant | Qdrant |
| Embeddings | Ollama | Ollama |
| Generation API | OpenAI-compatible | OpenAI-compatible |
| Generation engine | vLLM | llama.cpp |
| Inference compute | Arm CPU + NVIDIA GPU | Arm CPU |

Each platform uses model and context settings suited to its compute while preserving the same application contract.

## Review Data Privacy Boundaries

The runtime keeps inference requests, generated context, Qdrant collections, uploaded files, cron history, OpenClaw tasks, and Gateway state under your control.

Telegram still transports messages and uploads. Weather and browser searches contact public services, while setup downloads models and containers from external registries.

For sensitive deployments, you should review network exposure, Telegram suitability, host access, backups, model provenance, and the contents of every enabled tool.

## Identify Current System Scope

This Learning Path uses a text-first architecture, fixed skill routes, and one local LLM endpoint. It does not cover multi-model routing, multi-agent handoffs, or hardware benchmarking. The AgentRegistry and TaskDispatcher keep command behavior predictable within this scope.

## Explore Other Arm Deployment Topologies

The same endpoint-driven design can support additional deployment shapes:

- An always-on CPU-only Arm server with a compact local model
- An Arm edge gateway connected to a trusted private-LAN inference server
- A heterogeneous Arm AI workstation hosting larger local models

Each deployment changes the compute and trust boundary. It should not silently change where personal data is stored or which external services are contacted.

## Key Takeaways and Next Steps

You can now:

- Explain the local and external data boundaries of the reference runtime
- Deploy an operational OpenClaw-based runtime with local vLLM inference on DGX Spark
- Use Telegram memory, RAG, browser search, cron, and Gateway workflows
- Verify local persistence through Qdrant and runtime logs
- Move the same application workflow to llama.cpp on a CPU-only Armv9 platform

You have moved beyond a local-model demo and built a self-managed OpenClaw-based runtime that can adapt to two different Arm compute configurations.
