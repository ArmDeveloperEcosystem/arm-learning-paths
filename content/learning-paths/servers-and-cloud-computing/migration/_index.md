---
title: Migrating applications to Arm servers

minutes_to_complete: 15

who_is_this_for: This is an introductory topic for software developers looking to migrate applications to Arm servers.

description: Set up an Arm development environment, analyze dependencies, and understand common challenges and scenarios for migrating applications to Arm servers.

learning_objectives:
    - Set up an Arm development machine
    - Analyze application dependencies
    - Learn challenges and tips for application migration
    - Review common migration scenarios

prerequisites:
    - An [Arm based instance](/learning-paths/servers-and-cloud-computing/csp/) from a cloud service provider.

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T01:30:21Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 6b2b985c39579c4d0855c8c28b610ba558e25b451a6b755475ff4393e2810670
  summary_generated_at: '2026-06-02T04:24:49Z'
  summary_source_hash: 6b2b985c39579c4d0855c8c28b610ba558e25b451a6b755475ff4393e2810670
  faq_generated_at: '2026-06-03T01:30:21Z'
  faq_source_hash: 6b2b985c39579c4d0855c8c28b610ba558e25b451a6b755475ff4393e2810670
  summary: >-
    Learn the essentials of migrating applications to Arm servers on Linux. This introductory
    path guides you to set up an Arm-based development machine (typically a cloud instance), analyze
    application dependencies, and review common migration challenges and scenarios. It provides
    practical, language-specific guidance for C/C++ on Arm Neoverse with current compilers, Java
    on Arm (including areas to investigate for JVM performance), and Go (with emphasis on using
    recent releases). You also learn where to check third‑party software support using the Software
    Ecosystem Dashboard for Arm and the AWS Graviton Technical Guide. The only explicit prerequisite
    is access to an Arm-based instance from a cloud service provider.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need an Arm-based instance from a cloud service provider running Linux. A Linux Arm
      development machine can also be set up using a virtual machine such as Multipass.
  - question: Which C/C++ compiler versions should I use on Arm Neoverse?
    answer: >-
      Use the latest GCC or Clang/LLVM available for your Linux distribution. If a newer version
      is available beyond the distribution default, install that newer version.
  - question: How should I install Java on Arm Linux, and are there JVM options to consider?
    answer: >-
      There are several ways to install Java on Arm Linux; refer to the Java install guide linked
      from the path. Java runs well on Arm, and you should review which JVM flags impact performance.
  - question: Which Go version should I install for Arm servers?
    answer: >-
      Install the latest Go compiler and toolchain. Go 1.18 introduced a significant performance
      improvement, so staying current is recommended; refer to Go releases and the Go install
      guide.
  - question: Where can I check if my application’s dependencies or ISV software support Arm?
    answer: >-
      Use the Software Ecosystem Dashboard for Arm to review supported software. The AWS Graviton
      Technical Guide also lists ISV products with Arm support, and both resources accept GitHub
      issues for feedback.
# END generated_summary_faq

author: Jason Andrews

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
operatingsystems:
    - Linux
tools_software_languages:
    - Neon
    - SVE
    - Go
    - Runbook

further_reading:
    - resource:
        title: AWS Graviton Getting Started
        link: https://github.com/aws/aws-graviton-getting-started
        type: documentation
    - resource:
        title: AWS Graviton Processors
        link: https://dev.to/aws-builders/aws-graviton-processors-3nk3
        type: blog
    - resource:
        title: NVIDIA Getting Started with HPC on Arm64
        link: https://github.com/arm-hpc-devkit/nvidia-arm-hpc-devkit-users-guide
        type: blog
    - resource:
        title: Data points you need to know about ARM for your application code migration
        link: https://dev.to/aws-builders/data-points-you-need-to-know-about-arm-for-your-application-code-migration-5c0f
        type: blog
    - resource:
        title: Making your Go workloads up to 20% faster with Go 1.18 and AWS Graviton
        link: https://aws.amazon.com/blogs/compute/making-your-go-workloads-up-to-20-faster-with-go-1-18-and-aws-graviton/
        type: blog


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

