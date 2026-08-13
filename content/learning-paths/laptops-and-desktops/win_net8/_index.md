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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-11T16:19:47Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 0e48c317780ed95597f29059d547529b970df736a019653d499c4e2fe45cf2ce
  summary_generated_at: '2026-08-11T16:19:47Z'
  summary_source_hash: 0e48c317780ed95597f29059d547529b970df736a019653d499c4e2fe45cf2ce
  faq_generated_at: '2026-08-11T16:19:47Z'
  faq_source_hash: 0e48c317780ed95597f29059d547529b970df736a019653d499c4e2fe45cf2ce
  summary: >-
    You'll build and run a .NET 8 console application on Windows on Arm, then add targeted benchmarks.
    First, you'll clone a sample repository and use `System.Diagnostics.Stopwatch` with the `PerformanceTests`
    class to time focused code paths. Then, you'll review the output, compare results across builds, and
    develop a repeatable approach for measuring your own .NET benchmarks.
  faqs:
  - question: How do I know .NET 8 is installed correctly before starting?
    answer: >-
      The introduction includes a quick check to confirm the installation. Complete that verification
      step before cloning or running the sample application.
  - question: Which .NET SDK should I use during the steps, x64 or arm64?
    answer: >-
      Both x64 and arm64 SDKs are listed so you can build as directed when comparing results.
      Follow the step instructions to choose the SDK for each build.
  - question: Where do I get the sample application used for benchmarking?
    answer: >-
      Clone the repository from [Github](https://github.com/dawidborycki/Arm64.Performance.DotNet.git). It
      contains the console app scaffold and the benchmarking helpers you use.
  - question: Where should I add my custom benchmark code in the sample?
    answer: >-
      Add or modify test cases in the `PerformanceTests` class. Use the reusable methods from
      `PerformanceHelper` to time your code with `System.Diagnostics.Stopwatch`.
  - question: What result should I expect when the benchmarks run?
    answer: >-
      The console application prints timing results for each test. You should see execution time
      measurements that you can compare across runs or builds as instructed.
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
