---
title: Benchmark INT8 vs FP32 NEON inference on Arm Cortex-A9

minutes_to_complete: 45

who_is_this_for: This is an intermediate topic for software developers deploying neural networks on legacy Arm devices (ARMv7-A, Cortex-A9 class) who want to understand the real performance difference between INT8 and FP32 using explicit NEON intrinsics.

learning_objectives:
    - Understand why Cortex-A9 behaves differently from modern Arm cores for INT8 inference
    - Cross-compile a C benchmark binary for armeabi-v7a using Android NDK
    - Write explicit NEON intrinsic kernels for FP32 and INT8 matrix multiplication
    - Measure and compare inference performance on real Cortex-A9 hardware
    - Understand the INT8 widening chain (INT8 to INT16 to INT32) and its performance impact

prerequisites:
    - A Windows or Linux machine with Android NDK installed
    - Basic knowledge of C programming
    - An Android device with Arm Cortex-A9 (ARMv7-A) for testing
    - ADB installed and device connected with USB debugging enabled

author: Poojith Devan

### Tags
skilllevels: Intermediate
subjects: ML
armips:
    - Cortex-A9
operatingsystems:
    - Android
tools_software_languages:
    - C
    - Android NDK
    - TFLite
    - GCC

further_reading:
    - resource:
        title: Arm NEON Programmer's Guide
        link: https://developer.arm.com/documentation/den0018/latest
        type: documentation
    - resource:
        title: Arm Intrinsics Reference
        link: https://developer.arm.com/architectures/instruction-sets/intrinsics
        type: website
    - resource:
        title: QuantEdge — project source code
        link: https://github.com/poojithdevan4D/QuantEdge
        type: website



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
