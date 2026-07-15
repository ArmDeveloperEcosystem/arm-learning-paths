---
title: Review the Arm Continuum deployment and next steps
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Review what stayed the same

You deployed the same OpenClaw release on two Arm-based systems:

| Layer | NVIDIA DGX Spark | Radxa Orion O6 |
|---|---|---|
| OpenClaw runtime | Same Python runtime | Same Python runtime |
| User interface | Telegram | Telegram |
| Skills | Memory, RAG, search, weather, cron | Same skills |
| Vector memory | Qdrant | Qdrant |
| Embeddings | Ollama | Ollama |
| Generation API | OpenAI-compatible | OpenAI-compatible |
| Generation engine | vLLM | llama.cpp |
| Compute shape | Arm CPU + GPU | Arm CPU-only |

The exercise demonstrates software continuity, not identical performance. Each platform can use model and context settings appropriate to its available compute while preserving the same application-level contract.

## Review the local-first result

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

## Understand the v1.2 boundaries

This Learning Path intentionally uses the stable text-first v1.2 architecture.

It does not implement:

- Dynamic routing between multiple local LLMs
- Rich multi-agent collaboration
- A production VLM for images, diagrams, or video
- Per-household-member data authorization
- Automatic safety decisions from camera footage
- Hardware performance comparisons

The thin AgentRegistry and TaskDispatcher route explicit skills and preserve predictable command behavior. A later release can evolve these contracts without changing the LP1 user workflow.

## Extend the household assistant with local visual events

A future multimodal specialist can extend the household scenario:

```text
Camera event
      |
      v
Local frame extraction
      |
      v
MultimodalAnalysisAgent
      |
      v
Local event description
      |
      +-- event memory
      `-- Telegram notification
```

The first implementation should analyze a small number of representative frames rather than process every video frame. Original footage can remain local while OpenClaw sends only a concise event description when notification is required.

This is further work and is not enabled by the text-first model used in LP1.

## Apply the architecture to other Arm deployments

The same endpoint-driven design can support additional deployment shapes:

- An always-on CPU-only Arm server with a compact local model
- An Arm edge gateway connected to a trusted private-LAN inference server
- A heterogeneous Arm AI workstation hosting larger local models

Each deployment changes the compute and trust boundary. It should not silently change where personal data is stored or which external services are contacted.

## What you've learned

You can now:

- Explain the local and external data boundaries of OpenClaw
- Deploy an operational OpenClaw runtime with local vLLM inference on DGX Spark
- Use Telegram memory, RAG, browser search, cron, and Gateway workflows
- Verify local persistence through Qdrant and runtime logs
- Move the same application workflow to llama.cpp on a CPU-only Armv9 platform
- Identify where model routing and multimodal agents can extend the architecture

You have moved beyond a local-model demo and built a self-managed OpenClaw runtime that can adapt to two different Arm compute configurations.
