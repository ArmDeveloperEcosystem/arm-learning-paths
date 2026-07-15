---
title: Explore the OpenClaw Runtime and local-first data boundaries
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## From local inference to an operational assistant

Running a local LLM gives you a private way to generate text, but it does not yet give you an assistant you can use throughout the day. You still need a convenient way to ask questions, save information, search your documents, retrieve current information, and receive reminders without returning to a terminal each time.

In this Learning Path, you will deploy [OpenClaw Arm Continuum](https://github.com/odincodeshen/openclaw-arm-continuum) and interact with it from Telegram. This learning path uses a private household AI assistant as an example: you will save a household note, retrieve it later, ask questions about a local document, run an explicit web search, and schedule a proactive notification. The inference, embeddings, documents, vector memory, and task state remain on hardware you control. You can apply the same project architecture to other use cases that require private, locally controlled AI processing.

OpenClaw brings the interaction channel, local AI services, persistent memory, tools, and scheduled tasks together in one assistant runtime. It provides:

- **Mobile access through Telegram** for conversations, document uploads, and notifications
- **Local generation through vLLM or llama.cpp**, allowing the inference backend to match the Arm system
- **Persistent local memory and document retrieval** through Ollama embeddings and Qdrant
- **Tool-driven and proactive workflows** through explicit web search, scheduled tasks, and Telegram notifications

OpenClaw routes each request to the appropriate local model, data source, or tool while keeping persistent AI data under your control.

{{% notice Note %}}
**OpenClaw is the orchestration layer.** vLLM or llama.cpp provides local generation, while Ollama, Qdrant, browser search, and cron services extend the assistant with memory, tools, and proactive workflows.
{{% /notice %}}

## Understand the data boundary

Local-first does not mean that every byte stays offline. Telegram and web search are external network interactions. The important property is that the boundary is explicit and that the core AI data remains under your control.

| Data or operation | Location | External interaction |
|---|---|---|
| LLM inference | DGX Spark or CPU-only Arm host | Model weights are downloaded during setup |
| Embeddings | Local Ollama service | Model weights are downloaded during setup |
| Vector memory and RAG | Local Qdrant service | None during normal retrieval |
| Uploaded documents | Local OpenClaw workspace | Telegram transports the original upload |
| Cron state and task history | Local workspace and Gateway state | Telegram transports push messages |
| External data lookup | Local skill | Public data service selected by the skill |
| Browser search | Local Playwright worker | Search engine and selected public pages |

The runtime does not require a public cloud LLM API. However, content sent through Telegram is transported by Telegram, and explicit browser searches reveal the search request to external websites.

{{% notice Note %}}
Use synthetic or public data while following this Learning Path. The tutorial uses a demo bot and demo Qdrant collections so that you can reset and repeat the workflow without exposing personal household information.
{{% /notice %}}

## Follow the request path

In this Learning Path, Telegram requests follow this path:

```text
Telegram message
    -> OpenClaw Telegram gateway
    -> AgentRegistry and TaskDispatcher
        |-- Memory or RAG -> Ollama and Qdrant
        |-- Web search    -> Playwright browser worker
        |-- External data -> Purpose-built local skill
        `-- General chat  -> Local LLM endpoint
```

The reference runtime can also start a configured workflow automatically, without requiring a new Telegram message from the user:

```text
Cron schedule
    -> OpenClaw cron worker
    -> Local skill and local LLM
    -> Telegram push notification
```

Explicit slash commands remain deterministic. For example, `/search` always selects the browser-search workflow, while a plain-language weather question selects the weather skill. The local model is not allowed to reinterpret an explicit command and silently change its route.

## Use one API contract across Arm platforms

To demonstrate that the same project can run across systems with different hardware capabilities, this Learning Path uses an inference engine suited to each platform:

| Platform | Inference engine |
|---|---|
| NVIDIA DGX Spark | vLLM server |
| Radxa Orion O6 | llama.cpp server |

Both expose an OpenAI-compatible chat-completions API. The project therefore keeps the same upper-layer workflow on both platforms; only the configured endpoint and model name change.

This demonstrates the portability of the project architecture: the same local-first workflow can run across different Arm compute configurations by selecting a compatible inference backend.

## What you've learned and what's next

You now understand why a local-first assistant is more than a local model, which data remains local, which operations cross the network boundary, and how an OpenAI-compatible endpoint separates OpenClaw from the underlying inference engine.

Next, you will deploy the baseline runtime on NVIDIA DGX Spark.
