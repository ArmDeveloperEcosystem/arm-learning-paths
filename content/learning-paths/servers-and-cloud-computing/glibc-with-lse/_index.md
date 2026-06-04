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

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T01:06:30Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 74952d68380c7540306543b0a7520f6960f673dd55ad5f164365fcfe1470380e
  summary_generated_at: '2026-06-02T04:04:16Z'
  summary_source_hash: 74952d68380c7540306543b0a7520f6960f673dd55ad5f164365fcfe1470380e
  faq_generated_at: '2026-06-03T01:06:30Z'
  faq_source_hash: 74952d68380c7540306543b0a7520f6960f673dd55ad5f164365fcfe1470380e
  summary: >-
    This advanced path shows how to rebuild and install glibc with Armv8-A Large System Extensions
    (LSE) on an Arm server running Linux, then benchmark the impact on MongoDB. You will build
    MongoDB 5.3.2 from source to run with the LSE-enabled glibc, drive workloads using YCSB, and
    compare results against a No-LSE baseline. The steps focus on measuring throughput and runtime
    characteristics and provide guidance on when LSE can deliver a measurable uplift for multi-threaded
    workloads. Prerequisites are an Arm-based instance from a cloud service provider and a prior
    review of the LSE learning path. Expected duration is about 60 minutes.
  faqs:
  - question: What do I need before running this Learning Path?
    answer: >-
      You need an Arm-based instance from a cloud service provider running Linux. You should also
      review the separate Learning Path on LSE before starting. This is an advanced topic intended
      for experienced developers.
  - question: Do I need to rebuild glibc on the instance, and why?
    answer: >-
      Yes. The steps have you build and install glibc with LSE so library routines can use LSE
      atomic operations available on ARMv8-A, which you will then evaluate with workloads.
  - question: Which MongoDB version is used and how is it installed?
    answer: >-
      MongoDB 5.3.2 is built from source using the provided commands. You clone the repository,
      check out r5.3.2, install the listed dependencies, and build with SCons.
  - question: How do I run and validate the benchmarks with and without LSE?
    answer: >-
      You run YCSB against MongoDB configured to use the newly built glibc with LSE, then repeat
      with a No-LSE configuration. Compare the YCSB output, focusing on lines such as [OVERALL]
      Throughput(ops/sec), as shown in the examples.
  - question: What result should I expect from the No-LSE baseline?
    answer: >-
      YCSB prints summary lines including overall runtime, throughput in ops/sec, and GC metrics.
      The path provides a sample No-LSE output format that you can use to compare against the
      LSE run.
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

