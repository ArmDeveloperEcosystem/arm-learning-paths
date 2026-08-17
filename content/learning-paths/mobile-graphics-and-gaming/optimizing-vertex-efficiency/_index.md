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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-17T22:12:48Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: b18020b78a210a88a3fb6e958110d6a5544976eeb593abfa94318126277fb946
  summary_generated_at: '2026-08-17T22:12:48Z'
  summary_source_hash: b18020b78a210a88a3fb6e958110d6a5544976eeb593abfa94318126277fb946
  faq_generated_at: '2026-08-17T22:12:48Z'
  faq_source_hash: b18020b78a210a88a3fb6e958110d6a5544976eeb593abfa94318126277fb946
  summary: >-
    You'll use Arm Frame Advisor to diagnose vertex-data efficiency on Arm GPUs. Profile a frame,
    inspect Vertex Memory Efficiency for each draw, and identify inefficient passes. Refine the
    affected vertex representation in C or C++, then profile the same scene again to compare VME
    and validate the improvement.
  faqs:
  - question: How do I find low Vertex Memory Efficiency in Arm Frame Advisor?
    answer: >-
      Open the frame analysis and review the Vertex Memory Efficiency reported for each draw call.
      Draws with low VME are the priority for investigation, as shown by the shadow map example.
  - question: Which draws should I optimize first if several show low VME?
    answer: >-
      Start with the draws that contribute to the observed performance issue in your profiling
      run. Focus on passes where Frame Advisor reports especially low VME, such as the shadow
      map draws in the example.
  - question: What changes do I make to improve VME?
    answer: >-
      Adjust the vertex representation used by the affected draws based on your understanding
      of the attributes. Then re-run Arm Frame Advisor to see whether VME increases for those
      draws.
  - question: How do I verify that a change helped?
    answer: >-
      Analyze the same scene again and compare the VME values for the same draw calls. An increase
      in VME indicates the change improved vertex efficiency.
  - question: Which tool should I use to analyze Vertex Memory Efficiency on Android?
    answer: >-
      Use Arm Frame Advisor, which reports Vertex Memory Efficiency and is part of Arm Performance
      Studio.
# END generated_summary_faq

author:
    - Andrew Kilroy
    - Peter Harris

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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
