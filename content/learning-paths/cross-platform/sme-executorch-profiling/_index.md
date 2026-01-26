---
title: Profile ExecuTorch models with SME2 on Arm

minutes_to_complete: 90

who_is_this_for: This is an advanced topic for developers and performance engineers deploying ExecuTorch models on Arm-based devices who need to understand and reduce end-to-end inference latency.

learning_objectives:
  - Understand how SME2 acceleration changes the performance profile of ExecuTorch models by reducing compute-bound bottlenecks.
  - Learn how to interpret operator-level and operator-category breakdowns (for example, convolution, GEMM, data movement, and other operators).
  - Identify which operators benefit most from SME2 acceleration and which operators become the new performance bottlenecks.
  - Apply a model-agnostic profiling workflow that can be reused across different models and deployments.
  - Make evidence-based optimization decisions by comparing execution profiles with SME2 enabled and disabled.

prerequisites:
  - An Apple Silicon macOS host with Python 3.9 or later and CMake 3.29 or later.
  - Basic familiarity with ExecuTorch or PyTorch.
  - Optionally, an Android device with Armv9 and SME2 support for on-device testing. If used, power management
    settings should be configured to ensure consistent performance measurements.
    
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
