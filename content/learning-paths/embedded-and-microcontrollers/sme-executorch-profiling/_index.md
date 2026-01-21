---
title: Profiling ExecuTorch models with SME2 acceleration
minutes_to_complete: 90
who_is_this_for: Developers and performance engineers deploying ExecuTorch models on Arm devices who face latency challenges or want to use more advanced models. When end-to-end latency isn't meeting targets, operator-level profiling is the essential first step to understand where time is spent and make informed optimization decisions. This learning path guides you through profiling with SME2 acceleration to identify optimization opportunities and achieve better performance.
learning_objectives:
  - Understand how SME2 acceleration transforms ML performance by revealing operator-level bottlenecks that were previously hidden behind compute constraints
  - Learn to interpret operator-category breakdowns (CONV/GEMM/Data Movement/Other) and use them to identify which operators benefit most from acceleration and which become the new bottlenecks
  - Build confidence in applying a model-agnostic profiling workflow to your own model, enabling consistent performance analysis across your model portfolio
  - Discover the strategic insight that faster compute (via SME2) shifts optimization focus from compute-bound operations to data movement, fundamentally changing your optimization priorities
  - Develop the ability to make evidence-based optimization decisions by comparing SME2-on versus SME2-off profiles, moving from guesswork to data-driven performance improvements
prerequisites:
  - Apple Silicon macOS host with Python 3.9+ and CMake 3.29+
  - Basic ExecuTorch or PyTorch familiarity
  - "Optional: Armv9 Android device with SME2 for device runs"
author: Jason Zhu, Tyler Mullenbach, Damien Dooley 

### Tags
skilllevels: Advanced
subjects: ML
armips:
  - Cortex-A
tools_software_languages:
  - ExecuTorch
  - Python
  - CMake
operatingsystems:
  - macOS
  - Android

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
