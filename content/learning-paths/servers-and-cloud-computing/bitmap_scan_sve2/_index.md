---
title: Accelerate Bitmap Scanning with Neon and SVE Instructions on Arm servers
description: Learn how to implement and benchmark bitmap scanning operations for database workloads using scalar, Neon, and SVE instructions on Arm-based cloud instances.

minutes_to_complete: 20

who_is_this_for: This is an introductory topic for database developers, performance engineers, and anyone interested in optimizing data processing workloads on Arm-based cloud instances.


learning_objectives:
  - Understand bitmap scanning operations in database systems
  - Implement bitmap scanning with scalar, Neon, and SVE instructions
  - Compare performance between different implementations
  - Measure performance improvements on Graviton4 instances

prerequisites:
- An [Arm based instance](/learning-paths/servers-and-cloud-computing/csp/) from an appropriate
  cloud service provider.

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T00:25:22Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 1701b37580fe5d012a5e6fd322307742656a748dfb766fd48914011167386e95
  summary_generated_at: '2026-06-02T03:12:13Z'
  summary_source_hash: 1701b37580fe5d012a5e6fd322307742656a748dfb766fd48914011167386e95
  faq_generated_at: '2026-06-03T00:25:22Z'
  faq_source_hash: 1701b37580fe5d012a5e6fd322307742656a748dfb766fd48914011167386e95
  summary: >-
    Learn how to implement and benchmark bitmap scanning for database workloads on Arm-based cloud
    instances running Linux. You will build a simple bitmap data structure and multiple scanning
    routines in C—covering scalar, Neon, and SVE—and add a benchmarking harness to compare their
    behavior. The steps focus on Arm Neoverse servers, with examples targeting Neoverse V2–based
    instances such as AWS Graviton4, so you can measure performance differences across implementations.
    This introductory path is aimed at database developers and performance engineers; the only
    explicit prerequisite is access to an Arm-based instance from a cloud provider such as AWS,
    Microsoft Azure, Google Cloud, or Oracle.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      Provision an Arm-based instance from an appropriate cloud service provider running Linux.
      For the SVE sections, use a Neoverse V2–based server such as AWS Graviton4.
  - question: Where do I put the code for this Learning Path?
    answer: >-
      Create a file named bitvector_scan_benchmark.c with a text editor and copy in the provided
      code sections. This single file will contain the bit vector data structure, scalar implementations,
      Neon and SVE versions, and the benchmarking code.
  - question: Which bitmap scanning implementations will I build and compare?
    answer: >-
      You will implement a per-bit scalar baseline, an optimized scalar approach for sparse data,
      and vectorized versions using Neon and SVE. These are all placed in the same C source file
      for side-by-side benchmarking.
  - question: What results should I expect from the benchmarking step?
    answer: >-
      The benchmarking framework times multiple iterations using CLOCK_MONOTONIC and reports how
      many set-bit positions are found. You will be able to compare the relative performance of
      the scalar, Neon, and SVE implementations; specific numeric results are not provided.
  - question: How do I validate that all implementations are correct?
    answer: >-
      Use the same generated bitmaps and compare the counts (and positions if captured) returned
      by each implementation. The Learning Path includes helper functions to generate and analyze
      bitmaps so you can verify consistency across scalar, Neon, and SVE scans.
# END generated_summary_faq

author: Pareena Verma


### Tags
skilllevels: Introductory
subjects: Performance and Architecture
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
- SVE
- Neon
- Runbook

further_reading:
    - resource:
        title: Accelerate multi-token search in strings with SVE2 SVMATCH instruction
        link: https://community.arm.com/arm-community-blogs/b/architectures-and-processors-blog/posts/multi-token-search-strings-svmatch-instruction
        type: blog
    - resource:
        title: Arm SVE2 Programming Guide
        link: https://developer.arm.com/documentation/102340/latest/
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

