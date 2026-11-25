---
title: Deploy Silero VAD on Alif Ensemble E8 with ExecuTorch
description: Run Silero VAD on the Alif E8 on-board microphone, show live speech probabilities on its display, and verify a deterministic clip against a host reference.
minutes_to_complete: 150
draft: true
cascade:
  draft: true
who_is_this_for: This Learning Path is for embedded ML developers porting streaming audio inference to the Cortex-M55 HP core and Ethos-U85-256 on an Alif Ensemble E8.
learning_objectives:
  - Explain the waveform context and recurrent state retained between Silero VAD invocations
  - Export a quantized Ethos-U85 program and matching speech-probability reference using released Python packages
  - Build a deterministic validation configuration and a live microphone configuration from one E8 application
  - Program the E8, verify its MRAM payloads, and compare all 79 validation probabilities with the host reference
  - Capture the on-board microphone and interpret live probability, audio level, and capture-rate diagnostics
prerequisites:
  - An [Alif Ensemble E8 Development Kit](https://alifsemi.com/support/kits/ensemble-e8devkit/) with the tested A0 part AE822FA0E5597LS0, provisioned debug access, its 480 × 800 display attached, and a data-capable USB cable
  - An Apple silicon Mac with Python 3.12, Git, CMake, Ninja, ripgrep, and a C++ build toolchain
  - Access to the E8 application UART4 console through PRG USB and the board’s SW4 selector; no separate USB-to-UART adapter is required
  - Zephyr SDK 0.17.0, Alif Security Toolkit configured for E8 A0, and SEGGER J-Link
  - Experience with PyTorch model export, C++, and Zephyr builds
author: Usamah Zaheer
generate_summary_faq: false
rerun_summary: false
rerun_faqs: false
skilllevels: Advanced
subjects: AI/ML
armips:
  - Ethos-U
tools_software_languages:
  - ExecuTorch
  - PyTorch
  - Zephyr
  - Python
  - CMake
operatingsystems:
  - macOS
  - RTOS
further_reading:
  - resource:
      title: Deploy Silero VAD on Arm Ethos-U with ExecuTorch
      link: /learning-paths/embedded-and-microcontrollers/silero-vad-ethos-u/
      type: documentation
  - resource:
      title: Set up the Alif Ensemble E8 board
      link: /learning-paths/embedded-and-microcontrollers/alif-image-classification/board-setup/
      type: documentation
  - resource:
      title: Alif Ensemble E8 DevKit support
      link: https://alifsemi.com/support/kits/ensemble-e8devkit/
      type: website
  - resource:
      title: ExecuTorch Silero VAD export and runtime source
      link: https://github.com/pytorch/executorch/tree/12dac4aa042b66a7229e8d7d3af2bdde8c9f262f/examples/arm/silero_vad_example_ethos_u
      type: repository
  - resource:
      title: Silero VAD project
      link: https://github.com/snakers4/silero-vad
      type: repository

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1
layout: learningpathall
learning_path_main_page: "yes"
---
