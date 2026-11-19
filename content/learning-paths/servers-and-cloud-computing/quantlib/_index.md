---
title: Benchmark QuantLib on Azure Cobalt

description: Learn how to build QuantLib on an Arm-based Azure Cobalt virtual machine and run benchmark workloads to evaluate performance on Arm64 cloud infrastructure.

minutes_to_complete: 60

who_is_this_for: This is an advanced topic for developers who want to build and benchmark QuantLib on Arm-based cloud instances.

learning_objectives:
  - Identify why QuantLib is a useful benchmark for Arm-based cloud systems.
  - Create and connect to an Arm64 Azure Cobalt virtual machine running Ubuntu.
  - Build QuantLib from source with benchmark support enabled.
  - Run QuantLib benchmark workloads with different sizes and thread counts.
  - Record and compare benchmark results in a repeatable way.

prerequisites:
    - An Azure account with permission to create virtual machines
    - Basic familiarity with the Linux command line and SSH
    - Basic experience building C++ software from source

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-11-19T15:59:43Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 7a0e1bc938569aaa47aa021d5993f8f40503ed629fbe97eee8d99cec5d2ed3d8
  summary_generated_at: '2026-11-19T15:59:43Z'
  summary_source_hash: 7a0e1bc938569aaa47aa021d5993f8f40503ed629fbe97eee8d99cec5d2ed3d8
  faq_generated_at: '2026-11-19T15:59:43Z'
  faq_source_hash: 7a0e1bc938569aaa47aa021d5993f8f40503ed629fbe97eee8d99cec5d2ed3d8
  summary: >-
    You'll build and benchmark QuantLib on an Azure Cobalt-based Arm virtual machine. You'll provision an Ubuntu
    virtual machine and build QuantLib from source with benchmark support and CPU-specific compiler flags. Then, you'll
    run the benchmark executable. After a baseline run, you'll keep the workload size fixed and
    change the number of worker processes. You'll then compare reported throughput and runtime
    across runs to study scaling.
  faqs:
  - question: What Azure virtual machine configuration should I use?
    answer: >-
      Choose an Arm64 VM in a region that offers Azure Cobalt, such as West US 2. Use the `Standard_D4ps_v5` machine type and
      Ubuntu Server 22.04 LTS. 
  - question: Where do I run the QuantLib benchmark?
    answer: >-
      Change to `~/QuantLib-$QL_VER/test-suite` and run `./quantlib-benchmark` after the
      build.
  - question: How do I vary workload size or worker count?
    answer: >-
      Use `--size` for the workload size and `--nProc` for the number of worker processes.
      Keep `--size` fixed when you compare worker counts.
  - question: How do I check that benchmark support was built?
    answer: >-
      Use the source `--enable-benchmark` configure option and `CFLAGS` and `CXXFLAGS`
      settings. You'll then find a runnable `quantlib-benchmark` executable in the test
      suite.
  - question: What should I record from each benchmark run?
    answer: >-
      Record your `--size` and `--nProc` values alongside reported throughput in tasks per
      second and runtime. You can compare your runs with the example results.
# END generated_summary_faq

author: Chris Moroney

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
platforms:
    - Microsoft Azure Cobalt
armips:
    - Neoverse
tools_software_languages:
    - Azure
    - Ubuntu
    - QuantLib
    - GCC
    - CMake
    - Bash
operatingsystems:
    - Linux

further_reading:
    - resource:
        title: QuantLib GitHub repository
        link: https://github.com/lballabio/QuantLib
        type: website
    - resource:
        title: Azure Virtual Machines documentation
        link: https://learn.microsoft.com/azure/virtual-machines/
        type: documentation
    - resource:
        title: Learn about Arm Neoverse processors
        link: /learning-paths/servers-and-cloud-computing/intro/
        type: learning-path

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---
