---
title: How to Benchmark a Single KleidiAI Micro-kernel in ExecuTorch

minutes_to_complete: 30

who_is_this_for: This article is intended for advanced developers who want to leverage KleidiAI to accelerate ExecuTorch model inference on the AArch64 platform.

learning_objectives:
  - Cross-compile ExecuTorch for the ARM64 platform with XNNPACK and KleidiAI enabled, including SME/SME2 support.
  - Build and export ExecuTorch models that can be accelerated by KleidiAI using SME/SME2 instructions.
  - Use the `executor_runner` tool to collect ETDump profiling data.
  - Inspect and analyze ETRecord and ETDump files using the ExecuTorch Inspector API.

prerequisites:
  - An x86_64 Linux host machine running Ubuntu, with at least 15 GB of free disk space.
  - An Arm64 target system with support for SME or SME2.

author: Qixiang Xu

### Tags
skilllevels: Advanced
subjects: ML
armips:
    - Cortex-A
    - SME
    - Kleidai

tools_software_languages:
    - Python
    - cmake
    - XNNPACK

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
