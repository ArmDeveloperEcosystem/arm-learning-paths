---
title: Build a Hands-Free Selfie Android Application with MediaPipe
description: Learn how to build a hands-free selfie Android application using MediaPipe multimodal AI, Kotlin flows, CameraX, and MVVM architecture.

minutes_to_complete: 120

who_is_this_for: This is an introductory topic for mobile application developers interested in learning how to build an Android selfie application with Modern MediaPipe Multimodal AI, Kotlin flows, and CameraX, using the Modern Android Development (MAD) architecture design.

learning_objectives:
    - Architect a modern hands-free selfie Android app with MediaPipe.
    - Leverage lifecycle-aware components within the Model-View-ViewModel (MVVM) architecture.
    - Combine MediaPipe's face landmark detection and gesture recognition for integration in a multimodel selfie solution.
    - Use JetPack CameraX to access camera features.
    - Use Kotlin Flow APIs to handle multiple asynchronous data streams.

prerequisites:
    - A development machine with [Android Studio](https://developer.android.com/studio) installed.
    - A recent Arm-powered Android phone with a front-facing camera and a USB data cable.
    - Familiarity with Android development concepts.
    - Basic knowledge of Modern Android Architecture. See [Modern Android App Architecture](https://developer.android.com/courses/pathways/android-architecture).
    - Basic knowledge of Kotlin programming language, including [Coroutines](https://kotlinlang.org/docs/coroutines-overview.html) and [Kotlin Flows](https://kotlinlang.org/docs/flow.html).

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T23:49:17Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 13ff69755e51c6d7c355616f95703b3f2cefaedcf1f8dbeab31fe2e3db9aec74
  summary_generated_at: '2026-06-02T02:46:24Z'
  summary_source_hash: 13ff69755e51c6d7c355616f95703b3f2cefaedcf1f8dbeab31fe2e3db9aec74
  faq_generated_at: '2026-06-02T23:49:17Z'
  faq_source_hash: 13ff69755e51c6d7c355616f95703b3f2cefaedcf1f8dbeab31fe2e3db9aec74
  summary: >-
    Build a hands-free selfie Android app that runs on a recent Arm-powered Android phone using
    MediaPipe multimodal AI, Kotlin Flows, CameraX, and an MVVM architecture. You will set up
    Android Studio, connect a device with USB debugging, manage camera permissions, add MediaPipe
    dependencies, and incorporate Jetpack Lifecycle components. The path shows how to combine
    MediaPipe face landmark detection and gesture recognition, access camera features with CameraX,
    and handle multiple asynchronous data streams with SharedFlow and StateFlow. Prerequisites
    include Android Studio, a front-facing camera device, familiarity with Android development
    and Modern Android Architecture, and basic Kotlin knowledge (Coroutines and Flows). Estimated
    time to complete is about 120 minutes.
  faqs:
  - question: What do I need before running the app on a device?
    answer: >-
      Install Android Studio on your development machine and have a recent Arm-powered Android
      phone with a front-facing camera and a USB data cable. You should be familiar with Android
      development, Modern Android Architecture, Kotlin Coroutines, and Kotlin Flows.
  - question: How do I know my Android Studio setup is complete before coding?
    answer: >-
      Open Android Studio, accept license agreements, download all required assets, and choose
      the default or recommended settings. These steps prepare the environment used throughout
      the Learning Path.
  - question: How do I set up and verify device debugging over USB?
    answer: >-
      Enable USB debugging on your device, then connect it by USB and tap OK on the Allow USB
      debugging dialog. Check Always allow from this computer so Android Studio can deploy and
      debug the app without repeated prompts.
  - question: Which option should I use to access the camera in this app?
    answer: >-
      Use JetPack CameraX to access camera features. Camera permissions are handled in a dedicated
      step before running the app on your device.
  - question: How do I add MediaPipe and handle UI state and events?
    answer: >-
      Add MediaPipe dependencies by updating libs.versions.toml and project settings as shown
      in the steps that introduce MediaPipe Solutions and Tasks. Manage UI state with ViewModel
      and Jetpack Lifecycle, and use SharedFlow and StateFlow to emit and observe UI events and
      state across multiple subscribers.
# END generated_summary_faq

author: Han Yin

### Tags
skilllevels: Advanced
subjects: ML
armips:
    - Cortex-A
    - Mali GPU
tools_software_languages:
    - Android Studio
    - Kotlin
    - MediaPipe
operatingsystems:
    - Android


further_reading:
    - resource:
        title: Completed sample app
        link: https://github.com/hanyin-arm/sample-android-selfie-app-using-mediapipe-multimodality
        type: website
    - resource:
        title: Android app architecture
        link: https://developer.android.com/topic/architecture/intro
        type: documentation
    - resource:
        title: Android codelabs on ML
        link: https://developer.android.com/get-started/codelabs?category=androidml
        type: website
    - resource:
        title: How to bring your AI Model to Android devices
        link: https://android-developers.googleblog.com/2024/10/bring-your-ai-model-to-android-devices.html
        type: blog



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

