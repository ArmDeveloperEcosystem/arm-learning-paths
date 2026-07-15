---
title: Explore the OpenClaw Runtime and local-first data boundaries
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## From local inference to an operational assistant

Running a local LLM gives you a private way to generate text, but it does not yet give you an assistant you can use throughout the day. You still need a convenient way to ask questions, save information, search your documents, retrieve current information, and receive reminders without returning to a terminal each time.

In this Learning Path, you will deploy [OpenClaw Arm Continuum](https://github.com/odincodeshen/openclaw-arm-continuum) and interact with it from Telegram. This learning path uses a private household AI assistant as an example: you will save a household note, retrieve it later, ask questions about a local document, run an explicit web search, and schedule a proactive notification. The inference, embeddings, documents, vector memory, and task state remain on hardware you control. You can apply the same project architecture to other use cases that require private, locally controlled AI processing.

OpenClaw turns these separate capabilities into one assistant experience. It decides when to call the local model, when to retrieve local context, and when a request should be handled by a specific tool. Behind that experience, the runtime combines:

- **Telegram as the mobile interaction channel**
- **vLLM or llama.cpp as the local generation backend**
- **Ollama as the local embedding service**
- **Qdrant as persistent vector memory**
- **A Playwright browser worker for explicit web searches**
- **A cron worker for proactive Telegram notifications**
- **OpenClaw Gateway for dashboard and cron management**
- **A thin AgentRegistry and TaskDispatcher for deterministic skill routing**

{{% notice Note %}}
The key outcome is not simply a local model that answers prompts. You will build an operational assistant whose interaction channel, tools, persistent data, and inference backend work together while their data boundaries remain visible.
{{% /notice %}}

## Understand the data boundary

Local-first does not mean that every byte stays offline. Telegram and web search are external network interactions. The important property is that the boundary is explicit and that the core AI data remains under your control.

| Data or operation | Location | External interaction |
|---|---|---|
| LLM inference | DGX Spark or CPU-only Arm host | Model downloads during setup |
| Embeddings | Local Ollama service | Model download during setup |
| Vector memory and RAG | Local Qdrant service | None during normal retrieval |
| Uploaded documents | Local OpenClaw workspace | Telegram transports the original upload |
| Cron state and task history | Local workspace and Gateway state | Telegram transports push messages |
| Weather lookup | Local skill | Public weather service |
| Browser search | Local Playwright worker | Search engine and selected public pages |

The runtime does not require a public cloud LLM API. However, content sent through Telegram is transported by Telegram, and explicit browser searches reveal the search request to external websites.

{{% notice Note %}}
Use synthetic or public data while following this Learning Path. The tutorial uses a demo bot and demo Qdrant collections so that you can reset and repeat the workflow without exposing personal household information.
{{% /notice %}}

## Follow the request path

A normal Telegram request follows this path:

```text
Telegram message
      |
      v
OpenClaw Telegram gateway
      |
      v
AgentRegistry / TaskDispatcher
      |
      +-- memory or RAG -> Ollama + Qdrant
      +-- web search    -> Playwright scraper
      +-- weather       -> weather service
      `-- general chat  -> local LLM endpoint
```

Scheduled tasks use the same skills without waiting for a new message:

```text
Cron schedule
      |
      v
OpenClaw cron worker
      |
      v
Local skill and local LLM
      |
      v
Telegram push notification
```

Explicit slash commands remain deterministic. For example, `/search` always selects the browser-search workflow, while a plain-language weather question selects the weather skill. The local model is not allowed to reinterpret an explicit command and silently change its route.

## Use one API contract across Arm platforms

The two platforms in this Learning Path use different inference engines:

```text
NVIDIA DGX Spark -> vLLM server
Radxa Orion O6  -> llama.cpp server
```

Both expose an OpenAI-compatible chat-completions API. OpenClaw therefore uses the same upper-layer code and changes only the configured endpoint and model name.

```text
OpenClaw runtime
      |
      v
OpenAI-compatible endpoint
      |
      +-- vLLM on DGX Spark
      `-- llama.cpp on an Armv9 CPU-only system
```

This is the practical meaning of the Arm compute continuum in this Learning Path. It is not a hardware performance comparison. It is a software portability exercise across two different local compute configurations.

## What you've learned and what's next

You now understand why a local-first assistant is more than a local model, which data remains local, which operations cross the network boundary, and how an OpenAI-compatible endpoint separates OpenClaw from the underlying inference engine.

Next, you will deploy the baseline runtime on NVIDIA DGX Spark.
