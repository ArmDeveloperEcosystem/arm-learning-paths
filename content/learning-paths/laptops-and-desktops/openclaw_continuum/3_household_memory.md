---
title: Validate a local-first household assistant with Telegram and Qdrant
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Use a household assistant scenario

You will use a shared household assistant to validate the runtime. The example data is synthetic, but the workflow represents a practical local-first use case: household members can save maintenance information and retrieve it later without sending the memory to a public cloud LLM.

This tutorial treats household data as shared. It does not implement separate access control for each family member.

## Save a household memory

Send this command to the Telegram bot:

```text
/mem #home The boiler should be inspected every October.
```

OpenClaw performs the following operations:

```text
Telegram command
      |
      v
Memory skill
      |
      v
Ollama embedding
      |
      v
demo_tracker_memory in Qdrant
```

Wait for the confirmation, then retrieve the memory:

```text
/rag memory: When should the boiler be inspected?
```

The response should mention October.

## Verify the local collection

Confirm that the demo collection exists:

```bash
curl http://127.0.0.1:6333/collections/demo_tracker_memory
```

Retrieve a small set of stored points:

```bash
curl -sS -X POST \
  http://127.0.0.1:6333/collections/demo_tracker_memory/points/scroll \
  -H 'Content-Type: application/json' \
  -d '{"limit":5,"with_payload":true,"with_vector":false}'
```

Look for the synthetic boiler memory in the payload.

This check is important. It verifies the storage location from the data layer instead of trusting the assistant to describe its own architecture.

## Inspect the active agents and task history

Send:

```text
/agents
```

The response lists the thin agents registered by the v1.2 runtime, including memory, RAG, browser search, weather, and chat routes.

Inspect recent tasks:

```text
/tasks show
```

Task history records which agent handled the request, its status, and runtime duration. The v1.2 dispatcher selects skills and agents; it does not dynamically choose between multiple LLMs. Multi-model routing is intentionally outside the scope of this Learning Path.

## Ask for external weather data

Send a weather question in plain language:

```text
Cambridge weather tomorrow
```

OpenClaw routes the request to the weather skill. Do not add `/search` to this question. An explicit `/search` command selects the general browser worker instead of the dedicated weather route.

This request crosses the local data boundary because the skill contacts a public weather service. The local model API is still not replaced by a cloud LLM API.

## Review the acceptance criteria

This stage is successful when:

1. `/help` returns the command card.
2. `/mem` writes the synthetic household memory.
3. `/rag memory:` retrieves the memory.
4. Qdrant exposes the memory in `demo_tracker_memory`.
5. `/agents` and `/tasks show` report the selected local runtime path.
6. A plain-language weather question returns external weather data through the dedicated skill.

## What you've learned and what's next

You have validated the complete local memory path from Telegram to Ollama embeddings and Qdrant retrieval. You also identified an explicit external-data path through the weather skill.

Next, you will add household documents, browser search, and a proactive cron reminder.
