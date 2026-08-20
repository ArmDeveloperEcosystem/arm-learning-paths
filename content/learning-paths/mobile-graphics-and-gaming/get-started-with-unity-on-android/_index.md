---
title: Get started with Unity on Android

minutes_to_complete: 30

who_is_this_for: Unity developers who want to target Android devices

learning_objectives: 
    - Set up with Unity development
    - Build and deploy to an Android device
    - Launch the Profiler tool to investigate performance issues

prerequisites:
    - Basic knowledge of game engines and programming concepts
    - Recent Android device, such as a mobile phone or tablet
    - Desktop computer capable of running Unity

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-17T22:03:25Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: ab180c95be30dd0a07915d4294aa8b1373361f81fe13cee10b158876c93e2f55
  summary_generated_at: '2026-08-17T22:03:25Z'
  summary_source_hash: ab180c95be30dd0a07915d4294aa8b1373361f81fe13cee10b158876c93e2f55
  faq_generated_at: '2026-08-17T22:03:25Z'
  faq_source_hash: ab180c95be30dd0a07915d4294aa8b1373361f81fe13cee10b158876c93e2f55
  summary: >-
    You'll set up Unity with Android support, deploy a sample project, and profile it on a device.
    First, you'll switch the target platform, build the scene containing `Spin.cs`, and verify the app runs.
    Then, you'll use the **Profiler** on Unity in the editor and on-device to compare CPU, rendering, and memory
    activity across frames on Arm Cortex-A systems.
  faqs:
  - question: How do I know if I installed Android Build Support correctly?
    answer: >-
      Open the **Build Settings** window and check that Android appears as a selectable platform.
      If you can switch the project’s active platform to Android, the support is installed.
  - question: What should I see in the sample scene before building?
    answer: >-
      The scene contains a **Main Camera**, a **Directional Light**, and a **Cube** with a `Spin.cs` script
      attached. When you run the scene, the cube rotates.
  - question: Which platform should I make active before I build the project?
    answer: >-
      Set Android as the active platform in the **Build Settings** window. Building with the correct
      active platform ensures the output targets your Android device.
  - question: How do I confirm the Profiler is collecting data?
    answer: >-
      Open the **Profiler** on Unity and watch for the timeline to populate with frame samples. **CPU**,
      **Rendering**, and **Memory** charts should update as the app runs.
  - question: Should I profile in the editor or on my device first?
    answer: >-
      Start profiling in the Unity Editor for quick checks, then profile on your Android device
      to observe behavior on target hardware. Use both views to compare results across environments.
# END generated_summary_faq

author: Joshua Marshall-Law

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Gaming
armips:
    - Cortex-A
tools_software_languages:
    - Unity
    - csharp
operatingsystems:
    - Android

further_reading:
    - resource:
        title: Profiler overview 
        link: https://docs.unity3d.com/Manual/Profiler.html
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
