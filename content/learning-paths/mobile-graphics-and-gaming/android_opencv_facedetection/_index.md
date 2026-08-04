---
title: Detect faces with OpenCV on Android Devices

description: Learn how to implement face detection on Android devices using OpenCV, camera frame retrieval, and Haar cascade classifiers.

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for developers who are interested in creating Computer Vision applications with OpenCV on Android devices. 

learning_objectives:
   - Describe how you can use OpenCV for face detection.   
   - Use OpenCV to retrieve camera frames.
   - Use Haar cascade classifier for face detection.

prerequisites:
   - A development machine with [Android Studio](https://developer.android.com/studio) installed. 
   - An Android smartphone.
   - Familiarity with OpenCV, review [Create Computer Vision Applications with OpenCV on Android Devices](/learning-paths/mobile-graphics-and-gaming/android_opencv_camera/) before starting.

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-04T22:13:25Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 6a159280537ddec6aa26ae3c8610a25dc3c4737c89e94297e433313d12f532f1
  summary_generated_at: '2026-08-04T22:13:25Z'
  summary_source_hash: 6a159280537ddec6aa26ae3c8610a25dc3c4737c89e94297e433313d12f532f1
  faq_generated_at: '2026-08-04T22:13:25Z'
  faq_source_hash: 6a159280537ddec6aa26ae3c8610a25dc3c4737c89e94297e433313d12f532f1
  summary: >-
    You build a simple face-detection app on Android using
    OpenCV. You create a new Android Studio project, add OpenCV, and verify that camera frames
    are available for processing. You then include a pre-trained Haar cascade XML from OpenCV
    and use the cascade classifier to locate faces in captured frames. You focus on core setup
    decisions, load the cascade correctly, and check that detection runs on your device.
    By the end, you run the app on an Android smartphone and confirm that the OpenCV-based Haar
    cascade detects faces from camera frames using a classical machine learning approach.
  faqs:
  - question: Which Android Studio project template should I use to start?
    answer: >-
      Use the Empty Views Activity template. The steps show this selection during project creation.
  - question: How do I know I’ve added OpenCV to the project correctly?
    answer: >-
      Your project should build without unresolved OpenCV references, and the app should launch
      without OpenCV-related initialization errors. If imports or classes are missing, revisit
      the step where OpenCV is added.
  - question: Where do I get the Haar cascade file, and how do I reference it?
    answer: >-
      Use the pre-trained Haar cascade XML provided by OpenCV. Add the file to your project as
      shown in the steps and ensure your code loads it before running detection.
  - question: What should I check if I see no faces detected?
    answer: >-
      Confirm that camera frames are being retrieved and that the Haar cascade XML path is correct
      and loads successfully. If loading fails, fix the file location or resource reference and
      try again.
  - question: Can I use an emulator instead of a physical device?
    answer: >-
      This path lists an Android smartphone for testing. Emulator use is not explicitly listed.
# END generated_summary_faq

author: Dawid Borycki

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: ML
armips:
    - Cortex-A
operatingsystems:
    - Windows
    - macOS
tools_software_languages:
    - Android
    - Android Studio
    - Kotlin

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
