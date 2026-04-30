---
title: Benchmark a KleidiAI micro-kernel in ExecuTorch
description: Learn how to benchmark KleidiAI micro-kernels in ExecuTorch using SME/SME2 instructions on Arm64 platforms with ETDump profiling and analysis.

minutes_to_complete: 30

who_is_this_for: This is an advanced topic for developers, performance engineers, and ML framework contributors who want to benchmark and optimize KleidiAI micro-kernels within ExecuTorch to accelerate model inference on Arm64 platforms supporting SME/SME2 instructions.

learning_objectives:
  - Cross-compile ExecuTorch for Arm64 with XNNPACK and KleidiAI enabled, including SME/SME2 instructions
  - Build and export ExecuTorch models that can be accelerated by KleidiAI using SME/SME2 instructions
  - Use the executor_runner tool to run kernel workloads and collect ETDump profiling data.
  - Inspect and analyze ETRecord and ETDump files using the ExecuTorch Inspector API to understand kernel-level performance behavior.

prerequisites:
  - An x86_64 Linux host machine running Ubuntu, with at least 15 GB of free disk space
  - An Arm64 target system with support for SME or SME2 - see the Learning Path [Devices with native SME2 support](/learning-paths/cross-platform/multiplying-matrices-with-sme2/1-get-started/#devices)

generate_summary_faq: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-04-30T18:58:17Z'
  generator: template
  source_hash: b55d902389806f5e84e674e5ba1f1f2d9e38af370c289ad344eff2dad3475df1
  summary: >-
    Learn how to benchmark KleidiAI micro-kernels in ExecuTorch using SME/SME2 instructions on
    Arm64 platforms with ETDump profiling and analysis. It is designed for developers, performance
    engineers, and ML framework contributors who want to benchmark and optimize KleidiAI micro-kernels
    within ExecuTorch to accelerate model inference on Arm64 platforms supporting SME/SME2 instructions.
    By the end, you will be able to cross-compile ExecuTorch for Arm64 with XNNPACK and KleidiAI
    enabled, including SME/SME2 instructions, build and export ExecuTorch models that can be accelerated
    by KleidiAI using SME/SME2 instructions, and use the executor_runner tool to run kernel workloads
    and collect ETDump profiling data. It focuses on tools and technologies such as Python, ExecuTorch,
    XNNPACK, and KleidiAI, Linux environments, and Arm platforms including Cortex-A. The main
    steps cover Set up your environment, Cross-Compile ExecuTorch for the AArch64 platform, Accelerate
    ExecuTorch operators with KleidiAI micro-kernels, Create and quantize linear layer benchmark
    model, and Create and quantize convolution layer benchmark model.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will cross-compile ExecuTorch for Arm64 with XNNPACK and KleidiAI enabled, including
      SME/SME2 instructions, build and export ExecuTorch models that can be accelerated by KleidiAI
      using SME/SME2 instructions, and use the executor_runner tool to run kernel workloads and
      collect ETDump profiling data. Learn how to benchmark KleidiAI micro-kernels in ExecuTorch
      using SME/SME2 instructions on Arm64 platforms with ETDump profiling and analysis.
  - question: Who is this Learning Path for?
    answer: >-
      This is an advanced topic for developers, performance engineers, and ML framework contributors
      who want to benchmark and optimize KleidiAI micro-kernels within ExecuTorch to accelerate
      model inference on Arm64 platforms supporting SME/SME2 instructions.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: An x86_64 Linux host machine running
      Ubuntu, with at least 15 GB of free disk space; An Arm64 target system with support for
      SME or SME2 - see the Learning Path [Devices with native SME2 support](/learning-paths/cross-platform/multiplying-matrices-with-sme2/1-get-started/#devices).
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including Python, ExecuTorch, XNNPACK, and KleidiAI, Linux
      environments, and Arm platforms such as Cortex-A.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Set up your environment, Cross-Compile ExecuTorch
      for the AArch64 platform, Accelerate ExecuTorch operators with KleidiAI micro-kernels, Create
      and quantize linear layer benchmark model, and Create and quantize convolution layer benchmark
      model.
# END generated_summary_faq

author: Qixiang Xu

### Tags
skilllevels: Advanced
subjects: ML
armips:
    - Cortex-A

tools_software_languages:
    - Python
    - ExecuTorch
    - XNNPACK
    - KleidiAI

operatingsystems:
    - Linux


further_reading:
    - resource:
        title: Executorch User Guide 
        link: https://docs.pytorch.org/executorch/stable/intro-section.html
        type: documentation



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

