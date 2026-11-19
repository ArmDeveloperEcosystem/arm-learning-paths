---
title: Tune Redis performance on Arm

minutes_to_complete: 30

who_is_this_for: This is an advanced topic for software developers who want to tune Redis on Arm-based servers and evaluate performance-sensitive configuration settings.

learning_objectives:
    - Identify kernel parameters that can impact Redis performance.
    - Identify compiler and libraries that can impact Redis performance.
    - Tune Redis server configuration for improved performance.

prerequisites:
    - Cloud or bare-metal installation of a Redis server on Arm
    - Completion of [Learn how to deploy Redis](/learning-paths/servers-and-cloud-computing/redis/) if you don't already have Redis set up

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-11-19T16:04:57Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: d5d0565161d6897a2b00af3ba2261a9b9755468797df67deacd3efe5c0395460
  summary_generated_at: '2026-11-19T16:04:57Z'
  summary_source_hash: d5d0565161d6897a2b00af3ba2261a9b9755468797df67deacd3efe5c0395460
  faq_generated_at: '2026-11-19T16:04:57Z'
  faq_source_hash: d5d0565161d6897a2b00af3ba2261a9b9755468797df67deacd3efe5c0395460
  summary: >-
    You'll tune Redis on Arm-based Linux by measuring the effect of each change. First, you'll
    examine kernel settings, compiler options, and OpenSSL choices. You'll then start from a
    minimal `redis.conf`, adjust one server setting at a time, and compare throughput,
    latency, memory, and CPU use. Finally, you'll evaluate client-side pipelining against your
    workload to see whether it improves performance.
  faqs:
  - question: How do I apply and persist kernel parameter changes?
    answer: >-
      Use `sysctl -w` to apply a setting immediately. Add it to a file under `/etc/sysctl.d/`
      if you want it to persist after a reboot.
  - question: How should I compare Redis configuration changes?
    answer: >-
      Start with the baseline `redis.conf`, change one setting, and measure throughput,
      latency, memory use, and CPU use before changing another.
  - question: Why isn't one configuration recommended for every workload?
    answer: >-
      Your request mix and deployment conditions affect the best settings. Measure each option
      with your workload before keeping a configuration.
  - question: Should I also test compiler and OpenSSL choices?
    answer: >-
      Yes. Evaluate the compiler and OpenSSL options described in the Learning Path
      and compare their measured effect.
  - question: How should I test client-side pipelining?
    answer: >-
      Start with pipeline depth `1`, then test `4`, `8`, `16`, and `32`. Compare throughput,
      tail latency, and client-side memory use before choosing a depth for your workload.
# END generated_summary_faq

author:
    - Elham Harirpoush
    - Kelsey Steele

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
subjects: Databases
platforms:
  - Arm AGI CPU
  - AWS Graviton
  - Microsoft Azure Cobalt
  - Google Axion
  - Oracle Cloud Infrastructure (OCI) Ampere Compute
armips:
    - Neoverse
tools_software_languages:
    - Redis
    - Runbook

operatingsystems:
    - Linux

further_reading:
    - resource:
        title: Redis Documentation
        link: https://redis.io/docs/
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

