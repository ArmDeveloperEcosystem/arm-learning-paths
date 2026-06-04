---
title: Optimize Unity applications on Android using Neon intrinsics

minutes_to_complete: 90

description: Learn how to use Arm Neon intrinsics in Unity C# scripts to optimize code on Android and collect performance data using Unity Profiler.

who_is_this_for: Developers interested in leveraging the Unity Machine Learning Agents toolkit on Arm devices.

learning_objectives:
    - Use Arm Neon intrinsics in your Unity C# scripts
    - Optimize your code
    - Collect and compare performance data using the Unity Profiler and Analyzer tools

prerequisites:
    - Basic knowledge of Unity and C#
    - Recent Android device, such as a mobile phone or tablet
    - Desktop computer capable of running Unity
    - Unity version compatible with Unity Burst compiler 1.5 or later

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T00:10:08Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: f17ab3c4216495b88cee75a81612c11a4727d874114f914edf97c467f0d1c125
  summary_generated_at: '2026-06-02T03:00:21Z'
  summary_source_hash: f17ab3c4216495b88cee75a81612c11a4727d874114f914edf97c467f0d1c125
  faq_generated_at: '2026-06-03T00:10:08Z'
  faq_source_hash: f17ab3c4216495b88cee75a81612c11a4727d874114f914edf97c467f0d1c125
  summary: >-
    This advanced Learning Path guides you through using Arm Neon intrinsics in Unity C# scripts
    for Android, compiled with the Unity Burst compiler, and measuring results with the Unity
    Profiler and Analyzer tools. You will install Unity with Android build support, open a provided
    sample, configure an unoptimized baseline, then enable Burst and Neon intrinsics to compare
    performance across versions. The path was written using Unity v6.3 and Burst 1.8.28, though
    any Unity version compatible with Burst 1.5 or later is suitable. Prerequisites include basic
    Unity and C# knowledge, a desktop capable of running Unity, and a recent Android device for
    testing. Expect to complete the steps in around 90 minutes.
  faqs:
  - question: What do I need before running this Learning Path?
    answer: >-
      You need basic knowledge of Unity and C#, a recent Android device, a desktop capable of
      running Unity, and a Unity version compatible with the Burst compiler 1.5 or later. Android
      build support for Unity is required.
  - question: Which Unity and Burst versions are assumed?
    answer: >-
      Use a Unity version compatible with Burst 1.5 or later. The Learning Path was written using
      Unity v6.3 and Burst 1.8.28.
  - question: How do I enable the Burst package in my Unity project?
    answer: >-
      Open Window > Package Manager, set the Packages filter to Unity Registry, search for "Burst,"
      select it, and install or enable it. Follow the project setup described to allow Burst to
      compile the targeted code paths.
  - question: How do I switch the sample project between unoptimized, Burst, and Neon modes?
    answer: >-
      Edit Assets/BurstNeonCollisions/Scripts/CollisionCalculationScript.cs and set the codeMode
      constant (for example, Mode.Plain for unoptimized as shown). The Neon version will not function
      correctly on computers without Neon support, so run and profile that mode on an Android
      device.
  - question: How do I validate that the performance comparison worked?
    answer: >-
      Use the Unity Profiler and Analyzer to capture data for each mode—unoptimized, Burst, and
      Neon—on your Android device. You should see separate measurements that let you compare the
      collision-detection workload across modes.
# END generated_summary_faq

author: Ben Clark, Joshua Marshall-Law

### Tags
skilllevels: Advanced
subjects: Gaming
armips:
    - armv8
    - aarch64
    - arm64
    - arm architecture
    - Neon
tools_software_languages:
    - Unity
    - C#
operatingsystems:
    - Android


further_reading:
    - resource:
        title: Arm Neon documentation
        link: https://developer.arm.com/Architectures/Neon
        type: documentation
    - resource:
        title: Unity Burst compiler documentation
        link: https://docs.unity3d.com/Manual/com.unity.burst.html
        type: documentation



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

