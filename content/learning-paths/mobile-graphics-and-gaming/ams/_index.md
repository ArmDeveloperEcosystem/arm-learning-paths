---
title: Get started with Arm Performance Studio

description: Learn how to use each of the tools supplied with Arm Performance Studio (formerly known as Arm Mobile Studio).

minutes_to_complete: 60

who_is_this_for: Android application and games developers new to Arm Performance Studio.

learning_objectives:
    - Learn the basic features of each component of Arm Performance Studio. 
    - Get started profiling and optimizing your application.

prerequisites:
    - An Android device.
    - Arm Performance Studio supports applications built with OpenGL ES versions 2.0 to 3.2, or Vulkan versions 1.0 to 1.2.
    - For OpenGL ES applications, your device must be running Android 10 or later.
    - For Vulkan applications, your device must be running Android 9 or later.
    - A debuggable build of your application. 
    - Arm Performance Studio installed. Follow the [Arm Performance Studio install guide](/install-guides/ams) for instructions.
    - Android SDK Platform tools installed. Required for the Android Debug bridge (adb).

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T23:41:00Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 3d1a743c1b3ee617f52191fc9c9fd33a9d44454ac079f00b6f532e2865103377
  summary_generated_at: '2026-06-02T02:40:50Z'
  summary_source_hash: 3d1a743c1b3ee617f52191fc9c9fd33a9d44454ac079f00b6f532e2865103377
  faq_generated_at: '2026-06-02T23:41:00Z'
  faq_source_hash: 3d1a743c1b3ee617f52191fc9c9fd33a9d44454ac079f00b6f532e2865103377
  summary: >-
    This introductory path shows Android developers how to start profiling apps on devices with
    Mali-based GPUs using Arm Performance Studio. You will install the tools, connect an Android
    device over adb, explore a provided Streamline example capture, then profile your own debuggable
    build and generate a Performance Advisor HTML report using streamline-cli. The walkthrough
    focuses on Streamline and Performance Advisor basics. Prerequisites include an Android device,
    a debuggable app using OpenGL ES 2.0–3.2 or Vulkan 1.0–1.2 (Android 10+ for OpenGL ES, Android
    9+ for Vulkan), Arm Performance Studio installed, Android SDK Platform Tools (adb), and Python
    3.8 or later for the Performance Advisor script.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need an Android device, a debuggable build of your application, Arm Performance Studio
      installed, and the Android SDK Platform Tools (adb). For Performance Advisor’s connection
      script, install Python 3.8 or later.
  - question: Which graphics APIs and Android versions are supported?
    answer: >-
      Arm Performance Studio supports OpenGL ES versions 2.0 to 3.2 and Vulkan versions 1.0 to
      1.2. For OpenGL ES applications your device must run Android 10 or later; for Vulkan applications
      your device must run Android 9 or later.
  - question: How do I connect my Android device in Streamline?
    answer: >-
      Launch the Performance Studio Hub and open Streamline, then in the Start view select Android
      (adb) and choose your device. Streamline installs the gatord daemon and connects to the
      device; if your device is not listed, check that adb from the Android SDK Platform Tools
      is installed.
  - question: How do I open the example Streamline capture?
    answer: >-
      In Streamline, select File > Import, then choose Import Streamline Sample Captures and select
      the Android example. After import, double-click the report in Streamline Data to view it.
  - question: How do I generate a Performance Advisor report from a Streamline capture?
    answer: >-
      From a terminal, navigate to the capture and run the streamline-cli command with the -pa
      option on the .apc file. The capture is processed and an HTML report is generated, with
      warnings shown where applicable.
# END generated_summary_faq

author: Ronan Synnott

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

