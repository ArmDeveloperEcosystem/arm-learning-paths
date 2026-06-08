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

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T22:41:08Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: d9fe3cfc8f7a7092f40786763fc28e371697e4b57dba99b2c9b191dae4273911
  summary_generated_at: '2026-06-01T21:52:41Z'
  summary_source_hash: d9fe3cfc8f7a7092f40786763fc28e371697e4b57dba99b2c9b191dae4273911
  faq_generated_at: '2026-06-02T22:41:08Z'
  faq_source_hash: d9fe3cfc8f7a7092f40786763fc28e371697e4b57dba99b2c9b191dae4273911
  summary: >-
    This introductory path shows how to set up the Raspberry Pi Pico C/C++ SDK on a Raspberry
    Pi development computer and write bare-metal applications for the Arm Cortex-M0+ on the Pico.
    You will install the SDK using the pico_setup.sh script from GitHub, build and run a Hello
    World that prints over USB and blinks the on-board LED with GCC and CMake, measure execution
    cycles using the SysTick timer by comparing two Fibonacci implementations, and perform interactive
    debugging over SWD from the command line with gdb. Prerequisites are a Raspberry Pi Pico and
    a Raspberry Pi 3, 4, 400, or 5 as the host. The estimated time to complete is about 30 minutes.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need a Raspberry Pi Pico board and a Raspberry Pi 3, 4, 400, or 5 to use as the development
      computer. No other prerequisites are explicitly listed.
  - question: Which tools does the Pico SDK use to build applications?
    answer: >-
      The Pico SDK uses the GCC compiler and CMake to build applications. The installation script
      is provided as pico_setup.sh in GitHub.
  - question: How do I know the Hello World example worked?
    answer: >-
      The program prints “Hello” over USB and blinks the on-board LED. Seeing the repeated USB
      printout and the LED toggling confirms a successful build and run.
  - question: How can I measure the number of cycles a code section takes on the Pico?
    answer: >-
      Use the 24-bit SysTick system timer on Cortex-M0+. The example measures cycles while computing
      the Fibonacci series in two different ways and reports the counts.
  - question: How can I load and debug without pressing the BOOTSEL button each time?
    answer: >-
      Connect the three SWD debug pins on the Raspberry Pi Pico and load programs from the command
      line. You can then use gdb for interactive debugging over SWD.
# END generated_summary_faq

author: Jason Andrews

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

