---
title: Unlock quantized LLM performance on Arm-based NVIDIA DGX Spark using Armv9 SIMD instructions

minutes_to_complete: 60

who_is_this_for: This is an introductory topic for AI practitioners, performance engineers, and system architects who want to learn how to deploy and optimize quantized large language models (LLMs) on NVIDIA DGX Spark systems powered by the Grace-Blackwell (GB10) architecture.

learning_objectives:
    - Describe the Grace–Blackwell (GB10) architecture and its support for efficient AI inference
    - Build CUDA-enabled and CPU-only versions of llama.cpp for flexible deployment
    - Validate the functionality of both builds on the DGX Spark platform
    - Analyze how Armv9 SIMD instructions accelerate quantized LLM inference on the Grace CPU

prerequisites:
    - Access to an NVIDIA DGX Spark system with at least 15 GB of available disk space
    - Familiarity with command-line interfaces and basic Linux operations
    - Understanding of CUDA programming basics and GPU/CPU compute concepts
    - Basic knowledge of quantized large language models (LLMs) and machine learning inference
    - Experience building software from source using CMake and make


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
        title: NVIDIA DGX Spark website
        link: https://www.nvidia.com/en-gb/products/workstations/dgx-spark/
        type: website
    - resource:
        title: NVIDIA DGX Spark Playbooks GitHub repository
        link: https://github.com/NVIDIA/dgx-spark-playbooks
        type: documentation
    - resource:
        title: Profile llama.cpp performance with Arm Streamline and KleidiAI LLM kernels Learning Path
        link: https://learn.arm.com/learning-paths/servers-and-cloud-computing/llama_cpp_streamline/
        type: blog
    - resource:
        title: Arm-Powered NVIDIA DGX Spark Workstations to Redefine AI
        link: https://newsroom.arm.com/blog/arm-powered-nvidia-dgx-spark-ai-workstations
        type: blog

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
