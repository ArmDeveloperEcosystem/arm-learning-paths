---
title: Deploy quantized LLMs on DGX Spark using llama.cpp

draft: true
cascade:
    draft: true

minutes_to_complete: 60

who_is_this_for: This Learning Path is for AI practitioners, performance engineers, and system architects who want to understand how the Grace–Blackwell (GB10) platform enables efficient quantized LLM inference through CPU–GPU collaboration.

learning_objectives:
    - Understand the Grace–Blackwell (GB10) architecture and how it supports efficient AI inference
    - Build and validate both CUDA-enabled and CPU-only versions of llama.cpp for flexible deployment
    - Analyze how Armv9 SIMD instructions accelerate quantized LLM inference on the Grace CPU

prerequisites:
    - NVIDIA DGX Spark system with at least 15 GB of available disk space
    - Basic understanding of machine learning concepts

author: Odin Shen

### Tags
skilllevels: Introductory
subjects: ML
armips:
    - Cortex-A
    - Cortex-X
operatingsystems:
    - Linux
tools_software_languages:
    - Python
    - C
    - Bash
    - llama.cpp

further_reading:
    - resource:
        title: NVIDIA DGX Spark
        link: https://www.nvidia.com/en-gb/products/workstations/dgx-spark/
        type: website
    - resource:
        title: NVIDIA DGX Spark Playbooks
        link: https://github.com/NVIDIA/dgx-spark-playbooks
        type: documentation
    - resource:
        title: Explore llama.cpp architecture and the inference workflow
        link: https://learn.arm.com/learning-paths/servers-and-cloud-computing/llama_cpp_streamline/
        type: blog
    - resource:
        title: The Dawn of New Desktop Devices Arm-Powered NVIDIA DGX Spark Workstations to Redefine AI Computing
        link: https://newsroom.arm.com/blog/arm-powered-nvidia-dgx-spark-ai-workstations
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
