---
title: Build an on-device AI fitness tutor app on Android
description: Build an on-device Android fitness tutor app called AI Plank Tutor that uses CameraX and MediaPipe to score a plank pose, Arm AI Chat to generate local LLM feedback, and Android text-to-speech to speak corrections.
    
minutes_to_complete: 90

who_is_this_for: This Learning Path is for Android developers who want to explore creating an ML or Generative AI pipeline, including camera input, local Large Language Model (LLM) inference, and speech.

learning_objectives:
    - Detect human pose landmarks from live Android camera frames with MediaPipe.
    - Structure data and build compact prompts that turn raw data into useful LLM input.
    - Run a mobile-sized LLM on-device with Arm's AI Chat library.
    - Generate output as speech with Text-To-Speech.

prerequisites:
    - A development machine with Android Studio installed.
    - A recent Arm-powered Android phone in Developer Mode, with USB debugging enabled, a USB data cable, and at least 5 GB of free storage for the GGUF model import.
    - Android Debug Bridge (`adb`), included with the Android SDK platform tools.
    - Basic familiarity with Kotlin and Android app development.

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-21T21:58:52Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: ffd3800f451b7847ad61169a4b8edb63a84b83475d6790ab15378fd843153aa1
  summary_generated_at: '2026-07-21T21:58:52Z'
  summary_source_hash: ffd3800f451b7847ad61169a4b8edb63a84b83475d6790ab15378fd843153aa1
  faq_generated_at: '2026-07-21T21:58:52Z'
  faq_source_hash: ffd3800f451b7847ad61169a4b8edb63a84b83475d6790ab15378fd843153aa1
  summary: >-
    You'll build AI Plank Tutor, an on-device Android app that evaluates a static plank pose and
    delivers spoken correction. You'll configure CameraX and MediaPipe Pose Landmarker to extract
    landmarks from live camera frames, calculate joint angles, and compute a weighted score against
    an instructor reference. Then, you'll turn the largest joint-angle differences into a compact
    prompt for a local LLM. Finally, you'll integrate Arm AI Chat for GGUF inference and connect
    Android text-to-speech so the app speaks each correction. By the end, you'll have a complete
    on-device pipeline from camera input to spoken feedback.
  faqs:
  - question: Where should I add the CameraX initialization code?
    answer: >-
      Open `ui/MainActivity.kt` and replace the `TODO` in `setUpCamera()` with the provided
      `ProcessCameraProvider` snippet. When the provider is ready, the callback stores it and calls
      `bindCameraUseCases()`.
  - question: What do I do if the camera doesn't detect pose landmarks?
    answer: >-
      After CameraX initializes and binds its use cases, MediaPipe Pose Landmarker should produce
      landmarks for each frame. If the camera preview appears but no pose landmarks are detected, make sure that you granted camera
        permission and that your full body is visible in the frame. Then, check Logcat for
        `PoseLandmarkerHelper` errors. If the preview doesn't appear, confirm that
        `bindCameraUseCases()` runs after `ProcessCameraProvider` becomes available.
  - question: What defines the reference pose and weighting used to score the plank?
    answer: >-
      `data/PlankPoseData.kt` contains `referenceLandmarks` for the instructor pose and `angleWeights`
      that set the importance of each joint. The app uses these values to calculate joint angles
      and a weighted score.
  - question: How do I control which joint differences are sent to the LLM?
    answer: >-
      `ui/landmarker/PoseScoreHelper.kt` maps angles to names with `KEY_ANGLE_NAMES` and formats the
      largest differences in `angleDifference()`. Use the `filter` and `maxEntries` parameters to
      set a threshold and limit the entries included in the prompt.
  - question: Where do I add the AI Chat dependency and which model format should I use?
    answer: >-
      Add `implementation("com.arm:ai-chat:0.1.0")` to the `dependencies` block in `app/build.gradle`,
      then sync the project. 
# END generated_summary_faq

author: Ben Clark

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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
        title: Build a Hands-Free Selfie Android Application with MediaPipe
        link: https://learn.arm.com/learning-paths/mobile-graphics-and-gaming/build-android-selfie-app-using-mediapipe-multimodality/
        type: learning path
    - resource:
        title: Add an LLM to your Android app with Arm's AI Chat library
        link: https://learn.arm.com/learning-paths/mobile-graphics-and-gaming/android-ai-chat-lib/
        type: learning path
    - resource:
        title: AI Yoga Tutor
        link: https://developer.arm.com/community/arm-community-blogs/b/ai-blog/posts/ai-yoga-tutor
        type: blog
    - resource:
        title: AI Chat library on GitHub
        link: https://github.com/arm/ai-chat
        type: website
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
