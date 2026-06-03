---
title: Orchestrate a persistent local AI agent with Hermes on DGX Spark

draft: true
cascade:
    draft: true

description: Learn how to build a continuously running local AI agent on NVIDIA DGX Spark by combining Hermes Agent, Ollama, and Qdrant to handle event-driven document ingestion, semantic memory, and contextual retrieval using Arm Grace CPUs.

minutes_to_complete: 90

who_is_this_for: This is an advanced topic for developers building persistent local AI agent systems on NVIDIA DGX Spark who want to use Arm Grace CPUs for orchestration and Blackwell GPUs for local LLM inference and embeddings.

learning_objectives:
    - Describe how persistent AI runtimes combine orchestration, semantic memory, and local inference
    - Build a continuously running local AI agent using Hermes Agent, Ollama, and Qdrant
    - Use Arm Grace CPUs to orchestrate event-driven AI workflows on NVIDIA DGX Spark
    - Deploy semantic memory and contextual retrieval pipelines using vector embeddings and Qdrant

prerequisites:
    - An NVIDIA DGX Spark system with at least 15 GB of available disk space
    - Familiarity with running Python scripts and basic Docker container workflows

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
        title: Build a RAG pipeline on Arm-based NVIDIA DGX Spark
        link: /learning-paths/laptops-and-desktops/dgx_spark_rag/
        type: Learning Path
    - resource:
        title: Build an offline voice chatbot with faster-whisper and vLLM on DGX Spark
        link: /learning-paths/laptops-and-desktops/dgx_spark_voicechatbot/
        type: Learning Path
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
