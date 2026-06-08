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

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T21:57:47Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 8585bb59efa67b3a92314e4382339fc5c0a14bb458931c0d98f2748379003857
  summary_generated_at: '2026-06-01T21:24:49Z'
  summary_source_hash: 8585bb59efa67b3a92314e4382339fc5c0a14bb458931c0d98f2748379003857
  faq_generated_at: '2026-06-02T21:57:47Z'
  faq_source_hash: 8585bb59efa67b3a92314e4382339fc5c0a14bb458931c0d98f2748379003857
  summary: >-
    This advanced Learning Path guides you through deploying a MobileNetV2 image classification
    model to the Alif Ensemble E8 DevKit and running inference on the Ethos‑U85 NPU from the Cortex‑M55
    High‑Performance core. You will compile the model with ExecuTorch’s ahead‑of‑time compiler
    on an Arm‑based cloud instance, build ExecuTorch static libraries for a bare‑metal target,
    create a CMSIS project in VS Code by cloning a Blinky template, integrate SEGGER RTT, and
    adjust memory and linker settings. By the end, you will flash the firmware, run real‑time
    inference on a test image, and verify results over RTT. Prerequisites include C/C++ experience,
    the E8 DevKit with J‑Link, macOS on Apple Silicon with VS Code, and Arm‑based cloud access;
    estimated time is 120 minutes.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need C/C++ and embedded development experience, an Alif Ensemble E8 DevKit with a USB-C
      cable, and a SEGGER J-Link (included with the DevKit). You also need a macOS machine on
      Apple Silicon with Visual Studio Code, plus an AWS account or access to an Arm-based cloud
      instance.
  - question: Why should I build on an Arm-based cloud instance instead of my local host?
    answer: >-
      ExecuTorch’s Arm backend build scripts are designed for native Arm compilation, and components
      like the Vela compiler and CMSIS-NN target Arm. Using a Graviton-based EC2 instance avoids
      the complexity of cross-compilation and lets you compile the model and build the ExecuTorch
      static libraries natively.
  - question: When creating the firmware project, which components must be included?
    answer: >-
      Duplicate the Blinky example to a new CMSIS project (mv2_runner) and include the ExecuTorch
      libraries, the compiled MobileNetV2 model, and SEGGER RTT for debug output. Update the project
      references so they point to mv2_runner rather than the original Blinky.
  - question: How should I configure memory and linker settings for this workload?
    answer: >-
      Reconfigure MRAM allocation, stack/heap sizes, and the linker script to match the ML workload.
      The embedded model is about 3.7 MB (MRAM/flash), the runtime and application code add roughly
      800 KB, and inference needs approximately 7.6 MB of SRAM for memory pools and intermediate
      tensors.
  - question: What result should I expect after flashing, and how do I verify it?
    answer: >-
      The application initializes the Ethos-U85, loads the MobileNetV2 model via ExecuTorch, runs
      inference on an embedded test image, and prints the classification result. Use SEGGER RTT
      to view and verify the output in real time.
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

