---
title: Run ERNIE-4.5 Mixture of Experts model on Armv9 with llama.cpp

draft: true
cascade:
    draft: true

minutes_to_complete: 60

who_is_this_for: This Learning Path is for developers and engineers who want to deploy Mixture of Experts (MoE) models, such as ERNIE 4.5, on edge devices. MoE architectures allow large LLMs with 21 billion or more parameters to run with only a fraction of their weights active per inference, making them ideal for resource constrained environments.

learning_objectives:
    - Deploy MoE models like ERNIE-4.5 on edge devices using llama.cpp
    - Compare inference behavior between ERNIE-4.5 PT and Thinking versions
    - Measure performance impact of Armv9-specific hardware optimizations

prerequisites:
    - An Armv9 device with at least 32 GB of available disk space, for example, Radxa Orion O6

author: Odin Shen

### Tags
skilllevels: Introductory
subjects: ML
armips:
    - Cortex-A
operatingsystems:
    - Linux
tools_software_languages:
    - Python
    - C++
    - Bash
    - llama.cpp

### Cross-platform metadata only
shared_path: true
shared_between:
    - laptops-and-desktops
    - servers-and-cloud-computing
    - iot
    - mobile-graphics-and-gaming

further_reading:
    - resource:
        title: ERNIE-4.5-21B Modelscope
        link: https://modelscope.cn/models/unsloth/ERNIE-4.5-21B-A3B-PT-GGUF
        type: website
    - resource:
        title: llama.cpp GitHub repository
        link: https://github.com/ggml-org/llama.cpp
        type: documentation
    - resource:
        title: Build and run llama.cpp with Arm CPU optimizations
        link: /learning-paths/servers-and-cloud-computing/llama_cpp_streamline/
        type: website


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
