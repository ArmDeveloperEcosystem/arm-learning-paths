---
title: Compare KleidiCV Gaussian blur performance across Neon, SVE2, and SME on Android
description: Build a KleidiCV Gaussian blur benchmark for Android and evaluate how Neon, SVE2, and SME performance changes with image resolution and kernel size.

minutes_to_complete: 45

who_is_this_for: This is an advanced topic for C and C++ developers who want to evaluate SIMD image-processing implementations on an Arm-based Android device.

learning_objectives:
    - Build KleidiCV Gaussian blur examples with the Android NDK.
    - Run a minimal SME Gaussian blur example on an Android device.
    - Explore the performance of Neon, SVE2, and SME implementations with controlled CPU affinity.
    - Interpret how kernel size and image resolution affect SME speedup.

prerequisites:
    - A Ubuntu or Debian x86_64 Linux development machine with Git, CMake, Python 3, and Android Debug Bridge (`adb`) installed
    - Android SDK Platform-Tools and Android NDK r29 or later
    - A 64-bit Arm Android device with SVE2 and SME support
    - Basic familiarity with C++, CMake, and `adb`

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
    - CPP
    - CMake
    - Android NDK
    - Neon
    - SVE2
    - SME

further_reading:
    - resource:
        title: Android NDK guides
        link: https://developer.android.com/ndk/guides
        type: documentation
    - resource:
        title: KleidiCV
        link: https://gitlab.arm.com/kleidi/kleidicv
        type: documentation
    - resource:
        title: Arm Scalable Vector Extension
        link: https://support.arm.com/documentation/102340/latest/
        type: documentation
    - resource:
        title: Arm Scalable Matrix Extension
        link: https://support.arm.com/documentation/110636/latest/
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---
