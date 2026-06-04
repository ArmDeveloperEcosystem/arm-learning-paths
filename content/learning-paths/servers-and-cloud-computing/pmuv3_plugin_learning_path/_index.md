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

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T01:50:24Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 3ec6ae40daff557dd05cd092ff7d6b5a63954a1618605030a443f56fe5ffe490
  summary_generated_at: '2026-06-02T04:48:11Z'
  summary_source_hash: 3ec6ae40daff557dd05cd092ff7d6b5a63954a1618605030a443f56fe5ffe490
  faq_generated_at: '2026-06-03T01:50:24Z'
  faq_source_hash: 3ec6ae40daff557dd05cd092ff7d6b5a63954a1618605030a443f56fe5ffe490
  summary: >-
    This Learning Path shows how to instrument C/C++ applications on Arm-based Linux systems for
    precise, code-level performance analysis using the PMUv3 plugin. You will prepare the plugin,
    enable user-space access to Arm PMUv3 performance counters, and instrument one or multiple
    code sections to collect fine-grained metrics. The path demonstrates running a single collection
    over any of 15 event groups (bundles) and using a Python tool to plot raw PMU event values
    alongside KPIs such as MPKI, stalls, and IPC for visualization. Prerequisites include an Arm-based
    computer running Linux and some familiarity with Linux application performance analysis; no
    additional prerequisites are explicitly listed.
  faqs:
  - question: How do I enable and verify userspace access to the PMU counters?
    answer: >-
      Run: sudo sysctl kernel/perf_user_access=1. Verify with: cat /proc/sys/kernel/perf_user_access
      and expect a value of 1. This setting enables access until the next reboot.
  - question: How should I organize my directories before instrumenting code?
    answer: >-
      Keep three parallel directories: the Linux kernel source tree, the PMUv3 plugin source code,
      and a test directory for integrating the plugin into an application. If you use a different
      layout, adjust build commands to locate headers and libraries accordingly.
  - question: Which events and metrics can I collect in a single run?
    answer: >-
      You can collect raw event values and performance metrics for any of the 15 event groups
      (bundles) in a single run. The results can later be plotted with KPIs such as MPKI, stalls,
      and IPC.
  - question: How do I instrument multiple sections of code in C?
    answer: >-
      Include the two required headers, initialize the plugin with pmuv3_bundle_init() using the
      desired bundle number, then use start and stop functions with markers to identify each profiled
      segment. Cleanup steps are the same as for the single-section scenario.
  - question: How do I set up the Python environment to plot and analyze results?
    answer: >-
      On Ubuntu, install python-is-python3, python3-pip, and python3-venv, create and activate
      a virtual environment, then pip install pandas, pyyaml, matplotlib, and PyPDF2. Download
      the provided Python application to generate plots of raw PMU events and KPIs from your collected
      data.
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

