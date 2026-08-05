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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-05T14:53:10Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 6a159280537ddec6aa26ae3c8610a25dc3c4737c89e94297e433313d12f532f1
  summary_generated_at: '2026-08-05T14:53:10Z'
  summary_source_hash: 6a159280537ddec6aa26ae3c8610a25dc3c4737c89e94297e433313d12f532f1
  faq_generated_at: '2026-08-05T14:53:10Z'
  faq_source_hash: 6a159280537ddec6aa26ae3c8610a25dc3c4737c89e94297e433313d12f532f1
  summary: >-
    You'll build an Android app that performs face detection with OpenCV and a Haar cascade classifier.
    First, you'll configure the project, add OpenCV, retrieve camera frames, and load the pre-trained cascade.
    Then, you'll apply the classifier to live input, deploy the app to a connected smartphone, and exercise
    the detection pipeline.
  faqs:
  - question: Which Android Studio project template should I choose to follow the steps?
    answer: >-
      Use the **Empty Views Activity** template. It matches the structure expected by the instructions
      and keeps the project minimal.
  - question: How do I know OpenCV is correctly added before I write detection code?
    answer: >-
      Your project should sync and build without errors, and OpenCV classes should resolve in
      the editor. You can confirm runtime availability when the app runs on the device without
      OpenCV initialization errors.
  - question: Do I need to train a face detector for this project?
    answer: >-
      No. You'll use OpenCV’s pre‑trained Haar cascade for face detection, so you don't need
      to train a model.
  - question: What cascade file format do I use for face detection?
    answer: >-
      Use a Haar cascade XML file provided by OpenCV for face detection. It contains pre‑trained
      data the classifier loads at runtime.
  - question: What result should I expect when the app runs on the device?
    answer: >-
      You should see camera frames retrieved and processed with the Haar cascade classifier. Check
      for detections according to your app’s processing and display logic.
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
