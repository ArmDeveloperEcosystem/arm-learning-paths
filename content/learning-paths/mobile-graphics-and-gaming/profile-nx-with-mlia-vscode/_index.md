---
title: Capture and analyze neural accelerator (NX) profiling data with MLIA for VS Code

draft: true
cascade:
    draft: true

description: Profile a small neural upscaling model on an Android neural accelerator and use MLIA for VS Code to inspect cycle costs and follow graph operations to Python source.

minutes_to_complete: 90

who_is_this_for: >-
    You're a machine learning or graphics developer investigating model performance on Arm neural accelerators (NX).

learning_objectives:
    - Export a small neural upscaling model with Python debug information
    - Capture one NX dispatch with Android Scenario Runner
    - Inspect measured cycle costs in Model Explorer
    - Follow graph operations to Python source in VS Code

prerequisites:
    - An x86-64 Ubuntu 24.04 LTS host with internet access and permission to install development tools
    - Visual Studio Code 1.100 or later on the host
    - An NX-capable Android device with USB debugging. See the [MLIA for VS Code device requirements](https://github.com/arm/vscode-mlia/blob/main/docs/users/installation.md#requirements)
    - Python 3.12 with virtual environment support, Android Debug Bridge (ADB), curl, and tar on the host
    - Familiarity with Bash, ADB, and PyTorch model export

author: Matthew Sloyan

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

skilllevels: Advanced
subjects: ML
armips:
    - Mali
tools_software_languages:
    - MLIA
    - NX
    - Visual Studio Code
    - Model Explorer
    - ExecuTorch
    - Python
    - VGF
    - Vulkan
operatingsystems:
    - Linux
    - Android

further_reading:
    - resource:
        title: Quantize neural upscaling models with ExecuTorch
        link: /learning-paths/mobile-graphics-and-gaming/quantize-neural-upscaling-models/
        type: learningpath
    - resource:
        title: MLIA for VS Code user guide
        link: https://github.com/arm/vscode-mlia/blob/main/docs/users/README.md
        type: documentation
    - resource:
        title: Neural Statistics Vulkan layer
        link: https://github.com/arm/vulkan-layer-neural-statistics
        type: repository
    - resource:
        title: ML SDK for Vulkan
        link: https://github.com/arm/ai-ml-sdk-manifest
        type: repository
    - resource:
        title: Estimate neural accelerator performance with ML Inference Advisor
        link: /learning-paths/mobile-graphics-and-gaming/mlia-nx-performance-estimator/
        type: learningpath
    - resource:
        title: Analyze Ethos-U models with MLIA
        link: /learning-paths/embedded-and-microcontrollers/analyze-ethos-u-models-with-mlia/
        type: learningpath

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1
layout: learningpathall
learning_path_main_page: "yes"
---
