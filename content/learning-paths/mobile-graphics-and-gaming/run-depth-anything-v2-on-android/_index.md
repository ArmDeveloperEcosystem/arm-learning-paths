---
title: Run an Arm AI Portal depth estimation model on Android

draft: true
cascade:
    draft: true

description: Run an Arm-optimized Depth Anything V2 Small model locally on an Arm-based Android phone with ExecuTorch and render a relative-disparity map.

minutes_to_complete: 35

who_is_this_for: This Learning Path is for Android and machine learning developers who want to run monocular depth estimation locally on an Arm-based Android phone.

learning_objectives:
    - Prepare the Android command-line tools and connect an Arm-based Android phone
    - Download and run the Depth Anything V2 Small INT8 ExecuTorch model from the Arm AI Portal
    - Explain the model's fixed image preprocessing and relative-disparity output
    - Validate input-dependent relative-disparity maps across two images

prerequisites:
    - A macOS, x86_64 Linux, or Windows development computer with Git, Python 3 with `venv` and `pip`, and JDK 17 or later
    - An Arm-based Android phone running Android 9 or later
    - A Hugging Face account if the model repository requires authentication
    - A data-capable USB cable
    - Network access for the first Gradle build and model download
    - Basic familiarity with terminal commands and Android applications

author: Elad Gross

generate_summary_faq: true
rerun_summary: true
rerun_faqs: true

### Tags
skilllevels: Introductory
subjects: ML
armips:
    - Cortex-A
    - Arm C1
tools_software_languages:
    - Kotlin
    - Python
    - ExecuTorch
    - XNNPACK
    - KleidiAI
    - Arm AI Portal
    - Hugging Face
operatingsystems:
    - Android
    - macOS
    - Linux
    - Windows

further_reading:
    - resource:
        title: Run an Arm AI Portal image segmentation model on Android
        link: https://learn.arm.com/learning-paths/mobile-graphics-and-gaming/run-image-to-image-models-on-android/
        type: learning path
    - resource:
        title: Depth Anything V2 Small INT8 model card
        link: https://developer.arm.com/ai/models/hugging-face/Arm/depth-anything-v2-small-int8-xnnpack-executorch-vivo-x300/depth-anything-v2-small-int8-pte
        type: documentation
    - resource:
        title: Depth Anything V2 Small INT8 on Hugging Face
        link: https://huggingface.co/Arm/depth-anything-v2-small-int8-xnnpack-executorch-vivo-x300
        type: documentation
    - resource:
        title: Run apps on a hardware device
        link: https://developer.android.com/studio/run/device
        type: documentation
    - resource:
        title: ExecuTorch for Android
        link: https://docs.pytorch.org/executorch/stable/using-executorch-android.html
        type: documentation
    - resource:
        title: XNNPACK backend for ExecuTorch
        link: https://docs.pytorch.org/executorch/stable/backends-xnnpack.html
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---
