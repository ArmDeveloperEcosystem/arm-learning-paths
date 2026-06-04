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

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T23:28:34Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 037509ebca3a7c5a58bef247532919cd8196c7993e946ce519585cdc82073daa
  summary_generated_at: '2026-06-01T22:17:25Z'
  summary_source_hash: 037509ebca3a7c5a58bef247532919cd8196c7993e946ce519585cdc82073daa
  faq_generated_at: '2026-06-02T23:28:34Z'
  faq_source_hash: 037509ebca3a7c5a58bef247532919cd8196c7993e946ce519585cdc82073daa
  summary: >-
    This path shows how to create and build a cross-platform .NET MAUI application on Windows
    on Arm and measure code execution performance uplift on Arm64. Using Visual Studio 2022, you
    will start a new MAUI project, add C# helper classes to generate pseudo-random double-precision
    vectors and compute a*b+c, measure execution time with a PerformanceHelper, and present results
    in a list view. Prerequisites are a Windows on Arm computer such as a Lenovo Thinkpad X13s
    running Windows 11, or a Windows on Arm virtual machine, plus Visual Studio 2022 with .NET
    Multi-platform App UI development and Universal Windows Platform development installed. The
    path is introductory and takes about 30 minutes.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      Use a Windows on Arm computer such as a Lenovo ThinkPad X13s running Windows 11, or a Windows
      on Arm virtual machine. Install Visual Studio 2022 with the .NET Multi-platform App UI development
      and Universal Windows Platform development workloads.
  - question: Which Visual Studio components should I install?
    answer: >-
      Install Visual Studio 2022 with the .NET Multi-platform App UI development workload and
      the Universal Windows Platform development workload. These are explicitly listed prerequisites.
  - question: Which project type should I create in Visual Studio?
    answer: >-
      Create a .NET MAUI project. The Learning Path focuses on building and running it on Windows
      on Arm.
  - question: What code will I add to measure performance and what does it compute?
    answer: >-
      You will add a PerformanceHelper class to measure code execution time and a VectorHelper
      class that implements AdditionOfProduct, computing a*b+c over pseudo-random double-precision
      vectors. A list view displays the processing results.
  - question: How do I know the performance measurement part worked?
    answer: >-
      Build and run the app on Windows on Arm and check that the UI displays processing results
      and execution times. The Learning Path does not specify expected numbers; you use the reported
      timings to observe Arm64 performance.
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
    - .NET    
    - C#
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

