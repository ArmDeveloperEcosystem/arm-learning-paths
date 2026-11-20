---
title: Run Process watch on your Arm machine

minutes_to_complete: 20

who_is_this_for: This is an introductory topic for software developers who want to build and run the Process Watch tool on an Arm-based machine.
learning_objectives: 
    - Build and run the Process Watch tool on your Arm machine.
    - Describe how Process Watch works.
    - Check in real-time whether any workloads are using specific Arm instructions or features.

prerequisites:
    - An Arm-based system (bare metal server, cloud instance, or developer board) running Linux with kernel version 5.8.0 or later.
    - Root access, or the ability to run the sudo command.

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-11-18T20:26:43Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 3774f8cd7c5738f948d43bbb27b92b8d4d88d83a31f4eb5b44c9a5d31adeec8e
  summary_generated_at: '2026-11-18T20:26:43Z'
  summary_source_hash: 3774f8cd7c5738f948d43bbb27b92b8d4d88d83a31f4eb5b44c9a5d31adeec8e
  faq_generated_at: '2026-11-18T20:26:43Z'
  faq_source_hash: 3774f8cd7c5738f948d43bbb27b92b8d4d88d83a31f4eb5b44c9a5d31adeec8e
  summary: >-
    You'll build Process Watch on Arm-based Linux and use it to inspect instruction activity.
    First, you'll install dependencies, clone the source with submodules, and configure access for
    running the tool. Then, you'll learn how its sampled instruction counters appear by process.
    Finally, you'll compile and run a small C workload and check its Process Watch output for the
    expected instruction groups.
  faqs:
  - question: Do I need to clone submodules when getting the source?
    answer: >-
      Yes. Use `git clone --recursive` to ensure that all submodules are fetched with the Process
      Watch repository.
  - question: Should I run Process Watch as root, or can I enable it for a non-root user?
    answer: >-
      Run Process Watch as root for the documented setup. For non-root use, set capabilities
      with `sudo setcap CAP_PERFMON,CAP_BPF=+ep ./processwatch` and adjust
      `kernel.perf_event_paranoid` and `kernel.unprivileged_bpf_disabled`.
  - question: How do I see the available command-line options?
    answer: >-
      Run `sudo ./processwatch -h` to display the supported arguments and usage information.
  - question: What should I look for in the output to confirm specific Arm instructions are used?
    answer: >-
      Check the columns for `FPArmv8`, `NEON`, `SVE`, and `SVE2`. Look for non-zero counts for the `PID`
      and `NAME` of your workload, along with `%TOTAL` and `TOTAL` values that reflect sampled
      instructions.
  - question: How do I verify that Process Watch is observing my test workload?
    answer: >-
      Compile `workload.c`, run the resulting executable in the background, and note its PID.
      Start Process Watch with `-p` set to that PID. Check the workload row for changing totals
      and instruction counts.
# END generated_summary_faq

author: Graham Woodward

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
armips:
    - Cortex-A
    - Neoverse
tools_software_languages:
    - bpftool
    - libbpf
    - Capstone
    - C
    - CPP
    - Runbook

operatingsystems:
    - Linux

further_reading:
    - resource:
        title: Perf for Linux on Arm (LinuxPerf)
        link: /install-guides/perf/
        type: website
    - resource:
        title: Capstone 
        link: https://github.com/capstone-engine/capstone
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

