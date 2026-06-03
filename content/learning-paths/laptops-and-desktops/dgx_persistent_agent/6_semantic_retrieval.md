---
title: Add Semantic Retrieval and Contextual Reasoning
weight: 7
layout: "learningpathall"
---

## Add Semantic Retrieval and Contextual Reasoning

In this section, you will add ***semantic retrieval*** to Hermes Agent.

In the previous section, Hermes stored document summaries, embeddings, and metadata in Qdrant. This section turns that stored memory into an active reasoning source: Hermes will accept a question, retrieve relevant memories, assemble them as context, and send that context to the local model.

The runtime can already ingest documents, summarize them, generate embeddings, and store semantic memory in Qdrant. You will now add a ***query workflow*** so Hermes can search memory and use retrieved context to answer questions.

The workflow becomes:

```text
/workspace/query.txt
    -> Hermes embeds the question
    -> Qdrant returns relevant memories
    -> Hermes assembles context
    -> Ollama generates a grounded answer
```

This is the first stage where Hermes uses memory as reasoning context instead of only storing it.

## Contextual Retrieval Architecture

The retrieval pipeline uses all three runtime services:

| Component | Responsibility |
|---|---|
| Hermes Agent | Detects queries, generates query embeddings, assembles context |
| Ollama | Generates embeddings and contextual answers |
| Qdrant | Searches stored semantic memory |

The runtime keeps the same fixed memory configuration:

| Component | Value |
|---|---|
| Embedding model | `nomic-embed-text` |
| Vector dimension | `768` |
| Qdrant collection | `workspace_memory` |
| Retrieval limit | `3` |

Hermes will watch for a query file at:

```text
/workspace/query.txt
```

When the file exists, Hermes reads the question, deletes the query file, searches memory, and prints the answer in the container logs.

## Add Retrieval Functions to Hermes

Open and edit the file `~/dgx-hermes-agent/hermes/agent.py`.

Replace the file with the following version:

```python
import os
import uuid
import time
import ollama

from qdrant_client import QdrantClient
from qdrant_client.models import (
    Distance,
    VectorParams,
    PointStruct
)

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

The `search_memory()` function converts the user question into an embedding:

```python
embedding = generate_embedding(query)
```

It searches Qdrant using the current Qdrant Python client API:

```python
results = qdrant.query_points(
    collection_name=COLLECTION_NAME,
    query=embedding,
    limit=3
).points
```

The current API uses `query=embedding`. Do not use older examples that pass `query_vector=embedding`.

Qdrant returns scored point objects. Hermes reads the payload from each result:

```python
payload = result.payload
```

Only the path and summary are assembled into the retrieval context:

```python
memories.append({
    "path": payload.get("path"),
    "summary": payload.get("summary")
})
```

The context is converted into a prompt:

```python
context = "\n\n".join([
    f"Document: {m['path']}\nSummary:\n{m['summary']}"
    for m in memories
])
```

Hermes sends the question and retrieved memory to the local model:

```python
f"Question:\n{question}\n\n"
f"Relevant workspace memory:\n{context}"
```

The runtime loop checks for a query file:

```python
if os.path.exists("/workspace/query.txt"):
```

After reading the question, Hermes removes the query file:

```python
os.remove("/workspace/query.txt")
```

This makes query processing event-like while keeping the runtime simple and local.

## Runtime Compatibility Notes

The compatibility details in this section apply to the retrieval code you added in `search_memory()` and `query_workspace()`. The embedding API and vector dimension were covered in the previous section, so this section focuses on the Qdrant retrieval call and result parsing.

Use the current Qdrant semantic retrieval API inside `search_memory()`:

```python
results = qdrant.query_points(
    collection_name=COLLECTION_NAME,
    query=embedding,
    limit=3
).points
```

The current Qdrant client expects the query vector in the `query` argument. Do not use older examples that pass `query_vector=embedding`.

Qdrant returns scored point objects. Read each payload from `result.payload` before assembling the context:

```python
for result in results:
    payload = result.payload
```

In this section, `limit=3` is intentionally hardcoded in `search_memory()` so the retrieval behavior is easy to inspect. Later, runtime policy can make this value configurable.

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

## Create Test Memory

Before testing retrieval, create a few new documents so Qdrant contains useful semantic memory.

For each document, write the file in `/tmp` first and then move it into `workspace/inbox/`. This gives Hermes a completed file when the `on_created()` event fires.

Create a document about CPU orchestration:

```bash
cat > /tmp/cpu-orchestration-note.txt <<'EOF'
Arm CPUs are responsible for orchestration in persistent AI runtimes.
They coordinate filesystem events, runtime scheduling, container services,
document parsing, metadata handling, and vector database operations.
EOF

mv /tmp/cpu-orchestration-note.txt \
~/dgx-hermes-agent/workspace/inbox/cpu-orchestration-note.txt
```

Create a document about GPU inference:

```bash
cat > /tmp/gpu-inference-note.txt <<'EOF'
NVIDIA GPUs accelerate local model inference, token generation,
summarization, embedding generation, and contextual reasoning workloads.
EOF

mv /tmp/gpu-inference-note.txt \
~/dgx-hermes-agent/workspace/inbox/gpu-inference-note.txt
```

Create a document about semantic memory:

```bash
cat > /tmp/semantic-memory-note.txt <<'EOF'
Semantic memory stores embeddings and metadata in a vector database.
This allows persistent AI systems to retrieve relevant prior context
based on meaning instead of exact keyword matching.
EOF

mv /tmp/semantic-memory-note.txt \
~/dgx-hermes-agent/workspace/inbox/semantic-memory-note.txt
```

Watch the Hermes logs until each document is summarized, embedded, and stored.

Expected log lines include:

```text
[Agent] New file detected:
/workspace/inbox/cpu-orchestration-note.txt

[Agent] Running summarization inference...

[Agent] AI Summary:
- Arm CPUs handle orchestration in persistent AI runtimes.
- They manage filesystem events, runtime scheduling, and container services.
- Tasks also include document parsing, metadata handling, and vector database operations.

[Agent] Generating embeddings...
[Memory] Stored document: /workspace/inbox/cpu-orchestration-note.txt

[Agent] New file detected:
/workspace/inbox/gpu-inference-note.txt

[Agent] Running summarization inference...

[Agent] AI Summary:
- NVIDIA GPUs speed up local model inference processes.
- These GPUs enhance token generation, summarization, and embedding generation tasks.
- They also improve contextual reasoning workloads locally.

[Agent] Generating embeddings...
[Memory] Stored document: /workspace/inbox/gpu-inference-note.txt

[Agent] New file detected:
/workspace/inbox/semantic-memory-note.txt

[Agent] Running summarization inference...

[Agent] AI Summary:
- Semantic memory uses a vector database to store embeddings and metadata.
- This enables persistent AI systems to recall relevant past contexts based on meaning.
- The system avoids relying solely on exact keyword matching for retrieval.

[Agent] Generating embeddings...
[Memory] Stored document: /workspace/inbox/semantic-memory-note.txt
```

## Test Semantic Retrieval

Create a query file:

```bash
echo "How do CPUs help persistent AI systems?" \
> ~/dgx-hermes-agent/workspace/query.txt
```

Hermes checks for `/workspace/query.txt` in the runtime loop. When it sees the file, it reads the question, removes the file, embeds the question, searches Qdrant, and sends the retrieved context to Ollama.

In the Hermes logs, first confirm that semantic search started:

```text
[Memory] Searching semantic memory...
```

Next, confirm that Hermes printed the question and the retrieved memory context:

```text
[Workspace Query]
How do CPUs help persistent AI systems?

[Retrieved Memories]
Document: /workspace/inbox/cpu-orchestration-note.txt
Summary:
- Arm CPUs manage orchestration in persistent AI runtimes.
- They handle filesystem events, runtime scheduling, and container services.
- Additionally, they process document parsing, metadata handling, and vector database operations.

Document: /workspace/inbox/cpu-orchestration-note.txt
Summary:
- Arm CPUs handle orchestration in persistent AI runtimes.
- They manage filesystem events, runtime scheduling, and container services.
- Tasks also include document parsing, metadata handling, and vector database operations.

Document: /workspace/inbox/semantic-memory-note.txt
Summary:
- Semantic memory uses a vector database to store embeddings and metadata.
- This enables persistent AI systems to recall relevant past context based on meaning.
- Retrieval is done without relying solely on exact keyword matching.
```

Finally, confirm that Ollama generated a response from the retrieved context:

```text
[AI Response]
In persistent AI systems, CPUs play a crucial role in managing orchestration tasks that are essential for the system's operation. Specifically, Arm CPUs handle several key responsibilities:

1. **Orchestration Management**: They manage the overall orchestration of the runtime environment.
2. **Filesystem Events Handling**: CPU processes and responds to events related to file systems within the AI system.
3. **Runtime Scheduling**: They schedule tasks and processes based on current needs and resource availability.
4. **Container Services**: CPUs handle services running in containers, ensuring that these components operate efficiently.

Furthermore, Arm CPUs are involved in processing various data-related operations:
- **Document Parsing**: This involves breaking down documents into manageable chunks for further analysis or storage.
- **Metadata Handling**: They manage the creation and manipulation of metadata associated with data entities.
- **Vector Database Operations**: These include storing embeddings and metadata in vector databases, which is critical for semantic memory systems. Vector databases allow persistent AI systems to recall relevant past context based on meaning rather than exact keyword matching.

These functions collectively ensure that CPUs are central to maintaining the functionality and efficiency of persistent AI systems by managing both operational tasks and data processing needs.
```

The exact answer will vary, but it should refer to retrieved memory about CPU orchestration, filesystem events, scheduling, and runtime coordination.

## Verify Contextual Reasoning

Ask a second question:

```bash
echo "Why does the runtime need semantic memory?" \
> ~/dgx-hermes-agent/workspace/query.txt
```

Expected behavior:

- Hermes embeds the question
- Qdrant retrieves relevant summaries
- Hermes assembles the retrieved summaries into context
- Ollama generates an answer grounded in that context

The logs should include a retrieved memory from the semantic memory document you created earlier.

Example output:

```text
[Memory] Searching semantic memory...

[Workspace Query]
Why does the runtime need semantic memory?

[Retrieved Memories]
Document: /workspace/inbox/memory-test.txt
Summary:
- Persistent AI runtimes require memory to incorporate past workspace activities into future reasoning.
- Semantic memory in AI systems retains embeddings and metadata to store relevant context.
- This stored information allows for retrieval of pertinent context, enhancing the runtime's ability to reason effectively.

Document: /workspace/inbox/semantic-memory-note.txt
Summary:
- Semantic memory uses a vector database to store embeddings and metadata.
- This enables persistent AI systems to recall relevant past context based on meaning.
- Retrieval is done without relying solely on exact keyword matching.

Document: /workspace/inbox/semantic-memory-note.txt
Summary:
- Semantic memory uses a vector database to store embeddings and metadata.
- This enables persistent AI systems to recall relevant past contexts based on meaning.
- The system avoids relying solely on exact keyword matching for retrieval.

[AI Response]
The runtime needs semantic memory because it retains embeddings and metadata that store relevant context from past workspace activities. This allows the system to effectively reason by retrieving pertinent information, enhancing its ability to understand and respond to new inputs more intelligently. Unlike simple keyword matching, semantic memory uses a vector database which captures the meaning of words or concepts, enabling more accurate and contextualized recall of past events or knowledge.
```

## Retrieval Workflow

The full retrieval workflow is:

```text
query.txt question
    -> Ollama query embedding
    -> Qdrant workspace_memory search
    -> retrieved summaries
    -> Hermes context prompt
    -> Ollama contextual response
    -> Hermes log output
```

This creates a local contextual reasoning loop using persistent memory.

## CPU and GPU Responsibilities

The Arm Grace CPU coordinates retrieval:

- Watches for `query.txt`
- Reads and deletes the query file
- Calls Ollama for query embeddings
- Calls Qdrant for vector search
- Parses Qdrant result payloads
- Assembles retrieved context
- Calls Ollama for contextual reasoning

The Blackwell GPU accelerates:

- Query embedding generation
- Contextual LLM inference
- Response generation

Qdrant performs the vector similarity search and returns the most relevant memory payloads.

## Summary

You added ***semantic retrieval*** and ***contextual reasoning*** to Hermes Agent. The runtime now turns a question into an embedding, searches Qdrant with `query_points(...)`, assembles retrieved memory, and sends that context to `qwen2.5:7b`.

The runtime can now store memory and reason over it through the local `/workspace/query.txt` workflow.

Next, you will add autonomous workspace cognition.
