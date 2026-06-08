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

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T00:04:52Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 9950a58160736e0c60ad80ea602262347e2ba8a37a00e29f25dc96709026ea1f
  summary_generated_at: '2026-06-02T02:56:23Z'
  summary_source_hash: 9950a58160736e0c60ad80ea602262347e2ba8a37a00e29f25dc96709026ea1f
  faq_generated_at: '2026-06-03T00:04:52Z'
  faq_source_hash: 9950a58160736e0c60ad80ea602262347e2ba8a37a00e29f25dc96709026ea1f
  summary: >-
    This introductory Learning Path guides Unity developers through deploying a sample app to
    an Android device, collecting frame-level performance data with the Unity Profiler, and comparing
    captures in the Profile Analyzer. You will create a blank 3D (URP) Core project, import a
    sample from the Unity Asset Store, and run three code paths—Plain, Burst, and Neon with Arm
    Neon intrinsics—to observe differences. The steps emphasize recording datasets for the unoptimized
    and Neon modes, then loading them into the Analyzer to visualize and compare results. Prerequisites
    are a recent Android phone or tablet, a desktop capable of running Unity, basic Unity/programming
    knowledge, and the setup from Get started with Unity on Android.
  faqs:
  - question: What do I need before running this Learning Path?
    answer: >-
      Have a recent Android device, a desktop capable of running Unity, and basic Unity/programming
      knowledge. Complete the setup described in Get started with Unity on Android before proceeding.
  - question: Which Unity project template should I use when creating the project?
    answer: >-
      Create a blank project in Unity Hub using the 3D (URP) Core template. Even though the sample
      is a project, you will import it into this blank project.
  - question: How are the Profiler and Profile Analyzer used differently in this path?
    answer: >-
      You will use the Profiler to record data over a series of frames and drill into specific
      frames and timings. Then you will load the captured data into the Profile Analyzer to visualize
      and compare datasets.
  - question: Which sample modes should I run, and what do they represent?
    answer: >-
      The sample has three modes: Plain (unoptimized), Burst (code tagged for the Burst compiler
      to enable auto-vectorization), and Neon (uses Arm Neon intrinsics). You will collect data
      from the unoptimized (Plain) and optimized (Neon) versions for comparison.
  - question: How should I run the sample on the device during data collection?
    answer: >-
      Run the app in landscape orientation, as it works best on Android in this mode. The sample
      displays information in the bottom-right of the screen.
# END generated_summary_faq

author: Joshua Marshall-Law

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
armips:
    - armv8
    - aarch32
    - aarch64
    - arm64
    - arm architecture
tools_software_languages:
    - Unity
    - C#
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

