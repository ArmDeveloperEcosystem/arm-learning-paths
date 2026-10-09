---
title: Port the Win32 library to Arm64

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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-11T16:22:38Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: e9ee967b66e4ee21d2de58923e1049cd0e28ed055297e96f8811ede5af6f6daf
  summary_generated_at: '2026-08-11T16:22:38Z'
  summary_source_hash: e9ee967b66e4ee21d2de58923e1049cd0e28ed055297e96f8811ede5af6f6daf
  faq_generated_at: '2026-08-11T16:22:38Z'
  faq_source_hash: e9ee967b66e4ee21d2de58923e1049cd0e28ed055297e96f8811ede5af6f6daf
  summary: >-
    You'll create a C++ Win32 dynamic-link library (DLL) and use it from a Windows console application.
    First, you'll configure both projects for Arm64, rebuild them, and verify that the console app loads
    and calls the DLL successfully. Then, you'll switch between x64 and Arm64 builds to compare
    execution time on Windows on Arm.
  faqs:
  - question: Which projects do I need to create to follow this path?
    answer: >-
      Create a C++ Win32 DLL and a Windows console application that uses the DLL. The console
      app should call at least one exported function from the DLL.
  - question: How do I know the build produced Arm64 binaries?
    answer: >-
      Build the projects with an Arm64 target and run the resulting console app on Windows on
      Arm. If the app starts and calls into the DLL without loader errors, the artifacts match
      the expected architecture.
  - question: What should I check if the console app can't load the DLL after retargeting?
    answer: >-
      Verify that both the DLL and console app are built for the same architecture (Arm64). Also
      confirm the DLL is in the app’s runtime search path when you launch the executable.
  - question: How do I switch between x64 and Arm64 builds?
    answer: >-
      Select **x64** or **ARM64** from the platform dropdown, then select **Local Windows Debugger**.
      Run both configurations and compare the execution times reported by the application.
  - question: Can I complete this on a Windows on Arm virtual machine?
    answer: >-
      Yes. You can use a Windows on Arm computer or a Windows on Arm virtual machine.
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
