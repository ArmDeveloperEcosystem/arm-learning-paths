---
title: Profile an Android application with Arm Performance Studio

description: Profile a debuggable Android graphics application with Arm Performance Studio and analyze performance with Streamline, Performance Advisor, Frame Advisor, RenderDoc for Arm GPUs, and Mali Offline Compiler.

minutes_to_complete: 60

who_is_this_for: This is an introductory topic for Android application and games developers new to Arm Performance Studio.

learning_objectives:
    - Capture a Streamline profile from a debuggable Android application
    - Generate and inspect a Performance Advisor report
    - Capture and analyze a frame with Frame Advisor and RenderDoc for Arm GPUs
    - Use Mali Offline Compiler to estimate shader cost

prerequisites:
    - An Android device.
    - An debuggable build of your application built with OpenGL ES versions 2.0 to 3.2, or Vulkan versions 1.0 to 1.2.
    - For OpenGL ES applications, your device must be running Android 10 or later.
    - For Vulkan applications, your device must be running Android 9 or later.
    - Arm Performance Studio installed. Follow the [Arm Performance Studio install guide](/install-guides/ams/) for instructions.
    - Android SDK Platform tools installed for the Android Debug bridge (adb).

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-26T16:37:19Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 80078c6f05717cbf24c3b695a82fa15bbe477bd14a290195569dda4efe6599ee
  summary_generated_at: '2026-06-26T16:37:19Z'
  summary_source_hash: 80078c6f05717cbf24c3b695a82fa15bbe477bd14a290195569dda4efe6599ee
  faq_generated_at: '2026-06-26T16:37:19Z'
  faq_source_hash: 80078c6f05717cbf24c3b695a82fa15bbe477bd14a290195569dda4efe6599ee
  summary: >-
    You'll profile an Android graphics application on Arm
    Mali-based GPUs using Arm Performance Studio. After preparing a debuggable build, you'll
    connect an Android device over adb, explore a provided Streamline sample to understand the
    available views, then capture a profile from your own application and generate a Performance
    Advisor report with the CLI. You'll also perform frame-level inspection with Frame Advisor
    and RenderDoc for Arm GPUs, and use Mali Offline Compiler to estimate shader
    cost. By the end, you'll understand how to progress from example data to capturing on-device
    profiles and interpreting reports that inform deeper frame and shader analysis.
  faqs:
  - question: How do I launch Streamline and select my Android device?
    answer: >-
      Open the Performance Studio Hub and launch Streamline. In the Start view, choose Android
      (adb) as the device type and select your device from the list.
  - question: What should I check in my app build before profiling with Streamline?
    answer: >-
      Build a debuggable version and include options that facilitate call stack unwinding by Streamline.
      For Unity, enable Development Build in Build settings.
  - question: What steps import the example Streamline capture?
    answer: >-
      In Streamline, select File > Import, choose Import Streamline Sample Captures, then select
      the Android example and finish. The sample capture is added so you can open it and explore
      the views.
  - question: How do I generate a Performance Advisor report from a capture?
    answer: >-
      Open a terminal, navigate to the capture location, and run streamline-cli with the -pa option
      on the .apc file (for example, "Android - GPU Bound Example.apc"). The capture is processed
      and a Performance Advisor report is produced.
  - question: Do I need Python for Performance Advisor?
    answer: >-
      Yes. Performance Advisor uses a Python script to connect to your device and requires Python
      3.8 or later.
# END generated_summary_faq

author: Ronan Synnott

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
armips:
    - Cortex-A
    - Mali
    - Immortalis
operatingsystems:
    - Android
tools_software_languages:
    - Arm Performance Studio
    - Arm Mobile Studio

further_reading:
    - resource:
        title: Get started with Streamline Tutorial
        link: https://developer.arm.com/documentation/102477
        type: documentation
    - resource:
        title: Arm Streamline Performance Advisor Tutorial
        link: https://developer.arm.com/documentation/102478
        type: documentation
    - resource:
        title: Frame Advisor video tutorial
        link: https://developer.arm.com/Additional%20Resources/Video%20Tutorials/Capture%20and%20analyze%20a%20problem%20frame%20with%20Frame%20Advisor
        type: video
    - resource:
        title: Get started with Mali Offline Compiler Tutorial
        link: https://developer.arm.com/documentation/102468
        type: documentation
    - resource:
        title: Mali Offline Compiler video tutorial
        link: https://www.youtube.com/watch?v=zEybNlwd7SI
        type: website
    - resource:
        title: Optimization advice for graphics content on mobile devices
        link: https://developer.arm.com/documentation/102643
        type: documentation
    - resource:
        title: Android performance triage with Streamline
        link: https://developer.arm.com/documentation/102540
        type: documentation
    - resource:
        title: Arm GPU Best Practices Developer Guide
        link: https://developer.arm.com/documentation/101897
        type: documentation
    - resource:
        title: Integrate Arm Performance Studio into a CI workflow
        link: https://developer.arm.com/documentation/102543
        type: documentation
    - resource:
        title: RenderDoc Reference Guide
        link: https://renderdoc.org/docs/index.html
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

