---
title: Build a customer support chatbot on Android with Llama and ExecuTorch

minutes_to_complete: 60

draft: true
cascade:
    draft: true

who_is_this_for: This is an introductory Learning Path for software developers interested in building an on-device customer support chatbot for Android using Meta's Llama models and the ExecuTorch runtime. The chatbot runs entirely on-device — no cloud dependency — making it suitable for privacy-sensitive support scenarios. The focus is on Arm-based Android devices, with performance acceleration using KleidiAI and XNNPACK.

learning_objectives:
    - Set up a development environment for building and deploying ExecuTorch-based apps on Android.
    - Describe how ExecuTorch uses KleidiAI kernels to accelerate performance on Arm-based platforms.
    - Export a Llama 3.2 model to .pte format optimized for on-device inference.
    - Run a Llama model on an Arm-powered Android phone and verify inference performance.
    - Build and run an Android chat app configured as a customer support assistant.

prerequisites:
    - An Apple M1/M2/M3 development machine, or a Linux machine with at least 16GB of RAM.
    - An Arm-powered smartphone with the i8mm feature running Android, with 16GB of RAM.
    - A USB cable to connect your smartphone to your development machine.
    - Android Debug Bridge (adb) installed. Follow the steps in [adb](https://developer.android.com/tools/adb) to install Android SDK Platform Tools. The adb tool is included in this package.
    - Java 17 JDK. Follow the steps in [Java SE 17 Archive Downloads](https://www.oracle.com/java/technologies/javase/jdk17-archive-downloads.html) to download and install JDK for your host.
    - Python 3.10 or later.
    - A [Hugging Face](https://huggingface.co/) account with access to Meta Llama models.

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
    - GenAI
    - LLM

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
