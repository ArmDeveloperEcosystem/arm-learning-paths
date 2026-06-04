---
title: Custom software for simulation with IP Explorer
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

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T21:43:14Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 47cd598f6e33c12d3729c319a1d6a7afcd748de7acd6faea639f2e8600a085ed
  summary_generated_at: '2026-06-01T21:08:49Z'
  summary_source_hash: 47cd598f6e33c12d3729c319a1d6a7afcd748de7acd6faea639f2e8600a085ed
  faq_generated_at: '2026-06-02T21:43:14Z'
  faq_source_hash: 47cd598f6e33c12d3729c319a1d6a7afcd748de7acd6faea639f2e8600a085ed
  summary: >-
    This introductory path shows how to use Arm IP Explorer’s cloud simulation platforms to run
    and compare custom bare-metal software benchmarks on Arm Cortex-M processors using cycle count
    analysis. You will run a pre-installed example, then clone the provided software package to
    create your own benchmark from sample C projects that highlight marked code regions. Optionally
    build and test locally on Linux using Arm GNU Toolchain or Arm Compiler for Embedded. Next,
    package your application (custom-software.tgz), upload it via the Simulate Processors workflow,
    select AC6 in the UI, and run on Cortex-M instances (for example, Cortex-M0 and Cortex-M7).
    Requires an Arm account with IP Explorer access.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need an Arm account that can access IP Explorer. Optionally, have a Linux machine with
      the desired compilers installed if you plan to build the custom benchmark locally.
  - question: How do I create and edit the custom benchmark code?
    answer: >-
      Clone the software package repository referenced in the steps, which includes sample projects.
      Use the provided C source file with a marked code region to add or modify the algorithm
      you want to benchmark.
  - question: Where do I upload my custom software in IP Explorer, and what file should I select?
    answer: >-
      In IP Explorer, go to Simulate Processors, open your Cortex-M instance, then Software Simulation,
      and click +New. From Select/Upload Software choose +New, upload the custom-software.tgz
      you created, then select the my_example project, choose AC6 (Arm Compiler for Embedded),
      and run.
  - question: How do I compare performance across different Cortex-M processors?
    answer: >-
      Run the same benchmark on multiple Cortex-M instances (for example, Cortex-M0 and Cortex-M7).
      Use the cycle-accurate data produced by the simulation to compare results across cores.
  - question: What should I check if my Cortex-M instances are not listed?
    answer: >-
      Ensure you previously created the instances under Simulate Processors in IP Explorer, as
      the steps expect them to exist. If they are missing, create the required Cortex-M instances
      before starting a new Software Simulation.
# END generated_summary_faq

author: Ronan Synnott

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

