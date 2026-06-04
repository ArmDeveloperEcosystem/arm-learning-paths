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

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T00:06:38Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: e2f6f3005c119e6f6fe97612d4e2600849106f244bce729d56bfeeedb30637c2
  summary_generated_at: '2026-06-02T02:57:43Z'
  summary_source_hash: e2f6f3005c119e6f6fe97612d4e2600849106f244bce729d56bfeeedb30637c2
  faq_generated_at: '2026-06-03T00:06:38Z'
  faq_source_hash: e2f6f3005c119e6f6fe97612d4e2600849106f244bce729d56bfeeedb30637c2
  summary: >-
    Learn to analyze Android graphics workloads using Frame Advisor’s Render Graph view in Arm
    Performance Studio. You will capture GPU data with Streamline Performance Analyzer, then inspect
    the directed acyclic graph of workloads and resources to find GPU‑heavy sections, spot unused
    resources, and detect unwanted execution nodes. The path explains render graph concepts, shows
    how to generate a capture, and demonstrates actionable fixes such as removing unnecessary
    API calls. It applies to applications using OpenGL ES or Vulkan. Prerequisites include having
    Frame Advisor installed; a supported Android device is needed if you plan to analyze your
    own applications. Basic familiarity with Frame Advisor is recommended. Estimated time to complete
    is about 30 minutes on Linux, Windows, or macOS hosts.
  faqs:
  - question: What do I need before running this Learning Path?
    answer: >-
      Install Frame Advisor (part of Arm Performance Studio). If you plan to analyze your own
      applications, use a supported Android device. Basic familiarity with Frame Advisor is recommended;
      review the “Get started with Arm Performance Studio for mobile” section.
  - question: Which Streamline capture settings should I use to record GPU data for the render
      graph?
    answer: >-
      In Streamline’s Start view, open Configure Capture and enable GPU data collection. For an
      Arm GPU, deselect “Use advanced mode” and select the “Capture Arm GPU” checkbox.
  - question: What result should I expect from the Render Graph view?
    answer: >-
      You will see a directed acyclic graph of nodes and edges that summarizes GPU workloads (execution
      nodes) and resources for a single frame. It shows how data flows between passes and where
      outputs are consumed.
  - question: What should I check if the graph shows resources that are never consumed?
    answer: >-
      Identify outputs from a render or transfer node that have no downstream consumers in the
      graph. These indicate data written but not used in the frame and are candidates for review
      or removal in your application.
  - question: How do I decide whether an execution node can be removed?
    answer: >-
      If all outputs from a node are unnecessary, the computation is unnecessary and you can remove
      the corresponding API calls. Make changes carefully and verify the application after adjustments.
# END generated_summary_faq

author: Mark Thurman

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

