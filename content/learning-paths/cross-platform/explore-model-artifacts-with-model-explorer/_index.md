---
title: Visualize ExecuTorch, TOSA, and VGF artifacts with Google Model Explorer and Arm extensions
    
description: Inspect ExecuTorch PTE, TOSA, VGF, ETRecord, and ETDump model artifacts with Google Model Explorer and Arm extensions.

minutes_to_complete: 90

who_is_this_for: This Learning Path is for Edge AI developers who need to inspect model artifacts after backend delegation, understand graph structure and delegate coverage, and use those insights to reason about performance and behavior.

learning_objectives:
  - Set up Google Model Explorer with the combined ExecuTorch extension and separate Tensor Operator Set Architecture (TOSA) and VGF adapters. 
  - Open ExecuTorch deployment graphs and inspect delegate regions, work outside delegates, graph fragmentation, and backend-specific changes
  - Trace model transformations across PTE, TOSA, and VGF artifacts
  - Use ETRecord and ETDump overlays to connect exported graph structure with runtime profiling data

prerequisites:
  - Python 3.10, 3.11, or 3.12
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

further_reading:
  - resource:
      title: Google Model Explorer
      link: https://github.com/google-ai-edge/model-explorer
      type: repository
  - resource:
      title: ExecuTorch extension for Model Explorer
      link: https://github.com/arm/executorch-extension-model-explorer
      type: repository
  - resource:
      title: PTE adapter for Model Explorer
      link: https://github.com/arm/pte-adapter-model-explorer
      type: repository
  - resource:
      title: ETRecord adapter for Model Explorer
      link: https://github.com/arm/etrecord-adapter-model-explorer
      type: repository
  - resource:
      title: ETDump data provider for Model Explorer
      link: https://github.com/arm/etdump-data-provider-model-explorer
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
