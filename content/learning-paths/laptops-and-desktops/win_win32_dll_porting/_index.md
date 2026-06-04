---
title: How to port the Win32 library to Arm64

description: Learn how to create C/C++ Win32 DLLs and port them to Arm64 for use in Windows console applications.

minutes_to_complete: 90

who_is_this_for: This is an introductory topic for developers who want to learn how to port their Win32 applications to Arm64 

learning_objectives:
    - Create C/C++ Win32 DLL
    - Use Win32 DLL in the Console App
    - Learn how to port the C/C++ Win32 DLL to Arm64

prerequisites:
    - A Windows on Arm computer such as the Lenovo Thinkpad X13s running Windows 11 or a Windows on Arm [virtual machine](/learning-paths/cross-platform/woa_azure/).    
    - Refer to [Visual Studio 2022 with Arm build tools](/install-guides/vs-woa).
    

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T23:31:50Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: cacf4c6fc3cd3c2a9ab194f7a04981fd4820fca5482317a06c6b9fa02a1c9da2
  summary_generated_at: '2026-06-01T22:19:36Z'
  summary_source_hash: cacf4c6fc3cd3c2a9ab194f7a04981fd4820fca5482317a06c6b9fa02a1c9da2
  faq_generated_at: '2026-06-02T23:31:50Z'
  faq_source_hash: cacf4c6fc3cd3c2a9ab194f7a04981fd4820fca5482317a06c6b9fa02a1c9da2
  summary: >-
    This introductory Learning Path shows how to create a C/C++ Win32 DLL, use it from a Windows
    console application, and port the library to Arm64 for Windows on Arm. You work on a Windows
    on Arm device such as a Lenovo Thinkpad X13s running Windows 11 or a Windows on Arm virtual
    machine, using Visual Studio 2022 with Arm build tools. The steps include a brief overview
    of Armv8-A Arm64 concepts and focus on building and running the console app that consumes
    your DLL on Arm64. By the end, you will have exercised a practical migration workflow for
    a Win32 library to Arm64.
  faqs:
  - question: What do I need installed before starting?
    answer: >-
      Use a Windows on Arm computer or a Windows on Arm virtual machine and refer to the Visual
      Studio 2022 with Arm build tools installation guide. No other prerequisites are explicitly
      listed.
  - question: Can I complete this on a virtual machine instead of physical hardware?
    answer: >-
      Yes. The prerequisites explicitly allow a Windows on Arm virtual machine as an alternative
      to a Windows on Arm device.
  - question: What will I build and target by the end?
    answer: >-
      You will create a C/C++ Win32 DLL and a Windows console application that uses it, with both
      projects targeting Arm64 on Windows on Arm.
  - question: How do I choose the correct build target for Arm64?
    answer: >-
      The steps show how to configure your projects in Visual Studio 2022 with Arm build tools
      to build for Arm64. Follow the project configuration guidance provided in the path.
  - question: What should I check if my Arm64 build fails or the app cannot load the DLL?
    answer: >-
      Verify that Visual Studio 2022 with Arm build tools is installed, the project target is
      set to Arm64, and you are building and running on a Windows on Arm environment. Revisit
      the configuration steps to confirm the platform settings.
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
    - C
    - CPP     

further_reading:
    - resource:
        title: Arm64EC - Build and port apps for native performance on Arm
        link: https://learn.microsoft.com/en-us/windows/arm/arm64ec
        type: documentation
    - resource:
        title: Visual Studio on Arm-powered devices
        link: https://learn.microsoft.com/en-us/visualstudio/install/visual-studio-on-arm-devices?view=vs-2022
        type: documentation
    - resource:
        title: Load x64 Plug-ins (like VSTs) from your Arm Code using Arm64EC
        link: https://devblogs.microsoft.com/windows-music-dev/load-x64-plug-ins-like-vsts-from-your-arm-code-using-arm64ec/
        type: blog    


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

