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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-11T16:18:29Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: b3265b8bdc6a015b440b0a2fc040375cd4cb4a8b12f8717f955849e76ce0e4ec
  summary_generated_at: '2026-08-11T16:18:29Z'
  summary_source_hash: b3265b8bdc6a015b440b0a2fc040375cd4cb4a8b12f8717f955849e76ce0e4ec
  faq_generated_at: '2026-08-11T16:18:29Z'
  faq_source_hash: b3265b8bdc6a015b440b0a2fc040375cd4cb4a8b12f8717f955849e76ce0e4ec
  summary: >-
    You'll create a Windows Forms desktop application on Windows on Arm using Visual Studio. First, you'll
    assemble the UI, build the app, and add an ARM64 solution platform in **Configuration Manager**.
    Then, you'll run the same matrix multiplication workload across configurations, compare computation
    times, and see how the selected target platform affects execution on Arm64.
  faqs:
  - question: How do I add the ARM64 build configuration in Visual Studio?
    answer: >-
      Open the **target platform** dropdown (it initially shows **Any CPU**), select **Configuration Manager**,
      then choose **New Solution Platform**. In the **New Solution Platform** window, select **ARM64** and
      confirm.
  - question: What should I choose when I want to measure Arm64 performance?
    answer: >-
      Use the **ARM64** solution platform to measure code execution on Arm64. You can then contrast
      results with other available settings to compare computation times.
  - question: What should I check before I run timing comparisons?
    answer: >-
      Verify the active solution platform is set to the configuration you want to test and that
      the project builds without errors. Run the same matrix multiplication workload each time
      for a consistent comparison.
  - question: How do I switch between configurations after creating ARM64?
    answer: >-
      Use the **target platform** dropdown to select the active platform. You can also open
      **Configuration Manager** to review and change the active solution platform.
  - question: What result should I expect when I run the app under different settings?
    answer: >-
      The **Windows Forms** app launches normally, and the code reports matrix multiplication computation
      times. Expect timing values you can compare across the configurations you selected.
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
    - Windows Forms
    - csharp
    - dotnet

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
