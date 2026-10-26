---
title: Run optimized TinySD image generation from the Arm AI Portal on Arm-powered Android devices
description: Run an Arm-optimized TinySD image-generation model on Android with the supplied ExecuTorch adapter.
minutes_to_complete: 60

who_is_this_for: This Learning Path is for Android and machine learning developers who want to run an optimized text-to-image generation model locally on an Arm-based Android device.

learning_objectives:
    - Install the Android command-line tools and required SDK packages.
    - Build TinySD Studio and run it on an Arm-based Android phone.
    - Download, package, and import the TinySD ExecuTorch model, then generate a 512 x 512 image.
    - Compare images generated from the same prompt with different seeds.
    - Understand how the application adapter works and choose a route for another model package.

prerequisites:
    - A development machine supported by Android Studio
    - An Arm-based Android phone with Android 9 or later and 4 GB of free storage, or a development machine that can run an Arm64 Android emulator
    - A USB data cable when using a physical phone
    - A Java 17 or later JDK
    - Git installed and available in your `PATH`
    - Python 3 with `venv` and `pip` support
    - On macOS or Linux, `curl` and `unzip` installed and available in your `PATH`
    - A Hugging Face account with access to the model repositories

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-20T21:13:58Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 7db80d42457da5ab791f2818cf3eb35c53cc62169f712a62cd5d681925f82013
  summary_generated_at: '2026-08-20T21:13:58Z'
  summary_source_hash: 7db80d42457da5ab791f2818cf3eb35c53cc62169f712a62cd5d681925f82013
  faq_generated_at: '2026-08-20T21:13:58Z'
  faq_source_hash: 7db80d42457da5ab791f2818cf3eb35c53cc62169f712a62cd5d681925f82013
  summary: >-
    You'll run an Arm-optimized TinySD text-to-image model locally on an Arm64 Android
    phone with ExecuTorch and XNNPACK. You'll install and verify the Android command-line
    tools, build TinySD Studio, and download and import the TinySD INT8 package. Then,
    you'll generate and save a 512 x 512 image and compare another seed. You'll also
    trace the adapter, package importer, tokenizer, denoising loop, and image decoder,
    then choose an executable route for another model package.
  faqs:
  - question: Which model repository ID should I use?
    answer: >-
      Set `MODEL_ID` to `Arm/tiny-sd-int8-xnnpack-executorch-vivo-x300`, the Hugging Face repository for this application. Use the same value when you run the model downloader.
  - question: How do I check whether Android SDK Platform 35 is installed?
    answer: >-
      On macOS or Linux, run `test -d "$ANDROID_HOME/platforms/android-35"`. In Windows
      PowerShell, run `Test-Path "$env:ANDROID_HOME\platforms\android-35"`. The PowerShell
      check returns `True` when the platform directory exists.
  - question: Can I use an emulator instead of a physical phone?
    answer: >-
      You can use either a physical Arm64 Android phone or an Arm64 AVD. Use an
      emulator on a development computer with at least 16 GB of host memory, or use a physical
      phone with at least 7 GB of RAM.
  - question: What should I see after I generate an image?
    answer: >-
      The application tokenizes your prompt locally, reports progress through 25 denoising steps, and then
      displays a 512 x 512 image and the elapsed time. Select **Save image** to export the result as a PNG.
  - question: Where does the application tokenize the prompt and execute the model?
    answer: >-
      `TinySdImageGenerationAdapter.java` connects the shared application interface to
      `ClipTokenizer.java`, `ModelImporter.java`, and `TinySdRunner.java`. The tokenizer
      produces 77 CLIP token IDs, and the runner calls the ExecuTorch text encoder, UNet,
      and VAE decoder. `ScheduleData.java` loads the DPM-Solver++ values.
# END generated_summary_faq

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false


author:
- Kwashie Andoh
- Matt Cossins

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
    - Generative AI
    - Arm AI Portal
operatingsystems:
    - Android

further_reading:
    - resource:
        title: ExecuTorch for Android
        link: https://docs.pytorch.org/executorch/stable/using-executorch-android.html
        type: documentation
    - resource:
        title: ExecuTorch XNNPACK backend
        link: https://docs.pytorch.org/executorch/stable/backends-xnnpack.html
        type: documentation
    - resource:
        title: Create and manage Android virtual devices
        link: https://developer.android.com/studio/run/managing-avds
        type: documentation
    - resource:
        title: TinySD model card
        link: https://huggingface.co/Arm/tiny-sd-int8-xnnpack-executorch-vivo-x300
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---
