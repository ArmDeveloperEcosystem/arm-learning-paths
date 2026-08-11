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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-11T16:23:51Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 90f59c8b118f49161d34026d10ccb4bd036753cd1f44fc443b6fb74138cb1850
  summary_generated_at: '2026-08-11T16:23:51Z'
  summary_source_hash: 90f59c8b118f49161d34026d10ccb4bd036753cd1f44fc443b6fb74138cb1850
  faq_generated_at: '2026-08-11T16:23:51Z'
  faq_source_hash: 90f59c8b118f49161d34026d10ccb4bd036753cd1f44fc443b6fb74138cb1850
  summary: >-
    You'll create a Windows Presentation Foundation (WPF) desktop application and build it for multiple
    architectures on Windows on Arm. First, you'll use **Configuration Manager** to add an ARM64 target alongside
    x86_64. Then, you'll build and run each configuration. You'll compare computation times and learn how WPF
    uses XAML to separate the UI from business logic.
  faqs:
  - question: How do I add an ARM64 target to my WPF project?
    answer: >-
      Open the **Any CPU** drop-down on the Visual Studio toolbar, choose **Configuration Manager**,
      then select **New** under **Active Solution Platform**. In the **New Solution Platform** dialog,
      select **ARM64** and select **OK**.
  - question: How do I switch between ARM64 and x86_64 builds when running the app?
    answer: >-
      Use the **Solution Platform** drop-down on the toolbar to select the desired target. Rebuild
      and launch the application after switching the platform.
  - question: How do I confirm the build is targeting ARM64 before I run it?
    answer: >-
      Check that **Active Solution Platform** shows **ARM64** in **Configuration Manager** or on the toolbar.
      Build the project with that platform selected before starting the app.
  - question: What should I measure to compare execution times across platforms?
    answer: >-
      Run the same app scenario under each platform and record the computation times the app reports.
      Use the same inputs and steps for each run to make the comparison consistent.
  - question: Do I need to change any project properties besides the Solution Platform?
    answer: >-
      No additional property changes are listed. Select the platform in **Configuration Manager**
      and run the application to compare times.
# END generated_summary_faq

author: Dawid Borycki

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
    - Windows Presentation Foundation
    - csharp
    - dotnet
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
