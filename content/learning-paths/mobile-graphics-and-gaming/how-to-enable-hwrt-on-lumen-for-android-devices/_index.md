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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-17T22:04:33Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: edbabf8c8f6e7feb8df5a6e818febd4027876aca00e33215b20b19c71d285c0b
  summary_generated_at: '2026-08-17T22:04:33Z'
  summary_source_hash: edbabf8c8f6e7feb8df5a6e818febd4027876aca00e33215b20b19c71d285c0b
  faq_generated_at: '2026-08-17T22:04:33Z'
  faq_source_hash: edbabf8c8f6e7feb8df5a6e818febd4027876aca00e33215b20b19c71d285c0b
  summary: >-
    You'll enable Unreal Engine Lumen with hardware ray tracing on supported Android devices. Configure
    Lumen for global illumination and reflections, enable the SM5 shader format through Vulkan Desktop,
    and use deferred shading. Then toggle Lumen in the project or a Post Process Volume and compare
    its lighting and reflections with non-Lumen rendering.
  faqs:
  - question: Do I need to set Lumen for both Global Illumination and Reflections?
    answer: >-
      Yes. Open Project Settings > Engine - Rendering and select Lumen in the Global Illumination
      section and again in the Reflections section.
  - question: On Android, which option enables the SM5 shader format required by Lumen?
    answer: >-
      In Project Settings under Platforms - Android, enable Support Vulkan Desktop [Experimental].
      This activates SM5 for the Android target.
  - question: Which shading mode should I use with Lumen?
    answer: >-
      Use deferred shading. Go to Project Settings > Engine - Rendering and select deferred shading;
      ensure non-deferred options are not active.
  - question: Can I enable Lumen per scene instead of project-wide?
    answer: >-
      Yes. Add a Post Process Volume actor and choose Lumen in the Global Illumination sections
      in its Details panel.
  - question: What should I check if my Android build looks unchanged after enabling Lumen?
    answer: >-
      Confirm SM5 is enabled by turning on Support Vulkan Desktop [Experimental] and that deferred
      shading is selected. Also verify the device has a Mali GPU with hardware ray tracing support.
# END generated_summary_faq

author: Owen Wu

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Gaming
armips:
    - Immortalis
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
