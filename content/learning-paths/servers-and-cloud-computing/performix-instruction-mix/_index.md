---
title: Profile GPT-2 inference with the Arm Performix Instruction Mix recipe

description: Profile GPT-2 inference on Arm Neoverse with the Arm Performix Instruction Mix recipe, identify scalar versus vector execution patterns, and improve throughput with Neon, SVE, and KleidiAI kernels.

minutes_to_complete: 45

who_is_this_for: This is an introductory topic for developers who want to get started using the Arm Performix Instruction Mix recipe through a practical example.

learning_objectives: 
    - Use the Instruction Mix recipe to combine static disassembly with runtime sampling to show execution behavior
    - Build and run the GPT-2 inference example on an Arm Linux server
    - Identify why matrix multiplication dominates runtime and how vectorization changes the instruction mix
    - Compare throughput and instruction mix across scalar, Neon, SVE, and KleidiAI implementations

prerequisites:
    - Access to Arm Performix configured with a remote Arm Linux target. For setup, see the [Arm Performix install guide](/install-guides/performix/).
    - Basic understanding of C++ and compiler optimization
    - Basic understanding of matrix multiplication
    - Basic understanding of writing SIMD code with Neon or SVE

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-15T19:50:40Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 22b8b268d361bfa326a92845a7a0878e26719ef182c3e907fd6da5dcd5503388
  summary_generated_at: '2026-07-15T19:50:40Z'
  summary_source_hash: 22b8b268d361bfa326a92845a7a0878e26719ef182c3e907fd6da5dcd5503388
  faq_generated_at: '2026-07-15T19:50:40Z'
  faq_source_hash: 22b8b268d361bfa326a92845a7a0878e26719ef182c3e907fd6da5dcd5503388
  summary: >-
    You'll build a GPT-2 inference example on an Arm Linux target and use Arm Performix to analyze
    execution behavior. After running the Code Hotspots recipe to locate the dominant `matmul`
    kernel, you'll use the Instruction Mix recipe to compare scalar and vector execution patterns
    on Arm Neoverse. You'll then compare the scalar `gpt2` baseline with `gpt2_neon`, `gpt2_sve`,
    optional `gpt2_user`, and the KleidiAI-backed `gpt2_kai_sve` path, validating vectorization
    and throughput changes with Performix data and tokens-per-second results.
  faqs:
  - question: Which Performix recipe should I run first to find the bottleneck?
    answer: >-
      Start with the Code Hotspots recipe. Set the launch command to the baseline binary and use
      `-n 150` to bias the profile toward inference time, then review the top functions.
  - question: How do I know that matrix multiplication is the hotspot before I change any code?
    answer: >-
      The Code Hotspots report ranks functions by sampled time, so `kernels::matmul_ref()` should appear
      near the top. Use that evidence to decide where to focus subsequent Instruction Mix profiling.
  - question: Where do I add my Neon or SVE intrinsics, and what part of the loop should I change?
    answer: >-
      Edit `src/kernels/matmul_user.cpp`. Focus on the accumulation loop, `acc += row[j] * x[j];`,
      and consider lane utilization, loop unrolling, and how you handle the tail.
  - question: What binaries should I expect after building, and where are the reference implementations?
    answer: >-
      The build produces the scalar baseline `gpt2`, reference variants `gpt2_neon` and `gpt2_sve`,
      and `gpt2_user` when the user kernel is enabled. The reference kernels are implemented in
      `matmul_neon.cpp` and `matmul_sve.cpp`.
  - question: How do I verify that my vectorization worked using Performix?
    answer: >-
      Profile your rebuilt binary with the Instruction Mix recipe and compare the proportion of
      vector instructions with the baseline. You can also run the reference `gpt2_neon` and `gpt2_sve`
      and compare instruction mix and the program's tokens-per-second summary.
# END generated_summary_faq

author:
    - Kieran Hejmadi
    - Oliver Grainge

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
armips:
    - Neoverse
tools_software_languages:
    - Arm Performix
    - C
    - LLM
    - Neon
    - SVE
operatingsystems:
    - Linux
further_reading:
    - resource:
        title: Arm Performix User Guide
        link: https://developer.arm.com/documentation/110163/latest
        type: documentation
    - resource:
        title: Find code hotspots with Arm Performix
        link: /learning-paths/servers-and-cloud-computing/cpu_hotspot_performix/
        type: learning-path
    - resource:
        title: Identify code hotspots using Arm Performix through the Arm MCP Server
        link: /learning-paths/servers-and-cloud-computing/performix-mcp-agent/
        type: learning-path
    - resource:
        title: Arm MCP Server GitHub Repository
        link: https://github.com/arm/mcp
        type: website
    - resource:
        title: KleidiAI GitHub Repository
        link: https://gitlab.arm.com/kleidi/kleidiai
        type: website
    - resource:
        title: GPT-2 Example repository
        link: https://github.com/arm-education/GPT-2-Example
        type: website



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
