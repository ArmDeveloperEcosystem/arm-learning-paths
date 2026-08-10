---
title: Prepare the DGX Spark host and local services
description: Prepare an NVIDIA DGX Spark host with Docker, Ollama embeddings, Qdrant vector storage, and the pinned OpenClaw Arm Continuum repository.
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Prepare the DGX Spark host environment

Confirm that the Arm CPU and NVIDIA GPU are visible:

```bash
uname -m
nvidia-smi
```

The expected CPU architecture is:

```output
aarch64
```

{{% notice Note %}}
You'll use Docker Engine and Docker Compose to run services on your DGX Spark. For Docker installation steps, see the [Install Docker Engine](https://learn.arm.com/install-guides/docker/docker-engine/).
{{% /notice %}}

Confirm Docker GPU access:

```bash
docker run --rm --gpus all ubuntu nvidia-smi
```

You don't need to install the vLLM Python package or start a vLLM server directly on the DGX Spark host. The project's `compose.yaml` pulls a container image that already includes vLLM and starts the local inference server for you.

You need to install the NVIDIA driver and NVIDIA Container Toolkit so that this container can access the GPU.

## Configure Ollama for local embeddings

Unlike vLLM, Ollama isn't included as a service in the project's `compose.yaml`. Install and run Ollama separately on the DGX Spark host before starting the reference runtime.

Install Ollama using the [official Linux installer](https://docs.ollama.com/linux):

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

The project containers connect to Ollama through the Docker host gateway. Create a `systemd` override that configures Ollama to listen on the host interfaces:

```bash
sudo install -d -m 0755 /etc/systemd/system/ollama.service.d
printf '%s\n' '[Service]' 'Environment="OLLAMA_HOST=0.0.0.0:11434"' | \
  sudo tee /etc/systemd/system/ollama.service.d/override.conf
```

Confirm the override file:

```bash
sudo systemctl cat ollama
```

The output should include the override:

```output
# /etc/systemd/system/ollama.service.d/override.conf
[Service]
Environment="OLLAMA_HOST=0.0.0.0:11434"
```

Reload `systemd` and restart Ollama:

```bash
sudo systemctl daemon-reload
sudo systemctl enable --now ollama
sudo systemctl restart ollama
```

Pull the embedding model that you'll use:

```bash
ollama pull nomic-embed-text
```

Confirm that Ollama lists the model:

```bash
curl http://127.0.0.1:11434/api/tags
```

The output is similar to:

```output
{
  "models": [
    {
      "name": "nomic-embed-text:latest",
      "capabilities": ["embedding"]
    }
  ]
}
```

## Start Qdrant for persistent vector storage

Create a Docker volume so that vector data remains available when the Qdrant container is replaced:

```bash
docker volume create openclaw-qdrant-data
```

Start Qdrant on the host using the [official container image](https://qdrant.tech/documentation/quick-start/):

```bash
docker run -d \
  --name openclaw-qdrant \
  --restart unless-stopped \
  -p 6333:6333 \
  -p 6334:6334 \
  -v openclaw-qdrant-data:/qdrant/storage \
  qdrant/qdrant
```

The `docker run` command creates the container and is needed only the first time. If `openclaw-qdrant` already exists but is stopped, start it instead:

```bash
docker start openclaw-qdrant
```

Confirm that the Qdrant API responds:

```bash
curl http://127.0.0.1:6333/collections
```

The output is similar to:

```output
{
  "result": {"collections": []},
  "status": "ok"
}
```

The empty list is expected at this stage before the reference runtime creates its collections. The runtime creates collections when you save or ingest content.

{{% notice Warning %}}
The project containers need access to Ollama and Qdrant. Restrict ports `11434`, `6333`, and `6334` to the host and its Docker networks.
{{% /notice %}}

## Clone the reference repository

Clone the repository and check out the release that you'll use:

```bash
git clone https://github.com/odincodeshen/openclaw-arm-continuum.git
cd openclaw-arm-continuum
git checkout v1.2
```

The tag fixes the tutorial source version. Unversioned container images and model artifacts can still change when downloaded.

## What you've accomplished and what's next

You've prepared the DGX Spark host, configured local embeddings, started Qdrant, and checked out the reference repository.

Next, you'll configure the Telegram bot and start the OpenClaw runtime.
