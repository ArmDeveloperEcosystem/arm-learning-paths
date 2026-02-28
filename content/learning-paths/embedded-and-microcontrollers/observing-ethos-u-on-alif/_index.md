---
title: Observing Ethos-U85 NPU on Alif E8 with MNIST Inference

minutes_to_complete: 90

who_is_this_for: This is an introductory topic for embedded developers and ML engineers who want to run TinyML inference on physical hardware with Arm Ethos-U85 NPU acceleration.

learning_objectives:
    - Set up the Alif Ensemble E8 development kit for ML applications
    - Install and configure CMSIS Toolbox and build tools
    - Build and flash firmware using JLink
    - Run MNIST digit classification on Ethos-U85 NPU
    - Monitor inference results via UART and LED indicators

prerequisites:
    - Alif [Ensemble E8 Series Development Kit](https://alifsemi.com/ensemble-e8-series/) (contact [Alif Sales](https://alifsemi.com/support/sales-support/))
    - USB Type-C cable for programming
    - USB-TTL converter (1.8V logic level) for UART debug (optional)
    - Basic knowledge of embedded systems and C programming
    - Computer running Windows, Linux, or macOS

author_primary: Waheed Brown

author:
    - Waheed Brown
    - Fidel Makatia Omusilibwa

### Tags
skilllevels: Introductory
subjects: ML
armips:
    - Cortex-A
    - Cortex-M
    - Ethos-U

operatingsystems:
    - Linux
    - macOS
    - Windows

tools_software_languages:
    - C
    - CMSIS
    - TensorFlow Lite
    - SEGGER JLink
    - SEGGER RTT
    - GCC
    - Arm Compiler

further_reading:
    - resource:
        title: Introduction to TinyML on Arm using PyTorch and ExecuTorch
        link: /learning-paths/embedded-and-microcontrollers/introduction-to-tinyml-on-arm/
        type: documentation
    - resource:
        title: Visualize Ethos-U NPU performance with ExecuTorch on Arm FVPs
        link: /learning-paths/embedded-and-microcontrollers/visualizing-ethos-u-performance/
        type: documentation
    - resource:
        title: Alif Semiconductor Ensemble E8 Series
        link: https://alifsemi.com/ensemble-e8-series/
        type: website
    - resource:
        title: Arm Ethos-U85 NPU
        link: https://www.arm.com/products/silicon-ip-cpu/ethos/ethos-u85
        type: website
        type: documentation
    - resource:
        title: Arm Developers Guide for Cortex-M Processors and Ethos-U NPU
        link: https://developer.arm.com/documentation/109267/0101
        type: documentation




### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---