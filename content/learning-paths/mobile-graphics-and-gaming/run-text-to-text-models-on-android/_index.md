---
title: Run Arm AI Portal text-generation models on Android
description: Run validated Arm AI Portal text-generation models locally on Android with ExecuTorch, LiteRT, and ONNX Runtime, then extend the application for another model.

minutes_to_complete: 45

who_is_this_for: This Learning Path is for Android and machine learning developers who want to run optimized text-generation and text-embedding models locally on an Arm-based Android phone.

learning_objectives:
    - Prepare the Android command-line tools and connect an Arm-based Android phone.
    - Download and run an ExecuTorch text-generation model from the Arm AI Portal.
    - Understand how the starter application uses model catalog entries and runtime adapters.
    - Compare the validated ExecuTorch and ONNX Runtime GenAI adapter paths.

prerequisites:
    - A macOS, Linux, or Windows development machine with Git, Python 3.10 or later, and JDK 17
    - Tools for downloading and extracting ZIP archives on the machine
    - An Arm-based Android phone with enough free storage for application and model files
    - A data-capable USB cable
    - A Hugging Face account with access to the model repositories 
    - Basic familiarity with terminal commands and Android applications
    - Network access for the first Gradle build and model downloads

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-26T19:09:04Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: a769a51003cc02c288bf6e1c3dbe555a783dea2f4d20cdde45904ab718171088
  summary_generated_at: '2026-08-26T19:09:04Z'
  summary_source_hash: a769a51003cc02c288bf6e1c3dbe555a783dea2f4d20cdde45904ab718171088
  faq_generated_at: '2026-08-26T19:09:04Z'
  faq_source_hash: a769a51003cc02c288bf6e1c3dbe555a783dea2f4d20cdde45904ab718171088
  summary: >-
    You'll prepare Android command-line tools, connect an Arm-based phone, and run a validated Arm AI Portal text-generation model locally. First, you'll download SmolLM2 360M Instruct and build the starter application with its ExecuTorch adapter. Next, you'll copy the model into application-private storage and verify generated text offline. You'll also compare the ONNX Runtime GenAI adapter path and optionally prepare to support another model.
  faqs:
  - question: How do I know adb is ready to use my phone?
    answer: >-
      Run `adb devices -l` and look for your device marked `device` with a serial number. If it
      shows `unauthorized`, unlock the phone and accept the USB debugging prompt. On Windows,
      you might also need the phone manufacturer's USB driver.
  - question: Where should I place the model files on the device?
    answer: >-
      The application loads models from `filesDir/models/<model-id>/`. For development, stage the
      package under `/data/local/tmp` and use the `run-as` command to copy it into the application's
      private directory.
  - question: Which identifiers do I use to run the starter application?
    answer: >-
      Use `ANDROID_PACKAGE=com.arm.learningpath.texttotext` and
      `MODEL_ID=smollm2-360m-instruct-8da4w-xnnpack-executorch`. Keep the identifiers consistent
      with the entries in `model_catalog.json`.
  - question: How do I switch between ExecuTorch and ONNX Runtime GenAI adapters?
    answer: >-
      `ui/MainActivity.kt` reads the selected entry from `model_catalog.json`, and
      `inference/RuntimeRunnerFactory.kt` creates the adapter named by its `runtime` field. Select the
      validated catalog entry for the runtime you want to use.
  - question: How do I confirm that the sample runs offline?
    answer: >-
      Enable airplane mode and run the prompts again. Expect relevant, readable text without prompt
      echoes, role markers, tokenizer control tokens, or runtime diagnostics. This confirms that the
      model generates responses on-device without a network connection.
# END generated_summary_faq

author: Rachel Belachew

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: ML
armips:
    - Cortex-A
tools_software_languages:
    - Kotlin
    - Java
    - Python
    - Android Studio
    - ONNX Runtime
    - LiteRT
    - ExecuTorch
    - Arm AI Portal
    - Hugging Face

operatingsystems:
    - Android
    - macOS
    - Linux
    - Windows

further_reading:
    - resource:
        title: Arm AI Portal model catalog
        link: https://developer.arm.com/ai/models
        type: documentation
    - resource:
        title: ExecuTorch for Android
        link: https://docs.pytorch.org/executorch/stable/using-executorch-android.html
        type: documentation
    - resource:
        title: ONNX Runtime mobile deployment
        link: https://onnxruntime.ai/docs/tutorials/mobile/
        type: documentation
    - resource:
        title: LiteRT for Android
        link: https://ai.google.dev/edge/litert/android
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---

## What is the Arm AI Portal?

The [Arm AI Portal](https://developer.arm.com/ai/models) provides a catalog of AI models across different runtimes, use cases, optimization profiles, and Arm-based targets. It includes benchmarking and compatibility information, code examples, and deployment guidance.

Use an Android example application to run optimized text models from the Arm AI Portal on a physical Arm-based Android phone. Start with SmolLM2 text generation through ExecuTorch, then use the same application structure to explore validated LiteRT and ONNX models.

An application-level adapter connects the shared Android interface to one model workflow and runtime. It validates the model package, prepares text inputs, invokes ExecuTorch, LiteRT, or ONNX Runtime, and converts the outputs into generated text or an embedding summary.
