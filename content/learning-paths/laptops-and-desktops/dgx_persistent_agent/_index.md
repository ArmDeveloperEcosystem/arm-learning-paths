---
title: Orchestrate a Persistent Local AI Agent with Hermes on DGX Spark

description: Learn how to build a persistent local AI agent on NVIDIA DGX Spark using event-driven orchestration, semantic memory, and heterogeneous Arm CPU + GPU workloads. You'll combine Hermes Agent, Ollama, and Qdrant to create a continuously running local AI runtime capable of event-driven document ingestion, contextual retrieval, and scheduled workspace cognition.

minutes_to_complete: 90

who_is_this_for: This is an advanced topic for developers interested in persistent local AI agent systems, semantic memory architectures, and heterogeneous AI computing on NVIDIA DGX Spark. You'll learn how Arm-based Grace CPUs orchestrate long-running AI workflows including filesystem monitoring, semantic retrieval, runtime scheduling, and autonomous cognition, while Blackwell GPUs accelerate local language model inference and embeddings generation using Ollama. This Learning Path is a great fit if you want to understand how persistent AI runtimes operate continuously using coordinated CPU and GPU workloads.

learning_objectives:
    - Describe how persistent AI runtimes combine orchestration, semantic memory, and local inference
    - Build a continuously running local AI agent using Hermes Agent, Ollama, and Qdrant
    - Use Arm Grace CPUs to orchestrate event-driven AI workflows on NVIDIA DGX Spark
    - Deploy semantic memory and contextual retrieval pipelines using vector embeddings and Qdrant

prerequisites:
    - An NVIDIA DGX Spark system with at least 15 GB of available disk space

author: Odin Shen

### Tags
skilllevels: Advanced
subjects: ML
armips:
    - Cortex-A
operatingsystems:
    - Linux
tools_software_languages:
    - Python
    - Docker 
    - Ollama

further_reading:
    - resource:
        title: NVIDIA DGX Spark
        link: https://www.nvidia.com/en-gb/products/workstations/dgx-spark/
        type: website
    - resource:
        title: RAG Learning Path
        link: https://learn.arm.com/learning-paths/laptops-and-desktops/dgx_spark_rag/
        type: website
    - resource:
        title: Offline Voice Chatbot Learning Path
        link: https://learn.arm.com/learning-paths/laptops-and-desktops/dgx_spark_voicechatbot/
        type: documentation
    - resource:
        title: Unlock quantized LLM performance on Arm-based NVIDIA DGX Spark
        link: /learning-paths/laptops-and-desktops/dgx_spark_llamacpp/
        type: Learning Path


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
