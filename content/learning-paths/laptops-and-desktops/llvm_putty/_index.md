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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-28T16:21:25Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 631134875aac73e168b60b86d1ca7b4e898196f98cb2825a4238f62129d2d862
  summary_generated_at: '2026-07-28T16:21:25Z'
  summary_source_hash: 631134875aac73e168b60b86d1ca7b4e898196f98cb2825a4238f62129d2d862
  faq_generated_at: '2026-07-28T16:21:25Z'
  faq_source_hash: 631134875aac73e168b60b86d1ca7b4e898196f98cb2825a4238f62129d2d862
  summary: >-
    This Learning Path shows how to configure the LLVM toolchain in Visual Studio on a Windows
    on Arm system and compile a native application with Clang. Learners enable LLVM support in
    Visual Studio, set up required tools, and use Clang to build a CMake-based project. The hands-on
    work focuses on compiling the open-source PuTTY client as a native Windows on Arm binary,
    including installing the 32-bit x86 Strawberry Perl when needed. The path emphasizes choosing
    the correct compiler and target during configuration and driving the build from Visual Studio.
    After completing the steps, you produce a locally built PuTTY executable compiled natively
    for Windows on Arm.
  faqs:
  - question: Which Visual Studio setup do I need before building?
    answer: >-
      Install Visual Studio 2022 or higher and add LLVM support in Visual Studio. The steps assume
      that configuration is in place.
  - question: Do I need an Arm build of Strawberry Perl?
    answer: >-
      No. There is currently no Arm version of Strawberry Perl, so install the 32-bit x86 version.
  - question: What build system do I use for PuTTY in this path?
    answer: >-
      PuTTY is built as a CMake application. You use Clang from the LLVM toolchain to compile
      it for Windows on Arm.
  - question: Can I follow this on a Windows on Arm virtual machine?
    answer: >-
      Yes. Any Windows on Arm computer or a Windows on Arm virtual machine can be used.
  - question: What result should I expect when the build succeeds?
    answer: >-
      A native Windows on Arm build of the PuTTY application produced by Visual Studio using the
      LLVM toolchain.
# END generated_summary_faq

author: Pareena Verma

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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

