---
title: Build an RTX5 RTOS application with Keil μVision

description: Learn how to create, build, and debug an RTX5 RTOS-based application using Keil μVision with CMSIS-RTOS2 API and Event Recorder for embedded Cortex-M development.

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for software developers new to RTOS development.

learning_objectives: 
    - Implement a basic RTOS-based application

prerequisites:
    - An installation of [Arm Keil MDK](/install-guides/mdk/) or [Arm Development Studio](/install-guides/armds/) (MDK recommended)
    - Some familiarity with CMSIS is assumed

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-08T15:27:02Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: f6d44eb4221b75ee0b517012be56e5f73c21a982e0ff8eaa0bb3b35b53de4050
  summary_generated_at: '2026-07-08T15:27:02Z'
  summary_source_hash: f6d44eb4221b75ee0b517012be56e5f73c21a982e0ff8eaa0bb3b35b53de4050
  faq_generated_at: '2026-07-08T15:27:02Z'
  faq_source_hash: f6d44eb4221b75ee0b517012be56e5f73c21a982e0ff8eaa0bb3b35b53de4050
  summary: >-
    You'll create a minimal RTX5 application with the CMSIS-RTOS2
    API in Keil μVision. First, you'll install the latest CMSIS packs, configure a new project, and implement
    a `main()` that initializes the system tick and starts the kernel. Then, you'll create
    an `app_main` control thread that creates additional worker threads to demonstrate basic multitasking.
    After building, you'll run on a Fixed Virtual Platform from Keil MDK, inspect scheduler state
    and thread activity using the **RTX RTOS** view, and check formatted output in the **Serial Windows > Debug (printf)** window.
    Finally, you'll configure **CMSIS-View Event Recorder** to capture runtime events and redirect `STDOUT`
    when semihosting isn't available.
  faqs:
  - question: How do I check that the required CMSIS packs are installed before creating the project?
    answer: >-
      Open the **Pack Installer** from Keil MDK and install the latest CMSIS packs. Update to the most recent versions before proceeding.
  - question: What should main() do to start RTX5, and how do I confirm the kernel is running?
    answer: >-
      `main()` sets up the SysTick using `SystemCoreClockUpdate()`, initializes the RTOS, and starts
      the kernel. In debug, open **View > Watch Windows > RTX RTOS** to see the kernel state and active
      threads.
  - question: How many threads does the example create and where are they started?
    answer: >-
      The example starts three threads from `app_main` using `osThreadNew()`. The number and names
      are arbitrary and serve to illustrate basic thread creation.
  - question: What steps build and run the project in Keil MDK, and what should I monitor during
      execution?
    answer: >-
      Save all files, click Build (`F7`), then Debug (`Ctrl+F5`) to launch the FVP. Open the RTX RTOS
      view and the **Serial Windows > Debug (printf)** window, click Run (`F5`), and observe thread
      activity and output before stopping.
  - question: When should I use Event Recorder and how do I route STDOUT to it?
    answer: >-
      Use Event Recorder when semihosting isn't supported in Keil MDK. Enable **CMSIS-View > Event
      Recorder (DAP variant)**, set **CMSIS-Compiler > STDOUT (API)** to **Event Recorder**, and enable
      **CMSIS-Compiler > Core**. In Arm Development Studio, Event Recorder and Component Viewer aren't supported.
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
