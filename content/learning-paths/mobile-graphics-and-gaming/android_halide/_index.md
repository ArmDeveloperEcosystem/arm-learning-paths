---
title: Optimize image processing on Android using Halide
description: Learn how to build real-time image processing pipelines using Halide on Android, combining operations for improved performance in Kotlin applications.

minutes_to_complete: 180

who_is_this_for: This is an introductory topic for developers interested in learning how to use Halide for image processing. 

learning_objectives:
    - Learn the basics of Halide and set up your development environment
    - Build a simple real-time image processing pipeline with Halide
    - Make your image processing faster by combining operations in Halide
    - Use Halide pipelines in Android apps written with Kotlin

prerequisites:
    - Basic C++ knowledge
    - Android Studio with Android Emulator

# START generated_summary_faq

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-05T14:51:52Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 017e858b14ffeda855a6d41380d5d2e0d37a3e5cbbfb9013e3ad4bf2d71c0ca5
  summary_generated_at: '2026-08-05T14:51:52Z'
  summary_source_hash: 017e858b14ffeda855a6d41380d5d2e0d37a3e5cbbfb9013e3ad4bf2d71c0ca5
  faq_generated_at: '2026-08-05T14:51:52Z'
  faq_source_hash: 017e858b14ffeda855a6d41380d5d2e0d37a3e5cbbfb9013e3ad4bf2d71c0ca5
  summary: >-
    You'll build and integrate a Halide-based image processing pipeline on Android. You'll prototype
    Gaussian blur and thresholding, then use parallelization, tiling, and loop inspection to tune
    execution. After comparing fused stages with materialized intermediates, you'll generate a cross-compiled
    library for an Android ABI. You'll then integrate the library into a Kotlin app, and validate the
    processed frames on Android.
  faqs:
  - question: Which scheduling options should I try first to improve throughput?
    answer: >-
      Start with parallelization and tiling. Use `print_loop_nest()` to
      see how your schedule arranges loops and to verify changes behave as expected.
  - question: How do I choose between operator fusion and materializing intermediates?
    answer: >-
      Fuse stages to reduce memory traffic when results are used once and fit well in cache. Materialize
      with `compute_root()` or `compute_at()` for large filters or when an intermediate is reused
      by multiple consumers.
  - question: How do I confirm the cross-compiled pipeline targets the correct Android ABI?
    answer: >-
      Verify that the build uses the intended ABI, such as `arm64-v8a`, and ensure your Android
      project uses the same ABI. If the ABIs don’t match, your app might not load the pipeline
      library.
  - question: Do I need OpenCV in the Android app to follow the Learning Path?
    answer: >-
      No. OpenCV is used earlier to capture webcam frames for prototyping the pipeline on the
      host. You then call the compiled Halide pipeline from the Android app.
  - question: What should I check if the app fails to load the Halide pipeline library?
    answer: >-
      Check that the library was built for the same ABI as the app and that it's included in
      the Android project configuration. Also confirm the pipeline artifact from the AOT step
      is packaged with the app.
# END generated_summary_faq

author:
    - Éliás Bálint
    - Dawid Borycki
    - Steve Suzuki

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
armips:
    - Cortex-A
    - Cortex-X
operatingsystems:
    - Android
tools_software_languages:
    - Android Studio
    - Halide
    - CPP
    - Kotlin
    - Android Studio
    - CMake

further_reading:
    - resource:
        title: Halide documentation
        link: https://halide-lang.org/docs/index.html
        type: website
    - resource:
        title: Halide GitHub repository
        link: https://github.com/halide/Halide
        type: repository  
    - resource:
        title: Halide Tutorials
        link: https://halide-lang.org/tutorials/
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
