---
title: Profiling for Neoverse with Streamline CLI Tools

minutes_to_complete: 15

who_is_this_for: This is an introductory guide for developers who want to measure and optimize the performance of applications running on Arm Neoverse™-based servers.

learning_objectives: 
    - Identify the Arm top-down profiling methodology.
    - Use Streamline CLI tools to capture and analyze performance data from an application.

prerequisites:
    - An Arm Neoverse-based (N1, N2 or V1) computer running Amazon Linux 2023 or later, Debian 10 or later, RHEL 8 or later, or Ubuntu 20.04 or later

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-11-19T15:57:10Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 2869c5b6c97f5a7b831917816ddfd0358987f040072a1ae5466ff1eb46ffec1c
  summary_generated_at: '2026-11-19T15:57:10Z'
  summary_source_hash: 2869c5b6c97f5a7b831917816ddfd0358987f040072a1ae5466ff1eb46ffec1c
  faq_generated_at: '2026-11-19T15:57:10Z'
  faq_source_hash: 2869c5b6c97f5a7b831917816ddfd0358987f040072a1ae5466ff1eb46ffec1c
  summary: >-
    You'll profile applications on Arm Neoverse Linux servers with Streamline CLI tools and
    top-down analysis. First, you'll check hardware profiling support with Arm Sysreport and
    learn how pipeline slots reveal performance bottlenecks. You'll then build with debug
    information, capture samples with `sl-record`, analyze them with `sl-analyze`, and format
    the report with `sl-format.py`. Finally, you'll use function metrics to prioritize
    optimization.
  faqs:
  - question: How do I check whether my system supports hardware-assisted profiling?
    answer: >-
      Run Arm Sysreport and review its performance counter and Statistical Profiling Extension
      (SPE) entries. You can see the available CPU counters and whether SPE is present.
  - question: How do I include function names in the report?
    answer: >-
      Build your application with debug information before recording. You can then map sampled
      instructions to functions in the analysis.
  - question: Which Streamline CLI tools do I run, and in what order?
    answer: >-
      Use `sl-record` to capture samples, `sl-analyze` to create function metrics, and
      `sl-format.py` to format the results.
  - question: Which metrics help me identify a bottleneck?
    answer: >-
      Review `Retiring%`, `FE bound%`, `Bad spec%`, and `BE bound%` in the functions report.
      You can use their relative values to decide which functions need closer inspection.
  - question: What can I try if a hot function has instruction cache misses?
    answer: >-
      Consider profile-guided optimization to reduce less important code and leave more
      instruction cache space for critical paths. Measure again to check the effect.
# END generated_summary_faq

author: Julie Gaskin

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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

