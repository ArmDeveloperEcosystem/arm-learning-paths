---
title: Run image classification on an Alif Ensemble E8 DevKit using ExecuTorch and Ethos-U85

description: Deploy a MobileNetV2 image classification model to an Alif Ensemble E8 DevKit and run inference on the Ethos-U85 NPU.

draft: true
cascade:
    draft: true

minutes_to_complete: 120

who_is_this_for: This is an advanced topic for embedded developers who want to deploy a neural network model to an Arm Cortex-M55 microcontroller using ExecuTorch and an Ethos-U85 NPU.

learning_objectives:
    - Compile a MobileNetV2 model for the Ethos-U85 NPU using ExecuTorch's ahead-of-time (AOT) compiler on an Arm-based cloud instance.
    - Build ExecuTorch static libraries for bare-metal Cortex-M55 targets.
    - Configure CMSIS project files, memory layout, and linker scripts for an ML workload on the Alif Ensemble E8.
    - Run real-time image classification inference on the Ethos-U85 NPU and verify results using SEGGER Real-Time Transfer (RTT).

prerequisites:
    - Experience with C/C++ and embedded development concepts.
    - An [Alif Ensemble E8 DevKit](https://alifsemi.com/support/kits/ensemble-e8devkit/) with a USB-C cable.
    - A SEGGER J-Link debug probe (included in the DevKit).
    - A development machine running macOS on Apple Silicon with Visual Studio Code installed.
    - An AWS account or access to an Arm-based cloud instance for native Arm compilation.

author: Gabriel Peterson

skilllevels: Advanced
subjects: ML
armips:
    - Cortex-M
    - Ethos-U
tools_software_languages:
    - ExecuTorch
    - PyTorch
    - GCC
    - CMSIS-Toolbox
    - Python
operatingsystems:
    - Baremetal

further_reading:
    - resource:
        title: ExecuTorch Arm Ethos-U NPU Backend Tutorial
        link: https://docs.pytorch.org/executorch/1.0/tutorial-arm-ethos-u.html
        type: documentation
    - resource:
        title: Alif Ensemble E8 DevKit Support Page
        link: https://alifsemi.com/support/kits/ensemble-e8devkit/
        type: website
    - resource:
        title: Arm Ethos-U85 NPU Technical Overview
        link: https://developer.arm.com/Processors/Ethos-U85
        type: documentation
    - resource:
        title: CMSIS-Toolbox Documentation
        link: https://arm-software.github.io/CMSIS_6/latest/Toolbox/index.html
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
