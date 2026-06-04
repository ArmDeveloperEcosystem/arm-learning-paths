---
title: Benchmarking .NET 8 applications on Windows on Arm

description: Learn how to build, run, and benchmark .NET 8 Console applications to measure performance on Windows on Arm devices.

minutes_to_complete: 20

who_is_this_for: This learning path is for developers who want to benchmark the performance of the .NET 8 applications on Windows on Arm (WoA).

learning_objectives:
    - Build and run .NET 8 Console Applications
    - Benchmark .NET applications
    - Implement custom performance benchmarks

prerequisites:
    - A Windows on Arm computer such as the Lenovo Thinkpad X13s running Windows 11 or a Windows on Arm [virtual machine](/learning-paths/cross-platform/woa_azure/).
    - .NET 8 SDK for [x64](https://dotnet.microsoft.com/en-us/download/dotnet/thank-you/sdk-8.0.100-windows-x64-installer) and [arm64](https://dotnet.microsoft.com/en-us/download/dotnet/thank-you/sdk-8.0.100-windows-arm64-installer).
    - Any code editor, we recommend using [Visual Studio Code for Arm64](https://code.visualstudio.com/docs/?dv=win32arm64user).

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T23:27:37Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 218fd5b33e104360d5de9f632f9338e2f24041ea70f7a01fad0af6be2a11619c
  summary_generated_at: '2026-06-01T22:17:04Z'
  summary_source_hash: 218fd5b33e104360d5de9f632f9338e2f24041ea70f7a01fad0af6be2a11619c
  faq_generated_at: '2026-06-02T23:27:37Z'
  faq_source_hash: 218fd5b33e104360d5de9f632f9338e2f24041ea70f7a01fad0af6be2a11619c
  summary: >-
    This introductory path shows how to build, run, and benchmark .NET 8 Console applications
    on Windows on Arm, with a focus on measuring execution performance on Arm64. You will set
    up your development environment, verify your .NET installation, clone a sample repository,
    and implement custom benchmarks using System.Diagnostics.Stopwatch. Prerequisites include
    a Windows on Arm device or VM, the .NET 8 SDK for both x64 and arm64, and any code editor
    (Visual Studio Code for Arm64 is recommended). In about 20 minutes, you will be able to run
    the sample app and create simple, repeatable measurements to understand how your .NET code
    performs on Windows on Arm.
  faqs:
  - question: What do I need before running the benchmarks?
    answer: >-
      You need a Windows on Arm computer or a Windows on Arm virtual machine, the .NET 8 SDK for
      both x64 and arm64, and a code editor (Visual Studio Code for Arm64 is recommended). These
      are listed in the prerequisites.
  - question: How do I verify that .NET 8 is installed correctly on Windows on Arm?
    answer: >-
      Follow the “Before you begin” step to check your .NET installation. If anything is missing,
      install the .NET 8 SDK for both x64 and arm64 as listed in the prerequisites.
  - question: How do I get the sample application used in this Learning Path?
    answer: >-
      Clone the repository by running: git clone https://github.com/dawidborycki/Arm64.Performance.DotNet.git.
      The sample is a .NET console application created with dotnet new console.
  - question: How are the custom benchmarks implemented in this path?
    answer: >-
      They use the System.Diagnostics.Stopwatch class. The sample includes a PerformanceHelper
      static class with reusable timing methods and a PerformanceTests static class to organize
      test code.
  - question: How should I compare performance between x64 and Arm64 on Windows on Arm?
    answer: >-
      Install both the x64 and arm64 .NET 8 SDKs as listed, then run the same Stopwatch-based
      benchmarks as directed in the steps. Compare the reported execution times to observe differences.
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
    - Visual Studio
    - Visual Studio Code

further_reading:
    - resource:
        title: Announcing .NET 8
        link: https://devblogs.microsoft.com/dotnet/announcing-dotnet-8/
        type: blog
    - resource:
        title: Deploy .NET apps on Arm single-board computers
        link: https://learn.microsoft.com/en-us/dotnet/iot/deployment
        type: documentation
    - resource:
        title: .NET CLI
        link: https://learn.microsoft.com/en-us/dotnet/core/tools/
        type: documentation
    - resource:
        title: Performance improvements in .NET 8
        link: https://devblogs.microsoft.com/dotnet/performance-improvements-in-net-8/
        type: blog
    - resource:
        title: .NET Performance on arm64
        link: https://www.codeproject.com/Articles/5367981/NET-Performance-on-Arm64
        type: article


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

