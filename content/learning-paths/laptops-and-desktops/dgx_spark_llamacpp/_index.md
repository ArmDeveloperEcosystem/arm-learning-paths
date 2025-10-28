---
title: Deploying quantized LLMs on DGX Spark using llama.cpp

draft: true
cascade:
    draft: true

minutes_to_complete: 60

who_is_this_for: This session is intended for AI practitioners, performance engineers, and system architects who want to understand how the Grace–Blackwell (GB10) platform enables efficient quantized LLM inference through CPU–GPU collaboration.

learning_objectives:
    - Understand the Grace–Blackwell (GB10) architecture and how it supports efficient AI inference.
    - Build and validate both CUDA 13-enabled and CPU-only versions of llama.cpp for flexible deployment of quantized LLMs on the GB10 platform.
    - Observe and interpret how Armv9 SIMD instructions (Neon, SVE) are utilized during quantized LLM inference on the Grace CPU using Process Watch.

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
