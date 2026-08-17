---
title: Profile Android game performance in Godot with Arm Performance Studio

minutes_to_complete: 15

who_is_this_for: This is an introductory topic for Godot developers targeting Android devices who want to optimize game performance on Arm CPUs and Mali GPUs using Arm Performance Studio tools.

learning_objectives: 
    - Install the Arm Performance Studio Integration extension in Godot
    - Annotate your Godot game with performance markers for profiling in Streamline and Performance Advisor

prerequisites:
    - Familiarity with Godot
    - Familiarity with Arm Performance Studio tools

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-17T22:04:02Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: c655d84430d943ba1b103d12cd81cb831032d6897d1471264c2a832c17728a90
  summary_generated_at: '2026-08-17T22:04:02Z'
  summary_source_hash: c655d84430d943ba1b103d12cd81cb831032d6897d1471264c2a832c17728a90
  faq_generated_at: '2026-08-17T22:04:02Z'
  faq_source_hash: c655d84430d943ba1b103d12cd81cb831032d6897d1471264c2a832c17728a90
  summary: >-
    You'll instrument a Godot project with Arm Performance Studio Integration and profile it on
    an Arm-based Android device. Add event markers, regions, and channels to capture work across
    threads. Then inspect annotations in Streamline and use Performance Advisor charts to investigate
    frame rate, CPU, and GPU bottlenecks.
  faqs:
  - question: Which Godot versions does the Arm Performance Studio extension support?
    answer: >-
      The extension is compatible with Godot 4.3 and later.
  - question: How do I confirm the extension installed correctly in my project?
    answer: >-
      Add a script that creates PerformanceStudio.new() and call marker("Test"). If the project
      runs without script errors, the extension is available and your annotations can be captured.
  - question: What is the simplest way to add a point-in-time annotation?
    answer: >-
      Create a PerformanceStudio instance and call marker("Game Started") to emit a timestamped
      label. This appears in the Streamline timeline for correlation with performance data.
  - question: How do I define a region and where will it appear in reports?
    answer: >-
      Emit a pair of markers prefixed with "Region Start <name>" and "Region End <name>" around
      the code of interest. Performance Advisor shows these regions on the frame rate analysis
      chart and in dedicated per‑region charts.
  - question: When should I use channels instead of single markers?
    answer: >-
      Use channels to annotate durations on specific threads, such as asset loading or enemy spawning.
      Channels provide labeled spans that make it easier to trace long‑running operations alongside
      other events.
# END generated_summary_faq

author:
    - Albin Bernhardsson
    - Julie Gaskin

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
armips:
    - Cortex-A
    - Mali
tools_software_languages:
    - Godot
    - Arm Performance Studio
operatingsystems:
    - Windows
    - macOS
    - Linux

further_reading:
    - resource:
        title: Get started with Streamline 
        link: https://developer.arm.com/documentation/102477/latest/
        type: documentation
    - resource:
        title: Android performance triage with Streamline 
        link: https://developer.arm.com/documentation/102540/latest/
        type: documentation
    - resource:
        title: Get started with Performance Advisor 
        link: https://developer.arm.com/documentation/102478/latest/
        type: documentation
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
