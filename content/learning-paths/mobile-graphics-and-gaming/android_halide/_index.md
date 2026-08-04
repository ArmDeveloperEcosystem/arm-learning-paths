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
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-04T22:12:17Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 017e858b14ffeda855a6d41380d5d2e0d37a3e5cbbfb9013e3ad4bf2d71c0ca5
  summary_generated_at: '2026-08-04T22:12:17Z'
  summary_source_hash: 017e858b14ffeda855a6d41380d5d2e0d37a3e5cbbfb9013e3ad4bf2d71c0ca5
  faq_generated_at: '2026-08-04T22:12:17Z'
  faq_source_hash: 017e858b14ffeda855a6d41380d5d2e0d37a3e5cbbfb9013e3ad4bf2d71c0ca5
  summary: >-
    You build and integrate a real-time image processing
    pipeline with Halide on Android. You install and configure Halide, prototype a camera workflow
    that applies Gaussian blur followed by thresholding using OpenCV, and experiment with scheduling
    options such as parallelization and tiling. You then apply operator fusion and compare it
    with materializing intermediates using compute_root() and compute_at(), using print_loop_nest()
    to inspect how Halide arranges computation. Next, you generate an ahead-of-time cross-compiled
    pipeline library on the host for an Android ABI such as arm64-v8a, avoiding device-side builds
    and JIT. Finally, you integrate the resulting library into an Android application written
    in Kotlin.
  faqs:
  - question: How do I know I’ve set up Halide correctly before building the pipeline?
    answer: >-
      Compile and run a small pipeline that processes camera frames with blur and thresholding.
      If it builds without errors and you see processed frames update in real time, the setup
      is working.
  - question: Which scheduling options should I try first, and how do I compare results?
    answer: >-
      Start by applying parallelization and tiling as shown in the steps. Compare their impact
      by measuring how quickly frames are processed and whether the output remains correct.
  - question: When should I fuse stages and when should I materialize intermediates?
    answer: >-
      Prefer fusion to reduce memory traffic when intermediates are not reused. Materialize with
      compute_root() or compute_at() for large filters or when an intermediate result is consumed
      by multiple stages.
  - question: How do I check that my schedule actually fuses stages?
    answer: >-
      Use print_loop_nest() to inspect the generated loop structure. If producers are computed
      inside their consumers as intended, the output will reflect fused execution.
  - question: What output should I expect from AOT cross-compilation, and which Android ABI should
      I target?
    answer: >-
      Expect a native pipeline library built on the host for Android. Choose an ABI that matches
      your device or emulator, for example arm64-v8a, and then integrate the library into your
      Kotlin app.
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
