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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-02T19:29:08Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: e835a550c955b13805c7859ff64e3b8d7fdee68222569225c53a0f15db72f046
  summary_generated_at: '2026-07-02T19:29:08Z'
  summary_source_hash: e835a550c955b13805c7859ff64e3b8d7fdee68222569225c53a0f15db72f046
  faq_generated_at: '2026-07-02T19:29:08Z'
  faq_source_hash: e835a550c955b13805c7859ff64e3b8d7fdee68222569225c53a0f15db72f046
  summary: >-
    You'll use `llama.cpp` on an Armv9 Linux development board to deploy ERNIE-4.5
    Mixture of Experts models, validate inference, and confirm multilingual output with the Thinking
    variant. You'll install the PT and Thinking models, run the same task across both, and examine
    internal expert routing to see how only a subset of parameters is activated at runtime. Then, you'll compare a baseline CPU build with an Armv9-optimized build that enables SVE,
    i8mm, and dotprod, and benchmark them under identical conditions to measure the impact of
    Armv9-specific optimizations.
  faqs:
  - question: What result should I expect when verifying the setup on the Armv9 board?
    answer: >-
      You should see successful model inference and multilingual output from the ERNIE-4.5 Thinking
      variant. This confirms the llama.cpp build and runtime environment are working end to end.
  - question: Which ERNIE-4.5 variant should I use for the comparison step?
    answer: >-
      Use both PT and Thinking on the same task and with the same settings. This makes the differences
      in response style and reasoning easier to observe.
  - question: How do I inspect and interpret MoE expert routing during generation?
    answer: >-
      Use the inspection method shown in the steps to view which experts are selected per token.
      Compare activation patterns between PT and Thinking to understand routing differences.
  - question: How do I set up baseline and optimized builds to benchmark Armv9 features?
    answer: >-
      Build a regular CPU version and a separate Armv9-specific version with SVE, i8mm, and dotprod
      enabled. Run the same benchmarks on both builds and compare results under identical conditions.
  - question: What should I check if a model download or inference run fails?
    answer: >-
      Verify the device uses an Armv9 CPU and that at least 32 GB of disk space is available.
      Re-run the setup verification on the board before proceeding to comparisons or benchmarking.
# END generated_summary_faq

author: Odin Shen

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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
