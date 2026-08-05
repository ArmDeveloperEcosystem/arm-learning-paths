---
title: Optimize hardware ray tracing with Lumen on Android devices
description: Learn how to optimize hardware ray tracing with Lumen on Android devices powered by Arm Mali GPUs to maximize performance.

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for Unreal Engine developers interested in optimizing hardware ray tracing with Lumen on android devices.

learning_objectives:
    - Learn about ray tracing.
    - Understand what an acceleration structure is.
    - Learn about the best practices for getting the maximum performance of hardware ray tracing on Lumen for Arm devices.

prerequisites:
- A computer capable of running [Unreal Engine 5.3 or later version](https://www.unrealengine.com/en-US/download).
- An Android mobile device that has a Mali GPU with hardware ray tracing support.
- A USB cable to connect the mobile device to your computer.

# START generated_summary_faq

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-05T14:55:51Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 51b4879c8a82a6af42bc7f5d5e96a8d6fbcac673a409a8ad25c4912435791aef
  summary_generated_at: '2026-08-05T14:55:51Z'
  summary_source_hash: 51b4879c8a82a6af42bc7f5d5e96a8d6fbcac673a409a8ad25c4912435791aef
  faq_generated_at: '2026-08-05T14:55:51Z'
  faq_source_hash: 51b4879c8a82a6af42bc7f5d5e96a8d6fbcac673a409a8ad25c4912435791aef
  summary: >-
    You'll improve Lumen hardware ray tracing on Android devices with Arm Mali-based GPUs by refining
    acceleration-structure contents and organization. First, you'll choose which actors to include and exclude
    small contributors. Then, you'll inspect instancing with Unreal’s Ray Tracing Debug picker, and convert
    repeated objects to instanced actors. Finally, you'll check **Instance Overlap** to reduce traversal work
    while preserving the intended lighting.
  faqs:
  - question: What do I need to check before applying these optimizations?
    answer: >-
      Enable hardware ray tracing for Lumen on the target Android device as referenced in the
      prerequisite guidance. Open the Unreal Engine project and the level you plan to optimize.
  - question: How do I exclude nonessential actors from ray tracing?
    answer: >-
      Use the actor details panel and turn off ray tracing visibility for objects that do not
      affect lighting or are very small. Preview the scene to confirm that lighting quality remains
      acceptable.
  - question: How can I confirm whether repeated objects are instanced?
    answer: >-
      Run the command `r.RayTracing.Debug.PickerDomain 1` to set the picker to instance mode, then
      use **Ray Tracing Debug** and select **Picker**. Click scene elements to inspect their instancing
      status and convert repeated objects to instanced actors when possible.
  - question: What should I look for in the Instance Overlap view?
    answer: >-
      Open the **Instance Overlap** view under **Ray Tracing Debug** and look for areas showing high overlap.
      Adjust meshes and actor bounds so each bounding box contains minimal empty space and overlaps
      less with neighbors.
  - question: Why does removing small or overlapping geometry help?
    answer: >-
      You reduce hit tests because the acceleration structure stores scene geometry in a hierarchy.
      Fewer, less-overlapping bounds lower traversal work, which can improve hardware ray tracing
      efficiency.
# END generated_summary_faq

author: Owen Wu

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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
        title: Lumen Performance Guide 
        link: https://docs.unrealengine.com/5.2/en-US/lumen-performance-guide-for-unreal-engine/
        type: website
    - resource:
        title: Analyzing ray traced content with Arm Mobile Studio
        link: https://developer.arm.com/community/arm-community-blogs/b/mobile-graphics-and-gaming-blog/posts/analyzing-ray-traced-content
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
