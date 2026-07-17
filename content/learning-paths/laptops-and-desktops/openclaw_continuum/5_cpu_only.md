---
title: Move the OpenClaw runtime to a CPU-only Armv9 system
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Keep the workflow and replace the inference engine

This section uses a CIX-based Radxa Orion O6 running Debian 12. The goal is not to compare its performance with DGX Spark. The goal is to verify that the same OpenClaw workflow can use a different local inference backend.

The layers that stay the same are:

- Telegram commands
- Memory and RAG collection roles
- Ollama embeddings
- Qdrant vector storage
- Browser search
- Cron scheduling
- Gateway dashboard
- AgentRegistry and TaskDispatcher

The generation backend changes:

```text
DGX Spark       -> vLLM
Radxa Orion O6  -> llama.cpp
OpenClaw client -> OpenAI-compatible API for both
```

## Check the CPU-only host

On Orion O6, confirm the operating system, architecture, CPU features, memory, and disk capacity:

```bash
uname -a
cat /etc/os-release
lscpu
free -h
df -h /
```

Confirm that the host reports `aarch64` and has enough available memory and storage for the selected GGUF model and containers.

## Build llama.cpp

Clone and build llama.cpp:

```bash
cd $HOME
git clone https://github.com/ggml-org/llama.cpp.git
cd llama.cpp
cmake -B build
cmake --build build -j
```

This Learning Path uses an ERNIE 4.5 GGUF model as the CPU-oriented text backend. Place a complete, verified GGUF file under a local model directory. Before loading it, confirm the file size and GGUF header:

```bash
ls -lh $HOME/ernie_lp/model/*.gguf
head -c 4 $HOME/ernie_lp/model/ERNIE-4.5-21B-A3B-Thinking-Q4_0.gguf
echo
```

The header should be:

```output
GGUF
```

{{% notice Note %}}
A tensor-out-of-bounds error normally indicates an incomplete or corrupted GGUF download. Verify the file before changing GPU-layer or context settings.
{{% /notice %}}

## Start the OpenAI-compatible llama.cpp server

Start the server on the host:

```bash
cd $HOME/llama.cpp

./build/bin/llama-server \
  --jinja \
  -m $HOME/ernie_lp/model/ERNIE-4.5-21B-A3B-Thinking-Q4_0.gguf \
  -c 2048 \
  -t 12 \
  --host 127.0.0.1 \
  --port 8080
```

From another shell, inspect the model endpoint:

```bash
curl http://127.0.0.1:8080/v1/models
```

Send a short completion request:

```bash
curl -sS http://127.0.0.1:8080/v1/chat/completions \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "ernie-o6",
    "messages": [{"role":"user","content":"Reply with one sentence about local AI on Arm."}],
    "max_tokens": 80,
    "temperature": 0.2
  }'
```

Do not continue until this local endpoint generates a valid response.

## Prepare Ollama and Qdrant

Ollama should listen on `127.0.0.1:11434` and Qdrant on `127.0.0.1:6333`.

Pull the embedding model:

```bash
ollama pull nomic-embed-text
```

One way to start persistent Qdrant storage is:

```bash
docker run -d \
  --name qdrant \
  --restart unless-stopped \
  -p 6333:6333 \
  -v $HOME/qdrant_storage:/qdrant/storage \
  qdrant/qdrant:latest
```

## Configure the CPU-only profile

Clone the same release on Orion O6:

```bash
cd $HOME
git clone https://github.com/odincodeshen/openclaw-arm-continuum.git
cd openclaw-arm-continuum
git checkout v1.2
cp .env.arm-cpu-only.example .env
```

Set your bot and private tokens in `.env`:

```text
OPENCLAW_TELEGRAM_BOT_TOKEN=<your-telegram-bot-token>
OPENCLAW_TELEGRAM_ALLOWED_CHAT_IDS=<your-telegram-chat-id>
OPENCLAW_CRON_CHAT_IDS=<your-telegram-chat-id>
OPENCLAW_GATEWAY_TOKEN=<generated-random-token>
```

Confirm the inference settings:

```text
OPENCLAW_VLLM_BASE_URL=http://127.0.0.1:8080/v1
OPENCLAW_VLLM_MODEL=ernie-o6
OPENCLAW_VISION_ENABLED=false
OPENCLAW_TRACKER_COLLECTION=personal_tracker_memory
OPENCLAW_KNOWLEDGE_COLLECTION=personal_knowledge_base
```

Although the environment variable retains the `VLLM` name for compatibility, it represents the configured generation endpoint and can point to llama.cpp.

Using the same collection names preserves the application contract, but it does not copy Qdrant data from DGX Spark to Orion O6. Each host keeps its own local collection data unless you migrate it separately.

For a smaller CPU-only context budget, keep search and retrieval compact:

```text
OPENCLAW_MAX_TOKENS=128
OPENCLAW_RETRIEVAL_LIMIT=3
OPENCLAW_SCRAPER_LIMIT=2
OPENCLAW_WEB_CONTEXT_CHARS=1800
```

## Start the CPU-only runtime

Start the full tutorial stack:

```bash
docker compose \
  --env-file .env \
  -f compose.arm-cpu-only.yaml \
  --profile web \
  --profile gateway \
  --profile voice \
  up -d
```

Check the services:

```bash
docker compose --env-file .env -f compose.arm-cpu-only.yaml ps
docker logs --tail 80 openclaw-telegram
docker logs --tail 80 openclaw-memory-watcher
docker logs --tail 80 openclaw-cron
```

If you do not need voice for the LP1 tests, you can omit `--profile voice` and set `OPENCLAW_WHISPER_ENABLED=false`.

## Repeat the workflow

Send the following commands to the CPU-only bot:

```text
/help
/mem #home The CPU-only household assistant runs the same OpenClaw workflow.
/rag memory: What workflow does the CPU-only household assistant run?
/search Find current public guidance for reducing household heating energy use.
/cron add daily 19:30 CPU-only check :: Remind the household to review the heating notes.
/cron list
```

Success means the user workflow is unchanged even though generation moved from vLLM on DGX Spark to llama.cpp on an Armv9 CPU.

## What you've learned and what's next

You have moved the OpenClaw runtime from a heterogeneous DGX Spark platform to a CPU-only Armv9 system by replacing the inference endpoint rather than rewriting the application.

Next, you will review the software portability result and identify the boundaries of the v1.2 implementation.
