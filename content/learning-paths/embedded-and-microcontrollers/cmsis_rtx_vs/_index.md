---
title: Build an RTX5 RTOS application with Keil Studio (VS Code)

description: Learn how to create, configure, and debug an RTX5 RTOS application using Keil Studio for VS Code with CMSIS-RTOS2 API for embedded Cortex-M development.

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for software developers new to RTOS development.

learning_objectives: 
    - Understand the basics of RTX-based RTOS application development
    - Configure and manage an RTOS project in Keil Studio, including defining the memory map, selecting software components, and setting up debugging configurations for Cortex-M processors
    - Create and manage multiple threads within an RTX5 RTOS application

prerequisites:
    - Installation of [Arm Keil Studio for VS Code](/install-guides/keilstudio_vs)
    - Some familiarity with CMSIS is assumed

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T22:11:43Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: f4d1ab3448590c5654e2479937c9eec3e378d05229b29a45b8675139f40ac177
  summary_generated_at: '2026-06-01T21:30:42Z'
  summary_source_hash: f4d1ab3448590c5654e2479937c9eec3e378d05229b29a45b8675139f40ac177
  faq_generated_at: '2026-06-02T22:11:43Z'
  faq_source_hash: f4d1ab3448590c5654e2479937c9eec3e378d05229b29a45b8675139f40ac177
  summary: >-
    Learn to create, configure, and debug a basic RTX5 RTOS application for Arm Cortex-M using
    Keil Studio for VS Code and the CMSIS-RTOS2 API. You will set up a new csolution project,
    configure the Run-Time Environment (including C Startup), initialize the kernel by setting
    up SysTick with SystemCoreClockUpdate(), and implement an app_main thread that creates multiple
    RTOS threads. The steps target the supplied Cortex-M4 Fixed Virtual Platform (FVP), with build
    and debug driven from the VS Code environment. By the end, you can build, run, and observe
    thread output in the Debug Console. Prerequisites are installation of Arm Keil Studio for
    VS Code and some familiarity with CMSIS.
  faqs:
  - question: What do I need before running this Learning Path?
    answer: >-
      Install Arm Keil Studio for VS Code. Some familiarity with CMSIS is assumed.
  - question: Which target does this use, and can I run it on other hardware?
    answer: >-
      The steps are written for the supplied Cortex-M4 Fixed Virtual Platform (FVP). You can also
      run the project on other devices supported by CMSIS-Pack.
  - question: What project should I create and what initial setup is required?
    answer: >-
      Create a csolution project in Keil Studio for VS Code. When configuring the project's Run-Time
      Environment, add the system initialization code (C Startup).
  - question: How do I set up the OS and create threads?
    answer: >-
      Configure the SysTick timer using SystemCoreClockUpdate(), then initialize and start RTX5.
      Implement app_main to create threads with the CMSIS-RTOS2 API (the example uses three threads,
      but the number and names are flexible).
  - question: How do I build, debug, and verify that it works?
    answer: >-
      In the CMSIS Extension view, save your files and click the hammer icon to build. Start debugging
      with the Debug icon or the Run and Debug view, select your configured debug connection to
      launch the FVP, and expect to see thread messages printed in the Debug Console once the
      OS is initialized.
# END generated_summary_faq

author: Ronan Synnott

### Tags
skilllevels: Introductory
subjects: RTOS Fundamentals
armips:
    - Cortex-M
operatingsystems:
    - RTOS
tools_software_languages:
    - Keil RTX RTOS
    - Keil MDK
    - Arm Development Studio

further_reading:
    - resource:
        title: CMSIS-RTOS2 Documentation
        link: https://www.keil.com/pack/doc/CMSIS/RTOS2/html/index.html
        type: documentation
    - resource:
        title: Event Recorder and Component Viewer
        link: https://www.keil.com/pack/doc/compiler/EventRecorder/html/index.html
        type: documentation


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

