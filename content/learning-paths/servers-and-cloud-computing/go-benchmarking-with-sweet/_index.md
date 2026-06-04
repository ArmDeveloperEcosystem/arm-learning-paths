---
title: Benchmark Go performance with Sweet and Benchstat
description: Learn how to provision Arm64 and x86_64 VM instances on Google Cloud, then install and use Sweet and Benchstat to measure and compare Go application performance.

minutes_to_complete: 60

who_is_this_for: This introductory topic is for developers who want to measure and compare the performance of Go applications on Arm-based servers.

learning_objectives:
    - Provision Arm64 and x86_64 VM instances on Google Cloud 
    - Install Go, Sweet, and Benchstat on each VM instance
    - Run benchmarks and use Benchstat to compare Go application performance across architectures

prerequisites:
    - A [Google Cloud account](https://console.cloud.google.com/). This Learning Path can be run on any cloud provider or on-premises, but it focuses on Google Cloud’s Axion Arm64-based instances.
    - A local machine with [Google Cloud CLI](/install-guides/gcloud/) installed

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T01:07:15Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: aa78434138f08b424352302e92a1cd40d8297459bc65202715dcb41c40de6057
  summary_generated_at: '2026-06-02T04:05:11Z'
  summary_source_hash: aa78434138f08b424352302e92a1cd40d8297459bc65202715dcb41c40de6057
  faq_generated_at: '2026-06-03T01:07:15Z'
  faq_source_hash: aa78434138f08b424352302e92a1cd40d8297459bc65202715dcb41c40de6057
  summary: >-
    Provision Arm64 and x86_64 Linux VM instances on Google Cloud and use Go benchmarking tools
    to compare performance across architectures. You will create an Arm-based c4a-standard-4 and
    an Intel Emerald Rapids c4-standard-8 instance, install Go, Sweet, and Benchstat on both,
    then run Go Benchmarks with Sweet and analyze results with Benchstat (text or CSV). Prerequisites
    are a Google Cloud account and the Google Cloud CLI on your local machine. The path focuses
    on Google Cloud’s Axion Arm64-based instances but can also be run on other clouds or on-premises.
    Estimated time to complete is about 60 minutes.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need a Google Cloud account and the Google Cloud CLI installed on your local machine.
      No other explicit prerequisites are listed.
  - question: Which VM types should I create for the comparison?
    answer: >-
      Create an Arm-based c4a-standard-4 VM named "c4a" and an Intel-based Emerald Rapids c4-standard-8
      VM named "c4". The steps show how to launch each in the Google Cloud console.
  - question: Do I install Go, Sweet, and Benchstat on both VMs, and where should I run the install?
    answer: >-
      Yes, install on both VMs. The steps assume you run the installation from your home directory
      ($HOME), which results in a $HOME/benchmarks/sweet directory.
  - question: How do I execute and compare the benchmarks?
    answer: >-
      Run sweet on each VM to generate raw performance data. Then use benchstat to compare results
      from the different VMs.
  - question: What output should I expect from Benchstat?
    answer: >-
      Benchstat compares results to highlight performance differences and outputs text by default.
      It can also produce CSV output.
# END generated_summary_faq

author: Geremy Cohen

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
cloud_service_providers:
  - Google Cloud
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

