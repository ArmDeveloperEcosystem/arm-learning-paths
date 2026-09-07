---
title: Run optimized Whisper speech transcription models from the Arm AI Portal on Arm-powered Android devices

description: Run Arm-optimized Whisper models with LiteRT and ExecuTorch locally on Android, then extend Whisper Journal for another compatible model or adapter.

minutes_to_complete: 35

who_is_this_for: This Learning Path is for Android and machine learning developers who want to run optimized speech recognition models locally on an Arm-based Android device.

learning_objectives:
    - Prepare the Android command-line tools and connect an Arm-based Android phone.
    - Run Whisper Base with LiteRT, then compare it with Whisper Tiny running with ExecuTorch.
    - Understand how the importer installs model packages, the recorder captures audio, and the two supplied adapters run LiteRT or ExecuTorch and decode a transcript.
    - Register another compatible model or generate and validate a separate adapter.

prerequisites:
    - A macOS, Linux, or Windows development machine
    - An Arm-based Android phone with Android 9 or later and enough storage and memory for the application and model packages
    - Basic familiarity with terminal commands and Android applications
    - Git installed on the development machine
    - Python 3 with the `venv` and `pip` modules on the machine
    - Java Development Kit (JDK) 17 or later on the machine, available on your `PATH`
    - A tool for downloading files and a tool for extracting ZIP archives on the machine
    - A data-capable USB cable and microphone access on the phone
    - Network access for the first Gradle build and model downloads
    - A Hugging Face account with access to the model repositories

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-20T16:37:40Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 8f7ec47b76b780d899d9d42c1166aae9fab6e75c2b48707b5bb45f7f05d1abc8
  summary_generated_at: '2026-08-20T16:37:40Z'
  summary_source_hash: 8f7ec47b76b780d899d9d42c1166aae9fab6e75c2b48707b5bb45f7f05d1abc8
  faq_generated_at: '2026-08-20T16:37:40Z'
  faq_source_hash: 8f7ec47b76b780d899d9d42c1166aae9fab6e75c2b48707b5bb45f7f05d1abc8
  summary: >-
    You'll set up Android command-line tools, connect an Arm-based Android phone, and run an application called Whisper
    Journal locally. First, you'll transcribe speech with Whisper Base and LiteRT, then compare it with
    Whisper Tiny and ExecuTorch using the same recording conditions. Next, you'll trace how the importer,
    recorder, registry, and adapters connect each model package to an English transcript. Finally, you'll
    register a compatible model or generate and validate an adapter for a model with a different contract.
  faqs:
  - question: Which Android SDK and API levels do I need?
    answer: >-
      Install Android SDK Platform 35, Platform-Tools, and Build-Tools 34.0.0. The sample project
      compiles against API 35 and supports Android 9 (API 28) or later.
  - question: How do I know my Android phone is ready before installing the app?
    answer: >-
      Use Android Debug Bridge (`adb`) from Android SDK Platform-Tools to confirm that the phone is
      authorized, uses the `arm64-v8a` ABI, and runs Android 9 (API 28) or later.
  - question: Which adapter should I use for my Whisper package?
    answer: >-
      Select Whisper Base for the first workflow and Whisper Tiny for the guided comparison. The
      application registry chooses the LiteRT adapter for Base and the ExecuTorch adapter for Tiny.
      It also registers LiteRT profiles for Medium and Large V3 and the ExecuTorch adapter for Small.
  - question: What result should I expect after running inference?
    answer: >-
      The app records audio and produces an English transcript in a journal entry. Inference runs
      locally on the Android CPU, and the app doesn't upload the recording to a server.
  - question: How do I extend the app for a speech model that's not in the registered list?
    answer: >-
      Compare the model's task, runtime, package files, callable methods or signatures, tensors,
      audio preprocessing, tokenizer, decoder behavior, and output format with the supplied adapters.
      If the model doesn't match an adapter, modify an adapter or create a new one. Register it in
      `AdapterRegistry` and update the decoder profile when needed.
# END generated_summary_faq

author: 
- Kwashie Andoh
- Matt Cossins

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
    - resource:
        title: Whisper model repository
        link: https://github.com/openai/whisper
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---
