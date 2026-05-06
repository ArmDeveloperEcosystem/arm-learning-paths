---
title: Benchmark Linux kernel performance on Arm servers with Fastpath
description: Learn how to build custom Linux kernels using tuxmake and Fastpath, then benchmark and compare kernel versions on Arm-based EC2 instances.

minutes_to_complete: 90

who_is_this_for: This is an advanced topic for software developers and performance engineers who want to benchmark and compare different Linux kernel versions on Arm servers.

learning_objectives:
    - Build custom Linux kernels for Arm systems using tuxmake and Fastpath
    - Configure and provision Arm-based EC2 instances for kernel testing
    - Create and execute test plans that compare kernel performance across versions
    - Analyze benchmark results to identify performance differences between kernels

prerequisites:
    - An AWS account with permissions to create EC2 instances
    - Familiarity with basic Linux administration and SSH

generate_summary_faq: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-05-06T17:17:57Z'
  generator: template
  source_hash: 978d3da8668e38758c138313c31809f3de5a8cefd1b7c2b47a536c0ee364b692
  summary: >-
    Learn how to build custom Linux kernels using tuxmake and Fastpath, then benchmark and compare
    kernel versions on Arm-based EC2 instances. It is designed for software developers and performance
    engineers who want to benchmark and compare different Linux kernel versions on Arm servers.
    By the end, you will be able to build custom Linux kernels for Arm systems using tuxmake and
    Fastpath, configure and provision Arm-based EC2 instances for kernel testing, and create and
    execute test plans that compare kernel performance across versions. It focuses on tools and
    technologies such as Fastpath, tuxmake, and Linux, Linux environments, Arm platforms including
    Neoverse, and cloud platforms such as AWS. The main steps cover Understand the Fastpath kernel
    benchmarking workflow, Set up the kernel build host, Set up the Fastpath host, Set up the
    System Under Test, and Generate and execute the benchmark plan.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will build custom Linux kernels for Arm systems using tuxmake and Fastpath, configure
      and provision Arm-based EC2 instances for kernel testing, and create and execute test plans
      that compare kernel performance across versions. Learn how to build custom Linux kernels
      using tuxmake and Fastpath, then benchmark and compare kernel versions on Arm-based EC2
      instances.
  - question: Who is this Learning Path for?
    answer: >-
      This is an advanced topic for software developers and performance engineers who want to
      benchmark and compare different Linux kernel versions on Arm servers.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: An AWS account with permissions to create
      EC2 instances; Familiarity with basic Linux administration and SSH.
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including Fastpath, tuxmake, and Linux, Linux environments,
      Arm platforms such as Neoverse, and cloud platforms such as AWS.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Understand the Fastpath kernel benchmarking workflow,
      Set up the kernel build host, Set up the Fastpath host, Set up the System Under Test, and
      Generate and execute the benchmark plan.
# END generated_summary_faq

author: Geremy Cohen

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
cloud_service_providers:
  - AWS
armips:
    - Neoverse
operatingsystems:
    - Linux
tools_software_languages:
    - Fastpath
    - tuxmake
    - Linux

further_reading:
    - resource:
        title: Fastpath documentation
        link: https://fastpath.docs.arm.com/en/latest/index.html
        type: documentation
    - resource:
        title: Kernel install guide
        link: /learning-paths/servers-and-cloud-computing/kernel-build/
        type: guide
    - resource:
        title: AWS Compute Service Provider learning path
        link: /learning-paths/servers-and-cloud-computing/csp/
        type: guide

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---

