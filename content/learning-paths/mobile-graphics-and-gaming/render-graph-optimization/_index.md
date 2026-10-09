---
title: Optimize graphics performance using Frame Advisor render graphs
description: Learn how to use Frame Advisor's Render Graph view to identify and resolve graphics performance issues in Android applications.

minutes_to_complete: 30

who_is_this_for: Mobile application developers who wish to improve graphics performance.

learning_objectives:
    - Understand Frame Advisor's Render Graph view.
    - Use the Render Graph view to identify and resolve performance issues in your application.

prerequisites:
    - Frame Advisor, part of Arm Performance Studio, installed. Refer to the [Arm Performance Studio](/install-guides/ams/) install guide. 
    - If you wish to analyze your own applications you will need a supported Android device.
    - Some basic familiarity with Frame Advisor. Review the [Frame Advisor](/learning-paths/mobile-graphics-and-gaming/ams/fa/) section in [Get started with Arm Performance Studio for mobile](/learning-paths/mobile-graphics-and-gaming/ams/).

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-21T17:27:25Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 74d1fee67b211c4f6d2dd6feb6b9171aa90f359f2a76d522e2414fa4fb391fe0
  summary_generated_at: '2026-08-21T17:27:25Z'
  summary_source_hash: 74d1fee67b211c4f6d2dd6feb6b9171aa90f359f2a76d522e2414fa4fb391fe0
  faq_generated_at: '2026-08-21T17:27:25Z'
  faq_source_hash: 74d1fee67b211c4f6d2dd6feb6b9171aa90f359f2a76d522e2414fa4fb391fe0
  summary: >-
    You'll use Arm Performance Studio and Frame Advisor render graphs to find rendering work
    that wastes GPU resources. First, you'll capture GPU data with Streamline, then capture an affected
    frame in Frame Advisor. After that, you'll interpret execution and resource nodes to find unused outputs,
    unnecessary execution nodes, oversized textures, and inefficient transfers. Finally, you'll use the
    graph and the **API Calls** view to identify code to change.
  faqs:
  - question: How do I enable GPU data collection in Streamline before generating a render graph?
    answer: >-
      Open the **Configure Capture** section of the **Start** view and configure GPU data. For
      an Arm GPU, deselect **Use advanced mode** and select **Capture Arm GPU**.
  - question: What should I look for in the **Render Graph** view to understand frame execution?
    answer: >-
      Boxes (nodes) represent execution and resources, while arrows (edges) show how data moves
      between them. Focus on how resources produced by one node are consumed by later nodes to
      trace the frame’s data flow.
  - question: How do I spot unused resources in the graph?
    answer: >-
      Look for resources produced by an execution node that don't feed into any downstream node.
      In the example, depth and stencil outputs are written but never consumed, indicating unnecessary
      work.
  - question: What should I do if an execution node produces only unused outputs?
    answer: >-
      Remove any API calls that represent that unused computation. Review the graph and code carefully
      to confirm the work is truly unused before making changes.
  - question: Why begin with Streamline before inspecting a render graph?
    answer: >-
      Streamline helps you identify which parts of the application are GPU‑heavy so you can target
      the right frames. After it's identified, generate a render graph for those frames to investigate
      specific rendering inefficiencies.
# END generated_summary_faq

author: Mark Thurman

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

further_reading:
    - resource:
        title: Frame Advisor User Guide
        link: https://developer.arm.com/documentation/102693/latest/
        type: documentation
    - resource:
        title: Arm Performance Studio
        link: https://developer.arm.com/Tools%20and%20Software/Arm%20Performance%20Studio%20for%20Mobile
        type: website
    - resource:
        title: Get started with Arm Performance Studio for mobile
        link: /learning-paths/mobile-graphics-and-gaming/ams/fa
        type: website
    - resource:
        title: Analyze a frame with Frame Advisor
        link: /learning-paths/mobile-graphics-and-gaming/analyze_a_frame_with_frame_advisor
        type: website
    - resource:
        title: Video tutorial – Capture and analyze a problem frame with Frame Advisor
        link: https://developer.arm.com/Additional%20Resources/Video%20Tutorials/Capture%20and%20analyze%20a%20problem%20frame%20with%20Frame%20Advisor
        type: website

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
armips:
    - Mali
    - Immortalis
tools_software_languages:
    - OpenGL ES
    - Vulkan
operatingsystems:
    - Linux
    - Windows
    - macOS
    - Android

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
