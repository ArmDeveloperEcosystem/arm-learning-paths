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

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T23:55:26Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 0e51db9ceb25c31c42608f3c6744a4fa8f9d995805ed44a7d7fc83324889ea12
  summary_generated_at: '2026-06-02T02:50:53Z'
  summary_source_hash: 0e51db9ceb25c31c42608f3c6744a4fa8f9d995805ed44a7d7fc83324889ea12
  faq_generated_at: '2026-06-02T23:55:26Z'
  faq_source_hash: 0e51db9ceb25c31c42608f3c6744a4fa8f9d995805ed44a7d7fc83324889ea12
  summary: >-
    Learn to cross-compile and run LLM inference on Android using Google AI Edge’s MediaPipe with
    XNNPACK and KleidiAI-enhanced Arm i8mm. Starting from an x86_64 Ubuntu host (or a provided
    Docker setup), you install Android SDK/NDK and Bazel prerequisites, build a CPU inference
    engine, and run the Gemma 2B model on an Android device that supports i8mm (tested on Google
    Pixel 8 Pro). You then benchmark inference with the i8mm build flag enabled and disabled to
    compare performance. The path targets advanced Android developers and uses tools including
    MediaPipe, XNNPACK, Bazel, Android SDK/NDK, and Hugging Face. Expected outcomes are a working
    inference binary and benchmark results on your device.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need an x86_64 Linux machine running Ubuntu with about 500 MB free space or a Docker
      daemon to build and run the provided x86_64 Dockerfile, plus an Android phone that supports
      i8mm (tested on Google Pixel 8 Pro).
  - question: Should I install dependencies with Docker or directly on Ubuntu?
    answer: >-
      The path provides two options: build a Docker container with the dependencies or install
      them directly on an x86_64 Ubuntu machine. Choose Docker if you prefer a contained setup;
      use native installation if you already work on Ubuntu.
  - question: Which Bazel options target Android Arm64 and enable i8mm?
    answer: >-
      Use --config=android_arm64 to target Android Arm64 and --define=xnn_enable_arm_i8mm=true
      to enable i8mm. These flags are applied when building the inference tool.
  - question: How do I confirm the inference engine built correctly?
    answer: >-
      After the build completes, check for the binary in bazel-bin/mediapipe/tasks/cc/genai/inference/c/.
      The executable is named llm_inference_engine_cpu_main.
  - question: What result should I expect when running inference and benchmarking?
    answer: >-
      The inference tool runs an LLM on the Android device and produces output from an initial
      prompt. For benchmarking, you will cross-compile with and without the i8mm build flag to
      demonstrate performance differences using KleidiAI through XNNPACK.
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

