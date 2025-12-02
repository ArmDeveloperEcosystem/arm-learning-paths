---
title: Profile llama.cpp performance with Arm Streamline and KleidiAI LLM kernels

minutes_to_complete: 60

who_is_this_for: This is an advanced topic for software developers, performance engineers, and AI practitioners who want to optimize llama.cpp performance on Arm-based CPUs. 

learning_objectives:
    - Profile llama.cpp architecture and identify the role of the Prefill and Decode stages
    - Integrate Streamline Annotations into llama.cpp for fine-grained performance insights
    - Capture and interpret profiling data with Streamline
    - Analyze specific operators during token generation using Annotation Channels
    - Evaluate multi-core and multi-thread execution of llama.cpp on Arm CPUs

prerequisites:
    - Basic understanding of llama.cpp
    - Understanding of transformer models
    - Knowledge of Arm Streamline usage
    - An Arm Neoverse or Cortex-A hardware platform running Linux or Android

author: 
    - Zenon Zhilong Xiu
    - Odin Shen

### Tags
skilllevels: Advanced
subjects: ML
armips:
    - Cortex-A
    - Neoverse
tools_software_languages:
    - Arm Streamline
    - C++
    - llama.cpp
    - Profiling
operatingsystems:
    - Linux
    - Android

further_reading:
    - resource:
        title: llama.cpp project
        link: https://github.com/ggml-org/llama.cpp
        type: website
    - resource:
        title: Build and run llama.cpp on Arm servers
        link: /learning-paths/servers-and-cloud-computing/llama-cpu/
        type: website
    - resource:
        title: Run a Large Language Model chatbot with PyTorch using KleidiAI
        link: /learning-paths/servers-and-cloud-computing/pytorch-llama/
        type: website
    - resource:
        title: Arm Streamline User Guide 
        link: https://developer.arm.com/documentation/101816/9-7
        type: website
    - resource:
        title: KleidiAI project
        link: https://github.com/ARM-software/kleidiai
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
