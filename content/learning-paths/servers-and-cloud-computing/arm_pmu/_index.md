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

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T00:20:03Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 70ed68f472841d24321968188948c5c661a48445c0b07e54535d538233e048e3
  summary_generated_at: '2026-06-02T03:07:54Z'
  summary_source_hash: 70ed68f472841d24321968188948c5c661a48445c0b07e54535d538233e048e3
  faq_generated_at: '2026-06-03T00:20:03Z'
  faq_source_hash: 70ed68f472841d24321968188948c5c661a48445c0b07e54535d538233e048e3
  summary: >-
    Learn how to access Arm hardware performance counters (PMU) and the system counter from user
    space on Linux. You will measure time using the system counter with small assembly snippets
    (MRS/MSR), instrument event counters with PAPI, and use the Linux perf_event_open system call
    to read both single counters and groups (without multiplexing). The path covers installing
    PAPI, setting environment variables (PAPI_DIR and, if needed, LD_LIBRARY_PATH), enabling user-space
    access to counters, and building example programs with GCC. Target environment is an Arm computer
    running Linux; bare-metal or cloud metal instances expose more counters, and the steps were
    tested on the a1.metal instance type. You will finish with working code that reads hardware
    and system counter values.
  faqs:
  - question: What do I need before running the examples?
    answer: >-
      You need an Arm computer running Linux. A bare metal or cloud metal instance is recommended
      because it exposes more counters, while a VM may provide fewer counters. The instructions
      were tested on an a1.metal instance.
  - question: How do I decide between using the system counter, PAPI, or perf_event_open?
    answer: >-
      Use the system counter via MRS/MSR if you only need to measure time or cycles from user
      space. Use PAPI to instrument event counters in application code, or use the perf_event_open
      system call to read hardware event counters directly.
  - question: Which environment variables and permissions are required for the PAPI steps?
    answer: >-
      Set PAPI_DIR to the PAPI installation path, and you might need to add $PAPI_DIR/lib to LD_LIBRARY_PATH.
      The steps also include enabling user space access to counters using a sudo command to change
      a kernel setting.
  - question: What does the perf_event_open section demonstrate, and does it support multiplexing?
    answer: >-
      It provides two examples: reading a single hardware counter and reading a group of counters
      without multiplexing. perf_event_open does not support multiplexing.
  - question: What should I check if I cannot access certain hardware counters?
    answer: >-
      Confirm that user space access to counters has been enabled as shown in the steps. Also
      note that VMs may expose fewer counters; using a bare metal or cloud metal instance typically
      provides more.
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

