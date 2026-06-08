---
title: Create Computer Vision Applications with OpenCV on Android Devices
description: Learn how to create and configure an Android project with OpenCV support to process camera images for computer vision applications.

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for developers who are interested in creating Computer Vision Applications with OpenCV on Android Devices.

learning_objectives:
   - Describe what OpenCV is, and what it can offer.
   - Create and configure a project to add OpenCV support.
   - Process camera images using OpenCV.

prerequisites:
    - A development machine with [Android Studio](https://developer.android.com/studio) installed. 
    - An Android smartphone.

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T23:44:45Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 2137cec46fe8d57f11e9e4011306a140bba7d8a5b2326a746193c1794a148f75
  summary_generated_at: '2026-06-02T02:42:50Z'
  summary_source_hash: 2137cec46fe8d57f11e9e4011306a140bba7d8a5b2326a746193c1794a148f75
  faq_generated_at: '2026-06-02T23:44:45Z'
  faq_source_hash: 2137cec46fe8d57f11e9e4011306a140bba7d8a5b2326a746193c1794a148f75
  summary: >-
    Build an introductory Android camera app that uses OpenCV to process images on an Arm-based
    smartphone. Working in Android Studio on Windows, you create a Kotlin project, integrate the
    OpenCV library, enable camera permissions, and capture real-time frames using JavaCameraView.
    You then manage Mat objects and implement adaptive thresholding with OpenCV’s Imgproc.adaptiveThreshold,
    controlled by a simple UI toggle for real-time processing. The result is a runnable app on
    an Android smartphone that demonstrates live camera capture and basic computer vision processing.
    No additional prerequisites are explicitly listed beyond Android Studio on your development
    machine and an Android smartphone. Estimated time to complete is about 30 minutes.
  faqs:
  - question: Which Android Studio version should I use for this path?
    answer: >-
      The example uses Android Studio Jellyfish | 2023.3.1 Patch 1. The Learning Path does not
      list other versions, so follow the steps as shown with that release.
  - question: Do I need to develop on Windows to follow the steps?
    answer: >-
      Yes, the target operating system for the development machine in this Learning Path is Windows.
      The instructions and tooling are presented with that environment in mind.
  - question: Should I use Kotlin or Java for the project?
    answer: >-
      The steps configure the project to use Kotlin and show edits in MainActivity.kt. Java is
      listed among the tools, but the provided code examples use Kotlin.
  - question: How do I know OpenCV is integrated correctly?
    answer: >-
      Follow the steps to add the OpenCV library and imports like org.opencv.imgproc.Imgproc.
      A successful build and the ability to run the app with JavaCameraView and adaptive thresholding
      indicate the integration is working.
  - question: What result should I expect when I run the app on my phone?
    answer: >-
      You should see a camera preview from JavaCameraView. When you check the provided checkbox,
      adaptive thresholding is applied to the live frames; unchecking it shows the unprocessed
      preview.
# END generated_summary_faq

author: Dawid Borycki

### Tags
skilllevels: Introductory
subjects: Graphics
armips:
    - Cortex-A
operatingsystems:
    - Windows
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
        title: Enhanced OpenCV For Android Support & ARM Performance Gains
        link: https://opencv.org/blog/enhanced-opencv-for-android-support-arm-performance-gains/
        type: blog


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

