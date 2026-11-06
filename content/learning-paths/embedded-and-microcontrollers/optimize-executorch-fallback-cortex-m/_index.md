---
title: Optimize ML model deployment on microcontrollers with CMSIS-NN kernels

description: Build an ExecuTorch 1.5.1 application from the published ExecuTorch CMSIS Pack, that uses CMSIS-NN for optimized Cortex-M fallback.

minutes_to_complete: 60

who_is_this_for: This Learning Path is for embedded machine learning developers building ExecuTorch applications for Cortex-M CPUs and Ethos-U NPUs.

learning_objectives:
    - Export an ExecuTorch graph with Ethos-U, CMSIS-NN, and portable-kernel execution regions
    - Lower quantized CPU fallback operations to optimized CMSIS-NN-backed Cortex-M operators, and understand the benefits in doing so
    - Install and consume the published ExecuTorch CMSIS Pack for version 1.5.1 with selected runtime and operator components
    - Run an application built from the ExecuTorch CMSIS Pack on a Corstone-300 Ethos-U55 FVP
    - Understand when and why to use the ExecuTorch CMSIS Pack

prerequisites:
    - Git, VS Code, and Python 3.10 to 3.13 on Windows, macOS, or x86-64 Linux
    - Docker Desktop for FVP simulation on macOS
    - An internet connection and command-line access
    - Familiarity with PyTorch
    - Basic familiarity with Cortex-M processors and Ethos-U NPUs

author:
- Matt Cossins
- Kwashie Andoh

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false
test_maintenance: false

### Tags
skilllevels: Introductory
subjects: ML
armips:
    - Cortex-M
    - Ethos-U
operatingsystems:
    - Linux
    - Windows
    - macOS
tools_software_languages:
    - Python
    - PyTorch
    - ExecuTorch
    - CMSIS
    - CMSIS Pack
    - CMSIS-NN
    - FVP
    - vcpkg

further_reading:
    - resource:
        title: CMSIS-Executorch example project
        link: https://github.com/Arm-Examples/CMSIS-Executorch
        type: documentation
    - resource:
        title: Published ExecuTorch CMSIS Pack
        link: https://www.keil.arm.com/packs/executorch-pytorch/overview/
        type: documentation
    - resource:
        title: ExecuTorch Arm Cortex-M backend
        link: https://docs.pytorch.org/executorch/stable/backends/arm-cortex-m/arm-cortex-m-overview.html
        type: documentation
    - resource:
        title: ExecuTorch Arm Ethos-U backend
        link: https://docs.pytorch.org/executorch/stable/backends-arm-ethos-u.html
        type: documentation
    - resource:
        title: CMSIS-Toolbox MLOps integration
        link: https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/#mlops-information
        type: documentation
    - resource:
        title: CMSIS-NN documentation
        link: https://arm-software.github.io/CMSIS-NN/latest/
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---
