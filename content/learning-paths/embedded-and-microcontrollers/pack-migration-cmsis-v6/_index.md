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

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T22:37:02Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 8039812773c6c1ac45cceb4039cee801e627d67871b625283c1bb5b3fa2960b3
  summary_generated_at: '2026-06-01T21:48:37Z'
  summary_source_hash: 8039812773c6c1ac45cceb4039cee801e627d67871b625283c1bb5b3fa2960b3
  faq_generated_at: '2026-06-02T22:37:02Z'
  faq_source_hash: 8039812773c6c1ac45cceb4039cee801e627d67871b625283c1bb5b3fa2960b3
  summary: >-
    This path shows maintainers how to migrate a CMSIS v5-based CMSIS-Pack with device support
    to CMSIS v6 and update example projects for compatibility. You will update device support
    by switching from assembly-based startup to C-based startup files and creating scatter files,
    then migrate example projects from Arm Compiler 5 to Arm Compiler 6 and convert them to the
    CMSIS-Toolbox project standard (csolution/cproject). CMSIS v6 supports Arm Compiler for Embedded
    v6+, Arm GNU Toolchain v12+, LLVM v16+, and IAR EWARM v9.30+, and this path uses Arm Compiler
    for Embedded v6. Prerequisites are a solid understanding of CMSIS-Packs and a CMSIS v5 device-support
    pack. Target environments include Baremetal and RTOS.
  faqs:
  - question: Which toolchains can I use for CMSIS v6, and which one is used in this path?
    answer: >-
      CMSIS v6 supports Arm Compiler for Embedded (v6 and above), Arm GNU Toolchain (v12 and above),
      LLVM (v16 and above), and IAR Embedded Workbench for Arm (v9.30 and above). This Learning
      Path uses Arm Compiler for Embedded v6.
  - question: What do I need before running the migration steps?
    answer: >-
      You need a good understanding of CMSIS-Packs and a CMSIS-Pack with device support that was
      created for CMSIS v5. This path targets maintainers responsible for such packs.
  - question: What changes are required in device support when moving to CMSIS v6?
    answer: >-
      Switch from assembly-based startup code to C-based startup files and create scatter files.
      These updates prepare the device support for CMSIS v6 compatibility.
  - question: My example projects use Arm Compiler 5. What should I do first?
    answer: >-
      Migrate the projects to Arm Compiler for Embedded v6 before attempting conversion to the
      new CMSIS-Toolbox project format. In µVision, install the newly created device family pack,
      set the compiler to use default version 6 under Options for Target > Target, and configure
      defines in the C/C++ [AC6] tab.
  - question: When can I convert projects to the CMSIS-Toolbox csolution/cproject format?
    answer: >-
      After migrating your examples to Arm Compiler for Embedded v6, they can be automatically
      converted to the CMSIS-Toolbox project standard (csolution/cproject). The path assumes this
      conversion follows the compiler migration.
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

