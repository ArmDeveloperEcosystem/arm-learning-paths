---
title: Migrating CMSIS-Packs to CMSIS v6

description: Learn how to migrate a CMSIS v5-based CMSIS-Pack with device support to CMSIS v6 and update example projects for compatibility with the new CMSIS version.

minutes_to_complete: 10

who_is_this_for: This is an advanced topic for maintainers of CMSIS-Packs with device support.

learning_objectives: 
    - Migrate a CMSIS v5-based CMSIS-Pack with device support to CMSIS v6.
    - Update example projects.

prerequisites:
    - A good understanding of [CMSIS-Packs](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/index.html).
    - A CMSIS-Pack that contains device support and was created for CMSIS v5.

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-12T20:13:57Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 14883fd881c70754e80ea15e09499621c644079f52f28831f07376621e841228
  summary_generated_at: '2026-08-12T20:13:57Z'
  summary_source_hash: 14883fd881c70754e80ea15e09499621c644079f52f28831f07376621e841228
  faq_generated_at: '2026-08-12T20:13:57Z'
  faq_source_hash: 14883fd881c70754e80ea15e09499621c644079f52f28831f07376621e841228
  summary: >-
    You'll migrate a CMSIS v5-based CMSIS-Pack with device support to CMSIS v6. You'll confirm the
    toolchain, replace assembly startup code with C files, and create scatter files. You'll update
    example projects from Arm Compiler 5 to version 6 in µVision, then convert them to the
    CMSIS-Toolbox `csolution` and `cproject` formats.
  faqs:
  - question: Which toolchain should I use for this migration?
    answer: >-
      You use Arm Compiler for Embedded v6. CMSIS v6 also supports Arm GNU Toolchain
      v12 and above, LLVM v16 and above, and IAR Embedded Workbench for Arm v9.30 and above.
  - question: How do I update device support for CMSIS v6?
    answer: >-
      Replace assembly-based startup code with C-based startup files and create scatter files.
      Complete these updates before migrating example projects.
  - question: How do I switch my example project from Arm Compiler 5 to 6 in µVision?
    answer: >-
      Install the newly created device family pack, open **Options for Target - Target**, and set
      **Use default compiler version 6**. Then open the **C/C++ [AC6]** tab and set the appropriate defines.
  - question: When should I convert my project to the CMSIS-Toolbox format, and what files appear?
    answer: >-
      Convert to the new standard after migrating to Arm Compiler 6. The conversion targets the
      `csolution` and `cproject` format, so you should see `csolution` and `cproject` files in your project.
  - question: What should I check if my project still builds with old warning settings after switching
      compilers?
    answer: >-
      Review the **C/C++ [AC6]** settings and adjust your defines and warning configuration. It's
      good practice to revisit compiler warnings after changing the compiler version.
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
        title: Create a Device Family Pack - Hands-On Example
        link: https://github.com/Open-CMSIS-Pack/DFP-Pack-HandsOn
        type: GitHub Repository
    - resource:
        title: Arm Compiler for Embedded Migration and Compatibility Guide
        link: https://developer.arm.com/documentation/100068/latest/Migrating-from-Arm-Compiler-5-to-Arm-Compiler-for-Embedded-6
        type: Documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
