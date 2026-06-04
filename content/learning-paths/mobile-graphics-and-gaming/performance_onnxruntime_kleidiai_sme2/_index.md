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

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T00:03:23Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 1645a1c65527da010edd6fefddad3c865eac0f9cad417ba59709a57bb9dc847a
  summary_generated_at: '2026-06-02T02:55:45Z'
  summary_source_hash: 1645a1c65527da010edd6fefddad3c865eac0f9cad417ba59709a57bb9dc847a
  faq_generated_at: '2026-06-03T00:03:23Z'
  faq_source_hash: 1645a1c65527da010edd6fefddad3c865eac0f9cad417ba59709a57bb9dc847a
  summary: >-
    This Learning Path shows how to build ONNX Runtime for Android with KleidiAI micro-kernels
    and Arm Scalable Matrix Extension 2 (SME2) support, then profile model performance to assess
    acceleration. You will cross-compile ONNX Runtime (v1.23.2) using the Android NDK (r26b or
    newer, with r27 recommended), CMake, and Ninja on a Linux environment, and run benchmarks
    on an Android device that supports SME2. Using onnxruntime_perf_test and a ResNet-50 v2 model,
    you will measure execution, see how MLAS dispatches to KleidiAI kernels when SME2 is detected,
    and compare standard versus SME2-optimized runs. Prerequisites include an SME2-capable Android
    device, basic ML inference knowledge, and familiarity with the Android NDK and cross-compilation.
  faqs:
  - question: What do I need before building ONNX Runtime for Android in this path?
    answer: >-
      Install the Android NDK r26b or newer (r27 recommended), and ensure CMake and Ninja are
      in your PATH. You also need an Android device with Arm SME2 support, plus familiarity with
      NDK cross-compilation and basic model inference.
  - question: Which ONNX Runtime version is used and how do I check it out?
    answer: >-
      This path uses ONNX Runtime v1.23.2. Clone the repository and checkout v1.23.2 as shown
      in the build step.
  - question: How does ONNX Runtime select KleidiAI SME2 kernels at runtime?
    answer: >-
      ORT’s MLAS checks CPU capabilities for SME2 and, when available, dispatches to KleidiAI
      micro-kernels. Examples include Conv and GEMM via ArmKleidiAI::MlasConv, ArmKleidiAI::MlasGemmBatch,
      and ArmKleidiAI::MlasDynamicQGemmBatch.
  - question: How do I prepare the example model on the device for profiling?
    answer: >-
      Download the ResNet-50 v2 package, push it to /data/local/tmp with adb, and extract it on
      the device in that directory. You then run profiling with onnxruntime_perf_test against
      the extracted model files.
  - question: What should I check if I don’t observe SME2-optimized execution?
    answer: >-
      Verify the Android device supports Arm SME2, because MLAS only dispatches to KleidiAI when
      SME2 is detected. Without SME2, ONNX Runtime uses its default kernels (for example, Neon),
      and SME2-focused comparisons will not apply.
# END generated_summary_faq

author: Zenon Zhilong Xiu

### Tags
skilllevels: Advanced
subjects: ML
armips:
    - Cortex-A
    - Arm C1
tools_software_languages:
    - C++
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

