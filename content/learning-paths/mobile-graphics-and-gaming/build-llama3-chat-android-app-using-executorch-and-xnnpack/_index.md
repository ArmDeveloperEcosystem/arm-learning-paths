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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-05T14:58:01Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: a67074a2109bf0e98428dda0b2c4134bdb03aa16229cc09b899b5906f98c2ec9
  summary_generated_at: '2026-08-05T14:58:01Z'
  summary_source_hash: a67074a2109bf0e98428dda0b2c4134bdb03aa16229cc09b899b5906f98c2ec9
  faq_generated_at: '2026-08-05T14:58:01Z'
  faq_source_hash: a67074a2109bf0e98428dda0b2c4134bdb03aa16229cc09b899b5906f98c2ec9
  summary: >-
    You'll build and deploy an Android LLM chat app with ExecuTorch, XNNPACK, and KleidiAI on an Arm
    smartphone. First, you'll set up an isolated Python environment, prepare a Llama 3.2 1B Instruct model,
    and enable KleidiAI through XNNPACK for supported Arm chips. Then, you'll cross-compile the runner and
    JNI libraries with the Android NDK, integrate them, deploy the app, and run benchmarks.
  faqs:
  - question: Which Python environment should I use to install ExecuTorch dependencies?
    answer: >-
      Use an isolated environment. You can choose either a Python virtual environment or a Conda
      environment. You need only one environment.
  - question: How do I obtain and prepare the Llama 3.2 1B Instruct model for ExecuTorch?
    answer: >-
      Request access on Meta’s Llama Downloads page and use
      the time-limited download link you receive. Install the `llama-stack` package from `pip`, then
      run the provided command to download the model using your download link.
  - question: How do I know my Android NDK is set correctly before cross-compiling?
    answer: >-
      Set the `ANDROID_NDK` environment variable to your NDK path. Confirm that `$ANDROID_NDK/build/cmake/android.toolchain.cmake`
      exists so CMake can locate the Android toolchain.
  - question: What gets built when I compile for Android with KleidiAI enabled?
    answer: >-
      You'll build the ExecuTorch runtime and a Llama runner binary for Android, along with JNI libraries
      for the app. Use these artifacts to run the model and execute benchmarks on the Android
      device.
  - question: Can I use a different Llama model instead of 3.2 1B Instruct?
    answer: >-
      Yes. The same instructions apply to other Llama options with minimal modification.
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
