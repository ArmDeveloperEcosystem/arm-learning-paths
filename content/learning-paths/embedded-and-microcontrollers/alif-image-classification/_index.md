---
title: Run image classification on an Alif Ensemble E8 DevKit using ExecuTorch and Ethos-U85

description: Deploy a MobileNetV2 image classification model to an Alif Ensemble E8 DevKit and run inference on the Ethos-U85 NPU.

minutes_to_complete: 120

who_is_this_for: This is an advanced topic for embedded developers who want to deploy a neural network model to an Arm Cortex-M55 microcontroller using ExecuTorch and an Ethos-U85 NPU.

learning_objectives:
    - Compile a MobileNetV2 model for the Ethos-U85 NPU using ExecuTorch's ahead-of-time (AOT) compiler on an Arm-based cloud instance
    - Build ExecuTorch static libraries for bare-metal Cortex-M55 targets
    - Configure CMSIS project files, memory layout, and linker scripts for an ML workload on the Alif Ensemble E8
    - Run real-time image classification inference on the Ethos-U85 NPU and verify results using SEGGER Real-Time Transfer (RTT)

prerequisites:
    - Experience with C/C++ and embedded development concepts
    - An [Alif Ensemble E8 DevKit](https://alifsemi.com/support/kits/ensemble-e8devkit/) with a USB-C cable
    - A SEGGER J-Link debug probe (included in the DevKit)
    - A development machine running macOS on Apple Silicon with Visual Studio Code installed
    - An AWS account or access to an Arm-based cloud instance for native Arm compilation

generate_summary_faq: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-05-06T17:17:54Z'
  generator: template
  source_hash: 8585bb59efa67b3a92314e4382339fc5c0a14bb458931c0d98f2748379003857
  summary: >-
    Deploy a MobileNetV2 image classification model to an Alif Ensemble E8 DevKit and run inference
    on the Ethos-U85 NPU. It is designed for embedded developers who want to deploy a neural network
    model to an Arm Cortex-M55 microcontroller using ExecuTorch and an Ethos-U85 NPU. By the end,
    you will be able to compile a MobileNetV2 model for the Ethos-U85 NPU using ExecuTorch's ahead-of-time
    (AOT) compiler on an Arm-based cloud instance, build ExecuTorch static libraries for bare-metal
    Cortex-M55 targets, and configure CMSIS project files, memory layout, and linker scripts for
    an ML workload on the Alif Ensemble E8. It focuses on tools and technologies such as ExecuTorch,
    PyTorch, GCC, CMSIS-Toolbox, and Python, Baremetal environments, and Arm platforms including
    Cortex-M and Ethos-U. The main steps cover Set up the Alif Ensemble E8 DevKit, Compile the
    model on an Arm cloud instance, Create the image classification firmware project, Add the
    application code, and Configure memory layout and flash settings.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will compile a MobileNetV2 model for the Ethos-U85 NPU using ExecuTorch's ahead-of-time
      (AOT) compiler on an Arm-based cloud instance, build ExecuTorch static libraries for bare-metal
      Cortex-M55 targets, and configure CMSIS project files, memory layout, and linker scripts
      for an ML workload on the Alif Ensemble E8. Deploy a MobileNetV2 image classification model
      to an Alif Ensemble E8 DevKit and run inference on the Ethos-U85 NPU.
  - question: Who is this Learning Path for?
    answer: >-
      This is an advanced topic for embedded developers who want to deploy a neural network model
      to an Arm Cortex-M55 microcontroller using ExecuTorch and an Ethos-U85 NPU.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: Experience with C/C++ and embedded development
      concepts; An [Alif Ensemble E8 DevKit](https://alifsemi.com/support/kits/ensemble-e8devkit/)
      with a USB-C cable; A SEGGER J-Link debug probe (included in the DevKit); A development
      machine running macOS on Apple Silicon with Visual Studio Code installed; An AWS account
      or access to an Arm-based cloud instance for native Arm compilation.
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including ExecuTorch, PyTorch, GCC, CMSIS-Toolbox, and Python,
      Baremetal environments, and Arm platforms such as Cortex-M and Ethos-U.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Set up the Alif Ensemble E8 DevKit, Compile the model
      on an Arm cloud instance, Create the image classification firmware project, Add the application
      code, and Configure memory layout and flash settings.
# END generated_summary_faq

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

