---
title: Optimize network interrupt handling on Arm servers
description: Analyze and optimize interrupt request (IRQ) patterns on Arm Linux servers to improve network workload performance through IRQ distribution strategies.

   
minutes_to_complete: 20

who_is_this_for: This is an introductory topic for developers and performance engineers who are interested in understanding how network interrupt patterns can impact performance on cloud servers.

learning_objectives:
   - Analyze the current interrupt request (IRQ) layout on an Arm Linux system
   - Experiment with different interrupt options and patterns to improve performance
   - Configure optimal IRQ distribution strategies for your workload
   - Implement persistent IRQ management solutions

prerequisites:
    - An Arm computer running Linux
    - Some familiarity with the Linux command line

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T01:10:27Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 6fc608d45c4fdf85a77bddd4f8c26b05a7950d1086e578a8be0dd637feeb5d79
  summary_generated_at: '2026-06-02T04:07:50Z'
  summary_source_hash: 6fc608d45c4fdf85a77bddd4f8c26b05a7950d1086e578a8be0dd637feeb5d79
  faq_generated_at: '2026-06-03T01:10:27Z'
  faq_source_hash: 6fc608d45c4fdf85a77bddd4f8c26b05a7950d1086e578a8be0dd637feeb5d79
  summary: >-
    Learn how to analyze and adjust network interrupt (IRQ) distribution on Arm Linux servers
    to improve network workload performance. You will inspect the current IRQ layout, experiment
    with different IRQ management patterns using scripts provided in the Learning Path, and configure
    a distribution strategy appropriate for your workload, including making changes persistent.
    The guidance reflects observations across multiple cloud platforms and VM sizes, with specific
    notes for smaller systems (16 vCPUs or fewer). This introductory path is aimed at developers
    and performance engineers with an Arm computer running Linux and basic command-line familiarity.
    In about 20 minutes, you will be able to evaluate IRQ placement and apply a practical distribution
    approach for your system.
  faqs:
  - question: What do I need before running this Learning Path?
    answer: >-
      You need an Arm computer running Linux and some familiarity with the Linux command line.
      No additional prerequisites are explicitly listed.
  - question: How do I know how my NIC IRQs are currently distributed?
    answer: >-
      The steps show you how to understand and analyze the current IRQ configuration on your Arm
      Linux system. You will review how network interrupts are assigned across CPU cores before
      making changes.
  - question: Which IRQ distribution strategies can I try, and how are they applied?
    answer: >-
      The Learning Path presents multiple IRQ distribution strategies and provides scripts to
      implement them on your systems. You will experiment with assigning network IRQs to specific
      cores to improve cache locality and reduce contention, depending on your workload.
  - question: How should I choose a strategy for my system size or workload?
    answer: >-
      Effectiveness depends on system size and workload characteristics, and there is no single
      best approach. For systems with 16 vCPUs or less, recommendations include concentrating
      network IRQs on one or two CPU cores.
  - question: How do I make my IRQ configuration persistent and confirm it worked?
    answer: >-
      The Learning Path covers implementing persistent IRQ management solutions so your configuration
      survives reboots. You can validate changes by repeating the analysis steps and observing
      IRQ distribution under your workload.
# END generated_summary_faq

author: Kiel Friedt

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
armips:
    - Neoverse
    - Cortex-A
tools_software_languages:

operatingsystems:
    - Linux


further_reading:
    - resource:
        title: Perf for Linux on Arm (LinuxPerf)
        link: /install-guides/perf/
        type: website
    - resource:
        title: Tune network workloads on Arm-based bare-metal instances
        link: /learning-paths/servers-and-cloud-computing/tune-network-workloads-on-bare-metal/
        type: learning-path
    - resource:
        title: Get started with Arm-based cloud instances
        link: /learning-paths/servers-and-cloud-computing/csp/
        type: learning-path
    - resource:
        title: Linux kernel IRQ subsystem documentation
        link: https://www.kernel.org/doc/html/latest/core-api/irq/index.html
        type: website
    - resource:
        title: Microbenchmark and tune network performance with iPerf3
        link: /learning-paths/servers-and-cloud-computing/microbenchmark-network-iperf3/
        type: learning-path

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

