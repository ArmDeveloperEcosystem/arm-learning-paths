---
title: Profiling for Neoverse with Streamline CLI Tools

minutes_to_complete: 15

who_is_this_for: This is an introductory guide for developers who want to measure and optimize the performance of applications running on Arm Neoverse™-based servers.

learning_objectives: 
    - Describe Arm's top-down profiling methodology.
    - Use Streamline CLI tools to capture and analyze performance data from an application.

prerequisites:
    - An Arm Neoverse-based (N1, N2 or V1) computer running Linux. For your host OS, you can use Amazon Linux 2023 or newer, Debian 10 or newer, RHEL 8 or newer, or Ubuntu 20.04 or newer.

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T01:54:25Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: ef12378069d6f3538d8daefb5da7fc8e8ce4196277928d372745d12fde6e46a1
  summary_generated_at: '2026-06-02T04:50:40Z'
  summary_source_hash: ef12378069d6f3538d8daefb5da7fc8e8ce4196277928d372745d12fde6e46a1
  faq_generated_at: '2026-06-03T01:54:25Z'
  faq_source_hash: ef12378069d6f3538d8daefb5da7fc8e8ce4196277928d372745d12fde6e46a1
  summary: >-
    This introductory Learning Path shows how to profile applications on Arm Neoverse-based Linux
    servers using Streamline CLI tools and Arm’s top-down performance methodology. You begin by
    checking hardware-assisted profiling support with Arm Sysreport, examining perf counters and
    SPE availability (best results are on systems with at least 6 CPU counters). You then capture
    raw samples with sl-record, preprocess with sl-analyze, and format function-attributed metrics
    with sl-format.py. The path explains Frontend, Backend, and Retire concepts, demonstrates
    interpreting Retiring%, FE bound%, Bad spec%, and BE bound% in a sample report, and provides
    a short optimization checklist. Prerequisite: an Arm Neoverse (N1, N2, or V1) Linux system;
    supported host OS options include Amazon Linux 2023+, Debian 10+, RHEL 8+, or Ubuntu 20.04+.
  faqs:
  - question: What do I need before running the profiling steps?
    answer: >-
      You need an Arm Neoverse-based (N1, N2, or V1) computer running Linux. Supported host OS
      options include Amazon Linux 2023 or newer, Debian 10 or newer, RHEL 8 or newer, or Ubuntu
      20.04 or newer.
  - question: How do I know if my system supports hardware-assisted profiling?
    answer: >-
      Run the Arm Sysreport utility as described in the referenced guide. In the report, perf
      counters shows how many CPU counters are available and perf sampling indicates if SPE is
      available; systems with at least 6 available CPU counters provide better profiles.
  - question: Do I need to rebuild my application before profiling?
    answer: >-
      Yes. Build your application with debug information so the profiler can map instructions
      to source code and attribute metrics to functions.
  - question: Which Streamline CLI tools should I run and in what order?
    answer: >-
      Use sl-record to capture raw sampled data, sl-analyze to generate function-attributed counters
      and metrics, and sl-format.py to produce a human-readable report. Follow this sequence for
      each profiling run.
  - question: What result should I expect, and how do I interpret low Retiring%?
    answer: >-
      After sl-format.py, expect a functions report with top-down metrics: Retiring%, FE bound%,
      Bad spec%, and BE bound%. A low Retiring% indicates inefficient use of processing resources;
      if a function is frontend bound with high instruction cache miss rate, the checklist suggests
      applying profile-guided optimization to reduce less important code.
# END generated_summary_faq

author: Julie Gaskin

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
armips:
    - Neoverse
tools_software_languages:
    - Streamline CLI
    - Runbook

operatingsystems:
    - Linux


further_reading:
    - resource:
        title: Streamline CLI Tools User Guide 
        link: https://developer.arm.com/documentation/109847/latest/
        type: documentation
    - resource:
        title: Introducing Arm Streamline CLI tools 
        link: https://developer.arm.com/community/arm-community-blogs/b/servers-and-cloud-computing-blog
        type: blog
    - resource:
        title: About Streamline CLI Tools
        link: https://www.arm.com/products/development-tools/performance/streamline-cli
        type: website



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

