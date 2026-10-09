---
title: Profile llama.cpp performance with Arm Streamline and KleidiAI LLM kernels

minutes_to_complete: 60

who_is_this_for: This is an advanced topic for software developers, performance engineers, and AI practitioners who want to optimize llama.cpp performance on Arm-based CPUs.

description: Optimize llama.cpp on Arm CPUs by integrating Streamline Annotations to profile Prefill and Decode stages, analyze operators, and evaluate multi-core execution.

learning_objectives:
    - Profile llama.cpp architecture and identify the role of the Prefill and Decode stages.
    - Integrate marker annotations into llama.cpp for fine-grained performance insights.
    - Capture and interpret profiling data with Streamline.
    - Analyze specific operators during token generation using channel annotations.
    - Evaluate multi-core and multi-thread execution of llama.cpp on Arm CPUs.

prerequisites:
    - Basic understanding of llama.cpp
    - Understanding of transformer models
    - Knowledge of Arm Streamline usage
    - An Arm Neoverse or Cortex-A hardware platform running Linux or Android

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-09-15T21:27:17Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 49b58c9124cc76e2d884f0c0e95bffd2d7a9b4300f8ae9e31b362499bc95cc8f
  summary_generated_at: '2026-09-15T21:27:17Z'
  summary_source_hash: 49b58c9124cc76e2d884f0c0e95bffd2d7a9b4300f8ae9e31b362499bc95cc8f
  faq_generated_at: '2026-09-15T21:27:17Z'
  faq_source_hash: 49b58c9124cc76e2d884f0c0e95bffd2d7a9b4300f8ae9e31b362499bc95cc8f
  summary: >-
    You'll profile `llama.cpp` on Arm CPUs with Arm Streamline, including runs that use KleidiAI
    LLM kernels. First, you'll add marker annotations for prefill and decode phases and build `llama-cli`. Then, you'll prepare the
    model files and `gator` daemon, and capture traces. Finally, you'll inspect channel annotations
    and operator timing to distinguish pipeline stages and assess multi-core and
    multi-thread behavior during token generation.
  faqs:
  - question: How do I know that the marker annotations are working in Streamline?
    answer: >-
      During capture, look for marker annotations on the Streamline timeline. Each marker annotation is added
      before `llama_decode()` and records the start of a token-generation event. Marker annotations include
      values such as `past` and `n_eval`. If marker annotations don't appear, rebuild `llama.cpp` with the
      annotation changes and run the annotated `llama-cli`.
  - question: What do I need on the Arm target before starting a profiling capture?
    answer: >-
      Ensure that the `gator` daemon is configured and running on the Arm system. Place the built `llama-cli`
      and the required model files on the target so that Streamline can capture a representative run.
  - question: How do I differentiate prefill and decode phases in the results?
    answer: >-
      Use the inserted marker annotations to identify each stage in the Streamline timeline. Prefill is compute-intensive
      and decode is memory-bound, so compare their annotated ranges to understand where time is
      spent.
  - question: How can I analyze operator-level performance with channel annotations?
    answer: >-
      Enable channel annotations in the annotation integration so that Streamline displays separate lanes for
      grouped operations. Inspect the channel annotation lanes to see operator timing and overlaps during
      token generation.
  - question: How do I evaluate multi-core or multi-thread execution?
    answer: >-
      Capture a token generation run and use the marker and channel annotations to correlate work across
      cores and threads. Compare behavior during prefill and decode phases to see how execution is distributed.
# END generated_summary_faq

author: 
    - Zenon Zhilong Xiu
    - Odin Shen

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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
