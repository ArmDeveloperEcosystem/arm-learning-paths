---
title: Profile Unity application performance on Android devices
description: Learn how to deploy Unity applications to Android, profile code running on Arm devices, and analyze performance data for optimization.

minutes_to_complete: 40

who_is_this_for: Unity developers wanting to analyze the performance of their apps on Android devices

learning_objectives:
    - Deploy to Android
    - Profile code running on an Android device
    - Analyze performance data

prerequisites:
    - Recent Android device, such as a mobile phone or tablet
    - Desktop computer capable of running Unity
    - Basic knowledge of Unity and programming concepts
    - The setup described in the Learning Path [Get started with Unity on Android](/learning-paths/mobile-graphics-and-gaming/get-started-with-unity-on-android)

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-21T17:25:36Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 143a0925de4c87654b572f37b974a855581f345aefc7794014bbc16abc526163
  summary_generated_at: '2026-08-21T17:25:36Z'
  summary_source_hash: 143a0925de4c87654b572f37b974a855581f345aefc7794014bbc16abc526163
  faq_generated_at: '2026-08-21T17:25:36Z'
  faq_source_hash: 143a0925de4c87654b572f37b974a855581f345aefc7794014bbc16abc526163
  summary: >-
    You'll deploy a Unity collision sample to an Android device, collect performance data, and
    compare unoptimized and Arm Neon code. First, you'll create a URP project, import and deploy the sample,
    and examine the `Plain`, `Burst`, and `Neon` modes. Then, you'll use Unity Profiler to record and inspect
    frames. You'll also use Profile Analyzer to load, select, and compare the `Plain` and `Neon` recordings.
  faqs:
  - question: Do I need to create a new Unity project before importing the sample?
    answer: >-
      Yes. In Unity Hub, select **New Project**, select the **3D (URP) Core** template, and create
      a blank project before you import the sample.
  - question: Which tool should I use to examine results?
    answer: >-
      Use the Profiler to collect data and inspect specific frames. To use Profile Analyzer, open
      the Profiler window, load the recording there, then select **Pull Data** to analyze or
      compare datasets.
  - question: Which sample modes should I record for comparison?
    answer: >-
      Record the unoptimized `Plain` mode and the optimized `Neon` mode. You can also inspect
      `Burst` mode to see how its auto-vectorized code differs.
  - question: How do I compare the Plain and Neon recordings?
    answer: >-
      Compare recordings from the unoptimized `Plain` mode and the optimized `Neon` mode. Use the
      Profiler and Profile Analyzer to examine differences in frame timing and function execution.
  - question: What should I check if the Android device or app doesn't appear for profiling?
    answer: >-
      Confirm the app builds and deploys to the Android device using the steps from the [Get started with Unity on Android](/learning-paths/mobile-graphics-and-gaming/get-started-with-unity-on-android) Learning Path, then run the app on the device before recording. If
      no data appears, re-verify deployment and that the device is actively running the sample.
# END generated_summary_faq

author: Joshua Marshall-Law

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
armips:
    - Cortex-A
tools_software_languages:
    - Unity
    - csharp
operatingsystems:
    - Android

further_reading:
    - resource:
        title: Unity Profiler documentation
        link: https://docs.unity3d.com/Manual/Profiler.html
        type: documentation
    - resource:
        title: Unity Analyzer documentation
        link: https://docs.unity3d.com/Packages/com.unity.performance.profile-analyzer@0.4/manual/profiler-analyzer-window.html
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
