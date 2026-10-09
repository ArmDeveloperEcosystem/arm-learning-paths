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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-21T17:27:58Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 8dbebdcfaec46e10b63f8045e1eb45cefdd1aaa080c78b740a339bae8fabeb1f
  summary_generated_at: '2026-08-21T17:27:58Z'
  summary_source_hash: 8dbebdcfaec46e10b63f8045e1eb45cefdd1aaa080c78b740a339bae8fabeb1f
  faq_generated_at: '2026-08-21T17:27:58Z'
  faq_source_hash: 8dbebdcfaec46e10b63f8045e1eb45cefdd1aaa080c78b740a339bae8fabeb1f
  summary: >-
    You'll convert Stable Audio Open Small to LiteRT (`.tflite`) and run its audio-generation application
    on Android or macOS Arm devices. First, you'll prepare the workspace, download the model files, and
    convert its Conditioners, DiT, and AutoEncoder submodules. Then, you'll build LiteRT and FlatBuffers,
    compile the application for your chosen platform, run it with a text prompt, and retrieve the
    generated `output.wav` file.
  faqs:
  - question: How do I know the model download is complete before conversion?
    answer: >-
      Verify that `model_config.json` and `model.ckpt` are in your workspace directory. Run the
      listed `ls` command before you start conversion.
  - question: Where do I run CMake to build the Android app?
    answer: >-
      From your workspace, navigate to `ML-examples/kleidiai-examples/audiogen/app` and create a
      build directory. Run CMake from that build directory.
  - question: Which Android ABI should I use for Arm targets?
    answer: >-
      Set `ANDROID_ABI=arm64-v8a` in the CMake command for the Android build.
  - question: What paths do I pass to CMake after building LiteRT?
    answer: >-
      Build LiteRT and FlatBuffers, then configure CMake with `TF_INCLUDE_PATH`, `TF_LIB_PATH`, and
      `FLATBUFFER_INCLUDE_PATH`.
  - question: What result should I expect when running the program on the device?
    answer: >-
      Run `audiogen` on the device with a text prompt. After inference, pull
      `/data/local/tmp/app/output.wav` to your host machine.
# END generated_summary_faq

author:
    - Nina Drozd
    - Annie Tallund
    - Gian Marco Iodice
    - Adnan AlSinan
    - Aude Vuilliomenet

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
