---
title: Build .NET MAUI Applications on Arm64

description: Learn how to create and build cross-platform .NET MAUI applications and measure code execution performance uplift on Arm64.

minutes_to_complete: 30

who_is_this_for: This learning path is for developers who want to learn how to create cross-platform applications with .NET MAUI and leverage performance improvements on Arm64.

learning_objectives:
   - Create and build a .NET MAUI application
   - Measure code execution performance uplift on Arm64   

prerequisites:
    - A Windows on Arm computer such as the Lenovo Thinkpad X13s running Windows 11 or a Windows on Arm [virtual machine](/learning-paths/cross-platform/woa_azure/).
    - Visual Studio 2022 with .NET Multi-platform App UI development and Universal Windows Platform development installed.

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-11T16:20:13Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 4e0750e0bc7a01fbac8d76b22f311cbff4bf5e216db682f8607939d17454f779
  summary_generated_at: '2026-08-11T16:20:13Z'
  summary_source_hash: 4e0750e0bc7a01fbac8d76b22f311cbff4bf5e216db682f8607939d17454f779
  faq_generated_at: '2026-08-11T16:20:13Z'
  faq_source_hash: 4e0750e0bc7a01fbac8d76b22f311cbff4bf5e216db682f8607939d17454f779
  summary: >-
    You'll create a .NET MAUI project in Visual Studio on Windows on Arm and add a compute workload
    to measure execution time on Arm64. First, you'll implement helpers that generate vectors, calculate
    `a*b+c`, and time execution. Then, you'll update the UI with a **list view**, run the workload, and
    review its processing results and timings.
  faqs:
  - question: I don’t see the .NET MAUI project template in Visual Studio. What should I check?
    answer: >-
      Verify that the .NET Multi-platform App UI development workload is installed in Visual Studio.
      If it's missing, modify your installation to add it.
  - question: Where should I add the `PerformanceHelper` and `VectorHelper` classes?
    answer: >-
      Add both classes to the .NET MAUI project so both are accessible from the application code
      that triggers the computation and updates the UI.
  - question: What does the `AdditionOfProduct` method compute and with which data types?
    answer: >-
      It computes a*b+c over pseudo-randomly generated vectors of double-precision values. The
      operation produces results that are then used for timing and display.
  - question: How do I know the performance measurement is working?
    answer: >-
      Run the app and look for timing and processing results in the **list view**. If the list updates
      after triggering the operation, the measurement path is active.
  - question: Which build configuration should I use when measuring execution time?
    answer: >-
      No configuration is explicitly specified. Use the same configuration for all
      runs so measurements are comparable.
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
    - dotnet    
    - csharp
    - Visual Studio

further_reading:
    - resource:
        title: .NET Multi-platform App UI
        link: https://dotnet.microsoft.com/en-us/apps/maui
        type: documentation
    - resource:
        title: What is .NET MAUI?
        link: https://learn.microsoft.com/en-us/dotnet/maui/what-is-maui?view=net-maui-8.0
        type: Microsoft Learn
    - resource:
        title: .NET MAUI Source Code
        link: https://github.com/dotnet/maui
        type: GitHub repository

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
