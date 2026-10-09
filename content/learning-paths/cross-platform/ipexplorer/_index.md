---
title: Run custom software for simulation with Arm IP Explorer
description: Learn how to run custom software benchmarks on IP Explorer simulation platforms and compare performance across Arm Cortex-M processors using cycle count analysis.
minutes_to_complete: 60

who_is_this_for: This is an introductory topic for IP Explorer users using the software simulation platforms available.

learning_objectives: 
    - Run a pre-installed example on IP Explorer simulation platform
    - Create your own example benchmark
    - Upload and run your benchmark 

prerequisites:
    - An Arm account that can access IP Explorer
    - (Optional) A Linux machine with the desired compilers installed

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-29T16:38:13Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 47cd598f6e33c12d3729c319a1d6a7afcd748de7acd6faea639f2e8600a085ed
  summary_generated_at: '2026-07-29T16:38:13Z'
  summary_source_hash: 47cd598f6e33c12d3729c319a1d6a7afcd748de7acd6faea639f2e8600a085ed
  faq_generated_at: '2026-07-29T16:38:13Z'
  faq_source_hash: 47cd598f6e33c12d3729c319a1d6a7afcd748de7acd6faea639f2e8600a085ed
  summary: >-
    You'll use Arm IP Explorer to run built-in and custom software on cloud-hosted simulation platforms for
    Arm Cortex-M processors. You'll launch an example to collect cycle-accurate results, edit a marked C
    source region to create a benchmark, and build a `.tgz` archive on Linux. Then, you'll upload the
    archive, choose the project and compiler, and compare cycle counts across Cortex-M instances.
  faqs:
  - question: I don’t see my Cortex-M0 or Cortex-M7 instances under Simulate Processors — what should
      I check?
    answer: >-
      Confirm that you're logged in to IP Explorer and that you created the instances in the earlier step.
      Refresh **Simulate Processors** so recently created instances appear at the top.
  - question: After uploading custom-software.tgz, I don’t see my_example in the selection list—what
      should I do?
    answer: >-
      Wait for processing to finish, then reopen the **Select/Upload Software** menu. Confirm that
      you uploaded the `.tgz` archive produced by the provided software package.
  - question: Which compiler option should I choose when starting the simulation run?
    answer: >-
      Select Arm Compiler for Embedded (AC6). Use the same compiler
      when you run your custom benchmark.
  - question: How do I know what to change in the sample project to create my benchmark?
    answer: >-
      Edit the marked sections in the provided C source file to add or modify the code you want to
      measure. Keep the project structure unchanged so the package uploads correctly.
  - question: What result should I expect from a successful run, and how do I compare processors?
    answer: >-
      A successful run produces cycle-accurate benchmark results and confirms execution on a Fast
      Models system. Run the same software on **My Cortex-M0** and **My Cortex-M7**, then compare
      the reported cycle counts.
# END generated_summary_faq

author: Ronan Synnott

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
armips:
    - Cortex-A
    - Cortex-R
    - Cortex-M
operatingsystems:
    - Baremetal
tools_software_languages:
    - IP Explorer

### Cross-platform metadata only
shared_path: true
shared_between:
    - embedded-and-microcontrollers

further_reading:
    - resource:
        title: Arm IP Explorer
        link: https://www.arm.com/products/ip-explorer
        type: website
    - resource:
        title: Login to Arm IP Explorer
        link: https://ipexplorer.arm.com/
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
