---
title: Build a Hands-Free Selfie Android Application with MediaPipe

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

author: Han Yin

### Tags
skilllevels: Advanced
subjects: ML
armips:
    - Cortex-A
    - Cortex-X
    - Mali GPU
tools_software_languages:
    - mobile
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

