---
title: Optimize application performance using Arm Performix CPU microarchitecture analysis


minutes_to_complete: 60

who_is_this_for: This is an introductory topic for software developers who want to learn performance analysis methodologies for Linux applications on Arm Neoverse-based servers.

learning_objectives:
    - Identify CPU pipeline bottlenecks using the Arm Performix CPU Microarchitecture recipe
    - Analyze instruction types and SIMD utilization using the Instruction Mix recipe
    - Optimize application performance using vectorization and compiler flags
    - Compare performance profiles to measure execution improvements

prerequisites:
    - An Arm Neoverse-based server running Linux (bare-metal or cloud bare-metal instance preferred for access to hardware performance counters)
    - Familiarity with Linux command line
    - Basic understanding of CPU performance concepts

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T01:47:08Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: ec027f6022cc86a644a71a7d2016bf4601e2c4ac41570e861e9f124468b228ae
  summary_generated_at: '2026-06-02T04:47:05Z'
  summary_source_hash: ec027f6022cc86a644a71a7d2016bf4601e2c4ac41570e861e9f124468b228ae
  faq_generated_at: '2026-06-03T01:47:08Z'
  faq_source_hash: ec027f6022cc86a644a71a7d2016bf4601e2c4ac41570e861e9f124468b228ae
  summary: >-
    Analyze and improve a Linux application’s performance on Arm Neoverse-based servers using
    Arm Performix Runbook. You will configure a Performix connection, build a C Mandelbrot set
    generator, then run the CPU Microarchitecture recipe to identify pipeline bottlenecks and
    the Instruction Mix recipe to examine instruction types and SIMD utilization. Using these
    insights, apply vectorization and compiler flags and compare performance profiles to measure
    execution changes. Target environment: an Arm Neoverse server running Linux, with bare-metal
    or cloud bare-metal preferred for access to hardware performance counters. This introductory
    path assumes familiarity with the Linux command line and basic CPU performance concepts and
    is designed to be completed in about 60 minutes.
  faqs:
  - question: What do I need before running this Learning Path?
    answer: >-
      You need a Linux system on an Arm Neoverse-based server, with bare-metal or cloud bare-metal
      access preferred for hardware performance counters. You should be comfortable with the Linux
      command line and have a basic understanding of CPU performance concepts.
  - question: How do I know the sample Mandelbrot application built and runs correctly?
    answer: >-
      The program generates a 1920×1080 bitmap image of the fractal when it runs successfully.
      Use this output as a quick validation before launching Arm Performix analyses.
  - question: Which option should I select for the Instruction Mix recipe?
    answer: >-
      Choose Dynamic for the Analysis Mode. This path uses the Dynamic mode to report instruction
      types and SIMD utilization.
  - question: What should I look for in the CPU Microarchitecture recipe results?
    answer: >-
      Identify which instruction pipeline stages dominate program latency. Use those findings
      to focus subsequent changes on the most impactful bottlenecks.
  - question: How do I confirm whether my workload is using SIMD, and what if it isn’t?
    answer: >-
      Run the Instruction Mix recipe and review the SIMD utilization alongside the integer and
      floating-point instruction counts. If SIMD usage is absent, proceed with vectorization and
      appropriate compiler flags, then compare performance profiles to measure the effect.
# END generated_summary_faq

author:
- Brendan Long
- Kieran Hejmadi
- Jason Andrews

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
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

