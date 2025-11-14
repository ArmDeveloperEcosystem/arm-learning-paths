---
title: End-to-End RAG Pipeline on Grace–Blackwell (GB10)

draft: true
cascade:
    draft: true

minutes_to_complete: 60

who_is_this_for: This learning path is designed for developers and engineers who want to understand and implement a Retrieval-Augmented Generation (RAG) pipeline optimized for the Grace–Blackwell (GB10) platform. It is ideal for those interested in exploring how Arm-based Grace CPUs manage local document retrieval and orchestration, while Blackwell GPUs accelerate large language model inference through the open-source llama.cpp REST Server. By the end, learners will understand how to build an efficient hybrid CPU–GPU RAG system that leverages Unified Memory for seamless data sharing between computation layers.

learning_objectives:
    - Understand how a RAG system combines document retrieval and language model generation.  
    - Deploy a hybrid CPU–GPU RAG pipeline on the GB10 platform using open-source tools.
    - Use the llama.cpp REST Server for GPU-accelerated inference with CPU-managed retrieval.  
    - Build a reproducible RAG application that demonstrates efficient hybrid computing.  

prerequisites:
    - One NVIDIA DGX Spark system with at least 15 GB of available disk space.
    - Follow the previous [Learning Path](https://learn.arm.com/learning-paths/laptops-and-desktops/dgx_spark_llamacpp/) to install both the CPU and GPU builds of llama.cpp.

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
        title: Arm Learning Path
        link: https://learn.arm.com/learning-paths/laptops-and-desktops/dgx_spark_llamacpp/
        type: Learning Path


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
