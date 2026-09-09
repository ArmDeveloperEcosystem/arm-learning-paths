---
title: Explore KleidiCV Gaussian blur with SVE2 and SME on Android
description: Explore KleidiCV Gaussian blur on Android by building and comparing NEON, SVE2, and SME streaming-SVE implementations.

minutes_to_complete: 45

who_is_this_for: This is an advanced topic for C and C++ developers who want to evaluate SIMD image-processing implementations on an Arm-based Android device.

learning_objectives:
    - Build KleidiCV Gaussian blur examples with the Android NDK.
    - Run a minimal SME Gaussian blur example on an Android device.
    - Explore the performance of NEON, SVE2, and SME implementations with controlled CPU affinity.
    - Interpret how kernel size and image resolution affect SME speedup.

prerequisites:
    - A Linux development machine with Git, CMake, Python 3, and ADB installed.
    - Android SDK Platform-Tools and Android NDK r29 or later.
    - A 64-bit Arm Android device with SVE2 and SME support.
    - Basic familiarity with C++, CMake, and Android Debug Bridge (ADB).

author: Jett Zhou

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
armips:
    - Cortex-A
    - Cortex-X
operatingsystems:
    - Android
tools_software_languages:
    - ADB
    - C
    - C++
    - CMake
    - Android NDK
    - SVE2
    - SME

further_reading:
    - resource:
        title: KleidiCV
        link: https://gitlab.arm.com/kleidi/kleidicv
        type: documentation
    - resource:
        title: Arm Scalable Vector Extension
        link: https://developer.arm.com/documentation/101726/latest
        type: documentation
    - resource:
        title: Arm Scalable Matrix Extension
        link: https://developer.arm.com/documentation/109383/latest
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---
