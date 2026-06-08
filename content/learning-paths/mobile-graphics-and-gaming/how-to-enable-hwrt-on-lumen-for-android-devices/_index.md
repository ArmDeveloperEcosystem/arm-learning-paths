---
title: How to Enable Hardware Ray Tracing on Lumen for Android Devices

minutes_to_complete: 10

who_is_this_for: This is an introductory topic for Unreal Engine developers interested in using hardware ray tracing with Lumen on Arm devices.

learning_objectives:
    - Learn about Lumen and global illumination.
    - Enable hardware ray tracing on Lumen for Arm devices.

prerequisites:
- A computer capable of running [Unreal Engine 5.3 or later version](https://www.unrealengine.com/en-US/download).
- An Android mobile device that has a Mali GPU with hardware ray tracing support.
- A USB cable to connect the mobile device to your computer.

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T23:53:37Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 3f35558e0399cb4c851b120eaa2217a63c48336cbba96d23500d1b751e4aec63
  summary_generated_at: '2026-06-02T02:49:43Z'
  summary_source_hash: 3f35558e0399cb4c851b120eaa2217a63c48336cbba96d23500d1b751e4aec63
  faq_generated_at: '2026-06-02T23:53:37Z'
  faq_source_hash: 3f35558e0399cb4c851b120eaa2217a63c48336cbba96d23500d1b751e4aec63
  summary: >-
    This introductory Learning Path guides Unreal Engine developers through enabling hardware
    ray tracing for Lumen on Android devices with Arm Mali GPUs, including those based on Immortalis-G715
    or G720. You will first review Lumen and global illumination, then configure an Unreal Engine
    5.3+ project to use Lumen for Global Illumination and Reflections. The steps cover Android-specific
    requirements for Lumen’s hardware ray tracing, including enabling the SM5 shader format (via
    Support Vulkan Desktop [Experimental]) and selecting deferred shading mode, with an option
    to enable Lumen via a Post Process Volume. Prerequisites include a computer capable of running
    Unreal Engine, an Android device with a Mali GPU that supports hardware ray tracing, and a
    USB cable.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need a computer capable of running Unreal Engine 5.3 or later, an Android mobile device
      with a Mali GPU that supports hardware ray tracing, and a USB cable to connect the device
      to your computer.
  - question: Where do I enable Lumen for Global Illumination and Reflections?
    answer: >-
      Open Project Settings, go to Engine - Rendering, and select Lumen in the Global Illumination
      section and also select Lumen in the Reflections section.
  - question: Can I enable Lumen per scene instead of project-wide?
    answer: >-
      Yes. Add a Post Process Volume actor to your scene and select Lumen in the Global Illumination
      section of the volume’s details panel.
  - question: How do I enable the SM5 shader format for Android?
    answer: >-
      In Project Settings under Platforms - Android, enable Support Vulkan Desktop (Experimental)
      to activate SM5 shader format support.
  - question: Which shading path should I choose when using Lumen?
    answer: >-
      Use deferred shading. Lumen exclusively supports deferred shading mode, which you configure
      under Engine - Rendering in Project Settings.
# END generated_summary_faq

author: Owen Wu

### Tags
skilllevels: Introductory
subjects: Gaming
armips:
    - Immortalis-G715
    - Immortalis-G720
operatingsystems:
    - Android
tools_software_languages:
    - Unreal Engine


further_reading:
    - resource:
        title: Lumen Global Illumination and Reflections
        link: https://docs.unrealengine.com/5.3/en-US/lumen-global-illumination-and-reflections-in-unreal-engine/
        type: website
    - resource:
        title: Success in mobile games with ray tracing
        link: https://developer.arm.com/community/arm-community-blogs/b/mobile-graphics-and-gaming-blog/posts/mobile-gaming-success-with-ray-tracing
        type: blog
    - resource:
        title: Arm Performance Studio 
        link: https://developer.arm.com/Tools%20and%20Software/Arm%20Performance%20Studio
        type: website



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

