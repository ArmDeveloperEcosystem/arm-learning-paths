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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-17T22:07:01Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 189bd4833fcaafbad5fe84bd2ddee1e6006eb59afd3c2e90b1bbcd985719ee14
  summary_generated_at: '2026-08-17T22:07:01Z'
  summary_source_hash: 189bd4833fcaafbad5fe84bd2ddee1e6006eb59afd3c2e90b1bbcd985719ee14
  faq_generated_at: '2026-08-17T22:07:01Z'
  faq_source_hash: 189bd4833fcaafbad5fe84bd2ddee1e6006eb59afd3c2e90b1bbcd985719ee14
  summary: >-
    You'll accelerate LiteRT inference on Android with KleidiAI SME2 microkernels through XNNPACK.
    First, you'll create models using supported operators and data types, then build a KleidiAI-enabled benchmark
    and a baseline. After verifying SME2 support, you'll run both on the same model and compare results,
    including fallback behavior for unsupported operators.
  faqs:
  - question: What do I need on the Android device before running benchmarks?
    answer: >-
      Copy your LiteRT model file and two `benchmark_model` binaries to the device: one built with
      KleidiAI and SME2 enabled and one baseline build. Run both against the same model on the
      same device.
  - question: How do I know if my Android device supports SME2?
    answer: >-
      From an `adb` shell, inspect `/proc/cpuinfo` and look for an entry that indicates SME2 support.
      If you don't see SME2 listed, use a device from the provided SME2-capable list.
  - question: Which LiteRT operators are accelerated by SME2 through KleidiAI?
    answer: >-
      Only the subset of KleidiAI SME2 micro-kernels integrated into XNNPACK are accelerated.
      Operators outside the supported data types and quantization configurations use XNNPACK’s
      default implementation.
  - question: What result should I expect when comparing the two benchmark binaries?
    answer: >-
      The SME2-enabled binary demonstrates performance gains for models that use supported operators
      and data types. Both runs should complete successfully so you can compare their reported
      measurements.
  - question: What should I check if I don’t see an improvement with the SME2-enabled build?
    answer: >-
      Verify the device reports SME2 support, and confirm your model uses the supported operator
      configurations listed in the path. Also ensure you ran the SME2-enabled binary under the
      same conditions as the baseline.
# END generated_summary_faq

author: Jiaming Guo

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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
