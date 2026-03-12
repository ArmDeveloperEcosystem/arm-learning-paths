---
title: Run image classification on an Alif Ensemble E8 DevKit with ExecuTorch and Ethos-U85

minutes_to_complete: 120

who_is_this_for: This Learning Path is for embedded developers who want to deploy a neural network on an Arm Cortex-M55 microcontroller with an Ethos-U85 NPU. You will compile a MobileNetV2 model using ExecuTorch, embed it into bare-metal firmware, and run image classification on the Alif Ensemble E8 DevKit.

learning_objectives:
    - Compile a MobileNetV2 model for the Ethos-U85 NPU using ExecuTorch's ahead-of-time (AOT) compiler on an Arm-based cloud instance.
    - Build ExecuTorch static libraries for bare-metal Cortex-M55 targets.
    - Configure CMSIS project files, memory layout, and linker scripts for a large ML workload on the Alif Ensemble E8.
    - Run real-time image classification inference on the Ethos-U85 NPU and verify results through SEGGER RTT.

prerequisites:
    - An Alif Ensemble E8 DevKit with a USB-C cable.
    - A SEGGER J-Link debug probe (the DevKit has one built in).
    - A development machine running macOS (Apple Silicon) or Linux.
    - (Optional) An AWS account or access to an Arm-based cloud instance (Graviton c7g.4xlarge recommended). You can also build ExecuTorch locally on an Arm-based machine, though the steps will differ.
    - Basic familiarity with C/C++ and embedded development concepts.
    - VS Code installed on your development machine.

author: Gabriel Peterson

### Tags
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
