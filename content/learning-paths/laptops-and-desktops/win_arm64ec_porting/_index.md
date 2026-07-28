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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-28T16:27:42Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 3b3ecd451ed8b634c7fbe194248cdf1d33432633efbcbef5de713495041ff425
  summary_generated_at: '2026-07-28T16:27:42Z'
  summary_source_hash: 3b3ecd451ed8b634c7fbe194248cdf1d33432633efbcbef5de713495041ff425
  faq_generated_at: '2026-07-28T16:27:42Z'
  faq_source_hash: 3b3ecd451ed8b634c7fbe194248cdf1d33432633efbcbef5de713495041ff425
  summary: >-
    This Learning Path shows how to port a Qt-based Python desktop application with C/C++ DLL
    dependencies to Arm64 on Windows by configuring Arm64EC. Learners build the app, then choose
    a porting path that matches the project: update CMake by adding a statement block to CMakePresets.json,
    or create and configure a Visual Studio MSBuild project. Arm64EC enables Arm64 binaries to
    load existing x64 dependencies in the same process, so you can migrate components incrementally.
    By the end, learners configure builds for Arm64EC, port DLLs, and understand how to run mixed
    Arm64 and x64 components during the transition.
  faqs:
  - question: Should I use CMake or MSBuild to port my DLLs?
    answer: >-
      Use the build system your project already uses. This path demonstrates both approaches,
      and if you followed earlier steps with CMake, continue with the CMake method.
  - question: How do I know I'm targeting Arm64EC?
    answer: >-
      Verify that your preset or project configuration sets the build target to Arm64EC and matches
      the example shown in the step. A successful build with that target confirms the configuration
      is applied.
  - question: What do I change in CMake to port a DLL?
    answer: >-
      Edit CMakePresets.json and add the final statement block so the file matches the provided
      example. Rebuild to produce the Arm64EC build of the DLL.
  - question: In Visual Studio, which setting do I use to build for Arm64EC?
    answer: >-
      Create the Console Application project and set the build target to Arm64EC as described
      in the step. Use the specified project names and confirm the platform configuration before
      building.
  - question: Can I keep some dependencies as x64 while I port others?
    answer: >-
      Yes. Arm64EC allows x64 dependencies to load in the same process as Arm64 binaries, enabling
      incremental migration of components.
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

