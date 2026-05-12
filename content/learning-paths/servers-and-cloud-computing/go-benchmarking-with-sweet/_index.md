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
  template_version: summary-faq-v1
  generated_at: '2026-05-06T17:17:57Z'
  generator: template
  source_hash: aa78434138f08b424352302e92a1cd40d8297459bc65202715dcb41c40de6057
  summary: >-
    Learn how to provision Arm64 and x86_64 VM instances on Google Cloud, then install and use
    Sweet and Benchstat to measure and compare Go application performance. It is designed for
    This introductory topic is for developers who want to measure and compare the performance
    of Go applications on Arm-based servers. By the end, you will be able to provision Arm64 and
    x86_64 VM instances on Google Cloud, install Go, Sweet, and Benchstat on each VM instance,
    and run benchmarks and use Benchstat to compare Go application performance across architectures.
    It focuses on tools and technologies such as Go, Linux environments, Arm platforms including
    Neoverse, and cloud platforms such as Google Cloud. The main steps cover Overview, Launch
    an Arm-based c4a-standard-4 instance, Launch an Intel Emerald Rapids c4-standard-8 instance,
    Install Go, Sweet, and Benchstat, and Benchmark types and metrics.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will provision Arm64 and x86_64 VM instances on Google Cloud, install Go, Sweet, and
      Benchstat on each VM instance, and run benchmarks and use Benchstat to compare Go application
      performance across architectures. Learn how to provision Arm64 and x86_64 VM instances on
      Google Cloud, then install and use Sweet and Benchstat to measure and compare Go application
      performance.
  - question: Who is this Learning Path for?
    answer: >-
      This introductory topic is for developers who want to measure and compare the performance
      of Go applications on Arm-based servers.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: A [Google Cloud account](https://console.cloud.google.com/).
      This Learning Path can be run on any cloud provider or on-premises, but it focuses on Google
      Cloud’s Axion Arm64-based instances.; A local machine with [Google Cloud CLI](/install-guides/gcloud/)
      installed.
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including Go, Linux environments, Arm platforms such as Neoverse,
      and cloud platforms such as Google Cloud.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Overview, Launch an Arm-based c4a-standard-4 instance,
      Launch an Intel Emerald Rapids c4-standard-8 instance, Install Go, Sweet, and Benchstat,
      and Benchmark types and metrics.
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

