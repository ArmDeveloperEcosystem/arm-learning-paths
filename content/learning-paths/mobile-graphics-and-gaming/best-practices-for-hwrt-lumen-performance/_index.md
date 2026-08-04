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
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-04T22:15:15Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 51b4879c8a82a6af42bc7f5d5e96a8d6fbcac673a409a8ad25c4912435791aef
  summary_generated_at: '2026-08-04T22:15:15Z'
  summary_source_hash: 51b4879c8a82a6af42bc7f5d5e96a8d6fbcac673a409a8ad25c4912435791aef
  faq_generated_at: '2026-08-04T22:15:15Z'
  faq_source_hash: 51b4879c8a82a6af42bc7f5d5e96a8d6fbcac673a409a8ad25c4912435791aef
  summary: >-
    You tune Unreal Engine Lumen hardware ray tracing for Android devices with Arm Mali GPUs. You
    learn how acceleration structures guide ray traversal, then reduce traversal cost by excluding
    actors that do not affect
    lighting or are very small, apply instancing so repeated objects share geometry in the bottom-level
    acceleration structure, and analyze mesh overlap to tighten actor bounds. You use Unreal’s
    Ray Tracing Debug tools, including the Picker (with r.RayTracing.Debug.PickerDomain 1) and
    the Instance Overlap view, to inspect and validate changes. By the end, scenes are organized
    to build leaner acceleration structures and improve ray traversal efficiency on supported
    devices.
  faqs:
  - question: How do I decide which actors to exclude from ray tracing?
    answer: >-
      Remove actors that do not contribute to lighting and very small actors that add little and
      may introduce noise. In the actor Details panel, uncheck Visible in Ray Tracing.
  - question: How can I verify whether objects are being instanced for ray tracing?
    answer: >-
      Use Unreal’s Ray Tracing Debug Picker to inspect instancing. Run r.RayTracing.Debug.PickerDomain
      1, then use the Picker to check the instance mode for selected objects.
  - question: What should I look for in the Instance Overlap view before moving on?
    answer: >-
      Look for areas where actor bounding boxes overlap heavily. Adjust meshes or bounds to reduce
      empty space so each actor’s box is as tight as possible.
  - question: Why does removing geometry from the acceleration structure help?
    answer: >-
      Fewer primitives reduce the number of hit tests during traversal, lowering cost. Excluding
      very small actors can also reduce noise in indirect lighting.
  - question: How do I confirm an actor was removed from ray tracing after I uncheck it?
    answer: >-
      Use the Ray Tracing Debug tools to inspect the actor; excluded actors no longer participate
      in ray traversal. Re-enable it by checking Visible in Ray Tracing if needed.
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
