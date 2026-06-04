---
title: Develop desktop applications with Windows Forms on Windows on Arm

description: Learn how to create and build Windows Forms applications and measure code execution performance on Arm64.

minutes_to_complete: 30

who_is_this_for: This learning path is for developers who want to learn how to create Windows Forms applications on Windows on Arm (WoA).

learning_objectives:
    - Create and build a Windows Forms application
    - Measure code execution performance on Arm64

prerequisites:
    - A Windows on Arm computer such as the Lenovo Thinkpad X13s running Windows 11 or a Windows on Arm [virtual machine](/learning-paths/cross-platform/woa_azure/).
    - Visual Studio 2022 with .NET Desktop Development workload

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T23:25:52Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: d43413097704af29b9233dfe33fb675ffd5c6d5a172154d6a7542e77d6625c00
  summary_generated_at: '2026-06-01T22:16:20Z'
  summary_source_hash: d43413097704af29b9233dfe33fb675ffd5c6d5a172154d6a7542e77d6625c00
  faq_generated_at: '2026-06-02T23:25:52Z'
  faq_source_hash: d43413097704af29b9233dfe33fb675ffd5c6d5a172154d6a7542e77d6625c00
  summary: >-
    This introductory path shows how to create and build a Windows Forms desktop application in
    C#/.NET on Windows on Arm using Visual Studio 2022. You will configure build settings, including
    creating an ARM64 solution platform in Configuration Manager, then run the app under different
    settings and compare matrix multiplication computation times to observe execution behavior
    on Arm64. The target environment is a Windows on Arm device or a Windows on Arm virtual machine.
    Prerequisites are Visual Studio 2022 with the .NET Desktop Development workload and access
    to Windows on Arm. By the end, you will have a working WinForms app and a basic method to
    measure code performance on Arm64.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need a Windows on Arm computer running Windows 11 or a Windows on Arm virtual machine,
      plus Visual Studio 2022 with the .NET Desktop Development workload installed.
  - question: Which language and framework does the sample use?
    answer: >-
      The application is built with Windows Forms using C# on .NET.
  - question: How do I switch the project to build for ARM64 in Visual Studio?
    answer: >-
      Open the target platform dropdown (default is Any CPU), choose Configuration Manager, select
      New in Active solution platform, and pick ARM64 in the New Solution Platform dialog.
  - question: How do I confirm I’m building and running the ARM64 configuration?
    answer: >-
      Check that the Active solution platform in Visual Studio shows ARM64 before building and
      launching the application.
  - question: What result should I expect when comparing performance settings?
    answer: >-
      You will run the application under different build settings and compare the matrix multiplication
      computation times reported by the app to evaluate execution performance on Arm64.
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
    - Windows Forms
    - C#
    - .NET
    
further_reading:
    - resource:
        title: Windows Forms on .NET 8
        link: https://learn.microsoft.com/en-us/dotnet/desktop/winforms/?view=netdesktop-8.0
        type: documentation
    - resource:
        title: Arm64 Performance Improvements in .NET 8
        link: https://devblogs.microsoft.com/dotnet/this-arm64-performance-in-dotnet-8/
        type: blog


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

