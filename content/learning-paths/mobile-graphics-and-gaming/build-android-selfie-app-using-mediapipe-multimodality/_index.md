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
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-04T22:16:17Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 3345140b8b2864925454eeaafb7f4f114893258cbac48fbc92a59da08e47fc0b
  summary_generated_at: '2026-08-04T22:16:17Z'
  summary_source_hash: 3345140b8b2864925454eeaafb7f4f114893258cbac48fbc92a59da08e47fc0b
  faq_generated_at: '2026-08-04T22:16:17Z'
  faq_source_hash: 3345140b8b2864925454eeaafb7f4f114893258cbac48fbc92a59da08e47fc0b
  summary: >-
    You assemble a hands-free selfie Android app on Arm-based devices
    by setting up Android Studio, connecting a physical device with USB debugging, granting camera
    permission, integrating MediaPipe Solutions through Gradle version catalogs, and structuring
    app logic with ViewModel and Jetpack Lifecycle. You’ll wire Kotlin Flows to handle asynchronous
    streams, using SharedFlow for one-off UI events and later adopting StateFlow for observable
    screen state. You finish with a deployable project on an Arm-powered Android phone, with the
    camera permission flow in place and UI state preserved across configuration changes, establishing
    a solid MVVM foundation for integrating multimodal MediaPipe tasks.
  faqs:
  - question: Do I need a physical device, or can I use an emulator?
    answer: >-
      Use a recent Arm-powered Android phone with a front-facing camera. The steps walk you through
      enabling USB debugging and deploying to a connected device.
  - question: What should I check if my phone doesn’t appear as a deploy target in Android Studio?
    answer: >-
      Verify that USB debugging is enabled on the device and confirm the Allow USB debugging prompt,
      selecting Always allow from this computer. Use a data-capable USB cable and reconnect the
      device.
  - question: Where do I add the MediaPipe dependency version?
    answer: >-
      Open libs.versions.toml and append the specified line in the [versions] section. Save the
      file as instructed before proceeding to add dependencies that reference this version.
  - question: How do I know my ViewModel and Lifecycle setup is correct?
    answer: >-
      After wiring your ViewModel, rotate the screen or trigger a configuration change and confirm
      that the UI state persists. A clean build with no unresolved lifecycle or ViewModel symbols
      is another quick check.
  - question: Which Flow should I use for UI events versus screen state?
    answer: >-
      Use SharedFlow for one-off UI events that multiple subscribers may observe. Use StateFlow
      for observable screen state, and define a sealed class with a SharedFlow in MainViewModel
      to expose discrete UI events.
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
