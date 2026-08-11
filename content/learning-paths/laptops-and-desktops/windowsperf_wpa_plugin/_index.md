---
title: Get started with the Windows Performance Analyzer (WPA) plugin for WindowsPerf

description: Learn how to import WindowsPerf data in Windows Performance Analyzer (WPA) and visualize timeline and telemetry data using the WPA plugin.

minutes_to_complete: 15

who_is_this_for: This is an introductory topic for software developers interested in using the Windows Performance Analyzer (WPA) plugin for performance analysis.

learning_objectives:
    - Import WindowsPerf data as a .json file in WPA.
    - Visualize the timeline and telemetry data in WPA using the WPA plugin.

prerequisites:
    - A Windows on Arm laptop with WindowsPerf, Windows Performance Analyzer (WPA), and the WPA plugin installed.

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-11T16:27:59Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 61b40f83405e1a04315a61c2dd66a56e6604d3fee26d833039cf392f479b884f
  summary_generated_at: '2026-08-11T16:27:59Z'
  summary_source_hash: 61b40f83405e1a04315a61c2dd66a56e6604d3fee26d833039cf392f479b884f
  faq_generated_at: '2026-08-11T16:27:59Z'
  faq_source_hash: 61b40f83405e1a04315a61c2dd66a56e6604d3fee26d833039cf392f479b884f
  summary: >-
    You'll import WindowsPerf data into Windows Performance Analyzer (WPA) on Windows on Arm. You'll
    use `wperf stat` to capture data and save it as a `.json` file with `--output`, then open it
    in WPA. You'll inspect the plugin's timeline and telemetry views to verify recorded events and
    visualize the resulting data.
  faqs:
  - question: How do I generate the `.json` file to import into WPA?
    answer: >-
      Run WindowsPerf with the `wperf stat` command on a Windows on Arm system and save the output
      as a `.json` file using the `--output` option.
  - question: How do I confirm the WPA plugin is installed correctly?
    answer: >-
      Open the WindowsPerf `.json` file in WPA. If the plugin is installed correctly, WPA loads the data and
      exposes the plugin’s timeline and telemetry visualizations.
  - question: What result should I expect after I import the JSON into WPA?
    answer: >-
      You should see timeline and telemetry data corresponding to the WindowsPerf run. The plugin
      presents these views inside WPA for inspection.
  - question: What should I check if WPA fails to open my JSON file?
    answer: >-
      Verify the file was created by `wperf stat` on a Windows on Arm machine and saved as `.json`
      with the `--output` option. Also confirm the WPA plugin is installed using its install guide.
  - question: How do I view counting timeline data in WPA?
    answer: >-
      Collect data with `wperf stat` using the `-t` option, then open the generated `.json` file in
      WPA. In Graph Explorer, expand **Counting timeline** to view the recorded events by core or event.
# END generated_summary_faq

author: Alaaeddine Chakroun

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
armips:
    - Cortex-A
    - Neoverse
operatingsystems:
    - Windows
tools_software_languages:
    - WindowsPerf
    - perf
    - Windows Performance Analyzer

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
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
