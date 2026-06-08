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

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T23:46:04Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 8e05fb124ad18194fba2ed83adae3e52673b2fad41af998ca8d0aa8cb9785f5e
  summary_generated_at: '2026-06-02T02:43:45Z'
  summary_source_hash: 8e05fb124ad18194fba2ed83adae3e52673b2fad41af998ca8d0aa8cb9785f5e
  faq_generated_at: '2026-06-02T23:46:04Z'
  faq_source_hash: 8e05fb124ad18194fba2ed83adae3e52673b2fad41af998ca8d0aa8cb9785f5e
  summary: >-
    This introductory Android Learning Path shows how to build an OpenCV-based app accelerated
    with KleidiCV. You will create a new Android Studio project, add OpenCV with KleidiCV support,
    define a simple UI, and implement image processing on an input image. The app uses an ImageOperation
    enum (for tasks such as Gaussian blur, resizing, and rotation), an ImageProcessor that works
    with OpenCV Mat objects, and a PerformanceMetrics class that reports statistics like average
    and standard deviation. The path targets Android development in Android Studio using Kotlin
    or Java. Prerequisites include Android Studio, familiarity with Android development concepts,
    and an Android smartphone. Estimated completion time is about 45 minutes.
  faqs:
  - question: What do I need before running through the steps?
    answer: >-
      You need a development machine with Android Studio installed, familiarity with Android development
      concepts, and an Android smartphone. No other prerequisites are explicitly listed.
  - question: Which Android Studio version is referenced in the example?
    answer: >-
      The example uses Android Studio Ladybug 2024.2.1, Patch 3. If you are using a different
      version, menu names or screens may vary slightly from the instructions.
  - question: Where should I place the test image, and does it have to be PNG?
    answer: >-
      Create an assets folder under src/main and add an img.png file there. The app will convert
      the image as needed, and any image file can be used; the Learning Path uses a cameraman
      image.
  - question: Which files do I edit to define the UI and application logic?
    answer: >-
      Replace the contents of app/src/main/res/layout/activity_main.xml to define the UI. For
      logic, create the ImageOperation enum, ImageProcessor class, and PerformanceMetrics class
      as outlined in the steps.
  - question: What result should I expect when I run the app on my device?
    answer: >-
      The app processes the bundled image using operations such as Gaussian blur, resizing, and
      rotation. It also displays performance metrics, including average and standard deviation,
      for the executed operations.
# END generated_summary_faq

author: Dawid Borycki

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

