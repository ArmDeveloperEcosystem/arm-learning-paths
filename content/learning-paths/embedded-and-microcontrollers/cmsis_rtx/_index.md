---
title: Build an RTX5 RTOS application with Keil μVision

description: Learn how to create, build, and debug an RTX5 RTOS-based application using Keil μVision with CMSIS-RTOS2 API and Event Recorder for embedded Cortex-M development.

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for software developers new to RTOS development.

learning_objectives: 
    - Implement a basic RTOS-based application

prerequisites:
    - An installation of [Arm Keil MDK](/install-guides/mdk) or [Arm Development Studio](/install-guides/armds) (MDK recommended)
    - Some familiarity with CMSIS is assumed

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T22:10:56Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: d8c73d658fa7a8051131276b8567cbd7376aac3b8f6e87c8ecdf224443c3ef99
  summary_generated_at: '2026-06-01T21:30:25Z'
  summary_source_hash: d8c73d658fa7a8051131276b8567cbd7376aac3b8f6e87c8ecdf224443c3ef99
  faq_generated_at: '2026-06-02T22:10:56Z'
  faq_source_hash: d8c73d658fa7a8051131276b8567cbd7376aac3b8f6e87c8ecdf224443c3ef99
  summary: >-
    Learn how to create, build, and debug a basic RTX5 RTOS application using Keil μVision in
    Keil MDK. You will install or update CMSIS packs, initialize RTX5 via the CMSIS-RTOS2 API
    (including SysTick setup using SystemCoreClockUpdate), implement main() and an app_main thread
    that launches three RTOS threads, then build and run the project on an FVP from within the
    IDE. You will observe RTOS activity with the RTX RTOS watch window and route printf output,
    using Event Recorder when semihosting is unavailable. The path is introductory, targets Cortex‑M
    development, and includes notes for Arm Development Studio users. Prerequisites are an installation
    of Keil MDK or Arm Development Studio (MDK recommended) and some familiarity with CMSIS.
  faqs:
  - question: What do I need installed before running the steps, and which IDE should I use?
    answer: >-
      Install Arm Keil MDK or Arm Development Studio; Keil MDK is recommended. Some familiarity
      with CMSIS is assumed. If you use Arm Keil Studio for Visual Studio Code, follow the separate
      path for Keil Studio (VS Code).
  - question: How do I install the required CMSIS components for the project?
    answer: >-
      Open the Pack Installer and install the latest CMSIS packs. The Learning Path assumes you
      use the most up-to-date CMSIS content.
  - question: Which source files do I create, and where do I add them in the project?
    answer: >-
      Create main.c and app_main.c by right-clicking the Source folder under the FVP target, choosing
      Add new item, and selecting C file (.c). main.c contains the system and RTX5 initialization;
      app_main starts and manages additional threads.
  - question: How do I build, start the FVP, and observe the RTOS during debug in Keil MDK?
    answer: >-
      Save all files, build with F7, then click Debug (Ctrl+F5) to launch the FVP and enter debug
      mode. Use View > Watch Windows > RTX RTOS to inspect RTOS features and View > Serial Windows
      > Debug (printf) for printf output. Click Run (F5) to start and Stop when finished.
  - question: How do I enable Event Recorder for printf output in Keil MDK, and when should I
      use it?
    answer: >-
      Because Keil MDK does not support semihosting here, use CMSIS-View Event Recorder for printf
      functionality. In Manage Run-Time Environment, enable CMSIS-View > Event Recorder (DAP variant),
      set CMSIS-Compiler > STDOUT (API) to Event recorder, and enable CMSIS-Compiler > Core. In
      Arm Development Studio, Event Recorder and Component Viewer are not supported, so skip this
      section.
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

