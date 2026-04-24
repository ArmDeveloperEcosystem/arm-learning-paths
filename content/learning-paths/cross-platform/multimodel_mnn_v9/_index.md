---
title: Build a Multimodal Retail Restocking Assistant on Armv9 With MNN

    
minutes_to_complete: 90

who_is_this_for: This learning path is for developers and engineers who want to run multimodal image, audio, and text models on Armv9 Linux systems using MNN as a portable, CPU-first inference runtime. It is aimed at readers who are comfortable building software from source and want a reproducible on-device workflow without quantization or heterogeneous scheduling.

description: Learn how to build MNN on an Armv9 system, run text, vision, and audio prompts with a multimodal Omni model, and combine image and audio inputs into a single-shot retail restock ticket workflow.

learning_objectives:
    - Build MNN natively on an Armv9 Linux system for multimodal inference
    - Verify a CPU-only Omni model workflow with text, vision, and audio prompts
    - Create a reproducible multimodal application flow that combines image and audio inputs into an actionable restock ticket

prerequisites:
    - An Armv9 Linux device with at least 32 GB of available disk space, for example a Radxa Orion O6
    - Familiarity with the Linux command line, Git, and building C++ projects with CMake
    - Internet access to download source code, model assets, and sample data

author: Odin Shen

### Tags
skilllevels: Advanced
subjects: ML
armips:
    - Cortex-A
operatingsystems:
    - Linux
tools_software_languages:
    - CMake
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
        title: MNN GitHub repository
        link: https://github.com/alibaba/MNN
        type: website
    - resource:
        title: ModelScope model hub
        link: https://modelscope.cn/models
        type: website
    - resource:
        title: KleidiAI explainer
        link: /learning-paths/cross-platform/kleidiai-explainer/
        type: website
    - resource:
        title: Install CMake
        link: /install-guides/cmake/
        type: website
    - resource:
        title: Vision LLM inference on Android with KleidiAI and MNN
        link: /learning-paths/mobile-graphics-and-gaming/vision-llm-inference-on-android-with-kleidiai-and-mnn/
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
