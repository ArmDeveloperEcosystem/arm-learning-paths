---
title: Deploy Rust on Google Cloud C4A (Arm-based Axion VMs)

minutes_to_complete: 30

who_is_this_for: This learning path is intended for software developers deploying and optimizing Rust workloads on Linux/Arm64 environments, specifically using Google Cloud C4A virtual machines powered by Axion processors. 

learning_objectives:
  - Provision an Arm-based SUSE SLES virtual machine on Google Cloud (C4A with Axion processors)
  - Install Rust and configure the development environment on a SUSE Arm64 (C4A) instance
  - Verify Rust setup by compiling and running a sample program to ensure toolchain functionality 
  - Benchmark Rust using cargo bench with Criterion to measure execution speed, stability, and performance on Arm64 systems

prerequisites:
  - A [Google Cloud Platform (GCP)](https://cloud.google.com/free) account with billing enabled  
  - Basic familiarity with [Rust](https://www.rust-lang.org/)

author: Pareena Verma

##### Tags
skilllevels: Introductory
subjects: Performance and Architecture
cloud_service_providers: Google Cloud

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
