---
title: Enable Neural Super Sampling in Unreal Engine with ML Extensions
description: Learn how to configure ML Extensions for Vulkan emulation and enable Neural Super Sampling (NSS) in Unreal Engine for real-time upscaling.

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for developers experimenting with neural graphics using Unreal Engine® and ML Extensions for Vulkan®.

learning_objectives:
    - Understand how Arm enables neural graphics for game development
    - Configure ML extensions for Vulkan emulation
    - Enable Neural Super Sampling (NSS) in Unreal Engine
    - Run and visualize real-time upscaling with NSS

prerequisites:
    - Windows 11
    - Unreal Engine 4.27 or 5.4 or 5.6 (with the Templates and Feature Pack enabled)
    - Visual Studio (with Desktop Development with C++ and .NET desktop build tools)

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-17T22:11:27Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: f9e794dcaca9f4845b360594acd511726093e26f1f8a6f62b86f3fe2559ec8f0
  summary_generated_at: '2026-08-17T22:11:27Z'
  summary_source_hash: f9e794dcaca9f4845b360594acd511726093e26f1f8a6f62b86f3fe2559ec8f0
  faq_generated_at: '2026-08-17T22:11:27Z'
  faq_source_hash: f9e794dcaca9f4845b360594acd511726093e26f1f8a6f62b86f3fe2559ec8f0
  summary: >-
    You'll enable Arm NSS in Unreal Engine with Vulkan ML extensions on
    Windows. First, you'll install the Vulkan SDK and emulation layers, then add the Arm Neural Graphics Plugin
    and its VGF model to a C++ **Third Person** project. Then, you'll verify NSS, visualize model output, and use
    RenderDoc to investigate frames and Vulkan calls.
  faqs:
  - question: How do I know NSS is active in my level?
    answer: >-
      Run `ShowFlag.VisualizeTemporalUpscaler 1` in Unreal and check the rendering summary. You
      should see NSS listed. To hide the overview, run `ShowFlag.VisualizeTemporalUpscaler 0`.
  - question: Which Unreal Engine project template should I use for the example?
    answer: >-
      Create a new **Third Person** template project using the **C++** option. Open it in Visual Studio
      and build from source before enabling and running NSS.
  - question: How do I set up the ML emulation layers for Vulkan?
    answer: >-
      Install Vulkan SDK version 1.4.321.0 or later and the ML Emulation Layer for Vulkan version
      0.10.0 or later. Use Vulkan Configurator to set up the emulation layers used for ML extensions
      workloads.
  - question: How can I visualize the NSS model output while the game runs?
    answer: >-
      Run the command `r.NSS.Debug 1` in Unreal. The command adds real-time views showing the model output
      to help you inspect results.
  - question: When should I use RenderDoc?
    answer: >-
      Use RenderDoc when you see unexpected visual output or need to analyze a frame in detail.
      RenderDoc lets you step through a capture, inspect Vulkan API calls, and review shader inputs and
      outputs, with additional features available for Arm GPUs.
# END generated_summary_faq

author: Annie Tallund

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: ML
armips:
    - Mali
    - Immortalis
tools_software_languages:
    - Unreal Engine
    - Vulkan SDK
    - Visual Studio
    - NX
operatingsystems:
    - Windows

further_reading:
    - resource:
        title: Neural Graphics Development Kit
        link: https://developer.arm.com/mobile-graphics-and-gaming/neural-graphics
        type: website
    - resource:
        title: NSS Use Case Guide
        link: https://developer.arm.com/documentation/111009/latest/
        type: documentation
    - resource:
        title: RenderDoc for Arm GPUs
        link: https://developer.arm.com/Tools%20and%20Software/RenderDoc%20for%20Arm%20GPUs
        type: documentation
    - resource:
        title: How Arm Neural Super Sampling works
        link: https://community.arm.com/arm-community-blogs/b/mobile-graphics-and-gaming-blog/posts/how-arm-neural-super-sampling-works
        type: blog

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
