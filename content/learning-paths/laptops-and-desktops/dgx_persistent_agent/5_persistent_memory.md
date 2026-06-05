---
title: Build persistent semantic memory for Hermes Agent
description: Store Hermes Agent summaries and embeddings in Qdrant to create persistent semantic memory for workspace documents.
weight: 6
layout: "learningpathall"
---

## Update Hermes to add persistent memory

In this section, you'll add persistent semantic memory to Hermes Agent.

In the previous section, Hermes became an inference orchestrator: it watched the workspace, sent document content to Ollama, and printed an AI summary. You'll now extend this workflow so the summary and source content are no longer just log output. Hermes will encode the document as an embedding and store it in Qdrant as reusable memory.

The runtime can already monitor files and generate summaries with a local language model. You'll now generate embeddings for workspace content and store them in Qdrant.

The workflow becomes:

```text
workspace/inbox document
    -> Hermes summarizes with Ollama
    -> Hermes generates embedding
    -> Hermes stores vector + payload in Qdrant
    -> persistent semantic memory
```

Adding persistent memory turns Hermes from an event-driven summarizer into a local AI runtime with long-term memory.

### Understand persistent memory architecture

Semantic memory uses vector embeddings to represent document meaning. The memory pipeline spans three services:

| Component | Responsibility |
|---|---|
| Hermes Agent | Orchestrates ingestion, summaries, embeddings, and storage |
| Ollama | Generates summaries and embeddings |
| Qdrant | Stores vectors and metadata as persistent memory |

The fixed embedding configuration is:

| Component | Value |
|---|---|
| Embedding model | `nomic-embed-text` |
| Vector dimension | `768` |
| Qdrant collection | `workspace_memory` |
| Distance metric | Cosine |

The vector dimension must match the output size of the embedding model. For `nomic-embed-text`, the collection is created with a vector size of `768`.

For example, a document about CPU orchestration is first summarized by `qwen2.5:7b`. Hermes then sends the same document text to `nomic-embed-text`, receives a 768-dimensional embedding, and stores that vector in Qdrant with metadata. Metadata includes the file path, generated summary, and source content excerpt. Later, a query about "runtime scheduling" can retrieve this memory even if the document does not contain the exact same words.

### Pull the embedding model

Open a shell in the Ollama container:

```bash
docker exec -it ollama bash
```

Pull the embedding model:

```bash
ollama pull nomic-embed-text
```

Exit the container:

```bash
exit
```

The embedding model converts text into vectors. Qdrant stores those vectors and uses them later for semantic retrieval.

### Update the Hermes agent

Open and edit the file `~/dgx-hermes-agent/hermes/agent.py`.

Replace the file with the following version:

```python
import os
import uuid
import time
import ollama

from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

WATCH_DIR = "/workspace/inbox"

SUPPORTED_EXTENSIONS = [
    ".txt",
    ".md",
    ".log"
]

OLLAMA_HOST = os.getenv(
    "OLLAMA_HOST",
    "http://ollama:11434"
)

QDRANT_HOST = os.getenv(
    "QDRANT_HOST",
    "qdrant"
)

COLLECTION_NAME = "workspace_memory"

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

class WorkspaceHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return

        filename = os.path.basename(event.src_path)
        if filename.startswith("."):
            return

        ext = os.path.splitext(filename)[1]
        if ext not in SUPPORTED_EXTENSIONS:
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
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
```

#### Understand the code trace

Hermes connects to Qdrant using the Docker service name `qdrant`, read from the `QDRANT_HOST` environment variable with a default fallback. On startup, `ensure_collection()` creates the `workspace_memory` collection if it doesn't already exist, configured with a vector size of 768 and cosine distance to match the `nomic-embed-text` model output.

When a file is detected, `process_file()` calls `generate_summary()` and then `generate_embedding()` in sequence. The embedding uses `client.embed()` from the current Ollama Python SDK, and the result is read from `response["embeddings"][0]`. Hermes stores each document as a Qdrant `PointStruct` with the vector and a payload containing the file path, generated summary, and source content excerpt. The payload makes sure that future retrieval results include the document context needed to answer workspace queries.

#### Understand runtime filtering

The agent filters incoming files before processing. Only `.txt`, `.md`, and `.log` files are handled. Files whose names start with `.` are skipped, which avoids processing hidden files and temporary files created by editors or the operating system.

#### Understand runtime compatibility considerations

Use the Ollama embedding API inside the `generate_embedding()` function:

```python
client.embed(...)
```

Read the embedding from the `embeddings` list returned by Ollama:

```python
response["embeddings"][0]
```

Don't use older examples that call:

```python
client.embeddings(...)
```

The Qdrant vector dimension must match the embedding model output size. For this Learning Path, use `768` with `nomic-embed-text`.

This dimension is configured in `ensure_collection()`:

```python
vectors_config=VectorParams(
    size=768,
    distance=Distance.COSINE
)
```

If you change the embedding model later, update the Qdrant collection dimension to match the new model output. If the dimensions don't match, Qdrant will reject the inserted vectors.

### Rebuild Hermes

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

Leave this terminal open with the log stream running and open a second terminal for the next step.

On first startup, the output is similar to:

```output
[Memory] Created collection: workspace_memory
[Hermes Agent] Starting workspace watcher...
[Hermes Agent] Monitoring: /workspace/inbox
```
## Validate persistent semantic memory

After updating the Hermes Agent and rebuilding it to add persistent semantic memory, verify that the memory has been added as expected.

### Validate memory ingestion

In the second terminal, create a new document. Write it outside the inbox first, then move the completed file into `workspace/inbox/` so Hermes processes a fully written document.

```bash
cat > /tmp/memory-test.txt <<'EOF'
Persistent AI runtimes need memory so that previous workspace activity
can influence future reasoning. Semantic memory stores embeddings and
metadata so the runtime can retrieve relevant context later.
EOF

mv /tmp/memory-test.txt \
~/dgx-hermes-agent/workspace/inbox/memory-test.txt
```

Watch the first terminal running Hermes logs for the Hermes log output. 

The memory ingestion output is similar to:

```output
[Agent] New file detected:
/workspace/inbox/memory-test.txt

[Agent] Running summarization inference...

[Agent] AI Summary:
- Persistent AI runtimes require memory to incorporate past workspace activities into future reasoning.
- Semantic memory in AI systems retains embeddings and metadata to store relevant context.
- This stored information allows for retrieval of pertinent context, enhancing the runtime's ability to reason effectively.
```
The summary text will vary because it is generated by the local model.

The log stream output is similar to:

```output
[Agent] Generating embeddings...
[Memory] Stored document: /workspace/inbox/memory-test.txt
```

### Verify Qdrant memory

Open the Qdrant dashboard:

```text
http://localhost:6333/dashboard
```

Confirm that the `workspace_memory` collection exists:

![Qdrant dashboard showing the workspace_memory collection, confirming that Hermes created the collection#center](qdrant_dashboard_2.png "Qdrant Dashboard")

The dashboard shows the `workspace_memory` collection after Hermes starts and runs `ensure_collection()`. If the collection doesn't appear, check the Hermes logs for Qdrant connection errors and confirm that the `qdrant` container is running.

Open the collection and verify that points are being stored. Each point represents one ingested workspace document and contains:

- A 768-dimensional vector
- A `path` payload field
- A `summary` payload field
- A `content` payload field

![Qdrant workspace_memory collection showing stored vectors and payload fields#center](qdrant_dashboard_3.png "Qdrant workspace_memory vector and payload view")

Use this view to confirm that Qdrant has stored both the vector and payload metadata. The payload fields are important because later retrieval steps need the path and summary to assemble useful context for the LLM.

You can also inspect collection storage and memory usage:

![Qdrant collection storage view showing persistent memory usage#center](qdrant_dashboard_4.png "Qdrant workspace_memory memory usage view")

The memory usage view confirms that Qdrant is maintaining persistent collection state on disk. This matters because the vector memory survives container restarts as long as the `../qdrant:/qdrant/storage` volume remains mounted.

You can also inspect collections from the host:

```bash
curl http://localhost:6333/collections
```

The output is similar to:

```output
{"result":{"collections":[{"name":"workspace_memory"}]},"status":"ok","time":0.0001}
```

## Understand CPU and GPU responsibilities

The Arm Grace CPU coordinates the full memory pipeline: detecting new files, filtering by extension, reading content, calling Ollama for summaries and embeddings, creating and upserting Qdrant collections, and keeping the long-running runtime active.

The Blackwell GPU accelerates the model workloads, running summary generation with `qwen2.5:7b` and embedding generation with `nomic-embed-text`. Qdrant stores the results as persistent memory.

## What you've accomplished and what's next

You've now added persistent semantic memory to Hermes Agent by connecting it to Qdrant, creating the `workspace_memory` collection, generating local embeddings with Ollama, and storing vectors with document metadata.

The runtime can now ingest documents, summarize them, generate embeddings, and preserve that context as persistent vector memory.

Next, you'll add semantic retrieval and contextual question answering.

Before moving to the next section, press `Ctrl+C` in the first terminal running Hermes logs to stop the Hermes log stream. In the next section, you'll rebuild the Hermes container and run `docker logs -f hermes` again.
