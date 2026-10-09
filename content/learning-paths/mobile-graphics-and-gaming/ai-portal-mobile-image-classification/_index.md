---
title: Run optimized image classification models from the Arm AI Portal on Android

description: Run Arm-optimized LiteRT, ExecuTorch, and CLIP image-classification models on Android, then extend Photo Insight for another compatible model or adapter.

minutes_to_complete: 35

who_is_this_for: Use this Learning Path if you develop Android or machine learning applications and want to run optimized image-classification models locally on an Arm-based Android device.

learning_objectives:
    - Prepare the Android command-line tools and connect an Arm-based Android phone.
    - Download and run supported models from the Arm AI Portal
    - Trace how the three supplied adapters import models, provide task-specific controls, preprocess inputs, run LiteRT or ExecuTorch, and format results
    - Optionally register another compatible model or generate and validate a separate adapter

prerequisites:
    - A macOS, Linux, or Windows development machine
    - An Arm-based Android phone with Android 9 or later and enough storage for the application and model files
    - Basic familiarity with terminal commands and Android applications
    - Git installed on the development machine
    - Python 3 with the `venv` and `pip` modules on the machine
    - Java Development Kit (JDK) 17 or later on the machine, available on your `PATH`
    - A tool for downloading files and a tool for extracting ZIP archives on the machine
    - A data-capable USB cable
    - A Hugging Face account
    - Network access for the first Gradle build and model downloads

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-26T16:56:45Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 6e0f0efa26de1574fa9d877ab87cf476e4923892c3639e9149e10e61fb7b88b3
  summary_generated_at: '2026-08-26T16:56:45Z'
  summary_source_hash: 6e0f0efa26de1574fa9d877ab87cf476e4923892c3639e9149e10e61fb7b88b3
  faq_generated_at: '2026-08-26T16:56:45Z'
  faq_source_hash: 6e0f0efa26de1574fa9d877ab87cf476e4923892c3639e9149e10e61fb7b88b3
  summary: >-
   You'll set up Android command-line tools, connect an Arm-based Android phone, and run an application called Photo
    Insight locally. First, you'll import Arm AI Portal image-classification models through LiteRT or ExecuTorch, compare
    fixed-label ImageNet results with zero-shot CLIP matching, and trace how adapters validate models and format
    results. You'll then register a compatible model or generate and validate an adapter for a model with a
    different contract.
  faqs:
  - question: How do I know my Android phone is ready for debugging?
    answer: >-
      Enable **Developer options** and **USB debugging**, then run `adb devices -l`. Confirm that your phone
      appears with the state `device`. If it reports `unauthorized`, unlock the phone and accept the debugging
      prompt. If it doesn't appear, see [Run apps on a hardware device](https://developer.android.com/studio/run/device).
  - question: Which option should I use in Photo Insight to run a specific runtime or task?
    answer: >-
      Select the mode that matches the runtime and task you want to use. **LiteRT Quick Identify** and
      **ExecuTorch Quick Identify** run fixed-label ImageNet classification. **ExecuTorch CLIP Custom Match**
      ranks candidate descriptions that you enter at run time.
  - question: What result should I expect after running a model?
    answer: >-
      Photo Insight formats the result according to the selected adapter. Fixed-label ImageNet models display
      ranked labels from their bundled label set. CLIP ranks the candidate descriptions that you enter at run time.
  - question: What is the difference between fixed-label and zero-shot classification?
    answer: >-
      Fixed-label classification assigns an image to labels from a predefined set, such as ImageNet labels.
      Zero-shot CLIP classification compares the image with candidate descriptions that you provide at run time,
      so you can define the categories without retraining the model.
  - question: How do I decide whether to register a model or create a new adapter?
    answer: >-
      Compare the model's task, runtime, methods, tensors, preprocessing, outputs, labels or tokenizer, and
      required assets with the supplied adapters. Register it only when all required elements match. If any
      required element differs, use the coding-agent workflow to generate and validate another adapter.
# END generated_summary_faq

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
    - LiteRT
    - ExecuTorch
    - XNNPACK
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
        title: Create and manage Android virtual devices
        link: https://developer.android.com/studio/run/managing-avds
        type: documentation
    - resource:
        title: LiteRT for Android
        link: https://ai.google.dev/edge/litert/android
        type: documentation
    - resource:
        title: ExecuTorch for Android
        link: https://docs.pytorch.org/executorch/stable/using-executorch-android.html
        type: documentation
    - resource:
        title: XNNPACK backend for ExecuTorch
        link: https://docs.pytorch.org/executorch/stable/backends-xnnpack.html
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---
