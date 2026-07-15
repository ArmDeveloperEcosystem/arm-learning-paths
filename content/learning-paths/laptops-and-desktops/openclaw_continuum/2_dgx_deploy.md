---
title: Deploy the OpenClaw demo runtime on NVIDIA DGX Spark
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Check the host services

This section assumes Docker Engine, the Docker Compose plugin, the NVIDIA driver, and NVIDIA Container Toolkit are installed on DGX Spark.

Confirm that the Arm CPU and NVIDIA GPU are visible:

```bash
uname -m
nvidia-smi
```

The expected CPU architecture is:

```output
aarch64
```

Confirm Docker GPU access:

```bash
docker run --rm --gpus all ubuntu nvidia-smi
```

OpenClaw uses host Ollama for embeddings and host Qdrant for vector storage. Confirm that both endpoints respond:

```bash
curl http://127.0.0.1:11434/api/tags
curl http://127.0.0.1:6333/collections
```

Pull the embedding model if it is not already available:

```bash
ollama pull nomic-embed-text
```

## Clone the fixed tutorial version

Clone the repository and check out the release used by this Learning Path:

```bash
git clone https://github.com/odincodeshen/openclaw-arm-continuum.git
cd openclaw-arm-continuum
git checkout v1.2
```

Using a fixed release tag makes the tutorial reproducible even when development continues on `main`.

## Create a private environment file

Copy the DGX Spark environment template:

```bash
cp .env.example .env
```

Generate a Gateway token:

```bash
openssl rand -hex 32
```

Edit `.env` and set the four private values:

```text
OPENCLAW_TELEGRAM_BOT_TOKEN=<demo-bot-token>
OPENCLAW_TELEGRAM_ALLOWED_CHAT_IDS=<demo-chat-id>
OPENCLAW_CRON_CHAT_IDS=<demo-chat-id>
OPENCLAW_GATEWAY_TOKEN=<generated-random-token>
```

Use a dedicated tutorial bot when possible. Only allowlisted chat IDs can send commands to this runtime.

Change the collection names so that the tutorial does not use personal collections:

```text
OPENCLAW_TRACKER_COLLECTION=demo_tracker_memory
OPENCLAW_KNOWLEDGE_COLLECTION=demo_knowledge_base
OPENCLAW_RUNTIME_LABEL=DGX Spark Demo
```

The v1.2 DGX model is text-first. Disable experimental vision routing for this Learning Path:

```text
OPENCLAW_VISION_ENABLED=false
```

{{% notice Warning %}}
Never commit `.env`. It contains the Telegram bot token and Gateway authentication token. The repository ignores this file, but you should still verify `git status` before publishing changes.
{{% /notice %}}

## Start the runtime

Start the complete DGX Spark stack:

```bash
docker compose --env-file .env -f compose.yaml up -d
```

The first start can take time while Docker images and model weights are downloaded and vLLM initializes the model.

Inspect service state:

```bash
docker compose --env-file .env -f compose.yaml ps
docker logs --tail 80 openclaw-vllm
docker logs --tail 80 openclaw-telegram
docker logs --tail 80 openclaw-cron
```

Confirm the local model endpoint:

```bash
curl http://127.0.0.1:8000/v1/models
```

Confirm the local Gateway dashboard endpoint:

```bash
curl -I http://127.0.0.1:18789/
```

## Run the first Telegram test

Open the demo bot in Telegram and send:

```text
/help
```

The bot should return the OpenClaw command card. Next, send a short general message:

```text
Reply with one sentence confirming that this response uses the local runtime.
```

Watch the Telegram and vLLM logs while the request is processed:

```bash
docker logs --tail 40 openclaw-telegram
docker logs --tail 40 openclaw-vllm
```

The request appearing in the local logs confirms the runtime path. The model's text alone is not evidence that inference was local.

## Run the automated checks

Run the repository tests from the host:

```bash
PYTHONPATH=app python3 -m unittest discover -s tests
```

These tests validate command routing, task dispatch, cron parsing, ingestion helpers, and failure handling. They are software behavior tests, not hardware benchmarks.

## What you've learned and what's next

You have deployed the v1.2 OpenClaw runtime on NVIDIA DGX Spark, connected it to a demo Telegram bot, verified the local vLLM endpoint, and checked the runtime tests.

Next, you will use the deployment as a local-first household assistant and confirm that memory is stored in local Qdrant collections.
