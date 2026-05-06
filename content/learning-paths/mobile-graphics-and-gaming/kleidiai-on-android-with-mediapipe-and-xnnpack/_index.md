---
title: Run LLM inference on Android with KleidiAI, MediaPipe, and XNNPACK
description: Learn how to run LLM inference on Android devices using MediaPipe with KleidiAI-enhanced Arm i8mm features to benchmark the Gemma 2B model.

minutes_to_complete: 60

who_is_this_for: This is an advanced topic for Android developers who want to efficiently run LLMs on-device.

learning_objectives:
    - Install the prerequisites for cross-compiling new inference engines for Android.
    - Run LLM inference on an Android device with the Gemma 2B model using the Google AI Edge's MediaPipe framework.
    - Benchmark LLM inference speed with and without the KleidiAI-enhanced Arm i8mm processor feature.

prerequisites:
    - An x86_64 Linux machine running Ubuntu with approximately 500 MB of free space, or a docker daemon that can build and run a provided x86_64 Dockerfile.
    - An Android phone with support for i8mm (tested on Google Pixel 8 Pro).

generate_summary_faq: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-05-06T17:17:56Z'
  generator: template
  source_hash: 0e51db9ceb25c31c42608f3c6744a4fa8f9d995805ed44a7d7fc83324889ea12
  summary: >-
    Learn how to run LLM inference on Android devices using MediaPipe with KleidiAI-enhanced Arm
    i8mm features to benchmark the Gemma 2B model. It is designed for Android developers who want
    to efficiently run LLMs on-device. By the end, you will be able to install the prerequisites
    for cross-compiling new inference engines for Android, run LLM inference on an Android device
    with the Gemma 2B model using the Google AI Edge's MediaPipe framework, and benchmark LLM
    inference speed with and without the KleidiAI-enhanced Arm i8mm processor feature. It focuses
    on tools and technologies such as Java, MediaPipe, Android SDK, Android NDK, and Bazel, Linux
    environments, and Arm platforms including Cortex-A. The main steps cover Install dependencies,
    Run the Gemma 2B model using MediaPipe with XNNPACK, and Benchmark the Gemma 2B Model with
    KleidiAI.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will install the prerequisites for cross-compiling new inference engines for Android,
      run LLM inference on an Android device with the Gemma 2B model using the Google AI Edge's
      MediaPipe framework, and benchmark LLM inference speed with and without the KleidiAI-enhanced
      Arm i8mm processor feature. Learn how to run LLM inference on Android devices using MediaPipe
      with KleidiAI-enhanced Arm i8mm features to benchmark the Gemma 2B model.
  - question: Who is this Learning Path for?
    answer: >-
      This is an advanced topic for Android developers who want to efficiently run LLMs on-device.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: An x86_64 Linux machine running Ubuntu
      with approximately 500 MB of free space, or a docker daemon that can build and run a provided
      x86_64 Dockerfile.; An Android phone with support for i8mm (tested on Google Pixel 8 Pro).
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including Java, MediaPipe, Android SDK, Android NDK, and Bazel,
      Linux environments, and Arm platforms such as Cortex-A.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Install dependencies, Run the Gemma 2B model using
      MediaPipe with XNNPACK, and Benchmark the Gemma 2B Model with KleidiAI.
# END generated_summary_faq

author: 
    - Pareena Verma
    - Joe Stech
    - Adnan AlSinan

### Tags
skilllevels: Advanced
subjects: ML
armips:
    - Cortex-A
tools_software_languages:
    - Java
    - MediaPipe
    - Android SDK
    - Android NDK
    - Bazel
    - XNNPACK
    - Hugging Face

operatingsystems:
    - Linux


further_reading:
    - resource:
        title: MediaPipe Solutions Guide 
        link: https://ai.google.dev/edge/mediapipe/solutions/guide
        type: documentation
    - resource:
        title: Accelerating AI Developer Innovation Everywhere with New Arm Kleidi
        link: https://newsroom.arm.com/blog/arm-kleidi
        type: blog
    - resource:
        title: Faster Dynamically Quantized Inference with XNNPack 
        link: https://blog.tensorflow.org/2024/04/faster-dynamically-quantized-inference-with-xnnpack.html
        type: blog



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

