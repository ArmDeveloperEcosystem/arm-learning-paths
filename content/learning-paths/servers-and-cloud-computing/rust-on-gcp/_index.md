---
title: Deploy Rust on Google Cloud C4A (Arm-based Axion VMs)

description: Learn to deploy and benchmark Rust applications on Google Cloud C4A virtual machines powered by Arm-based Axion processors.

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for developers deploying and optimizing Rust workloads on Linux/Arm64 environments, specifically using Google Cloud C4A virtual machines powered by Axion processors. 

learning_objectives:
  - Provision an Arm-based SUSE SLES virtual machine on Google Cloud (C4A with Axion processors)
  - Install Rust and configure the development environment on a SUSE Arm64 (C4A) instance
  - Verify Rust setup by compiling and running a sample program to ensure toolchain functionality 
  - Benchmark Rust using cargo bench with Criterion to measure execution speed, stability, and performance on Arm64 systems

prerequisites:
  - A [Google Cloud Platform (GCP)](https://cloud.google.com/free) account with billing enabled  
  - Basic familiarity with [Rust](https://www.rust-lang.org/)

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false
# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-05-06T17:17:59Z'
  generator: template
  source_hash: c3dd7a0ff9c645635e41b2d9110f4c52de627b752e33c3c6775e1d2e3ffc381d
  summary: >-
    Learn to deploy and benchmark Rust applications on Google Cloud C4A virtual machines powered
    by Arm-based Axion processors. It is designed for developers deploying and optimizing Rust
    workloads on Linux/Arm64 environments, specifically using Google Cloud C4A virtual machines
    powered by Axion processors. By the end, you will be able to provision an Arm-based SUSE SLES
    virtual machine on Google Cloud (C4A with Axion processors), install Rust and configure the
    development environment on a SUSE Arm64 (C4A) instance, and verify Rust setup by compiling
    and running a sample program to ensure toolchain functionality. It focuses on tools and technologies
    such as Rust, Cargo, and Criterion, Linux environments, Arm platforms including Neoverse,
    and cloud platforms such as Google Cloud. The main steps cover Get started with Rust on Google
    Axion C4A (Arm Neoverse-V2), Create a Google Axion C4A Arm virtual machine on GCP, Perform
    baseline testing, Benchmark Rust performance using Criterion, and FIXED, DO NOT MODIFY.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will provision an Arm-based SUSE SLES virtual machine on Google Cloud (C4A with Axion
      processors), install Rust and configure the development environment on a SUSE Arm64 (C4A)
      instance, and verify Rust setup by compiling and running a sample program to ensure toolchain
      functionality. Learn to deploy and benchmark Rust applications on Google Cloud C4A virtual
      machines powered by Arm-based Axion processors.
  - question: Who is this Learning Path for?
    answer: >-
      This is an introductory topic for developers deploying and optimizing Rust workloads on
      Linux/Arm64 environments, specifically using Google Cloud C4A virtual machines powered by
      Axion processors.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: A [Google Cloud Platform (GCP)](https://cloud.google.com/free)
      account with billing enabled; Basic familiarity with [Rust](https://www.rust-lang.org/).
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including Rust, Cargo, and Criterion, Linux environments,
      Arm platforms such as Neoverse, and cloud platforms such as Google Cloud.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Get started with Rust on Google Axion C4A (Arm Neoverse-V2),
      Create a Google Axion C4A Arm virtual machine on GCP, Perform baseline testing, Benchmark
      Rust performance using Criterion, and FIXED, DO NOT MODIFY.
# END generated_summary_faq

author: Pareena Verma

##### Tags
skilllevels: Introductory
subjects: Performance and Architecture
cloud_service_providers:
  - Google Cloud

armips:
  - Neoverse

tools_software_languages:
  - Rust
  - Cargo
  - Criterion

operatingsystems:
  - Linux

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
further_reading:
  - resource:
      title: Google Cloud documentation
      link: https://cloud.google.com/docs
      type: documentation

  - resource:
      title: Rust documentation
      link: https://doc.rust-lang.org/stable/
      type: documentation
  
  - resource:
      title: Cargo bench documentation
      link: https://doc.rust-lang.org/cargo/commands/cargo-bench.html
      type: documentation   

weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---

