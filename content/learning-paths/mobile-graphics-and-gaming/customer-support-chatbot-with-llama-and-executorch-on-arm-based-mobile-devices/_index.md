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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-04T22:17:42Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: eedf979d466cc9fbcfd891c42fa892aee3f5fdfba92558849b506e282edf573e
  summary_generated_at: '2026-08-04T22:17:42Z'
  summary_source_hash: eedf979d466cc9fbcfd891c42fa892aee3f5fdfba92558849b506e282edf573e
  faq_generated_at: '2026-08-04T22:17:42Z'
  faq_source_hash: eedf979d466cc9fbcfd891c42fa892aee3f5fdfba92558849b506e282edf573e
  summary: >-
    You build and deploy an on-device customer support chatbot for Android using Meta’s Llama 3.2
    with the ExecuTorch runtime. You create an isolated Python environment, set up ExecuTorch, and
    review Llama capabilities to inform model choice. You obtain the Llama 3.2 1B Instruct weights,
    export the model to .pte for ExecuTorch, and
    cross-compile the Llama runner and ExecuTorch with XNNPACK and KleidiAI to target Arm cores
    with the i8mm feature for quantized inference. You then deploy to an Arm-powered Android phone,
    run the chatbot locally, validate that the model loads and responds to prompts,
    and verify inference performance without a cloud dependency.
  faqs:
  - question: How do I know my Android NDK path is set correctly before building?
    answer: >-
      Verify that ANDROID_NDK points to an installation containing build/cmake/android.toolchain.cmake.
      If that file exists, CMake can cross-compile the Android binaries.
  - question: Which Llama model variant should I use for this chatbot?
    answer: >-
      This path uses the Llama 3.2 1B Instruct model. The same instructions apply to other Llama
      variants with minimal modification.
  - question: What artifact should the export step produce for ExecuTorch?
    answer: >-
      Export the model to a .pte file optimized for on-device inference. The Android runner uses
      this .pte file to load and execute the model.
  - question: What should I check before deploying to my Android phone?
    answer: >-
      Connect the device over USB and ensure Android Debug Bridge (adb) is installed on the host.
      Confirm the phone is discoverable by adb before proceeding.
  - question: What result should I expect when I run the chatbot on Android?
    answer: >-
      The runner or app should load the exported Llama model and respond to prompts as a customer
      support assistant. You can then verify that inference runs on-device and observe performance
      on the target hardware.
# END generated_summary_faq

author: Parichay Das

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
