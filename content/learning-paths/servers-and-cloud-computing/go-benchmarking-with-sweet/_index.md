---
title: Benchmark Go performance with Sweet and Benchstat
description: Learn how to provision Arm64 and x86_64 VM instances on Google Cloud, then install and use Sweet and Benchstat to measure and compare Go application performance.

minutes_to_complete: 60

who_is_this_for: This introductory topic is for developers who want to measure and compare the performance of Go applications on Arm-based servers.

learning_objectives:
    - Provision Arm64 and x86_64 virtual machine (VM) instances on Google Cloud.
    - Install Go, Sweet, and Benchstat on each VM instance.
    - Run benchmarks and use Benchstat to compare Go application performance across architectures.

prerequisites:
    - A [Google Cloud account](https://console.cloud.google.com/)
    - A local machine with [Google Cloud CLI](/install-guides/gcloud/) installed

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-09-10T22:09:01Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: b7a41161facac3d4497bdf431195907e06d2c350d1c235dd5d370fe7aa3666e9
  summary_generated_at: '2026-09-10T22:09:01Z'
  summary_source_hash: b7a41161facac3d4497bdf431195907e06d2c350d1c235dd5d370fe7aa3666e9
  faq_generated_at: '2026-09-10T22:09:01Z'
  faq_source_hash: b7a41161facac3d4497bdf431195907e06d2c350d1c235dd5d370fe7aa3666e9
  summary: >-
    You'll compare Go application performance on Arm-based and Intel Google Cloud VMs. First,you'll install Go, Sweet, and Benchstat on both systems, run the same benchmarks, and collect comparable results. Then, you'll use Benchstat to analyze statistical differences and review the output as text or CSV. This gives you a reproducible basis for comparing application performance across architectures.
  faqs:
  - question: How do I know that the VM is configured correctly before continuing?
    answer: >-
      On the VM instances page, confirm that the series and machine type is `c4a-standard-4` for the Arm-based VM
      and `c4-standard-8` for the Intel-based VM. 
  - question: Do I need to install Go, Sweet, and Benchstat on both VMs?
    answer: >-
      Yes. The comparison relies on running the same Go Benchmarks natively on each architecture
      and then using Benchstat to analyze the two result sets.
  - question: Where does the Sweet installation go, and what should I check?
    answer: >-
      Run the installer from your home directory, which creates a `$HOME/benchmarks/sweet`
      path. Verify that the directory exists before you proceed to run benchmarks.
  - question: When should I run Sweet versus Benchstat?
    answer: >-
      Run Sweet on each VM to execute the benchmarks and generate raw performance data. After
      both runs complete, use Benchstat to compare the results across the two systems.
  - question: Which metrics should I inspect in the Benchstat output?
    answer: >-
      Inspect `sec/op` for execution time, `average-RSS-bytes` for average resident memory,
      `peak-RSS-bytes` for maximum resident memory, and `peak-VM-bytes` for maximum virtual memory.
      Lower values indicate less time or memory for these metrics.
# END generated_summary_faq

author: Geremy Cohen

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
platforms:
  - Google Axion
armips:
    - Neoverse
tools_software_languages:
    - Go
operatingsystems:
    - Linux

further_reading:
    - resource:
        title: Effective Go
        link: https://go.dev/doc/effective_go#performance
        type: blog
    - resource:
        title: Benchmark testing in Go
        link: https://dev.to/stefanalfbo/benchmark-testing-in-go-17dc
        type: blog

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
