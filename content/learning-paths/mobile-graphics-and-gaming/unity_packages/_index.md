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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-21T17:30:02Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 42d8afc97e0ca6ce97b03e48d734df0cc0d445a917bd6af2e82c12c86de4776b
  summary_generated_at: '2026-08-21T17:30:02Z'
  summary_source_hash: 42d8afc97e0ca6ce97b03e48d734df0cc0d445a917bd6af2e82c12c86de4776b
  faq_generated_at: '2026-08-21T17:30:02Z'
  faq_source_hash: 42d8afc97e0ca6ce97b03e48d734df0cc0d445a917bd6af2e82c12c86de4776b
  summary: >-
    You'll install Unity packages that expose Arm GPU metrics and add context to performance analysis.
    First, you'll add System Metrics Mali in **Package Manager** and verify the **Mali System Metrics** chart
    in the Unity Profiler. Then, you'll install the Arm Performance Studio integration from its Git
    URL, add markers, channels, counters, and Custom Activity Maps in Streamline, and use region
    markers in Performance Advisor.
  faqs:
  - question: Which Unity version do I need to use the System Metrics Mali package?
    answer: >-
      The System Metrics Mali package is supported in Unity 2021.2 and later. Use a compatible
      Unity version before adding the package.
  - question: How do I add the System Metrics Mali package if it doesn’t appear in Package Manager?
    answer: >-
      In Unity, select **Window > Package Manager**. Select the **+** icon, choose **Add package
      by name…**, enter `com.unity.profiling.systemmetrics.mali`, and select **Add**.
  - question: How do I verify that Arm GPU hardware counters show up in the Unity Profiler?
    answer: >-
      Open the Unity Profiler and check that **Mali System Metrics** appears at the bottom of the
      profiler modules. If you don't see it, select **Profiler Modules** and enable **Mali System Metrics**.
  - question: What does the Arm Performance Studio Unity integration enable during profiling?
    answer: >-
      Use the integration to add timeline markers and custom counters to your Unity project. In
      Streamline, these annotations give performance data context. Use paired region markers to
      show regions in a Performance Advisor report.
  - question: Do I need to choose Streamline or Performance Advisor for the annotations, and how
      do I see them?
    answer: >-
      You can use the integration with both Streamline and Performance Advisor. In Streamline,
      look for markers on the timeline, expand **UnityMain** in **Core Map** for channel annotations,
      and view custom counters as timeline charts. Use region markers to view regions in Performance Advisor.
# END generated_summary_faq

author: Julie Gaskin

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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
