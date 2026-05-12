---
title: How to use the Arm Performance Monitoring Unit and System Counter
description: Learn how to access and use Arm hardware performance counters and the system counter from user space using PAPI, perf_event_open, and assembly code for performance instrumentation.

minutes_to_complete: 90

who_is_this_for: This is an advanced topic for software developers who want to instrument hardware event counters or the system counter in software applications.

learning_objectives:
    - Understand different options for accessing counters from user space
    - Use the system counter to measure time in code
    - Use PAPI to instrument event counters in code
    - Use the Linux perf_event_open system call to instrument event counters in code
prerequisites:
    - An Arm computer running Linux. A bare metal or cloud metal instance is best because they expose more counters. You can use a virtual machine (VM), but fewer counters may be available. These instructions have been tested on the `a1.metal` instance type.

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v2
  generated_at: '2026-05-08T18:10:01Z'
  generator: template
  source_hash: 70ed68f472841d24321968188948c5c661a48445c0b07e54535d538233e048e3
  summary_generated_at: '2026-05-08T18:10:01Z'
  summary_source_hash: 70ed68f472841d24321968188948c5c661a48445c0b07e54535d538233e048e3
  faq_generated_at: '2026-05-08T18:10:01Z'
  faq_source_hash: 70ed68f472841d24321968188948c5c661a48445c0b07e54535d538233e048e3
  summary: >-
    Learn how to access and use Arm hardware performance counters and the system counter from
    user space using PAPI, perf_event_open, and assembly code for performance instrumentation.
    It is designed for software developers who want to instrument hardware event counters or the
    system counter in software applications. By the end, you will be able to understand different
    options for accessing counters from user space, use the system counter to measure time in
    code, and use PAPI to instrument event counters in code. It focuses on tools and technologies
    such as PAPI, perf, Assembly, GCC, and Runbook, Linux environments, and Arm platforms including
    Neoverse. The main steps cover Counter access options, Use a system counter, Use PAPI for
    counting, and Use perf_event_open for counting.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will understand different options for accessing counters from user space, use the system
      counter to measure time in code, and use PAPI to instrument event counters in code. Learn
      how to access and use Arm hardware performance counters and the system counter from user
      space using PAPI, perf_event_open, and assembly code for performance instrumentation.
  - question: Who is this Learning Path for?
    answer: >-
      This is an advanced topic for software developers who want to instrument hardware event
      counters or the system counter in software applications.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: An Arm computer running Linux. A bare
      metal or cloud metal instance is best because they expose more counters. You can use a virtual
      machine (VM), but fewer counters may be available. These instructions have been tested on
      the `a1.metal` instance type.
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including PAPI, perf, Assembly, GCC, and Runbook, Linux environments,
      and Arm platforms such as Neoverse.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Counter access options, Use a system counter, Use
      PAPI for counting, and Use perf_event_open for counting.
# END generated_summary_faq

author: Julio Suarez

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
armips:
    - Neoverse
tools_software_languages:
    - PAPI
    - perf
    - Assembly
    - GCC
    - Runbook

operatingsystems:
    - Linux

further_reading:
    - resource:
        title: Linux perf_events documentation
        link: https://www.man7.org/linux/man-pages/man2/perf_event_open.2.html
        type: documentation
    - resource:
        title: PAPI documentation
        link: https://github.com/icl-utk-edu/papi/wiki
        type: documentation
    - resource:
        title: Perf
        link: https://en.wikipedia.org/wiki/Perf_%28Linux%29
        type: documentation


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

