---
title: Deploy Hermes Agent as an orchestration runtime
description: Deploy Hermes Agent as a containerized orchestration runtime that watches a shared workspace and logs file events on DGX Spark.
weight: 4
layout: "learningpathall"
---

## Add Hermes Agent to the runtime stack

In this section, you'll add Hermes Agent to the runtime stack.

Hermes Agent acts as the orchestration layer for the local AI runtime. It watches the workspace, detects runtime events, and coordinates the next action without requiring a user to manually run each step.

Hermes is the CPU-side orchestration runtime. It runs continuously, watches the shared workspace, and reacts when new files are created. This is the first step toward a persistent local AI agent.

In this section, Hermes doesn't call a language model yet. You'll first build the event-driven runtime foundation, where a new file in `workspace/inbox/` triggers a filesystem event, Hermes handles it, and prints a content preview to the logs.

In later sections, you'll add local inference, persistent memory, semantic retrieval, and autonomous cognition.

### Create the Hermes runtime directory

Return to the project root:

```bash
cd ~/dgx-hermes-agent
```

Create the Hermes source directory:

```bash
mkdir -p hermes
```

The project directory now looks like this:

```text
dgx-hermes-agent/
|-- compose/
|-- hermes/
|-- models/
|-- qdrant/
`-- workspace/
```

### Create the Hermes container image

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

### Create the Hermes runtime service

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

#### Understand the code trace

The runtime defines `WATCH_DIR = "/workspace/inbox"` as the monitored location. The `WorkspaceHandler` class inherits from `FileSystemEventHandler` and handles `on_created()` events. Directory events are filtered out immediately so only new files are processed. Each new file path is passed to `summarize_file()`, which reads and prints the first 500 characters.

The main loop uses `Observer` from the `watchdog` library to keep the process alive. The `while True: time.sleep(1)` loop is the core of a persistent orchestration runtime. The CPU holds the process open, polls for events, and triggers work when the runtime state changes.

### Update Docker Compose

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

The final Compose file now defines four services: `ollama`, `qdrant`, `open-webui`, and `hermes`. Hermes mounts the same shared workspace as the other services and receives environment variables for Ollama and Qdrant, which will be used in later sections.

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

The output is similar to:

```output
CONTAINER ID   IMAGE                                COMMAND                CREATED         STATUS                 PORTS                                                             NAMES
8439b1e36b6c   compose-hermes                       "python -u agent.py"   2 seconds ago   Up 2 seconds                                                                             hermes
8cb62495cb7b   ghcr.io/open-webui/open-webui:main   "bash start.sh"        3 hours ago     Up 3 hours (healthy)   0.0.0.0:3000->8080/tcp, [::]:3000->8080/tcp                       open-webui
367b013fd34c   ollama/ollama:latest                 "/bin/ollama serve"    3 hours ago     Up 3 hours             0.0.0.0:11434->11434/tcp, [::]:11434->11434/tcp                   ollama
e770401a4a0f   qdrant/qdrant:latest                 "./entrypoint.sh"      3 hours ago     Up 3 hours             0.0.0.0:6333-6334->6333-6334/tcp, [::]:6333-6334->6333-6334/tcp   qdrant
```
You'll see `hermes` alongside the existing runtime services.

## Validate the Hermes runtime 

After building the Hermes runtime, verify that it works as expected.

### Verify the Hermes runtime logs

Follow the Hermes logs:

```bash
docker logs -f hermes
```

The output is similar to:

```output
[Hermes Agent] Starting workspace watcher...
[Hermes Agent] Monitoring: /workspace/inbox
```

The output shows that Hermes started and is watching the shared inbox directory. Leave this terminal open with the log stream running and open a second terminal for the next step.

### Validate event-driven processing

Open a second terminal on the host and create a new test file. Use a filename that doesn't already exist so the `on_created()` event is triggered.

Create the file outside the inbox first, then move the completed file into `workspace/inbox/`:

```bash
echo "Hermes watches the workspace and reacts to new files." \
> /tmp/runtime-test.txt

mv /tmp/runtime-test.txt \
~/dgx-hermes-agent/workspace/inbox/runtime-test.txt
```
Doing this avoids triggering the filesystem event before the file content has finished writing.

Return to the terminal that is following Hermes logs. 

The output is similar to:

```output
[Agent] New file detected:
/workspace/inbox/runtime-test.txt

[Agent] File content preview:
Hermes watches the workspace and reacts to new files.
```

When the file is moved into `workspace/inbox/` on the host, the shared volume mount makes it visible inside the container immediately. The `watchdog` observer detects the new file and calls `on_created()`, which reads the file and prints the content preview you see in the logs.

### Verify shared workspace access

Hermes sees the host file path through the mounted container path:

| Host path | Container path |
|---|---|
| `~/dgx-hermes-agent/workspace/inbox` | `/workspace/inbox` |

This shared mount is what allows the host, Hermes, Ollama, and later memory workflows to operate on the same persistent runtime state.

## Understand CPU orchestration responsibilities

This section demonstrates the CPU-side work required by persistent AI systems. The Arm CPU runs the long-lived service process, monitors filesystem events, schedules runtime activity, processes files, and manages the containerized service lifecycle. The GPU becomes important when model inference is added, but the persistent runtime is coordinated entirely by the CPU.

## What you've accomplished and what's next

You've added Hermes Agent to the DGX Spark runtime stack as a persistent Python service. The runtime now has a Hermes container, a filesystem watcher, and a Docker Compose service that mounts the shared workspace.

You also verified that creating a new file in `workspace/inbox/` triggers Hermes logs, which confirms that the event-driven orchestration path is working.

Next, you'll connect Hermes to Ollama for local LLM summarization.

Before moving to the next section, press `Ctrl+C` in terminal 1 to stop the Hermes log stream. In the next section, you'll rebuild the Hermes container and run `docker logs -f hermes` again.
