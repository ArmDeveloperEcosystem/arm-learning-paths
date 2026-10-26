---
title: Get started with Scalable Vector Extension 2 on Android
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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-05T14:54:23Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 57714a67548fda35a8b2c7333b75148640ec07172a6f21ee64ca0ed4a4484f99
  summary_generated_at: '2026-08-05T14:54:23Z'
  summary_source_hash: 57714a67548fda35a8b2c7333b75148640ec07172a6f21ee64ca0ed4a4484f99
  faq_generated_at: '2026-08-05T14:54:23Z'
  faq_source_hash: 57714a67548fda35a8b2c7333b75148640ec07172a6f21ee64ca0ed4a4484f99
  summary: >-
    You'll enable SVE2 in an Android Studio project with the Android NDK,
    then implement and benchmark a fused multiply-add operation. First, you'll add native C++ helpers, create
    two FMA implementations, and time them on a 64-bit Arm Android device. Then, you'll compare the results
    to validate a minimal SVE2 example and measure its performance difference.
  faqs:
  - question: Where do I add the SVE2 intrinsics and helper code?
    answer: >-
      Edit `native-lib.cpp` under `app/cpp/`. Add the necessary includes, helper functions, both FMA
      implementations with and without SVE2, and the `measureExecutionTime` template in that file.
  - question: How do I know SVE2 support is enabled in Android Studio?
    answer: >-
      Your project should compile SVE2 intrinsics without errors and build successfully for your
      target. After you rebuild, run the app to execute both code paths and obtain timing results.
  - question: What result should I expect from the two fused multiply-add (FMA) implementations?
    answer: >-
      Both FMA implementations should return the same output. The FMA implementation with SVE2 should compute the result 3 to 4 times faster than the FMA without SVE2, depending on vector length.
  - question: How many iterations should I pass to `measureExecutionTime`?
    answer: >-
      Choose a value large enough to get stable timings on your device, then keep it the same
      for both implementations. The function returns a duration you can compare directly between
      the SVE2 and non-SVE2 runs.
  - question: What should I check if the project fails to build after enabling SVE2?
    answer: >-
      Verify you edited the correct source file and included the headers listed in the steps.
      Then, sync and rebuild the project to apply the configuration changes.
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
