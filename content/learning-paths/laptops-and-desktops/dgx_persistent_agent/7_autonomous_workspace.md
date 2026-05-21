---
title: Add Autonomous Workspace Cognition
weight: 8
layout: "learningpathall"
---

## Add Autonomous Workspace Cognition

In this section, you will add ***autonomous workspace cognition*** to Hermes Agent.

In the previous section, Hermes could answer a question by retrieving relevant memory on demand. This section adds proactive behavior: Hermes will periodically review stored workspace memory, identify recurring themes, and write a summary without waiting for a user query.

For example, if the workspace contains notes about CPU orchestration, GPU inference, and semantic memory, Hermes can generate a scheduled workspace summary that explains those themes and how they relate to the current local AI runtime.

The runtime can already ingest documents, build semantic memory, and answer questions using retrieved context. You will now add a ***periodic cognition workflow*** that reviews stored memory and generates a workspace-level summary.

The workflow becomes:

```text
stored workspace memory
    -> scheduled cognition loop
    -> Hermes aggregates summaries
    -> Ollama analyzes recurring themes
    -> workspace-summary.txt
```

This is the final stage of the Learning Path. Hermes becomes a persistent autonomous local AI runtime that can monitor, remember, retrieve, and periodically reason about workspace state.

## Autonomous Cognition Overview

Autonomous cognition means the runtime performs useful reasoning without waiting for a new document or explicit query.

Hermes will:

- Load runtime policy from `/workspace/config/runtime.json`
- Continue watching `workspace/inbox/`
- Continue ingesting supported files into semantic memory
- Continue answering questions from `/workspace/query.txt`
- Periodically summarize the stored workspace memory
- Write the summary to `/workspace/memory/workspace-summary.txt`

The runtime remains local-first. Files, models, vector memory, and summaries stay on the DGX Spark system.

## Create the Runtime Config Directory

Create the configuration directory if it does not already exist:

```bash
mkdir -p ~/dgx-hermes-agent/workspace/config
```

Create and edit the file `~/dgx-hermes-agent/workspace/config/runtime.json`.

Add the following content:

```json
{
  "summary_interval_hours": 8,
  "supported_extensions": [
    ".txt",
    ".md",
    ".log"
  ],
  "retrieval_limit": 3,
  "summary_output": "/workspace/memory/workspace-summary.txt"
}
```

The policy file controls runtime behavior without rebuilding the container.

| Policy | Purpose |
|---|---|
| `summary_interval_hours` | Controls how often Hermes generates a workspace summary |
| `supported_extensions` | Controls which file types Hermes ingests |
| `retrieval_limit` | Records the intended semantic retrieval depth for the runtime policy |
| `summary_output` | Defines where Hermes writes the workspace summary |

The verified code in this section keeps semantic retrieval at `limit=3`, matching the policy value shown above. The policy file makes this setting visible for later hardening, where the retrieval function can load it dynamically.

## Add Autonomous Cognition to Hermes

Open and edit the file `~/dgx-hermes-agent/hermes/agent.py`.

Replace the file with the following version:

```python
import os
import json
import uuid
import time
import ollama

from datetime import datetime
from qdrant_client import QdrantClient
from qdrant_client.models import (
    Distance,
    VectorParams,
    PointStruct
)

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

WATCH_DIR = "/workspace/inbox"
CONFIG_PATH = "/workspace/config/runtime.json"
COLLECTION_NAME = "workspace_memory"

OLLAMA_HOST = os.getenv(
    "OLLAMA_HOST",
    "http://ollama:11434"
)
QDRANT_HOST = os.getenv(
    "QDRANT_HOST",
    "qdrant"
)

client = ollama.Client(host=OLLAMA_HOST)
qdrant = QdrantClient(
    host=QDRANT_HOST,
    port=6333
)

def ensure_collection():
    collections = qdrant.get_collections().collections
    names = [c.name for c in collections]
    if COLLECTION_NAME not in names:
        qdrant.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(
                size=768,
                distance=Distance.COSINE
            )
        )
        print(f"[Memory] Created collection: {COLLECTION_NAME}")

def load_runtime_config():
    with open(CONFIG_PATH, "r") as f:
        return json.load(f)

class WorkspaceHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        filename = os.path.basename(event.src_path)
        # Ignore hidden files
        if filename.startswith("."):
            return
        ext = os.path.splitext(filename)[1]
        config = load_runtime_config()
        supported_extensions = config.get(
            "supported_extensions",
            [".txt"]
        )
        if ext not in supported_extensions:
            return

        print(f"\n[Agent] New file detected:")
        print(event.src_path)
        process_file(event.src_path)

def generate_summary(content):
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
    return response["message"]["content"]

def generate_embedding(content):
    response = client.embed(
        model="nomic-embed-text",
        input=content[:4000]
    )
    return response["embeddings"][0]

def store_memory(path, content, summary, embedding):
    point_id = str(uuid.uuid4())
    qdrant.upsert(
        collection_name=COLLECTION_NAME,
        points=[
            PointStruct(
                id=point_id,
                vector=embedding,
                payload={
                    "path": path,
                    "summary": summary,
                    "content": content[:4000]
                }
            )
        ]
    )
    print(f"[Memory] Stored document: {path}")

def search_memory(query):
    print("\n[Memory] Searching semantic memory...")
    embedding = generate_embedding(query)
    results = qdrant.query_points(
        collection_name=COLLECTION_NAME,
        query=embedding,
        limit=3
    ).points

    memories = []
    for result in results:
        payload = result.payload
        memories.append({
            "path": payload.get("path"),
            "summary": payload.get("summary")
        })
    return memories

def query_workspace(question):
    memories = search_memory(question)
    context = "\n\n".join([
        f"Document: {m['path']}\nSummary:\n{m['summary']}"
        for m in memories
    ])
    response = client.chat(
        model="qwen2.5:7b",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a persistent AI workspace assistant. "
                    "Answer questions using the retrieved workspace memory."
                )
            },
            {
                "role": "user",
                "content": (
                    f"Question:\n{question}\n\n"
                    f"Relevant workspace memory:\n{context}"
                )
            }
        ]
    )
    answer = response["message"]["content"]
    print("\n[Workspace Query]")
    print(question)

    print("\n[Retrieved Memories]")
    print(context)

    print("\n[AI Response]")
    print(answer)

def generate_workspace_summary():
    print("\n[Cognition] Generating workspace summary...")
    results = qdrant.scroll(
        collection_name=COLLECTION_NAME,
        limit=10,
        with_payload=True
    )[0]
    summaries = []
    for result in results:
        payload = result.payload
        summaries.append(
            payload.get("summary", "")
        )
    combined = "\n\n".join(summaries)
    response = client.chat(
        model="qwen2.5:7b",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an autonomous workspace cognition agent. "
                    "Analyze the workspace summaries and identify "
                    "important recurring themes and insights."
                )
            },
            {
                "role": "user",
                "content": combined[:6000]
            }
        ]
    )
    workspace_summary = response["message"]["content"]
    config = load_runtime_config()
    output_path = config.get(
        "summary_output",
        "/workspace/memory/workspace-summary.txt"
    )
    with open(output_path, "w") as f:
        f.write(
            f"Workspace Summary\n"
            f"Generated: {datetime.now()}\n\n"
        )
        f.write(workspace_summary)
    print("\n[Cognition] Workspace summary updated:")
    print(output_path)

def process_file(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        print("\n[Agent] Running summarization inference...")
        summary = generate_summary(content)

        print("\n[Agent] AI Summary:")
        print(summary)

        print("\n[Agent] Generating embeddings...")
        embedding = generate_embedding(content)
        store_memory(
            path,
            content,
            summary,
            embedding
        )
    except Exception as e:
        print(f"[Agent] Error: {e}")

if __name__ == "__main__":
    print("\n[Hermes Agent] Starting workspace watcher...")
    print(f"[Hermes Agent] Monitoring: {WATCH_DIR}")

    ensure_collection()
    observer = Observer()
    observer.schedule(
        WorkspaceHandler(),
        WATCH_DIR,
        recursive=False
    )
    observer.start()
    last_summary_time = 0
    try:
        while True:
            time.sleep(5)
            config = load_runtime_config()
            summary_interval_hours = config.get(
                "summary_interval_hours",
                8
            )
            interval_seconds = (
                summary_interval_hours * 3600
            )
            current_time = time.time()

            # Periodic autonomous cognition
            if (
                current_time - last_summary_time
                > interval_seconds
            ):
                generate_workspace_summary()
                last_summary_time = current_time

            # Interactive semantic retrieval
            if os.path.exists("/workspace/query.txt"):
                with open("/workspace/query.txt", "r") as f:
                    question = f.read().strip()
                os.remove("/workspace/query.txt")
                query_workspace(question)

    except KeyboardInterrupt:
        observer.stop()
    observer.join()
```

## Code Trace

This version adds JSON configuration loading:

```python
CONFIG_PATH = "/workspace/config/runtime.json"
```

```python
def load_runtime_config():
    with open(CONFIG_PATH, "r") as f:
        return json.load(f)
```

File filtering now comes from runtime policy:

```python
config = load_runtime_config()

supported_extensions = config.get(
    "supported_extensions",
    [".txt"]
)
```

The cognition function reads stored memory from Qdrant:

```python
results = qdrant.scroll(
    collection_name=COLLECTION_NAME,
    limit=10,
    with_payload=True
)[0]
```

It extracts stored summaries:

```python
summaries.append(
    payload.get("summary", "")
)
```

It asks the local model to analyze recurring themes:

```python
"You are an autonomous workspace cognition agent. "
"Analyze the workspace summaries and identify "
"important recurring themes and insights."
```

It writes the result to the configured summary output path:

```python
output_path = config.get(
    "summary_output",
    "/workspace/memory/workspace-summary.txt"
)
```

The main loop reloads runtime policy every cycle:

```python
config = load_runtime_config()
```

This allows changes to `runtime.json` to affect runtime behavior without rebuilding the container.

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

Follow the logs:

```bash
docker logs -f hermes
```

On startup, the first cognition cycle runs immediately because `last_summary_time` starts at `0`.

Expected output:

```text
[Cognition] Generating workspace summary...
[Cognition] Workspace summary updated:
/workspace/memory/workspace-summary.txt
```

This startup behavior is expected and validates that the cognition pipeline can read memory, call Ollama, and write the summary file.

## Verify Workspace Summary Output

View the generated summary on the host:

```bash
cat ~/dgx-hermes-agent/workspace/memory/workspace-summary.txt
```

Expected structure:

```text
Workspace Summary
Generated: 2026-05-20 22:53:29.539079

### Recurring Themes and Insights:

1. **Semantic Memory in Persistent AI Systems:**
   - Semantic memory utilizes a vector database to store embeddings and metadata.
   - This approach allows for context-based retrieval rather than relying solely on exact keyword matching.
   - The system can recall relevant past contexts based on meaning, enhancing its reasoning capabilities.

2. **GPU Utilization:**
   - NVIDIA GPUs are crucial for speeding up local model inference processes.
   - They enhance tasks such as token generation, summarization, and embedding generation.
   - These GPUs also improve the performance of contextual reasoning workloads locally.

3. **Arm CPUs in Persistent AI Runtimes:**
   - Arm CPUs handle orchestration by managing various operational tasks including:
     - Filesystem events
     - Runtime scheduling
     - Container services
   - They also process document parsing, metadata handling, and vector database operations.
   - These tasks are essential for maintaining the overall functionality and efficiency of the persistent AI runtime.

### Summary:
The key insights from the workspace summaries revolve around how semantic memory enables context-based recall in AI systems, the role of NVIDIA GPUs in accelerating model inference tasks, and the multifaceted responsibilities of Arm CPUs in orchestrating various operational aspects of a persistent AI environment. These themes highlight the interdependence of different hardware components and their specific roles in enhancing the performance and effectiveness of AI systems.
```

The summary content will vary because it is generated by the local model from stored memory.

## Validate Event-Driven Ingestion

Create a new file. As in the previous sections, write it outside the inbox first and then move it into `workspace/inbox/` so Hermes reads a completed file.

```bash
cat > /tmp/autonomous-runtime-note.txt <<'EOF'
Autonomous workspace cognition allows a persistent AI runtime to analyze
stored memory on a schedule. This helps the system identify recurring
themes, summarize activity, and maintain awareness of workspace state.
EOF

mv /tmp/autonomous-runtime-note.txt \
~/dgx-hermes-agent/workspace/inbox/autonomous-runtime-note.txt
```

Expected Hermes logs:

```text
[Agent] New file detected:
/workspace/inbox/autonomous-runtime-note.txt

[Agent] Running summarization inference...

[Agent] AI Summary:
- Autonomous workspace cognition enables an ongoing AI analysis of stored data at scheduled intervals.
- The system uses this analysis to detect recurring themes and summarize activities within the workspace.
- It maintains scheduled awareness of workspace state from stored memory.

[Agent] Generating embeddings...
[Memory] Stored document: /workspace/inbox/autonomous-runtime-note.txt
```

The new document is added to semantic memory and can be included in future workspace summaries.

## Validate Semantic Retrieval Still Works

Autonomous cognition adds scheduling and workspace-level summaries, but it should not break the interactive retrieval workflow from the previous section. Validate semantic retrieval again to confirm that Hermes can still process `/workspace/query.txt` while the cognition loop is enabled.

Create a query:

```bash
echo "What is autonomous workspace cognition?" \
> ~/dgx-hermes-agent/workspace/query.txt
```

Expected logs:

```text
[Memory] Searching semantic memory...

[Workspace Query]
What is autonomous workspace cognition?

[Retrieved Memories]
Document: /workspace/inbox/autonomous-runtime-note.txt
Summary:
- Autonomous workspace cognition enables an ongoing AI analysis of stored data at scheduled intervals.
- The system uses this analysis to detect recurring themes and summarize activities within the workspace.
- It maintains scheduled awareness of workspace state from stored memory.

Document: /workspace/inbox/memory-test.txt
Summary:
- Persistent AI runtimes require memory to incorporate past workspace activities into future reasoning.
- Semantic memory in AI systems retains embeddings and metadata to store relevant context.
- This stored information allows for retrieval of pertinent context, enhancing the runtime's ability to reason effectively.

Document: /workspace/inbox/cpu-orchestration-note.txt
Summary:
- Arm CPUs manage orchestration in persistent AI runtimes.
- They handle filesystem events, runtime scheduling, and container services.
- Additionally, they process document parsing, metadata handling, and vector database operations.

[AI Response]
Autonomous workspace cognition is a feature that enables ongoing AI analysis of stored data at scheduled intervals. This system uses the analysis to detect recurring themes and summarize activities within the workspace. It maintains scheduled awareness from stored memory, allowing the runtime to reason over the information it has already ingested.
```

This confirms that autonomous cognition was added without removing the query workflow from the previous section.

## Validate Runtime Policy Reload

Runtime policy reload is important because persistent AI systems should be configurable without rebuilding containers or restarting the full stack. In this validation, you temporarily change the supported file extensions and confirm that Hermes applies the new policy during its normal runtime loop.

Open and edit the file `~/dgx-hermes-agent/workspace/config/runtime.json`.

Change the supported extensions so Hermes only ingests Markdown files:

```json
{
  "summary_interval_hours": 8,
  "supported_extensions": [
    ".md"
  ],
  "retrieval_limit": 3,
  "summary_output": "/workspace/memory/workspace-summary.txt"
}
```

Wait 5 to 10 seconds for the runtime loop to reload the policy.

Create a `.txt` file:

```bash
echo "This text file should be ignored by the current policy." \
> /tmp/ignored-policy-test.txt

mv /tmp/ignored-policy-test.txt \
~/dgx-hermes-agent/workspace/inbox/ignored-policy-test.txt
```

Hermes should not ingest it because `.txt` is no longer in `supported_extensions`.

Now create a Markdown file:

```bash
cat > /tmp/accepted-policy-test.md <<'EOF'
# Policy Test

This Markdown file should be ingested because the runtime policy allows
files with the .md extension.
EOF

mv /tmp/accepted-policy-test.md \
~/dgx-hermes-agent/workspace/inbox/accepted-policy-test.md
```

Expected logs:

```text
[Agent] New file detected:
/workspace/inbox/accepted-policy-test.md

[Agent] Running summarization inference...

[Agent] AI Summary:
- The document discusses key strategies for enhancing local business support through AI technologies.
- It highlights the importance of personalized customer experiences as enabled by advanced data analysis and machine learning techniques.
- Recommendations include integrating chatbots and virtual assistants to improve communication efficiency and customer service.
```

This validates that Hermes reloads runtime configuration dynamically.

Restore the original policy when you are done:

```json
{
  "summary_interval_hours": 8,
  "supported_extensions": [
    ".txt",
    ".md",
    ".log"
  ],
  "retrieval_limit": 3,
  "summary_output": "/workspace/memory/workspace-summary.txt"
}
```

## Trigger a Faster Cognition Cycle

For validation, you can temporarily reduce the summary interval.

Open and edit the file `~/dgx-hermes-agent/workspace/config/runtime.json`.

Set a very small interval:

```json
{
  "summary_interval_hours": 0.001,
  "supported_extensions": [
    ".txt",
    ".md",
    ".log"
  ],
  "retrieval_limit": 3,
  "summary_output": "/workspace/memory/workspace-summary.txt"
}
```

This is approximately 3.6 seconds. With this setting, Hermes repeatedly triggers the cognition loop after only a short pause. In the logs, you should see `[Cognition] Generating workspace summary...` and `[Cognition] Workspace summary updated:` appear again and again while the runtime is active.

This fast interval is useful for validation, but it is intentionally aggressive. Leave it enabled only long enough to confirm that scheduling works, then restore the interval to a larger value.

Follow the logs:

```bash
docker logs -f hermes
```

Expected output:

```text
[Cognition] Generating workspace summary...
[Cognition] Workspace summary updated:
```

Restore the interval to `8` after validation to avoid continuous summary generation:

```json
{
  "summary_interval_hours": 8,
  "supported_extensions": [
    ".txt",
    ".md",
    ".log"
  ],
  "retrieval_limit": 3,
  "summary_output": "/workspace/memory/workspace-summary.txt"
}
```

## Validate Persistent Runtime Lifecycle

Restart the stack:

```bash
cd ~/dgx-hermes-agent/compose
docker compose restart hermes
```

Follow the logs:

```bash
docker logs -f hermes
```

Expected output:

```text
[Hermes Agent] Starting workspace watcher...
[Hermes Agent] Monitoring: /workspace/inbox
```

The `workspace_memory` collection remains in Qdrant because the Qdrant storage directory is persisted on the host.

Verify that the summary file still exists:

```bash
ls ~/dgx-hermes-agent/workspace/memory/
```

You should see `workspace-summary.txt`.

This confirms that the runtime state persists across container restarts.

## Runtime Validation Summary

At this point, the local runtime supports:

| Capability | Status |
|---|---|
| Workspace monitoring | Complete |
| Local summarization | Complete |
| Embedding generation | Complete |
| Persistent vector memory | Complete |
| Semantic retrieval | Complete |
| Contextual reasoning | Complete |
| Autonomous workspace cognition | Complete |
| Dynamic runtime policy reload | Complete |

## CPU and GPU Responsibilities

The Arm Grace CPU coordinates the autonomous runtime:

- Filesystem monitoring
- Runtime policy loading
- Dynamic configuration reload
- Background scheduling
- Semantic memory aggregation
- Query workflow coordination
- Workspace summary lifecycle

The Blackwell GPU accelerates:

- Summarization
- Embedding generation
- Contextual reasoning
- Autonomous workspace analysis

The result is a heterogeneous local AI system where the CPU coordinates persistent workflows and the GPU accelerates model execution.

## Runtime Behavior Notes

The final runtime still uses the Ollama and Qdrant APIs introduced in the previous sections. The notes below focus on runtime behavior that is specific to autonomous cognition and policy-driven orchestration.

Runtime configuration is reloaded inside the main loop:

```python
config = load_runtime_config()
```

This means changes to `/workspace/config/runtime.json` can affect behavior without rebuilding the Hermes container. If the JSON file is malformed, Hermes will fail when it tries to reload the policy, so validate the file syntax after editing.

Workspace cognition reads stored memory using Qdrant `scroll(...)`:

```python
results = qdrant.scroll(
    collection_name=COLLECTION_NAME,
    limit=10,
    with_payload=True
)[0]
```

This is different from semantic search. `scroll(...)` is used here to collect recent stored summaries for workspace-level analysis, while `query_points(...)` is still used for question-driven semantic retrieval.

On startup, the first cognition cycle runs immediately because `last_summary_time` starts at `0`:

```python
last_summary_time = 0
```

This behavior is expected. It validates that Hermes can read memory, call Ollama, and write the configured summary output path.

The current implementation primarily handles file creation events through:

```python
on_created()
```

For validation, use new filenames. Existing files or file modifications may not trigger ingestion. File modification handling is a natural next improvement for a hardened runtime.

The `retrieval_limit` value is present in `runtime.json`, but the verified retrieval code in this section still uses `limit=3` inside `search_memory()`. Treat the policy value as a visible configuration placeholder for later hardening.

## Summary

You completed the ***persistent autonomous local AI runtime*** on DGX Spark. The finished system demonstrates how an Arm CPU can coordinate long-running AI workflows while a GPU accelerates summarization, embedding generation, contextual reasoning, and workspace-level cognition.

This Learning Path uses DGX Spark as the reference platform, but the architecture is reusable beyond this specific system. The same pattern can be adapted to other Arm platforms that can run containerized services, local inference backends, vector memory, and a CPU-side orchestration runtime.

The key idea is that persistent AI systems are ***distributed orchestration systems***, not just single inference calls. Hermes coordinates workspace ingestion, semantic memory, retrieval, autonomous summaries, and runtime policy, while the inference and memory services remain replaceable implementation choices.

This implementation is intentionally a minimal MVP. It validates the end-to-end architecture, but it does not yet handle production concerns such as repeated updates to the same file, deduplication, re-indexing, versioned memory records, or file modification events. Those hardening steps are natural extensions once the core runtime pattern is working.
