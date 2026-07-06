---
title: Build an on-device AI Plank Tutor on Android

draft: true
cascade:
    draft: true
    
minutes_to_complete: 90

who_is_this_for: This Learning Path is for Android developers who want to explore creating an ML/GenAI pipeline, including camera input, local LLM inference, and speech.

learning_objectives:
    - Detect human pose landmarks from live Android camera frames with MediaPipe.
    - Structure data and build compact prompts that turn raw data into useful LLM input.
    - Run a mobile-sized LLM on-device with Arm's AI Chat library.
    - Speak generated output with Text-To-Speech.

prerequisites:
    - A development machine with Android Studio installed.
    - A recent Arm-powered Android phone in Developer Mode, with USB debugging enabled, a USB data cable, and at least 5 GB of free storage for the GGUF model import.
    - Android Debug Bridge (`adb`), included with the Android SDK platform tools.
    - Basic familiarity with Kotlin and Android app development.

author: Ben Clark

### Tags
skilllevels: Introductory
subjects: ML
armips:
    - Cortex-A
    - Arm AI Chat library
tools_software_languages:
    - Android Studio
    - Kotlin
    - CameraX
    - MediaPipe
    - LLM
    - Neon
    - SVE2
    - SME2
operatingsystems:
    - Android

further_reading:
    - resource:
        title: AI Yoga Tutor
        link: https://developer.arm.com/community/arm-community-blogs/b/ai-blog/posts/ai-yoga-tutor
        type: blog
    - resource:
        title: AI Chat - Explore and evaluate LLMs on Android and ChromeOS
        link: https://developer.arm.com/community/arm-community-blogs/b/announcements/posts/ai-chat-explore-and-evaluate-llms-on-android-and-chromeos
        type: blog
    - resource:
        title: AI Chat library on GitHub
        link: https://github.com/arm/ai-chat
        type: website
    - resource:
        title: AI Chat library @ Maven Central
        link: https://central.sonatype.com/artifact/com.arm/ai-chat
        type: documentation
    - resource:
        title: MediaPipe Pose Landmarker
        link: https://ai.google.dev/edge/mediapipe/solutions/vision/pose_landmarker
        type: documentation
    - resource:
        title: Android TextToSpeech
        link: https://developer.android.com/reference/android/speech/tts/TextToSpeech
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
