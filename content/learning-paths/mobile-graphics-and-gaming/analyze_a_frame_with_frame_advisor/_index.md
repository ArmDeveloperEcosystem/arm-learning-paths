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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-04T22:10:25Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: c09f19098244d58cf869b79e004ff834bb88afb08dfdeb3ebda30aab64f7b481
  summary_generated_at: '2026-08-04T22:10:25Z'
  summary_source_hash: c09f19098244d58cf869b79e004ff834bb88afb08dfdeb3ebda30aab64f7b481
  faq_generated_at: '2026-08-04T22:10:25Z'
  faq_source_hash: c09f19098244d58cf869b79e004ff834bb88afb08dfdeb3ebda30aab64f7b481
  summary: >-
    You capture and analyze a single frame from an Android application using Frame Advisor in Arm
    Performance Studio. You start a new trace, select the target
    device and application, choose the correct graphics API when needed, and capture a representative
    problem frame. After analysis, you use the Frame Hierarchy to inspect render passes and
    step through draw calls to see how the scene is constructed. You use the Render Graph to visualize
    data flow and spot passes or attachments that do not contribute to the final output. You use Content
    Metrics to highlight geometry costs and navigate from high‑primitive draw calls back
    to the corresponding scene elements. By the end, you can pinpoint costly meshes and redundant
    work in a captured frame.
  faqs:
  - question: Which API setting should I use when I start a capture?
    answer: >-
      If your application uses Vulkan, change the API setting to Vulkan before starting the capture
      session. Otherwise, keep the default setting for OpenGL ES.
  - question: When should I trigger a capture to analyze a problem area?
    answer: >-
      Play the application until the problem area is about to occur, then trigger the capture
      just before it. This timing includes the relevant rendering work in the analyzed frame.
  - question: What result should I expect after a successful capture?
    answer: >-
      You should see the Analysis screen with captured frames listed in the Frame Hierarchy. From
      there, expand render passes and step through draw calls to review how the scene was built.
  - question: How do I identify complex meshes and jump to their draw calls?
    answer: >-
      Open Content Metrics, select Draws, and sort by the highest number of primitives to find
      the most complex objects. Right‑click a draw and choose Navigate to call to select it in
      the Frame Hierarchy and view it in the Framebuffers view.
  - question: What should I look for in the Render Graph?
    answer: >-
      Use the Render Graph to follow data flow across render passes and resources. Look for passes
      and input or output attachments that do not contribute to the final output; the final pass
      outputs to the swapchain.
# END generated_summary_faq

author: Julie Gaskin

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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
