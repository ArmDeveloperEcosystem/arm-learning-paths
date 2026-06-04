---
title: Build a RAG pipeline on Arm-based NVIDIA DGX Spark

description: Learn how to build a Retrieval-Augmented Generation (RAG) pipeline on NVIDIA DGX Spark combining Arm Grace CPU orchestration with Blackwell GPU-accelerated inference using llama.cpp.

minutes_to_complete: 60

who_is_this_for: This is an advanced topic for developers who want to build a Retrieval-Augmented Generation (RAG) pipeline on the NVIDIA DGX Spark platform. You'll learn how Arm-based Grace CPUs handle document retrieval and orchestration, while Blackwell GPUs speed up large language model inference using the open-source llama.cpp REST server. This is a great fit if you're interested in combining Arm CPU management with GPU-accelerated AI workloads.

learning_objectives:
    - Describe how a RAG system combines document retrieval and language model generation
    - Deploy a hybrid CPU-GPU RAG pipeline on the GB10 platform using open-source tools
    - Use the llama.cpp REST Server for GPU-accelerated inference with CPU-managed retrieval
    - Build a reproducible RAG application that demonstrates efficient hybrid computing

prerequisites:
    - An NVIDIA DGX Spark system with at least 15 GB of available disk space

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T23:02:18Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: facf9c504a3caceb62ef898a04a6760e8aafeb7e802e5727cb80d3a7e7e344d0
  summary_generated_at: '2026-06-01T22:03:59Z'
  summary_source_hash: facf9c504a3caceb62ef898a04a6760e8aafeb7e802e5727cb80d3a7e7e344d0
  faq_generated_at: '2026-06-02T23:02:18Z'
  faq_source_hash: facf9c504a3caceb62ef898a04a6760e8aafeb7e802e5727cb80d3a7e7e344d0
  summary: >-
    This advanced Learning Path guides you through building a hybrid Retrieval-Augmented Generation
    (RAG) pipeline on Arm-based NVIDIA DGX Spark (Grace–Blackwell/GB10). You will set up a Python
    environment on Linux, prepare the e5-base-v2 embedding model and the Llama 3.1 8B Instruct
    LLM, load a sample document corpus, and index it with FAISS for vector search on Arm Grace
    CPUs. You will run GPU-accelerated inference via the llama.cpp REST server on Blackwell GPUs
    while CPU-managed retrieval orchestrates requests. Finally, you will monitor unified memory
    behavior and GPU utilization to validate zero-copy data sharing. Prerequisite: an NVIDIA DGX
    Spark with at least 15 GB free disk space; related llama.cpp background is recommended.
  faqs:
  - question: Do I need to complete another Learning Path before starting this one?
    answer: >-
      It is recommended to first complete “Unlock quantized LLM performance on Arm-based NVIDIA
      DGX Spark” to learn about CPU and GPU builds of llama.cpp. That background helps when deploying
      the RAG solution in this path.
  - question: What platform and resources are required to follow the steps?
    answer: >-
      You need an NVIDIA DGX Spark (Grace–Blackwell/GB10) system running Linux with at least 15
      GB of available disk space. No other explicit prerequisites are listed.
  - question: Which models and libraries does the RAG pipeline use?
    answer: >-
      The pipeline uses e5-base-v2 for embeddings and Llama 3.1 8B Instruct for generation. It
      relies on Python, Hugging Face tooling, FAISS for vector search, and the llama.cpp REST
      server for GPU-accelerated inference.
  - question: How should I set up the Python environment for this project?
    answer: >-
      Create a Python virtual environment and upgrade pip. Then install torch from the PyTorch
      CPU wheel index along with transformers==4.46.2 and sentence-transformers==2.7 as shown
      in the steps.
  - question: How do I verify the pipeline is working and monitor performance?
    answer: >-
      After integration, run the RAG model server and issue a query against your document corpus
      to exercise retrieval and GPU-backed generation. Use the monitoring steps to observe unified
      memory and GPU utilization from separate terminals and confirm zero-copy data sharing during
      inference.
# END generated_summary_faq

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
    - llama.cpp 
    - Hugging Face

further_reading:
    - resource:
        title: Nvidia DGX Spark
        link: https://www.nvidia.com/en-gb/products/workstations/dgx-spark/
        type: website
    - resource:
        title: EdgeXpert from MSI
        link: https://ipc.msi.com/product_detail/Industrial-Computer-Box-PC/AI-Supercomputer/EdgeXpert-MS-C931
        type: website
    - resource:
        title: Nvidia DGX Spark Playbooks
        link: https://github.com/NVIDIA/dgx-spark-playbooks
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

