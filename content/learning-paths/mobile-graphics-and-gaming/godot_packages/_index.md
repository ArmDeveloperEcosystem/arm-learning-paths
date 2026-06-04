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

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T23:52:55Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 44e7b5fe3fda52267dc1957319439895293276602b1f533de5665adaf6f7cafe
  summary_generated_at: '2026-06-02T02:49:25Z'
  summary_source_hash: 44e7b5fe3fda52267dc1957319439895293276602b1f533de5665adaf6f7cafe
  faq_generated_at: '2026-06-02T23:52:55Z'
  faq_source_hash: 44e7b5fe3fda52267dc1957319439895293276602b1f533de5665adaf6f7cafe
  summary: >-
    Learn how to profile Android games built with Godot using Arm Performance Studio. You install
    the Arm Performance Studio Integration extension from the Godot Asset Library, then add annotations
    in GDScript with the PerformanceStudio class, including single markers, regions, and threaded
    channels. You visualize these annotations in Streamline and Performance Advisor to correlate
    game events with CPU and GPU activity on Arm-based Android devices, including Mali GPUs. The
    path is introductory, takes about 15 minutes, and targets Godot 4.3 or later on Windows, macOS,
    or Linux. Prerequisites include familiarity with Godot and Arm Performance Studio tools. By
    the end, you will have a project instrumented for profiling and ready to analyze with Arm’s
    tools.
  faqs:
  - question: Which Godot versions support the Arm Performance Studio extension?
    answer: >-
      The extension is compatible with Godot 4.3 and later.
  - question: How do I install the Arm Performance Studio Integration in my Godot project?
    answer: >-
      Open your project, select AssetLib, search for "Arm Performance Studio Integration," then
      double-click the result and choose Download. When prompted, you can change the install folder
      before completing the installation.
  - question: How do I add a basic marker and where will I see it?
    answer: >-
      Create an instance of the PerformanceStudio class in your script and call marker("Label").
      These markers appear on the Streamline timeline to help correlate game behavior with performance
      data.
  - question: How do I define a performance region and how is it reported?
    answer: >-
      Emit a pair of markers with labels prefixed by "Region Start <Name>" and "Region End <Name>".
      Regions appear on the frame rate analysis chart in the Performance Advisor report, with
      dedicated charts for each region at the end of the report.
  - question: When should I use channels, and what do they capture?
    answer: >-
      Use channels for threaded, duration-based annotations tied to a specific software thread.
      Define a PerformanceStudio_Channel, then add annotations with labels (and optional color)
      to trace tasks like asset loading or enemy spawning.
# END generated_summary_faq

author: Albin Bernhardsson, Julie Gaskin

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

