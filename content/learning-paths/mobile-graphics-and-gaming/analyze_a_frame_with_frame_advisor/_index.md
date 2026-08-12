---
title: Analyze a frame with Frame Advisor
description: Learn how to capture frame data from Android applications and analyze performance inefficiencies using Frame Advisor in Arm Performance Studio.

minutes_to_complete: 10

who_is_this_for: Android application developers who want to learn how to use Frame Advisor.

learning_objectives: 
    - Capture data from a significant frame in your Android application
    - Inspect draw calls for rendering inefficiencies
    - Use the Render Graph to analyze how the frame is constructed
    - Analyze mesh geometry for inefficiencies

prerequisites:
    - An Android device in developer mode with USB debugging enabled. These [Arm Performance Studio supported devices](https://developer.arm.com/Tools%20and%20Software/Arm%20Mobile%20Studio#Supported-Devices) have been tested internally within Arm and confirmed to work with Arm Performance Studio.
    - A debuggable build of your application built with OpenGL ES versions 2.0 to 3.2 or Vulkan versions 1.0 to 1.2 and installed on your device. For OpenGL ES applications, your device must be running Android 10 or later. For Vulkan applications, your device must be running Android 9 or later. 
    - Arm Performance Studio downloaded and installed from [Product Download Hub](https://developer.arm.com/downloads/view/MOBST-PRO0). It's supported on Windows, Linux, and macOS host platforms. For installation instructions, see the [Arm Performance Studio install guide](/install-guides/ams/).
    - Android SDK Platform tools [downloaded and installed](https://developer.android.com/studio/releases/platform-tools.html). SDK Platform tools is required for [Android Debug bridge (adb)](https://developer.android.com/studio/command-line/adb). Add the path to ADB to your `PATH` environment variable.
    - The device connected through USB and accessible through ADB. To test the connection, open a command prompt and enter the `adb devices` command.

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-05T14:50:36Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: c09f19098244d58cf869b79e004ff834bb88afb08dfdeb3ebda30aab64f7b481
  summary_generated_at: '2026-08-05T14:50:36Z'
  summary_source_hash: c09f19098244d58cf869b79e004ff834bb88afb08dfdeb3ebda30aab64f7b481
  faq_generated_at: '2026-08-05T14:50:36Z'
  faq_source_hash: c09f19098244d58cf869b79e004ff834bb88afb08dfdeb3ebda30aab64f7b481
  summary: >-
    You'll capture and analyze a representative frame with Frame Advisor in Arm Performance Studio.
    First, you'll choose the graphics API, record a problem area, and inspect render passes and draw calls
    in the Analysis view. Then, you'll use the Render Graph view to find unnecessary work. Finally, you'll use the Content Metrics view to
    locate complex geometry and navigate to its draw call in the framebuffer.
  faqs:
  - question: How do I confirm Frame Advisor sees my device and app before capturing?
    answer: >-
      Open **New Trace** and check that your device and the target application appear in the lists.
  - question: Which API setting should I choose for my application?
    answer: >-
      Select **Vulkan** for Vulkan applications and **OpenGL ES** for OpenGL ES applications. Set this
      under **API settings** before starting the capture session.
  - question: What result should I expect after I start the capture session?
    answer: >-
      After you start the session, you can play to the problem area while the application launches
      automatically on the device and captures. When analysis completes, you'll see the Frame hierarchy
      with frames, render passes, and draw calls.
  - question: How do I know which render pass produces the on-screen image?
    answer: >-
      In the **Render Graph**, follow the flow from left to right and look for the pass that outputs
      to the swapchain. That pass is the final stage that renders to the screen.
  - question: How can I find and inspect expensive geometry?
    answer: >-
      Open **Content Metrics**, choose **Draws**, and sort by the highest number of primitives to surface
      complex objects. Right-click a candidate and select **Navigate to call** to highlight it in
      the Frame hierarchy and view it in the framebuffer.
# END generated_summary_faq

author: Julie Gaskin

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
armips:
    - Mali
    - Immortalis
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
