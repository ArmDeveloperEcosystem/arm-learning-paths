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

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T23:56:51Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: b55d902389806f5e84e674e5ba1f1f2d9e38af370c289ad344eff2dad3475df1
  summary_generated_at: '2026-06-02T02:51:58Z'
  summary_source_hash: b55d902389806f5e84e674e5ba1f1f2d9e38af370c289ad344eff2dad3475df1
  faq_generated_at: '2026-06-02T23:56:51Z'
  faq_source_hash: b55d902389806f5e84e674e5ba1f1f2d9e38af370c289ad344eff2dad3475df1
  summary: >-
    This Learning Path shows how to benchmark KleidiAI micro-kernels in ExecuTorch on Arm64 platforms
    that support SME or SME2. You will set up an isolated Python environment on an x86_64 Ubuntu
    host, cross-compile ExecuTorch for AArch64 with XNNPACK and KleidiAI (including SME/SME2),
    and build and export quantized benchmark models for Fully Connected and Conv2d operators.
    On an Arm64 target with SME/SME2, you will run workloads with executor_runner, measure throughput
    and latency, and collect ETDump traces. You will then use the ExecuTorch Inspector API to
    inspect ETRecord and ETDump files to understand kernel-level behavior across GEMM variants.
    Prerequisites are explicitly listed in the path.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need an x86_64 Linux host running Ubuntu with at least 15 GB of free disk space and
      an Arm64 target device that supports SME or SME2. The path targets Linux environments.
  - question: Should I use a Python virtual environment, and how long should it stay active?
    answer: >-
      Yes. Create and activate a Python virtual environment before building ExecuTorch, and keep
      it activated while completing the steps so dependencies install and run in the correct location.
  - question: Which toolchain should I install to cross-compile ExecuTorch for AArch64?
    answer: >-
      Install the GNU Arm cross-compilation toolchain on your x86_64 host along with Ninja as
      the CMake build backend. The path cross-compiles ExecuTorch with XNNPACK and KleidiAI enabled
      for the Arm64 target.
  - question: How do I know if KleidiAI micro-kernels are being used for my operators?
    answer: >-
      ExecuTorch automatically dispatches to KleidiAI within XNNPACK when an operator’s data types
      and quantization match supported configurations. You can confirm by collecting ETDump data
      and inspecting it with the ExecuTorch Inspector API.
  - question: What results should I expect after running executor_runner?
    answer: >-
      executor_runner runs kernel workloads and collects ETDump profiling data. Use the ExecuTorch
      Inspector API to examine ETRecord and ETDump files and review kernel-level behavior, along
      with throughput and latency measurements produced during the runs.
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

