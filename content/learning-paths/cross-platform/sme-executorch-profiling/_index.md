---
title: Profile ExecuTorch models with SME2 on Arm

minutes_to_complete: 90

description: Learn how to profile and optimize ExecuTorch models using SME2 acceleration on Arm platforms, including operator-level analysis and performance bottleneck identification.

who_is_this_for: This is an advanced topic for developers and performance engineers who deploy ExecuTorch models on Arm devices and want to understand and reduce inference latency.

learning_objectives:
  - Understand how SME2 acceleration changes the performance profile of ExecuTorch models by reducing compute-bound bottlenecks
  - Interpret operator-level and operator-category breakdowns (for example, convolution, GEMM, data movement, and other operators)
  - Identify which operators benefit most from SME2 acceleration and which operators become the new performance bottlenecks
  - Apply a model-agnostic profiling workflow that you reuse across different models and deployments
  - Make evidence-based optimization decisions by comparing execution profiles with SME2 enabled and disabled

prerequisites:
  - An Apple Silicon macOS host with Python 3.9 or later and CMake 3.29 or later
  - Basic familiarity with ExecuTorch or PyTorch
  - Optionally, an Android device with Armv9 and SME2 support for on-device testing (if used, configure power management settings to ensure consistent performance measurements)

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-29T16:50:36Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 36f7dfe13c8c940abbaad2b61620b3b1c6d97f580de15e573b45ef7760753797
  summary_generated_at: '2026-07-29T16:50:36Z'
  summary_source_hash: 36f7dfe13c8c940abbaad2b61620b3b1c6d97f580de15e573b45ef7760753797
  faq_generated_at: '2026-07-29T16:50:36Z'
  faq_source_hash: 36f7dfe13c8c940abbaad2b61620b3b1c6d97f580de15e573b45ef7760753797
  summary: >-
    You'll profile ExecuTorch models on Arm with SME2 acceleration using a repeatable workflow. You'll set up
    macOS, build SME2-enabled and SME2-disabled runner binaries, and export a model to `.pte`. You'll
    run timing-only and trace-enabled passes to capture operator and category breakdowns for convolution,
    GEMM, and data movement. Then, you'll compare the profiles to identify SME2 gains and new bottlenecks,
    and use structured agent skills to automate and validate the workflow.
  faqs:
  - question: How do I know SME2 acceleration is active in my run?
    answer: >-
      Build separate runner binaries with SME2 enabled and disabled, then compare their profiles.
      The operator-category breakdown shows whether the SME2-enabled run shifts time away from
      compute-bound operators.
  - question: What do I need in place before running the profiling steps?
    answer: >-
      Prepare an exported `.pte` model and two ExecuTorch runner binaries, one with SME2 enabled and
      one with SME2 disabled. Complete model-specific input and output handling during onboarding.
  - question: What result should I expect from the timing-only and trace-enabled runs?
    answer: >-
      The timing-only run provides end-to-end latency. The trace-enabled run produces operator-level
      and operator-category breakdowns for pinpointing bottlenecks.
  - question: Where can I find a concrete example of model onboarding and export?
    answer: >-
      Use `executorch/examples/models/efficient_sam` as a model-onboarding example. It demonstrates
      the full process, including input and output details, and provides a template for your model.
  - question: How do the agent skills help automate this workflow?
    answer: >-
      Agent skills define inputs, actions, expected outputs, and validation checks for each profiling
      task. Use them with an AI coding assistant or CI to run the pipeline and verify required artifacts
      and checks.
# END generated_summary_faq

author:
    - Jason Zhu
    - Tyler Mullenbach
    - Damien Dooley

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
subjects: ML
armips:
  - Cortex-A
  - Arm C1
tools_software_languages:
  - ExecuTorch
  - Python
  - CMake
  - SME2
operatingsystems:
  - macOS
  - Android

shared_path: true
shared_between:
    - laptops-and-desktops
    - mobile-graphics-and-gaming

further_reading:
  - resource:
      title: ExecuTorch documentation
      link: https://docs.pytorch.org/executorch/stable/index.html
      type: documentation
  - resource:
      title: Arm SME2 overview
      link: https://www.arm.com/technologies/sme2
      type: documentation
  - resource:
      title: Arm Kleidi kernels
      link: https://www.arm.com/markets/artificial-intelligence/software/kleidi
      type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---
