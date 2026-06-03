---
title: Add semantic retrieval and contextual reasoning
weight: 7
layout: "learningpathall"
---

## Add semantic retrieval and contextual reasoning

In this section, you will add semantic retrieval to Hermes Agent.

In the previous section, Hermes stored document summaries, embeddings, and metadata in Qdrant. This section turns that stored memory into an active reasoning source: Hermes will accept a question, retrieve relevant memories, assemble them as context, and send that context to the local model.

The runtime can already ingest documents, summarize them, generate embeddings, and store semantic memory in Qdrant. You will now add a query workflow so Hermes can search memory and use retrieved context to answer questions.

The workflow becomes:

```output
/workspace/query.txt
    -> Hermes embeds the question
    -> Qdrant returns relevant memories
    -> Hermes assembles context
    -> Ollama generates a grounded answer
```

This is the first stage where Hermes uses memory as reasoning context instead of only storing it.

## Contextual retrieval architecture

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

## Add retrieval functions to Hermes

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

## Code trace

`search_memory()` embeds the user question with `generate_embedding()`, then calls `qdrant.query_points()` with `query=embedding` to retrieve the three closest semantic matches. Each result's payload is read from `result.payload`, and the path and summary are assembled into a list of memories.

`query_workspace()` joins those memories into a context string, then sends both the original question and the assembled context to `qwen2.5:7b` using the chat API. The model receives prior workspace memory as part of the prompt, so its answer is grounded in ingested documents rather than general knowledge.

The main runtime loop checks for `/workspace/query.txt` on each iteration. When the file exists, Hermes reads the question, deletes the file immediately to avoid re-processing, and calls `query_workspace()`.

## Runtime compatibility notes

Use `qdrant.query_points()` with `query=embedding` when calling the vector search API. Older examples use `query_vector=embedding`, which is not compatible with current versions of the Qdrant Python client. Read each result's payload with `result.payload` before assembling the retrieval context.

The `limit=3` value in `search_memory()` is hardcoded to keep the retrieval behavior easy to inspect. You can make it configurable later.

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

Leave this terminal open with the log stream running and open a second terminal for the next step.

Expected startup output:

```output
[Hermes Agent] Starting workspace watcher...
[Hermes Agent] Monitoring: /workspace/inbox
```

## Create test memory

In terminal 2, create a few new documents so Qdrant contains useful semantic memory.

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

Watch terminal 1 until each document is summarized, embedded, and stored.

The expected output is similar to:

```output
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

## Test semantic retrieval

In terminal 2, create a query file:

```bash
echo "How do CPUs help persistent AI systems?" \
> ~/dgx-hermes-agent/workspace/query.txt
```

Hermes checks for `/workspace/query.txt` in the runtime loop. When it sees the file, it reads the question, removes the file, embeds the question, searches Qdrant, and sends the retrieved context to Ollama.

In terminal 1, confirm that semantic search started:

```output
[Memory] Searching semantic memory...
```

Then confirm that Hermes printed the question and the retrieved memory context:

```output
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

```output
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

## Verify contextual reasoning

In terminal 2, ask a second question:

```bash
echo "Why does the runtime need semantic memory?" \
> ~/dgx-hermes-agent/workspace/query.txt
```

Hermes embeds the question, Qdrant retrieves relevant summaries, Hermes assembles those summaries into context, and Ollama generates an answer grounded in the retrieved memory.

The logs should include a retrieved memory from the semantic memory document you created earlier.

The output is similar to:

```output
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

## Retrieval workflow

The full retrieval workflow is:

```output
query.txt question
    -> Ollama query embedding
    -> Qdrant workspace_memory search
    -> retrieved summaries
    -> Hermes context prompt
    -> Ollama contextual response
    -> Hermes log output
```

This creates a local contextual reasoning loop using persistent memory.

## CPU and GPU responsibilities

The Arm Grace CPU coordinates the retrieval workflow: watching for `query.txt`, reading and deleting the query file, calling Ollama for the query embedding, searching Qdrant for relevant memories, parsing result payloads, assembling the retrieved context, and calling Ollama again for contextual reasoning.

The Blackwell GPU accelerates query embedding generation, contextual LLM inference, and response generation. Qdrant performs the vector similarity search and returns the most relevant memory payloads.

## Summary

Before moving to the next section, press `Ctrl+C` in terminal 1 to stop the Hermes log stream. The next section rebuilds the Hermes container and runs `docker logs -f hermes` again.

You added semantic retrieval and contextual reasoning to Hermes Agent. The runtime now turns a question into an embedding, searches Qdrant with `query_points(...)`, assembles retrieved memory, and sends that context to `qwen2.5:7b`.

The runtime can now store memory and reason over it through the local `/workspace/query.txt` workflow.

Next, you will add autonomous workspace cognition.
