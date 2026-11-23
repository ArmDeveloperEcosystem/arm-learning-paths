---
title: Deploy Rust on Arm-based Google Cloud C4A virtual machines

description: Learn to deploy and benchmark Rust applications on Google Cloud C4A virtual machines powered by Arm-based Axion processors.

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for developers deploying and optimizing Rust workloads on Linux/Arm64 environments, specifically using Google Cloud C4A virtual machines (VMs) powered by Axion processors. 

learning_objectives:
  - Provision an Arm-based SUSE Linux Enterprise Server (VM) on Google Cloud.
  - Install Rust and configure the development environment on a SUSE Arm64 C4A instance.
  - Verify Rust setup by compiling and running a sample program to ensure toolchain functionality.
  - Benchmark Rust using cargo bench with Criterion to measure execution speed, stability, and performance.

prerequisites:
  - A [Google Cloud Platform (GCP)](https://cloud.google.com/free) account with billing enabled  
  - Basic familiarity with [Rust](https://www.rust-lang.org/)

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-11-23T20:58:10Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 1be76412266eadb1a632cfbb0d94f70e68034c85d3689c6d5b74dc3bd75bed48
  summary_generated_at: '2026-11-23T20:58:10Z'
  summary_source_hash: 1be76412266eadb1a632cfbb0d94f70e68034c85d3689c6d5b74dc3bd75bed48
  faq_generated_at: '2026-11-23T20:58:10Z'
  faq_source_hash: 1be76412266eadb1a632cfbb0d94f70e68034c85d3689c6d5b74dc3bd75bed48
  summary: You'll build and benchmark Rust code on a Google Axion C4A VM running SUSE
    Linux. First, you'll provision the instance and install the Rust toolchain. You'll then create a small
    Cargo project to check compilation and execution, then measure its build time. Finally, you'll
    configure a Criterion benchmark in a separate project and run `cargo bench` to inspect the
    results.
  faqs:
  - question: How do I check that Rust compiles on the C4A instance?
    answer: Create a sample project with `cargo new hello`, then run `cargo run`. A successful
      build and program run checks the toolchain before benchmarking.
  - question: Which SUSE packages do I install before Rust?
    answer: Refresh and update packages with `sudo zypper refresh` and `sudo zypper update -y`. 
      Then, install `curl`, `gcc`, and `make` with `sudo zypper install -y curl gcc make`.
  - question: Which files does the sample Cargo project create?
    answer: After `cargo new hello`, inspect `Cargo.toml` for project configuration and `src/main.rs`
      for the sample program. Use `cargo run` to build and run it.
  - question: Where do I configure Criterion?
    answer: Add the Criterion dependency and a `[[bench]]` target to `Cargo.toml` in the benchmark
      project. After that, create the benchmark source file.
  - question: What should I inspect after running the benchmark?
    answer: Check that Criterion completes without errors. Review its measured benchmark results
      in the console output.
# END generated_summary_faq

author: Pareena Verma

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

##### Tags
skilllevels: Introductory
subjects: Performance and Architecture
platforms:
  - Google Axion

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

