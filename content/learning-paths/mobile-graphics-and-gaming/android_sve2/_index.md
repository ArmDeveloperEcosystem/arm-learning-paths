---
title: Get started with Scalable Vector Extension 2 (SVE2) on Android
minutes_to_complete: 40

who_is_this_for: This is an introductory topic for software developers interested in learning how to use the Scalable Vector Extension 2 (SVE2) on Arm powered mobile devices running Android. 

learning_objectives:
    - Enable Scalable Vector Extension 2 (SVE2) support in Android Studio.
    - Implement an Android application that uses the Android Native Development Kit (NDK) to calculate the fused multiply-add (FMA).
    - Measure the performance uplift by using SVE2 intrinsics.

prerequisites:
    - A x86_64 or Apple development machine with Android Studio installed.
    - A 64-bit Arm powered smartphone running Android.
    - Knowledge of Single instruction Multi Data (SIMD)
    - Knowledge of [Neon](https://developer.arm.com/documentation/102474/latest)
    - Knowledge of [Scalable Vector Extension (SVE)](https://developer.arm.com/documentation/101726/4-0)

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T23:46:40Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: be91053c5abcdd669ff8da7e66b2f717c4adaac27b3fb44ea073b69a68d2dba7
  summary_generated_at: '2026-06-02T02:44:16Z'
  summary_source_hash: be91053c5abcdd669ff8da7e66b2f717c4adaac27b3fb44ea073b69a68d2dba7
  faq_generated_at: '2026-06-02T23:46:40Z'
  faq_source_hash: be91053c5abcdd669ff8da7e66b2f717c4adaac27b3fb44ea073b69a68d2dba7
  summary: >-
    This Learning Path guides you through enabling Scalable Vector Extension 2 (SVE2) in Android
    Studio and implementing a native Android NDK example that computes vector fused multiply-add
    (a * b + c) using SVE2 intrinsics. You will write C++ code to generate pseudo-random input
    data, add helper functions, and create a reusable measureExecutionTime template to time N
    invocations of FMA implementations with and without SVE2 on a 64-bit Arm smartphone running
    Android. The introduction places SVE2 in the context of the ARMv9-A architecture. Prerequisites
    include Android Studio on an x86_64 or Apple development machine, a 64-bit Arm Android device,
    and familiarity with SIMD, Neon, and SVE. The expected outcome is a working project that builds,
    runs, and compares execution times.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need Android Studio installed on an x86_64 or Apple development machine and access to
      a 64-bit Arm smartphone running Android. Prior knowledge of SIMD, Neon, and SVE is expected.
  - question: How do I enable SVE2 support in Android Studio for this project?
    answer: >-
      Follow the step titled “Enable SVE2 support in Android Studio” to configure the project
      so SVE2 intrinsics compile for your NDK code. The path guides you through the necessary
      project changes to build and run on a 64-bit Arm device.
  - question: Which source file do I modify to add the FMA and timing code?
    answer: >-
      You will modify native-lib.cpp located under app/cpp/. This file is updated to implement
      the FMA routines and the measureExecutionTime template function.
  - question: How is performance measured, and what result should I expect to see?
    answer: >-
      A measureExecutionTime template function runs N invocations of the FMA implementations with
      and without SVE2 intrinsics and returns their execution times. You should see timing results
      that let you compare the two paths; specific numbers are not provided.
  - question: Can I complete this path without a physical Arm-based Android device?
    answer: >-
      A 64-bit Arm-powered smartphone running Android is listed as a prerequisite. The path does
      not list an emulator or non-Arm alternative.
# END generated_summary_faq

author: Dawid Borycki

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
armips:
    - Cortex-A
operatingsystems:
    - Android
tools_software_languages:
    - Android Studio

further_reading:
    - resource:
        title: Learn the architecture - Introducing SVE2 guide 
        link: https://developer.arm.com/documentation/102340/0100
        type: documentation
    - resource:
        title: Exploring the SVE intrinsics
        link: https://developer.arm.com/documentation/102699/0100/Optimizing-with-intrinsics
        type: documentation
    - resource:
        title: Kotlin Programming Language
        link: https://kotlinlang.org
        type: website
    - resource:
        title: Android Studio
        link: https://developer.android.com/studio
        type: website




### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

