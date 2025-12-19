---
title: Build a RAG pipeline on Arm-based NVIDIA DGX Spark
minutes_to_complete: 60

who_is_this_for: This is an advanced topic for developers who want to build a Retrieval-Augmented Generation (RAG) pipeline on the NVIDIA DGX Spark platform. You'll learn how Arm-based Grace CPUs handle document retrieval and orchestration, while Blackwell GPUs speed up large language model inference using the open-source llama.cpp REST server. This is a great fit if you're interested in combining Arm CPU management with GPU-accelerated AI workloads.

learning_objectives:
    - Describe how a RAG system combines document retrieval and language model generation
    - Deploy a hybrid CPU-GPU RAG pipeline on the GB10 platform using open-source tools
    - Use the llama.cpp REST Server for GPU-accelerated inference with CPU-managed retrieval
    - Build a reproducible RAG application that demonstrates efficient hybrid computing

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
