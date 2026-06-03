---
title: Build the DGX Spark AI runtime foundation
weight: 3
layout: "learningpathall"
---

## Build the DGX Spark AI runtime foundation

In this section, you will prepare the base runtime used by the rest of the Learning Path.

You will install Docker, configure GPU-enabled containers, create a persistent workspace, and start the initial runtime service stack:

- Ollama for local inference
- Qdrant for vector memory
- Open WebUI for browser-based model access

Hermes Agent is added in the next section. This section builds the local infrastructure it depends on.

## Verify the DGX Spark environment

Start by verifying that your DGX Spark system exposes the expected Arm CPU and NVIDIA GPU environment.

Check the CPU architecture:

```bash
uname -m
```

The expected output is:

```text
aarch64
```

Check the Linux distribution. DGX Spark runs Ubuntu 24.04:

```bash
lsb_release -a
```

Check that the NVIDIA GPU and CUDA driver stack are visible:

```bash
nvidia-smi
```

Confirm that the command shows the GPU name (NVIDIA GB10), driver version, and CUDA version. Make a note of the CUDA version, as you will use a matching container image when verifying GPU passthrough in the next step.

Example output:

```text
nvidia-smi
Wed May 20 18:12:05 2026       
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 580.95.05              Driver Version: 580.95.05      CUDA Version: 13.0     |
+-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA GB10                    On  |   0000000F:01:00.0 Off |                  N/A |
| N/A   36C    P8              4W /  N/A  | Not Supported          |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+

+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|    0   N/A  N/A            3565      G   /usr/lib/xorg/Xorg                      137MiB |
|    0   N/A  N/A            3776      G   /usr/bin/gnome-shell                    164MiB |
|    0   N/A  N/A            5115      G   .../8305/usr/lib/firefox/firefox        239MiB |
|    0   N/A  N/A           85940      G   ...m Performix/arm-performix-gui         54MiB |
+-----------------------------------------------------------------------------------------+
```

## Install Docker

If Docker is not already installed, the [Docker Engine install guide](/install-guides/docker/docker-engine/) covers installation in detail.

To install quickly, run:

```bash
curl -fsSL get.docker.com -o get-docker.sh && sh get-docker.sh
```

Allow your user to run Docker commands without `sudo`, then apply the new group membership in the current shell:

```bash
sudo usermod -aG docker $USER
newgrp docker
```

Verify Docker is working:

```bash
docker run hello-world
```

You should see a message confirming that Docker is installed and working.

## Install NVIDIA Container Toolkit

The NVIDIA Container Toolkit enables Docker to expose the GPU to containers using the `--gpus` flag. Without it, containers cannot access the GPU regardless of the driver version installed on the host.

Add the NVIDIA Container Toolkit GPG key:

```bash
curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | \
sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg
```

Add the NVIDIA Container Toolkit repository:

```bash
curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
```

Install the toolkit:

```bash
sudo apt update
sudo apt install -y nvidia-container-toolkit
```

Register the NVIDIA runtime with Docker. This adds the `nvidia` runtime to Docker's daemon configuration so containers can request GPU access with `--gpus`:

```bash
sudo nvidia-ctk runtime configure --runtime=docker
```

Restart Docker to apply the configuration change:

```bash
sudo systemctl restart docker
```

## Verify GPU-enabled containers

Run a CUDA validation container:

```bash
docker run --rm --gpus all \
nvcr.io/nvidia/cuda:13.0.1-devel-ubuntu24.04 \
nvidia-smi
```

If you have not pulled this image before, Docker downloads it before running `nvidia-smi`. This can take a few minutes depending on your network connection.

```text
Unable to find image 'nvcr.io/nvidia/cuda:13.0.1-devel-ubuntu24.04' locally
13.0.1-devel-ubuntu24.04: Pulling from nvidia/cuda
03f66a4525ea: Pull complete 
c03b8ec8dd33: Pull complete 
cae1e96ffa7d: Pull complete 
2cb956a72162: Pull complete 
817eab9d3c52: Pull complete 
cc43ec4c1381: Pull complete 
30fc8198a31e: Pull complete 
c88eadd06616: Pull complete 
c7ba38867e8d: Pull complete 
fd2e70db7702: Pull complete 
85eb6b47da08: Pull complete 
Digest: sha256:7d2f6a8c2071d911524f95061a0db363e24d27aa51ec831fcccf9e76eb72bc92
Status: Downloaded newer image for nvcr.io/nvidia/cuda:13.0.1-devel-ubuntu24.04

==========
== CUDA ==
==========

CUDA Version 13.0.1

Container image Copyright (c) 2016-2023, NVIDIA CORPORATION & AFFILIATES. All rights reserved.

This container image and its contents are governed by the NVIDIA Deep Learning Container License.
By pulling and using the container, you accept the terms and conditions of this license:
https://developer.nvidia.com/ngc/nvidia-deep-learning-container-license

A copy of this license is made available in this container at /NGC-DL-CONTAINER-LICENSE for your convenience.

Sun May 24 10:13:04 2026       
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 580.159.03             Driver Version: 580.159.03     CUDA Version: 13.0     |
+-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA GB10                    On  |   0000000F:01:00.0 Off |                  N/A |
| N/A   44C    P0             10W /  N/A  | Not Supported          |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+

+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|  No running processes found                                                             |
+-----------------------------------------------------------------------------------------+
```

If the command prints GPU information from inside the container, Docker GPU passthrough is working.

Docker can now run GPU-accelerated containers on DGX Spark.

## Create the persistent workspace

Create the project directory:

```bash
mkdir -p ~/dgx-hermes-agent
cd ~/dgx-hermes-agent
```

Create the directory structure used by the runtime:

```bash
mkdir -p \
workspace/inbox \
workspace/memory \
workspace/logs \
workspace/processed \
workspace/config \
models \
compose \
qdrant
```

The workspace should now look like this:

```text
dgx-hermes-agent/
|-- compose/
|-- models/
|-- qdrant/
|-- workspace/
|   |-- config/
|   |-- inbox/
|   |-- logs/
|   |-- memory/
|   `-- processed/
```

The `workspace/` directory is shared across runtime services. Hermes will later monitor `workspace/inbox/`, write generated artifacts to `workspace/memory/`, and read runtime policies from `workspace/config/`.

## Build the runtime service stack

Create and edit the file `~/dgx-hermes-agent/compose/docker-compose.yml`.

Add the following content:

```yaml
services:

  ollama:
    image: ollama/ollama:latest
    container_name: ollama

    ports:
      - "11434:11434"

    dns:
      - 8.8.8.8
      - 1.1.1.1

    volumes:
      - ../models:/root/.ollama
      - ../workspace:/workspace

    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: all
              capabilities: [gpu]

    environment:
      - NVIDIA_VISIBLE_DEVICES=all

    restart: unless-stopped

  qdrant:
    image: qdrant/qdrant:latest
    container_name: qdrant

    ports:
      - "6333:6333"
      - "6334:6334"

    volumes:
      - ../qdrant:/qdrant/storage

    restart: unless-stopped

  open-webui:
    image: ghcr.io/open-webui/open-webui:main
    container_name: open-webui

    ports:
      - "3000:8080"

    environment:
      - OLLAMA_BASE_URL=http://ollama:11434

    volumes:
      - open-webui:/app/backend/data

    depends_on:
      - ollama

    restart: unless-stopped

volumes:
  open-webui:
```

This Compose stack creates the first three runtime services. Hermes will be added as a fourth service later. The explicit DNS settings in the Ollama service help the container reach the model registry reliably. You will verify this in the networking step.

## Runtime service roles

The initial stack separates model execution, memory storage, and user interaction.

| Service | Role |
|---|---|
| Ollama | Runs local language and embedding models |
| Qdrant | Stores persistent vector memory |
| Open WebUI | Provides a local browser interface to Ollama |

The `models/` directory persists Ollama models on the host. The `qdrant/` directory persists vector database storage. The `workspace/` directory is mounted into Ollama now and will also be mounted into Hermes later.

Ollama does not orchestrate workspace files by itself. The workspace mount verification step confirms shared storage access. Hermes will become the service that reads workspace files and decides when to call Ollama.

## Start the runtime stack

If Ollama is already installed as a host service, stop it to avoid port conflicts:

```bash
sudo systemctl stop ollama
sudo systemctl disable ollama
```

Start the container stack:

```bash
cd ~/dgx-hermes-agent/compose
docker compose up -d
```

{{% notice Note %}}
The first `docker compose up -d` run can take several minutes because Docker needs to pull the service images. The time depends on your network speed.
{{% /notice %}}

Verify that the containers are running:

```bash
docker ps
```

You should see containers similar to:

```text
NAME         IMAGE                                COMMAND               SERVICE      CREATED         STATUS                            PORTS
ollama       ollama/ollama:latest                 "/bin/ollama serve"   ollama       5 seconds ago   Up 4 seconds                      0.0.0.0:11434->11434/tcp, [::]:11434->11434/tcp
open-webui   ghcr.io/open-webui/open-webui:main   "bash start.sh"       open-webui   4 seconds ago   Up 4 seconds (health: starting)   0.0.0.0:3000->8080/tcp, [::]:3000->8080/tcp
qdrant       qdrant/qdrant:latest                 "./entrypoint.sh"     qdrant       5 seconds ago   Up 4 seconds                      0.0.0.0:6333-6334->6333-6334/tcp, [::]:6333-6334->6333-6334/tcp
```

## Verify container networking

Open a shell in the Ollama container:

```bash
docker exec -it ollama bash
```

You may see a warning such as `groups: cannot find name for group ID 992`. It appears when the container's `/etc/group` file has no entry for your host user's GID and is harmless. The shell opens normally and all commands work as expected.

Verify DNS resolution:

```bash
getent hosts registry.ollama.ai
```

Example output:

```text
root@367b013fd34c:/# getent hosts registry.ollama.ai
2606:4700:3036::6815:4be3 registry.ollama.ai
2606:4700:3034::ac43:b6e5 registry.ollama.ai
```

Exit the container shell:

```bash
exit
```

The DNS settings in the Compose file help the container reach the Ollama model registry reliably.

## Pull local models

Open a shell in the Ollama container:

```bash
docker exec -it ollama bash
```

Pull the language model:

```bash
ollama pull qwen2.5:7b
```

Pull the embedding model:

```bash
ollama pull nomic-embed-text
```

Exit the container:

```bash
exit
```

These model names are used throughout the examples, so keep them when following along. The architecture supports other suitable models.

Because the `models/` directory is mounted into the container as a volume, downloaded models are stored on the host at `~/dgx-hermes-agent/models/` and persist even if the container is removed or recreated.

| Model | Purpose |
|---|---|
| `qwen2.5:7b` | Local chat, summarization, reasoning |
| `nomic-embed-text` | Embedding generation for semantic memory |

## Verify local inference

Open a shell in the Ollama container:

```bash
docker exec -it ollama bash
```

Run the local model:

```bash
ollama run qwen2.5:7b
```

Enter a short prompt, such as:

```text
Summarize the role of CPU orchestration for an AI agent in one sentence.
```

After the model responds, type `/bye` to exit the interactive model session, then type `exit` to leave the container shell.

You can also monitor GPU activity from another terminal while the model is running:

```bash
nvtop
```

During inference, you should see GPU utilization rise on the Blackwell GPU as the model processes the prompt and generates tokens. This confirms the model is running on the GPU rather than falling back to the CPU.

This step validates that local inference is available before Hermes begins calling Ollama programmatically.

## Verify Open WebUI

Open a browser and navigate to:

```text
http://localhost:3000
```

On first launch, Open WebUI presents a setup screen asking for a name and email address. This creates a local admin account. The email does not need to be real and no data leaves your system. Enter any values and continue to the main interface.

To verify that Ollama is reachable from the host, navigate to:

```text
http://localhost:11434
```

If Ollama is running, the browser displays the message `Ollama is running`. This confirms that the Ollama container is accessible on the expected port. Open WebUI connects to Ollama using the internal Docker network address `http://ollama:11434`, but from the host you use `localhost:11434`.

Use Open WebUI to confirm that the local model is listed and available for chat. Open WebUI is not used in the agent workflow in the sections that follow. Hermes calls Ollama directly through its API, so Open WebUI serves only as a convenient way to validate the inference stack before the agent takes over.

## Verify Qdrant

Open the Qdrant dashboard:

```text
http://localhost:6333/dashboard
```

![Qdrant dashboard running locally before the workspace_memory collection is created#center](qdrant_dashboard.png "Qdrant Dashboard")

Qdrant is running, but it does not contain the `workspace_memory` collection yet. Hermes creates that collection later when you add persistent memory.

## Verify the shared workspace mount

Open another terminal on your DGX Spark system and create a test file on the host. Do not run this command inside a container.

```bash
echo "Arm CPUs orchestrate persistent AI workflows." \
> ~/dgx-hermes-agent/workspace/inbox/test.txt
```

Verify that the shared mount is visible by opening a shell in the Ollama container:

```bash
docker exec -it ollama bash
```

Inside the container, run:

```bash
ls -l /workspace
cat /workspace/inbox/test.txt
```

You should see:

```text
drwxrwxr-x 2 1001 1001 4096 May 20 18:16 config
drwxrwxr-x 2 1001 1001 4096 May 20 18:37 inbox
drwxrwxr-x 2 1001 1001 4096 May 20 18:16 logs
drwxrwxr-x 2 1001 1001 4096 May 20 18:16 memory
drwxrwxr-x 2 1001 1001 4096 May 20 18:16 processed
```

And the file content:

```text
Arm CPUs orchestrate persistent AI workflows.
```

Exit the container:

```bash
exit
```

## Summary

You have built the runtime foundation for the persistent local AI system. The DGX Spark environment now has Docker, Docker Compose, NVIDIA Container Toolkit, GPU-enabled containers, persistent workspace storage, and the initial Ollama, Qdrant, and Open WebUI services.

You also verified shared workspace access, local inference, and the fixed model setup used by the later sections.

Next, you will add Hermes Agent as the persistent orchestration runtime.
