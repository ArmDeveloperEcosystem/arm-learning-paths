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

generate_summary_faq: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-04-30T18:58:17Z'
  generator: template
  source_hash: 1701b37580fe5d012a5e6fd322307742656a748dfb766fd48914011167386e95
  summary: >-
    Learn how to implement and benchmark bitmap scanning operations for database workloads using
    scalar, Neon, and SVE instructions on Arm-based cloud instances. It is designed for database
    developers, performance engineers, and anyone interested in optimizing data processing workloads
    on Arm-based cloud instances. By the end, you will be able to understand bitmap scanning operations
    in database systems, implement bitmap scanning with scalar, Neon, and SVE instructions, and
    compare performance between different implementations. It focuses on tools and technologies
    such as SVE, Neon, and Runbook, Linux environments, Arm platforms including Neoverse, and
    cloud platforms such as AWS, Microsoft Azure, Google Cloud, and Oracle. The main steps cover
    Optimize bitmap scanning in databases with SVE and Neon on Arm servers, Build and manage a
    bit vector in C, Implement scalar bitmap scanning in C, Vectorized bitmap scanning with Neon
    and SVE, and Benchmarking bitmap scanning across implementations.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will understand bitmap scanning operations in database systems, implement bitmap scanning
      with scalar, Neon, and SVE instructions, and compare performance between different implementations.
      Learn how to implement and benchmark bitmap scanning operations for database workloads using
      scalar, Neon, and SVE instructions on Arm-based cloud instances.
  - question: Who is this Learning Path for?
    answer: >-
      This is an introductory topic for database developers, performance engineers, and anyone
      interested in optimizing data processing workloads on Arm-based cloud instances.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: An [Arm based instance](/learning-paths/servers-and-cloud-computing/csp/)
      from an appropriate cloud service provider.
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including SVE, Neon, and Runbook, Linux environments, Arm
      platforms such as Neoverse, and cloud platforms such as AWS, Microsoft Azure, Google Cloud,
      and Oracle.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Optimize bitmap scanning in databases with SVE and
      Neon on Arm servers, Build and manage a bit vector in C, Implement scalar bitmap scanning
      in C, Vectorized bitmap scanning with Neon and SVE, and Benchmarking bitmap scanning across
      implementations.
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

