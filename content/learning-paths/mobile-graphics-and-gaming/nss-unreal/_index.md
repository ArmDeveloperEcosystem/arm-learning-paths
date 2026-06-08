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


generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T00:00:50Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 7ffbac59b340f3ef5119d2f5ba4a786fd15d521bb294f3a4213b083c9b4ce23d
  summary_generated_at: '2026-06-02T02:54:18Z'
  summary_source_hash: 7ffbac59b340f3ef5119d2f5ba4a786fd15d521bb294f3a4213b083c9b4ce23d
  faq_generated_at: '2026-06-03T00:00:50Z'
  faq_source_hash: 7ffbac59b340f3ef5119d2f5ba4a786fd15d521bb294f3a4213b083c9b4ce23d
  summary: >-
    This Learning Path shows how to configure ML Extensions for Vulkan emulation and enable Arm
    Neural Super Sampling (NSS) in Unreal Engine on Windows 11. You will install the Vulkan SDK
    and activate the ML Emulation Layer with Vulkan Configurator, download the NSS Unreal plugin
    (including its VGF model), create a C++ Third Person template project, and run the level to
    visualize real-time upscaling. The steps explain how Arm enables neural graphics in Unreal
    and how to verify NSS using console commands and plugin settings, with optional frame capture
    in RenderDoc for analysis. Prerequisites include Windows 11, Unreal Engine 4.27 or 5.4 or
    5.6, and Visual Studio with C++ and .NET desktop build tools. Estimated time: about 30 minutes.
  faqs:
  - question: Which Unreal Engine versions should I use for this path?
    answer: >-
      The prerequisites list Unreal Engine 4.27 or 5.4 or 5.6. The Unreal Engine 5.5 plugin is
      deprecated; refer to the plugin repository documentation for details.
  - question: Do I need the Vulkan SDK, and how are the ML emulation layers enabled?
    answer: >-
      Yes. The Vulkan SDK is required to use the Vulkan Configurator, which sets up the emulation
      layers used to run ML extensions for Vulkan workloads. The Vulkan layer configuration activates
      the ML Emulation Layer so it runs with the Unreal Engine plugin.
  - question: Where do I get the NSS plugin and what does it include?
    answer: >-
      Download the latest release .zip from the Neural Super Sampling Unreal Engine Plugin GitHub
      repository. The release package contains the plugin and the VGF model file; extract it on
      your Windows machine.
  - question: How do I verify that NSS is active and view its output in Unreal?
    answer: >-
      Press Play, then run ShowFlag.VisualizeTemporalUpscaler 1 to see NSS listed in the rendering
      summary (use 0 to hide it). To visualize the model’s output in real time, run r.NSS.Debug
      1. You can also view and configure the active neural network model under Project Settings
      > Plugins > Neural Super Sampling.
  - question: When should I use RenderDoc during this workflow?
    answer: >-
      Use RenderDoc to capture and inspect frames when you see unexpected visual output or need
      to analyze the rendering sequence. It lets you step through Vulkan API calls, examine shader
      inputs/outputs, and review resource state, with additional features available for Arm GPUs.
# END generated_summary_faq

author: Annie Tallund

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

