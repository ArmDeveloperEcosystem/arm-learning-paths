---
title: (Optional) Port the app to a CPU-only Armv9 system
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Cross-platform portability

You can optionally move the runtime from NVIDIA DGX Spark to a CIX-based Radxa Orion O6 running Debian 12. `llama.cpp` provides local generation on the Armv9 CPU.

The Telegram interface, local memory and RAG, browser search, scheduled workflows, and deterministic routing remain unchanged. Only the local generation backend changes:

| Platform | Local generation backend | Runtime API contract |
|---|---|---|
| NVIDIA DGX Spark | vLLM | OpenAI-compatible API |
| Radxa Orion O6 | `llama.cpp` | OpenAI-compatible API |

{{% notice Note %}}
These backends match the environments used in this Learning Path and the [Run ERNIE-4.5 Mixture of Experts model on Armv9 with `llama.cpp`](/learning-paths/cross-platform/ernie_moe_v9/) Learning Path. You can use another local backend with a compatible OpenAI chat-completions API.
{{% /notice %}}

## Verify system requirements on Armv9 host

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

Follow the steps in [Set up `llama.cpp` on an Armv9 development board](/learning-paths/cross-platform/ernie_moe_v9/2_llamacpp_installation/). Install the dependencies, compile `llama.cpp`, download the ERNIE-4.5 Thinking Q4 GGUF model, and run its basic inference test.

The following commands use these installation paths:

```text
$HOME/llama.cpp/build/bin/llama-server
$HOME/models/ernie-4.5/ERNIE-4.5-21B-A3B-Thinking-Q4_0.gguf
```

## Deploy llama.cpp OpenAI-compatible server

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

Don't continue until this local endpoint generates a valid response.

Press `Ctrl+C` in the server shell after the smoke test. Create a user `systemd` service so that `llama.cpp` starts automatically and restarts after a failure:

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

## Provision supporting local services

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

If the container already exists, start it:

```bash
docker start openclaw-qdrant
```

Otherwise, create persistent storage and start Qdrant. Bind its ports to `localhost`:

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

## Configure the CPU-only runtime environment

Clone the same release on Orion O6:

```bash
cd $HOME
git clone https://github.com/odincodeshen/openclaw-arm-continuum.git
cd openclaw-arm-continuum
git checkout v1.2
cp .env.arm-cpu-only.example .env
```

Create a separate bot for this runtime with the [Telegram Bot tutorial](https://core.telegram.org/bots/tutorial). Don't reuse the DGX Spark bot token because two polling runtimes can compete for its updates. Have each account send a message to the new bot, then repeat the `getUpdates` process from the DGX Spark setup to obtain each `message.chat.id` value.

Generate a new Gateway token:

```bash
openssl rand -hex 32
```

Set the new bot and private tokens in `.env`:

```text
OPENCLAW_TELEGRAM_BOT_TOKEN=<your-telegram-bot-token>
OPENCLAW_TELEGRAM_ALLOWED_CHAT_IDS=<first-telegram-chat-id>,<second-telegram-chat-id>
OPENCLAW_CRON_CHAT_IDS=<first-telegram-chat-id>,<second-telegram-chat-id>
OPENCLAW_GATEWAY_TOKEN=<generated-gateway-token>
OPENCLAW_CRON_TIMEZONE=<your-IANA-timezone>
```

Separate multiple chat IDs with commas. Use the same IANA timezone format as before; scheduled jobs use UTC if you omit it.

Confirm the inference settings:

```text
OPENCLAW_VLLM_BASE_URL=http://127.0.0.1:8080/v1
OPENCLAW_VLLM_MODEL=ernie-o6
OPENCLAW_VISION_ENABLED=false
OPENCLAW_TRACKER_COLLECTION=personal_tracker_memory
OPENCLAW_KNOWLEDGE_COLLECTION=personal_knowledge_base
```

The `VLLM` variable name is retained for compatibility, but it can point to `llama.cpp`.

Using the same collection names keeps the configuration consistent, but it doesn't copy Qdrant data from DGX Spark. Each host keeps its own data.

Keep the CPU-only context small and disable unused voice transcription:

```text
OPENCLAW_MAX_TOKENS=128
OPENCLAW_RETRIEVAL_LIMIT=3
OPENCLAW_SCRAPER_LIMIT=2
OPENCLAW_WEB_CONTEXT_CHARS=1800
OPENCLAW_WHISPER_ENABLED=false
```

## Launch the CPU-only application stack

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
If this command can't resolve the hostname, inspect the Orion host DNS configuration with `cat /etc/resolv.conf`. Then update `OPENCLAW_DNS_SERVER_1` and `OPENCLAW_DNS_SERVER_2` in `.env` with DNS servers that are reachable from your network, restart the stack, and run the check again.
{{% /notice %}}

## Validate shared workflows on CPU

Test the CPU-only deployment with a budget assistant shared by two household members.

Create a file named `budget.txt` on the device that you use Telegram on:

```text
Shared household weekly budget: £120.
```

Upload the file with the `/knowledge` caption and copy the filename returned by the bot. Each allowlisted household member can then add a synthetic expense from their own chat:

```text
/mem #budget Groceries: £45.
/mem #budget Household supplies: £20.
```

After both entries are saved, either member can ask:

```text
/rag <returned-file-name> Based on the shared budget and the saved budget entries, how much remains?
```

Replace `<returned-file-name>` with the filename that was returned when you uploaded `budget.txt`.

The response should report that £55 remains. Both members use the same local collection, without separate per-member access controls.

The response alone doesn't prove which inference backend generated it. Inspect the Telegram runtime log:

```bash
docker logs --tail 20 openclaw-telegram
```

Look for the memory write handled by `memory_agent` and the completed retrieval request handled by `rag_agent`. Then, inspect the `llama.cpp` service log:

```bash
journalctl --user -u openclaw-llama.service -n 30 --no-pager
```

Look for a successful request to `/v1/chat/completions`. The Telegram response and both log entries confirm that the OpenClaw-based workflow is now using `llama.cpp` for local generation on the Armv9 CPU.

## Compare Arm deployment architectures

You've now built a local-first household assistant with memory, document RAG, browser search, and scheduled notifications. You ran the assistant with vLLM on NVIDIA DGX Spark, then moved it to `llama.cpp` on Radxa Orion O6.

The following comparison shows what stayed the same across the two Arm-based implementations and what changed with the local generation backend:

| Layer | NVIDIA DGX Spark | Radxa Orion O6 |
|---|---|---|
| Reference runtime services | Same services | Same services |
| User interface | Telegram | Telegram |
| Skills | Memory, RAG, search, weather, cron | Same skills |
| Vector memory | Qdrant | Qdrant |
| Embeddings | Ollama | Ollama |
| Generation API | OpenAI-compatible | OpenAI-compatible |
| Generation engine | vLLM | `llama.cpp` |
| Inference compute | Arm CPU + NVIDIA GPU | Arm CPU |

Each platform uses model and context settings suited to its compute while preserving the same application contract.

## Review data privacy boundaries

The runtime keeps inference requests, generated context, Qdrant collections, uploaded files, cron history, OpenClaw tasks, and Gateway state under your control.

Telegram still transports messages and uploads. Weather and browser searches contact public services, while setup downloads models and containers from external registries.

For sensitive deployments, review network exposure, Telegram suitability, host access, backups, model provenance, and the contents of every enabled tool.

## What you've learned and what's next

You've now moved the OpenClaw-based runtime from DGX Spark to a CPU-only Armv9 system by replacing the inference endpoint.

The same endpoint-driven design can support additional deployment shapes:

- An always-on CPU-only Arm server with a compact local model
- An Arm edge gateway connected to a trusted private-LAN inference server
- A heterogeneous Arm AI workstation hosting larger local models

Each deployment changes the compute and trust boundary. It shouldn't silently change where personal data is stored or which external services are contacted.
