---
title: Build an Android chat application with ONNX Runtime API
description: Learn how to build ONNX Runtime and the generate() API for Android to run a Phi-3 model on Arm-based smartphones.


minutes_to_complete: 60

who_is_this_for: This is an advanced topic for software developers interested in learning how to build an Android chat app with ONNX Runtime and ONNX Runtime Generate() API.

learning_objectives: 
    - Build ONNX Runtime and ONNX Runtime generate() API for Android.
    - Run a Phi-3 model using ONNX Runtime on an Arm-based smartphone.

prerequisites:
    - A Windows x86_64 development machine with at least 16GB of RAM.
    - An Android phone with at least 8GB of RAM. This learning path was tested on Samsung Galaxy S24.

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T23:48:15Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: deeb745d72457138cb81252c421205cd8dfb43b5e29ceee3a15c5842cc90cc33
  summary_generated_at: '2026-06-02T02:45:40Z'
  summary_source_hash: deeb745d72457138cb81252c421205cd8dfb43b5e29ceee3a15c5842cc90cc33
  faq_generated_at: '2026-06-02T23:48:15Z'
  faq_source_hash: deeb745d72457138cb81252c421205cd8dfb43b5e29ceee3a15c5842cc90cc33
  summary: >-
    This advanced Learning Path guides you through cross-compiling ONNX Runtime and its generate()
    API for Android on a Windows x86_64 host, then running a Phi-3 model on an Arm-based (Cortex-A)
    smartphone. You will set up Android Studio, the Android NDK (tested with 27.3.13750724), Python
    3.13, CMake 4.1.0, and Ninja 1.12.1; build ONNX Runtime and the onnxruntime-genai Generate()
    API; prepare and run a Phi-3-mini model; and view performance metrics using a command-line
    model runner. You will also build and run a Kotlin-based Android chat demo from the onnxruntime-inference-examples
    repository. Prerequisites include a Windows machine with at least 16GB RAM and an Android
    phone with at least 8GB RAM (tested on Samsung Galaxy S24).
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need a Windows x86_64 development machine with at least 16GB of RAM and an Android phone
      with at least 8GB of RAM. This path was tested on a Samsung Galaxy S24. The operating systems
      used are Windows and Android.
  - question: Which software versions should I install for the build environment?
    answer: >-
      Install Android Studio (latest recommended), Android NDK tested with version 27.3.13750724,
      Python 3.13, CMake tested with version 4.1.0, and Ninja tested with version 1.12.1. These
      versions are referenced in the steps.
  - question: What is the build target for ONNX Runtime and the generate() API?
    answer: >-
      You cross-compile ONNX Runtime and the generate() API for Android CPU. The steps use the
      Android NDK toolchain during the build.
  - question: Where should the CMake toolchain file point when building the model runner?
    answer: >-
      Set -DCMAKE_TOOLCHAIN_FILE to the android.toolchain.cmake file inside your installed Android
      NDK. The example path in the steps references NDK 27.3.13750724 under the Android SDK; update
      it to match your local installation.
  - question: What result should I expect when running the benchmark on the phone?
    answer: >-
      The benchmark prepares and runs a Phi-3-mini model on your Android device. You should be
      able to view performance metrics produced by the model runner.
# END generated_summary_faq

author: Koki Mitsunami

### Tags
skilllevels: Advanced
subjects: ML
armips:
    - Cortex-A
tools_software_languages:
    - Kotlin
    - CPP
    - ONNX Runtime
    - Android
    - Hugging Face

operatingsystems:
    - Windows
    - Android


further_reading:
    - resource:
        title: ONNX Runtime
        link: https://onnxruntime.ai/docs/
        type: documentation
    - resource:
        title: ONNX Runtime generate() API
        link: https://onnxruntime.ai/docs/genai/
        type: documentation
    - resource:
        title: Accelerating AI Developer Innovation Everywhere with New Arm Kleidi
        link: https://newsroom.arm.com/blog/arm-kleidi
        type: blog



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

