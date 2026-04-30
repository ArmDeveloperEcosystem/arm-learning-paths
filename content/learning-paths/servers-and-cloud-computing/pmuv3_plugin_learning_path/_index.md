---
title: Implement Code level Performance Analysis using the PMUv3 plugin 

minutes_to_complete: 60

who_is_this_for: Engineers who want to carry out C/C++ performance analysis by instrumenting code at the block level.

learning_objectives: 
    - Generate a fine-grained, precise measurement of functions and other sections of code.
    - Instrument your code to analyze a single section or multiple sections using the provided instrumentation scenarios.
    - Run and collect performance metrics and raw event values for any of the 15 event groups (bundles) in a single run.
    - Use a tool to plot raw PMU event values along with KPI metric values such as MPKI, stalls, and IPC to aid performance visualization.

prerequisites:
    - An Arm-based computer running Linux.
    - Some familiarity with Linux application performance analysis.

generate_summary_faq: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-04-30T18:58:19Z'
  generator: template
  source_hash: 3ec6ae40daff557dd05cd092ff7d6b5a63954a1618605030a443f56fe5ffe490
  summary: >-
    Implement Code level Performance Analysis using the PMUv3 plugin walks you through an end-to-end
    Arm software workflow. It is designed for Engineers who want to carry out C/C++ performance
    analysis by instrumenting code at the block level. By the end, you will be able to generate
    a fine-grained, precise measurement of functions and other sections of code, instrument your
    code to analyze a single section or multiple sections using the provided instrumentation scenarios,
    and run and collect performance metrics and raw event values for any of the 15 event groups
    (bundles) in a single run. It focuses on tools and technologies such as C, CPP, Python, and
    Runbook, Linux environments, and Arm platforms including Neoverse. The main steps cover PMUv3
    plugin features, Download and build the PMUv3 plugin, Instrument one section of code, Plot,
    visualize, and analyze the results, and Instrument multiple sections of code.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will generate a fine-grained, precise measurement of functions and other sections of
      code, instrument your code to analyze a single section or multiple sections using the provided
      instrumentation scenarios, and run and collect performance metrics and raw event values
      for any of the 15 event groups (bundles) in a single run.
  - question: Who is this Learning Path for?
    answer: >-
      Engineers who want to carry out C/C++ performance analysis by instrumenting code at the
      block level.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: An Arm-based computer running Linux.;
      Some familiarity with Linux application performance analysis.
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including C, CPP, Python, and Runbook, Linux environments,
      and Arm platforms such as Neoverse.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around PMUv3 plugin features, Download and build the PMUv3
      plugin, Instrument one section of code, Plot, visualize, and analyze the results, and Instrument
      multiple sections of code.
# END generated_summary_faq

author: Gayathri Narayana Yegna Narayanan

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
armips:
    - Neoverse
tools_software_languages:
    - C
    - CPP
    - Python
    - Runbook

operatingsystems:
    - Linux


further_reading:
    - resource:
        title: Arm Neoverse N2 PMU Guide
        link: https://developer.arm.com/documentation/PJDOC-466751330-590448/2-0/?lang=en
        type: documentation
    - resource:
        title: Arm CPU Telemetry Solution Topdown Methodology Specification
        link: https://developer.arm.com/documentation/109542/0100/?lang=en
        type: documentation
    - resource:
        title: Arm Neoverse N2 Core Telemetry Specification
        link: https://developer.arm.com/documentation/109215/0200/?lang=en
        type: documentation


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

