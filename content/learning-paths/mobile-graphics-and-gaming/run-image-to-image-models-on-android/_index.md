---
title: Run an Arm AI Portal image segmentation model on Android
description: Run the Arm-optimized MobileSAM model locally on an Android phone with ExecuTorch and inspect its image-segmentation adapter.

minutes_to_complete: 40

who_is_this_for: This Learning Path is for Android and machine learning developers who want to run an optimized image-segmentation model locally on an Arm-based Android phone.

learning_objectives:
    - Prepare the Android command-line tools and connect an Arm-based Android phone
    - Download and run the MobileSAM ExecuTorch model from the Arm AI Portal
    - Understand how the Android adapter validates, prepares, and renders MobileSAM results
    - Optionally inspect an unsupported image model before implementing a model-specific adapter

prerequisites:
    - A macOS, Linux, or Windows development computer with Git, Python 3, and Java 17 or later
    - An Arm-based Android phone running Android 9 or later
    - A Hugging Face account 
    - A data-capable USB cable
    - Basic familiarity with terminal commands and Android applications
    - Network access for the first Gradle build and model download

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-27T16:21:44Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: fae64ee9e2e918f7a895c5cbe2981b6926d07eb1651cd4fad02bf2949f26a5df
  summary_generated_at: '2026-08-27T16:21:44Z'
  summary_source_hash: fae64ee9e2e918f7a895c5cbe2981b6926d07eb1651cd4fad02bf2949f26a5df
  faq_generated_at: '2026-08-27T16:21:44Z'
  faq_source_hash: fae64ee9e2e918f7a895c5cbe2981b6926d07eb1651cd4fad02bf2949f26a5df
  summary: >-
    You'll build Image Analysis and use its validated ExecuTorch adapter to run MobileSAM locally on an Arm-based
    Android phone. You'll prepare the Android SDK, connect the phone, and let Gradle provision the JDK 17 build
    toolchain. You'll then download and stage the model, generate and validate masks from two images, and inspect
    the adapter's preprocessing and output checks. An optional final section helps you plan and validate another
    model-specific adapter.
  faqs:
  - question: How do I verify my Android phone is connected and authorized?
    answer: >-
      Enable **Developer options** and **USB debugging**, then run `adb devices -l`. The output
      should list the device with its serial and show it as authorized. If it reports `unauthorized`,
      unlock the phone and accept the debugging prompt. On Windows, you might also need the phone
      manufacturer’s USB driver.
  - question: How does the project obtain the JDK 17 build toolchain?
    answer: >-
      Your installed `java` and `javac` commands must report JDK 17 or later so that Gradle can start.
      The project configures Gradle to use a compatible JDK 17 build toolchain and download one
      automatically when it isn't already available.
  - question: How do I run MobileSAM on the Android phone?
    answer: >-
      Download `mobile_sam_raspberry_executorch_optimized.pte`. Copy it into the directory named by the MobileSAM
      catalog entry under application-private storage, then start Image Analysis. Select **Load model**,
      choose an image, and select **Run segmentation** to generate the mask.
  - question: What confirms that MobileSAM produced a valid result?
    answer: >-
      Check that the application displays a translucent cyan mask over a plausible object boundary.
      Confirm that Image Analysis reports finite intersection over union (IoU), coverage, and logit values.
      Run a second image and confirm that the mask changes with the input.
  - question: Can Image Analysis run another model without code changes?
    answer: >-
      Image Analysis already includes validated ExecuTorch adapters for MobileSAM and Depth Anything V2.
      Another model needs a compatible catalog entry and a model-specific adapter. The included LiteRT
      and ONNX adapter files are stubs that need implementation and device validation before use.
# END generated_summary_faq

author: Rachel Belachew

generate_summary_faq: true
rerun_summary: true
rerun_faqs: true


### Tags
skilllevels: Introductory
subjects: ML
armips:
    - Cortex-A
tools_software_languages:
    - Kotlin
    - Python
    - ExecuTorch
    - XNNPACK
    - KleidiAI
    - Arm AI Portal
    - Hugging Face
operatingsystems:
    - Android
    - macOS
    - Linux
    - Windows

further_reading:
    - resource:
        title: Run Depth Anything V2 depth estimation on Android
        link: https://learn.arm.com/learning-paths/mobile-graphics-and-gaming/run-depth-anything-v2-on-android/
        type: learning path
    - resource:
        title: Arm AI Portal
        link: https://developer.arm.com/ai/models
        type: documentation
    - resource:
        title: Run apps on a hardware device
        link: https://developer.android.com/studio/run/device
        type: documentation
    - resource:
        title: Android Debug Bridge
        link: https://developer.android.com/tools/adb
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
