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

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T23:52:25Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 23df12c0e165a4120fa25b5573437121bc7af141376758ccd051ddac14e180fb
  summary_generated_at: '2026-06-02T02:48:56Z'
  summary_source_hash: 23df12c0e165a4120fa25b5573437121bc7af141376758ccd051ddac14e180fb
  faq_generated_at: '2026-06-02T23:52:25Z'
  faq_source_hash: 23df12c0e165a4120fa25b5573437121bc7af141376758ccd051ddac14e180fb
  summary: >-
    This introductory path shows how to set up Unity for Android, build and deploy a simple sample
    to a real device, and begin investigating performance with the Unity Profiler. You will install
    the latest Unity with Android Build Support, open a provided scene that includes a small C#
    script, switch the project to the Android platform, and run it on a recent Android phone or
    tablet. You then launch the Profiler in the editor and on a connected device to review CPU,
    graphics, and memory timelines and start diagnosing why a basic scene runs slowly. Prerequisites
    are basic game‑engine knowledge and a desktop capable of running Unity; the estimated time
    to complete is about 30 minutes.
  faqs:
  - question: What do I need before running this Learning Path?
    answer: >-
      You need basic knowledge of game engines and programming concepts, a recent Android device
      (phone or tablet), and a desktop computer capable of running Unity. No other explicit prerequisites
      are listed.
  - question: Which Unity components should I install to target Android?
    answer: >-
      Install the latest version of Unity and add Android Build Support. The setup step in the
      path calls out both items before you open the sample project.
  - question: How do I open and inspect the sample project and scene?
    answer: >-
      Extract the sample project from the path, open it in Unity, and double-click SampleScene
      in the Project tab. Select the Cube object to view the attached Spin.cs script.
  - question: How do I switch the project to Android and build for my device?
    answer: >-
      Open File -> Build Profile to access the window where you switch the active platform to
      Android. Then use the Build Settings workflow described in the steps to produce and deploy
      the Android build.
  - question: Should I profile in the editor or on my Android device?
    answer: >-
      Use the Unity Profiler in the editor for quick, high-level checks, then profile on your
      Android device to reflect end-user characteristics. Expect a per-frame timeline with CPU,
      graphics, and memory data when profiling is active.
# END generated_summary_faq

author: Joshua Marshall-Law

### Tags
skilllevels: Introductory
subjects: Gaming
armips:
    - Cortex
tools_software_languages:
    - Unity
    - C#
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

