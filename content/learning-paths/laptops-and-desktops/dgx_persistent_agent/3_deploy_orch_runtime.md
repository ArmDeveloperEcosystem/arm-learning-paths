---
title: Deploy Hermes orchestration runtime
weight: 4
layout: "learningpathall"
---

## Deploy Hermes orchestration runtime

In this section, you will add Hermes Agent to the runtime stack.

The purpose of Hermes Agent is to act as the orchestration layer for the local AI runtime. It watches the workspace, detects runtime events, and coordinates the next action without requiring a user to manually run each step.

Hermes is the CPU-side orchestration runtime. It runs continuously, watches the shared workspace, and reacts when new files are created. This is the first step toward a persistent local AI agent.

In this section, Hermes does not call a language model yet. You will first build the event-driven runtime foundation, where a new file in `workspace/inbox/` triggers a filesystem event, Hermes handles it, and a content preview is printed to the logs.

Later sections add local inference, persistent memory, semantic retrieval, and autonomous cognition.

## Create the Hermes runtime directory

Return to the project root:

```bash
cd ~/dgx-hermes-agent
```

Create the Hermes source directory:

```bash
mkdir -p hermes
```

The project directory should now look like this:

```output
dgx-hermes-agent/
|-- compose/
|-- hermes/
|-- models/
|-- qdrant/
`-- workspace/
```

## Create the Hermes container image

Create and edit the file `~/dgx-hermes-agent/hermes/Dockerfile`.

Add the following content:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    git \
    curl \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir \
    ollama \
    qdrant-client \
    watchdog \
    sentence-transformers \
    pypdf \
    python-dotenv

COPY . /app

CMD ["python", "-u", "agent.py"]
```

This image installs the dependencies used throughout the Learning Path. Some packages, such as `ollama` and `qdrant-client`, are used in later sections. Installing them now keeps the Hermes container image consistent as the runtime gains capabilities.

The `CMD` uses `python -u` to enable unbuffered output. This is important for a persistent service because log messages appear immediately in `docker logs -f hermes` rather than being held in a buffer.

## Create the Hermes runtime service

Create and edit the file `~/dgx-hermes-agent/hermes/agent.py`.

Add the following content:

```python
import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

WATCH_DIR = "/workspace/inbox"

class WorkspaceHandler(FileSystemEventHandler):

    def on_created(self, event):

        if event.is_directory:
            return

        print(f"\n[Agent] New file detected:")
        print(event.src_path)

        summarize_file(event.src_path)

def summarize_file(path):

    try:

        with open(path, "r") as f:
            content = f.read()

        print("\n[Agent] File content preview:")
        print(content[:500])

    except Exception as e:

        print(f"[Agent] Error reading file: {e}")

if __name__ == "__main__":

    print("\n[Hermes Agent] Starting workspace watcher...")
    print(f"[Hermes Agent] Monitoring: {WATCH_DIR}")

    observer = Observer()

    observer.schedule(
        WorkspaceHandler(),
        WATCH_DIR,
        recursive=False
    )

    observer.start()

    try:

        while True:
            time.sleep(1)

    except KeyboardInterrupt:

        observer.stop()

    observer.join()
```

This first version of the agent starts a long-running runtime process, watches `/workspace/inbox`, and handles file creation events.

The `summarize_file()` function does not use an LLM yet. For now, it reads and prints the first 500 characters of the file. This validates the filesystem event pipeline before adding model inference.

## Code trace

The runtime defines `WATCH_DIR = "/workspace/inbox"` as the monitored location. The `WorkspaceHandler` class inherits from `FileSystemEventHandler` and handles `on_created()` events. Directory events are filtered out immediately so only new files are processed. Each new file path is passed to `summarize_file()`, which reads and prints the first 500 characters.

The main loop uses `Observer` from the `watchdog` library to keep the process alive. The `while True: time.sleep(1)` loop is the core of a persistent orchestration runtime. The CPU holds the process open, polls for events, and triggers work when the runtime state changes.

## Update Docker Compose

Open and edit the file `~/dgx-hermes-agent/compose/docker-compose.yml`.

Add the Hermes service under `services:`:

```yaml
  hermes:
    build:
      context: ../hermes

    container_name: hermes

    volumes:
      - ../workspace:/workspace

    environment:
      - OLLAMA_HOST=http://ollama:11434
      - QDRANT_HOST=qdrant

    depends_on:
      - ollama
      - qdrant

    restart: unless-stopped
```

The final Compose file now defines four services: `ollama`, `qdrant`, `open-webui`, and `hermes`. Hermes mounts the same shared workspace as the other services and receives environment variables for Ollama and Qdrant, which are used in later sections.

## Build the Hermes runtime

Build the Hermes container:

```bash
cd ~/dgx-hermes-agent/compose
docker compose build hermes
```

The first build installs the Python dependencies listed in the Dockerfile.

Start the stack:

```bash
docker compose up -d
```

Verify that the Hermes container is running:

```bash
docker ps
```

You should see hermes alongside the existing runtime services:

```text
CONTAINER ID   IMAGE                                COMMAND                CREATED         STATUS                 PORTS                                                             NAMES
8439b1e36b6c   compose-hermes                       "python -u agent.py"   2 seconds ago   Up 2 seconds                                                                             hermes
8cb62495cb7b   ghcr.io/open-webui/open-webui:main   "bash start.sh"        3 hours ago     Up 3 hours (healthy)   0.0.0.0:3000->8080/tcp, [::]:3000->8080/tcp                       open-webui
367b013fd34c   ollama/ollama:latest                 "/bin/ollama serve"    3 hours ago     Up 3 hours             0.0.0.0:11434->11434/tcp, [::]:11434->11434/tcp                   ollama
e770401a4a0f   qdrant/qdrant:latest                 "./entrypoint.sh"      3 hours ago     Up 3 hours             0.0.0.0:6333-6334->6333-6334/tcp, [::]:6333-6334->6333-6334/tcp   qdrant
```

## Verify Hermes runtime logs

Follow the Hermes logs:

```bash
docker logs -f hermes
```

Expected output:

```output
[Hermes Agent] Starting workspace watcher...
[Hermes Agent] Monitoring: /workspace/inbox
```

This confirms that Hermes started and is watching the shared inbox directory. Leave this terminal open with the log stream running and open a second terminal for the next step.

## Validate event-driven processing

Open a second terminal on the host and create a new test file. Use a filename that does not already exist so the `on_created()` event is triggered.

Create the file outside the inbox first, then move the completed file into `workspace/inbox/`. This avoids triggering the filesystem event before the file content has finished writing.

```bash
echo "Hermes watches the workspace and reacts to new files." \
> /tmp/runtime-test.txt

mv /tmp/runtime-test.txt \
~/dgx-hermes-agent/workspace/inbox/runtime-test.txt
```

Return to the terminal that is following Hermes logs. You should see output similar to:

```output
[Agent] New file detected:
/workspace/inbox/runtime-test.txt

[Agent] File content preview:
Hermes watches the workspace and reacts to new files.
```

When the file is moved into `workspace/inbox/` on the host, the shared volume mount makes it visible inside the container immediately. The `watchdog` observer detects the new file and calls `on_created()`, which reads the file and prints the content preview you see in the logs.

## Verify shared workspace access

Hermes sees the host file path through the mounted container path:

| Host path | Container path |
|---|---|
| `~/dgx-hermes-agent/workspace/inbox` | `/workspace/inbox` |

This shared mount is what allows the host, Hermes, Ollama, and later memory workflows to operate on the same persistent runtime state.

## Runtime responsibilities

At this stage, Hermes monitors the filesystem, handles events, reads files, and triggers workflow steps. It is not yet performing inference, generating embeddings, or storing vectors. Those capabilities are added incrementally so you can validate each layer of the runtime before moving on.

## CPU orchestration responsibilities

This section demonstrates the CPU-side work required by persistent AI systems. The Arm CPU runs the long-lived service process, monitors filesystem events, schedules runtime activity, processes files, and manages the containerized service lifecycle. The GPU becomes important when model inference is added, but the persistent runtime is coordinated entirely by the CPU.

## Summary

Before moving to the next section, press `Ctrl+C` in terminal 1 to stop the Hermes log stream. The next section rebuilds the Hermes container and runs `docker logs -f hermes` again.

You added Hermes Agent to the DGX Spark runtime stack as a persistent Python service. The runtime now has a Hermes container, a filesystem watcher, and a Docker Compose service that mounts the shared workspace.

You also verified that creating a new file in `workspace/inbox/` triggers Hermes logs, which confirms that the event-driven orchestration path is working.

Next, you will connect Hermes to Ollama for local LLM summarization.
