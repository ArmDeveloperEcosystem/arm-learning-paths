---
title: Unlock quantized LLM performance on Arm-based NVIDIA DGX Spark

description: Learn how to build and optimize quantized LLMs using llama.cpp on NVIDIA DGX Spark with Grace-Blackwell architecture, leveraging Armv9 SIMD acceleration.

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


generate_summary_faq: true

rerun_summary: false
rerun_faqs: false
# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-05-06T17:17:55Z'
  generator: template
  source_hash: ada333cc887badfd57815708ef93e172543da74f2c995b46a916817917e92394
  summary: >-
    Learn how to build and optimize quantized LLMs using llama.cpp on NVIDIA DGX Spark with Grace-Blackwell
    architecture, leveraging Armv9 SIMD acceleration. It is designed for AI practitioners, performance
    engineers, and system architects who want to learn how to deploy and optimize quantized large
    language models (LLMs) on NVIDIA DGX Spark systems powered by the Grace-Blackwell (GB10) architecture.
    By the end, you will be able to describe the Grace–Blackwell (GB10) architecture and its support
    for efficient AI inference, build CUDA-enabled and CPU-only versions of llama.cpp for flexible
    deployment, and validate the functionality of both builds on the DGX Spark platform. It focuses
    on tools and technologies such as Python, C, Bash, and llama.cpp, Linux environments, and
    Arm platforms including Cortex-A and Cortex-X. The main steps cover Explore Grace Blackwell
    architecture for efficient quantized LLM inference, Verify your Grace Blackwell system readiness
    for AI inference, Build the GPU version of llama.cpp on GB10, Build the CPU version of llama.cpp
    on GB10, and Analyze CPU instruction mix using Process Watch.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will describe the Grace–Blackwell (GB10) architecture and its support for efficient
      AI inference, build CUDA-enabled and CPU-only versions of llama.cpp for flexible deployment,
      and validate the functionality of both builds on the DGX Spark platform. Learn how to build
      and optimize quantized LLMs using llama.cpp on NVIDIA DGX Spark with Grace-Blackwell architecture,
      leveraging Armv9 SIMD acceleration.
  - question: Who is this Learning Path for?
    answer: >-
      This is an introductory topic for AI practitioners, performance engineers, and system architects
      who want to learn how to deploy and optimize quantized large language models (LLMs) on NVIDIA
      DGX Spark systems powered by the Grace-Blackwell (GB10) architecture.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: Access to an NVIDIA DGX Spark system
      with at least 15 GB of available disk space; Familiarity with command-line interfaces and
      basic Linux operations; Understanding of CUDA programming basics and GPU/CPU compute concepts;
      Basic knowledge of quantized large language models (LLMs) and machine learning inference;
      Experience building software from source using CMake and make.
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including Python, C, Bash, and llama.cpp, Linux environments,
      and Arm platforms such as Cortex-A and Cortex-X.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Explore Grace Blackwell architecture for efficient
      quantized LLM inference, Verify your Grace Blackwell system readiness for AI inference,
      Build the GPU version of llama.cpp on GB10, Build the CPU version of llama.cpp on GB10,
      and Analyze CPU instruction mix using Process Watch.
# END generated_summary_faq

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
        link: /learning-paths/servers-and-cloud-computing/llama_cpp_streamline/
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

