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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-26T17:33:13Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 70ed68f472841d24321968188948c5c661a48445c0b07e54535d538233e048e3
  summary_generated_at: '2026-06-26T17:33:13Z'
  summary_source_hash: 70ed68f472841d24321968188948c5c661a48445c0b07e54535d538233e048e3
  faq_generated_at: '2026-06-26T17:33:13Z'
  faq_source_hash: 70ed68f472841d24321968188948c5c661a48445c0b07e54535d538233e048e3
  summary: >-
    In this Learning Path, you access Arm hardware event counters and the system counter from
    user space on Linux using the PMU. You start by distinguishing software and hardware events,
    then use a minimal assembly approach with `MRS` and `MSR` to read the system counter and measure
    time around a function. You then instrument event counters with PAPI, including environment
    configuration and user-space counter access. You finish with two C examples that use
    `perf_event_open` to read either a single counter or a group of counters without multiplexing.
    By the end, you build and run working code that returns measurable counter values suitable
    for basic performance instrumentation on Arm systems.
  faqs:
  - question: How do I know the system counter example produced a valid measurement?
    answer: >-
      The program should report a positive difference in system counter ticks between the two
      reads that bracket the target function. A zero or negative value usually means the reads
      are not placed correctly around the region being measured.
  - question: Which Arm instructions are used to access system registers for counting?
    answer: >-
      Use `MRS` to read a system register and `MSR` to write a system register. These two instructions
      are sufficient for the system counter example.
  - question: PAPI cannot find its headers or libraries at build or runtime. What should I check?
    answer: >-
      Set `PAPI_DIR` to the location where PAPI is installed. Depending on your system, you might
      also need `LD_LIBRARY_PATH` to include `$PAPI_DIR/lib`.
  - question: What should I do before using PAPI or `perf_event_open` to access counters from user
      space?
    answer: >-
      Run the `sudo` command in the steps that writes the recommended value to the file under `/proc/sys/kernel`.
      This enables user-space access to the counters for the examples.
  - question: When using `perf_event_open`, which example should I use to read multiple counters
      at once?
    answer: >-
      Use the group example to read several counters together without multiplexing. The single-counter
      example configures just one event, and `perf_event_open` in this Learning Path does not support multiplexing.
# END generated_summary_faq

author: Julio Suarez

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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
