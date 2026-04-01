---
title: Multimodal On-Device Inference on Armv9 with MNN for Audio and Vision

minutes_to_complete: 60

who_is_this_for: This is a multimodal use case topic for developers and engineers who want to eploy multimodal (image + audio + text) models on Armv9 edge devices and use MNN as a portable, CPU-first inference runtime to build a reproducible, CPU-only workflow without quantization or heterogeneous scheduling

description: Learn how to deploy Multimodal models on Armv9 devices using MNN, compare PT and Thinking variants, and measure Armv9-specific hardware optimization impact.

learning_objectives:
    - Deploy Multimodal models on edge devices using MNN
    - Apply image and audio with PoC on Arm v9 CPU

prerequisites:
    - An Armv9 device with at least 32 GB of available disk space, for example, Radxa Orion O6

author: Odin Shen

### Tags
skilllevels: Advanced
subjects: ML
armips:
    - Cortex-A
operatingsystems:
    - Linux
tools_software_languages:
    - Python
    - CPP
    - Bash

### Cross-platform metadata only
shared_path: true
shared_between:
    - laptops-and-desktops
    - servers-and-cloud-computing
    - mobile-graphics-and-gaming

further_reading:
    - resource:
        title: MNN Modelscope
        link: 
        type: website
    - resource:
        title: 
        link: 
        type: website
    - resource:
        title: Run ERNIE-4.5 Mixture of Experts model on Armv9 with llama.cpp
        link: /learning-paths/cross-platform/ernie_moe_v9/

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
