---
title: Port the Application Workflow to a CPU-Only Armv9 System
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview of Cross-Platform Portability

This runtime architecture is designed to work across Arm systems with different compute configurations. In the previous sections, you deployed it on NVIDIA DGX Spark, a heterogeneous CPU-GPU platform using vLLM for local generation. In this section, you will move the same application workflows to a CIX-based Radxa Orion O6 running Debian 12, with llama.cpp providing local generation on the Armv9 CPU.

The Telegram interface, local memory and RAG, browser search, scheduled workflows, and deterministic routing remain unchanged. Only the local generation backend changes:

| Platform | Local generation backend | Runtime API contract |
|---|---|---|
| NVIDIA DGX Spark | vLLM | OpenAI-compatible API |
| Radxa Orion O6 | llama.cpp | OpenAI-compatible API |

{{% notice Note %}}
These backends were selected to build on the environments used in the earlier chapters and in [Run ERNIE-4.5 Mixture of Experts model on Armv9 with llama.cpp](/learning-paths/cross-platform/ernie_moe_v9/). They are not fixed architecture requirements. You can use another local inference backend that provides a compatible OpenAI chat-completions API.
{{% /notice %}}

## Verify System Requirements on Armv9 Host

On Orion O6, confirm the operating system, architecture, CPU features, memory, and disk capacity:

```bash
uname -a
cat /etc/os-release
lscpu
free -h
df -h /
```

Confirm that the host reports `aarch64` and has enough available memory and storage for the selected GGUF model and containers.

## Prepare llama.cpp and the ERNIE model

Follow [Set up llama.cpp on an Armv9 development board](/learning-paths/cross-platform/ernie_moe_v9/2_llamacpp_installation/) to install the build dependencies, compile llama.cpp, download the ERNIE-4.5 Thinking Q4 GGUF model, and run the basic inference test on Orion O6.

After you complete the setup in that Learning Path, continue with the steps below. They use the following installation paths:

```text
$HOME/llama.cpp/build/bin/llama-server
$HOME/models/ernie-4.5/ERNIE-4.5-21B-A3B-Thinking-Q4_0.gguf
```

## Deploy llama.cpp OpenAI-Compatible Server

Start the server on the host:

```bash
cd $HOME/llama.cpp

./build/bin/llama-server \
  --jinja \
  -m $HOME/models/ernie-4.5/ERNIE-4.5-21B-A3B-Thinking-Q4_0.gguf \
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

Press `Ctrl+C` in the server shell after the smoke test. Create a user systemd service so that llama.cpp starts automatically and restarts after a failure:

```bash
mkdir -p $HOME/.config/systemd/user

tee $HOME/.config/systemd/user/openclaw-llama.service > /dev/null <<'EOF'
[Unit]
Description=llama.cpp server for the OpenClaw-based runtime
Wants=network-online.target
After=network-online.target

[Service]
Type=simple
ExecStart=%h/llama.cpp/build/bin/llama-server --jinja -m %h/models/ernie-4.5/ERNIE-4.5-21B-A3B-Thinking-Q4_0.gguf -c 2048 -t 12 --host 127.0.0.1 --port 8080
Restart=on-failure
RestartSec=5

[Install]
WantedBy=default.target
EOF
```

Enable the service and allow it to remain active when you log out:

```bash
systemctl --user daemon-reload
systemctl --user enable --now openclaw-llama.service
sudo loginctl enable-linger $USER
systemctl --user status openclaw-llama.service --no-pager
```

Confirm that the managed endpoint responds:

```bash
curl http://127.0.0.1:8080/v1/models
```

## Provision Supporting Local Services

Install Ollama on the Orion O6 host:

```bash
curl -fsSL https://ollama.com/install.sh | sh
sudo systemctl enable --now ollama
```

The CPU-only compose file uses host networking, so its containers can reach Ollama through `127.0.0.1:11434`. Pull the embedding model:

```bash
ollama pull nomic-embed-text
```

Confirm that Ollama responds and lists `nomic-embed-text`:

```bash
curl http://127.0.0.1:11434/api/tags
```

Check whether the Qdrant container already exists:

```bash
docker ps -a --filter name=openclaw-qdrant
```

If it already exists, start it:

```bash
docker start openclaw-qdrant
```

Otherwise, create persistent storage and start Qdrant. Bind its ports to localhost:

```bash
docker volume create openclaw-qdrant-data

docker run -d \
  --name openclaw-qdrant \
  --restart unless-stopped \
  -p 127.0.0.1:6333:6333 \
  -p 127.0.0.1:6334:6334 \
  -v openclaw-qdrant-data:/qdrant/storage \
  qdrant/qdrant:latest
```

Confirm that the local API responds:

```bash
curl http://127.0.0.1:6333/collections
```

## Configure the CPU-Only Runtime Environment

Clone the same release on Orion O6:

```bash
cd $HOME
git clone https://github.com/odincodeshen/openclaw-arm-continuum.git
cd openclaw-arm-continuum
git checkout v1.2
cp .env.arm-cpu-only.example .env
```

Create a separate Telegram bot for the CPU-only runtime by following the [Telegram Bot tutorial](https://core.telegram.org/bots/tutorial). Do not reuse the bot token from the running DGX Spark deployment because two polling runtimes using the same bot can compete for Telegram updates.

Generate a new Gateway token:

```bash
openssl rand -hex 32
```

Set the new bot and private tokens in `.env`:

```text
OPENCLAW_TELEGRAM_BOT_TOKEN=<your-telegram-bot-token>
OPENCLAW_TELEGRAM_ALLOWED_CHAT_IDS=<first-chat-id>,<second-chat-id>
OPENCLAW_CRON_CHAT_IDS=<first-chat-id>,<second-chat-id>
OPENCLAW_GATEWAY_TOKEN=<generated-random-token>
```

Separate multiple allowlisted chat IDs with commas. Both household members can then use the same bot and shared local collections.

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

## Launch the CPU-Only Application Stack

Voice transcription is not used in this Learning Path. Keep it disabled in `.env`:

```text
OPENCLAW_WHISPER_ENABLED=false
```

Start the full tutorial stack:

```bash
docker compose \
  --env-file .env \
  -f compose.arm-cpu-only.yaml \
  --profile web \
  --profile gateway \
  up -d
```

Check the services:

```bash
docker compose --env-file .env -f compose.arm-cpu-only.yaml ps
docker logs --tail 80 openclaw-telegram
docker logs --tail 80 openclaw-memory-watcher
docker logs --tail 80 openclaw-cron
```

Confirm that the browser worker can resolve a public hostname:

```bash
docker exec openclaw-browser-scraper python -c "import socket; print(socket.gethostbyname('duckduckgo.com'))"
```

{{% notice Note %}}
If this command cannot resolve the hostname, inspect the Orion host DNS configuration with `cat /etc/resolv.conf`. Then update `OPENCLAW_DNS_SERVER_1` and `OPENCLAW_DNS_SERVER_2` in `.env` with DNS servers that are reachable from your network, restart the stack, and run the check again.
{{% /notice %}}

## Validate Shared Workflows on CPU

The previous chapters used a household assistant to validate memory, document retrieval, browser search, and scheduled reminders. In this section, you continue the household scenario on the CPU-only deployment by creating a simple budget assistant that two household members can share.

Create a file named `budget.txt` on the device where you use Telegram:

```text
Shared household weekly budget: £120.
```

Upload the file to the bot. Any caption other than `/tracker` or `/mem` routes the upload to knowledge indexing by default, so use `/knowledge` as the caption to make the destination explicit. Each allowlisted household member can then add a synthetic expense from their own Telegram chat:

```text
/mem #budget Groceries: £45.
/mem #budget Household supplies: £20.
```

After both entries are saved, either member can ask:

```text
/rag <returned-file-name> Based on the shared budget and the saved budget entries, how much remains?
```

The response should report that £55 remains. This simple example demonstrates how allowlisted household members can contribute to and query the same local collection. The reference runtime treats this as shared household data and does not provide separate per-member access controls.

The response alone does not prove which inference backend generated it. Inspect the Telegram runtime log:

```bash
docker logs --tail 20 openclaw-telegram
```

Look for the memory write handled by `memory_agent` and the completed retrieval request handled by `rag_agent`. Then inspect the llama.cpp service log:

```bash
journalctl --user -u openclaw-llama.service -n 30 --no-pager
```

Look for a successful request to `/v1/chat/completions`. The Telegram response and both log entries confirm that the OpenClaw-based workflow is now using llama.cpp for local generation on the Armv9 CPU.

This simplified example does not reset the budget at the start of each week. You can extend the runtime with a dedicated budget agent and scheduled workflow to manage weekly periods and resets.

## What you've learned and what's next

You have moved the OpenClaw-based runtime from DGX Spark to a CPU-only Armv9 system by replacing the inference endpoint rather than rewriting the application.

Next, you will review the software portability result and identify the current implementation boundaries.
