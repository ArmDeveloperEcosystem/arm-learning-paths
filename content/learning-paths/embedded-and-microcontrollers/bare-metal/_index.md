---
title: Create an Armv8-A embedded application

description: Learn how to create, build, and run a bare-metal embedded application for Armv8-A processors using Arm Compiler for Embedded and Fixed Virtual Platforms, including basic exception handling.

minutes_to_complete: 60   

who_is_this_for: This is an introductory topic for embedded software developers new to Armv8-A processors and/or the Arm Compiler for Embedded.

learning_objectives: 
    - Create and build an example project
    - Run example on Fixed Virtual Platform (FVP)
    - Understand basic boot code and other syntax
    - Extend example to use different I/O mechanisms
    - Extend example to implement basic exception handling

prerequisites:
    - Some familiarity with embedded programming is assumed

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T22:08:50Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 6521f17d1a10ab8871d13917923f7f64320f69301b4c0c5f5b528163d3cb43c6
  summary_generated_at: '2026-06-01T21:29:37Z'
  summary_source_hash: 6521f17d1a10ab8871d13917923f7f64320f69301b4c0c5f5b528163d3cb43c6
  faq_generated_at: '2026-06-02T22:08:50Z'
  faq_source_hash: 6521f17d1a10ab8871d13917923f7f64320f69301b4c0c5f5b528163d3cb43c6
  summary: >-
    Build and run a bare-metal Armv8-A “Hello World” on a Fixed Virtual Platform, then extend
    it with minimal boot code, UART output, and basic exception handling. You will use Arm Development
    Studio or the standalone Arm Compiler for Embedded with Arm Fixed Virtual Platforms (FVP),
    targeting the FVP_Base_AEMvA model that implements four processors. The steps include creating
    a project, adding a reset handler to park secondary cores and run on one, replacing semihosting-based
    printf with PL011 UART output, and enabling asynchronous exceptions with GICv3 and a timer
    interrupt routed to EL3. Some familiarity with embedded programming is assumed. Estimated
    time to complete is about 60 minutes.
  faqs:
  - question: What tools do I need before starting?
    answer: >-
      Install Arm Development Studio and configure your license, or install Arm Compiler for Embedded
      and Arm Fixed Virtual Platforms individually. The Learning Path also references an example
      Docker image that includes these tools.
  - question: Which Fixed Virtual Platform should I use to run the example?
    answer: >-
      Use the FVP_Base_AEMvA Architecture Envelope Model. It is a generic Arm Architecture platform
      implementing 4 processors.
  - question: How do I ensure the application runs on a single core after reset?
    answer: >-
      Create a minimal reset handler at EL3 that reads MPIDR_EL1 to identify the core and parks
      all but one processor. The application then executes on the selected processor.
  - question: How do I know if printf is using semihosting and how do I redirect output?
    answer: >-
      Import the symbol __use_no_semihosting to detect or disable semihosting. Modify the code
      to send output to the PL011 UART provided by the FVP; note that semihosting uses HLT and
      would halt on real hardware without a debugger.
  - question: How are interrupts configured in the event-driven example?
    answer: >-
      Asynchronous exceptions are enabled and routed to EL3. You initialize GICv3 in gic.s and
      configure the timer as an interrupt source.
# END generated_summary_faq

author: Ronan Synnott

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
armips:
    - Cortex-A
operatingsystems:
    - Baremetal
tools_software_languages:
    - Arm Development Studio
    - Arm Compiler for Embedded
    - Arm Fast Models

further_reading:
    - resource:
        title: Arm Cortex-A Series Programmer's Guide for ARMv8-A
        link: https://developer.arm.com/documentation/den0024
        type: documentation
    - resource:
        title: Arm Compiler for Embedded User Guide
        link: https://developer.arm.com/documentation/100748
        type: documentation


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

