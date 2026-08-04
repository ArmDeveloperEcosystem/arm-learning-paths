---
title: Build an Android chat app with Llama, KleidiAI, ExecuTorch, and XNNPACK 
description: Learn how to build an Android chat application with Llama models using ExecuTorch, XNNPACK, and KleidiAI for accelerated performance on Arm smartphones.

minutes_to_complete: 60

who_is_this_for: This is an introductory topic for software developers interested in learning how to build an Android chat app with Llama, KleidiAI, ExecuTorch, and XNNPACK.

learning_objectives: 
    - Set up an ExecuTorch development environment.
    - Describe how ExecuTorch uses KleidiAI kernels to accelerate performance on Arm-based platforms.
    - Describe how 4-bit groupwise PTQ quantization reduces model size without significantly sacrificing model accuracy.
    - Build and run Llama models using ExecuTorch on your development machine.
    - Build and run an Android Chat app with different Llama models using ExecuTorch on an Arm-based smartphone.

prerequisites:
    - An Apple M1/M2 development machine with Android Studio installed or a Linux machine with at least 16GB of RAM.
    - An Arm-powered smartphone with the i8mm feature running Android, with 16GB of RAM.
    - A USB cable to connect your smartphone to your development machine.
    - Android Debug Bridge (adb) installed on your device. Follow the steps in [adb](https://developer.android.com/tools/adb)  to install Android SDK Platform Tools. The adb tool is included in this package.
    - Java 17 JDK. Follow the steps in [Java 17 JDK](https://www.oracle.com/java/technologies/javase/jdk17-archive-downloads.html) to download and install JDK for host.
    - Python 3.10.

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-04T22:16:49Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: a67074a2109bf0e98428dda0b2c4134bdb03aa16229cc09b899b5906f98c2ec9
  summary_generated_at: '2026-08-04T22:16:49Z'
  summary_source_hash: a67074a2109bf0e98428dda0b2c4134bdb03aa16229cc09b899b5906f98c2ec9
  faq_generated_at: '2026-08-04T22:16:49Z'
  faq_source_hash: a67074a2109bf0e98428dda0b2c4134bdb03aa16229cc09b899b5906f98c2ec9
  summary: >-
    You set up ExecuTorch with XNNPACK and KleidiAI, prepare
    a Llama 3.2 1B model, and cross-compiling Android components that run on Arm smartphones with
    the i8mm feature. You build the ExecuTorch runtime and JNI libraries, then deploy a Llama
    runner and a simple chat application to validate on‑device inference. You learn how
    KleidiAI kernels integrate through XNNPACK and how 4‑bit groupwise post‑training quantization
    reduces model size while maintaining practical accuracy for Arm targets. Finally, you configure
    the Android NDK toolchain and run a benchmark on real hardware to confirm
    the end‑to‑end setup.
  faqs:
  - question: Which Python environment option should I use for ExecuTorch?
    answer: >-
      Use either a Python virtual environment or a Conda environment; you only need one. Creating
      an isolated environment is the recommended practice before installing ExecuTorch dependencies.
  - question: How do I verify the Android NDK is configured before cross-compiling?
    answer: >-
      Set the ANDROID_NDK environment variable to your NDK installation. Confirm that $ANDROID_NDK/build/cmake/android.toolchain.cmake
      exists so CMake can cross-compile.
  - question: Which Llama model do the steps use, and can I substitute another?
    answer: >-
      The steps use the Llama 3.2 1B Instruct model. The same instructions apply to other options
      with minimal modification.
  - question: What should I check before deploying to the phone?
    answer: >-
      Connect the Arm-based Android smartphone over USB and ensure Android Debug Bridge (adb)
      from the Android SDK Platform Tools is installed. This allows the development machine to
      discover and communicate with the device.
  - question: What result should I expect when running the benchmark or app on the device?
    answer: >-
      The Llama runner or chat application should execute on the phone using the exported model
      without errors. A successful run indicates that model preparation, the ExecuTorch build,
      and the Android NDK configuration are correct.
# END generated_summary_faq

author: 
    - Varun Chari
    - Pareena Verma

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: ML
armips:
    - Cortex-A
tools_software_languages:
    - Java
    - CPP
    - Python
    - Hugging Face
    - ExecuTorch

operatingsystems:
    - macOS
    - Android

further_reading:
    - resource:
        title: ExecuTorch Overview
        link: https://pytorch.org/executorch-overview
        type: website
    - resource:
        title: ExecuTorch Documentation
        link: https://pytorch.org/executorch/stable/index.html
        type: documentation
    - resource:
        title: ExecuTorch Examples
        link: https://github.com/pytorch/executorch/blob/main/examples/README.md
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
