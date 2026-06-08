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

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T01:23:50Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 36bf3c45f0b38350714ba41ea88c1551b33f6d299a65b3b0d6668fee2d88d835
  summary_generated_at: '2026-06-02T04:18:16Z'
  summary_source_hash: 36bf3c45f0b38350714ba41ea88c1551b33f6d299a65b3b0d6668fee2d88d835
  faq_generated_at: '2026-06-03T01:23:50Z'
  faq_source_hash: 36bf3c45f0b38350714ba41ea88c1551b33f6d299a65b3b0d6668fee2d88d835
  summary: >-
    Learn how to profile llama.cpp inference on Arm CPUs using Arm Streamline. This advanced path
    guides you to integrate Streamline Annotation Markers and Annotation Channels into the llama.cpp
    codebase to visualize and analyze the Prefill and Decode stages, and to perform operator-level
    timing during token generation. You will build llama-cli, configure the gator daemon, and
    prepare your Arm Neoverse or Cortex-A target running Linux or Android with the required executables
    and model files. By the end, you will capture and interpret Streamline data and evaluate multi-core
    and multi-thread execution characteristics. Prerequisites include familiarity with llama.cpp,
    transformer models, and Arm Streamline.
  faqs:
  - question: What do I need before running the profiling steps?
    answer: >-
      You need an Arm Neoverse or Cortex-A hardware platform running Linux or Android, plus a
      basic understanding of llama.cpp, transformer models, and Arm Streamline usage. These are
      listed prerequisites for this Learning Path.
  - question: Which option should I use to visualize the Prefill and Decode stages?
    answer: >-
      Use Streamline’s Annotation Marker feature and insert markers in llama.cpp to tag the Prefill
      and Decode stages. These markers appear in the Streamline timeline to correlate performance
      data with token generation phases.
  - question: How can I analyze operator-level performance during token generation?
    answer: >-
      Use Streamline Annotation Channels to group related operations and track their timing as
      separate visual channels. This lets you examine execution time per node in the compute graph
      and see concurrent operations over time.
  - question: How do I evaluate multi-core or multi-thread execution in this path?
    answer: >-
      Capture a Streamline profile while running llama.cpp and use your annotations to correlate
      activity during Prefill and Decode across threads and cores. The Learning Path guides you
      through assessing multi-core and multi-thread execution on Arm CPUs.
  - question: What should I check if Streamline is not collecting data from my target?
    answer: >-
      Verify that the gator daemon is configured and running on the target system. Also ensure
      the required executables and model files are present on the device before capturing data.
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

