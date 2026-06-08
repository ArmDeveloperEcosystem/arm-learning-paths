---
title: Analyze a frame with Frame Advisor
description: Learn how to capture frame data from Android applications and analyze performance inefficiencies using Frame Advisor in Arm Performance Studio.


minutes_to_complete: 10

who_is_this_for: Android application developers who want to learn how to use Frame Advisor.

learning_objectives: 
    - Capture data from a significant frame in your application
    - Find inefficiencies in the application with Frame Advisor

prerequisites:
    - An Android device. These [devices](https://developer.arm.com/Tools%20and%20Software/Arm%20Mobile%20Studio#Supported-Devices) have been tested internally within Arm and confirmed to work with Arm Performance Studio.
    - Arm Performance Studio supports applications built with OpenGL ES versions 2.0 to 3.2 or Vulkan versions 1.0 to 1.2. For OpenGL ES applications, your device must be running Android 10 or later. For Vulkan applications, your device must be running Android 9 or later.
    - A debuggable build of your application. 
    - Download and install Arm Performance Studio from [Product Download Hub](https://developer.arm.com/downloads/view/MOBST-PRO0). It is supported on Windows, Linux, and macOS host platforms.
    - Download and install [Android SDK Platform tools](https://developer.android.com/studio/releases/platform-tools.html). Required for [Android Debug bridge (adb)](https://developer.android.com/studio/command-line/adb).

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T23:42:06Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: d5406f24ab38522b21e348ed3829ede7b1bcdce28e81ec4fddebbec280d2cb89
  summary_generated_at: '2026-06-02T02:41:30Z'
  summary_source_hash: d5406f24ab38522b21e348ed3829ede7b1bcdce28e81ec4fddebbec280d2cb89
  faq_generated_at: '2026-06-02T23:42:06Z'
  faq_source_hash: d5406f24ab38522b21e348ed3829ede7b1bcdce28e81ec4fddebbec280d2cb89
  summary: >-
    This introductory Learning Path shows how to use Frame Advisor in Arm Performance Studio to
    capture a significant frame from an Android application and analyze where time is spent. You
    will connect a supported device, start a trace from Frame Advisor, and examine the captured
    frame’s render passes and draw calls, including primitive counts. You will use the Render
    Graph to understand how data flows between passes and to spot attachments that do not contribute
    to the final output, and the Content Metrics view to identify complex meshes by sorting and
    navigating to high-primitive draw calls. Prerequisites include a debuggable build, Arm Performance
    Studio on Windows, Linux, or macOS, Android SDK Platform-tools (adb), and an Android device
    running OpenGL ES 2.0–3.2 (Android 10+) or Vulkan 1.0–1.2 (Android 9+).
  faqs:
  - question: What do I need before running Frame Advisor?
    answer: >-
      You need a supported Android device, a debuggable build of your app, Arm Performance Studio
      installed on Windows, Linux, or macOS, and Android SDK Platform Tools (adb). Frame Advisor
      supports OpenGL ES 2.0–3.2 on Android 10+ and Vulkan 1.0–1.2 on Android 9+.
  - question: How do I start a capture trace from my device?
    answer: >-
      Open Frame Advisor and choose New Trace. Select your connected device and the target application,
      switch the API to Vulkan if needed, then click Next to start the capture session; the app
      launches automatically on the device.
  - question: How do I know the capture and analysis worked?
    answer: >-
      When analysis completes, the Analysis screen appears with the Frame Hierarchy listing captured
      frames, render passes, and draw calls. You can step through draw calls to see how the scene
      is built.
  - question: Which view helps me find unused render passes or attachments?
    answer: >-
      Use the render graph. It visualizes how data flows between render passes and resources so
      you can spot passes or attachments that are not used in the final output to the swapchain.
  - question: How can I locate the most complex meshes in my scene?
    answer: >-
      Open the Content Metrics view, select Draws, and sort by the highest number of primitives
      (Prims). Right-click a top entry and choose Navigate to call to select it in the Frame Hierarchy
      and view it in the Framebuffers view.
# END generated_summary_faq

author: Julie Gaskin

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
armips:
    - Mali GPUs
    - Immortalis GPUs
tools_software_languages:
    - Frame Advisor
operatingsystems:
    - Android
   


further_reading:
    - resource:
        title: Frame Advisor user guide 
        link: https://developer.arm.com/documentation/102693/latest/
        type: documentation
    - resource:
        title: Introducing Arm Frame Advisor 
        link: https://developer.arm.com/community/arm-community-blogs/b/mobile-graphics-and-gaming-blog/posts/arm-mobile-studio-2023-5
        type: blog
    - resource:
        title: Arm Performance Studio for Mobile 
        link: https://developer.arm.com/Tools%20and%20Software/Arm%20Performance%20Studio%20for%20Mobile
        type: website



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

