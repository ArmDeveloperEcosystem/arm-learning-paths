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

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T23:45:29Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 3a120620bbc56e796aa45fbe01aa1455fbee085a1a4cf0d055416b7e95e72d0d
  summary_generated_at: '2026-06-02T02:43:15Z'
  summary_source_hash: 3a120620bbc56e796aa45fbe01aa1455fbee085a1a4cf0d055416b7e95e72d0d
  faq_generated_at: '2026-06-02T23:45:29Z'
  faq_source_hash: 3a120620bbc56e796aa45fbe01aa1455fbee085a1a4cf0d055416b7e95e72d0d
  summary: >-
    Build an introductory Android app that detects faces in real time using OpenCV. Working in
    Android Studio on Windows or macOS, you will create a Kotlin project, add OpenCV, retrieve
    camera frames, and apply a Haar cascade classifier using a pre-trained XML file. The steps
    focus on the essentials for camera access and classical face detection with OpenCV on Android
    devices, relevant to Arm Cortex-A based smartphones. Prerequisites include Android Studio
    on your development machine, an Android smartphone, and familiarity with OpenCV (with a recommended
    prior Learning Path for review). The estimated time to complete is about 30 minutes.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need Android Studio installed on a Windows or macOS machine, an Android smartphone,
      and familiarity with OpenCV. The path recommends reviewing the “Create Computer Vision Applications
      with OpenCV on Android Devices” Learning Path first.
  - question: Do I need a specific version of Android Studio?
    answer: >-
      The example uses Android Studio Jellyfish | 2023.3.1 Patch 1. If you use a different version,
      expect minor UI differences when creating the project.
  - question: Which Haar cascade file should I use and how is it included?
    answer: >-
      This path uses OpenCV’s pre-trained Haar cascades, which are XML files. The steps indicate
      which cascade to use and how to include it in your project.
  - question: How do I know OpenCV is correctly added and camera frames are being read?
    answer: >-
      After following the setup steps, you should be able to build the project and retrieve camera
      frames via OpenCV without errors. If frame retrieval works, proceed to the face detection
      step with the Haar cascade.
  - question: What should I check if faces are not being detected?
    answer: >-
      Confirm that the correct Haar cascade XML file is included and loaded, and that valid camera
      frames are being passed to the classifier. Revisit the steps to ensure OpenCV integration
      and frame retrieval are configured as shown.
# END generated_summary_faq

author: Dawid Borycki

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

