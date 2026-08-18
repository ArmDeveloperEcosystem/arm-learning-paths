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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-17T22:07:35Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 0db365140107125f0dd330363a00a5790214a12c859fb5cd573a8d66af4293c3
  summary_generated_at: '2026-08-17T22:07:35Z'
  summary_source_hash: 0db365140107125f0dd330363a00a5790214a12c859fb5cd573a8d66af4293c3
  faq_generated_at: '2026-08-17T22:07:35Z'
  faq_source_hash: 0db365140107125f0dd330363a00a5790214a12c859fb5cd573a8d66af4293c3
  summary: >-
    You'll cross-compile ExecuTorch with XNNPACK and KleidiAI for an `aarch64` SME or SME2 system.
    Create quantized Fully Connected and Conv2d benchmark models that can use KleidiAI, then run
    them with `executor_runner`. Inspect ETRecord and ETDump traces with the ExecuTorch Inspector API
    to validate kernel selection and compare behavior across variants.
  faqs:
  - question: Do I need to keep my Python virtual environment active while building and exporting
      models?
    answer: >-
      Yes. Keep your virtual environment active so build and runtime dependencies install and
      import from the same isolated location.
  - question: What should I check on the Arm64 target before I run benchmarks?
    answer: >-
      Verify the device supports SME or SME2; the prerequisites link lists devices with native
      SME2 support. Also confirm you deploy the AArch64 ExecuTorch binaries and libraries produced
      by cross-compilation.
  - question: Which configurations will make my operators use KleidiAI micro-kernels?
    answer: >-
      Use operator data types and quantization settings that match KleidiAI-supported paths in
      XNNPACK. The benchmark models focus on Fully Connected and INT8 Conv2d (including 1×1) with
      GEMM variants designed to exercise KleidiAI micro-kernels.
  - question: What output should I expect from `executor_runner`, and how do I confirm it captured
      profiling data?
    answer: >-
      `executor_runner` produces performance measurements such as throughput and latency and writes
      `ETDump` and `ETRecord` profiling data. Use the ExecuTorch Inspector API to open those files and
      verify which kernels executed and their behavior.
  - question: I tested multiple GEMM variants but see little difference. What should I review
      before rerunning?
    answer: >-
      Confirm you are running on SME/SME2-capable hardware and that your build enables XNNPACK
      and KleidiAI with SME/SME2. Ensure the models are quantized and use operator configurations
      that map to KleidiAI micro-kernels, then re-run and compare `ETDump` traces.
# END generated_summary_faq

author: Qixiang Xu

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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
