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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-17T22:05:45Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: d2559b0bde2b716640df74ca831be6736a77417de5ce0e641f1e43a267e8f58b
  summary_generated_at: '2026-08-17T22:05:45Z'
  summary_source_hash: d2559b0bde2b716640df74ca831be6736a77417de5ce0e641f1e43a267e8f58b
  faq_generated_at: '2026-08-17T22:05:45Z'
  faq_source_hash: d2559b0bde2b716640df74ca831be6736a77417de5ce0e641f1e43a267e8f58b
  summary: >-
    You'll cross-compile MediaPipe with XNNPACK for Android `arm64` and run Gemma 2B on an i8mm-capable
    device. First, you'll build and verify the binary with Bazel, then run inference. After running inference, you'll create a second build without
    i8mm and benchmark both variants to assess the effect of KleidiAI integration on supported Android
    hardware.
  faqs:
  - question: Which installation option should I choose for dependencies?
    answer: >-
      Use the Docker option if you have a working Docker daemon and prefer an isolated, reproducible
      environment. Choose the native Ubuntu option if you want to install dependencies directly
      on your `x86_64` Linux host.
  - question: How do I confirm the Bazel build created the Android CPU inference binary?
    answer: >-
      List the Bazel output directory. You should see `llm_inference_engine_cpu_main`
      under `bazel-bin/mediapipe/tasks/cc/genai/inference/c/`.
  - question: Which Bazel options enable the i8mm path with KleidiAI for Android arm64?
    answer: >-
      Build the target `mediapipe/tasks/cc/genai/inference/c:llm_inference_engine_cpu_main` with
      `--config=android_arm64` and `--define=xnn_enable_arm_i8mm=true`. These options select the Android
      `arm64` build and enable the i8mm path integrated through XNNPACK.
  - question: How do I build a comparison binary without i8mm?
    answer: >-
      Re-run the same Bazel build for the target but omit `--define=xnn_enable_arm_i8mm=true`. Use
      the two binaries with and without the flag for the benchmarking step.
  - question: What result should I expect from the benchmark runs?
    answer: >-
      You should obtain measurements for both builds to compare the effect of enabling i8mm and
      KleidiAI. Differences between the runs indicate the impact of the i8mm-enabled path on your
      device.
# END generated_summary_faq

author: 
    - Pareena Verma
    - Joe Stech
    - Adnan AlSinan

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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
