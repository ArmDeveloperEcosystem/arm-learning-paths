---
title: Learn the Arm Neoverse N1 performance analysis methodology

minutes_to_complete: 60

who_is_this_for: This is an introductory topic for software developers who want to learn about performance analysis methodology for Linux applications running on Arm Neoverse.

learning_objectives:
    - Understand sampling and counting for performance analysis
    - Learn commonly used hardware metrics
    - Analyze a sample application using the Arm Telemetry Solution and Linux Perf
    - Make an application code change and see improved performance

prerequisites:
    - An Arm Neoverse N1 computer running Linux. A bare metal or cloud metal instance is best because they expose more counters. You can use a virtual machine (VM), but it may offer fewer counters and some commands might not succeed. These instructions have been tested on the `a1.metal` instance type.

generate_summary_faq: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-04-30T18:58:19Z'
  generator: template
  source_hash: e6a652fd0b32796433a380012a79def743bc5452a52ffae785007977a2a8e3e0
  summary: >-
    Learn the Arm Neoverse N1 performance analysis methodology walks you through an end-to-end
    Arm software workflow. It is designed for software developers who want to learn about performance
    analysis methodology for Linux applications running on Arm Neoverse. By the end, you will
    be able to understand sampling and counting for performance analysis, learn commonly used
    hardware metrics, and analyze a sample application using the Arm Telemetry Solution and Linux
    Perf. It focuses on tools and technologies such as perf, Telemetry, and Runbook, Linux environments,
    and Arm platforms including Neoverse. The main steps cover Introduction to performance analysis,
    Build an example application, Gather performance metrics, and Optimize the application.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will understand sampling and counting for performance analysis, learn commonly used
      hardware metrics, and analyze a sample application using the Arm Telemetry Solution and
      Linux Perf.
  - question: Who is this Learning Path for?
    answer: >-
      This is an introductory topic for software developers who want to learn about performance
      analysis methodology for Linux applications running on Arm Neoverse.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: An Arm Neoverse N1 computer running
      Linux. A bare metal or cloud metal instance is best because they expose more counters. You
      can use a virtual machine (VM), but it may offer fewer counters and some commands might
      not succeed. These instructions have been tested on the `a1.metal` instance type.
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including perf, Telemetry, and Runbook, Linux environments,
      and Arm platforms such as Neoverse.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Introduction to performance analysis, Build an example
      application, Gather performance metrics, and Optimize the application.
# END generated_summary_faq

author: Jason Andrews

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
armips:
    - Neoverse
tools_software_languages:
    - perf
    - Telemetry
    - Runbook


operatingsystems:
    - Linux

further_reading:
    - resource:
        title: "Arm Neoverse N1: Core Performance Analysis Methodology"
        link: https://armkeil.blob.core.windows.net/developer/Files/pdf/white-paper/neoverse-n1-core-performance-v2.pdf
        type: documentation
    - resource:
        title: "Arm Neoverse N1 PMU Guide"
        link: https://developer.arm.com/documentation/PJDOC-466751330-547673/r4p1/ 
        type: documentation
    - resource:
        title: "Introduction to Computer Architecture"
        link: https://www.arm.com/resources/education/education-kits/computer-architecture 
        type: book
    - resource:
        title: "Computer Architecture: A Quantitative Approach"
        link: https://www.amazon.com/Computer-Architecture-Quantitative-John-Hennessy/dp/012383872X
        type: documentation


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

