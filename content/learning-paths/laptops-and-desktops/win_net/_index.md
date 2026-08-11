---
title: Build a Windows on Arm native application with .NET

description: Learn how to build and run a .NET 6 Windows Presentation Foundation (WPF) application on Windows on Arm machines.

minutes_to_complete: 20

who_is_this_for: This is an introductory topic for software developers doing native development on Windows on Arm computers.

learning_objectives:
    - Build and run a .NET 6 Windows Presentation Foundation (WPF) application on a Windows on Arm machine

prerequisites:
    - A Windows on Arm computer such as the Lenovo Thinkpad X13s running Windows 11 or a Windows on Arm [virtual machine](/learning-paths/cross-platform/woa_azure/).

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-11T16:19:17Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: d25d6adb2606d2be5ff6fa0e8b5d65f83d67c14bd8fa12b86b014c41bad8cb77
  summary_generated_at: '2026-08-11T16:19:17Z'
  summary_source_hash: d25d6adb2606d2be5ff6fa0e8b5d65f83d67c14bd8fa12b86b014c41bad8cb77
  faq_generated_at: '2026-08-11T16:19:17Z'
  faq_source_hash: d25d6adb2606d2be5ff6fa0e8b5d65f83d67c14bd8fa12b86b014c41bad8cb77
  summary: >-
    You'll build and run a native .NET 6 Windows Presentation Foundation (WPF) application on Windows
    on Arm. You'll configure Visual Studio 2022 with the .NET desktop development workload, create a
    project that targets .NET 6, and launch it on a device or virtual machine. You'll also validate
    the target framework in project settings.
  faqs:
  - question: Where do I enable the .NET desktop development workload?
    answer: >-
      Open the Windows **Start** menu, launch Visual Studio Installer, and select **Modify**. On the
      **Workloads** tab, select **.NET desktop development** and apply the changes.
  - question: Which version of Visual Studio should I use?
    answer: >-
      Use Visual Studio 2022 or higher. Make sure the .NET desktop development workload is installed
      before creating the project.
  - question: Can I complete this on a virtual machine instead of physical hardware?
    answer: >-
      Yes. You can use a Windows on Arm virtual machine for this guide.
  - question: How do I confirm the project targets .NET 6?
    answer: >-
      Open the project properties in Visual Studio and check **Target Framework**. It should list
      `.NET 6`.
  - question: What result should I expect after building and running the WPF app?
    answer: >-
      The solution builds successfully and the WPF application launches on your Windows on Arm
      system. You should see the app start without build errors.
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
    - dotnet
    - Visual Studio

further_reading:
    - resource:
        title: Announcing .NET 6
        link: https://devblogs.microsoft.com/dotnet/announcing-net-6/
        type: blog
    - resource:
        title: Deploy .NET apps on Arm single-board computers
        link: https://learn.microsoft.com/en-us/dotnet/iot/deployment
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
