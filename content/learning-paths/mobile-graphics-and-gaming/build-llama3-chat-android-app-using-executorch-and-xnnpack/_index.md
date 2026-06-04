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

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T23:49:55Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 688b5b6eddc0480fa732308802d225696371c22a468bb6b140c6b74908222bbc
  summary_generated_at: '2026-06-02T02:46:55Z'
  summary_source_hash: 688b5b6eddc0480fa732308802d225696371c22a468bb6b140c6b74908222bbc
  faq_generated_at: '2026-06-02T23:49:55Z'
  faq_source_hash: 688b5b6eddc0480fa732308802d225696371c22a468bb6b140c6b74908222bbc
  summary: >-
    Learn how to build and deploy a simple LLM-based Android chat app using ExecuTorch with XNNPACK
    and KleidiAI on Arm smartphones. You will set up an ExecuTorch development environment, prepare
    the Llama 3.2 1B Instruct model, and understand how KleidiAI kernels and the i8mm feature
    accelerate quantized LLMs, along with the role of 4-bit groupwise PTQ. The path covers building
    the ExecuTorch runtime and JNI libraries, cross-compiling a Llama runner with the Android
    NDK, and running benchmarks on device. Prerequisites include an Apple M1/M2 or Linux host,
    an Arm-powered Android phone with i8mm (both with 16GB RAM), USB, adb, Java 17 JDK, and Python
    3.10. Estimated time: about 60 minutes.
  faqs:
  - question: Do I need macOS or Linux for the host, and what resources are required?
    answer: >-
      Use an Apple M1/M2 development machine with Android Studio installed, or a Linux machine
      with at least 16GB of RAM. Python 3.10 and Java 17 JDK are also required.
  - question: What Android device requirements should I confirm before starting?
    answer: >-
      Use an Arm-powered smartphone running Android that includes the i8mm feature and has 16GB
      of RAM. You also need a USB cable and adb (from Android SDK Platform Tools) installed on
      your host.
  - question: When setting up ExecuTorch, should I use a Python virtual environment or Conda?
    answer: >-
      Create an isolated Python environment for ExecuTorch; you can use either a Python virtual
      environment or a Conda environment. You only need one of these options.
  - question: How do I obtain and prepare the Llama model used in this path?
    answer: >-
      Request access to Llama from Meta’s Llama Downloads page, accept the Responsible Use Guide,
      and use the provided 24-hour download link. Install the llama-stack package from pip, then
      download the Llama 3.2 1B Instruct model following the provided steps.
  - question: What should I set before cross-compiling the Llama runner for Android, and what
      outputs should I expect?
    answer: >-
      Set ANDROID_NDK to your NDK path and ensure the CMake android.toolchain.cmake file is available.
      The build produces the ExecuTorch runtime with KleidiAI, associated libraries (including
      JNI libraries), and a Llama runner binary for Android.
# END generated_summary_faq

author: 
    - Varun Chari
    - Pareena Verma

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

