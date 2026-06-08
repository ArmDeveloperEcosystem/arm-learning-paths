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

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T23:50:22Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 9ccf2cdd6406694d85c553204479d7ff1f688512056a3c76d4c85266cdc418b1
  summary_generated_at: '2026-06-02T02:47:30Z'
  summary_source_hash: 9ccf2cdd6406694d85c553204479d7ff1f688512056a3c76d4c85266cdc418b1
  faq_generated_at: '2026-06-02T23:50:22Z'
  faq_source_hash: 9ccf2cdd6406694d85c553204479d7ff1f688512056a3c76d4c85266cdc418b1
  summary: >-
    Learn to build and deploy an on-device customer support chatbot for Android using Meta’s Llama
    3.2 and the ExecuTorch runtime with KleidiAI integrated through XNNPACK on Arm. You set up
    a development environment on macOS or Linux, install ExecuTorch in a Python virtual environment,
    obtain the Llama 3.2 1B Instruct model, and export it to .pte for on-device inference. You
    then cross-compile ExecuTorch and a Llama runner with the Android NDK and CMake, enabling
    KleidiAI kernels for Arm chips with the i8mm feature, and run the model on an Arm-powered
    Android phone to verify inference performance. Prerequisites include a compatible host, an
    Android device with i8mm and 16GB RAM, adb, Java 17 JDK, Python 3.10+, and a Hugging Face
    account with Llama access.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need a macOS (Apple M1/M2/M3) or Linux machine with at least 16GB RAM, and an Arm-powered
      Android smartphone with the i8mm feature and 16GB RAM. Also prepare a USB cable, adb (Android
      SDK Platform Tools), Java 17 JDK, Python 3.10 or later, and a Hugging Face account with
      access to Meta Llama models.
  - question: Should I use a Python virtual environment for ExecuTorch, and which Python version
      is required?
    answer: >-
      Yes, the best practice is to create an isolated Python virtual environment before installing
      ExecuTorch dependencies. Use Python 3.10 or later.
  - question: How do I obtain and prepare the Llama model for ExecuTorch?
    answer: >-
      Request access on Meta’s Llama Downloads page, accept the Responsible Use Guide, and use
      the time-limited download link you receive. Install the llama-stack package from pip, download
      the model, and export it to .pte format optimized for on-device inference as described in
      the path.
  - question: Which Llama model variant does this path use, and can I try others?
    answer: >-
      This path uses the Llama 3.2 1B Instruct model. The same instructions apply to other variants
      with minimal modification.
  - question: How do I build and run the chatbot on Android, and how do I confirm it works?
    answer: >-
      Set the ANDROID_NDK path, ensure the CMake Android toolchain file is available, then use
      CMake to cross-compile ExecuTorch and libraries with KleidiAI and build the Llama runner
      for Android. Deploy to the phone, run the model, and follow the path’s steps to verify on-device
      inference performance without cloud dependency.
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

