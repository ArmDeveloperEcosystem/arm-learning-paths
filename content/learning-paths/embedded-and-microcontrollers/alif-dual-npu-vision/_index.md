---
title: Run parallel vision inference on an Alif Ensemble E8 with Zephyr

draft: true
cascade:
    draft: true
    
description: Build a power-conscious live camera demo that drives Ethos-U55 and Ethos-U85 from one Cortex-M55 MCU.

minutes_to_complete: 90

who_is_this_for: This is an advanced topic for embedded ML developers who want to run two ExecuTorch models concurrently on separate Ethos-U NPUs under Zephyr.

learning_objectives:
    - Explain how one MCU can coordinate two NPUs while avoiding the power and system cost of a second MCU or application processor
    - Configure an Alif Ensemble E8 DevKit for native Zephyr camera, ISP, display, and dual-NPU operation
    - Build, package, and flash an ExecuTorch application that targets Ethos-U55 and Ethos-U85
    - Validate live camera capture, model results, and parallel inference timing

prerequisites:
    - Experience with C/C++, embedded systems, and Zephyr build concepts
    - A development machine running macOS on Apple Silicon with Homebrew and the Xcode Command Line Tools installed
    - An [Alif Ensemble E8 DevKit](https://alifsemi.com/support/kits/ensemble-e8devkit/) with an MT9M114 camera connected to J16 and an MW405 display
    - Alif SEROM 1.105.65 and SERAM 1.110.0 installed on the board
    - Alif SEToolkit 1.10 installed on the development machine

author: Varun Chari

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

skilllevels: Advanced
subjects: ML
armips:
    - Cortex-M55
    - Ethos-U55
    - Ethos-U85
tools_software_languages:
    - ExecuTorch
    - Zephyr
    - Python
    - GCC
operatingsystems:
    - macOS
    - RTOS

further_reading:
    - resource:
        title: Alif Ensemble E8 DevKit support page
        link: https://alifsemi.com/support/kits/ensemble-e8devkit/
        type: website
    - resource:
        title: Alif SDK pull request 879
        link: https://github.com/alifsemi/sdk-alif/pull/879
        type: website
    - resource:
        title: Ethos-U core driver multi-variant merge
        link: https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-core-driver/-/commit/b7cd193afde80afe8bbae9a26d2ca6586554f054
        type: website
    - resource:
        title: ExecuTorch Arm Ethos-U NPU backend tutorial
        link: https://docs.pytorch.org/executorch/stable/tutorial-arm-ethos-u.html
        type: documentation
    - resource:
        title: Run image classification on an Alif Ensemble E8 DevKit using ExecuTorch and Ethos-U85
        link: /learning-paths/embedded-and-microcontrollers/alif-image-classification/
        type: documentation
    - resource:
        title: Dual-NPU live vision sample source
        link: https://github.com/varunchariArm/sdk-alif/tree/dual-npu-main-integration/samples/modules/executorch/dual_npu_vision
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---
