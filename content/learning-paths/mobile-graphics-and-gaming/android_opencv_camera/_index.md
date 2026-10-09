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

# START generated_summary_faq

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-05T14:52:41Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: f2827150956a0bd11232b9fe0c594cbd6254e035554cae6f3011e06813b741bf
  summary_generated_at: '2026-08-05T14:52:41Z'
  summary_source_hash: f2827150956a0bd11232b9fe0c594cbd6254e035554cae6f3011e06813b741bf
  faq_generated_at: '2026-08-05T14:52:41Z'
  faq_source_hash: f2827150956a0bd11232b9fe0c594cbd6254e035554cae6f3011e06813b741bf
  summary: >-
    You'll build an Android app that captures and processes camera frames with OpenCV. First, you'll configure a
    Kotlin project, add camera access and a `JavaCameraView`, and implement frame handling with `Mat`
    objects. Then, you'll apply adaptive thresholding when processing is enabled and run the app on a device
    to switch between the original and thresholded live views.
  faqs:
  - question: What result should I expect when I run the app after adding OpenCV?
    answer: >-
      You should see a camera preview from `JavaCameraView` after granting camera permission. Starting
      the preview shows live frames. To switch to an adaptive thresholded image, check the processing checkbox.
  - question: Where do I add the camera view and UI controls?
    answer: >-
      Edit `activity_main.xml` to include a `JavaCameraView`, start and stop buttons,
      and a checkbox. Replace the existing layout with the provided XML so the controls appear
      correctly.
  - question: Which OpenCV component provides frames for processing in this app?
    answer: >-
      `JavaCameraView` supplies camera frames. You'll process those frames as OpenCV `Mat` objects in
      your activity code.
  - question: Do I need to use the exact project and package names shown?
    answer: >-
      Using the provided names is recommended. However, you can choose different names, as long as you stay consistent
      across the project configuration and code. 
  - question: What should I check if the camera preview doesn't appear?
    answer: >-
      Verify the app has camera permission and that the `JavaCameraView` is present in the layout.
      Use the start control to begin the preview before expecting frames to update.
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
