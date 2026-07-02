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
  generated_at: '2026-07-02T17:53:39Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: e835a550c955b13805c7859ff64e3b8d7fdee68222569225c53a0f15db72f046
  summary_generated_at: '2026-07-02T17:53:39Z'
  summary_source_hash: e835a550c955b13805c7859ff64e3b8d7fdee68222569225c53a0f15db72f046
  faq_generated_at: '2026-07-02T17:53:39Z'
  faq_source_hash: e835a550c955b13805c7859ff64e3b8d7fdee68222569225c53a0f15db72f046
  summary: >-
    This Learning Path shows how to deploy ERNIE‑4.5 Mixture of Experts models on an Armv9 development
    board using llama.cpp, verify on‑device inference, and evaluate model behavior. Learners configure
    the environment, run ERNIE‑4.5 PT and Thinking variants, and validate multilingual outputs.
    The path then contrasts the two models’ inference styles and demonstrates how to inspect internal
    MoE expert routing during generation. Finally, learners build and benchmark two configurations—a
    baseline CPU build and an Armv9‑optimized build that enables SVE, i8mm, and dotprod instructions—to
    compare results and understand the impact of Armv9 hardware features on MoE inference.
  faqs:
  - question: What should I verify after setting up llama.cpp on the Armv9 board?
    answer: >-
      Confirm that the build completes and a simple inference runs successfully on the device.
      The steps use a Radxa Orion O6 as an example platform to validate that inference is working
      end‑to‑end.
  - question: Which ERNIE‑4.5 variant should I run for my task?
    answer: >-
      Use PT for general‑purpose, multilingual tasks. Use the Thinking variant for multi‑step
      reasoning where more deliberate output is preferred.
  - question: How do I check that multilingual inference is working correctly?
    answer: >-
      Run the Thinking variant with prompts in more than one language and confirm that the outputs
      are coherent and relevant. The steps explicitly validate multilingual responses as part
      of the setup.
  - question: How do I compare PT and Thinking behavior and observe MoE expert routing?
    answer: >-
      Run the same task with both models and compare the differences in output style. Use the
      routing inspection described in the comparison step to see which experts activate per token;
      both models share about 21B parameters with roughly 3B active at runtime.
  - question: How do I benchmark Armv9 optimizations and interpret the results?
    answer: >-
      Run two scenarios: a baseline CPU build and an Armv9‑optimized build with SVE, i8mm, and
      dotprod enabled, then record both results. You should see a measurable difference between
      the runs; if not, verify you used the Armv9‑specific build and repeat the test.
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

