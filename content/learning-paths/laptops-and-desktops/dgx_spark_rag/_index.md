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
  template_version: summary-faq-v1
  generated_at: '2026-05-06T17:17:55Z'
  generator: template
  source_hash: facf9c504a3caceb62ef898a04a6760e8aafeb7e802e5727cb80d3a7e7e344d0
  summary: >-
    Learn how to build a Retrieval-Augmented Generation (RAG) pipeline on NVIDIA DGX Spark combining
    Arm Grace CPU orchestration with Blackwell GPU-accelerated inference using llama.cpp. It is
    designed for developers who want to build a Retrieval-Augmented Generation (RAG) pipeline
    on the NVIDIA DGX Spark platform. You'll learn how Arm-based Grace CPUs handle document retrieval
    and orchestration, while Blackwell GPUs speed up large language model inference using the
    open-source llama.cpp REST server. This is a great fit if you're interested in combining Arm
    CPU management with GPU-accelerated AI workloads. By the end, you will be able to describe
    how a RAG system combines document retrieval and language model generation, deploy a hybrid
    CPU-GPU RAG pipeline on the GB10 platform using open-source tools, and use the llama.cpp REST
    Server for GPU-accelerated inference with CPU-managed retrieval. It focuses on tools and technologies
    such as Python, llama.cpp, and Hugging Face, Linux environments, and Arm platforms including
    Cortex-A. The main steps cover Explore building a RAG pipeline on Arm-based Grace–Blackwell
    systems, Configure the RAG development environment and models, Add documents to the RAG vector
    database, Build and run the RAG pipeline, and Monitor unified memory performance.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will describe how a RAG system combines document retrieval and language model generation,
      deploy a hybrid CPU-GPU RAG pipeline on the GB10 platform using open-source tools, and use
      the llama.cpp REST Server for GPU-accelerated inference with CPU-managed retrieval. Learn
      how to build a Retrieval-Augmented Generation (RAG) pipeline on NVIDIA DGX Spark combining
      Arm Grace CPU orchestration with Blackwell GPU-accelerated inference using llama.cpp.
  - question: Who is this Learning Path for?
    answer: >-
      This is an advanced topic for developers who want to build a Retrieval-Augmented Generation
      (RAG) pipeline on the NVIDIA DGX Spark platform. You'll learn how Arm-based Grace CPUs handle
      document retrieval and orchestration, while Blackwell GPUs speed up large language model
      inference using the open-source llama.cpp REST server. This is a great fit if you're interested
      in combining Arm CPU management with GPU-accelerated AI workloads.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: An NVIDIA DGX Spark system with at least
      15 GB of available disk space.
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including Python, llama.cpp, and Hugging Face, Linux environments,
      and Arm platforms such as Cortex-A.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Explore building a RAG pipeline on Arm-based Grace–Blackwell
      systems, Configure the RAG development environment and models, Add documents to the RAG
      vector database, Build and run the RAG pipeline, and Monitor unified memory performance.
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

