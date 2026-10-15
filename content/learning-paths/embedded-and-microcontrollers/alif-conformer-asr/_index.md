---
title: Run offline Conformer speech recognition on Alif Ensemble E8 with ExecuTorch

draft: true
cascade:
    draft: true
    
description: Deploy Conformer ASR on an Alif Ensemble E8, capture live speech, and verify offline transcription and Ethos-U85 execution with ExecuTorch.

minutes_to_complete: 120

who_is_this_for: This Learning Path is for embedded ML developers who want to capture and transcribe live speech on an Alif Ensemble E8 using ExecuTorch and the Ethos-U85 NPU.

learning_objectives:
    - Prepare a quantized Conformer model with Alif MLEK for ExecuTorch deployment
    - Build and flash the E8 application and its external-flash model
    - Capture live speech and assess the transcription on the connected display
    - Confirm Ethos-U85 inference with UART performance counters and verify standalone restart

prerequisites:
    - Experience with C/C++, CMake, and embedded baremetal development concepts
    - Familiarity with PyTorch, ExecuTorch, and quantized model deployment
    - A Linux development machine, or an Apple Silicon Mac running macOS 15 or later
    - An Alif Ensemble E8 AI/ML AppKit (AK-E8-AIML), or an E8 DevKit with a compatible attached display, and a USB-C data cable

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
        title: Deploy Silero VAD on Arm Ethos-U with ExecuTorch
        link: /learning-paths/embedded-and-microcontrollers/silero-vad-ethos-u/
        type: learning-path
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
