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

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T23:20:57Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: e60ce02e9d1872da06bc5bfeb18c7ec65f2bc17defb2b75292f930fb3ad41711
  summary_generated_at: '2026-06-01T22:13:07Z'
  summary_source_hash: e60ce02e9d1872da06bc5bfeb18c7ec65f2bc17defb2b75292f930fb3ad41711
  faq_generated_at: '2026-06-02T23:20:57Z'
  faq_source_hash: e60ce02e9d1872da06bc5bfeb18c7ec65f2bc17defb2b75292f930fb3ad41711
  summary: >-
    Follow this advanced, approximately 30-minute Learning Path to build and run an ASP.NET Core
    8 Web API on Windows on Arm (Arm64). You will create a project that uses dependency injection
    for services, build it with the .NET 8 SDK for arm64, run it locally, and confirm from console
    output that the server is listening on localhost. The target environment is a Windows 11 on
    Arm device such as a Lenovo ThinkPad X13s or a Windows on Arm virtual machine, using any code
    editor (Visual Studio Code for Arm64 recommended). By the end, you will have a working ASP.NET
    Core 8 web server suitable as a starting point for headless IoT scenarios on Arm.
  faqs:
  - question: What do I need before running this Learning Path?
    answer: >-
      You need a Windows on Arm computer running Windows 11 or a Windows on Arm virtual machine,
      the .NET 8 SDK for arm64, and a code editor. Visual Studio Code for Arm64 is recommended,
      but any editor will work.
  - question: How do I create and run the ASP.NET Core Web API project on Windows on Arm?
    answer: >-
      Follow the steps to create the Web API project, then open a command prompt, change to the
      project folder, and run the application. The path shows using dotnet run to build and start
      the server.
  - question: What result should I expect when the server starts successfully?
    answer: >-
      The console output will indicate the server is listening on a localhost URL and that the
      application has started in the Development environment. The example output shows a line
      like “Now listening on: http://localhost:5203”.
  - question: What should I check if dotnet run doesn’t show a listening address?
    answer: >-
      Confirm the .NET 8 SDK for arm64 is installed and that you are in the project’s directory
      before running the command. Rebuild from the project folder and review the console output
      for build errors.
  - question: How are dependency injection services used in this path?
    answer: >-
      You will create services and consume them via ASP.NET Core’s built-in dependency injection.
      The steps guide you to register and use these services from your Web API.
# END generated_summary_faq

author: Dawid Borycki

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

