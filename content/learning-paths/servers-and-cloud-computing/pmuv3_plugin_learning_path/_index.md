---
title: Implement code-level performance analysis using the PMUv3 plugin 

minutes_to_complete: 60

who_is_this_for: Engineers who want to carry out C or C++ performance analysis by instrumenting code at the block level.

learning_objectives: 
    - Generate a fine-grained, precise measurement of functions and other sections of code.
    - Instrument your code to analyze a single section or multiple sections.
    - Run and collect performance metrics and raw event values for any of the 15 event groups (bundles) in a single run.
    - Use a tool to plot raw PMU event values along with KPI metric values such as MPKI, stalls, and IPC to aid performance visualization.

prerequisites:
    - An Arm-based computer running Linux, such as an Arm AGI CPU platform
    - Some familiarity with Linux application performance analysis

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-11-18T20:24:31Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 996e16308e0deb510bb0872bbeb1111dc7c628318b9befae1f883e2dcd6fc369
  summary_generated_at: '2026-11-18T20:24:31Z'
  summary_source_hash: 996e16308e0deb510bb0872bbeb1111dc7c628318b9befae1f883e2dcd6fc369
  faq_generated_at: '2026-11-18T20:24:31Z'
  faq_source_hash: 996e16308e0deb510bb0872bbeb1111dc7c628318b9befae1f883e2dcd6fc369
  summary: >-
    You'll instrument C code with the PMUv3 plugin to measure selected regions on Arm-based
    Linux. First, you'll enable user-space PMU access and build the plugin. Then, you'll add headers
    and measurement calls to one code section before extending to multiple sections.
    Finally, you'll plot raw counter values and derived metrics to compare the measured regions.
  faqs:
  - question: How do I know userspace PMU access is enabled before I run the plugin?
    answer: >-
      Run `cat /proc/sys/kernel/perf_user_access` and check that it prints `1`. If needed, run
      `sudo sysctl kernel/perf_user_access=1` to enable user-space access.
  - question: What do I do if PMU access fails after a reboot?
    answer: >-
      Run `sudo sysctl kernel/perf_user_access=1` again after a reboot. The setting doesn't
      persist across restarts.
  - question: How should I organize my directories before I instrument my application?
    answer: >-
      Keep three parallel directories: the Linux kernel source tree, the PMUv3 plugin source,
      and a test application directory. If your layout differs, adjust your build to locate the
      plugin headers and libraries.
  - question: How do I identify each code section when collecting PMUv3 counters?
    answer: >-
      Initialize the bundle once, then give each section its own marker and index in the start and stop calls. The output labels the measurements by section.
  - question: What should I expect from the plotting tool, and how do I confirm my run captured data?
    answer: >-
      Use the Python plotting program to inspect raw PMU events and metrics such as MPKI,
      stalls, and IPC. Check that your plots contain data for the instrumented regions.
# END generated_summary_faq

author: Gayathri Narayana Yegna Narayanan

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
platforms:
    - Arm AGI CPU
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

