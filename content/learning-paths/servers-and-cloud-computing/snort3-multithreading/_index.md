---
title: Optimize the performance of Snort 3 using multithreading

minutes_to_complete: 45

who_is_this_for: This Learning Path is for software developers familiar with Snort who want to optimize performance by leveraging the benefits of multithreading.

learning_objectives: 
    - Install Snort and dependencies.
    - Configure Snort Lua files to enable multithreading.
    - Use multithreading to process capture files and measure performance.

prerequisites:
    - An Arm-based instance from a cloud provider, or an Arm server running Ubuntu 20.04 or 22.04
    - A basic understanding of Snort operation and configuration

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-11-23T21:00:55Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 0cb9816250d474fd69a5e83d248a1226eb6688f0d5066ae583a093aaf58c7be3
  summary_generated_at: '2026-11-23T21:00:55Z'
  summary_source_hash: 0cb9816250d474fd69a5e83d248a1226eb6688f0d5066ae583a093aaf58c7be3
  faq_generated_at: '2026-11-23T21:00:55Z'
  faq_source_hash: 0cb9816250d474fd69a5e83d248a1226eb6688f0d5066ae583a093aaf58c7be3
  summary: You'll test Snort 3 multithreading on an Arm-based Linux server. First, you'll build Snort
    and prepare the host with CPU isolation, affinity, and Transparent HugePages settings. You'll
    configure rules and PCAP inputs, then map packet threads to CPU cores in the Lua configuration.
    Finally, you'll run Snort with multiple packet threads, inspect per-core activity with `mpstat`,
    and compare packets per second and runtime.
  faqs:
  - question: How do I choose a packet-thread count?
    answer: Match the packet-thread count to the cores reserved for Snort. Check the CPU isolation
      and affinity settings before running the PCAP test.
  - question: What should I check after editing /etc/default/grub?
    answer: Check that the Transparent HugePages and CPU isolation parameters contain your intended
      CPU ranges, then apply the configuration.
  - question: Where do I configure packet threads?
    answer: Set the thread-to-core mappings in `common.lua`, then use `--max-packet-threads 10`
      in the Snort command for ten packet threads.
  - question: How do I check the rule set before the PCAP test?
    answer: Check that `snort.lua` points to the intended rules directory. Ensure that the required
      rules are present before running Snort.
  - question: How do I assess the multithreaded run?
    answer: Run `mpstat -P 0-9 1` to inspect CPU activity across the example cores. Compare packets
      per second and runtime for the one-thread and ten-thread PCAP runs.
# END generated_summary_faq

author: Preema Merlin Dsouza

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Libraries
platforms:
  - AWS Graviton
  - Microsoft Azure Cobalt
  - Google Axion
  - Oracle Cloud Infrastructure (OCI) Ampere Compute
armips:
    - Neoverse
tools_software_languages:
    - AWS EC2
    - Snort3
    - Bash
    - GCC
operatingsystems:
    - Linux

further_reading:
    - resource:
        title: Snort3 Documentation
        link: https://docs.snort.org/start/
        type: documentation
    - resource:
        title: Performance Optimization for NGFW Whitepaper 
        link: https://files.techmahindra.com/static/img/pdf/next-generation-firewall.pdf
        type: blog

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

