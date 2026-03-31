---
title: Perform Semantic Search
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

# Perform Semantic Search

In this section, you query the Qdrant vector database using **semantic similarity search**.

Unlike traditional keyword search, semantic search compares vector embeddings to identify the most relevant results based on **meaning and context** rather than exact keyword matches.

This capability enables AI applications such as chatbots, recommendation systems, and knowledge retrieval platforms.


## Architecture overview

The semantic search workflow retrieves the most relevant documents using vector similarity.

```text
User Query
      |
      v
Sentence Transformer Model
      |
      v
Query Embedding Vector
      |
      v
Qdrant Vector Database
      |
      v
Similarity Search
      |
      v
Top Matching Documents
```


## Create the search script

Create the Python script used to query the vector database.

```bash
vi search.py
```

Add the following code:

```python
from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer

client = QdrantClient(url="http://localhost:6333")

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

query = "What is vector search?"

query_vector = model.encode(query).tolist()

results = client.query_points(
    collection_name="axion_demo",
    query=query_vector,
    limit=2
)

print("\nTop results:\n")

for point in results.points:
    print(point.payload["text"])
```

### What this script does

This script performs the following steps:

- Connects to the Qdrant vector database
- Loads a pretrained transformer embedding model
- Converts the query into a vector embedding
- Performs similarity search against stored vectors
- Returns the most relevant documents

## Run the search script

Execute the search script.

```bash
python3.11 search.py
```

The output is similar to:
```output
Vector databases enable semantic search.
Qdrant is optimized for vector similarity search.
```

This confirms that the system successfully retrieved the most semantically relevant documents.

## Why semantic search is powerful

Traditional search engines rely on keyword matching, which often fails when queries are phrased differently.

Semantic search uses vector embeddings to capture meaning.

| User Query              | Retrieved Result                                 |
| ----------------------- | ------------------------------------------------ |
| What is vector search?  | Vector databases enable semantic search          |
| Explain Qdrant          | Qdrant is optimized for vector similarity search |
| How do embeddings work? | Vector databases enable semantic search          |

This allows applications to understand **intent rather than exact wording**.

## What you've learned and what's next

In this section, you learned how to:

- Convert user queries into vector embeddings
- Query the Qdrant vector database
- Retrieve semantically relevant documents
- Understand how semantic similarity search works

In the next section, you will extend this workflow to build a **chatbot-style knowledge retrieval system**, allowing users to interactively query the vector database using natural language.
