---
title: Write Arm Assembler functions

minutes_to_complete: 60
description: Learn how to write mixed C and assembly programs for Cortex-M microcontrollers using Keil MDK, following Arm Procedure Call Standard conventions.

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T22:01:17Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 24245102b7b6cefd0d4f67fbfaff1fb27c913de33665929ec3cb15293a1b3b51
  summary_generated_at: '2026-06-01T21:26:11Z'
  summary_source_hash: 24245102b7b6cefd0d4f67fbfaff1fb27c913de33665929ec3cb15293a1b3b51
  faq_generated_at: '2026-06-02T22:01:17Z'
  faq_source_hash: 24245102b7b6cefd0d4f67fbfaff1fb27c913de33665929ec3cb15293a1b3b51
  summary: >-
    Learn to write mixed C and assembly for Cortex-M microcontrollers using Keil MDK, following
    the Arm Procedure Call Standard. You will set up a bare-metal Cortex-M4 project either in
    Keil Studio (VS Code, CMSIS Solution) or in μVision, target the ARMCM4 device, and, in μVision,
    add CMSIS Core and Device Startup components and use the Models Cortex-M Debugger with the
    Cortex-M4 Fixed Virtual Platform. You will implement assembly subroutines (my_strcpy and my_capitalize),
    call them from C, and step through execution to understand their operation. This introductory
    path expects some familiarity with C/Assembly and an installed Keil MDK, and takes about 60
    minutes to complete.
  faqs:
  - question: Which Keil environment should I use, and what setup steps differ?
    answer: >-
      You can use Keil Studio (VS Code) or µVision. In Keil Studio, create a CMSIS Solution (csolution),
      select the ARMCM4 target, choose Blank Solution, and ensure Arm Compiler 6 is selected.
      In µVision, create a new project, select ARMCM4, and add CMSIS > Core and Device > Startup.
  - question: How do I run the example on a Cortex-M4 Fixed Virtual Platform instead of hardware?
    answer: >-
      This path uses the Cortex‑M4 FVP provided with MDK. In µVision, set the Debug option to
      Models Cortex-M Debugger and open Settings to configure it for the FVP.
  - question: How do I add the main C file in each environment?
    answer: >-
      In µVision, right‑click Source Group 1, choose Add New Item, select C file (.c), and name
      it main.c. In Keil Studio, open main.c within the Source Files group of your CMSIS Solution.
  - question: What assembly functions do I implement and how are they called?
    answer: >-
      Implement my_strcpy(const char *src, char *dst) and my_capitalize(char *str). The main C
      function creates character arrays and calls these subroutines to copy and capitalize a string.
  - question: What calling convention should the assembly subroutines follow?
    answer: >-
      Write the subroutines to conform to the Arm Procedure Call Standard, using Arm register
      calling conventions. This enables the C code to call the assembly routines as shown in the
      example.
# END generated_summary_faq

author: Ronan Synnott

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

