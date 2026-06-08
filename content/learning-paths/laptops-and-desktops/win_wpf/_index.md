---
title: Develop applications with Windows Presentation Foundation (WPF) on Windows on Arm

description: Learn how to create and build Windows Presentation Foundation (WPF) applications and measure code execution performance uplift on Arm64.

minutes_to_complete: 30

who_is_this_for: This learning path is for developers who want to learn how to create desktop applications and leverage performance improvements on Arm64.

learning_objectives:
    - Create and build a Windows Presentation Foundation (WPF) application
    - Measure code execution performance uplift on Arm64    

prerequisites:
    - A Windows on Arm computer such as the Lenovo Thinkpad X13s running Windows 11 or a Windows on Arm [virtual machine](/learning-paths/cross-platform/woa_azure/).
    - Visual Studio 2022 with .NET desktop development installed.

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T23:33:26Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: cc1a494e7b03672122ff84073b677a93659eca7df601b3f77c7e7fd536cc1af9
  summary_generated_at: '2026-06-01T22:20:26Z'
  summary_source_hash: cc1a494e7b03672122ff84073b677a93659eca7df601b3f77c7e7fd536cc1af9
  faq_generated_at: '2026-06-02T23:33:26Z'
  faq_source_hash: cc1a494e7b03672122ff84073b677a93659eca7df601b3f77c7e7fd536cc1af9
  summary: >-
    This Learning Path shows how to create and build a Windows Presentation Foundation (WPF) desktop
    application on Windows on Arm and compare execution times between ARM64 and x86_64 builds
    using Visual Studio 2022. You will work with WPF and XAML to define the UI, then use Visual
    Studio’s Configuration Manager to add an ARM64 Solution Platform and run the app under different
    settings to measure code execution performance uplift on Arm64. The target environment is
    a Windows on Arm computer (or a Windows on Arm virtual machine) with the .NET desktop development
    workload installed. By the end, you will have built and executed a WPF app and gathered timing
    comparisons across build configurations.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need a Windows on Arm computer (such as a Lenovo ThinkPad X13s) or a Windows on Arm
      virtual machine, and Visual Studio 2022 with .NET desktop development installed. No additional
      prerequisites are explicitly listed.
  - question: Which Visual Studio option do I use to target ARM64?
    answer: >-
      Use the Any CPU drop-down, choose Configuration Manager, then select New from the Active
      Solution Platform menu. In the New Solution Platform window, choose ARM64 and click OK.
  - question: Do I also need an x86_64 configuration for comparison?
    answer: >-
      Yes. The procedure prepares both ARM64 and x86_64 builds so you can compare computation
      times. Repeat the New Solution Platform steps to create the additional architecture.
  - question: How do I run the app to compare execution times across configurations?
    answer: >-
      Select the desired platform in Active Solution Platform, build, and launch the app from
      Visual Studio. Run it under each configuration and compare the computation times as instructed
      in the steps.
  - question: How do I know the app is running as ARM64 rather than x86_64?
    answer: >-
      Ensure ARM64 is selected as the Active Solution Platform before building and launching.
      The app will run using the architecture of the active platform you selected.
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
    - Windows Presentation Foundation
    - C#
    - .NET
    - Visual Studio
    
further_reading:
    - resource:
        title: Windows Presentation Foundation
        link: https://learn.microsoft.com/en-us/dotnet/desktop/wpf/?view=netdesktop-8.0
        type: documentation
    - resource:
        title: Syncfusion UI controls
        link: https://www.syncfusion.com
        type: website


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

