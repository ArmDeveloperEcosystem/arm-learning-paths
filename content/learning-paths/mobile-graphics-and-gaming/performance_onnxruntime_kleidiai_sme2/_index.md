---
title: Profile ONNX model performance with SME2 using KleidiAI and ONNX Runtime
description: Learn how to build ONNX Runtime with KleidiAI and SME2 support for Android and profile ONNX model performance to compare acceleration improvements.

minutes_to_complete: 40

who_is_this_for: This is an advanced topic for software developers, performance engineers, and AI practitioners. 

learning_objectives: 
    - Build ONNX Runtime with KleidiAI and SME2 support for Android
    - Profile ONNX model performance using benchmark tools
    - Analyze how KleidiAI kernels accelerate ONNX operators with SME2
    - Compare performance improvements between standard and SME2-optimized execution

prerequisites:
    - An Android device with Arm SME2 support
    - Basic understanding of machine learning model inference
    - Familiarity with Android NDK and cross-compilation

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-17T22:13:41Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 2f249bc941318c8900cc74e846036643d5250a2dc0309228a5d839006c7bdb25
  summary_generated_at: '2026-08-17T22:13:41Z'
  summary_source_hash: 2f249bc941318c8900cc74e846036643d5250a2dc0309228a5d839006c7bdb25
  faq_generated_at: '2026-08-17T22:13:41Z'
  faq_source_hash: 2f249bc941318c8900cc74e846036643d5250a2dc0309228a5d839006c7bdb25
  summary: >-
    You'll build ONNX Runtime for Android with KleidiAI SME2 microkernels and profile a model on
    a device. First, you'll cross-compile with the Android NDK, deploy the binaries and model, and use
    `onnxruntime_perf_test` to capture baseline and SME2 results. Then, you'll compare KleidiAI dispatch,
    operator execution and end-to-end inference time with ResNet-50 v2.
  faqs:
  - question: How do I confirm that KleidiAI is used at runtime?
    answer: >-
      MLAS checks CPU capabilities at runtime and dispatches to KleidiAI when SME2 is present.
      When enabled, GEMM and convolution operators use ArmKleidiAI kernels instead of the default
      MLAS paths.
  - question: Which ONNX Runtime version should I use?
    answer: >-
      Use ONNX Runtime v1.23.2.
  - question: Which Android NDK version should I use for the build?
    answer: >-
      Use Android NDK r26b or later. NDK r27 or later is recommended for the latest SME2 toolchain
      support.
  - question: Where should I place the ResNet-50 v2 model files on the device?
    answer: >-
      Copy the archive to `/data/local/tmp` and extract it there. The example uses `adb` to push the
      file and `tar` to unpack it under that directory.
  - question: What should I check if SME2 acceleration doesn’t appear to be used?
    answer: >-
      Verify the Android device supports SME2, because MLAS enables KleidiAI only when SME2 is detected.
      If SME2 is unavailable, MLAS falls back to its default kernels (for example, Neon), and
      you can still profile that baseline.
# END generated_summary_faq

author: Zenon Zhilong Xiu

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
subjects: ML
armips:
    - Cortex-A
    - Arm C1
tools_software_languages:
    - CPP
    - ONNX Runtime
    - SME2
operatingsystems:
    - Android
    - Linux

further_reading:
    - resource:
        title: Arm Scalable Matrix Extension Introduction (Part 1)
        link: https://developer.arm.com/community/arm-community-blogs/b/architectures-and-processors-blog/posts/arm-scalable-matrix-extension-introduction
        type: blog
    - resource:
        title: Arm Scalable Matrix Extension Instructions (Part 2)
        link: https://developer.arm.com/community/arm-community-blogs/b/architectures-and-processors-blog/posts/arm-scalable-matrix-extension-introduction-p2
        type: blog
    - resource:
        title: Arm SME2 Introduction (Part 4)
        link: https://developer.arm.com/community/arm-community-blogs/b/architectures-and-processors-blog/posts/part4-arm-sme2-introduction
        type: blog

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
