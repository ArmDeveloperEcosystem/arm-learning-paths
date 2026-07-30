---
title: Review the Deployment Across Arm Platforms
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Compare Arm Deployment Architectures

In this Learning Path, you built a local-first household assistant and used Telegram to validate persistent memory, document RAG, browser search, and scheduled notifications. You first ran these workflows with local vLLM inference on NVIDIA DGX Spark, then moved the same application experience to llama.cpp on the Armv9 CPU of a Radxa Orion O6.

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

The exercise demonstrates software portability across different compute configurations. Each platform can use model and context settings appropriate to its available compute while preserving the same application-level contract.

## Review Data Privacy Boundaries

The runtime keeps the following state under your control:

- Model inference requests and generated context
- Qdrant memory and RAG collections
- Uploaded document files
- Cron definitions and run history
- OpenClaw task history
- Gateway state

External boundaries remain visible:

- Telegram transports messages and uploaded files.
- Weather and browser-search tasks contact public network services.
- Model and container downloads contact external registries during setup.

For sensitive deployments, you should review network exposure, Telegram suitability, host access, backups, model provenance, and the contents of every enabled tool.

## Identify Current System Scope

This Learning Path uses a text-first architecture with deterministic skill routing and one configured local LLM endpoint.

It does not implement:

- Dynamic routing across multiple local LLMs
- Multi-agent collaboration or autonomous agent handoffs
- Hardware performance benchmarking

The thin AgentRegistry and TaskDispatcher route explicit skills and preserve predictable command behavior within this scope.

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
