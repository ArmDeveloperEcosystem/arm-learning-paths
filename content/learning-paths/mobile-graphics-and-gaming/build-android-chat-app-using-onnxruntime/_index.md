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

# START generated_summary_faq

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-05T14:56:16Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 79f888973a2466f22aa83ee29469442d7b89fbed17e28984e256897115863dd0
  summary_generated_at: '2026-08-05T14:56:16Z'
  summary_source_hash: 79f888973a2466f22aa83ee29469442d7b89fbed17e28984e256897115863dd0
  faq_generated_at: '2026-08-05T14:56:16Z'
  faq_source_hash: 79f888973a2466f22aa83ee29469442d7b89fbed17e28984e256897115863dd0
  summary: >-
    You'll build ONNX Runtime and its `generate()` API for Android on a Windows host, then deploy a
    Phi-3 model to an Arm-based smartphone. First, you'll configure the Android NDK, cross-compile the runtime
    and text-generation components, and build a C model runner with CMake and Ninja. Then, you'll launch
    the Android demo app in Android Studio to validate on-device inference.
  faqs:
  - question: How do I point CMake to the correct Android NDK for these builds?
    answer: >-
      Use the `CMAKE_TOOLCHAIN_FILE` option with the `android.toolchain.cmake` path from the installed
      NDK. Ensure the path and version match the NDK you installed.
  - question: Which header files do I need to copy before configuring the C model runner?
    answer: >-
      Copy `src\ort_genai.h` and `src\ort_genai_c.h` into `examples\c\include`. If these headers
      are missing, the model runner configuration will fail with include errors.
  - question: How do I know ONNX Runtime and the generate() API built successfully?
    answer: >-
      The build is successful when the configure and build stages complete without errors and
      produce Android-targeted binaries and headers. You should then be able to configure and build
      the `examples\c` model runner without missing include or link errors.
  - question: What result should I expect when I run the Phi-3-mini benchmark on my phone?
    answer: >-
      The run executes on the Android device and prints performance metrics. Proceed when the
      metrics appear and the process exits cleanly without runtime errors.
  - question: Which commit of the demo app repository should I check out in Android Studio?
    answer: >-
      Check out commit `7a635daae48450ff142e5c0848a564b245f04112`.
      You might be able to use a later commit, but the Learning Path was tested with that specific commit.
# END generated_summary_faq

author: Koki Mitsunami

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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
