---
title: Run an Arm AI Portal image segmentation model on Android
description: Run the Arm-optimized MobileSAM model locally on an Android phone with ExecuTorch and inspect its image-segmentation adapter.

minutes_to_complete: 40

who_is_this_for: This Learning Path is for Android and machine learning developers who want to run an optimized image-segmentation model locally on an Arm-based Android phone.

learning_objectives:
    - Prepare the Android command-line tools and connect an Arm-based Android phone
    - Download and run the MobileSAM ExecuTorch model from the Arm AI Portal
    - Understand how the Android adapter validates, prepares, and renders MobileSAM results
    - Optionally inspect another image model before implementing a model-specific adapter

prerequisites:
    - A macOS, Linux, or Windows development computer with Git, Python 3, and Java 17 or later
    - An Arm-based Android phone running Android 9 or later
    - A Hugging Face account 
    - A data-capable USB cable
    - Basic familiarity with terminal commands and Android applications

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
    You'll build and run a MobileSAM image-segmentation application on an Arm-based Android phone. First, you'll
    install Android command-line tools. Next, you'll connect the phone, download the validated ExecuTorch
    model from the Arm AI Portal, and stage it in application-private storage. After selecting an
    image and box prompt, you'll inspect the adapter’s preprocessing, output validation, and mask
    rendering. Finally, you'll optionally learn how to use AI Portal models without a validated adapter.
  faqs:
  - question: How do I verify my Android phone is connected and authorized?
    answer: >-
      Enable **Developer options** and **USB debugging**, then run `adb devices -l`. The output
      should list the device with its serial and show it as authorized. If it reports `unauthorized`,
      unlock the phone and accept the debugging prompt. On Windows, you might also need the phone
      manufacturer’s USB driver.
  - question: What does the MobileSAM run produce?
    answer: >-
      After you select an image and run segmentation, the application displays a translucent cyan
      mask over the selected object. The result panel reports the selected mask, predicted IoU, and
      mask coverage. It also reports the mask logit range, model load time, and run time.
  - question: How do I run MobileSAM on the Android phone?
    answer: >-
      Download `mobile_sam_raspberry_executorch_optimized.pte`. Copy it into the directory named by the MobileSAM
      catalog entry under application-private storage, and start the application. Select **Load
      model**, choose an image, and select **Run segmentation** to generate the mask.
  - question: Do I need to modify the code to run the validated MobileSAM path?
    answer: >-
      No. The application already includes the catalog entry, adapter, preprocessing, and mask
      rendering for MobileSAM with ExecuTorch.
  - question: What should I check before using a different model?
    answer: >-
      Review the model’s runtime dependencies, tensor mappings, preprocessing, prompt control, output
      decoder, and visualization needs. The included LiteRT and ONNX adapter files are stubs and
      need implementation and validation before they can execute a new model.
# END generated_summary_faq

author: Rachel Belachew

generate_summary_faq: true
rerun_summary: false
rerun_faqs: false


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
