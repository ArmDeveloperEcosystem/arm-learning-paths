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
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-04T22:12:46Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: f2827150956a0bd11232b9fe0c594cbd6254e035554cae6f3011e06813b741bf
  summary_generated_at: '2026-08-04T22:12:46Z'
  summary_source_hash: f2827150956a0bd11232b9fe0c594cbd6254e035554cae6f3011e06813b741bf
  faq_generated_at: '2026-08-04T22:12:46Z'
  faq_source_hash: f2827150956a0bd11232b9fe0c594cbd6254e035554cae6f3011e06813b741bf
  summary: >-
    You build an Android Studio app that uses OpenCV to capture
    and process live camera frames. You create a new project, add the OpenCV library, and enable
    camera permissions before wiring up JavaCameraView for preview. The layout adds buttons to
    start and stop the preview and a checkbox to control real-time processing. In MainActivity,
    you manage OpenCV Mat objects and implement adaptive thresholding with Imgproc.adaptiveThreshold,
    applying it only when the checkbox is selected. By the end, you can run the app on a phone
    and confirm that the preview toggles between raw and processed output.
  faqs:
  - question: Which project template should I pick when I create the app?
    answer: >-
      Select Empty Views Activity in the New Project window. This matches the project structure
      used in the steps.
  - question: Which language should I choose when I set up the project?
    answer: >-
      Choose Kotlin. The code changes and examples reference Kotlin files such as MainActivity.kt.
  - question: Where do I add the camera preview and UI controls?
    answer: >-
      Edit activity_main.xml as shown to add the start/stop controls, the processing checkbox,
      and the camera preview using JavaCameraView.
  - question: How do I know OpenCV is integrated correctly before I run on a device?
    answer: >-
      Your project should build without errors, imports like Mat and Imgproc should resolve, and
      JavaCameraView should compile. On the device, the preview should appear and the processing
      checkbox should change the displayed output.
  - question: What should I check if the camera preview is blank or processing doesn’t change
      the image?
    answer: >-
      Confirm camera permission is enabled and use the provided control to start the preview.
      Make sure the checkbox is selected to apply adaptive thresholding and that the device camera
      is available.
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
