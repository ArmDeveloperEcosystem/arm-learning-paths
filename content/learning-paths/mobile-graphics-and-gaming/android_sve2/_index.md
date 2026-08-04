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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-04T22:14:29Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 975e643e02da19a2aca65d87bee7bf08b37dbab6b47d79280b656fae3f6988d3
  summary_generated_at: '2026-08-04T22:14:29Z'
  summary_source_hash: 975e643e02da19a2aca65d87bee7bf08b37dbab6b47d79280b656fae3f6988d3
  faq_generated_at: '2026-08-04T22:14:29Z'
  faq_source_hash: 975e643e02da19a2aca65d87bee7bf08b37dbab6b47d79280b656fae3f6988d3
  summary: >-
    You enable Scalable Vector Extension 2 (SVE2) support
    in Android Studio, implementing a native fused multiply-add (FMA) operation with the Android
    NDK, and comparing it with a non-SVE2 version. You modify native-lib.cpp under app/cpp/
    to generate pseudo-random vectors using the C++ <random> library and add a measureExecutionTime
    template that records the runtime of N invocations for both implementations. After building
    and deploying to a 64-bit Arm Android device, you run both code paths and compare the measured
    execution times to observe the effect of using SVE2 intrinsics for vectorized computation.
  faqs:
  - question: How do I know SVE2 support is enabled correctly in my Android Studio project?
    answer: >-
      The project builds without errors when using SVE2 intrinsics and deploys to a 64-bit Arm
      Android device. You should be able to run both the SVE2 and non-SVE2 code paths and obtain
      timing results for each.
  - question: Which source file should I modify to add the helper functions and FMA implementations?
    answer: >-
      Edit native-lib.cpp located under app/cpp/. This file hosts the helper code, FMA routines,
      and the timing utility.
  - question: What output should I expect when I run the timing code?
    answer: >-
      You obtain execution times from measureExecutionTime for N invocations of the non-SVE2 and
      SVE2 implementations. Use these numbers to compare the two paths.
  - question: What should I check if SVE2 intrinsics fail to compile?
    answer: >-
      Verify that SVE2 support is enabled in Android Studio as described earlier and that you
      are building for a 64-bit Arm target device. Rebuild after confirming the configuration.
  - question: How do I validate that the SVE2 and non-SVE2 FMA results are correct?
    answer: >-
      Run both implementations on the same input vectors and compare their outputs. The results
      should match numerically for the same inputs.
# END generated_summary_faq

author: Dawid Borycki

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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
