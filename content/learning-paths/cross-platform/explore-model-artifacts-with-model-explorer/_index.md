---
title: Visualize ExecuTorch PTE, TOSA, VGF, ETRecord, and ETDump artifacts with Google's Model Explorer

draft: true
cascade:
    draft: true

description: Learn how to inspect ExecuTorch PTE, TOSA, VGF, ETRecord, and ETDump model artifacts with Google Model Explorer and Arm adapters.

minutes_to_complete: 90

who_is_this_for: This learning path is for Edge AI developers who need to inspect model artifacts after backend delegation, understand graph structure and delegate coverage, and use those insights to reason about performance and behavior.

learning_objectives:
  - Explain what Google Model Explorer is and how adapters add support for Arm model artifacts
  - Install Model Explorer, launch it with the PTE, TOSA, and VGF adapters, and use the runtime overlay extension for ETRecord and ETDump
  - Open ExecuTorch .pte files and compare portable CPU, XNNPACK CPU, and Ethos-U artifacts
  - Use PTE visualization to reason about delegate regions, work outside delegates, graph fragmentation, and backend-specific changes
  - Inspect TOSA flatbuffers as an intermediate representation used by Arm compiler and backend workflows
  - Inspect VGF artifacts for Vulkan ML and neural graphics workloads
  - Use ETRecord and ETDump overlays to connect exported graph structure with runtime profiling data

prerequisites:
  - Python 3.10 or later
  - Basic familiarity with PyTorch, ExecuTorch, or model deployment workflows

author:
  - Matt Cossins

### Tags
skilllevels: Introductory
subjects: ML
armips:
  - Cortex-A
  - Cortex-M
  - Ethos-U
  - Mali
tools_software_languages:
  - Model Explorer
  - ExecuTorch
  - PyTorch
  - Python
  - TOSA
  - VGF
  - ETRecord
  - ETDump
  
operatingsystems:
  - Linux
  - macOS
  - Windows

shared_path: true
shared_between:
  - embedded-and-microcontrollers
  - mobile-graphics-and-gaming
  - ai

further_reading:
  - resource:
      title: Google Model Explorer
      link: https://github.com/google-ai-edge/model-explorer
      type: repository
  - resource:
      title: PTE adapter for Model Explorer
      link: https://github.com/arm/pte-adapter-model-explorer
      type: repository
  - resource:
      title: TOSA adapter for Model Explorer
      link: https://github.com/arm/tosa-adapter-model-explorer
      type: repository
  - resource:
      title: VGF adapter for Model Explorer
      link: https://github.com/arm/vgf-adapter-model-explorer
      type: repository
  - resource:
      title: ExecuTorch documentation
      link: https://docs.pytorch.org/executorch/stable/index.html
      type: documentation
  - resource:
      title: ExecuTorch ETRecord
      link: https://docs.pytorch.org/executorch/stable/etrecord.html
      type: documentation
  - resource:
      title: ExecuTorch ETDump
      link: https://docs.pytorch.org/executorch/stable/etdump.html
      type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---
