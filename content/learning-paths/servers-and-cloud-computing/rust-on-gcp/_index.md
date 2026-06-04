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
  template_version: summary-faq-v3
  generated_at: '2026-06-03T02:04:00Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: c3dd7a0ff9c645635e41b2d9110f4c52de627b752e33c3c6775e1d2e3ffc381d
  summary_generated_at: '2026-06-02T05:07:00Z'
  summary_source_hash: c3dd7a0ff9c645635e41b2d9110f4c52de627b752e33c3c6775e1d2e3ffc381d
  faq_generated_at: '2026-06-03T02:04:00Z'
  faq_source_hash: c3dd7a0ff9c645635e41b2d9110f4c52de627b752e33c3c6775e1d2e3ffc381d
  summary: >-
    This introductory Learning Path shows how to deploy and benchmark Rust on Google Cloud C4A
    virtual machines powered by Arm-based Axion processors (Arm Neoverse-V2 cores). You will provision
    a SUSE SLES Arm64 instance in the Google Cloud Console (for example, c4a-standard-4 with 4
    vCPUs and 16 GB memory), install Rust with rustup and essential build tools, verify the toolchain
    by building and running a simple program, and run cargo bench with Criterion to measure execution
    speed and stability. It targets developers working on Linux/Arm64 in Google Cloud and takes
    about 30 minutes. Prerequisites are a GCP account with billing enabled and basic Rust familiarity.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need a Google Cloud Platform (GCP) account with billing enabled and basic familiarity
      with Rust. No other explicit prerequisites are listed.
  - question: Which VM type and OS should I create on Google Cloud?
    answer: >-
      Use a Google Axion C4A Arm instance, specifically the c4a-standard-4 machine type in the
      Google Cloud Console. The Learning Path provisions a SUSE SLES Arm64 environment on this
      instance.
  - question: How do I install Rust and build tools on the SUSE Arm64 VM?
    answer: >-
      Update the system with zypper and install curl, gcc, and make. Then install Rust using rustup
      to prepare the environment for building and benchmarking Rust applications.
  - question: How do I verify that the Rust toolchain is working?
    answer: >-
      Create a new project with cargo new hello, then run it with cargo run. A successful build
      prints the standard Hello, world! message and shows normal Cargo compile and run output.
  - question: How do I set up and run benchmarks with Criterion?
    answer: >-
      Create a new project, add criterion = "0.5" to Cargo.toml, and define a bench target (for
      example, my_benchmark with harness = false). Place your benchmark code under benches/ and
      run cargo bench to execute Criterion and collect performance measurements on Arm64.
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

