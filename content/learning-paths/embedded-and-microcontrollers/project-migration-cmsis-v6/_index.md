---
title: Migrating Projects to CMSIS v6

description: Learn how to migrate CMSIS v5 projects to CMSIS v6 by identifying supported toolchains, installing required CMSIS-Packs, and selecting the necessary software components.

minutes_to_complete: 10

who_is_this_for: This is an advanced topic for embedded developers who want to migrate their projects to CMSIS v6.

learning_objectives: 
    - Identify the supported toolchains.
    - Install the required CMSIS-Packs.
    - Select the software components needed to migrate your projects to CMSIS v6.

prerequisites:
    - A CMSIS v5 based project.
    - A basic understanding of the CMSIS-Pack system.

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-12T20:14:54Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 5130291152d14cd1883221f160de8ef3a3295872220a7d1f985ba032011eeaf5
  summary_generated_at: '2026-08-12T20:14:54Z'
  summary_source_hash: 5130291152d14cd1883221f160de8ef3a3295872220a7d1f985ba032011eeaf5
  faq_generated_at: '2026-08-12T20:14:54Z'
  faq_source_hash: 5130291152d14cd1883221f160de8ef3a3295872220a7d1f985ba032011eeaf5
  summary: >-
    You'll migrate an existing CMSIS v5 project to CMSIS v6 by aligning its toolchain, packs, and
    device selection. First, you'll replace deprecated packs, map generic devices to Cortex_DFP equivalents,
    and convert Keil MDK `uvprojx` projects to Open-CMSIS-Pack `csolution` format. Then, you'll diagnose
    missing devices, unresolved RTE components, and linker warnings during migration.
  faqs:
  - question: How do I confirm my toolchain is supported?
    answer: >-
      Check your versions against the supported list: Arm Compiler for Embedded v6 and later,
      Arm GNU Toolchain v12 and later, LLVM v16 and later, or IAR Embedded Workbench for Arm v9.30
      and later. Use the [Arm Compiler for Embedded Migration and Compatibility Guide](https://developer.arm.com/documentation/100068/latest/Migrating-from-Arm-Compiler-5-to-Arm-Compiler-for-Embedded-6) to move from v5 to v6.
  - question: Which CMSIS-Packs do I need when migrating from CMSIS v5?
    answer: >-
      Install `ARM.CMSIS.6.0.0.pack`, `ARM.Cortex_DFP.1.0.0.pack`, and `ARM.CMSIS-RTX.5.8.0.pack`.
      These replace the `ARM.CMSIS.5.x.x` pack during migration to CMSIS v6.
  - question: I used the Keil.ARM_Compiler pack—what should I install now?
    answer: >-
      Install `ARM.CMSIS-View.1.1.0.pack` and `ARM.CMSIS_Compiler.2.0`. These packs contain the content
      that moved from the deprecated `Keil.ARM_Compiler` pack.
  - question: How do I resolve a missing device after migration?
    answer: >-
      Change the device selection from the CMSIS v5 generic device to the corresponding device
      in the `Cortex_DFP` pack. Use the included device mapping table to select the matching
      `ARMCMx` variant and features.
  - question: Where can I find instructions for converting a `uvprojx` project?
    answer: >-
      For instructions, see the [Convert uvprojx-based projects to csolution](/learning-paths/embedded-and-microcontrollers/uvprojx-conversion/) Learning Path. It covers
      importing, converting, and building `uvprojx` projects in Keil Studio for VS Code and on
      the command line.
# END generated_summary_faq

author: Christopher Seidl

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
subjects: Libraries
armips:
    - Cortex-M
tools_software_languages:
    - CMSIS
    - CMSIS-Toolbox
operatingsystems:
    - Baremetal
    - RTOS

further_reading:
    - resource:
        title: Keil Studio User's Guide
        link: https://developer.arm.com/documentation/108029/latest/
        type: documentation
    - resource:
        title: Introducing Keil MDK Version 6
        link: https://community.arm.com/arm-community-blogs/b/internet-of-things-blog/posts/keil-mdk-version-6
        type: blog
    - resource:
        title: keil.arm.com
        link: https://keil.arm.com
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
