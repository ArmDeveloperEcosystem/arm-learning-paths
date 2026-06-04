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

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T21:37:05Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: e835a550c955b13805c7859ff64e3b8d7fdee68222569225c53a0f15db72f046
  summary_generated_at: '2026-06-01T21:05:21Z'
  summary_source_hash: e835a550c955b13805c7859ff64e3b8d7fdee68222569225c53a0f15db72f046
  faq_generated_at: '2026-06-02T21:37:05Z'
  faq_source_hash: e835a550c955b13805c7859ff64e3b8d7fdee68222569225c53a0f15db72f046
  summary: >-
    This advanced Learning Path shows how to deploy ERNIE-4.5 Mixture of Experts (MoE) models
    on Armv9 devices using llama.cpp on Linux. You will set up an Armv9 development board (for
    example, a Radxa Orion O6 with at least 32 GB of available disk space), run and verify inference,
    and validate multilingual outputs with the ERNIE-4.5 Thinking variant. You then compare the
    PT and Thinking models, inspect MoE expert routing, and benchmark a baseline CPU build against
    an Armv9-optimized build that enables SVE, i8mm, and dotprod instructions to measure their
    impact. The outcome is the ability to deploy, compare, and benchmark ERNIE-4.5 MoE models
    on Armv9 in about 60 minutes.
  faqs:
  - question: What do I need before running this Learning Path?
    answer: >-
      You need an Armv9 device with at least 32 GB of available disk space. The steps assume a
      Linux environment and use a Radxa Orion O6 as an example platform.
  - question: Which ERNIE-4.5 variants are used, and what will I compare?
    answer: >-
      You will work with the PT and Thinking variants of ERNIE-4.5. The path compares their inference
      behavior on the same task and shows how to inspect internal MoE expert routing. Both share
      the same MoE architecture and parameter count (around 21B total, about 3B active at runtime).
  - question: How do I validate that my setup and model inference are working?
    answer: >-
      You verify inference on an Armv9 development board and validate multilingual outputs using
      the ERNIE Thinking variant. Successful inference confirms the environment and model setup
      are ready for the comparison and benchmarking steps.
  - question: What Armv9 optimizations are benchmarked, and how are they tested?
    answer: >-
      You measure performance with and without Armv9 vector instruction optimizations. The comparison
      is between a baseline regular CPU build and an Armv9-specific build with SVE, i8mm, and
      dotprod enabled.
  - question: How can I observe which MoE experts are used during generation?
    answer: >-
      The path includes steps to inspect internal MoE expert routing behavior while generating
      outputs. You use this to understand how the PT and Thinking variants route tokens to experts
      during inference.
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

