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

generate_summary_faq: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-04-30T18:58:19Z'
  generator: template
  source_hash: ed85d6171f3c05bfdf1b396065fb0c73ce88724ff63fd1c3c8a93d4c27dd59f8
  summary: >-
    Run Process watch on your Arm machine walks you through an end-to-end Arm software workflow.
    It is designed for software developers who want to build and run the Process Watch tool on
    an Arm-based machine. By the end, you will be able to build and run the Process Watch tool
    on your Arm machine, describe how Process Watch works, and check in real-time whether any
    workloads are using specific Arm instructions or features. It focuses on tools and technologies
    such as bpftool, libbpf, Capstone, C, and CPP, Linux environments, and Arm platforms including
    Cortex-A and Neoverse. The main steps cover Install dependencies, Run Process Watch, Learn
    how Process Watch works, and Using Process Watch.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will build and run the Process Watch tool on your Arm machine, describe how Process
      Watch works, and check in real-time whether any workloads are using specific Arm instructions
      or features.
  - question: Who is this Learning Path for?
    answer: >-
      This is an introductory topic for software developers who want to build and run the Process
      Watch tool on an Arm-based machine.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: An Arm-based system (bare metal server,
      cloud instance, or developer board) running Linux with kernel version 5.8.0 or later.; Root
      access, or the ability to run the sudo command.
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including bpftool, libbpf, Capstone, C, and CPP, Linux environments,
      and Arm platforms such as Cortex-A and Neoverse.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Install dependencies, Run Process Watch, Learn how
      Process Watch works, and Using Process Watch.
# END generated_summary_faq

author: Graham Woodward

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

