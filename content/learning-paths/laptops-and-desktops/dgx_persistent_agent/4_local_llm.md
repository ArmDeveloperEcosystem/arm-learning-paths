---
title: Add local LLM inference to the Hermes Agent
weight: 5
layout: "learningpathall"
---

## Connect Hermes Agent to Ollama

In this section, you'll connect Hermes Agent to Ollama.

This step turns Hermes from a file watcher into an inference orchestrator. Hermes still controls the workflow, but it now sends document content to Ollama and uses the model response as part of the runtime output.

The runtime already watches `workspace/inbox/` and reacts when a file is created. You'll now extend that workflow so Hermes sends file content to a local language model and prints an AI-generated summary.

The workflow becomes:

```output
workspace/inbox document
    -> Hermes on_created() handler
    -> Hermes calls Ollama
    -> Local LLM summary
```

This introduces the first GPU-accelerated step in the persistent runtime.

### Configure Ollama runtime access

Hermes reaches Ollama through the Docker Compose network.

In the Hermes Compose service, you added this environment variable earlier:

```output
environment:
  - OLLAMA_HOST=http://ollama:11434
```

Inside the Docker network, the service name `ollama` resolves to the Ollama container. Hermes uses this URL when it creates the Ollama Python client.

Verify that the Ollama container is running:

```bash
cd ~/dgx-hermes-agent/compose
docker ps
```

You should see both `ollama` and `hermes` running.

### Verify the local language model

You pulled `qwen2.5:7b` when you built the runtime foundation. Run an inference test to confirm that the model is still available inside the Ollama container:

```bash
docker exec -it ollama ollama run qwen2.5:7b
```

Enter a short prompt:

```text
Summarize persistent AI runtimes in one sentence.
```

Type `/bye` to exit the model session.

### Add inference support to Hermes

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

#### Understand the code trace

The updated agent imports the `ollama` package and reads `OLLAMA_HOST` from the container environment, with `http://ollama:11434` as the fallback. An `ollama.Client` is created at startup so the connection is ready before any files arrive.

When a new file is detected, `summarize_file()` sends the content to `qwen2.5:7b` using the chat API with a system prompt that requests a three-point bullet summary. The input is capped at 4000 characters to keep requests manageable and avoid sending very large files to the model.

### Rebuild Hermes to connect to Ollama

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

```output
[Hermes Agent] Starting workspace watcher...
[Hermes Agent] Monitoring: /workspace/inbox
```

Leave this terminal open with the log stream running and open a second terminal for the next step.

## Validate Hermes connection to Ollama

After rebuilding Hermes, verify that it's connected to Ollama as expected.

### Validate AI summarization

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

Return to terminal 1 to see the Hermes log output. You should see output similar to:

```output
[Agent] New file detected:
/workspace/inbox/ai-runtime-note.txt

[Agent] Running local inference...

[Agent] AI Summary:
- Persistent AI systems function beyond simple prompt-response interactions, operating as ongoing local services.
- These systems monitor events, manage workflows, and maintain stored memory for extended periods.
- They utilize GPU acceleration during model inference to enhance performance.
```

The generated summary text will vary because it is produced by the local model.

### Verify GPU-accelerated inference

To observe GPU activity during inference, keep terminal 1 open with the Hermes log stream running. In terminal 2, schedule a new file to be created after a short delay, then start `nvtop` immediately:

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

The background command creates the file after five seconds, giving `nvtop` time to start before Ollama begins inference. During summarization, `nvtop` should show GPU activity from the Ollama model runtime. Watch terminal 1 to see the Hermes log output as inference runs.

Press `q` to quit `nvtop` after reviewing the GPU activity.

## Understand CPU and GPU responsibilities

The Arm Grace CPU coordinates the full workflow: watching the workspace, handling filesystem events, reading files, preparing model requests, and sending API calls to Ollama. The Blackwell GPU accelerates the model workload, running LLM inference, generating tokens, and producing the summary. This pattern repeats throughout the Learning Path. Hermes orchestrates and Ollama executes.

## What you've accomplished and what's next

You've now extended Hermes with local LLM inference through the Ollama Python SDK and the `OLLAMA_HOST` runtime setting. New files in the workspace can now trigger summarization with `qwen2.5:7b`, and you can validate GPU activity with `nvtop`.

The runtime has moved from file detection to event-driven AI summarization.

Next, you'll add persistent semantic memory with embeddings and Qdrant.

Before moving to the next section, press `Ctrl+C` in terminal 1 to stop the Hermes log stream. In the next section, you'll rebuild the Hermes container and run `docker logs -f hermes` again.
