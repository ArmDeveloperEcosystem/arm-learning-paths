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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-08T15:25:42Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 6521f17d1a10ab8871d13917923f7f64320f69301b4c0c5f5b528163d3cb43c6
  summary_generated_at: '2026-07-08T15:25:42Z'
  summary_source_hash: 6521f17d1a10ab8871d13917923f7f64320f69301b4c0c5f5b528163d3cb43c6
  faq_generated_at: '2026-07-08T15:25:42Z'
  faq_source_hash: 6521f17d1a10ab8871d13917923f7f64320f69301b4c0c5f5b528163d3cb43c6
  summary: >-
    You'll create a bare‑metal Armv8‑A application, build
    it with Arm Compiler for Embedded, and run it on the `FVP_Base_AEMvA` model. After bringing
    up a Hello World example that uses semihosting for `printf`, you'll replace that mechanism by retargeting
    output to the PL011 UART provided by the Fixed Virtual Platform. You'll add a minimal EL3 reset handler
    to boot only one processor and place the remaining cores into sleep. You'll then
    introduce basic exception handling by routing exceptions to EL3 and configuring the Generic
    Interrupt Controller (GICv3) with a timer as an interrupt source, enabling a simple event‑driven
    workflow that you can observe on the model.
  faqs:
  - question: Which Arm tools should I install to follow the steps?
    answer: >-
      You can use Arm Development Studio with a configured license, or install Arm Compiler for
      Embedded and Arm Fixed Virtual Platforms (FVP) individually. The examples run on an FVP
      model.
  - question: Which Fixed Virtual Platform should I use, and how many CPUs does it provide?
    answer: >-
      Use the FVP_Base_AEMvA Architecture Envelope Model. It's a generic Arm Architecture platform
      that implements four processors.
  - question: How do I confirm that printf isn't using semihosting before switching to the UART?
    answer: >-
      Import `symbol __use_no_semihosting` in `hello.c`. If your build or run depends on semihosting,
      this exposes the dependency and prompts you to retarget `printf` to the PL011 UART on the
      FVP.
  - question: What should I expect after adding the reset handler?
    answer: >-
      The minimal reset handler puts all but one processor to sleep and runs the application on
      a single processor. This ensures the rest of the example executes on one core.
  - question: How do I know my interrupt setup is working?
    answer: >-
      Exceptions are routed to EL3 and GICv3 is initialized with the timer as an interrupt source.
      When the timer triggers, your handler is invoked, demonstrating the event‑driven flow.
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
