---
title: Port Applications to Arm64 using Arm64EC

description: Learn how to port Qt-based Python desktop applications with C/C++ dependencies to Arm64 using Arm64EC on Windows on Arm.

minutes_to_complete: 90

who_is_this_for: This is an introductory topic for developers who want to learn how to port their applications to Arm64 using Arm64EC. 

learning_objectives:
    - Build a Qt-based Python desktop application
    - Create C/C++ dependencies and use them in the Qt-based Python app
    - Learn how to port the C/C++ based dependencies to Arm64 using Arm64EC

prerequisites:
    - A Windows on Arm computer such as the Lenovo Thinkpad X13s running Windows 11 or a Windows on Arm [virtual machine](/learning-paths/cross-platform/woa_azure/).
    - Any code editor. [Visual Studio Code for Arm64](https://code.visualstudio.com/docs/?dv=win32arm64user) is suitable.
    - Visual Studio 2022 with Arm build tools. [Refer to this guide for the installation steps](https://developer.arm.com/documentation/102528/0100/Install-Visual-Studio).
    

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T23:18:19Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 3b3ecd451ed8b634c7fbe194248cdf1d33432633efbcbef5de713495041ff425
  summary_generated_at: '2026-06-01T22:12:11Z'
  summary_source_hash: 3b3ecd451ed8b634c7fbe194248cdf1d33432633efbcbef5de713495041ff425
  faq_generated_at: '2026-06-02T23:18:19Z'
  faq_source_hash: 3b3ecd451ed8b634c7fbe194248cdf1d33432633efbcbef5de713495041ff425
  summary: >-
    This Learning Path shows how to port a Qt-based Python desktop application with C/C++ dependencies
    to Arm64 on Windows using Arm64EC. You will build the app, create C/C++ DLLs, and port each
    DLL to Arm64 by configuring Arm64EC targets with both CMake (editing CMakePresets.json) and
    MSBuild in Visual Studio 2022. Arm64EC allows Arm64 binaries and existing x64 dependencies
    to run in the same process, enabling staged migration. The target environment is Windows on
    Arm hardware running Windows 11 or a Windows on Arm virtual machine. Prerequisites are Visual
    Studio 2022 with Arm build tools and a code editor such as Visual Studio Code for Arm64. Estimated
    time to complete is about 90 minutes.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need a Windows on Arm computer running Windows 11 or a Windows on Arm virtual machine,
      any code editor (Visual Studio Code for Arm64 is suitable), and Visual Studio 2022 with
      Arm build tools installed.
  - question: 'Which option should I use to port DLLs: CMake or MSBuild?'
    answer: >-
      Use the option that matches your project. This path demonstrates both: CMake (used earlier
      in the path) and MSBuild with Visual Studio 2022.
  - question: How do I enable Arm64EC for a CMake project in this path?
    answer: >-
      Modify the CMakePresets.json file by adding the final statement block shown in the steps
      to configure the build target for Arm64EC. This config lets you build the DLLs for Arm64EC.
  - question: How do I set up an MSBuild project for Arm64EC in Visual Studio 2022?
    answer: >-
      Create a new Console Application project in Visual Studio 2022 and set the build target
      to Arm64EC. The steps provide example solution and project names to guide the configuration.
  - question: What result should I expect after building with Arm64EC?
    answer: >-
      Your application can load existing x64 dependencies in the same process as your Arm64 binaries,
      easing the transition of x64 apps to Arm64. As described in the introduction, this approach
      can improve app performance without changing code.
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
    - Qt    

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

