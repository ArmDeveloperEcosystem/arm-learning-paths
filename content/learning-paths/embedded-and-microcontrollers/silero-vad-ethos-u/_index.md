---
title: Deploy Silero VAD on Arm Ethos-U with ExecuTorch
description: Export a stateful Silero voice activity detection model with ExecuTorch, run it on an Arm Ethos-U85 Fixed Virtual Platform, and validate its output.

draft: true
cascade:
    draft: true

minutes_to_complete: 90

who_is_this_for: This is an introductory topic for embedded machine learning developers who want to evaluate streaming audio inference with ExecuTorch on Arm Ethos-U.

learning_objectives:
    - Set up ExecuTorch and the Arm development tools for Corstone-320 and Ethos-U85
    - Export and quantize a stateful Silero VAD model as a `.pte` file
    - Build and run a bare-metal voice activity detection application on a Corstone-320 Fixed Virtual Platform
    - Validate simulated speech probabilities against a host-generated reference

prerequisites:
    - A Linux host using x86_64 or arm64, or an Apple Silicon macOS host
    - Python 3.10 through 3.13, Git, CMake 3.24 or later, and a C++17 compiler
    - An internet connection for downloading ExecuTorch dependencies, the Silero VAD model, Arm tools, and the Fixed Virtual Platform
    - Basic familiarity with PyTorch models and command-line development tools

author: Usamah Zaheer

generate_summary_faq: true
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: ML
armips:
    - Cortex-M
    - Ethos-U
tools_software_languages:
    - ExecuTorch
    - PyTorch
    - Python
    - CMake
    - Arm GNU Toolchain
    - Arm Fixed Virtual Platform
    - Vela
operatingsystems:
    - Linux
    - macOS
    - Baremetal

further_reading:
    - resource:
        title: ExecuTorch Arm Ethos-U backend
        link: https://docs.pytorch.org/executorch/stable/backends/arm-ethos-u/arm-ethos-u-overview.html
        type: documentation
    - resource:
        title: ExecuTorch Arm Ethos-U quantization
        link: https://docs.pytorch.org/executorch/stable/backends/arm-ethos-u/arm-ethos-u-quantization.html
        type: documentation
    - resource:
        title: Silero VAD Ethos-U example source
        link: https://github.com/usamahz/executorch/tree/4af907b2192d89369440a1dc0488c1792781a82d/examples/arm/silero_vad_example_ethos_u
        type: website
    - resource:
        title: Silero VAD project
        link: https://github.com/snakers4/silero-vad
        type: website
    - resource:
        title: Ethos-U85 operator support in ExecuTorch
        link: https://docs.pytorch.org/executorch/stable/backends/arm-ethos-u/U85_op_support.html
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---
