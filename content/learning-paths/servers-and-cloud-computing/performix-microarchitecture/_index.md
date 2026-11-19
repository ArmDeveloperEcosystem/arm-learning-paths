---
title: Analyze CPU microarchitecture with Arm Performix

minutes_to_complete: 60

who_is_this_for: This is an introductory topic for software developers who want to learn performance analysis methodologies for Linux applications on Arm Neoverse-based servers.

learning_objectives:
    - Identify CPU pipeline bottlenecks using the Arm Performix CPU Microarchitecture recipe.
    - Analyze instruction types and SIMD utilization using the Instruction Mix recipe.
    - Optimize application performance using vectorization and compiler flags.
    - Compare performance profiles to measure execution improvements.

prerequisites:
    - An Arm Neoverse-based server running Linux, such as an Arm AGI CPU platform
    - Bare-metal server or cloud bare-metal access is preferred for hardware performance counters
    - Familiarity with Linux command line
    - Basic understanding of CPU performance concepts

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-11-18T20:22:57Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: f07c3428c4322f5dd76ed331cef7ff89c682e26a7d6c13f5f44aeb4345f64b72
  summary_generated_at: '2026-11-18T20:22:57Z'
  summary_source_hash: f07c3428c4322f5dd76ed331cef7ff89c682e26a7d6c13f5f44aeb4345f64b72
  faq_generated_at: '2026-11-18T20:22:57Z'
  faq_source_hash: f07c3428c4322f5dd76ed331cef7ff89c682e26a7d6c13f5f44aeb4345f64b72
  summary: >-
    You'll profile a C++ Mandelbrot application on an Arm Neoverse Linux system with Arm
    Performix. First, you'll build the application and connect Performix to the target. Then, you'll
    use CPU Microarchitecture results to identify latency bottlenecks, and Instruction Mix
    results to inspect Single Instruction, Multiple Data (SIMD) use. Finally, you'll change the source or compiler settings and compare
    new profiles with the baseline.
  faqs:
  - question: Which executable path should I enter when launching a recipe?
    answer: >-
      Enter the full path to your compiled C++ Mandelbrot executable on the target system. An
      absolute path helps you avoid launching a different binary.
  - question: Which option should I use for Analysis Mode in the Instruction Mix recipe?
    answer: >-
      Select **Dynamic** for **Analysis Mode** to collect the instruction categories that your
      workload runs.
  - question: How do I interpret the CPU Microarchitecture results to choose my next step?
    answer: >-
      Look for pipeline stages with the largest latency contribution. Use those results to
      choose a source or compiler change, then collect another profile to compare.
  - question: How do I know if the application uses SIMD instructions?
    answer: >-
      Check the **Instruction Mix** categories for Single Instruction, Multiple Data (SIMD) or vector instructions. If you see none,
      consider whether vectorizing the hot functions can help your workload.
  - question: How do I run the Mandelbrot generator with multiple threads?
    answer: >-
      Pass a thread-count argument to the Mandelbrot executable. If you omit it, the program
      runs with one thread. You can increase the count to compare profiles.
# END generated_summary_faq

author:
    - Brendan Long
    - Kieran Hejmadi
    - Jason Andrews

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
platforms:
    - Arm AGI CPU
armips:
    - Neoverse
tools_software_languages:
    - Arm Performix
    - C
    - Runbook

operatingsystems:
    - Linux

further_reading:
    - resource:
        title: "Find CPU Cycle Hotspots with Arm Performix"
        link: /learning-paths/servers-and-cloud-computing/cpu_hotspot_performix/
        type: documentation
    - resource:
        title: Arm Performix User Guide
        link: https://developer.arm.com/documentation/110163/latest
        type: documentation
    - resource:
        title: "Port Code to Arm Scalable Vector Extension (SVE)"
        link: /learning-paths/servers-and-cloud-computing/sve/
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

