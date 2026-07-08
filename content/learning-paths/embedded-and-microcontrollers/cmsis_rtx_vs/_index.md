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
    - Installation of [Arm Keil Studio for VS Code](/install-guides/keilstudio_vs/)
    - Some familiarity with CMSIS is assumed

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-08T15:27:34Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 989064eaa54dfab7f135038e3c3f0bfa932ba95512ca1dcdc36c034edf731445
  summary_generated_at: '2026-07-08T15:27:34Z'
  summary_source_hash: 989064eaa54dfab7f135038e3c3f0bfa932ba95512ca1dcdc36c034edf731445
  faq_generated_at: '2026-07-08T15:27:34Z'
  faq_source_hash: 989064eaa54dfab7f135038e3c3f0bfa932ba95512ca1dcdc36c034edf731445
  summary: >-
    You'll create, configure, and debug an RTX5-based
    application in Keil Studio for VS Code using the CMSIS-RTOS2 API. First, you'll create a CMSIS Solution
    project, select required components in the **Run-Time Environment**, and add system startup so
    RTX5 can initialize the SysTick timer with `SystemCoreClockUpdate()` before starting the scheduler.
    Then, you'll implement an `app_main` thread that launches multiple worker threads and builds
    the project using the CMSIS extension. Using the Cortex-M4 Fixed Virtual Platform as the target,
    you'll run and step through the program and verify execution by observing periodic thread
    messages printed in the **Debug Console**.
  faqs:
  - question: Which target should I use if I don’t have hardware available?
    answer: >-
      Use the Cortex-M4 Fixed Virtual Platform (FVP) referenced in the steps. The procedure also
      applies to other devices supported by CMSIS-Pack.
  - question: How do I start a debug session in Keil Studio for VS Code?
    answer: >-
      Select the **Debug** icon or open the **Run and Debug** view, then choose the configured debug connection
      to launch the FVP. Use the standard debugging controls to step through your code.
  - question: How do I know the RTOS is running correctly?
    answer: >-
      After initialization, the **Debug Console** displays messages from your threads. Look for output
      similar to: `[model] hello from thread 1/2/3`.
  - question: Where do main.c and app_main.c come from?
    answer: >-
      `main.c` is created automatically in the Source Files group when you set up the CMSIS Solution
      project. Add `app_main.c` by clicking the **+** icon in the Source Files group.
  - question: Can I change the number or names of the threads?
    answer: >-
      Yes. The number and naming of threads created by `app_main` are flexible, so adjust them to
      match your application structure.
# END generated_summary_faq

author: Ronan Synnott

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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
