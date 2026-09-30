---
title: Increase application performance with libhugetlbfs 

minutes_to_complete: 60

who_is_this_for: This is an advanced topic for engineers looking for ways to increase performance on Arm servers.

description: Enable and measure libhugetlbfs performance improvements for MySQL and other workloads on Arm Linux servers.

learning_objectives:
    - Enable `libhugetlbfs` on an Arm server running Linux.
    - Evaluate performance improvements for workloads such as MySQL.

prerequisites:
    - An Arm server or virtual machine instance from a cloud service provider with Ubuntu installed
    - Knowledge of how to build a MySQL server and run the sysbench benchmark test

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-09-15T21:24:53Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 7bde4f2f84516a1671b2269f859bd167080d76755331e15d4ee08eb1c0a9e00c
  summary_generated_at: '2026-09-15T21:24:53Z'
  summary_source_hash: 7bde4f2f84516a1671b2269f859bd167080d76755331e15d4ee08eb1c0a9e00c
  faq_generated_at: '2026-09-15T21:24:53Z'
  faq_source_hash: 7bde4f2f84516a1671b2269f859bd167080d76755331e15d4ee08eb1c0a9e00c
  summary: >-
    You'll enable `libhugetlbfs` on an Arm Linux server and configure hugepages for application
    text, data, heap allocations, and shared memory. First, you'll apply the settings to a MySQL
    workload, use `sysbench` to capture a baseline, and compare results after the change. Then, you'll
    use the comparison to evaluate whether large pages might help workloads affected by
    frequent TLB misses.
  faqs:
  - question: Which build options do I need to change to compile MySQL with libhugetlbfs?
    answer: >-
      Add the flags to both `-DCMAKE_C_FLAGS` and `-DCMAKE_CXX_FLAGS` when you configure
      the MySQL build. Applying the flags to both C and C++ ensures the full server build picks
      up the change.
  - question: Do I also need to change how I start mysqld after building?
    answer: >-
      Yes. Change both the build and the run of the MySQL server to enable
      `libhugetlbfs`.
  - question: What should I check if the build fails after I add the flags?
    answer: >-
      Confirm that you applied the options to both `-DCMAKE_C_FLAGS` and `-DCMAKE_CXX_FLAGS`. Verify that the
      required Ubuntu packages for `libhugetlbfs` are installed, and that the library path you reference
      matches your system.
  - question: How do I measure whether libhugetlbfs helped my MySQL workload?
    answer: >-
      Use your existing sysbench workflow to record a baseline, enable `libhugetlbfs`, and rerun
      the same tests. Compare the before-and-after results to evaluate any change.
  - question: When is libhugetlbfs likely to help my application?
    answer: >-
      `libhugetlbfs` can benefit applications that use considerable amounts of memory and might incur many TLB
      misses. Workloads with sizable code, data, or heap sections are good candidates.
# END generated_summary_faq

author: Bolt Liu

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

skilllevels: Advanced
subjects: Databases
platforms:
  - AWS Graviton
  - Microsoft Azure Cobalt
  - Google Axion
  - Oracle Cloud Infrastructure (OCI) Ampere Compute
armips:
    - Neoverse
operatingsystems:
    - Linux
tools_software_languages:
    - MySQL
    - GCC
    - Runbook

test_images:
    - ubuntu:latest
test_link: null
test_maintenance: false

further_reading:
    - resource:
        title: libhugetlbfs manual page
        link: https://linux.die.net/man/7/libhugetlbfs
        type: documentation
    - resource:
        title: libhugetlbfs HOW TO
        link: https://github.com/libhugetlbfs/libhugetlbfs/blob/master/HOWTO
        type: documentation

weight: 1
layout: learningpathall
learning_path_main_page: 'yes'
---
