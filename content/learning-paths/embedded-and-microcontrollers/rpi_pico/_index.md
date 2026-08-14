---
title: Get started with Raspberry Pi Pico

description: Setup tools and start programming with Raspberry Pi Pico

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for embedded software developers new to Raspberry Pi Pico.

learning_objectives: 
    - Install the Raspberry Pi Pico SDK.
    - Run a hello world example.
    - Measure application performance.
    - Debug applications with gdb.

prerequisites:
    - Raspberry Pi Pico board.
    - Raspberry Pi 3, 4, 400, or 5 as a development computer.

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-13T18:50:05Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: e408a86c9afbacbac3ab183c88a25e7101ac8e696e2d5023ac010a9b7764ce2a
  summary_generated_at: '2026-08-13T18:50:05Z'
  summary_source_hash: e408a86c9afbacbac3ab183c88a25e7101ac8e696e2d5023ac010a9b7764ce2a
  faq_generated_at: '2026-08-13T18:50:05Z'
  faq_source_hash: e408a86c9afbacbac3ab183c88a25e7101ac8e696e2d5023ac010a9b7764ce2a
  summary: >-
    You'll set up a Raspberry Pi Pico C and C++ development environment and debug applications on
    Cortex-M0+. First, you'll install the Pico SDK, build a hello example with CMake and GCC, and
    verify its LED and USB output. Then, you'll measure Fibonacci implementations with SysTick and
    use the Serial Wire Debug (SWD) interface to load and debug programs without BOOTSEL.
  faqs:
  - question: Which script installs the Pico SDK, and when should I run it?
    answer: >-
      Use the `pico_setup.sh` script maintained in GitHub. Run it before building the examples so
      the SDK and build files are available.
  - question: What result should I expect when I run the hello example?
    answer: >-
      The on-board LED blinks, and the program prints Hello messages over USB. Seeing both indicates
      the board and SDK setup work.
  - question: How do I know my build environment is configured correctly before moving on?
    answer: >-
      CMake configure and build complete without errors and produce binaries for the Pico. Running
      the hello program confirms the toolchain and SDK are usable.
  - question: How do I verify that SysTick is measuring cycles as intended?
    answer: >-
      Run the performance example and check the printed cycle counts. The two Fibonacci implementations
      should report different counts, showing the counter is active.
  - question: How can I load and debug Pico applications without using BOOTSEL?
    answer: >-
      Use the three-pin SWD interface. SWD lets you load and run from the command
      line and debug interactively with `gdb`.
# END generated_summary_faq

author: Jason Andrews

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
armips:
    - Cortex-M
operatingsystems:
    - Baremetal
tools_software_languages:
    - Raspberry Pi

further_reading:
    - resource:
        title: Raspberry Pi Pico SDK documentation
        link: https://raspberrypi.github.io/pico-sdk-doxygen/ 
        type: documentation
    - resource:
        title: Raspberry Pi Pico documentation
        link: https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
