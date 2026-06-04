---
title: Build and run the Arm Machine Learning Evaluation Kit examples

description: Learn how to build examples from the Machine Learning Evaluation Kit (MLEK) and run them on the Arm Ecosystem FVP for machine learning application development on microcontrollers.

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for embedded software developers interested in machine learning applications.

learning_objectives:
    - Build examples from Machine Learning Evaluation Kit (MLEK)
    - Run the examples on Arm Ecosystem FVP

prerequisites:
    - Some familiarity with embedded programming
    - A Linux host machine running Ubuntu

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T22:33:38Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: acf43df3c6f344b55bb413b7483d60e26d0e137489ac148bca64500e443140ab
  summary_generated_at: '2026-06-01T21:46:02Z'
  summary_source_hash: acf43df3c6f344b55bb413b7483d60e26d0e137489ac148bca64500e443140ab
  faq_generated_at: '2026-06-02T22:33:38Z'
  faq_source_hash: acf43df3c6f344b55bb413b7483d60e26d0e137489ac148bca64500e443140ab
  summary: >-
    This Learning Path shows how to build sample applications from the Arm Machine Learning Evaluation
    Kit (MLEK) and run them on an Arm Ecosystem Fixed Virtual Platform (FVP) for bare-metal ML
    development on microcontrollers. You will set up the Corstone-320 FVP, build the MLEK examples
    using a supported toolchain (such as GCC or Arm Compiler for Embedded), and locate the generated
    .axf images in the cmake-*/bin directory. You then launch an application on the FVP, selecting
    the binary with -a and configuring the Ethos-U NPU MACs using -C mps4_board.subsystem.ethosu.num_macs
    so they match the build. Targets include Cortex-M55 with Ethos-U85. Prerequisites are familiarity
    with embedded programming and an Ubuntu Linux host (20.04 or 22.04 on x86_64 recommended).
    Estimated time: about 30 minutes.
  faqs:
  - question: What do I need on my host machine before running the steps?
    answer: >-
      Use a Linux host running Ubuntu; 20.04 or 22.04 is recommended. The instructions have been
      tested on x86_64 and assume some familiarity with embedded programming.
  - question: Which FVP should I install to run the examples?
    answer: >-
      Install the Corstone-320 Ecosystem FVP on your local machine. You can download Arm Ecosystem
      FVPs from the Arm Developer website and follow the Fast Model and Fixed Virtual Platform
      install guide.
  - question: Where will the built binaries be located after compiling MLEK?
    answer: >-
      The built examples are .axf files found under a cmake-*/bin directory, which depends on
      your build configuration. An example path is similar to cmake-build-mps4-sse-320-ethos-u85-256-gnu/bin/.
  - question: How do I choose and run a specific example on the FVP?
    answer: >-
      Use the -a option to specify the application image (.axf) to load when launching the FVP.
      Configure the Ethos-U component using -C mps4_board.subsystem.ethosu.num_macs to match your
      build.
  - question: What Arm IP and reference system do these examples target?
    answer: >-
      The examples let you investigate the software stack and evaluate performance on Cortex-M55
      and Ethos-U85. They are run on Arm Corstone reference systems, such as the Corstone-320
      FVP; similar steps apply to other platforms.
# END generated_summary_faq

author: Ronan Synnott

### RS: Learning Path hidden until AWS instance updated
draft: false
cascade:
    draft: false


### Tags
skilllevels: Introductory
subjects: ML
armips:
    - Cortex-M
    - Ethos-U
    - Corstone
operatingsystems:
    - Baremetal
tools_software_languages:
    - Arm Virtual Hardware
    - FVP
    - GCC
    - Arm Compiler for Embedded

further_reading:
    - resource:
        title: ML Evaluation Kit Quick Start Guide
        link: https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/main/docs/quick_start.md
        type: documentation
    - resource:
        title: Creating ML applications for embedded devices on Arm Virtual Hardware
        link: https://devsummit.arm.com/flow/arm/devsummit22/sessions-catalog/page/sessions/session/1656589322296001Tbrk
        type: website


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

