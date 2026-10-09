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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-05T14:58:35Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: eedf979d466cc9fbcfd891c42fa892aee3f5fdfba92558849b506e282edf573e
  summary_generated_at: '2026-08-05T14:58:35Z'
  summary_source_hash: eedf979d466cc9fbcfd891c42fa892aee3f5fdfba92558849b506e282edf573e
  faq_generated_at: '2026-08-05T14:58:35Z'
  faq_source_hash: eedf979d466cc9fbcfd891c42fa892aee3f5fdfba92558849b506e282edf573e
  summary: >-
    You'll build and deploy an on-device Android customer support chatbot with Meta’s Llama 3.2,
    ExecuTorch, and KleidiAI. First, you'll set up the environment and choose a model and quantization approach. Then, you'll
    obtain Llama 3.2 1B Instruct weights and export them to `.pte`. Finally, you'll cross-compile the runner with
    the Android NDK and enable KleidiAI through XNNPACK, then deploy to an Arm phone and run inference.
  faqs:
  - question: Which Llama model variant should I download, and can I use a different one?
    answer: >-
      You should use the Llama 3.2 1B Instruct model. If you want to use a different model, you can adapt the same steps to other
      variants with minimal modification.
  - question: What output should I have after exporting the model for ExecuTorch?
    answer: >-
      You should produce a `.pte` file. This format is optimized for on-device inference and is
      loadable by the ExecuTorch runtime.
  - question: What should I check if the Android cross-compile step fails to find the toolchain?
    answer: >-
      Verify that `ANDROID_NDK` is set to the correct path and that `build/cmake/android.toolchain.cmake`
      exists there. Also confirm your ExecuTorch dependencies are installed in the Python environment.
  - question: How do I make sure KleidiAI acceleration is included in my Android build?
    answer: >-
      Build ExecuTorch and its libraries for Android with KleidiAI kernels enabled through XNNPACK. Use the provided CMake configuration to include these kernels.
  - question: What result should I expect when I run the chatbot on the phone?
    answer: >-
      The Llama runner or chat app should load the exported model and generate responses to prompts
      on the device.
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
