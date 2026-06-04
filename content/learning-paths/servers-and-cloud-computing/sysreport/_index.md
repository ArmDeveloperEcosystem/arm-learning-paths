---
title: Get ready for performance analysis with Sysreport

minutes_to_complete: 10

who_is_this_for: This is an introductory topic for software developers who want to use the system capability reporting tool, Sysreport, to understand and configure the performance features of their Arm Linux system.

learning_objectives: 
    - Run Sysreport to get a quick report of the system configuration
    - Discover which performance analysis features are available and enabled 
    - Make configuration changes to improve performance information collection

prerequisites:
    - An Arm-based system (bare metal server, cloud instance, developer board) running Linux 

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T02:09:35Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: d15c3083cb881838f6500eb56dfafb636d73bb282484a7f1b8f4a855dda37fb4
  summary_generated_at: '2026-06-02T05:16:32Z'
  summary_source_hash: d15c3083cb881838f6500eb56dfafb636d73bb282484a7f1b8f4a855dda37fb4
  faq_generated_at: '2026-06-03T02:09:35Z'
  faq_source_hash: d15c3083cb881838f6500eb56dfafb636d73bb282484a7f1b8f4a855dda37fb4
  summary: >-
    Use Sysreport to quickly assess the performance-related capabilities of an Arm Linux system
    and decide what to configure before profiling. This introductory path walks you through running
    the command-line tool on Arm Cortex-A and Neoverse-based platforms, including cloud instances
    (AWS, Microsoft Azure, Google Cloud, Oracle), bare metal servers, developer boards, and Raspberry
    Pi devices. You will verify access to the system shell, confirm Python (invoked as python3)
    and Git are available, run Sysreport, and analyze its on-screen summary of hardware and operating
    system configuration. By the end, you can identify which performance analysis features are
    present or enabled and determine any configuration changes needed to improve performance information
    collection. Estimated time to complete: about 10 minutes.
  faqs:
  - question: What do I need before running Sysreport on my Arm system?
    answer: >-
      You need an Arm-based system running Linux and the ability to log in via SSH or use a local
      console, with comfort on the Linux command line. The path asks you to confirm that Python
      and Git are installed.
  - question: Which Python command should I use for the steps?
    answer: >-
      The path assumes Python is invoked with the python3 command. If your environment uses a
      different command, adjust accordingly.
  - question: How do I confirm Python is installed?
    answer: >-
      Run python3 --version and look for a version string, for example “Python 3.9.5.” If no version
      is shown, Python may not be installed or python3 may not be the correct command on your
      system.
  - question: What result should I expect after running Sysreport?
    answer: >-
      Sysreport prints an on-screen summary of system configuration oriented toward performance
      analysis. It includes hardware and operating system details and indicates which performance
      features are available and enabled.
  - question: What should I check if a feature I expected is missing in the report?
    answer: >-
      Use the report to decide whether to switch to a different system or make configuration changes
      to reach the desired state for performance analysis. The path guides you to examine the
      output and consider changes where needed.
# END generated_summary_faq

author: James Whitaker

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
cloud_service_providers:
  - AWS
  - Microsoft Azure
  - Google Cloud
  - Oracle
armips:
    - Cortex-A 
    - Neoverse
tools_software_languages:
    - Python
    - Runbook

operatingsystems:
    - Linux


further_reading:
    - resource:
        title: Perf for Linux on Arm (LinuxPerf)
        link: /install-guides/perf/
        type: website
    - resource:
        title: APerf 
        link: /install-guides/aperf/
        type: website
    - resource:
        title: Arm Performance Studio
        link: /install-guides/ams/
        type: website


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

