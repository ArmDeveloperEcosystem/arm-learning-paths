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
    

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T21:52:19Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 36f7dfe13c8c940abbaad2b61620b3b1c6d97f580de15e573b45ef7760753797
  summary_generated_at: '2026-06-01T21:19:22Z'
  summary_source_hash: 36f7dfe13c8c940abbaad2b61620b3b1c6d97f580de15e573b45ef7760753797
  faq_generated_at: '2026-06-02T21:52:19Z'
  faq_source_hash: 36f7dfe13c8c940abbaad2b61620b3b1c6d97f580de15e573b45ef7760753797
  summary: >-
    This advanced Learning Path shows how to profile ExecuTorch models on Arm with SME2 acceleration
    in approximately 90 minutes. You will set up a reusable Apple Silicon macOS workspace (Python
    3.9+ and CMake 3.29+), build ExecuTorch runner binaries with SME2 enabled and disabled, export
    PyTorch models to .pte, and run a two-pass analysis (timing-only and then trace-enabled).
    The model-agnostic workflow produces operator-level and operator-category breakdowns (for
    example, convolution, GEMM, data movement) so you can see how latency shifts when compute
    speeds up under SME2. Optionally, you can run on an Android Armv9 device with SME2 after configuring
    power management for consistent measurements. By the end, you can compare execution profiles
    and make evidence-based optimization decisions.
  faqs:
  - question: What do I need on my host machine before starting the setup?
    answer: >-
      Use an Apple Silicon macOS system with Python 3.9 or later and CMake 3.29 or later. Basic
      familiarity with ExecuTorch or PyTorch is expected.
  - question: Do I need an Android device, and how should it be configured if I use one?
    answer: >-
      An Android device is optional and should have Armv9 with SME2 support for on-device testing.
      If you use one, configure its power management settings to keep performance measurements
      consistent.
  - question: Which model format should I export, and is the profiling pipeline model-specific?
    answer: >-
      Export your model to ExecuTorch .pte format. After that, the same runners, scripts, and
      analysis steps apply regardless of model architecture; see the EfficientSAM example in executorch/examples/models
      for a concrete onboarding reference.
  - question: How do I collect profiling data for comparison?
    answer: >-
      Build ExecuTorch runner binaries with SME2 enabled and disabled, then run the two-run analysis
      consisting of a timing-only pass and a trace-enabled pass. The Learning Path also provides
      structured agent skills that you can use to automate these actions in an AI assistant or
      CI system.
  - question: What result should I expect when enabling SME2, and how do I interpret the profiles?
    answer: >-
      Inference latency often improves significantly with SME2 enabled, which can shift execution
      time to other parts of the model. Use the operator-level and operator-category breakdowns
      to identify which operators benefit most and which become the new bottlenecks.
# END generated_summary_faq

author: Jason Zhu, Tyler Mullenbach, Damien Dooley 

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

