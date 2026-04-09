---
title: Generate and index vector embeddings
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Create vector embeddings from text

In this section, you generate vector embeddings from sample text data and store them in the **Qdrant vector database**.

Embeddings are numerical vector representations of data such as text, images, or audio. These vectors capture semantic meaning, allowing applications to perform similarity search and retrieve the most relevant results.

Using **Sentence Transformers**, you convert text into embeddings and store them in Qdrant for efficient vector indexing and retrieval.

## Architecture overview

The workflow focuses on embedding generation and vector storage.

```text
Text Documents
      |
      v
Sentence Transformer Model
      |
      v
Vector Embeddings
      |
      v
Qdrant Vector Database
      |
      v
Indexed Vectors Ready for Search
```

## Install Python libraries

Make sure the `qdrant-env` virtual environment is active before installing libraries. If you opened a new terminal, reactivate it:

```bash
source ~/qdrant-env/bin/activate
```

Install the Python libraries required for embedding generation and communication with the Qdrant API.

```bash
pip install qdrant-client sentence-transformers
```

These libraries provide:

- **qdrant-client** — Python interface for interacting with Qdrant
- **sentence-transformers** — pretrained transformer models for generating embeddings

## Create project directory

Create a working directory for the vector ingestion scripts.
```bash
mkdir qdrant-rag-demo
cd qdrant-rag-demo
```

The directory will contain the Python scripts used to generate embeddings and query the vector database.

## Create the ingestion script

**Create the Python file:**

```bash
vi ingest.py
```

**Add the following code:**

```python
from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance, PointStruct
from sentence_transformers import SentenceTransformer

client = QdrantClient(url="http://localhost:6333")

collection_name = "axion_demo"

client.recreate_collection(
    collection_name=collection_name,
    vectors_config=VectorParams(size=384, distance=Distance.COSINE),
)

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

documents = [
    "Axion processors provide Arm based cloud compute.",
    "Vector databases enable semantic search.",
    "Qdrant is optimized for vector similarity search.",
    "RAG pipelines combine retrieval with LLMs."
]

vectors = model.encode(documents)

points = [
    PointStruct(id=i, vector=vectors[i].tolist(), payload={"text": documents[i]})
    for i in range(len(documents))
]

client.upsert(collection_name=collection_name, points=points)

print("Documents indexed successfully in Qdrant")
```

### What this script does

The script performs several important operations:

- Connects to the Qdrant API
- Creates a vector collection
- Loads a transformer model for embeddings
- Converts text documents into vector embeddings
- Stores the vectors inside the Qdrant database

## Run the ingestion script

Execute the script to generate embeddings and store them in Qdrant.

```bash
python ingest.py
```
The output is similar to:
```output
Documents indexed successfully in Qdrant!
```

The output confirms that the vectors have been successfully inserted into the database.

## Verify the vector collection

Check that the vector collection exists in Qdrant.

```bash
curl http://localhost:6333/collections
```

The output is similar to:
```output
{"result":{"collections":[{"name":"axion_demo"}]},"status":"ok","time":4.01e-6}
```

## What you've learned and what's next

In this section, you learned how to:

- Install Python libraries for vector search workloads
- Generate embeddings using a transformer model
- Create a vector collection in Qdrant
- Store embeddings as indexed vectors
- Verify the stored vector collection

In the next section, you will query the vector database and perform semantic similarity search, enabling AI-powered retrieval and chatbot-style knowledge queries.
