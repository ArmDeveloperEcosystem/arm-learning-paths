---
title: Deploy MobileSAM on Alif Ensemble E8 with ExecuTorch
description: Export MobileSAM, deploy camera and NPU inference on the Alif E8, and validate live progress through UART and retained integer-model references.
minutes_to_complete: 120
draft: true
cascade:
  draft: true
who_is_this_for: This Learning Path is for embedded ML developers who want to deploy live MobileSAM segmentation on an Alif Ensemble E8 using ExecuTorch and Zephyr.
learning_objectives:
  - Trace the fixed-prompt and quantized tensor contracts from model export to live camera inference
  - Export a MobileSAM model for the E8 HP core and Ethos-U85-256
  - Build a Zephyr application within its scratch and application RAM budgets
  - Program and verify the model and firmware, then validate camera capture and NPU inference through UART
  - Distinguish integer execution agreement from image accuracy and the optional dashboard's known DSI errors
prerequisites:
  - An [Alif Ensemble E8 Development Kit](https://alifsemi.com/support/kits/ensemble-e8devkit/), revision A0 (`AE822FA0E5597LS0`), with its MT9M114 selfie camera; the default application does not use the display
  - Internet access to download the supplied public calibration image; optionally, an RGB image representative of your own camera scenes
  - Experience with PyTorch model export, C++, and Zephyr builds
  - An Apple silicon Mac with Python 3.12, Git, CMake, Ninja, and a C++ build toolchain
  - Zephyr SDK 0.17.0, west, Alif Security Toolkit, SEGGER J-Link, and Expect
  - Access to the HP UART4 console through PRG USB and the board's SW4 selector
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
  - MobileSAM
  - Zephyr
  - Python
  - CMake
operatingsystems:
  - macOS
  - RTOS
further_reading:
  - resource:
      title: Run MobileSAM prompt segmentation on Arm Ethos-U85 with ExecuTorch
      link: /learning-paths/embedded-and-microcontrollers/deploy-mobilesam-on-ethos-u/
      type: documentation
  - resource:
      title: Set up the Alif Ensemble E8 board
      link: /learning-paths/embedded-and-microcontrollers/alif-image-classification/board-setup/
      type: documentation
  - resource:
      title: Alif Ensemble E8 DevKit support page
      link: https://alifsemi.com/support/kits/ensemble-e8devkit/
      type: website
  - resource:
      title: ExecuTorch Arm Ethos-U backend documentation
      link: https://docs.pytorch.org/executorch/stable/embedded-arm-ethos-u.html
      type: documentation
  - resource:
      title: MobileSAM source repository
      link: https://github.com/ChaoningZhang/MobileSAM
      type: repository

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1
layout: learningpathall
learning_path_main_page: "yes"
---
