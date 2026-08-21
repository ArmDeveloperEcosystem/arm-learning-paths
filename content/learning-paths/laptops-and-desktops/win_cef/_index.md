---
title: Develop desktop applications with Chromium Embedded Framework on Windows on Arm

description: Learn how to create and build Chromium Embedded Framework desktop applications using CMake and web technologies on Windows on Arm.

minutes_to_complete: 30

who_is_this_for: This learning path is for developers who want to learn how to use web technologies for developing Desktop apps on Windows on Arm (WoA).

learning_objectives:
    - Create and build a Chromium Embedded Framework (CEF) project using CMake
    - Modify and style the application

prerequisites:
    - A Windows on Arm computer such as the Lenovo Thinkpad X13s running Windows 11 or a Windows on Arm [virtual machine](/learning-paths/cross-platform/woa_azure/).
    - Visual Studio 2022.

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-11T16:17:56Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 995ccce630912ea85925d7b3e6ad9191bbfcbd76f31186f68a579b4ced21d522
  summary_generated_at: '2026-08-11T16:17:56Z'
  summary_source_hash: 995ccce630912ea85925d7b3e6ad9191bbfcbd76f31186f68a579b4ced21d522
  faq_generated_at: '2026-08-11T16:17:56Z'
  faq_source_hash: 995ccce630912ea85925d7b3e6ad9191bbfcbd76f31186f68a579b4ced21d522
  summary: >-
    You'll create a CEF desktop application on Windows on Arm using
    CMake and C++. First, you'll configure the project for Visual Studio 2022, build it, and launch a
    Chromium-based window. Then, you'll integrate local HTML, CSS, and JavaScript assets to build a project that you can iterate on with familiar web technologies.
  faqs:
  - question: Which CMake generator should I pick in Visual Studio on Windows on Arm?
    answer: >-
      Pick the Visual Studio generator that matches your installed Visual Studio 2022. If you
      open the folder as a CMake project in Visual Studio, let the IDE configure it and choose
      a configuration that targets Windows on Arm.
  - question: What should I see when I run the built application?
    answer: >-
      A desktop window backed by Chromium should launch and render the default page included in
      the project. Seeing a basic template or sample content confirms the embedded browser is
      running.
  - question: Where should I put my HTML, CSS, and JavaScript so the app can load them?
    answer: >-
      Place assets in the locations referenced by the starter project or by paths in the application
      code. If the content doesn't appear, check that the file paths are correct relative to
      the working directory used at runtime.
  - question: How do I confirm I’m building for Windows on Arm and not another architecture?
    answer: >-
      Check the build output for the target platform when you run
      `cmake -G "Visual Studio 17" -A arm64 -B build` before building.
  - question: What should I check if the window opens but shows a blank or unstyled page?
    answer: >-
      Verify that the initial URL or local file path the application loads is correct and accessible.
      Update the asset location or move the assets to the expected location, then rebuild and run again.
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
    - CPP
    - CMake 
    - HTML
    - JavaScript
    - CSS

further_reading:
    - resource:
        title: CEF GitHub Repository
        link: https://github.com/chromiumembedded/cef
        type: documentation
    - resource:
        title: Chromium Embedded Framework
        link: https://en.wikipedia.org/wiki/Chromium_Embedded_Framework
        type: website   

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
