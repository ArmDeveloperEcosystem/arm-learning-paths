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


generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T23:01:47Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: ada333cc887badfd57815708ef93e172543da74f2c995b46a916817917e92394
  summary_generated_at: '2026-06-01T22:03:05Z'
  summary_source_hash: ada333cc887badfd57815708ef93e172543da74f2c995b46a916817917e92394
  faq_generated_at: '2026-06-02T23:01:47Z'
  faq_source_hash: ada333cc887badfd57815708ef93e172543da74f2c995b46a916817917e92394
  summary: >-
    This Learning Path shows how to build and validate both CUDA-enabled and CPU-only versions
    of llama.cpp on an Arm-based NVIDIA DGX Spark system with the Grace–Blackwell (GB10) architecture
    running Linux. You will review GB10 fundamentals, including the Grace CPU with Armv9 Cortex‑X925
    and Cortex‑A725 cores, verify system readiness (CPU, OS, Blackwell GPU, and CUDA toolkit),
    compile llama.cpp for GPU and CPU targets, and confirm both builds function on DGX Spark.
    You then analyze Armv9 SIMD behavior on the Grace CPU using Process Watch, observing instruction
    usage during quantized LLM inference. Prerequisites include DGX Spark access (15 GB free),
    Linux CLI skills, CUDA basics, quantized LLM knowledge, and experience building with CMake
    and make.
  faqs:
  - question: What do I need before running the steps on DGX Spark?
    answer: >-
      You need access to an NVIDIA DGX Spark system with at least 15 GB of available disk space.
      Familiarity with Linux and the command line, CUDA programming basics, knowledge of quantized
      LLMs, and experience building from source with CMake and make are expected.
  - question: How do I confirm my DGX Spark is ready for building llama.cpp?
    answer: >-
      Verify your Grace CPU configuration and operating system, ensure the Blackwell GPU and CUDA
      drivers are active, and confirm that the CUDA toolkit is installed. The readiness section
      guides you through these checks before you start building.
  - question: 'Which llama.cpp build should I use on GB10: GPU or CPU-only?'
    answer: >-
      Use the CUDA-enabled GPU build when the Blackwell GPU and a CUDA 13 environment are available
      for quantized LLM workloads. Use the CPU-only build to run entirely on the Grace CPU, which
      leverages Armv9 vector capabilities such as SVE2, BFloat16, and I8MM.
  - question: What result should I expect after completing the builds?
    answer: >-
      You will have both a CUDA-enabled and a CPU-only llama.cpp build ready to run on DGX Spark.
      The Learning Path includes steps to validate that each build functions correctly on the
      platform.
  - question: How do I analyze the Armv9 instruction mix during CPU inference?
    answer: >-
      Use Process Watch to observe Neon SIMD instruction execution on the Grace CPU. The path
      also explains why SVE and SVE2 remain inactive under the current kernel configuration during
      this analysis.
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

