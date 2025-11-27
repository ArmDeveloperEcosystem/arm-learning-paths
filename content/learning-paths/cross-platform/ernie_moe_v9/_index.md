---
title: Running ERNIE Mixture of Experts (MoE) Models on Armv9 with llama.cpp

draft: true
cascade:
    draft: true

minutes_to_complete: 60

who_is_this_for: This learning path is designed for developers and engineers looking to deploy Mixture-of-Experts (MoE) models — such as ERNIE-4.5 — on edge-class devices. MoE architectures allow massive LLMs (21B+ parameters) to run with only a fraction of their weights active per inference, making them ideal for resource-constrained environments.

learning_objectives:
    - Understand how MoE models like ERNIE-4.5 enable large-scale inference on edge devices.
    - Set up and execute ERNIE-4.5 (PT and Thinking versions) using llama.cpp and compare the inference behavior.
    - Analyze the performance impact of enabling Armv9-specific hardware optimizations.

prerequisites:
    - One Arm V9 device at least 32GB of available disk space. In this learning path, I use [Radxa O6](https://radxa.com/products/orion/o6/)

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
        title: ERNIE-4.5-21B Modelscope link
        link: https://modelscope.cn/models/unsloth/ERNIE-4.5-21B-A3B-PT-GGUF
        type: website
    - resource:
        title: llama.cpp github repo
        link: https://github.com/ggml-org/llama.cpp.git
        type: documentation
    - resource:
        title: Arm Learning Path
        link: https://learn.arm.com/learning-paths/servers-and-cloud-computing/llama_cpp_streamline/
        type: Learning Path


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
