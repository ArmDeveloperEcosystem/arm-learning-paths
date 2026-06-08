---
title: Accelerate LiteRT Models on Android with KleidiAI and SME2
description: Learn how to accelerate LiteRT model inference on Android using KleidiAI with SME2 instructions and validate performance with the benchmark tool.

minutes_to_complete: 45

who_is_this_for: This is an advanced topic for developers looking to leverage Arm's Scalable Matrix Extension 2 (SME2) instructions to accelerate LiteRT model inference on Android.

learning_objectives: 
- Understand how KleidiAI integrates with LiteRT
- Build the LiteRT benchmark tool and enable XNNPACK and KleidiAI with SME2 support in LiteRT
- Create LiteRT models that can be accelerated by SME2 through KleidiAI
- Use the benchmark tool to evaluate and validate the SME2 acceleration performance of LiteRT models

prerequisites:
- An Arm64 Linux development machine 
- An Android device that supports Arm SME2 architecture features - see this [list of devices with SME2 support](/learning-paths/cross-platform/multiplying-matrices-with-sme2/1-get-started/#devices)

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T23:56:24Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: a744c8118a5a3cb97eee7bee271f768bdd71b4286e723c38a7b4ff6cd9e08d18
  summary_generated_at: '2026-06-02T02:51:34Z'
  summary_source_hash: a744c8118a5a3cb97eee7bee271f768bdd71b4286e723c38a7b4ff6cd9e08d18
  faq_generated_at: '2026-06-02T23:56:24Z'
  faq_source_hash: a744c8118a5a3cb97eee7bee271f768bdd71b4286e723c38a7b4ff6cd9e08d18
  summary: >-
    This advanced Learning Path shows how to accelerate LiteRT (Lite Runtime) model inference
    on Android by enabling KleidiAI with Scalable Matrix Extension 2 (SME2) via XNNPACK, then
    validating the results with the benchmark_model tool. You will examine how LiteRT, XNNPACK,
    and KleidiAI fit together; create LiteRT models that match the subset of operators currently
    accelerated by SME2; build two benchmark_model binaries (one with KleidiAI+SME2 and one baseline
    using Neon micro-kernels); and run benchmarks on an SME2-capable Android device. Prerequisites
    are an Arm64 Linux development machine and an Android device with SME2 support (a device list
    is linked in the path). By the end, you can compare benchmark outputs to evaluate SME2 acceleration
    for your models.
  faqs:
  - question: What do I need before building and benchmarking?
    answer: >-
      You need an Arm64 Linux development machine and an Android device that supports Arm SME2.
      You also need a LiteRT model (for example, fc_fp32.tflite) and two benchmark_model binaries
      built with and without KleidiAI and SME2.
  - question: How do I check if my Android device supports SME2?
    answer: >-
      On the device, use an ADB shell and run cat /proc/cpuinfo. Look for a feature entry indicating
      SME2 support, and you can also refer to the linked list of SME2-capable devices in the prerequisites.
  - question: Which parts of my LiteRT model are accelerated through KleidiAI SME2?
    answer: >-
      Only a subset of KleidiAI SME2 micro-kernels has been integrated into XNNPACK. Supported
      operator data types and quantization configurations are listed in the path; other operators
      use XNNPACK’s default implementation.
  - question: Why build two versions of the benchmark_model tool?
    answer: >-
      You build one version with KleidiAI and SME2 enabled and another without SME2 to establish
      a Neon-based baseline. Running both lets you evaluate and validate the acceleration provided
      by SME2-enabled micro-kernels.
  - question: What should I check if my benchmark does not reflect SME2 acceleration?
    answer: >-
      Confirm the device reports SME2 support and that your model uses operators and data types
      covered by the integrated SME2 micro-kernels. If not supported, LiteRT will use XNNPACK’s
      default implementation during inference.
# END generated_summary_faq

author: Jiaming Guo

### Tags
skilllevels: Advanced
subjects: ML
armips:
    - Cortex-A
    - Cortex-X
    - Arm C1
tools_software_languages:
    - C
    - Python
    - SME2
operatingsystems:
    - Android



further_reading:
    - resource:
        title: LiteRT model optimization
        link: https://ai.google.dev/edge/litert/models/model_optimization
        type: website
    - resource:
        title: Convert Pytorch model to LiteRT model
        link: https://ai.google.dev/edge/litert/models/pytorch_to_tflite
        type: website
    - resource:
        title: LiteRT repository
        link: https://github.com/google-ai-edge/LiteRT?tab=readme-ov-file#1--i-have-a-pytorch-model
        type: website



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

