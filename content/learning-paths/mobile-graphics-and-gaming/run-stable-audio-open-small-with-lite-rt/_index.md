---
title: Generate audio with Stable Audio Open Small on LiteRT
description: Learn how to convert and deploy the Stable Audio Open Small text-to-audio model to LiteRT format for audio generation on Android devices and macOS.

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for developers looking to deploy the Stable Audio Open Small text-to-audio model using LiteRT on an Android™ device or on a reasonably modern platform with macOS®.

learning_objectives:
    - Download and test the Stable Audio Open Small model. 
    - Convert the Stable Audio Open Small model to the LiteRT (.tflite) format.
    - Compile the application for an Arm CPU.
    - Create a simple application that generates audio. 
    - Run the application on an Android smartphone and generate an audio snippet.

prerequisites:
    - A Linux-based x86 or macOS development machine with at least 8 GB of RAM and 50 GB of disk space (tested on Ubuntu 22.04 with x86_64).
    - A [HuggingFace](https://huggingface.co/) account.
    - An Android phone in [developer mode](https://developer.android.com/studio/debug/dev-options) and a cable to connect it to your development machine.

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T00:07:29Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 388cab0dcb284c29fe2ad82f2b2934d9243c6356b2885d26db0a97c1a1d4d393
  summary_generated_at: '2026-06-02T02:58:12Z'
  summary_source_hash: 388cab0dcb284c29fe2ad82f2b2934d9243c6356b2885d26db0a97c1a1d4d393
  faq_generated_at: '2026-06-03T00:07:29Z'
  faq_source_hash: 388cab0dcb284c29fe2ad82f2b2934d9243c6356b2885d26db0a97c1a1d4d393
  summary: >-
    This Learning Path shows how to take the Stable Audio Open Small text-to-audio model from
    Hugging Face, convert its submodules to LiteRT (.tflite), build LiteRT from the TensorFlow
    repository using Bazel, and compile a simple C++ application for Arm-based Android (arm64-v8a)
    with the Android NDK and CMake. You will run the app on an Android smartphone to generate
    an audio snippet from a text prompt. The path assumes a Linux-based x86 or macOS development
    machine, a Hugging Face account, and an Android device in developer mode with a USB cable.
    macOS is mentioned as a platform, but the provided steps focus on Android deployment.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need a Linux-based x86 or macOS development machine with at least 8 GB RAM and 50 GB
      of disk, a Hugging Face account, and an Android phone in developer mode with a USB cable.
      These are the only explicit prerequisites listed.
  - question: Which model files do I download from Hugging Face, and how do I verify them?
    answer: >-
      Download model_config.json and model.ckpt from the Stable Audio Open Small page and copy
      them into your workspace. Verify that both files exist in the workspace before proceeding.
  - question: Which tool versions are required for the environment setup?
    answer: >-
      Install Android NDK r27b or newer, Python 3.10 or newer (tested with 3.10), and CMake 3.16.0
      or newer (tested with 3.28.1). LiteRT is built using Bazel, but a specific Bazel version
      is not listed.
  - question: How are the model components converted to LiteRT format?
    answer: >-
      You will clone a repository that provides scripts to convert the model’s three submodules
      into LiteRT (.tflite) and generate the inference application. Follow the steps to run these
      scripts after downloading the model assets.
  - question: What result should I expect when running the Android app, and how do I configure
      the build?
    answer: >-
      Configure CMake with the Android NDK toolchain, set ANDROID_ABI=arm64-v8a, and pass the
      TensorFlow include and library paths. The app takes a text prompt and outputs an audio file;
      successful generation confirms the pipeline is working.
# END generated_summary_faq

author:
    - Nina Drozd
    - Gian Marco Iodice
    - Adnan AlSinan
    - Aude Vuilliomenet
    - Annie Tallund

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

operatingsystems:
    - Linux
    - Android

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
        title: Fast Text-to-Audio Generation with Adversarial Post-Training
        link: https://arxiv.org/abs/2505.08175
        type: website




### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

