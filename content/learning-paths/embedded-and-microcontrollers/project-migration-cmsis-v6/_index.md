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

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T22:37:32Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 7a192506fc8a15423d1257fe92e7655053e38be85aad8310dae29602e483fbba
  summary_generated_at: '2026-06-01T21:48:57Z'
  summary_source_hash: 7a192506fc8a15423d1257fe92e7655053e38be85aad8310dae29602e483fbba
  faq_generated_at: '2026-06-02T22:37:32Z'
  faq_source_hash: 7a192506fc8a15423d1257fe92e7655053e38be85aad8310dae29602e483fbba
  summary: >-
    Learn how to migrate CMSIS v5 projects to CMSIS v6 for Cortex-M targets on bare-metal or RTOS.
    Verify your toolchain (Arm Compiler for Embedded v6+, Arm GNU Toolchain v12+, LLVM v16+, or
    IAR Embedded Workbench for Arm v9.30+; Arm Compiler v5 is not supported), install the required
    CMSIS-Packs (ARM.CMSIS.6.0.0, ARM.Cortex_DFP.1.0.0, ARM.CMSIS-RTX.5.8.0), and update device
    selection using the Cortex_DFP mappings. If your project used Keil.ARM_Compiler, install ARM.CMSIS-View.1.1.0
    and ARM.CMSIS_Compiler.2.0. A troubleshooting section addresses common issues including missing
    devices, RTE component errors, linker messages, and RTX5 runtime problems. Prerequisites:
    a CMSIS v5 project and basic CMSIS-Pack knowledge.
  faqs:
  - question: Which toolchain versions are supported for CMSIS v6?
    answer: >-
      Use one of the following: Arm Compiler for Embedded v6 and above, Arm GNU Toolchain v12
      and above, LLVM Toolchain v16 and above, or IAR Embedded Workbench for Arm v9.30 and above.
      Arm Compiler v5 is not supported, and earlier versions of the listed toolchains are not
      guaranteed to work.
  - question: Which CMSIS-Packs do I need when migrating from CMSIS v5 to v6?
    answer: >-
      Install ARM.CMSIS.6.0.0, ARM.Cortex_DFP.1.0.0, and ARM.CMSIS-RTX.5.8.0. These replace the
      monolithic ARM.CMSIS.5.x.x pack for CMSIS v6.
  - question: I used the Keil.ARM_Compiler pack. Which packs replace it for CMSIS v6?
    answer: >-
      Install ARM.CMSIS-View.1.1.0 and ARM.CMSIS_Compiler.2.0. The Keil.ARM_Compiler pack is deprecated
      and its content has moved into these packs.
  - question: How do I map my CMSIS v5 device to the Cortex_DFP pack?
    answer: >-
      Switch your device selection to a supported device in the Cortex_DFP pack using the provided
      mapping table. For example, ARMCM4/ARMCM4_FP maps to ARMCM4 (SP_FPU, MPU) and ARMCM7/ARMCM7_SP/ARMCM7_DP
      maps to ARMCM7 (DP_FPU, MPU).
  - question: What should I do if I’m using a Keil MDK v5 uvprojx project?
    answer: >-
      Use the project format conversion guidance to move from uvprojx to the Open-CMSIS-Pack csolution
      format. Follow the referenced learning path to import, convert, and build in Keil Studio
      for VS Code or on the command line.
# END generated_summary_faq

author: Christopher Seidl

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

