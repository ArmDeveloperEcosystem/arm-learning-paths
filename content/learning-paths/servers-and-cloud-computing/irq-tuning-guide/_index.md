---
title: Optimize network interrupt handling on Arm servers
description: Analyze and optimize interrupt request (IRQ) patterns on Arm Linux servers to improve network workload performance through IRQ distribution strategies.

minutes_to_complete: 20

who_is_this_for: This is an introductory topic for developers and performance engineers who are interested in understanding how network interrupt patterns can impact performance on cloud servers.

learning_objectives:
   - Analyze the current interrupt request (IRQ) layout on an Arm Linux system.
   - Experiment with different interrupt options and patterns to improve performance.
   - Configure optimal IRQ distribution strategies for your workload.
   - Implement persistent IRQ management solutions.

prerequisites:
    - An Arm computer running Linux
    - Some familiarity with the Linux command line

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-09-15T21:16:42Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 1b984aa3a8728506e72fa6241dd6ba8c874159d19379f7c9b610fb16d02c2afb
  summary_generated_at: '2026-09-15T21:16:42Z'
  summary_source_hash: 1b984aa3a8728506e72fa6241dd6ba8c874159d19379f7c9b610fb16d02c2afb
  faq_generated_at: '2026-09-15T21:16:42Z'
  faq_source_hash: 1b984aa3a8728506e72fa6241dd6ba8c874159d19379f7c9b610fb16d02c2afb
  summary: >-
    You'll analyze and tune network IRQ handling on Arm Linux servers. First, you'll review the current
    IRQ layout, compare placements that pin network interrupts to CPU cores, and test cache locality and contention. Then, you'll apply `smp_affinity` range
    assignments, choose strategies for different system sizes, and make the selected
    settings persistent for repeatable workload testing.
  faqs:
  - question: What should I do if an IRQ change reduces performance?
    answer: >-
      Restore the default IRQ handling by running `sudo systemctl unmask irqbalance` and
      `sudo systemctl enable --now irqbalance`. If `irqbalance` isn't installed on a Debian-based
      system, install it with `sudo apt install irqbalance`.
  - question: Which IRQ distribution pattern should I start with on a small server with 16 vCPUs or fewer?
    answer: >-
      Start by concentrating network IRQs on one or two CPU cores instead of spreading them across
      all cores. Use the `smp_affinity` range assignment recommended in the path to bind the interrupts.
  - question: What result should I expect after applying a new IRQ pattern?
    answer: >-
      You should see NIC interrupts bound to the cores that you selected, and a consistent distribution
      under network load. Compare the new layout to your baseline to confirm that the change took effect.
  - question: How do I make my IRQ configuration persist across reboots?
    answer: >-
      IRQ changes reset at reboot. Add your affinity settings to `/etc/rc.local` or create a
      systemd service file so that the assignments are reapplied when the system starts.
  - question: What should I try if network behavior doesn't improve with my first pattern?
    answer: >-
      Switch to an alternative distribution strategy and retest, because effectiveness depends
      on workload and system size. No single approach is optimal everywhere, so iterate and validate
      under representative load.
# END generated_summary_faq

author: Kiel Friedt

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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
