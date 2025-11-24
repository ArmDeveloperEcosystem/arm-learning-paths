---
title: Build a RAG pipeline on Arm-based Grace–Blackwell systems
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Get started

Before starting this Learning Path, you should complete [Unlock quantized LLM performance on Arm-based NVIDIA DGX Spark](/learning-paths/laptops-and-desktops/dgx_spark_llamacpp/) to learn about the CPU and GPU builds of llama.cpp. This background is recommended for building the RAG solution on llama.cpp.

The NVIDIA DGX Spark is also referred to as the Grace-Blackwell platform or GB10, the name of the NVIDIA Grace-Blackwell Superchip. 

## What is RAG?

Retrieval-Augmented Generation (RAG) combines information retrieval with language-model generation.
Instead of relying solely on pre-trained weights, a RAG system retrieves relevant text from a document corpus and passes it to a language model to create factual, context-aware responses.

Here is a typical pipeline:

User Query ─> Embedding ─> Vector Search ─> Context ─> Generation ─> Answer

Each stage in this pipeline plays a distinct role in transforming a question into a context-aware response:

* Embedding model: Converts text into dense numerical vectors. An example is e5-base-v2.
* Vector database: Searches for semantically similar chunks. An example is FAISS.
* Language model: Generates an answer conditioned on retrieved context. An example is Llama 3.1 8B Instruct.

## Why is Grace–Blackwell good for RAG pipelines?

The Grace–Blackwell (GB10) platform combines Arm-based Grace CPUs with NVIDIA Blackwell GPUs, forming a unified architecture optimized for large-scale AI workloads.

Its unique CPU–GPU design and unified memory enable seamless data exchange, making it an ideal foundation for RAG systems that require both fast document retrieval and high-throughput language model inference.

The GB10 platform includes:

- Grace CPU (Armv9.2 architecture) – 20 cores including 10 Cortex-X925 cores and 10 Cortex-A725 cores
- Blackwell GPU – CUDA 13.0 Tensor Core architecture
- Unified Memory (128 GB NVLink-C2C) – Shared address space between CPU and GPU which allows both processors to access the same 128 GB unified memory region without copy operations. 

The GB10 provides the following benefits for RAG applications:

- Hybrid execution – Grace CPU efficiently handles embedding, indexing, and API orchestration.
- GPU acceleration – Blackwell GPU performs token generation with low latency.
- Unified memory – Eliminates CPU to GPU copy overhead because tensors and document vectors share the same memory region.
- Open-source friendly – Works natively with PyTorch, FAISS, Transformers, and FastAPI.

## RAG system architecture

Here is a diagram of the architecture:

```console
.
                     ┌─────────────────────────────────────┐
                     │         User Query                  │
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

## Create an engineering assistant

You can use this architecture to create an engineering assistant.

The assistant retrieves technical references from datasheets, programming guides, and application notes and and generates helpful explanations for software developers.  

This use case illustrates how a RAG system can provide contextual knowledge without retraining the model.

The technology stack you will use is listed below:

| **Stage** | **Technology / Framework** | **Hardware Execution** | **Function** |
|------------|-----------------------------|--------------------------|---------------|
| Document Processing | pypdf, text preprocessing scripts | Grace CPU | Converts PDFs and documents into plain text, performs cleanup and segmentation. |
| Embedding Generation | e5-base-v2 via sentence-transformers | Grace CPU | Transforms text into semantic vector representations for retrieval. |
| Semantic Retrieval | FAISS and LangChain | Grace CPU | Searches the vector index to find the most relevant text chunks for a given query. |
| Text Generation | llama.cpp REST Server (GGUF model) | Blackwell GPU and Grace CPU | Generates natural language responses using the Llama 3 model, accelerated by GPU inference. |
| Pipeline Orchestration | Python (RAG Query Script) | Grace CPU | Coordinates embedding, retrieval, and generation via REST API calls. |
| Unified Memory Architecture | Unified LPDDR5X shared memory | Grace CPU and Blackwell GPU | Enables zero-copy data sharing between CPU and GPU for improved latency and efficiency. |


## Prerequisites Check

Before starting, run the following commands to confirm your hardware is ready:

```bash
# Check Arm CPU architecture
lscpu | grep "Architecture"
```

The expected result is:

```output
Architecture:                            aarch64
```

Print the NVIDIA GPU information:

```bash
# Confirm visible GPU and driver version
nvidia-smi
```

Look for CUDA version 13.0 or later and Driver version 580.95.05 or later.

{{% notice Note %}}
If your software versions are lower than the versions mentioned above, you should upgrade before proceeding.
{{% /notice %}}

## Summary

You now understand how RAG works and why Grace–Blackwell is ideal for RAG systems. The unified memory architecture allows the Grace CPU to handle document retrieval while the Blackwell GPU accelerates text generation, all without data copying overhead.

Next, you'll set up your development environment and install the required tools to build this RAG system.