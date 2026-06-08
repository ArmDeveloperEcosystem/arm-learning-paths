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

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T23:47:45Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: ef70ed2089132df657bd1ebfb9a66a39934d8a118b1e73974148ce11c104fef5
  summary_generated_at: '2026-06-02T02:45:10Z'
  summary_source_hash: ef70ed2089132df657bd1ebfb9a66a39934d8a118b1e73974148ce11c104fef5
  faq_generated_at: '2026-06-02T23:47:45Z'
  faq_source_hash: ef70ed2089132df657bd1ebfb9a66a39934d8a118b1e73974148ce11c104fef5
  summary: >-
    This introductory Learning Path shows Unreal Engine developers how to improve hardware ray
    tracing with Lumen on Android devices powered by Arm Mali GPUs, including Immortalis series.
    In approximately 30 minutes, you learn the basics of ray tracing and acceleration structures,
    then apply best practices in Unreal Engine 5.3 or later to get the most from Lumen on Arm
    devices. You will trim the acceleration structure by excluding non‑contributing and very small
    actors, use instancing so BLAS data is shared, and minimize mesh overlap. The path uses Unreal
    Editor Ray Tracing Debug tools such as the Instance Overlap view and r.RayTracing.Debug.PickerDomain
    to inspect changes. Prerequisites are a machine that can run Unreal Engine 5.3+, an Android
    device with hardware ray tracing on a Mali GPU, and a USB cable.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need a computer capable of running Unreal Engine 5.3 or later, an Android device with
      a Mali GPU that supports hardware ray tracing, and a USB cable to connect the device to
      your computer. No other prerequisites are explicitly listed.
  - question: Should I enable Lumen hardware ray tracing before following these optimizations?
    answer: >-
      If you are not familiar with Lumen and global illumination, review the guidance on enabling
      hardware ray tracing for Lumen on Android devices before proceeding. This path focuses on
      optimization once hardware ray tracing is available.
  - question: How do I exclude actors that don’t help lighting from ray tracing?
    answer: >-
      In Unreal Editor, use the actor details panel to turn off the appropriate ray tracing visibility
      for objects that do not contribute to lighting and for very small actors. This reduces geometry
      in the acceleration structure and can cut noise in indirect lighting.
  - question: How can I check and use instancing to improve efficiency?
    answer: >-
      Instanced actors share geometry in the BLAS, reducing memory and improving cache behavior.
      To inspect instancing, run the command r.RayTracing.Debug.PickerDomain 1 and use the Ray
      Tracing Debug Picker in the Unreal Editor.
  - question: How do I identify and reduce mesh overlap in the acceleration structure?
    answer: >-
      Open the Instance Overlap view under Ray Tracing Debug to visualize overlap in your level.
      Aim for tight actor bounding boxes with minimal empty space to lower traversal cost.
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

