---
title: Migrate a .NET application to Azure Cobalt 100
description: Learn how to build and run an OrchardCore CMS .NET application on Azure Cobalt 100 processors, covering AnyCPU configuration and shared C library integration.

minutes_to_complete: 25

who_is_this_for: This is an advanced topic for .NET developers who want to take advantage of the performance and cost benefits of Azure Cobalt processors.

learning_objectives: 
    - Build and run a basic OrchardCore CMS application
    - Integrate a simple C shared library into a .NET application
    - Configure architecture-agnostic builds using AnyCPU
    - Evaluate the performance of different .NET versions

prerequisites:
    - A Microsoft Azure account with permissions to deploy virtual machines
    - .NET SDK 8.0 or later 
    - Basic knowledge of C and C#
    - GCC installed (Linux) or access to a cross-compiler
    - OrchardCore application created using the .NET CLI or Visual Studio

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-27T18:52:59Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 08d8f0c86625ef41476d3a8b24bad9b0a0820797022ef847bf9bb17a976726a7
  summary_generated_at: '2026-07-27T18:52:59Z'
  summary_source_hash: 08d8f0c86625ef41476d3a8b24bad9b0a0820797022ef847bf9bb17a976726a7
  faq_generated_at: '2026-07-27T18:52:59Z'
  faq_source_hash: 08d8f0c86625ef41476d3a8b24bad9b0a0820797022ef847bf9bb17a976726a7
  summary: >-
    You'll migrate a .NET OrchardCore CMS application to an Azure Cobalt 100 Arm-based virtual
    machine. You'll provision Ubuntu 24.04, build and run the application, add a native C component
    that C# calls through `DllImport`, and configure an architecture-agnostic `AnyCPU` build for Arm
    and x86. You'll then review .NET version choices and confirm the expected native output.
  faqs:
  - question: Which network port should I open to reach the OrchardCore app on the VM?
    answer: >-
      Open port 8080 to the internet as part of the VM setup. After starting the app, connect
      to the VM’s public IP on port 8080.
  - question: What artifact should I get when I compile the C code into a shared library?
    answer: >-
      The `gcc` command produces a shared object named `libmylib.so`. This is the library the C# code
      will load.
  - question: How do I verify the C library call worked from C#?
    answer: >-
      Call the function via `DllImport` and check the application’s console output for `Hello from
      the C library!`. Seeing that line confirms that the native call executed.
  - question: Which build option should I use so the same build runs on both Arm and x86?
    answer: >-
      Use .NET’s `AnyCPU` configuration. It provides an architecture-agnostic managed build that
      runs on both architectures.
  - question: Which .NET versions does this path highlight for support status on Arm?
    answer: >-
      .NET 8 (current LTS, support until Nov 2026), .NET 9 (STS, support until Nov 2026), and
      .NET 10 (next LTS, preview). These versions frame the version-by-version discussion.
# END generated_summary_faq

author: Joe Stech

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
cloud_service_providers:
  - Microsoft Azure
armips:
    - Neoverse
tools_software_languages: 
    - .NET
    - Orchard Core
    - C
operatingsystems:
    - Linux

further_reading:
    - resource:
        title: Orchard Core documentation
        link: https://docs.orchardcore.net/
        type: documentation  
    - resource:
        title: OrchardCore GitHub Repository
        link: https://github.com/OrchardCMS/OrchardCore
        type: documentation
    - resource:
        title: .NET documentation
        link: https://learn.microsoft.com/en-us/dotnet/
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
