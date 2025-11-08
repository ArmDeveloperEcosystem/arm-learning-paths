---
title: Understanding RAG on Grace–Blackwell (GB10)
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What is RAG?

This module provides the conceptual foundation for how Retrieval-Augmented Generation operates on the ***Grace–Blackwell*** (GB10) platform before you begin building the system in the next steps.

**Retrieval-Augmented Generation (RAG)** combines information retrieval with language-model generation.
Instead of relying solely on pre-trained weights, a RAG system retrieves relevant text from a document corpus and passes it to a language model to create factual, context-aware responses.

Typical pipeline:

User Query ─> Embedding ─> Vector Search ─> Context ─> Generation ─> Answer

* ***Embedding model*** (e.g., E5-base-v2): Converts text into dense numerical vectors.
* ***Vector database*** (e.g., FAISS): Searches for semantically similar chunks.
* ***Language model*** (e.g., Llama 3.1 8B Instruct – GGUF Q8_0): Generates an answer conditioned on retrieved context.

More information about RAG system and the challenges of building them can be found in this [learning path](https://learn.arm.com/learning-paths/servers-and-cloud-computing/copilot-extension/1-rag/)


## Why Grace–Blackwell (GB10)?

The GB10 platform integrates:
- ***Grace CPU (Arm v9.2)*** – 20 cores (10 × Cortex-X925 + 10 × Cortex-A725)
- ***Blackwell GPU*** – CUDA 13.0 Tensor Core architecture
- ***Unified Memory (128 GB NVLink-C2C)*** – Shared address space between CPU and GPU. The shared NVLink-C2C interface allows both processors to access the same 128 GB Unified Memory region without copy operations — a key feature validated later in Module 4.

Benefits for RAG:
- ***Hybrid execution*** – Grace CPU efficiently handles embedding, indexing, and API orchestration.
- ***GPU acceleration*** – Blackwell GPU performs token generation with low latency.
- ***Unified memory*** – Eliminates CPU↔GPU copy overhead; tensors and document vectors share the same memory region.
- ***Open-source friendly*** – Works natively with PyTorch, FAISS, Transformers, and FastAPI.

## Conceptual Architecture

```
                     ┌─────────────────────────────────────┐
                     │             User Query              │
                     └──────────────┬──────────────────────┘
                                    │
                                    ▼
                         ┌────────────────────┐
                         │    Embedding (E5)  │
                         │    → FAISS (CPU)   │
                         └────────────────────┘
                                    │
                                    ▼
                         ┌────────────────────┐
                         │   Context Builder  │
                         │    (Grace CPU)     │
                         └────────────────────┘
                                    │
                                    ▼
             ┌───────────────────────────────────────────────┐
             │         llama.cpp (GGUF Model, Q8_0)          │
             │           -ngl 40 --ctx-size 8192             │
             │   Grace CPU + Blackwell GPU (split compute)   │
             └───────────────────────────────────────────────┘
                                    │
                                    ▼
                         ┌────────────────────┐
                         │  FastAPI Response  │
                         └────────────────────┘

```

To make the concept concrete, this learning path will later demonstrate a small **engineering assistant** example.  
The assistant retrieves technical references (e.g., Arm SDK, TensorRT, or OpenCL documentation) and generates helpful explanations for software developers.  
This use case illustrates how a RAG system can provide **real, contextual knowledge** without retraining the model.

| **Stage** | **Technology / Framework** | **Hardware Execution** | **Function** |
|------------|-----------------------------|--------------------------|---------------|
| **Document Processing** | pypdf, text preprocessing scripts | Grace CPU | Converts PDFs and documents into plain text, performs cleanup and segmentation. |
| **Embedding Generation** | E5-base-v2 via sentence-transformers | Grace CPU | Transforms text into semantic vector representations for retrieval. |
| **Semantic Retrieval** | FAISS + LangChain | Grace CPU | Searches the vector index to find the most relevant text chunks for a given query. |
| **Text Generation** | llama.cpp REST Server (GGUF model) | Blackwell GPU + Grace CPU | Generates natural language responses using the Llama 3 model, accelerated by GPU inference. |
| **Pipeline Orchestration** | Python (RAG Query Script) | Grace CPU | Coordinates embedding, retrieval, and generation via REST API calls. |
| **Unified Memory Architecture** | NVLink-C2C Shared Memory | Grace CPU + Blackwell GPU | Enables zero-copy data sharing between CPU and GPU for improved latency and efficiency. |


## Prerequisites Check

In the following content, I am using [EdgeXpert](https://ipc.msi.com/product_detail/Industrial-Computer-Box-PC/AI-Supercomputer/EdgeXpert-MS-C931), a product from [MSI](https://www.msi.com/index.php).

Before proceeding, verify that your GB10 system meets the following:

Run the following commands to confirm your hardware environment:

```bash
# Check Arm CPU architecture
lscpu | grep "Architecture"

# Confirm visible GPU and driver version
nvidia-smi
```

Expected output:
- ***Architecture***:   aarch64
- ***CUDA Version***:   13.0 (or later)
- ***Driver Version***: 580.95.05


## Wrap-up

In this module, you learned the foundational concepts of **Retrieval-Augmented Generation (RAG)** and how it benefits from the **Grace–Blackwell (GB10)** architecture.  
You explored how the **Grace CPU** and **Blackwell GPU** collaborate through **Unified Memory**, enabling seamless data sharing and hybrid execution for AI workloads.

With the conceptual architecture and hardware overview complete, you are now ready to begin hands-on implementation.  
In the next module, you will **prepare the development environment**, install the required dependencies, and verify that both the **E5-base-v2** embedding model and **Llama 3.1 8B Instruct** LLM are functional on the **Grace–Blackwell platform**.

This marks the transition from **theory to practice** — moving from conceptual RAG fundamentals to building your own hybrid CPU–GPU RAG pipeline.