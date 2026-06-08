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

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T02:11:21Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: e6a652fd0b32796433a380012a79def743bc5452a52ffae785007977a2a8e3e0
  summary_generated_at: '2026-06-02T05:19:33Z'
  summary_source_hash: e6a652fd0b32796433a380012a79def743bc5452a52ffae785007977a2a8e3e0
  faq_generated_at: '2026-06-03T02:11:21Z'
  faq_source_hash: e6a652fd0b32796433a380012a79def743bc5452a52ffae785007977a2a8e3e0
  summary: >-
    Learn how to analyze Linux application performance on Arm Neoverse N1 using the Arm Telemetry
    Solution and Linux perf. You will build a slightly modified DynamoRIO stride benchmark, collect
    sampling and counting data, and interpret commonly used hardware metrics. Following the Telemetry
    Solution install guide, you will set up the required tools (including Python and perf) and
    use g++ to compile the example. You will then enable software prefetching with compile-time
    defines, rerun measurements, and compare results to assess the impact of the change. The steps
    target an Arm Neoverse N1 system; bare metal or cloud metal instances are recommended, and
    results vary by hardware. Estimated time: about 60 minutes.
  faqs:
  - question: Do I need a bare-metal Neoverse N1 system, or can I use a VM?
    answer: >-
      Use an Arm Neoverse N1 computer running Linux. A bare metal or cloud metal instance is best
      because they expose more counters; a VM may offer fewer counters and some commands might
      not succeed. These instructions have been tested on the a1.metal instance type.
  - question: Which tools must be installed before I build and profile the example?
    answer: >-
      Follow the Arm Telemetry Solution install guide to install the required tools on your Arm
      Neoverse server; this includes Python and Linux perf. You also need the GNU C++ compiler
      (g++), as described in the GNU Compiler install guide.
  - question: What application is used as the example, and what does it measure?
    answer: >-
      The example is the DynamoRIO stride benchmark, a pointer-chasing micro-benchmark that accesses
      values in a 16 MB array with positions determined by the chased pointers. The provided code
      is slightly modified to increase the number of iterations. The original source is at https://github.com/DynamoRIO/dynamorio/blob/master/clients/drcachesim/tests/stride_benchmark.cpp.
  - question: Can I run this Learning Path on hardware other than the N1SDP, and how will results
      differ?
    answer: >-
      Yes. The white paper uses the Neoverse N1 Software Development Platform (N1SDP), which differs
      from Neoverse N1 servers and cloud instances, so your results will be different. You can
      also run on single board computers with Cortex-A76 processors such as Raspberry Pi 5, Khadas
      Edge2, or Orange Pi 5; the example output provided is from a Khadas Edge2.
  - question: How do I enable and tune software prefetching in the sample application?
    answer: >-
      Recompile the application with two compile-time defines to enable data prefetching, as shown
      in the steps. You can experiment with values of DIST to observe performance impact; the
      white paper shows performance saturating at DIST=40 on N1SDP, but your results will vary
      by hardware.
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

