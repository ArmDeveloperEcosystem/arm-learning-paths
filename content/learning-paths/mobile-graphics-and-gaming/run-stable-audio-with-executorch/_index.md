---
title: Generate audio with Stable Audio Open Small using ExecuTorch
description: Learn how to convert the Stable Audio Open Small model to ExecuTorch format and build an audio generation application for Android or macOS.
minutes_to_complete: 45

who_is_this_for: This is an introductory topic for developers who want to deploy the Stable Audio Open Small text-to-audio model using ExecuTorch on an Android device or macOS.

learning_objectives:
    - Download the Stable Audio Open Small model from Hugging Face
    - Convert the Stable Audio Open Small model to ExecuTorch (.pte) format
    - Build the audio generation application for Arm CPUs
    - Run the application on an Android smartphone or macOS and generate audio snippets

prerequisites:
    - A Linux-based x86 or macOS development machine with at least 8 GB of RAM and 50 GB of disk space (tested on Ubuntu 22.04 with x86_64 and macOS with Apple Silicon)
    - A [Hugging Face](https://huggingface.co/) account
    - An Android phone in [developer mode](https://developer.android.com/studio/debug/dev-options) with at least 8 GB of RAM and a cable to connect it to your development machine

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-21T17:28:51Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 193214d8cd0514c1ab05a6f8c93b4c01992f33529452e7bcd5c9910a32c79f29
  summary_generated_at: '2026-08-21T17:28:51Z'
  summary_source_hash: 193214d8cd0514c1ab05a6f8c93b4c01992f33529452e7bcd5c9910a32c79f29
  faq_generated_at: '2026-08-21T17:28:51Z'
  faq_source_hash: 193214d8cd0514c1ab05a6f8c93b4c01992f33529452e7bcd5c9910a32c79f29
  summary: >-
    You'll convert the Stable Audio Open Small text-to-audio model to ExecuTorch `.pte` files and run
    the audio-generation application on macOS or Android Arm devices. First, you'll set up Python and CMake,
    download the Hugging Face model files, and export its three submodules. Then, you'll build and
    run the app on Apple silicon or cross-compile it for Android, transfer the required files,
    and retrieve the generated WAV audio.
  faqs:
  - question: Which ExecuTorch installation option should I use?
    answer: >-
      Install `executorch==1.0.0` with `pip`. Alternatively, clone ExecuTorch, check out `v1.0.0`,
      and run `bash ./install_executorch.sh`.
  - question: How do I know the model conversion to ExecuTorch worked?
    answer: >-
      After conversion, verify that `conditioners_model.pte`, `dit_model.pte`, and
      `autoencoder_model.pte` exist in the `audiogen-et` directory.
  - question: When building on macOS, what environment assumptions apply?
    answer: >-
      Create a fresh Python 3.10 virtual environment for the macOS build. Use macOS on Apple silicon
      (Arm64).
  - question: What should I check before running on an Android device?
    answer: >-
      Use an Arm64 Android device with at least 8 GB of RAM. The prerequisites specify `FEAT_DotProd`
      support and optional `FEAT_I8MM` support. Confirm that `adb devices` detects your connected
      device before you transfer the files.
  - question: What result should I expect when I run the application?
    answer: >-
      When you run the app, it generates a short audio sample from your text prompt. On macOS,
      the `.wav` file is saved in the current directory. On Android, exit the `adb shell` and pull
      the output file from `/data/local/tmp/app`.
# END generated_summary_faq

author:
    - Adnan AlSinan
    - Pareena Verma

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
armips:
    - Cortex-A
    - Cortex-X

tools_software_languages:
    - CPP
    - Python
    - Hugging Face
    - ExecuTorch

operatingsystems:
    - Linux
    - Android
    - macOS

further_reading:
    - resource:
        title: Stability AI and Arm Collaborate to Release Stable Audio Open Small, Enabling Real-World Deployment for On-Device Audio Generation
        link: https://stability.ai/news/stability-ai-and-arm-release-stable-audio-open-small-enabling-real-world-deployment-for-on-device-audio-control
        type: blog
    - resource:
        title: "Unlocking audio generation on Arm CPUs to all: Running Stable Audio Open Small with KleidiAI"
        link: https://community.arm.com/arm-community-blogs/b/ai-blog/posts/audio-generation-arm-cpus-stable-audio-open-small-kleidiai
        type: blog
    - resource:
        title: ExecuTorch Documentation
        link: https://pytorch.org/executorch/stable/index.html
        type: documentation
    - resource:
        title: Arm KleidiAI Project
        link: https://gitlab.arm.com/kleidi/kleidiai
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
