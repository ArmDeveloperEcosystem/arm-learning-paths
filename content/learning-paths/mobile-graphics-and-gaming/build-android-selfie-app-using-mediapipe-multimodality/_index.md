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

# START generated_summary_faq

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-05T14:56:50Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 3345140b8b2864925454eeaafb7f4f114893258cbac48fbc92a59da08e47fc0b
  summary_generated_at: '2026-08-05T14:56:50Z'
  summary_source_hash: 3345140b8b2864925454eeaafb7f4f114893258cbac48fbc92a59da08e47fc0b
  faq_generated_at: '2026-08-05T14:56:50Z'
  faq_source_hash: 3345140b8b2864925454eeaafb7f4f114893258cbac48fbc92a59da08e47fc0b
  summary: >-
    You'll build the core of a hands-free selfie Android app with MediaPipe, Kotlin Flow, CameraX, and
    MVVM. First, you'll configure Android Studio, connect a physical device, and handle camera permissions.
    Then, you'll add MediaPipe Tasks through a version catalog, structure UI state with ViewModel and Jetpack
    Lifecycle, and connect asynchronous events with `SharedFlow` and `StateFlow`.
  faqs:
  - question: Where do I add MediaPipe versions and dependencies?
    answer: >-
      Add the version entry in `libs.versions.toml`. After updating the
      catalog and syncing, Android Studio should resolve the MediaPipe artifacts so you can import
      the corresponding classes in your code.
  - question: How do I know my device is correctly set up for debugging?
    answer: >-
      Enable USB debugging on the phone, then confirm the **Allow USB debugging** dialog by selecting **Always allow from this computer** and tapping the 
      **OK** button. If you don't see the dialog, review
      the Android Developer guidance for setting up a device for development.
  - question: When should I handle camera permissions in this project?
    answer: >-
      Handle camera permissions immediately after connecting your device and before integrating
      AI features to avoid runtime blockers
      when accessing the camera with CameraX later.
  - question: How do I verify that ViewModel is preserving UI state?
    answer: >-
      Populate state through the `ViewModel` class, then rotate the device or trigger a configuration
      change. The screen-level state should persist without refetching, indicating the `ViewModel`
      is working as intended.
  - question: Which Kotlin Flow type should I use for events versus state?
    answer: >-
      Use `SharedFlow` for one-time UI events that multiple subscribers may observe. Use `StateFlow`
      for observable, current UI state that the View needs to render and react to over time.
# END generated_summary_faq

author: Han Yin

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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
