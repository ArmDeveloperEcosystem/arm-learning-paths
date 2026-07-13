---
title: Write Arm Assembler functions

minutes_to_complete: 60
description: Learn how to write mixed C and assembly programs for Cortex-M microcontrollers using Keil MDK, following Arm Procedure Call Standard conventions.

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-08T15:21:04Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 24245102b7b6cefd0d4f67fbfaff1fb27c913de33665929ec3cb15293a1b3b51
  summary_generated_at: '2026-07-08T15:21:04Z'
  summary_source_hash: 24245102b7b6cefd0d4f67fbfaff1fb27c913de33665929ec3cb15293a1b3b51
  faq_generated_at: '2026-07-08T15:21:04Z'
  faq_source_hash: 24245102b7b6cefd0d4f67fbfaff1fb27c913de33665929ec3cb15293a1b3b51
  summary: >-
    You'll build a small mixed C and assembly program for
    Cortex-M using Keil MDK. First, you'll set up a project in either Keil Studio (VS Code) or μVision for
    the `ARMCM4` target, add CMSIS core and startup components where required, and configure the
    Cortex-M4 Fixed Virtual Platform as the debug target. Then, you'll write
    two assembly subroutines for string copy and capitalization, called from a C `main()` function,
    while following the Arm Procedure Call Standard. By stepping through the program in the debugger,
    you'll observe register use and memory updates and verify that the destination buffer reflects
    the copied and capitalized string.
  faqs:
  - question: Do I need a physical board to run the examples?
    answer: >-
      No. The steps use the Cortex-M4 Fixed Virtual Platform provided with MDK, so you can run
      and debug without hardware.
  - question: Which target device should I select when creating the project?
    answer: >-
      Select **ARMCM4** as the target device. This applies to both Keil Studio (VS Code) and μVision.
  - question: How do I configure debugging to use the Fixed Virtual Platform in μVision?
    answer: >-
      Open **Options for Target**, go to the **Debug** tab, and select **Models Cortex-M Debugger**. Use this
      configuration to run on the Cortex-M4 FVP.
  - question: Which components do I add when setting up the μVision project?
    answer: >-
      Add **CMSIS > Core and Device > Startup** when prompted for software components. This prepares
      the project for the ARMCM4 device and startup sequence.
  - question: What result should I expect when the C and assembly functions run correctly?
    answer: >-
      The destination buffer contains a copy of the source string, and the capitalization routine
      updates characters as intended. Step through the code to observe register usage and memory
      changes that match these operations.
# END generated_summary_faq

author: Ronan Synnott

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

who_is_this_for: This is an introductory topic for software developers who are interested in programming microcontrollers with C/Assembly.

learning_objectives: 
    - Write a mixed C program and assembly language subroutines for the microcontroller. 
    - Call the subroutines written in assembly in a C function.  
    - Use Arm register calling conventions when writing subroutines in assembly language.  
    - Step through the code to understand operation.

prerequisites:
    - Some familiarity with C/Assembly.
    - An installation of Keil MDK

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
armips:
    - Cortex-M
operatingsystems:
    - Baremetal
tools_software_languages:
    - Keil MDK

further_reading:
    - resource:
        title: Efficient Embedded Education Kit
        link: https://github.com/arm-university/Efficient-Embedded-Systems-Design-Education-Kit
        type: website

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # Indicates this should be surfaced when looking for related content. Only set for _index.md of learning path content.
# ================================================================================
---
