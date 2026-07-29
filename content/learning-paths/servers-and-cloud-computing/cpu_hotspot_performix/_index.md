---
title: Find Code Hotspots with Arm Performix
description: Learn how to profile and identify CPU hotspots in C++ applications on Arm Neoverse using Arm Performix flame graphs to guide optimization.

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for software developers and performance engineers who want to identify code hotspots in applications running on Arm Linux systems.

learning_objectives: 
    - Run the Code Hotspots recipe in Arm Performix
    - Identify which functions consume the most CPU cycles and target them for optimization

prerequisites:
    - Access to Arm Performix
    - Basic understanding of C++

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-27T18:46:41Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 58dba071f70b4f85b87b3bd27b3a7ba3ff985f80079a42e05b797a998aeaf104
  summary_generated_at: '2026-07-27T18:46:41Z'
  summary_source_hash: 58dba071f70b4f85b87b3bd27b3a7ba3ff985f80079a42e05b797a998aeaf104
  faq_generated_at: '2026-07-27T18:46:41Z'
  faq_source_hash: 58dba071f70b4f85b87b3bd27b3a7ba3ff985f80079a42e05b797a998aeaf104
  summary: >-
    You'll profile a C++ Mandelbrot renderer on Arm Neoverse with Arm Performix and use flame graphs
    to find hot code. You'll build the 1920×1080 bitmap example, capture a Code Hotspots baseline,
    connect hot functions to source and call paths, edit the hottest loops, and profile it again.
    By the end, you'll use flame graph evidence to target optimization work.
  faqs:
  - question: What result should I expect after running the Code Hotspots recipe?
    answer: >-
      Expect a flame graph that highlights the hottest functions in the run. The Mandelbrot example
      typically surfaces `Mandelbrot::getIterations` and its `__hypot` call path in the stack if they
      dominate CPU time.
  - question: Where is the output bitmap written when running under Arm Performix?
    answer: >-
      The code writes to the relative path `./images/green.bmp`. Confirm the working directory used
      by Arm Performix so the image appears where you expect, or adjust the path in the code.
  - question: Which source file shows the baseline program flow I should compare against?
    answer: >-
      Open `src/main_single_thread.cpp`. It drives the Mandelbrot computation that generates the
      1920×1080 bitmap used for profiling.
  - question: How do I read the flame graph to decide what to change first?
    answer: >-
      Wider frames represent more sampled CPU time. Start with the widest frames near the top
      of the stack and trace down the call path to find the exact functions to modify.
  - question: How do I validate that my changes improved the hot path?
    answer: >-
      Rebuild the program and run the Code Hotspots recipe again. Compare the new flame graph
      to the baseline; a reduction in the previous hotspot’s width indicates the change had an
      effect.
# END generated_summary_faq

author: Kieran Hejmadi

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
armips:
    - Neoverse
tools_software_languages:
    - Arm Performix
    - C++
    - Runbook
operatingsystems:
    - Linux

further_reading:
    - resource:
        title: Optimize application performance using Arm Performix CPU microarchitecture analysis
        link: /learning-paths/servers-and-cloud-computing/performix-microarchitecture/
        type: documentation
    - resource:
        title: Arm Performix User Guide
        link: https://developer.arm.com/documentation/110163/latest
        type: documentation
    - resource:
        title: Flame Graphs 
        link: https://www.brendangregg.com/flamegraphs.html
        type: blog

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
