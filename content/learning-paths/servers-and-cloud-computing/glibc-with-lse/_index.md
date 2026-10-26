---
title: Learn about glibc with Large System Extensions for performance improvement
description: Rebuild and benchmark glibc with LSE atomics on Arm servers, then evaluate scalability using MongoDB workloads and guidance on when LSE delivers a measurable uplift.

minutes_to_complete: 60

who_is_this_for: This is an advanced topic for software developers interested in learning how to improve the performance of their workloads on Arm servers.

learning_objectives:
  - Build and install glibc with Large System Extensions (LSE) on an Arm server.
  - Benchmark workload performance using glibc with LSE optimizations.
  - Benchmark MongoDB using glibc with LSE optimizations.

prerequisites:
  - An Arm-based instance from a cloud service provider
  - Review the learning path on [LSE](/learning-paths/servers-and-cloud-computing/lse/)

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-09-10T22:08:32Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 3e7669935944f2d75d64937d9a1b2b4ba21745c7fecf9f5f45642550a0128dcd
  summary_generated_at: '2026-09-10T22:08:32Z'
  summary_source_hash: 3e7669935944f2d75d64937d9a1b2b4ba21745c7fecf9f5f45642550a0128dcd
  faq_generated_at: '2026-09-10T22:08:32Z'
  faq_source_hash: 3e7669935944f2d75d64937d9a1b2b4ba21745c7fecf9f5f45642550a0128dcd
  summary: >-
    You'll rebuild `glibc` with Arm LSE and evaluate the runtime with MongoDB. First, you'll build MongoDB from source, run YCSB workloads with the LSE-enabled library, and repeat the benchmark with a NoLSE baseline. By comparing throughput and runtime, you can determine whether LSE-enabled atomics make a measurable difference for MongoDB workloads.
  faqs:
  - question: How do I start MongoDB with the custom glibc?
    answer: >-
      First, copy `libcrypt.so` into the custom glibc build's `crypt` directory. Then, launch
      `mongod` through `testrun.sh` with `mongodb.conf` and the WiredTiger cache setting.
  - question: Which MongoDB version should I build for the benchmark?
    answer: >-
      Use the repository tag r5.3.2.
  - question: Which YCSB workload should I run for the comparison?
    answer: >-
      Use a single YCSB workload profile and keep it identical across both LSE and NoLSE runs to compare results under consistent conditions.
  - question: What output should I capture from the NoLSE baseline to compare later?
    answer: >-
      Record the summary lines that include `[OVERALL] RunTime(ms)` and `[OVERALL] Throughput(ops/sec)`.
      The example output also shows GC statistics that you can keep for reference.
  - question: What performance uplift does the example report for LSE?
    answer: >-
      The example reports about 3.14% uplift: throughput increases from 6,662.13 operations per
      second with No-LSE `glibc` to 6,871.61 operations per second with LSE `glibc`.
# END generated_summary_faq

author: Ying Yu

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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
