---
title: Optimize the performance of Snort 3 using multithreading

minutes_to_complete: 45

who_is_this_for: This Learning Path is for software developers familiar with Snort who want to optimize performance by leveraging the benefits of multithreading.

learning_objectives: 
    - Install Snort and dependencies.
    - Configure Snort Lua files to enable multithreading.
    - Use multithreading to process capture files and measure performance.

prerequisites:
    - An Arm-based instance from a cloud provider, or an Arm server running Ubuntu 20.04 or 22.04.
    - A basic understanding of Snort's operation and configuration.
    

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T02:06:38Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 95da7df14cf36fe01e00868356cf117aa46007ac32e61b0df64d2eea28a5466e
  summary_generated_at: '2026-06-02T05:11:39Z'
  summary_source_hash: 95da7df14cf36fe01e00868356cf117aa46007ac32e61b0df64d2eea28a5466e
  faq_generated_at: '2026-06-03T02:06:38Z'
  faq_source_hash: 95da7df14cf36fe01e00868356cf117aa46007ac32e61b0df64d2eea28a5466e
  summary: >-
    Learn how to install Snort 3 on an Arm-based Linux server and configure it to use multithreading
    for processing capture files. You will adjust Snort’s Lua configuration to set the number
    of packet-processing threads, prepare the system by enabling Transparent HugePages and setting
    CPU isolation and affinity via GRUB, set up a rule set, and download PCAPs to test and measure
    performance. The path targets developers with a basic understanding of Snort and applies to
    Arm platforms, including Neoverse. It runs on Ubuntu 20.04 or 22.04 on an Arm server or an
    Arm-based cloud instance such as AWS EC2. Estimated time to complete is about 45 minutes.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need an Arm-based instance from a cloud provider, or an Arm server running Ubuntu 20.04
      or 22.04, and a basic understanding of Snort’s operation and configuration. No other explicit
      prerequisites are listed.
  - question: Which platforms and services can I use for the Arm instance?
    answer: >-
      You can use Arm-based instances from AWS, Microsoft Azure, Google Cloud, or Oracle. The
      tools list includes AWS EC2, but the procedure does not require a specific provider.
  - question: How do I enable multithreading in Snort 3?
    answer: >-
      Edit the Snort 3 Lua configuration to specify the number of threads that process network
      traffic. The steps show where to set the thread count for a single Snort instance.
  - question: How do I configure CPU affinity and memory settings before testing?
    answer: >-
      Append the provided kernel parameter line to /etc/default/grub to enable Transparent HugePages
      (THP) and set CPU isolation and affinity. The path includes an example for systems with
      CPUs 0–95, pinning CPUs 0–9 to Snort; adjust the CPU numbers for your hardware.
  - question: What should I expect when processing PCAP files with multithreading enabled?
    answer: >-
      Snort 3 will concurrently process packets from the capture files using multiple threads
      within one instance. You will measure performance as described in the steps, and alerts
      will be produced according to your configured rule set.
# END generated_summary_faq

author: Preema Merlin Dsouza

### Tags
skilllevels: Introductory
subjects: Libraries
cloud_service_providers:
  - AWS
  - Microsoft Azure
  - Google Cloud
  - Oracle
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

