---
title: Tune network workloads on Arm-based bare-metal instances

minutes_to_complete: 60

who_is_this_for: This is an advanced topic for engineers who want to tune the performance of network workloads on Arm Neoverse-based bare-metal instances.

learning_objectives: 
    - Set up Apache Tomcat and wrk2 to benchmark HTTP on an Arm Neoverse bare‑metal host
    - Establish a reproducible baseline baseline (file‑descriptor limits, logging, thread counts, fixed core set)
    - Tune NIC queue count to match available cores and measure impact
    - Improve NUMA locality by placing Tomcat on the NIC's NUMA node and aligning worker threads with cores
    - Compare IOMMU strict mode and IOMMU passthrough mode, and select the configuration that delivers the best performance for your workload

prerequisites:
    - An Arm Neoverse-based bare-metal server running Ubuntu 24.04 to run Apache Tomcat
    - Access to an x86_64 bare-metal server running Ubuntu 24.04 to run `wrk2`
    - Basic familiarity with Java applications

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T02:13:37Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 9f2b3f6c5e76ecb754de5c0fd84278ff71f71c5c7906acdc06911f2feff1f5fd
  summary_generated_at: '2026-06-02T05:23:06Z'
  summary_source_hash: 9f2b3f6c5e76ecb754de5c0fd84278ff71f71c5c7906acdc06911f2feff1f5fd
  faq_generated_at: '2026-06-03T02:13:37Z'
  faq_source_hash: 9f2b3f6c5e76ecb754de5c0fd84278ff71f71c5c7906acdc06911f2feff1f5fd
  summary: >-
    This advanced Learning Path shows how to benchmark and tune an HTTP network workload on Arm
    Neoverse-based bare‑metal servers using Apache Tomcat, wrk2, and OpenJDK 21 on Ubuntu 24.04.
    You will set up Tomcat on an Arm Neoverse host and wrk2 on an x86_64 host, establish a reproducible
    baseline (file‑descriptor limits, logging, thread counts, and a fixed core set), then apply
    targeted tuning: adjust NIC queue counts to match available CPUs, improve NUMA locality by
    running Tomcat on the NIC’s NUMA node, and compare IOMMU strict versus passthrough modes.
    Validated on an AWS c8g.metal‑48xl instance, the expected outcome is a clear, repeatable process
    to measure and refine throughput and latency for your workload.
  faqs:
  - question: What do I need before running the benchmark?
    answer: >-
      You need an Arm Neoverse-based bare-metal server with Ubuntu 24.04 to run Apache Tomcat,
      and an x86_64 bare-metal server with Ubuntu 24.04 to run wrk2. Basic familiarity with Java
      applications is assumed. Tomcat runs on OpenJDK 21.
  - question: Do I need to raise file descriptor limits on both the client and server?
    answer: >-
      Yes. Increase the file-descriptor limit on both the Tomcat server and the wrk2 client to
      avoid running out under load (for example, set it to 65535).
  - question: How should I choose the NIC queue count during tuning?
    answer: >-
      Match the number of NIC transmit/receive queues to the number of CPUs you keep online. Reducing
      queues when using a small CPU set helps distribute interrupts more evenly and can stabilize
      throughput and latency on Arm Neoverse systems.
  - question: How do I decide where to place Tomcat for NUMA locality?
    answer: >-
      Use numactl -H to inspect NUMA topology and relative latencies; cross‑NUMA latency is higher
      than intra‑NUMA. Place Tomcat on the NIC’s NUMA node and align worker threads with the cores
      on that node.
  - question: How do I compare IOMMU strict mode with passthrough?
    answer: >-
      Update the kernel command line via GRUB to set iommu.strict=0 and iommu.passthrough=1, then
      reboot and benchmark again. Compare results with strict mode enabled and select the configuration
      that performs best for your workload.
# END generated_summary_faq

author: Ying Yu, Ker Liu, Rui Chang

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
armips:
    - Neoverse
tools_software_languages:
    - Apache Tomcat
    - wrk2
    - OpenJDK 21
operatingsystems:
    - Linux

further_reading:
  - resource:
      title: OpenJDK Wiki 
      link: https://wiki.openjdk.org/
      type: documentation

  - resource:
      title: Apache Tomcat documentation
      link: https://tomcat.apache.org/tomcat-11.0-doc/index.html
      type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

