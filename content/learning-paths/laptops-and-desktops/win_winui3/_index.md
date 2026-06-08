---
title: Develop Windows applications with WinUI3 on Windows on Arm

description: Learn how to create and build Windows UI Library (WinUI) applications and measure code execution performance on Arm64.

minutes_to_complete: 30

who_is_this_for: This learning path is for developers who want to learn how to create cross-platform applications and leverage performance improvements on Arm64.

learning_objectives:
    - Create and build a Windows UI Library (WinUI) application
    - Measure code execution performance on Arm64    

prerequisites:
    - A Windows on Arm computer such as the Lenovo Thinkpad X13s running Windows 11 or a Windows on Arm [virtual machine](/learning-paths/cross-platform/woa_azure/).
    - Visual Studio 2022 with .NET desktop development and Universal Windows Platform development installed.

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T23:32:13Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 383dcf17bce86b24a2d9c8d0982fa6e9ddf954955c16b420463ada951753dbfa
  summary_generated_at: '2026-06-01T22:20:00Z'
  summary_source_hash: 383dcf17bce86b24a2d9c8d0982fa6e9ddf954955c16b420463ada951753dbfa
  faq_generated_at: '2026-06-02T23:32:13Z'
  faq_source_hash: 383dcf17bce86b24a2d9c8d0982fa6e9ddf954955c16b420463ada951753dbfa
  summary: >-
    This Learning Path shows how to create and build a Windows UI Library (WinUI 3) application
    in C#/.NET using Visual Studio 2022 on Windows on Arm, then compare code execution performance
    on Arm64 versus x64. You will configure Visual Studio for Release builds, select the target
    architecture, launch the app, and use matrix multiplication to measure and compare computation
    times across the two architectures. Prerequisites are a Windows on Arm computer (or a Windows
    on Arm virtual machine) and Visual Studio 2022 with the .NET desktop development and Universal
    Windows Platform development workloads installed. Designed for an introductory audience focused
    on migration to Arm, the path takes about 30 minutes.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need a Windows on Arm device such as a Lenovo ThinkPad X13s running Windows 11 or a
      Windows on Arm virtual machine. Install Visual Studio 2022 with the .NET desktop development
      and Universal Windows Platform development workloads.
  - question: Which Visual Studio settings should I use to build and run for each architecture?
    answer: >-
      Set the Configuration to Release. Then choose the target architecture as x64 or ARM64 and
      select Arm64.WinUIApp (Package) when targeting ARM64.
  - question: How do I run the performance comparison between x64 and ARM64?
    answer: >-
      Launch the application for x64 first, perform the matrix multiplication calculations as
      described, then switch the architecture to ARM64 and repeat. Record the computation times
      to compare the results.
  - question: How do I confirm I built the app for ARM64?
    answer: >-
      In Visual Studio, verify the Configuration is set to Release and the Architecture dropdown
      shows ARM64. Ensure the startup item is Arm64.WinUIApp (Package) before running.
  - question: Can I complete this Learning Path without a physical Arm device?
    answer: >-
      Yes. A Windows on Arm virtual machine is listed as an acceptable environment in the prerequisites.
# END generated_summary_faq

author: Dawid Borycki

### Tags
skilllevels: Introductory
subjects: Migration to Arm
armips:
    - Cortex-A
operatingsystems:
    - Windows
tools_software_languages:
    - WinUI 3
    - C#
    - .NET
    - Visual Studio
    
further_reading:
    - resource:
        title: Microsoft's Official WinUI 3 Documentation
        link: https://learn.microsoft.com/en-us/windows/apps/winui/winui3/
        type: documentation  
    - resource:
        title: Example Applications and Code for WinUI
        link: https://github.com/Microsoft/WinUI-Gallery
        type: website


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

