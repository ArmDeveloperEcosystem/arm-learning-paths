---
title: Run optimized Arm AI Portal image upscaling models on Android

description: Build Photo Upscale, import QuickSRNetSmall, SESR-M5, or RealESR-general-x4v3 through ExecuTorch, and upscale saved photos locally on the CPU of an Arm-based Android device.
minutes_to_complete: 40
who_is_this_for: Android and machine learning developers who want to upscale saved photos locally on an Arm-based Android device using optimized models from the Arm AI Portal.
learning_objectives:
    - Prepare the Android command-line tools and connect an Arm-based Android phone.
    - Download and run supported upscaling models from the Arm AI Portal.
    - Recognize how the supplied adapter prepares image tiles, runs ExecuTorch, and combines the upscaled output.
prerequisites:
    - A macOS, Linux, or Windows development machine
    - An Arm-based Android phone with Android 9 or later, and the `arm64-v8a` Application Binary Interface (ABI)
    - Enough storage on the phone for the application and model files
    - Basic familiarity with terminal commands and Android applications
    - Git installed on the development machine
    - Python 3.10 or later with the `venv` and `pip` modules on the machine
    - Java Development Kit (JDK) 17 on the machine, available on your `PATH`
    - A tool for downloading files, and a tool for extracting ZIP archives on the machine
    - A data-capable USB cable
    - Network access for the first Gradle build and model downloads

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-11-25T15:50:53Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 338a03e4b43233c18e3a30bdf190dc343f1ed9dad67e9fdb1d710e4824f83456
  summary_generated_at: '2026-11-25T15:50:53Z'
  summary_source_hash: 338a03e4b43233c18e3a30bdf190dc343f1ed9dad67e9fdb1d710e4824f83456
  faq_generated_at: '2026-11-25T15:50:53Z'
  faq_source_hash: 338a03e4b43233c18e3a30bdf190dc343f1ed9dad67e9fdb1d710e4824f83456
  summary: >-
    You'll build Photo Upscale for an Arm-based Android phone and import an Arm AI Portal model. You'll use the application to
    upscale a saved photo locally with ExecuTorch. First, you'll prepare the Android tools and
    connect your phone. You'll then download QuickSRNetSmall, compare the original and upscaled
    images, and save a PNG. Finally, you'll examine how the app validates models, processes image
    tiles, blends outputs, and measures processing time.
  faqs:
  - question: How do I know that my Android phone is connected and authorized for debugging?
    answer: >-
      Run `adb devices -l` and check that your phone and its serial appear. If you see
      `unauthorized`, unlock the phone and accept the USB debugging prompt. If your phone doesn't
      appear, see [Run apps on a hardware device](https://developer.android.com/studio/run/device).
  - question: Which model should I import first, and how do I select it?
    answer: >-
      Start with QuickSRNetSmall. Set `MODEL_ID` to its repository ID and run the download commands
      from the project directory. Copy `quicksr.pte` to the **Downloads** directory of the phone.
      In Photo Upscale, select **Add or change model** and choose `quicksr.pte` from **Downloads**.
  - question: Why does the model download result in a connection to huggingface.co?
    answer: >-
      The `download_model.py` download script calls `huggingface_hub` and connects to
      `https://huggingface.co` by default. The script retrieves Arm AI Portal models hosted on Hugging Face.
  - question: What result should I expect after running inference?
    answer: >-
      Expect an image four times wider and taller than your input. With the supplied 96 × 64
      example image, you should see an output image with dimensions 384 × 256. Compare the original and upscaled detail, then
      save the output as a PNG.
  - question: How does Photo Upscale process photos larger than one tile?
    answer: >-
      You can use a photo with dimensions up to 512 × 512 pixels. Photo Upscale rejects larger photos. When either
      dimension exceeds 128 pixels, Photo Upscale splits the photo into overlapping 128-pixel tiles. It
      upscales each tile with ExecuTorch, and blends the outputs.
# END generated_summary_faq

author: Matt Cossins
generate_summary_faq: false
rerun_summary: false
rerun_faqs: false
skilllevels: Introductory
subjects: AI/ML
armips:
    - Cortex-A
tools_software_languages:
    - Android Studio
    - Java
    - ExecuTorch
    - XNNPACK
    - Arm AI Portal
    - Hugging Face
operatingsystems:
    - Android
further_reading:
    - resource:
        title: Arm AI Portal model catalog
        link: https://developer.arm.com/ai/models
        type: documentation
    - resource:
        title: Run apps on a hardware device
        link: https://developer.android.com/studio/run/device
        type: documentation
    - resource:
        title: Run ExecuTorch on Android
        link: https://docs.pytorch.org/executorch/stable/using-executorch-android.html
        type: documentation
    - resource:
        title: XNNPACK backend for ExecuTorch
        link: https://docs.pytorch.org/executorch/stable/backends-xnnpack.html
        type: documentation
### FIXED, DO NOT MODIFY
weight: 1
layout: learningpathall
learning_path_main_page: "yes"
---
