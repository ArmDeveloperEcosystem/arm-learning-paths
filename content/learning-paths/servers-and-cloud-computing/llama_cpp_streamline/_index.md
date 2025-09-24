---
title: Use Streamline to analyze LLM on CPU with llama.cpp and KleidiAI

minutes_to_complete: 50

who_is_this_for: This advanced topic is for software developers, performance engineers, and AI practitioners who want to run llama.cpp on Arm-based CPUs, learn how to use Arm Streamline to capture and analyze performance data, understand how LLM inference behaves at the Prefill and Decode stages.

learning_objectives:
    - Describe the architecture of llama.cpp and the role of Prefill and Decode stages
    - Integrate Streamline Annotations into llama.cpp for fine-grained performance insights
    - Capture and interpret profiling data with Streamline
    - Use Annotation Channels to analyze specific operators during token generation
    - Evaluate multi-core and multi-thread execution of llama.cpp on Arm CPUs

prerequisites:
    - Basic understanding of llama.cpp
    - Understanding of transformer model
    - Knowledge of Streamline usage
    - An Arm Neoverse or Cortex-A hardware platform running Linux or Android to test the application

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
    - KleidiAI
    - Neoverse
    - Profiling
operatingsystems:
    - Linux
    - Android

further_reading:
    - resource:
        title: llama.cpp project
        link:  https://github.com/ggml-org/llama.cpp
        type:  source code
    - resource:
        title: Qwen1_5-0_5b-chat-q4_0.gguf 
        link: https://huggingface.co/Qwen/Qwen1.5-0.5B-Chat-GGUF/blob/main/qwen1_5-0_5b-chat-q4_0.gguf 
        type:  LLM model
    - resource:
        title: Arm Streamline User Guide 
        link: https://developer.arm.com/documentation/101816/9-7
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
