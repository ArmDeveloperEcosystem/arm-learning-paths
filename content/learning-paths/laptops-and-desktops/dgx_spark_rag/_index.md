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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-28T16:15:07Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: facf9c504a3caceb62ef898a04a6760e8aafeb7e802e5727cb80d3a7e7e344d0
  summary_generated_at: '2026-07-28T16:15:07Z'
  summary_source_hash: facf9c504a3caceb62ef898a04a6760e8aafeb7e802e5727cb80d3a7e7e344d0
  faq_generated_at: '2026-07-28T16:15:07Z'
  faq_source_hash: facf9c504a3caceb62ef898a04a6760e8aafeb7e802e5727cb80d3a7e7e344d0
  summary: >-
    This Learning Path guides learners through building a Retrieval-Augmented Generation (RAG)
    pipeline on Arm-based NVIDIA DGX Spark (Grace–Blackwell, GB10). You configure a Python environment,
    prepare the e5-base-v2 embedding model and a Llama 3.1 8B Instruct model, and convert a sample
    corpus into clean, chunked text for vectorization. Using FAISS on Arm, you create a vector
    index and then connect CPU-based retrieval and indexing with GPU-accelerated inference via
    the llama.cpp REST server. After running queries to validate end-to-end behavior on real documentation
    data, you monitor system memory and GPU activity to observe unified memory behavior from idle
    through active RAG queries.
  faqs:
  - question: Do I need to complete the quantized LLM Learning Path before starting this one?
    answer: >-
      It is recommended to complete the Learning Path on unlocking quantized LLM performance on
      Arm-based NVIDIA DGX Spark. That background covers CPU and GPU builds of llama.cpp used
      in this RAG solution.
  - question: Which models should I use for embeddings and generation in this RAG pipeline?
    answer: >-
      Use e5-base-v2 for embeddings and Llama 3.1 8B Instruct for generation. These models are
      prepared during the environment setup steps.
  - question: What should I expect after preparing documents and building the FAISS index?
    answer: >-
      Your documents are converted into clean, chunked text segments, then vectorized and indexed
      by FAISS. The result is a searchable vector database that returns the most relevant chunks
      for a query.
  - question: How do I know the retrieval and generation components are integrated correctly?
    answer: >-
      Run a query and confirm the response reflects information from your loaded documentation.
      Retrieval and indexing run on the Arm Grace CPUs, and generation uses the llama.cpp REST
      server on Blackwell GPUs.
  - question: What should I look for when monitoring unified memory performance on GB10?
    answer: >-
      Start from an idle state, then launch the model server and issue a query while observing
      system memory and GPU activity. You should see changes between idle and active states that
      align with zero-copy data sharing and hybrid AI inference described in the steps.
# END generated_summary_faq

author: Odin Shen

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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

