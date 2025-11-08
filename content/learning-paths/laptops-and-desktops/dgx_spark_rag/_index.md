---
title: End-to-End RAG Pipeline on Grace–Blackwell (GB10)

draft: true
cascade:
    draft: true

minutes_to_complete: 60

who_is_this_for: This learning path teaches how a Retrieval-Augmented Generation (RAG) pipeline operates efficiently in a hybrid CPU–GPU environment on the Grace–Blackwell (GB10) platform. Learners will explore how Arm-based Grace CPUs perform document retrieval and orchestration, while Blackwell GPUs handle language model inference through the open-source llama.cpp REST Server.

learning_objectives:
    - Understand how a RAG system combines document retrieval and language model generation.  
    - Deploy a hybrid CPU–GPU RAG pipeline on the GB10 platform using open-source tools.
    - Use the llama.cpp REST Server for GPU-accelerated inference with CPU-managed retrieval.  
    - Build a reproducible RAG application that demonstrates efficient hybrid computing.  

prerequisites:
    - One NVIDIA DGX Spark system with at least 15 GB of available disk space.

author: Odin Shen

### Tags
skilllevels: Introductory
subjects: ML
armips:
    - Cortex-X
    - Cortex-A
operatingsystems:
    - Linux
tools_software_languages:
    - Python
    - C++
    - Bash
    - llama.cpp

further_reading:
    - resource:
        title: Nvidia DGX Spark
        link: https://www.nvidia.com/en-gb/products/workstations/dgx-spark/
        type: website
    - resource:
        title: Nvidia DGX Spark Playbooks
        link: https://github.com/NVIDIA/dgx-spark-playbooks
        type: documentation
    - resource:
        title: Arm Blog Post
        link: https://newsroom.arm.com/blog/arm-powered-nvidia-dgx-spark-ai-workstations
        type: Blog

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
