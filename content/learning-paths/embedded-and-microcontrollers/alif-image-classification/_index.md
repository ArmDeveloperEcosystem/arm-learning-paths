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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-08T15:19:18Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 8585bb59efa67b3a92314e4382339fc5c0a14bb458931c0d98f2748379003857
  summary_generated_at: '2026-07-08T15:19:18Z'
  summary_source_hash: 8585bb59efa67b3a92314e4382339fc5c0a14bb458931c0d98f2748379003857
  faq_generated_at: '2026-07-08T15:19:18Z'
  faq_source_hash: 8585bb59efa67b3a92314e4382339fc5c0a14bb458931c0d98f2748379003857
  summary: >-
    You'll deploy a MobileNetV2 image classifier on the Alif Ensemble
    E8 DevKit by compiling the model and runtime for the Ethos-U85 NPU, building a CMSIS project,
    and running inference with SEGGER RTT output. First, you'll validate the board, debug probe, and flashing
    workflow, then use an Arm-based cloud instance to produce ExecuTorch static libraries and
    an Ethos-U85–targeted model. Next, you'll create an `mv2_runner` firmware project from the Blinky
    template, add the provided application code that initializes the NPU and executes inference
    on a test image, and integrate RTT for result reporting. Finally, you'll make memory layout
    and linker updates so the model, runtime, and SRAM working set fit, enabling real-time classification
    on the device.
  faqs:
  - question: Which core should I target when flashing and debugging the firmware?
    answer: >-
      Use the Cortex-M55 High-Performance (HP) core to orchestrate inference on the Ethos-U85.
      The steps assume this core for building, flashing, and running the application.
  - question: What artifacts should I expect after compiling on the Arm cloud instance?
    answer: >-
      You should have ExecuTorch static libraries and a compiled MobileNetV2 model targeted for
      the Ethos-U85. These outputs are linked into the `mv2_runner` firmware project.
  - question: After duplicating the Blinky example, which project files need to be updated?
    answer: >-
      Rename blinky.cproject.yml to `mv2_runner.cproject.yml` and replace internal references from
      `blinky` to `mv2_runner`. This establishes a new CMSIS project for the application.
  - question: Where do I place the provided main.cpp and how do I verify it works?
    answer: >-
      Place `main.cpp` in the `mv2_runner` project directory as instructed. When you flash and run
      the firmware, check the SEGGER RTT console for the printed classification result.
  - question: What memory changes are required for the model and runtime to fit?
    answer: >-
      Increase MRAM allocation for the embedded model (about 3.7 MB) and code (around 800 KB),
      and provision approximately 7.6 MB of SRAM for inference buffers. Update stack/heap sizes
      and the linker script in the CMSIS project accordingly.
# END generated_summary_faq

author: Gabriel Peterson

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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

