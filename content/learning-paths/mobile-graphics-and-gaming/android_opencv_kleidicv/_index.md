---
title: Accelerate an OpenCV-based Android Application with KleidiCV
description: Learn how to accelerate OpenCV-based Android applications using KleidiCV for enhanced computer vision performance.

minutes_to_complete: 45

who_is_this_for: This is an introductory topic for developers who are interested in creating Computer Vision applications with OpenCV and KleidiCV on Android Devices.

learning_objectives:
   - Describe what KleidiCV is, and what it can offer.
   - Create and configure a project to add OpenCV support.
   - Process images using OpenCV functionality.

prerequisites:
    - A development machine with [Android Studio](https://developer.android.com/studio) installed. 
    - Familiarity with Android development concepts.
    - An Android smartphone.

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-04T22:13:59Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 69daa146ea3c1f903af1c958894eaee33af8690870274c96427f4d411403bcea
  summary_generated_at: '2026-08-04T22:13:59Z'
  summary_source_hash: 69daa146ea3c1f903af1c958894eaee33af8690870274c96427f4d411403bcea
  faq_generated_at: '2026-08-04T22:13:59Z'
  faq_source_hash: 69daa146ea3c1f903af1c958894eaee33af8690870274c96427f4d411403bcea
  summary: >-
    You build an Android app that uses OpenCV with KleidiCV
    to accelerate common image processing tasks on Arm-based devices. You create a new Android
    Studio project, add OpenCV with KleidiCV support, and define a simple UI to load and process
    an image from assets. You use an ImageOperation enum for operations such as Gaussian blur,
    resizing, and rotation, an ImageProcessor that applies them to OpenCV Mat objects, and a
    PerformanceMetrics component that reports basic statistics. By the end,
    you run the app on a smartphone, switch operations, and observe the resulting processed
    images and metrics to validate that acceleration is wired into the OpenCV workflow.
  faqs:
  - question: Which Android Studio template should I start with?
    answer: >-
      Select Empty Views Activity in the New Project wizard. The example uses Android Studio Ladybug
      2024.2.1, Patch 3, though other versions are not explicitly listed.
  - question: Where do I place the input image and what should it be named?
    answer: >-
      Create an assets folder under src/main and add a file named img.png. The source content
      can be any image, as the app converts it during processing.
  - question: What should I check if the app cannot load the asset image?
    answer: >-
      Verify the folder path is exactly src/main/assets and the file name matches img.png. Rebuild
      the project after adding the asset to ensure Android Studio picks it up.
  - question: Which image operations are implemented in the example?
    answer: >-
      The ImageOperation enum includes operations such as Gaussian blur, resizing, and rotation.
      Refer to the enum definition in the code to see the full set available.
  - question: What result should I expect after applying an operation?
    answer: >-
      The app applies the selected ImageOperation to the asset image and displays the processed
      result. It also shows basic metrics from PerformanceMetrics so you can review the outcome.
# END generated_summary_faq

author: Dawid Borycki

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Graphics
armips:
    - Cortex-A
operatingsystems:
    - Android
tools_software_languages:
    - Android
    - Android Studio
    - Kotlin
    - Java

further_reading:
    - resource:
        title: OpenCV
        link: https://opencv.org
        type: documentation
    - resource:
        title: OpenCV on Android
        link: https://opencv.org/android/
        type: documentation
    - resource:
        title: KleidiCV
        link: https://gitlab.arm.com/kleidi/kleidicv
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
