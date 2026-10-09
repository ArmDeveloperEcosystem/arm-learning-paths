---
title: Run Conformer speech recognition on an Alif Ensemble E8 AI/ML AppKit using ExecuTorch and Ethos-U85

description: Build and deploy the Alif MLEK Conformer ASR application with ExecuTorch on the Alif Ensemble E8 AppKit and Ethos-U85 NPU.

minutes_to_complete: 120

who_is_this_for: This is an advanced topic for embedded ML developers who want to learn how to build a Conformer-based speech recognition application and run it on a physical Alif Ensemble E8 AppKit using ExecuTorch and the Ethos-U85 NPU.

learning_objectives:
    - Understand what a Conformer model is, and why it is used for Automatic Speech Recognition (ASR) applications
    - Use the ML Embedded Evaluation Kit (MLEK) to prepare the Conformer model for ExecuTorch deployment
    - Build and run the ASR application on the Corstone-320 FVP, and understand how it works
    - Understand how the ASR application is adapted from an FVP flow, to running on a physical Alif E8 AppKit
    - Build, flash, and verify the ASR application on the E8 AppKit
    - Verify the transcription on the connected display

prerequisites:
    - Experience with C/C++, CMake, and embedded baremetal development concepts
    - Familiarity with PyTorch, ExecuTorch, and quantized model deployment
    - A Linux development machine, or an Apple Silicon Mac running macOS 15 or later (Docker Desktop is also required for the macOS FVP flow)
    - An Alif Ensemble E8 AI/ML AppKit (AK-E8-AIML) and a USB-C data cable.

author: 
    - Matt Cossins
    - Kwashie Andoh  

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
    - CMake
    - Python
    - Conformer
operatingsystems:
    - Baremetal
    - Linux
    - macOS

further_reading:
    - resource:
        title: "End-to-End INT8 Conformer on Arm: Training, Quantization, and Deployment on Ethos-U85"
        link: https://developer.arm.com/community/arm-community-blogs/b/internet-of-things-blog/posts/end-to-end-int8-conformer-on-arm-training-quantization-and-deployment-on-ethos-u85
        type: blog
    - resource:
        title: Alif ML Embedded Evaluation Kit
        link: https://github.com/alifsemi/alif_ml-embedded-evaluation-kit/tree/main
        type: repository
    - resource:
        title: Arm ML Embedded Evaluation Kit
        link: https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit
        type: repository
    - resource:
        title: Alif Ensemble E8 AppKit Support Page
        link: https://alifsemi.com/support/kits/ensemble-e8appkit/
        type: website
    - resource:
        title: ExecuTorch Arm Ethos-U NPU Backend Tutorial
        link: https://docs.pytorch.org/executorch/stable/tutorial-arm-ethos-u.html
        type: documentation
### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
