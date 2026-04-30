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

generate_summary_faq: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-04-30T18:58:17Z'
  generator: template
  source_hash: a744c8118a5a3cb97eee7bee271f768bdd71b4286e723c38a7b4ff6cd9e08d18
  summary: >-
    Learn how to accelerate LiteRT model inference on Android using KleidiAI with SME2 instructions
    and validate performance with the benchmark tool. It is designed for developers looking to
    leverage Arm's Scalable Matrix Extension 2 (SME2) instructions to accelerate LiteRT model
    inference on Android. By the end, you will be able to understand how KleidiAI integrates with
    LiteRT, build the LiteRT benchmark tool and enable XNNPACK and KleidiAI with SME2 support
    in LiteRT, and create LiteRT models that can be accelerated by SME2 through KleidiAI. It focuses
    on tools and technologies such as C, Python, and SME2, Android environments, and Arm platforms
    including Cortex-A, Cortex-X, and Arm C1. The main steps cover Explore LiteRT, XNNPACK, KleidiAI,
    and SME2, Create LiteRT models, Build the LiteRT benchmark tool, and Benchmark the LiteRT
    model.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will understand how KleidiAI integrates with LiteRT, build the LiteRT benchmark tool
      and enable XNNPACK and KleidiAI with SME2 support in LiteRT, and create LiteRT models that
      can be accelerated by SME2 through KleidiAI. Learn how to accelerate LiteRT model inference
      on Android using KleidiAI with SME2 instructions and validate performance with the benchmark
      tool.
  - question: Who is this Learning Path for?
    answer: >-
      This is an advanced topic for developers looking to leverage Arm's Scalable Matrix Extension
      2 (SME2) instructions to accelerate LiteRT model inference on Android.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: An Arm64 Linux development machine;
      An Android device that supports Arm SME2 architecture features - see this [list of devices
      with SME2 support](/learning-paths/cross-platform/multiplying-matrices-with-sme2/1-get-started/#devices).
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including C, Python, and SME2, Android environments, and Arm
      platforms such as Cortex-A, Cortex-X, and Arm C1.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Explore LiteRT, XNNPACK, KleidiAI, and SME2, Create
      LiteRT models, Build the LiteRT benchmark tool, and Benchmark the LiteRT model.
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

