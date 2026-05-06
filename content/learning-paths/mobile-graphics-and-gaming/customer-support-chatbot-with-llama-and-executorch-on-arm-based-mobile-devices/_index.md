---
title: Build a customer support chatbot on Android with Llama and ExecuTorch
description: Learn how to build a customer support chatbot for Android using Llama 3.2, ExecuTorch, and KleidiAI to run on-device inference on Arm platforms.

minutes_to_complete: 60

who_is_this_for: This is an introductory topic for software developers interested in building an on-device customer support chatbot for Android using Meta's Llama models and the ExecuTorch runtime.

learning_objectives:
    - Set up a development environment for building and deploying ExecuTorch-based apps on Android
    - Describe how ExecuTorch uses KleidiAI kernels to accelerate performance on Arm-based platforms
    - Export a Llama 3.2 model to .pte format optimized for on-device inference
    - Run a Llama model on an Arm-powered Android phone and verify inference performance
    - Build and run an Android chat app configured as a customer support assistant

prerequisites:
    - An Apple M1/M2/M3 development machine, or a Linux machine with at least 16GB of RAM
    - An Arm-powered smartphone with the i8mm feature running Android, with 16GB of RAM
    - A USB cable to connect your smartphone to your development machine
    - Android Debug Bridge (adb) installed. Follow the steps in [adb](https://developer.android.com/tools/adb) to install Android SDK Platform Tools
    - Java 17 JDK. Follow the steps in [Java SE 17 Archive Downloads](https://www.oracle.com/java/technologies/javase/jdk17-archive-downloads.html) to download and install JDK for your host
    - Python 3.10 or later
    - A [Hugging Face](https://huggingface.co/) account with access to Meta Llama models

generate_summary_faq: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-05-06T17:17:56Z'
  generator: template
  source_hash: 9ccf2cdd6406694d85c553204479d7ff1f688512056a3c76d4c85266cdc418b1
  summary: >-
    Learn how to build a customer support chatbot for Android using Llama 3.2, ExecuTorch, and
    KleidiAI to run on-device inference on Arm platforms. It is designed for software developers
    interested in building an on-device customer support chatbot for Android using Meta's Llama
    models and the ExecuTorch runtime. By the end, you will be able to set up a development environment
    for building and deploying ExecuTorch-based apps on Android, describe how ExecuTorch uses
    KleidiAI kernels to accelerate performance on Arm-based platforms, and export a Llama 3.2
    model to .pte format optimized for on-device inference. It focuses on tools and technologies
    such as Java, Python, and ExecuTorch, macOS, Linux, and Android environments, and Arm platforms
    including Cortex-A. The main steps cover Create a development environment, Set up ExecuTorch,
    Understand Llama models, Prepare Llama models for ExecuTorch, and Run the chatbot on Android.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will set up a development environment for building and deploying ExecuTorch-based apps
      on Android, describe how ExecuTorch uses KleidiAI kernels to accelerate performance on Arm-based
      platforms, and export a Llama 3.2 model to .pte format optimized for on-device inference.
      Learn how to build a customer support chatbot for Android using Llama 3.2, ExecuTorch, and
      KleidiAI to run on-device inference on Arm platforms.
  - question: Who is this Learning Path for?
    answer: >-
      This is an introductory topic for software developers interested in building an on-device
      customer support chatbot for Android using Meta's Llama models and the ExecuTorch runtime.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: An Apple M1/M2/M3 development machine,
      or a Linux machine with at least 16GB of RAM; An Arm-powered smartphone with the i8mm feature
      running Android, with 16GB of RAM; A USB cable to connect your smartphone to your development
      machine; Android Debug Bridge (adb) installed. Follow the steps in [adb](https://developer.android.com/tools/adb)
      to install Android SDK Platform Tools; Java 17 JDK. Follow the steps in [Java SE 17 Archive
      Downloads](https://www.oracle.com/java/technologies/javase/jdk17-archive-downloads.html)
      to download and install JDK for your host; Python 3.10 or later; A [Hugging Face](https://huggingface.co/)
      account with access to Meta Llama models.
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including Java, Python, and ExecuTorch, macOS, Linux, and
      Android environments, and Arm platforms such as Cortex-A.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Create a development environment, Set up ExecuTorch,
      Understand Llama models, Prepare Llama models for ExecuTorch, and Run the chatbot on Android.
# END generated_summary_faq

author: Parichay Das

### Tags
skilllevels: Introductory
subjects: ML
armips:
    - Cortex-A

tools_software_languages:
    - Java
    - Python
    - ExecuTorch

operatingsystems:
    - macOS
    - Linux
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
        title: KleidiAI
        link: https://gitlab.arm.com/kleidi/kleidiai
        type: website
    - resource:
        title: Build an Android chat app with Llama, KleidiAI, ExecuTorch, and XNNPACK
        link: /learning-paths/mobile-graphics-and-gaming/build-llama3-chat-android-app-using-executorch-and-xnnpack/
        type: learning-path


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

