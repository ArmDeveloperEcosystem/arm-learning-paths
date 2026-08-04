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
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-04T22:15:51Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 79f888973a2466f22aa83ee29469442d7b89fbed17e28984e256897115863dd0
  summary_generated_at: '2026-08-04T22:15:51Z'
  summary_source_hash: 79f888973a2466f22aa83ee29469442d7b89fbed17e28984e256897115863dd0
  faq_generated_at: '2026-08-04T22:15:51Z'
  faq_source_hash: 79f888973a2466f22aa83ee29469442d7b89fbed17e28984e256897115863dd0
  summary: >-
    You build ONNX Runtime and the generate() API for Android,
    then deploying a Phi-3-mini model on an Arm-based smartphone. You configure a Windows development
    environment, cross-compile ONNX Runtime for Android CPU with the Android NDK, and build the
    generate() API to enable the text generation loop. You then compile and run a model runner
    on the device to produce generated text and view performance metrics. Finally, you build an
    Android chat application from the onnxruntime-inference-examples repository at a pinned commit
    in Android Studio to demonstrate local inference and verify end-to-end functionality.
  faqs:
  - question: What should I check if CMake cannot find the Android toolchain?
    answer: >-
      Confirm that CMAKE_TOOLCHAIN_FILE points to the Android NDK toolchain file under the expected
      NDK version (27.3.13750724) in your Android SDK directory. Ensure the path matches the one
      used in the steps.
  - question: How do I know the ONNX Runtime and Generate() API builds for Android succeeded?
    answer: >-
      The build finishes without errors and produces cross-compiled libraries and example binaries
      in the build output directories. You should be able to proceed to run the model runner on
      the device in the next step.
  - question: Which model variant is used for the benchmark, and how can I validate it runs?
    answer: >-
      The steps use the Phi-3-mini model. A successful run shows the model loading, generated
      text output, and performance metrics on the console.
  - question: Should I use the latest onnxruntime-inference-examples for the chat app?
    answer: >-
      Use commit 7a635daae48450ff142e5c0848a564b245f04112 as shown. Later commits are not tested
      in this Learning Path.
  - question: What should I expect when running the Android chat app from Android Studio?
    answer: >-
      The app installs on the connected device and opens a chat interface. You can enter prompts
      and observe locally generated responses to confirm end-to-end inference.
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
