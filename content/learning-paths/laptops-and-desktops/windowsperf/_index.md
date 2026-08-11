---
title: Get started with WindowsPerf

description: Learn how to install WindowsPerf on Windows on Arm machines and generate sample performance reports for CPU profiling.

minutes_to_complete: 20

who_is_this_for: This is an introductory topic for software developers working on laptops and desktops and new to the Arm architecture.

learning_objectives:
    - Install WindowsPerf on Windows on Arm machine
    - Generate a sample report

prerequisites:
    - Windows on Arm desktop or development machine

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-11T16:27:03Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: b03c7d15729468a2c3a4e5fa7f6c6cec49c940e9f02c5f4330a832524ef7db8b
  summary_generated_at: '2026-08-11T16:27:03Z'
  summary_source_hash: b03c7d15729468a2c3a4e5fa7f6c6cec49c940e9f02c5f4330a832524ef7db8b
  faq_generated_at: '2026-08-11T16:27:03Z'
  faq_source_hash: b03c7d15729468a2c3a4e5fa7f6c6cec49c940e9f02c5f4330a832524ef7db8b
  summary: >-
    You'll install WindowsPerf on Windows on Arm and use the `wperf` command-line interface to generate
    a performance report. You'll use two profiling models: counting with `wperf stat` to capture
    aggregate occurrences
    of Arm PMU events, and sampling with `wperf sample` or `wperf record` to attribute event frequencies
    to functions, basic blocks, or instructions. You'll select events (for example,
    `inst_spec`, `vfp_spec`, `ase_spec`, and `ld_spec`), pinning to a core and running for a defined
    interval. Then, you'll interpret counters and sampling output so you can recognize a successful run.
  faqs:
  - question: Which command should I run first to verify that WindowsPerf is working?
    answer: >-
      Start with a short counting run using `wperf stat` on a few events for a brief timeout. For
      example, use `inst_spec`, `vfp_spec`, `ase_spec`, and `ld_spec` to confirm you see nonzero aggregate
      counts without errors.
  - question: When should I use `wperf stat` versus `wperf sample` or `wperf record`?
    answer: >-
      Use `wperf stat` to obtain aggregate counts of PMU events over a measurement window. Use
      `wperf sample` or `wperf record` to collect samples that show where events occur at the function,
      basic block, or instruction level.
  - question: How do I choose the CPU core and duration for a measurement?
    answer: >-
      Select the core with the `-c` option (for example, `-c 0`) and control the run length with `--timeout`.
      Pick values that cover the code you want to observe during the measurement window.
  - question: What result should I expect from a sampling run?
    answer: >-
      Sampling output attributes PMU event occurrences to program locations at the function, basic
      block, or instruction levels. If you see only totals, verify that you used a sampling
      command rather than `wperf stat`.
  - question: Which events or metrics can I try from the cheat sheet examples?
    answer: >-
      The examples use `inst_spec`, `vfp_spec`, `ase_spec`, and `ld_spec`, and include the `imix` metric,
      which groups related events. You can also add an additional event such as `l1i_c`.
# END generated_summary_faq

author: Ronan Synnott

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

further_reading:
    - resource:
        title: Announcing WindowsPerf Open-source performance analysis tool for Windows on Arm
        link: https://developer.arm.com/community/arm-community-blogs/b/servers-and-cloud-computing-blog/posts/announcing-windowsperf
        type: blog
    - resource:
        title: WindowsPerf release 2.4.0 introduces the first stable version of sampling model support
        link: https://www.linaro.org/blog/windowsperf-release-2-4-0-introduces-the-first-stable-version-of-sampling-model-support/
        type: blog
    - resource:
        title: WindowsPerf Release 2.5.1
        link: https://www.linaro.org/blog/windowsperf-release-2-5-1/
        type: blog
    - resource:
        title: WindowsPerf Release 3.0.0
        link: https://www.linaro.org/blog/windowsperf-release-3-0-0/
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
        title: WindowsPerf releases
        link: https://gitlab.com/Linaro/WindowsPerf/windowsperf/-/releases
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
