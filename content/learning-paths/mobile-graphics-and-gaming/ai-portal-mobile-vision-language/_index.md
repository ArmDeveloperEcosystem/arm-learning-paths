---
title: Run an optimized vision-language model from the Arm AI Portal on Android

draft: true
cascade:
    draft: true
    
description: Run the Arm-optimized Qwen3-VL model locally with llama.cpp to generate text from an image and prompt on Android.

minutes_to_complete: 35

who_is_this_for: This Learning Path is for Android and machine learning developers who want to run an optimized vision-language model locally on an Arm-based Android device.

learning_objectives:
    - Prepare the Android command-line tools and connect an Arm-based Android phone
    - Download and run the supported Qwen3-VL model package from the Arm AI Portal
    - Trace how Vision Chat validates and extracts the model package ZIP, prepares an image and prompt, runs llama.cpp, and generates text
    - Interpret model-load, image-and-prompt, and token-generation measurements on a physical phone

prerequisites:
    - A macOS, Linux, or Windows development machine
    - An Arm-based Android phone with Android 9 or later, `asimddp` and `i8mm` CPU features, and at least 4 GB of free storage
    - Basic familiarity with terminal commands and Android applications
    - Git installed on the development machine
    - Python 3 with the `venv` and `pip` modules on the machine
    - Java Development Kit (JDK) 17 or later on the machine, available on your `PATH`
    - A tool for downloading files and a tool for extracting ZIP archives on the machine
    - A data-capable USB cable
    - A Hugging Face account
    - Network access for the first Gradle build and model downloads

author: Matt Cossins

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: ML
armips:
    - Cortex-A
tools_software_languages:
    - Android Studio
    - Java
    - C++
    - llama.cpp
    - KleidiAI
    - Arm AI Portal
    - Hugging Face
operatingsystems:
    - Android

further_reading:
    - resource:
        title: Run apps on a hardware device
        link: https://developer.android.com/studio/run/device
        type: documentation
    - resource:
        title: Arm AI Portal model catalog
        link: https://developer.arm.com/ai/models
        type: documentation
    - resource:
        title: Qwen3-VL 2B Instruct model package
        link: https://huggingface.co/Arm/qwen3-vl-2b-instruct-q4-k-m-ggml-llama-cpp-vivo-x300
        type: documentation
    - resource:
        title: llama.cpp multimodal documentation
        link: https://github.com/ggml-org/llama.cpp/tree/master/tools/mtmd
        type: documentation
    - resource:
        title: KleidiAI repository
        link: https://github.com/ARM-software/kleidiai
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---
