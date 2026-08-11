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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-11T16:23:20Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 8726f05daf1b14dd97adaceabb57c5bafece7cfd323b38a4a87bad3c1b51d0da
  summary_generated_at: '2026-08-11T16:23:20Z'
  summary_source_hash: 8726f05daf1b14dd97adaceabb57c5bafece7cfd323b38a4a87bad3c1b51d0da
  faq_generated_at: '2026-08-11T16:23:20Z'
  faq_source_hash: 8726f05daf1b14dd97adaceabb57c5bafece7cfd323b38a4a87bad3c1b51d0da
  summary: >-
    You'll create a WinUI 3 application in Visual Studio on Windows on Arm and build it in **Release**
    for both x64 and Arm64. First, you'll configure the
    startup selection, choose the target architecture from Visual Studio’s dropdowns, and run
    the packaged app (`Arm64.WinUIApp (Package)`) to execute a matrix multiplication. By
    repeating the run for x64 and ARM64, you'll capture the computation times shown by the app
    and compare results across architectures. The workflow keeps code changes minimal and focuses
    on build configuration, launch choices, and reading application output to understand execution
    behavior on Arm64 versus x64.
  faqs:
  - question: Which Visual Studio settings should I use before running the app for timing?
    answer: >-
      Set **Configuration** to **Release**. Select the architecture (**x64** or **ARM64**) in the
      dropdowns, then choose `Arm64.WinUIApp (Package)` as the startup item.
  - question: How do I switch between x64 and ARM64 runs to compare performance?
    answer: >-
      Change the architecture in Visual Studio’s dropdown from **x64** to **ARM64** (or vice versa),
      ensure **Release** is selected, and run the app again. Record the computation time shown by the app
      for each run.
  - question: Do I need to modify the code when changing architectures?
    answer: >-
      No code changes are required for the comparison. Use the same project and switch the architecture
      in Visual Studio’s configuration.
  - question: How do I know I’m measuring the right thing in the app?
    answer: >-
      Use the application’s matrix multiplication feature and note the computation time it displays.
      Compare the displayed times between the x64 and ARM64 runs.
  - question: I don’t see ARM64 in the architecture list. What should I check?
    answer: >-
      Confirm you are using a Windows on Arm device or a supported Windows on Arm virtual machine
      and that the required Visual Studio workloads from the prerequisites are installed.
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
    - WinUI 3
    - csharp
    - dotnet
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
