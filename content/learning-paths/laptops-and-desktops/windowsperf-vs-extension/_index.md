---
title: Analyze performance data with the Visual Studio extension for WindowsPerf

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
  - Visual Studio 2022 Community Edition, WindowsPerf, WindowsPerf Visual Studio extension, and WPA installed.

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-11T16:25:59Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 4b88beee8d8aa7ec61969d8a7278dd37f65c97562c7db0a514819b2c56a3561b
  summary_generated_at: '2026-08-11T16:25:59Z'
  summary_source_hash: 4b88beee8d8aa7ec61969d8a7278dd37f65c97562c7db0a514819b2c56a3561b
  faq_generated_at: '2026-08-11T16:25:59Z'
  faq_source_hash: 4b88beee8d8aa7ec61969d8a7278dd37f65c97562c7db0a514819b2c56a3561b
  summary: >-
    You'll integrate WindowsPerf into Visual Studio 2022 on Windows on Arm to collect and review
    performance data. First, you'll configure the required tools, run counting sessions from **View** >
    **Counting Settings**, and inspect the results. Then, you'll use **View** > **Sampling Explorer**
    to analyze samples and use the Arm Statistical Profiling Extension (SPE) when supported.
  faqs:
  - question: How do I know the WindowsPerf Visual Studio extension is installed correctly?
    answer: >-
      In Visual Studio 2022, the **View** menu should include **Counting Settings** and **Sampling Explorer**.
      If these entries are missing, check that the extension is installed and that you are running
      Visual Studio 2022 on Windows on Arm.
  - question: Where do I configure which events are counted before collecting data?
    answer: >-
      Open **View** > **Counting Settings** to display the **Counting Settings** dialog. Use this dialog to
      review and adjust the available parameters for your run.
  - question: What result should I expect after a counting run?
    answer: >-
      The extension produces a counting report you can explore in Visual Studio. You can then
      open the report in WPA using the WindowsPerf WPA plugin.
  - question: How do I start a sampling session and set its preferences?
    answer: >-
      Open **View** > **Sampling Explorer**, then select the **Configure the sampling command** icon to set
      preferences. Start the sampling run from **Sampling Explorer** and review the results when
      it completes.
  - question: What does it mean if I don't see any SPE options in the sampling workflow?
    answer: >-
      Your system doesn't support SPE. The SPE feature is available only on hardware that supports it. If your system doesn't support SPE, use the standard sampling feature instead.
# END generated_summary_faq

author: 
  - Nader Zouaoui

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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
