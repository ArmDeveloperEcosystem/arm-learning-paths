---
title: Run ERNIE-4.5 Mixture of Experts model on Armv9 with llama.cpp

minutes_to_complete: 60

who_is_this_for: This is an advanced topic for developers and engineers who want to deploy Mixture of Experts (MoE) models, such as ERNIE 4.5, on edge devices. MoE architectures allow large LLMs with 21 billion or more parameters to run with only a fraction of their weights active per inference, making them ideal for resource constrained environments.

description: Learn how to deploy ERNIE-4.5 Mixture of Experts models on Armv9 devices using llama.cpp, compare PT and Thinking variants, and measure Armv9-specific hardware optimization impact.

learning_objectives:
    - Deploy MoE models like ERNIE-4.5 on edge devices using llama.cpp
    - Compare inference behavior between ERNIE-4.5 PT and Thinking versions
    - Measure performance impact of Armv9-specific hardware optimizations

prerequisites:
    - An Armv9 device with at least 32 GB of available disk space, for example, Radxa Orion O6

generate_summary_faq: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-05-06T17:17:53Z'
  generator: template
  source_hash: e835a550c955b13805c7859ff64e3b8d7fdee68222569225c53a0f15db72f046
  summary: >-
    Learn how to deploy ERNIE-4.5 Mixture of Experts models on Armv9 devices using llama.cpp,
    compare PT and Thinking variants, and measure Armv9-specific hardware optimization impact.
    It is designed for developers and engineers who want to deploy Mixture of Experts (MoE) models,
    such as ERNIE 4.5, on edge devices. MoE architectures allow large LLMs with 21 billion or
    more parameters to run with only a fraction of their weights active per inference, making
    them ideal for resource constrained environments. By the end, you will be able to deploy MoE
    models like ERNIE-4.5 on edge devices using llama.cpp, compare inference behavior between
    ERNIE-4.5 PT and Thinking versions, and measure performance impact of Armv9-specific hardware
    optimizations. It focuses on tools and technologies such as Python, CPP, Bash, and llama.cpp,
    Linux environments, and Arm platforms including Cortex-A. The main steps cover Understand
    Mixture of Experts architecture for edge deployment, Set up llama.cpp on an Armv9 development
    board, Compare ERNIE model behavior and expert routing, and Optimize performance with Armv9
    hardware features.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will deploy MoE models like ERNIE-4.5 on edge devices using llama.cpp, compare inference
      behavior between ERNIE-4.5 PT and Thinking versions, and measure performance impact of Armv9-specific
      hardware optimizations. Learn how to deploy ERNIE-4.5 Mixture of Experts models on Armv9
      devices using llama.cpp, compare PT and Thinking variants, and measure Armv9-specific hardware
      optimization impact.
  - question: Who is this Learning Path for?
    answer: >-
      This is an advanced topic for developers and engineers who want to deploy Mixture of Experts
      (MoE) models, such as ERNIE 4.5, on edge devices. MoE architectures allow large LLMs with
      21 billion or more parameters to run with only a fraction of their weights active per inference,
      making them ideal for resource constrained environments.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: An Armv9 device with at least 32 GB
      of available disk space, for example, Radxa Orion O6.
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including Python, CPP, Bash, and llama.cpp, Linux environments,
      and Arm platforms such as Cortex-A.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Understand Mixture of Experts architecture for edge
      deployment, Set up llama.cpp on an Armv9 development board, Compare ERNIE model behavior
      and expert routing, and Optimize performance with Armv9 hardware features.
# END generated_summary_faq

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
    - CPP
    - Bash
    - llama.cpp

### Cross-platform metadata only
shared_path: true
shared_between:
    - laptops-and-desktops
    - servers-and-cloud-computing
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

