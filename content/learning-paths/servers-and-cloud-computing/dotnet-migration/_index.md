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

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T00:44:01Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 08d8f0c86625ef41476d3a8b24bad9b0a0820797022ef847bf9bb17a976726a7
  summary_generated_at: '2026-06-02T03:38:20Z'
  summary_source_hash: 08d8f0c86625ef41476d3a8b24bad9b0a0820797022ef847bf9bb17a976726a7
  faq_generated_at: '2026-06-03T00:44:01Z'
  faq_source_hash: 08d8f0c86625ef41476d3a8b24bad9b0a0820797022ef847bf9bb17a976726a7
  summary: >-
    Learn how to migrate and run an OrchardCore CMS .NET application on Azure Cobalt 100 Arm-based
    virtual machines. You will build and run the app on Ubuntu 24.04 with port 8080 open, integrate
    a simple C shared library that is invoked from C# via DllImport, and configure .NET AnyCPU
    so the same build runs on both Arm and x86. The path also reviews .NET version choices and
    support status to help you evaluate behavior on Arm. Prerequisites include an Azure account
    with VM permissions, .NET SDK 8.0 or later, GCC or a cross-compiler, basic C and C# knowledge,
    and an OrchardCore app created with the .NET CLI or Visual Studio.
  faqs:
  - question: What do I need in Azure before I start?
    answer: >-
      You need a Microsoft Azure account with permissions to deploy virtual machines. The path
      assumes you can create and configure an Azure Cobalt 100 instance.
  - question: Which VM image and network settings should I use for the OrchardCore app?
    answer: >-
      Launch an Azure Cobalt 100 (Arm-based) VM running Ubuntu 24.04 and open port 8080 to the
      internet. If you need help creating the VM, see the Create an Azure Cobalt 100 VM Learning
      Path.
  - question: What tools and project setup are required on the VM?
    answer: >-
      Install .NET SDK 8.0 or later and ensure GCC is available on Linux (or use a cross-compiler).
      You should also have an OrchardCore application created using the .NET CLI or Visual Studio,
      and basic knowledge of C and C#.
  - question: How do I build the C shared library and verify it is called from .NET?
    answer: >-
      Compile the C source with: gcc -shared -o libmylib.so -fPIC mylib.c, which produces libmylib.so.
      Call the function from C# via DllImport; when invoked, it prints: Hello from the C library!.
  - question: How do I run the same build on both Arm and x86 machines?
    answer: >-
      Use .NET’s AnyCPU configuration to produce an architecture-agnostic build. The path shows
      how to configure and run the OrchardCore app so it can execute on Arm-based cloud VMs as
      well as x86 systems.
# END generated_summary_faq

author: Joe Stech

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

