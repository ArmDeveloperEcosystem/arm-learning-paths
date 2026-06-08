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

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T00:08:09Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 7970846a399ddcdb488d90bf19cce3c6b74df6348e88914aed83661b2597fe7b
  summary_generated_at: '2026-06-02T02:58:48Z'
  summary_source_hash: 7970846a399ddcdb488d90bf19cce3c6b74df6348e88914aed83661b2597fe7b
  faq_generated_at: '2026-06-03T00:08:09Z'
  faq_source_hash: 7970846a399ddcdb488d90bf19cce3c6b74df6348e88914aed83661b2597fe7b
  summary: >-
    This Learning Path shows how to download the Stable Audio Open Small model from Hugging Face,
    convert it to ExecuTorch (.pte), and build an audio generation application targeting Arm CPUs.
    You will set up a Python 3.10+ environment, install ExecuTorch 1.0.0, and build with CMake;
    Android builds use the Android NDK, and macOS (Apple Silicon) uses ExecuTorch with XNNPack
    and Arm KleidiAI. You will then run the application on an Android smartphone or macOS to generate
    short audio snippets. Prerequisites include a Linux-based x86 or macOS development machine
    with 8 GB RAM and 50 GB disk space, a Hugging Face account, and an Android phone in developer
    mode with at least 8 GB RAM and a cable; Android devices should have an Arm CPU with FEAT_DotProd
    (dotprod).
  faqs:
  - question: What do I need before running the conversion and build steps?
    answer: >-
      Use a Linux-based x86 or macOS development machine with at least 8 GB RAM and 50 GB of disk
      space, and sign in to a Hugging Face account. For Android, enable developer mode on a phone
      with at least 8 GB RAM and an Arm CPU that supports FEAT_DotProd; Python 3.10+ and CMake
      3.16+ are required, and the Android NDK is referenced (version not fully specified in the
      excerpt).
  - question: Which ExecuTorch installation option should I use?
    answer: >-
      You can install executorch==1.0.0 from PyPI, which is the simplest path. Alternatively,
      clone the ExecuTorch repository, check out v1.0.0, and run the provided installation script.
  - question: How should I set up the Python environment for conversion?
    answer: >-
      Create and activate a Python 3.10 virtual environment in the audiogen-et directory to isolate
      dependencies. Then install ExecuTorch before running the conversion step.
  - question: How do I know the model conversion to ExecuTorch succeeded?
    answer: >-
      The conversion produces a .pte file for Stable Audio Open Small. Proceed to the build steps
      once this file is created.
  - question: What should I check if the Android build or run fails?
    answer: >-
      Confirm you are targeting an Arm64 Android device with FEAT_DotProd and sufficient memory
      (8 GB recommended) and that developer mode is enabled. Ensure required tools like CMake
      and the Android NDK are installed, and follow the cross-compilation steps for Android.
# END generated_summary_faq

author:
    - Adnan AlSinan
    - Pareena Verma

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

