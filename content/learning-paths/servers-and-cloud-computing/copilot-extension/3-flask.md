---
title: RAG System
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What is a RAG system?

RAG stands for "Retrieval Augmented Generation". It describes an AI framework that combines information retrieval with text generation to improve the quality and accuracy of AI-generated content.

The basic flow of a RAG system looks like this:

1. Retrieval: The system searches a knowledge base, usually using some combination of vector and/or text search.
2. Augmentation: The retrieved information is then provided as context to a generative AI model to provide additional context for the user's query.
3. The AI model uses both thye retrieved knowledge and its internal understanding to generate a more useful response to the user.

The benefits of a RAG system revolve around improved factual accuracy of responses. It also allows a system to understand more up-to-date information, since you can add additional knowledge to the knowledge base much more easily than you could retrain the model.

Most importantly, RAG lets you provide reference links to the user, showing the user where the system is getting its information.

## How do I implement RAG in Flask?

In the [Build a GitHub Copilot Extension in Python](learning-paths/servers-and-cloud-computing/gh-copilot-simple/) Learning Path, you created a simple Copilot Extension in Python. Here, you'll add RAG functionality to that Flask app.

You already generated a vector store in a previous section, which you will use as the knowledge base for your RAG retrieval.

As you saw in the [Build a GitHub Copilot Extension in Python](learning-paths/servers-and-cloud-computing/gh-copilot-simple/) Learning Path, the `/agent` endpoint is what GitHub will invoke to send a query to your Extension.

There are a minimum of two things you must add to your existing Extension to obtain RAG functionality:

1. Vector search functions, to find context from your knowledge base.
2. A system prompt that instructs your system about how to use the context from your knowledge base.

### Vector search

First, import necessary Python packages:

```Python
import faiss
import json
import requests
import numpy as np
```

Then create functions to load the FAISS index that you previously created, and invoke them:

```Python
def load_faiss_index(index_path: str):
    """Load the FAISS index from a file."""
    print(f"Loading FAISS index from {index_path}")
    index = faiss.read_index(index_path)
    print(f"Loaded index containing {index.ntotal} vectors")
    return index

def load_metadata(metadata_path: str):
    """Load metadata from a JSON file."""
    print(f"Loading metadata from {metadata_path}")
    with open(metadata_path, 'r') as f:
        metadata = json.load(f)
    print(f"Loaded metadata for {len(metadata)} items")
    return metadata

FAISS_INDEX = load_faiss_index("faiss_index.bin")
FAISS_METADATA = load_metadata("metadata.json")
```

You put these objects in global variables so they stay in memory persistently.

After this, create the functions to make embeddings and search embeddings:

```Python
def create_embedding(query: str, headers=None):
    print(f"Creating embedding using model: {MODEL_NAME}")
    copilot_req = {
        "model": MODEL_NAME,
        "input": [query]
    }
    r = requests.post(llm_client, json=copilot_req, headers=headers)
    r.raise_for_status()
    return_dict = r.json()

    return return_dict['data'][0]['embedding']


def embedding_search(query: str, k: int = 5, headers=None):
    """
    Search the FAISS index with a text query.

    Args:
    query (str): The text to search for.
    k (int): The number of results to return.

    Returns:
    list: A list of dictionaries containing search results with distances and metadata.
    """
    print(f"Searching for: '{query}'")
    # Convert query to embedding
    query_embedding = create_embedding(query, headers)
    query_array = np.array(query_embedding, dtype=np.float32).reshape(1, -1)

    # Perform the search
    distances, indices = FAISS_INDEX.search(query_array, k)
    print(distances, indices)
    # Prepare results
    results = []
    for i, (dist, idx) in enumerate(zip(distances[0], indices[0])):
        if idx != -1:  # -1 index means no result found
            if float(dist) < DISTANCE_THRESHOLD:
                result = {
                    "rank": i + 1,
                    "distance": float(dist),
                    "metadata": FAISS_METADATA[idx]
                }
                # store the result in the metrics db but don't block
                # store_result(result)
                results.append(result)

    return results
```