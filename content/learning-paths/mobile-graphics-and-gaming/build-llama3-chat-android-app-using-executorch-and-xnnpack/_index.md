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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-05-06T17:17:56Z'
  generator: template
  source_hash: 688b5b6eddc0480fa732308802d225696371c22a468bb6b140c6b74908222bbc
  summary: >-
    Learn how to build an Android chat application with Llama models using ExecuTorch, XNNPACK,
    and KleidiAI for accelerated performance on Arm smartphones. It is designed for software developers
    interested in learning how to build an Android chat app with Llama, KleidiAI, ExecuTorch,
    and XNNPACK. By the end, you will be able to set up an ExecuTorch development environment,
    describe how ExecuTorch uses KleidiAI kernels to accelerate performance on Arm-based platforms,
    and describe how 4-bit groupwise PTQ quantization reduces model size without significantly
    sacrificing model accuracy. It focuses on tools and technologies such as Java, CPP, Python,
    Hugging Face, and ExecuTorch, macOS and Android environments, and Arm platforms including
    Cortex-A. The main steps cover Create a development environment, ExecuTorch Setup, Understanding
    Llama models, Prepare Llama models for ExecuTorch, and Run Benchmark on Android phone.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will set up an ExecuTorch development environment, describe how ExecuTorch uses KleidiAI
      kernels to accelerate performance on Arm-based platforms, and describe how 4-bit groupwise
      PTQ quantization reduces model size without significantly sacrificing model accuracy. Learn
      how to build an Android chat application with Llama models using ExecuTorch, XNNPACK, and
      KleidiAI for accelerated performance on Arm smartphones.
  - question: Who is this Learning Path for?
    answer: >-
      This is an introductory topic for software developers interested in learning how to build
      an Android chat app with Llama, KleidiAI, ExecuTorch, and XNNPACK.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: An Apple M1/M2 development machine with
      Android Studio installed or a Linux machine with at least 16GB of RAM.; An Arm-powered smartphone
      with the i8mm feature running Android, with 16GB of RAM.; A USB cable to connect your smartphone
      to your development machine.; Android Debug Bridge (adb) installed on your device. Follow
      the steps in [adb](https://developer.android.com/tools/adb) to install Android SDK Platform
      Tools. The adb tool is included in this package.; Java 17 JDK. Follow the steps in [Java
      17 JDK](https://www.oracle.com/java/technologies/javase/jdk17-archive-downloads.html) to
      download and install JDK for host.; Python 3.10.
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including Java, CPP, Python, Hugging Face, and ExecuTorch,
      macOS and Android environments, and Arm platforms such as Cortex-A.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Create a development environment, ExecuTorch Setup,
      Understanding Llama models, Prepare Llama models for ExecuTorch, and Run Benchmark on Android
      phone.
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

