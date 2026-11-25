---
title: Run optimized Arm AI Portal image upscaling models on Android

description: Build Photo Upscale, import QuickSRNetSmall, SESR-M5, or RealESR-general-x4v3 through ExecuTorch, and upscale saved photos locally on the CPU of an Arm-based Android device.
minutes_to_complete: 40
who_is_this_for: Android and machine learning developers who want to upscale saved photos locally on an Arm-based Android device using optimized models from the Arm AI Portal.
learning_objectives:
    - Prepare the Android command-line tools and connect an Arm-based Android phone.
    - Download and run supported upscaling models from the Arm AI Portal.
    - Explain how the supplied adapter prepares image tiles, runs ExecuTorch, and combines the upscaled output.
prerequisites:
    - A macOS, Linux, or Windows development machine
    - An Arm-based Android phone with Android 9 or later, the `arm64-v8a` ABI, and enough storage for the application and model files
    - Basic familiarity with terminal commands and Android applications
    - Git installed on the development machine
    - Python 3.10 or later with the `venv` and `pip` modules on the machine
    - Java Development Kit (JDK) 17 on the machine, available on your `PATH`
    - A tool for downloading files and a tool for extracting ZIP archives on the machine
    - A data-capable USB cable
    - Network access for the first Gradle build and model downloads
author: Matt Cossins
generate_summary_faq: true
rerun_summary: false
rerun_faqs: false
skilllevels: Introductory
subjects: AI/ML
armips:
    - Cortex-A
tools_software_languages:
    - Android Studio
    - Java
    - ExecuTorch
    - XNNPACK
    - Arm AI Portal
    - Hugging Face
operatingsystems:
    - Android
further_reading:
    - resource:
        title: Arm AI Portal model catalog
        link: https://developer.arm.com/ai/models
        type: documentation
    - resource:
        title: Run apps on a hardware device
        link: https://developer.android.com/studio/run/device
        type: documentation
    - resource:
        title: Run ExecuTorch on Android
        link: https://docs.pytorch.org/executorch/stable/using-executorch-android.html
        type: documentation
    - resource:
        title: XNNPACK backend for ExecuTorch
        link: https://docs.pytorch.org/executorch/stable/backends-xnnpack.html
        type: documentation
### FIXED, DO NOT MODIFY
weight: 1
layout: learningpathall
learning_path_main_page: "yes"
---
