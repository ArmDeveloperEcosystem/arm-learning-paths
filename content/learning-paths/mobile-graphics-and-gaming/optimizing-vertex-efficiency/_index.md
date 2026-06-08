---
title: Optimize graphics vertex efficiency for Arm GPUs
description: Learn how to optimize vertex representations and analyze Vertex Memory Efficiency using Arm Frame Advisor for improved GPU performance on Android.

minutes_to_complete: 10

who_is_this_for: This is an advanced topic for Android graphics application developers aiming to enhance GPU performance through smarter vertex optimization.

learning_objectives:
    - Optimize vertex representations on Arm GPUs.
    - Analyze Vertex Memory Efficiency using Arm Frame Advisor.

prerequisites:
    - Understanding of vertex attributes.
    - Familiarity with Arm Frame Advisor (part of Arm Performance Studio).

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T00:02:15Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 586a505543df4237c943ea47210d735fafe7d5ed2c6ad18b1b99227987ef9b15
  summary_generated_at: '2026-06-02T02:55:06Z'
  summary_source_hash: 586a505543df4237c943ea47210d735fafe7d5ed2c6ad18b1b99227987ef9b15
  faq_generated_at: '2026-06-03T00:02:15Z'
  faq_source_hash: 586a505543df4237c943ea47210d735fafe7d5ed2c6ad18b1b99227987ef9b15
  summary: >-
    This advanced Learning Path guides Android graphics developers through diagnosing and improving
    vertex data efficiency on Arm GPUs. Using Arm Frame Advisor (part of Arm Performance Studio),
    you will profile frames to analyze the Vertex Memory Efficiency metric, identify low-efficiency
    draw calls (for example, shadow map passes), and apply vertex representation optimizations
    in your C/C++ rendering code. The focus is on understanding what drives poor VME on Arm Immortalis
    and Mali devices and making targeted changes to reduce vertex bandwidth pressure. Prerequisites
    include knowledge of vertex attributes and familiarity with Arm Frame Advisor. Estimated time
    to complete is about 10 minutes.
  faqs:
  - question: How do I know if Vertex Memory Efficiency is low in my frame?
    answer: >-
      Profile your frame with Arm Frame Advisor and inspect the VME metric for each draw call.
      Low VME values indicate inefficient vertex data usage that warrants investigation.
  - question: What should I check if the shadow map draw calls report low VME?
    answer: >-
      Review the vertex representations and attributes used by those draw calls. The Learning
      Path guides you through approaches to address inefficiency identified by Frame Advisor.
  - question: What do I need before running the steps in this path?
    answer: >-
      You should understand vertex attributes and be familiar with Arm Frame Advisor, which is
      part of Arm Performance Studio. The content assumes an advanced level of graphics knowledge.
  - question: Which platforms and GPUs does this apply to?
    answer: >-
      The Learning Path targets Android applications running on Arm GPUs, including Arm Immortalis
      and Mali. The analysis is performed with Arm Frame Advisor.
  - question: How do I validate that my changes improved vertex efficiency?
    answer: >-
      Re-profile the frame in Arm Frame Advisor and compare VME for the affected draw calls before
      and after your changes. An increase in VME indicates improved vertex efficiency.
# END generated_summary_faq

author:
    - Andrew Kilroy
    - Peter Harris

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
armips:
    - Immortalis
    - Mali
tools_software_languages:
    - C
    - CPP
operatingsystems:
    - Android

further_reading:
    - resource:
        title: Arm GPU Best Practices Developer Guide
        link:  https://developer.arm.com/documentation/101897/0304/Vertex-shading/Attribute-layout
        type:  documentation
    - resource:
        title: Frame Advisor User Guide
        link: https://developer.arm.com/documentation/102693/latest/
        type: documentation
    - resource:
        title: Analyze a Frame with Frame Advisor
        link: /learning-paths/mobile-graphics-and-gaming/analyze_a_frame_with_frame_advisor/
        type: blog
    - resource:
        title: Arm Performance Studio
        link: https://developer.arm.com/Tools%20and%20Software/Arm%20Performance%20Studio%20for%20Mobile
        type: website
    - resource:
        title: Attribute Layouts
        link: https://developer.arm.com/documentation/101897/0304/Vertex-shading/Attribute-layout
        type: website



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

