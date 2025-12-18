---
title: Benchmark a KleidiAI micro-kernel in ExecuTorch

minutes_to_complete: 30

who_is_this_for: This is an advanced topic for developers, performance engineers, and ML framework contributors who want to benchmark and optimize KleidiAI micro-kernels within ExecuTorch to accelerate model inference on Arm64 platforms supporting SME/SME2 instructions.

learning_objectives:
  - Cross-compile ExecuTorch for Arm64 with XNNPACK and KleidiAI enabled, including SME/SME2 instructions
  - Build and export ExecuTorch models that can be accelerated by KleidiAI using SME/SME2 instructions
  - Use the executor_runner tool to run kernel workloads and collect ETDump profiling data.
  - Inspect and analyze ETRecord and ETDump files using the ExecuTorch Inspector API to understand kernel-level performance behavior.

prerequisites:
  - An x86_64 Linux host machine running Ubuntu, with at least 15 GB of free disk space
  - An Arm64 target system with support for SME or SME2 - see the Learning Path [Devices with native SME2 support](/learning-paths/cross-platform/multiplying-matrices-with-sme2/1-get-started/#devices-with-native-sme2-support)

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
