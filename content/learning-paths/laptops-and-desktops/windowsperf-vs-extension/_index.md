---
title: Learn how to use the Visual Studio extension for WindowsPerf

description: Learn how to install and use the WindowsPerf Visual Studio extension to generate counting and sampling reports and analyze performance data in Windows Performance Analyzer.

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for software developers using Visual Studio on Windows on Arm who want to integrate WindowsPerf into their development flow.

learning_objectives:
  - Install and use the WindowsPerf Visual Studio extension.
  - Generate a counting report and explore the data.
  - Review the report in Windows Performance Analyzer (WPA). 
  - Generate a sample report and explore the data.

prerequisites:
  - A desktop or laptop running Windows on Arm.
  - Visual Studio 2022 Community Edition, WindowsPerf, WindowsPerf Visual Studio extension, and Windows Performance Analyzer (WPA) installed. 

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T23:36:56Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 1dd709b14537e06c80b9cdee58729cfa7066f44f0de4ceabe5450b33288731aa
  summary_generated_at: '2026-06-02T02:37:03Z'
  summary_source_hash: 1dd709b14537e06c80b9cdee58729cfa7066f44f0de4ceabe5450b33288731aa
  faq_generated_at: '2026-06-02T23:36:56Z'
  faq_source_hash: 1dd709b14537e06c80b9cdee58729cfa7066f44f0de4ceabe5450b33288731aa
  summary: >-
    This introductory Learning Path shows how to install and use the WindowsPerf Visual Studio
    extension on Windows on Arm to generate counting and sampling reports and analyze performance
    data in Windows Performance Analyzer (WPA). You configure Visual Studio 2022 Community Edition
    with WindowsPerf, the WindowsPerf extension, and the WPA tooling, then run counting and sampling
    sessions from within Visual Studio. You review results in Visual Studio and in WPA, and, if
    your hardware supports it, explore the SPE subset of the sampling feature. By the end, you
    can produce and examine WindowsPerf reports as part of a Windows on Arm development workflow.
    No additional prerequisites are listed beyond the required tools.
  faqs:
  - question: What do I need installed before I start?
    answer: >-
      You need a Windows on Arm desktop or laptop with Visual Studio 2022 Community Edition, WindowsPerf,
      the WindowsPerf Visual Studio extension, and Windows Performance Analyzer (WPA). The Learning
      Path provides install guides for each tool.
  - question: How do I open and configure the counting settings in Visual Studio?
    answer: >-
      In Visual Studio 2022, open the View menu and select Counting Settings to open the dialog.
      From there, configure the counting parameters as shown in the Learning Path.
  - question: How do I generate a counting report and review it in WPA?
    answer: >-
      After configuring counting, generate a report in Visual Studio and explore the data in the
      IDE. You can then review the report in Windows Performance Analyzer (WPA) using the WindowsPerf
      WPA plugin described in the Learning Path.
  - question: Where do I find the sampling tools and set sampling preferences?
    answer: >-
      Open the View menu in Visual Studio 2022 and select Sampling Explorer. In the Sampling Explorer
      window, use the Configure the sampling command icon to set your preferences.
  - question: What should I check if the SPE feature does not work on my system?
    answer: >-
      The SPE section requires hardware that supports the Arm Statistical Profiling Extension.
      If your CPU does not support SPE, this feature will not function and you should proceed
      with the general Sampling feature instead.
# END generated_summary_faq

author: 
  - Nader Zouaoui

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
armips:
  - Cortex-A
operatingsystems:
  - Windows
tools_software_languages:
  - WindowsPerf
  - perf
  - Visual Studio

further_reading:
  - resource:
      title: Announcing WindowsPerf Open-source performance analysis tool for Windows on Arm
      link: https://developer.arm.com/community/arm-community-blogs/b/servers-and-cloud-computing-blog/posts/announcing-windowsperf
      type: blog
  - resource:
      title: WindowsPerf Release 3.7.2
      link: https://www.linaro.org/blog/expanding-profiling-capabilities-with-windowsperf-372-release/
      type: blog
  - resource:
      title: WindowsPerf Visual Studio Extension v2.1.0
      link: https://www.linaro.org/blog/launching--windowsperf-visual-studio-extension-v210/
      type: blog
  - resource:
      title: Windows on Arm overview
      link: https://learn.microsoft.com/en-us/windows/arm/overview
      type: website
  - resource:
      title: Linaro Windows on Arm project
      link: https://www.linaro.org/windows-on-arm/
      type: website
  - resource:
      title: WindowsPerf Visual Studio extension releases
      link: https://github.com/arm-developer-tools/windowsperf-vs-extension/releases
      type: website
  - resource:
      title: WindowsPerf releases
      link: https://github.com/arm-developer-tools/windowsperf/releases
      type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1 # _index.md always has weight of 1 to order correctly
layout: "learningpathall" # All files under learning paths have this same wrapper
learning_path_main_page: "yes" # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

