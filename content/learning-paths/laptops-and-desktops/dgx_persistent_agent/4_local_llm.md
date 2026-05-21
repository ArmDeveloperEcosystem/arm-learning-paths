---
title: Add Local LLM Inference
weight: 5
layout: "learningpathall"
---

## Add Local LLM Inference

In this section, you will connect ***Hermes Agent*** to ***Ollama***.

The purpose of this step is to turn Hermes from a file watcher into an ***inference orchestrator***. Hermes still controls the workflow, but it now sends document content to Ollama and uses the model response as part of the runtime output.

The runtime already watches `workspace/inbox/` and reacts when a file is created. You will now extend that workflow so Hermes sends file content to a ***local language model*** and prints an AI-generated summary.

The workflow becomes:

```text
workspace/inbox document
    -> Hermes on_created() handler
    -> Hermes calls Ollama
    -> Local LLM summary
```

This introduces the first GPU-accelerated step in the persistent runtime.

## Configure Ollama Runtime Access

Hermes reaches Ollama through the Docker Compose network.

In the Hermes Compose service, this environment variable was added earlier:

```yaml
environment:
  - OLLAMA_HOST=http://ollama:11434
```

Inside the Docker network, the service name `ollama` resolves to the Ollama container. Hermes uses this URL when it creates the Ollama Python client.

Verify that the Ollama container is running:

```bash
cd ~/dgx-hermes-agent/compose
docker ps
```

You should see both ***ollama*** and ***hermes*** running.


## Verify the Local Language Model

You pulled `qwen2.5:7b` when you built the runtime foundation. In this section, run a quick inference test to confirm that the model is still available inside the Ollama container:

```bash
docker exec -it ollama ollama run qwen2.5:7b
```

Enter a short prompt:

```text
Summarize persistent AI runtimes in one sentence.
```

Exit the model session when finished.

## Add Inference Support to Hermes

Open and edit the file `~/dgx-hermes-agent/hermes/agent.py`.

Replace the file with the following version:

```python
import os
import time
import ollama

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

WATCH_DIR = "/workspace/inbox"

OLLAMA_HOST = os.getenv(
    "OLLAMA_HOST",
    "http://ollama:11434"
)

client = ollama.Client(host=OLLAMA_HOST)

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

        print("\n[Agent] Running local inference...")

        response = client.chat(
            model="qwen2.5:7b",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a local AI workspace assistant. "
                        "Summarize the document in 3 concise bullet points."
                    )
                },
                {
                    "role": "user",
                    "content": content[:4000]
                }
            ]
        )

        summary = response["message"]["content"]

        print("\n[Agent] AI Summary:")
        print(summary)

    except Exception as e:

        print(f"[Agent] Error: {e}")

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

## Code Trace

This version adds the Ollama Python SDK:

```python
import ollama
```

Hermes reads the Ollama endpoint from the runtime environment:

```python
OLLAMA_HOST = os.getenv(
    "OLLAMA_HOST",
    "http://ollama:11434"
)
```

The client connects to the Ollama service:

```python
client = ollama.Client(host=OLLAMA_HOST)
```

The file content is sent to the local model:

```python
response = client.chat(
    model="qwen2.5:7b",
    messages=[
        {
            "role": "system",
            "content": (
                "You are a local AI workspace assistant. "
                "Summarize the document in 3 concise bullet points."
            )
        },
        {
            "role": "user",
            "content": content[:4000]
        }
    ]
)
```

The runtime limits the input to the first 4000 characters:

```python
"content": content[:4000]
```

This keeps the initial workflow simple and avoids sending very large files to the model.

## Rebuild Hermes

Rebuild the Hermes container:

```bash
cd ~/dgx-hermes-agent/compose
docker compose build hermes
```

Restart the runtime:

```bash
docker compose up -d
```

Follow the Hermes logs:

```bash
docker logs -f hermes
```

Expected startup output:

```text
[Hermes Agent] Starting workspace watcher...
[Hermes Agent] Monitoring: /workspace/inbox
```

## Validate AI Summarization

Create a new file in another terminal. Write the file outside the inbox first, then move it into `workspace/inbox/` so Hermes sees a completed file.

```bash
cat > /tmp/ai-runtime-note.txt <<'EOF'
Persistent AI systems are not only prompt-response applications.
They run as long-lived local services that monitor events, coordinate
runtime workflows, store memory, and use GPU acceleration when model
inference is required.
EOF

mv /tmp/ai-runtime-note.txt \
~/dgx-hermes-agent/workspace/inbox/ai-runtime-note.txt
```

Return to the Hermes logs. You should see output similar to:

```text
[Agent] New file detected:
/workspace/inbox/ai-runtime-note.txt

[Agent] Running local inference...

[Agent] AI Summary:
- Persistent AI systems function beyond simple prompt-response interactions, operating as ongoing local services.
- These systems monitor events, manage workflows, and maintain stored memory for extended periods.
- They utilize GPU acceleration during model inference to enhance performance.
```

The generated summary text will vary because it is produced by the local model.

## Verify GPU-accelerated Inference

To observe GPU activity during inference, use two terminals.

In terminal 1, follow Hermes logs:

```bash
docker logs -f hermes
```

In terminal 2, schedule a new file to be created after a short delay, then start `nvtop` immediately:

```bash
(
sleep 5
cat > /tmp/gpu-inference-test.txt <<'EOF'
DGX Spark combines Arm CPU orchestration with NVIDIA GPU acceleration.
The CPU coordinates persistent services, while the GPU accelerates local
language model inference and summarization workloads.
EOF

mv /tmp/gpu-inference-test.txt \
~/dgx-hermes-agent/workspace/inbox/gpu-inference-test.txt
) &
nvtop
```

The background command creates the file after five seconds, giving `nvtop` time to start before Ollama begins inference. During summarization, `nvtop` should show activity from the Ollama container or model runtime. This confirms that the GPU is accelerating local inference while Hermes coordinates the workflow.

## Runtime Responsibilities

The runtime now has a clear separation of responsibilities.

Hermes is responsible for:

- Filesystem monitoring
- Reading workspace files
- Preparing prompts
- Calling the Ollama API
- Printing runtime logs
- Coordinating the workflow lifecycle

Ollama is responsible for:

- Loading the local model
- Running token generation
- Returning the generated summary

## CPU and GPU Responsibilities

The Arm Grace CPU coordinates the workflow:

- Watches the workspace
- Receives filesystem events
- Reads file content
- Prepares model requests
- Sends API calls to Ollama
- Logs runtime progress

The Blackwell GPU accelerates the model workload:

- Local LLM inference
- Token generation
- AI summarization

This pattern is repeated throughout the Learning Path. Hermes orchestrates; Ollama executes model inference.

## Summary

You extended Hermes with ***local LLM inference*** through the Ollama Python SDK and the `OLLAMA_HOST` runtime setting. New files in the workspace can now trigger summarization with `qwen2.5:7b`, and GPU activity can be validated with `nvtop`.

The runtime has moved from simple file detection to ***event-driven AI summarization***.

Next, you will add persistent semantic memory with embeddings and Qdrant.
