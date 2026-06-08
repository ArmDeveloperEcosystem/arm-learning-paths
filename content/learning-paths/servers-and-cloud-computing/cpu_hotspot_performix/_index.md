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

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T00:38:16Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 58dba071f70b4f85b87b3bd27b3a7ba3ff985f80079a42e05b797a998aeaf104
  summary_generated_at: '2026-06-02T03:30:14Z'
  summary_source_hash: 58dba071f70b4f85b87b3bd27b3a7ba3ff985f80079a42e05b797a998aeaf104
  faq_generated_at: '2026-06-03T00:38:16Z'
  faq_source_hash: 58dba071f70b4f85b87b3bd27b3a7ba3ff985f80079a42e05b797a998aeaf104
  summary: >-
    This Learning Path shows how to find code hotspots in C++ applications running on Arm Linux
    systems using Arm Performix on Arm Neoverse. You will build and run a C++11 Mandelbrot example
    that generates a 1920×1080 bitmap, profile baseline performance with the Code Hotspots recipe,
    and read the resulting flame graph to identify functions that dominate CPU time. The steps
    then use those insights to focus potential improvements, such as investigating calls like
    __hypot within Mandelbrot::getIterations. This is an introductory path aimed at developers
    and performance engineers. Prerequisites are access to Arm Performix and a basic understanding
    of C++. By the end, you will be able to run the recipe and pinpoint CPU-intensive functions
    for deeper analysis.
  faqs:
  - question: Which Arm Performix feature should I run to find hotspots?
    answer: >-
      Use the Code Hotspots recipe. It samples execution and produces a flame graph that highlights
      the functions consuming the most CPU time.
  - question: What do I need before running the steps?
    answer: >-
      You need access to Arm Performix and a basic understanding of C++. The example runs on an
      Arm Linux system, as described by the Learning Path.
  - question: What do I build and what output should I expect from the example?
    answer: >-
      You will build a C++11 program that computes the Mandelbrot set and writes a 1920×1080 bitmap
      image. The source is provided so you can rebuild, profile, and relate flame graph results
      back to specific functions and loops.
  - question: How do I know profiling worked?
    answer: >-
      After running the Code Hotspots recipe, you should see a flame graph that clearly shows
      the hottest functions. In the example, __hypot appears as a hotspot invoked by Mandelbrot::getIterations.
  - question: What should I check if the image file is missing when profiling under Arm Performix?
    answer: >-
      The Learning Path notes that myplot.draw() uses a relative path (./images/green.bmp) and
      that Arm Performix launches the binary in a different location. Follow the step guidance
      to ensure the output is written to the intended directory.
# END generated_summary_faq

author: Kieran Hejmadi

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

