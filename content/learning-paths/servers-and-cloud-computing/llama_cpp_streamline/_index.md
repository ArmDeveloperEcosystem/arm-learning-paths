---
title: Profile llama.cpp performance with Arm Streamline and KleidiAI LLM kernels

minutes_to_complete: 60

who_is_this_for: This is an advanced topic for software developers, performance engineers, and AI practitioners who want to optimize llama.cpp performance on Arm-based CPUs.

description: Optimize llama.cpp on Arm CPUs by integrating Streamline Annotations to profile Prefill and Decode stages, analyze operators, and evaluate multi-core execution.

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

generate_summary_faq: true

# rerun_summary: false
# rerun_faqs: false
# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-05-06T17:17:58Z'
  generator: template
  source_hash: 36bf3c45f0b38350714ba41ea88c1551b33f6d299a65b3b0d6668fee2d88d835
  summary: >-
    Optimize llama.cpp on Arm CPUs by integrating Streamline Annotations to profile Prefill and
    Decode stages, analyze operators, and evaluate multi-core execution. It is designed for software
    developers, performance engineers, and AI practitioners who want to optimize llama.cpp performance
    on Arm-based CPUs. By the end, you will be able to profile llama.cpp architecture and identify
    the role of the Prefill and Decode stages, integrate Streamline Annotations into llama.cpp
    for fine-grained performance insights, and capture and interpret profiling data with Streamline.
    It focuses on tools and technologies such as Arm Streamline, CPP, llama.cpp, and Profiling,
    Linux and Android environments, and Arm platforms including Cortex-A and Neoverse. The main
    steps cover Overview, Explore llama.cpp architecture and the inference workflow, Integrate
    Streamline Annotations into llama.cpp, Analyze token generation performance with Streamline
    profiling, and Implement operator-level performance analysis with Annotation Channels.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will profile llama.cpp architecture and identify the role of the Prefill and Decode
      stages, integrate Streamline Annotations into llama.cpp for fine-grained performance insights,
      and capture and interpret profiling data with Streamline. Optimize llama.cpp on Arm CPUs
      by integrating Streamline Annotations to profile Prefill and Decode stages, analyze operators,
      and evaluate multi-core execution.
  - question: Who is this Learning Path for?
    answer: >-
      This is an advanced topic for software developers, performance engineers, and AI practitioners
      who want to optimize llama.cpp performance on Arm-based CPUs.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: Basic understanding of llama.cpp; Understanding
      of transformer models; Knowledge of Arm Streamline usage; An Arm Neoverse or Cortex-A hardware
      platform running Linux or Android.
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including Arm Streamline, CPP, llama.cpp, and Profiling, Linux
      and Android environments, and Arm platforms such as Cortex-A and Neoverse.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Overview, Explore llama.cpp architecture and the inference
      workflow, Integrate Streamline Annotations into llama.cpp, Analyze token generation performance
      with Streamline profiling, and Implement operator-level performance analysis with Annotation
      Channels.
# END generated_summary_faq

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
    - CPP
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

