---
title: Architecture
weight: 8

### FIXED, DO NOT MODIFY
layout: learningpathall
---

# Chatbot Architecture Using Qdrant

In this section, you explore the architecture behind the chatbot retrieval system built using Qdrant on Google Axion Arm-based infrastructure.

This architecture demonstrates how modern AI systems perform **semantic similarity search** to retrieve relevant information from stored knowledge.

Unlike traditional keyword search systems, vector databases allow applications to retrieve information based on **semantic meaning and contextual similarity**.


## System architecture

The chatbot system retrieves relevant information through vector embeddings and similarity search.

```text
User Question
      │
      ▼
Embedding Model
(Sentence Transformer)
      │
      ▼
Vector Representation
      │
      ▼
Qdrant Vector Database
(Vector Similarity Search)
      │
      ▼
Top Matching Knowledge
      │
      ▼
Chatbot Response
```



## Components

**Embedding Model**

The embedding model converts text into numerical vectors representing semantic meaning.

**Example model used:**

```text
sentence-transformers/all-MiniLM-L6-v2
```

This lightweight transformer model is commonly used for semantic search and AI retrieval workloads.

## Vector Database (Qdrant)
Qdrant stores and indexes vector embeddings generated from documents and user queries.

It enables fast **nearest-neighbor similarity search**, which finds the most relevant vectors based on semantic similarity.

Key capabilities:

- high performance vector indexing
- semantic similarity search
- scalable vector storage

## Knowledge Base

The system stores knowledge documents such as:

- technical documentation
- support articles
- FAQs
- internal company knowledge

During ingestion, these documents are converted into embeddings and stored in Qdrant.

## Chatbot Query Engine

When the user asks a question:

1. The query is converted into an embedding
2. Qdrant searches for the closest vectors
3. The chatbot returns relevant information

This process enables the chatbot to understand intent and meaning, rather than relying solely on keyword matching.

## Benefits of This Architecture

This design provides several advantages:

- semantic search instead of keyword matching
- scalable knowledge retrieval
- faster query responses
- efficient AI workloads on Arm infrastructure

## Running on Axion

This example demonstrates that Axion Arm infrastructure can efficiently run vector search workloads.

- Benefits include:
- energy-efficient compute
- scalable cloud infrastructure
- optimized performance for AI workloads

## What you've learned

In this section, you learned how the chatbot retrieval system works using vector search.

You explored:

- How embeddings represent semantic meaning
- How Qdrant stores and indexes vectors
- How similarity search retrieves relevant knowledge
- How this architecture supports chatbot and RAG systems

Together, these components form the foundation for modern AI-powered search and knowledge retrieval systems running on Arm-based cloud infrastructure.
