---
title: Integrate a KleidiAI SME2 kernel into XNNPACK

minutes_to_complete: 45

draft: true
cascade:
    draft: true

who_is_this_for: This is an advanced topic for software developers and performance engineers who want to integrate a KleidiAI SME2 microkernel into an existing AI inference framework.

learning_objectives:
    - Understand the XNNPACK `qd8_f16_qc4w` fully connected operator and its quantized matrix formats
    - Select a KleidiAI microkernel by matching quantization contracts, not only data types
    - Pack XNNPACK qd8 activations and QC4W weights into the layouts required by a KleidiAI SME2 kernel
    - Add runtime SME2 dispatch with a safe fallback path
    - Build and validate the integration on an Android Arm device

prerequisites:
    - Familiarity with C or C++ and basic matrix multiplication
    - Android Debug Bridge (`adb`) and an Android Arm device with SME2 support for the validation steps
    - Android NDK r29, or a compatible Android NDK

author: Arm

generate_summary_faq: true
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
subjects: ML
armips:
    - Armv9-A
tools_software_languages:
    - C++
    - Android NDK
    - KleidiAI
    - SME2
    - XNNPACK
operatingsystems:
    - Android
    - Linux

further_reading:
    - resource:
        title: KleidiAI repository
        link: https://github.com/ARM-software/kleidiai
        type: website
    - resource:
        title: XNNPACK repository
        link: https://github.com/google/XNNPACK
        type: website
    - resource:
        title: Arm SME2 introduction, part 4
        link: https://developer.arm.com/community/arm-community-blogs/b/architectures-and-processors-blog/posts/part4-arm-sme2-introduction
        type: blog
    - resource:
        title: Understand KleidiAI SME2 matmul microkernels
        link: /learning-paths/mobile-graphics-and-gaming/kai_sme2_matmul_ukernel_explained/
        type: learning-path

### FIXED, DO NOT MODIFY
# ==============================================================================
weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---
