---
title: Build a Windows on Arm native application with clang

description: Learn how to configure the LLVM toolchain with Visual Studio to build native Windows on Arm applications using the open-source PuTTY project.

minutes_to_complete: 60

who_is_this_for: This is an introductory topic for software developers doing native development on Windows on Arm computers.

learning_objectives:
    - Configure the native LLVM toolchain with Visual Studio to compile for Windows on Arm
    - Build open-source PuTTY application for Windows on Arm using the native LLVM toolchain

prerequisites:
    - A Windows on Arm computer such as the Lenovo Thinkpad X13s running Windows 11 or a Windows on Arm [virtual machine](/learning-paths/cross-platform/woa_azure/).

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T23:09:11Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 631134875aac73e168b60b86d1ca7b4e898196f98cb2825a4238f62129d2d862
  summary_generated_at: '2026-06-01T22:07:27Z'
  summary_source_hash: 631134875aac73e168b60b86d1ca7b4e898196f98cb2825a4238f62129d2d862
  faq_generated_at: '2026-06-02T23:09:11Z'
  faq_source_hash: 631134875aac73e168b60b86d1ca7b4e898196f98cb2825a4238f62129d2d862
  summary: >-
    This introductory Learning Path shows how to configure the native LLVM toolchain in Visual
    Studio to compile a Windows on Arm application, using the open-source PuTTY project as the
    example. You will set up Visual Studio 2022 or later with LLVM support, install the required
    32-bit x86 Strawberry Perl package, and then build PuTTY with Clang for Windows on Arm. The
    path targets developers working on a Windows on Arm computer or a Windows on Arm virtual machine
    and is designed to be completed in about 60 minutes. By the end, you will have compiled PuTTY
    natively for Windows on Arm using the LLVM toolchain integrated with Visual Studio.
  faqs:
  - question: Do I need Arm hardware, or can I use a virtual machine?
    answer: >-
      You can use either. The prerequisites list a Windows on Arm computer such as the Lenovo
      ThinkPad X13s running Windows 11 or a Windows on Arm virtual machine.
  - question: Which version of Visual Studio and components are required?
    answer: >-
      Use Visual Studio 2022 or higher and install LLVM support in Visual Studio. The steps assume
      LLVM is available through the Visual Studio installer.
  - question: Which Strawberry Perl package should I install on Windows on Arm?
    answer: >-
      Install the 32-bit x86 version of Strawberry Perl. There is currently no Arm version available.
  - question: Which compiler and build system are used to compile PuTTY?
    answer: >-
      The path uses Clang from the LLVM toolchain within Visual Studio to build a CMake application.
      The example application is PuTTY.
  - question: What result should I expect after the build completes?
    answer: >-
      You should have a successful build of the PuTTY application for Windows on Arm using the
      native LLVM toolchain. A completed build produces PuTTY artifacts in your configured build
      output.
# END generated_summary_faq

author: Pareena Verma

### Tags
skilllevels: Introductory
subjects: Migration to Arm
armips:
    - Cortex-A
operatingsystems:
    - Windows
tools_software_languages:
    - LLVM
    - Visual Studio Code

further_reading:
    - resource:
        title: How to setup Windows on Arm for LLVM development
        link: https://old.linaro.org/blog/how-to-set-up-windows-on-arm-for-llvm-development/
        type: blog
    - resource:
        title: LLVM - Windows on Arm
        link: https://linaro.atlassian.net/wiki/spaces/LLVM/overview/
        type: website


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

