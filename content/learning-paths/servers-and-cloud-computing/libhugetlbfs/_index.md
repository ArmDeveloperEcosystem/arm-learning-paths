---
title: Increase application performance with libhugetlbfs 

minutes_to_complete: 60

who_is_this_for: This is an advanced topic for engineers looking for ways to increase performance on Arm servers.

description: Enable and measure libhugetlbfs performance improvements for MySQL and other workloads on Arm Linux servers.

learning_objectives:
    - Enable libhugetlbfs on an Arm server running Linux
    - Evaluate performance improvements for workloads such as MySQL

prerequisites:
    - An Arm server or virtual machine instance from a cloud service provider with Ubuntu installed
    - Knowledge of how to build a MySQL server and run the sysbench benchmark test

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T01:21:05Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 66d13edff1371295f0e88a618e924ca67b85bcc8aa72034d1e582a0b267f0d05
  summary_generated_at: '2026-06-02T04:16:07Z'
  summary_source_hash: 66d13edff1371295f0e88a618e924ca67b85bcc8aa72034d1e582a0b267f0d05
  faq_generated_at: '2026-06-03T01:21:05Z'
  faq_source_hash: 66d13edff1371295f0e88a618e924ca67b85bcc8aa72034d1e582a0b267f0d05
  summary: >-
    This Learning Path shows how to enable libhugetlbfs on an Arm server running Ubuntu Linux
    and measure its impact on memory-intensive workloads. You will configure hugepages so application
    text, data, malloc, and shared memory can use larger pages, then apply the approach to MySQL
    by modifying its build flags and benchmarking with sysbench to compare results. The target
    environment is an Arm server or a cloud VM (for example, from AWS, Microsoft Azure, Google
    Cloud, or Oracle) with Ubuntu installed. This advanced path expects familiarity with building
    MySQL and running sysbench. Tools referenced include GCC and MySQL. Estimated time to complete
    is about 60 minutes.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need an Arm server or virtual machine with Ubuntu installed, plus knowledge of how to
      build a MySQL server and run the sysbench benchmark test. No additional prerequisites are
      explicitly listed.
  - question: Can I use a cloud VM for this Learning Path?
    answer: >-
      Yes. An Arm-based instance from AWS, Microsoft Azure, Google Cloud, or Oracle with Ubuntu
      installed meets the environment requirement.
  - question: Where do I add libhugetlbfs build options when compiling MySQL?
    answer: >-
      Add the options to both -DCMAKE_C_FLAGS and -DCMAKE_CXX_FLAGS during the MySQL build configuration
      as described in the steps. The path shows the required flags to enable libhugetlbfs.
  - question: Do I need to change both build and run settings for MySQL?
    answer: >-
      Yes. The steps explain how to modify both the build and the run of the MySQL server to enable
      libhugetlbfs.
  - question: How should I evaluate the effect of enabling libhugetlbfs?
    answer: >-
      Run your baseline workload, then enable libhugetlbfs and repeat the same test to compare
      results. For MySQL, you are expected to use sysbench to measure before-and-after performance.
# END generated_summary_faq

author: Bolt Liu

skilllevels: Advanced
subjects: Databases
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

