---
title: Build and benchmark a WebAssembly app on AWS Graviton with wasmCloud


generate_summary_faq: true
description: Build a small Rust HTTP application as a WebAssembly component, run it with wasmCloud on AWS Graviton, and measure response time and throughput.

minutes_to_complete: 45

who_is_this_for: This is an introductory topic for developers who want to run WebAssembly applications on Arm servers and understand their performance characteristics.

learning_objectives:
  - Identify how a WebAssembly component and its wasmCloud host work together.
  - Build and run a Rust HTTP handler on an AWS Graviton server.
  - Measure warm response time and concurrent request throughput.
  - Interpret the measurements and explain when instance reuse can help.

prerequisites:
  - An AWS account and an [AWS Graviton instance](/learning-paths/servers-and-cloud-computing/csp/) running Ubuntu 24.04 with SSH access and sudo privileges
  - Basic Linux command-line knowledge and familiarity with HTTP requests
  

author:
    - Jason Andrews
    - Liam Randall
 
generate_summary_faqs: true
rerun_summary: false
rerun_faqs: false

skilllevels: Introductory
subjects: Web
platforms:
  - AWS Graviton
armips:
  - Neoverse
tools_software_languages:
  - wasmCloud
  - Rust
  - WebAssembly
operatingsystems:
  - Linux
further_reading:
  - resource:
      title: wasmCloud application quickstart
      link: https://wasmcloud.com/docs/quickstart/
      type: documentation
  - resource:
      title: wasmCloud runtime
      link: https://wasmcloud.com/docs/runtime/
      type: documentation
  - resource:
      title: wasmCloud benchmark scripts
      link: https://github.com/wasmCloud/wasmCloud/tree/main/scripts/bench
      type: documentation
  - resource:
      title: wasmCloud benchmark results
      link: https://wasmcloud.github.io/arewefastyet/
      type: documentation
  - resource:
      title: wrk HTTP benchmarking tool
      link: https://github.com/wg/wrk
      type: documentation
  - resource:
      title: Install Rust on Arm Linux
      link: /install-guides/rust/
      type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---
