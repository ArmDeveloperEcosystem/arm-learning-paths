---
title: Run optimized object-detection models from the Arm AI Portal on Android

description: Run Arm-optimized YOLOv5s, YOLOv8s, and YOLOv9s models on Android to detect objects in saved images or a live camera feed.

minutes_to_complete: 35

who_is_this_for: This Learning Path is for Android and machine learning developers who want to run optimized object detection locally on an Arm-based Android device. It demonstrates an ExecuTorch adapter that selects the preprocessing and output decoding required by supported YOLO models.

learning_objectives:
    - Prepare the Android command-line tools and connect an Arm-based Android phone
    - Download and run a supported object-detection model from the Arm AI Portal
    - Explain how the supplied adapter selects version-specific preprocessing and output decoding for supported YOLO models
    - Register another compatible detector or optionally generate and validate a separate adapter

prerequisites:
    - A macOS, Linux, or Windows development machine
    - Git installed on the development machine
    - Python 3 on the machine with the `venv` and `pip` modules
    - Java Development Kit (JDK) 17 or later, available on your machine's `PATH`
    - A tool for downloading files and a tool for extracting ZIP archives on the machine
    - An Arm-based Android phone with Android 9 or later with enough free storage for the application and model files
    - A Hugging Face account with access to the model repositories 
    - A data-capable USB cable
    - Network access for the first Gradle build and model downloads
    - Basic familiarity with terminal commands and Android applications

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-25T19:46:15Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: d9a501d32775df3afb23f03f0264284568d8415e524f9f828116d62e278db390
  summary_generated_at: '2026-08-25T19:46:15Z'
  summary_source_hash: d9a501d32775df3afb23f03f0264284568d8415e524f9f828116d62e278db390
  faq_generated_at: '2026-08-25T19:46:15Z'
  faq_source_hash: d9a501d32775df3afb23f03f0264284568d8415e524f9f828116d62e278db390
  summary: >-
    You'll build and run an application called Scene Detector on an Arm-based Android phone. First, you'll install the Android
    command-line tools, connect a device with `adb`, and build the application with Gradle. Next, you'll start with the Arm AI
    Portal YOLOv8s model in ExecuTorch. You'll analyze a saved image and a live camera feed, then learn how to
    register a compatible detector or create and validate an adapter for an unsupported model.
  faqs:
  - question: How do I verify that my Android phone is connected to adb?
    answer: >-
      Run `adb devices -l`. Confirm that your phone appears with a device serial and the state `device`.
      If it reports `unauthorized`, unlock the phone and accept the debugging prompt.
  - question: What should I check if adb doesn't list my phone on Linux?
    answer: >-
      Ensure Android `udev` rules are installed and that your user belongs to the `plugdev` group.
      Reconnect the device after updating the rules or group membership.
  - question: Do I need network access during setup?
    answer: >-
      Yes. The first Gradle build downloads dependencies, and the model downloader retrieves model files
      from Hugging Face.
  - question: How does the confidence threshold affect object detection?
    answer: >-
      A higher confidence threshold removes more lower-scoring detections. Reduce the default `75%`
      threshold if the model doesn't display expected objects, but be aware that lower thresholds can
      increase false positives and the amount of work passed to non-maximum suppression.
  - question: How do I add a detector that Scene Detector doesn't support?
    answer: >-
      Register the model directly if it matches a supplied detector strategy. Otherwise, use the coding
      agent workflow to generate another adapter.
  - question: How do I run detection on a saved image?
    answer: >-
      Import a supported `.pte` model, select **Choose saved image**, choose an image, and select **Detect objects**.
      The application displays the annotated image, detected objects, confidence scores, and processing time.
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
