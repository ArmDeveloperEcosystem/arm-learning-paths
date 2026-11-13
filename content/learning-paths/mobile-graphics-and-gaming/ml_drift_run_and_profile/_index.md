---
title: Run and Profile ML Drift on Arm Mali GPUs

draft: true
cascade:
    draft: true
    
description: Build and run Stable Diffusion on an Android Mali GPU with ML Drift, inspect a unified shader, and profile GPU activity with Arm Streamline.
minutes_to_complete: 30
lastmod: 2026-10-30
who_is_this_for: GPU and system engineers who want to explore ML Drift and its unified shaders for GPU-accelerated workloads in custom graphics and inference runtimes.
learning_objectives:
    - Build and run Stable Diffusion on an Android device with an Arm Mali GPU
    - Capture and inspect Mali GPU activity with Arm Streamline
prerequisites:
    - An Android device with an Arm Mali GPU
    - Android Studio
    - Arm Performance Studio
    - Familiarity with C++ and command-line tools
author: Kieran Hejmadi
draft: true
cascade:
    draft: true
generate_summary_faq: true
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: ML
armips:
    - Mali
tools_software_languages:
    - C++
    - OpenCL
    - ML Drift
    - Streamline
operatingsystems:
    - macOS
    - Android
further_reading:
    - resource:
        title: ML Drift launch announcement
        link: https://developers.googleblog.com/ml-drift-next-gen-gpu-aiml-inference-at-the-edge/
        type: blog
    - resource:
        title: ML Drift source repository
        link: https://github.com/google-ai-edge/ml-drift
        type: code
    - resource:
        title: Arm Streamline User Guide
        link: https://support.arm.com/documentation/101816/latest/
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
