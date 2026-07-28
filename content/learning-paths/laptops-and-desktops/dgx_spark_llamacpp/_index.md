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
    - Understanding of CUDA programming basics, as well as GPU and CPU compute concepts
    - Basic knowledge of quantized large language models (LLMs) and machine learning inference
    - Experience building software from source using CMake and make

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-28T16:14:08Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: ada333cc887badfd57815708ef93e172543da74f2c995b46a916817917e92394
  summary_generated_at: '2026-07-28T16:14:08Z'
  summary_source_hash: ada333cc887badfd57815708ef93e172543da74f2c995b46a916817917e92394
  faq_generated_at: '2026-07-28T16:14:08Z'
  faq_source_hash: ada333cc887badfd57815708ef93e172543da74f2c995b46a916817917e92394
  summary: >-
    You'll prepare NVIDIA DGX Spark with its Grace CPU and Blackwell GPU, build `llama.cpp` for CUDA
    and CPU execution, and inspect Armv9 vector instructions during quantized LLM inference. You'll
    verify CUDA, compile both variants, and use Process Watch to examine Neon activity and the
    current lack of SVE and SVE2. You'll finish with GPU and CPU binaries.
  faqs:
  - question: How do I know my DGX Spark is ready before building?
    answer: >-
      Confirm the Grace CPU configuration, operating system, Blackwell GPU, and CUDA drivers are
      active, and verify the CUDA 13 toolkit is installed.
  - question: Which build should I start with, GPU-enabled or CPU-only?
    answer: >-
      If the Blackwell GPU and CUDA are available, start with the GPU-enabled `llama.cpp` build.
      Also build the CPU-only version to run on the Grace CPU and to keep a flexible deployment
      option.
  - question: What result should I expect after a successful build?
    answer: >-
      You should get a compiled `llama.cpp` binary targeting either the GPU or the CPU that runs
      quantized LLM inference. A quick test run should complete without errors on the DGX Spark.
  - question: How do I validate that the CPU-only build uses Armv9 vector features?
    answer: >-
      Run an inference with the CPU-only binary and analyze it with Process Watch to observe the
      instruction mix. Expect to see Neon SIMD activity; SVE and SVE2 might remain inactive under
      the current kernel configuration.
  - question: Why don’t I see SVE or SVE2 instructions in my Process Watch results?
    answer: >-
      Under the current kernel configuration used in this path, SVE and SVE2 remain inactive.
      This is expected, and the analysis focuses on Neon SIMD execution on the Grace CPU.
# END generated_summary_faq

author: Odin Shen

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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
