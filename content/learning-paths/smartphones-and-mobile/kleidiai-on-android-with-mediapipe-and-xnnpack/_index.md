---
title: LLM inference on Android with KleidiAI, MediaPipe, and XNNPACK
draft: true
minutes_to_complete: 60

who_is_this_for: Android developers who want to efficiently run LLMs on-device.

learning_objectives:
    - Install prerequisites for cross-compiling new inference engines for Android.
    - Run (and benchmark) the Gemma 2B model using the Google MediaPipe ML framework, with XNNPACK as the primitive provider.
    - Improve inference efficiency with KleidiAI's int4 kernels via XNNPACK, and benchmark the results.

prerequisites:
    - You will need an x86_64 Linux machine running Ubuntu with approximately 500 MB of free space, or a docker daemon that can run a provided x86_64 image.
    - You will need an Android phone with support for i8mm (tested on Pixel 8 Pro)

author_primary: Pareena Verma, Joe Stech

### Tags
skilllevels: Advanced
subjects: ML
armips:
    - Cortex-A
    - Cortex-X
tools_software_languages:
    - Java
    - MediaPipe
    - Android SDK
    - Android NDK
    - Bazel
    - XNNPACK
operatingsystems:
    - Linux


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
