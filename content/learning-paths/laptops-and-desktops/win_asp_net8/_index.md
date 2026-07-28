---
title: Run ASP.NET Core Web Server on Arm64

description: Learn how to build and run an ASP.NET Core 8 web server application with Web API and dependency injection services on Windows on Arm.

minutes_to_complete: 30

who_is_this_for: This is an advanced topic for developers who are interested in building a web server for a headless IoT applications.

learning_objectives:
   - Build and run an ASP.NET Core 8 application
   - Create a Web API
   - Create and use services using the dependency injection

prerequisites:
    - A Windows on Arm computer such as the Lenovo Thinkpad X13s running Windows 11 or a Windows on Arm [virtual machine](/learning-paths/cross-platform/woa_azure/).
    - .NET 8 SDK for [arm64](https://dotnet.microsoft.com/en-us/download/dotnet/thank-you/sdk-8.0.100-windows-arm64-installer).
    - Any code editor, we recommend using [Visual Studio Code for Arm64](https://code.visualstudio.com/docs/?dv=win32arm64user).

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-28T16:29:16Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: e60ce02e9d1872da06bc5bfeb18c7ec65f2bc17defb2b75292f930fb3ad41711
  summary_generated_at: '2026-07-28T16:29:16Z'
  summary_source_hash: e60ce02e9d1872da06bc5bfeb18c7ec65f2bc17defb2b75292f930fb3ad41711
  faq_generated_at: '2026-07-28T16:29:16Z'
  faq_source_hash: e60ce02e9d1872da06bc5bfeb18c7ec65f2bc17defb2b75292f930fb3ad41711
  summary: >-
    This Learning Path shows how to create, build, and run an ASP.NET Core 8 Web API on Windows
    on Arm for a headless IoT scenario. You start a new Web API project, then build and launch
    it with the .NET CLI. The runtime output helps you verify success by printing the hosting
    environment and the localhost URL where the server listens. Learners add services using ASP.NET
    Core’s built-in dependency injection and use them from controllers, then access the API from
    a browser or HTTP client. By the end, you can recognize a successful startup from the console
    logs and interact with a running Arm64 web server.
  faqs:
  - question: Which project template should I pick to start?
    answer: >-
      Use the ASP.NET Core Web API project template. The path uses Arm64.HeadlessIoT as an example
      project name, but any name works.
  - question: Where should I run dotnet run from?
    answer: >-
      Run it from the project directory that contains the .csproj file. This ensures the CLI builds
      and starts the correct project.
  - question: How do I know the server started correctly?
    answer: >-
      Check the console for lines such as "Now listening on: http://localhost:PORT" and "Application
      started. Press Ctrl+C to shut down." The output also shows the hosting environment (for
      example, Development).
  - question: How do I access the API endpoint locally?
    answer: >-
      Open the exact localhost URL printed in the console in a browser or an HTTP client. Use
      the scheme, host, and port shown after "Now listening on:".
  - question: How do I stop the server when I’m done?
    answer: >-
      Press Ctrl+C in the terminal where the app is running. The process exits and the server
      stops listening on the local port.
# END generated_summary_faq

author: Dawid Borycki

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
subjects: Migration to Arm
armips:
    - Cortex-A
operatingsystems:
    - Windows
tools_software_languages:
    - .NET    
    - Visual Studio Code

further_reading:
    - resource:
        title: Cross-Platform IoT Programming with .NET Core 3.0
        link: https://learn.microsoft.com/en-us/archive/msdn-magazine/2019/august/net-core-cross-platform-iot-programming-with-net-core-3-0
        type: article
    - resource:
        title: Deploy .NET apps on Arm single-board computers
        link: https://learn.microsoft.com/en-us/dotnet/iot/deployment
        type: documentation
    - resource:
        title: ASP.NET Core
        link: https://dotnet.microsoft.com/en-us/apps/aspnet
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

