---
title: Install and Use Arm integration packages for Unity
description: Learn how to install Arm integration packages in Unity to view GPU metrics in Unity Profiler and annotate games with markers for Arm Performance Studio.

minutes_to_complete: 20

who_is_this_for: This is an introductory topic for Unity developers who are targeting Android devices and want to get more insight into how their game performs on devices with Arm CPUs and GPUs.

learning_objectives: 
    - Install the packages in Unity
    - View Arm GPU metrics in the Unity Profiler
    - Annotate your Unity game with markers that give context to a profile in Arm Performance Studio tools

prerequisites:
    - Familiarity with Unity and the Unity Profiler
    - Familiarity with Arm Performance Studio tools

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T00:09:23Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 4a990e957658b03bac9306d5f8e6955734cc1d3b063f43c38ac525ed1bf95b79
  summary_generated_at: '2026-06-02T02:59:56Z'
  summary_source_hash: 4a990e957658b03bac9306d5f8e6955734cc1d3b063f43c38ac525ed1bf95b79
  faq_generated_at: '2026-06-03T00:09:23Z'
  faq_source_hash: 4a990e957658b03bac9306d5f8e6955734cc1d3b063f43c38ac525ed1bf95b79
  summary: >-
    Learn how to install Arm integration packages in Unity to profile games targeting Android
    devices with Arm CPUs and GPUs. In about 20 minutes, you add the System Metrics Mali package
    to enable Arm GPU hardware counters in the Unity Profiler (supported in Unity 2021.2 and later)
    and integrate annotations that appear in Arm Performance Studio tools, Streamline and Performance
    Advisor. You work on Windows, macOS, or Linux. By the end, you can configure Unity to display
    Arm GPU metrics and annotate your project with markers and custom counters to add context
    in Arm Performance Studio. Prerequisites include familiarity with Unity, the Unity Profiler,
    and Arm Performance Studio tools.
  faqs:
  - question: Do I need a specific Unity version to view Arm GPU metrics?
    answer: >-
      Yes. The System Metrics Mali package is supported in Unity versions 2021.2 and later.
  - question: How do I install the System Metrics Mali package in Unity?
    answer: >-
      Open Window > Package Manager, click the + button, and choose Add package by name. Enter
      com.unity.profiling.systemmetrics.mali to add the package.
  - question: What result should I expect in the Unity Profiler after installing the Mali metrics
      package?
    answer: >-
      You will be able to read and display GPU hardware counters from Arm GPUs in the Unity Profiler.
  - question: How do I enable annotations for Arm Performance Studio from my Unity project?
    answer: >-
      Use the Arm Performance Studio Unity integration package to add annotations. It lets you
      mark the timeline with events and custom counters that provide context alongside performance
      data in Streamline and are visible to Performance Advisor.
  - question: What should I check if the Mali metrics package is not available or GPU metrics
      do not appear?
    answer: >-
      Verify that your project uses Unity 2021.2 or later and that you added the package by name
      as com.unity.profiling.systemmetrics.mali. After installation, open the Unity Profiler to
      view the Arm GPU hardware counters.
# END generated_summary_faq

author: Julie Gaskin

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
armips:
    - Cortex-A
    - Mali
tools_software_languages:
    - Unity
    - Arm Performance Studio
operatingsystems:
    - Windows
    - macOS
    - Linux


further_reading:
    - resource:
        title: Get started with Streamline 
        link: https://developer.arm.com/documentation/102477/latest/
        type: documentation
    - resource:
        title: Android performance triage with Streamline 
        link: https://developer.arm.com/documentation/102540/latest/
        type: documentation
    - resource:
        title: Get started with Performance Advisor 
        link: https://developer.arm.com/documentation/102478/latest/
        type: documentation
    - resource:
        title: Tackling profiling for mobile games with Unity and Arm
        link: https://blog.unity.com/games/tackling-profiling-for-mobile-games-with-unity-and-arm
        type: blog
    - resource:
        title: Arm Performance Studio 
        link: https://developer.arm.com/Tools%20and%20Software/Arm%20Mobile%20Studio
        type: website



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

