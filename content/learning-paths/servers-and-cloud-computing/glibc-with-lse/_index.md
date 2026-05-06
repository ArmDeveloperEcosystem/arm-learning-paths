---
title: Learn about glibc with Large System Extensions (LSE) for performance improvement
description: Rebuild and benchmark glibc with LSE atomics on Arm servers, then evaluate scalability using MongoDB workloads and guidance on when LSE delivers a measurable uplift.

minutes_to_complete: 60

who_is_this_for: This is an advanced topic for software developers interested in learning how to improve the performance of their workloads on Arm servers.

learning_objectives:
- Build and install glibc with LSE on an Arm server
- Benchmark workload performance using glibc with LSE optimizations
- Benchmark MongoDB using glibc with LSE optimizations

prerequisites:
- An Arm based instance from a cloud service provider.
- Review the learning path on [LSE](/learning-paths/servers-and-cloud-computing/lse/)

generate_summary_faq: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-05-06T17:17:57Z'
  generator: template
  source_hash: 74952d68380c7540306543b0a7520f6960f673dd55ad5f164365fcfe1470380e
  summary: >-
    Rebuild and benchmark glibc with LSE atomics on Arm servers, then evaluate scalability using
    MongoDB workloads and guidance on when LSE delivers a measurable uplift. It is designed for
    software developers interested in learning how to improve the performance of their workloads
    on Arm servers. By the end, you will be able to build and install glibc with LSE on an Arm
    server, benchmark workload performance using glibc with LSE optimizations, and benchmark MongoDB
    using glibc with LSE optimizations. It focuses on tools and technologies such as glibc, LSE,
    MongoDB, and Runbook, Linux environments, and Arm platforms including Neoverse. The main steps
    cover Build Glibc with LSE, Start MongoDB utilizing the newly built Glibc with LSE, Benchmark
    MongoDB with YCSB, and Compare the results with LSE and NoLSE.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will build and install glibc with LSE on an Arm server, benchmark workload performance
      using glibc with LSE optimizations, and benchmark MongoDB using glibc with LSE optimizations.
      Rebuild and benchmark glibc with LSE atomics on Arm servers, then evaluate scalability using
      MongoDB workloads and guidance on when LSE delivers a measurable uplift.
  - question: Who is this Learning Path for?
    answer: >-
      This is an advanced topic for software developers interested in learning how to improve
      the performance of their workloads on Arm servers.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: An Arm based instance from a cloud service
      provider.; Review the learning path on [LSE](/learning-paths/servers-and-cloud-computing/lse/).
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including glibc, LSE, MongoDB, and Runbook, Linux environments,
      and Arm platforms such as Neoverse.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Build Glibc with LSE, Start MongoDB utilizing the
      newly built Glibc with LSE, Benchmark MongoDB with YCSB, and Compare the results with LSE
      and NoLSE.
# END generated_summary_faq

author: Ying Yu

### Tags
skilllevels: Advanced
subjects: Performance and Architecture

armips:
- Neoverse



operatingsystems:
- Linux

tools_software_languages:
- glibc
- LSE
- MongoDB
- Runbook



further_reading:
    - resource:
        title: Arm's LSE for atomics and MySQL
        link: https://mysqlonarm.github.io/ARM-LSE-and-MySQL/
        type: blog
    - resource:
        title: MongoDB documentation
        link: https://www.mongodb.com/docs/
        type: documentation


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

