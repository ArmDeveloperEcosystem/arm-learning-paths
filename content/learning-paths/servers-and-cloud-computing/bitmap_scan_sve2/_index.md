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
- An [Arm-based instance](/learning-paths/servers-and-cloud-computing/csp/) from an appropriate cloud service provider.

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-30T21:37:19Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 1701b37580fe5d012a5e6fd322307742656a748dfb766fd48914011167386e95
  summary_generated_at: '2026-06-30T21:37:19Z'
  summary_source_hash: 1701b37580fe5d012a5e6fd322307742656a748dfb766fd48914011167386e95
  faq_generated_at: '2026-06-30T21:37:19Z'
  faq_source_hash: 1701b37580fe5d012a5e6fd322307742656a748dfb766fd48914011167386e95
  summary: >-
    You'll implement and benchmark bitmap scanning for database-style
    workloads on Arm Neoverse V2–based servers, such as AWS Graviton4. First, you'll build a compact
    bit vector in C and add baseline and improved scalar scanning routines. Then, you'll implement Neon
    and SVE vectorized versions to process data in wider chunks. You'll use a benchmarking harness
    that measures each approach so the relative behavior of scalar, Neon, and SVE implementations can
    be compared on an Arm-based Linux instance. By the end, you'll run a single C program
    that exercises all variants and produces timing results suitable for side-by-side evaluation.
  faqs:
  - question: Where should I place the code as I follow the steps?
    answer: >-
      Use a single source file named bitvector_scan_benchmark.c. Add the bit vector type, helper
      functions, scalar scan routines, Neon and SVE implementations, and the benchmarking code
      into this file as directed.
  - question: What must the bitmap data structure contain before I add the scan functions?
    answer: >-
      It includes a byte array that holds the bits, the physical size in bytes, and the logical
      size in bits. The same file also adds helpers to generate and analyze test bitmaps.
  - question: In what order should I implement and test the scanning approaches?
    answer: >-
      Start with the per-bit scalar baseline, then the optimized scalar version, followed by the
      Neon implementation, and finally SVE. After each addition, run the benchmark to compare
      against the previous versions.
  - question: What result should I expect from the benchmarking step?
    answer: >-
      The framework measures elapsed time for each scan function over a chosen number of iterations
      and tracks how many set-bit positions were found. Use the same input bitmap and iteration
      count when comparing implementations.
  - question: How can I exercise different workload characteristics when benchmarking?
    answer: >-
      Use the provided bitmap generation helpers to create datasets with varying densities. Sparse
      and dense bitmaps highlight different behaviors across the scalar, Neon, and SVE implementations.
# END generated_summary_faq

author: Pareena Verma

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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

