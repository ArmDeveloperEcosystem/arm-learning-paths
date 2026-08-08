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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-05T14:53:49Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 69daa146ea3c1f903af1c958894eaee33af8690870274c96427f4d411403bcea
  summary_generated_at: '2026-08-05T14:53:49Z'
  summary_source_hash: 69daa146ea3c1f903af1c958894eaee33af8690870274c96427f4d411403bcea
  faq_generated_at: '2026-08-05T14:53:49Z'
  faq_source_hash: 69daa146ea3c1f903af1c958894eaee33af8690870274c96427f4d411403bcea
  summary: >-
    You'll build an OpenCV-based Android app and enable KleidiCV to accelerate image processing. First, you'll
    configure the project, add an input image, and define a UI for results. Then, you'll implement a modular
    pipeline with `ImageOperation`, `ImageProcessor`, and `PerformanceMetrics`. You'll run operations such
    as blur, resize, or rotate, and inspect the processed image and performance statistics.
  faqs:
  - question: How do I know OpenCV and KleidiCV are correctly added to the project?
    answer: >-
      Build and run the app on your Android device. If image operations execute without errors
      and the UI shows updated output with performance metrics, the libraries are integrated.
  - question: Where do I put the input image, and what file types work?
    answer: >-
      Place the image under `src/main/assets` and name it `img.png`. Any kind of image file can be
      used; the app converts it to the required type during processing.
  - question: What should I check if the image doesn’t load in the app?
    answer: >-
      Confirm the assets folder path is `src/main/assets` and the file name matches `img.png` exactly,
      including case. Use the **Project** view in Android Studio to verify the location, then rebuild.
  - question: Which file do I edit for the UI, and what should I see after running?
    answer: >-
      Edit `app/src/main/res/layout/activity_main.xml`. When you run the app, you should see the
      defined layout, processed image, and performance metrics.
  - question: How can I switch or add image operations?
    answer: >-
      Select a different entry from the `ImageOperation` enum to apply another operation. To extend
      functionality, add a new enum value with its implementation and have `ImageProcessor` apply
      it.
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
