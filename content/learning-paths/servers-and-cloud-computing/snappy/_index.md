---
title: Measure performance of compression libraries on Arm servers

minutes_to_complete: 10

who_is_this_for: This is an introductory topic for software developers using compression
  libraries on Arm servers.


learning_objectives:
- Install and run lzbench with snappy and zstd
- Measure compression library performance running on 64-bit Arm AWS EC2 instance

prerequisites:
- An [Arm based instance](/learning-paths/servers-and-cloud-computing/csp/) from an appropriate
  cloud service provider.

generate_summary_faq: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-04-30T18:58:19Z'
  generator: template
  source_hash: 62edadd9a4163e020b55d33f541a13ceb604c3700ba56787b650563c446a3b0d
  summary: >-
    Measure performance of compression libraries on Arm servers walks you through an end-to-end
    Arm software workflow. It is designed for software developers using compression libraries
    on Arm servers. By the end, you will be able to install and run lzbench with snappy and zstd
    and measure compression library performance running on 64-bit Arm AWS EC2 instance. It focuses
    on tools and technologies such as snappy and Runbook, Linux environments, Arm platforms including
    Neoverse, and cloud platforms such as AWS and Oracle. The main steps cover Install lzbench
    and measure algorithm performance.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will install and run lzbench with snappy and zstd and measure compression library performance
      running on 64-bit Arm AWS EC2 instance.
  - question: Who is this Learning Path for?
    answer: >-
      This is an introductory topic for software developers using compression libraries on Arm
      servers.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: An [Arm based instance](/learning-paths/servers-and-cloud-computing/csp/)
      from an appropriate cloud service provider.
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including snappy and Runbook, Linux environments, Arm platforms
      such as Neoverse, and cloud platforms such as AWS and Oracle.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Install lzbench and measure algorithm performance.
# END generated_summary_faq

author: Pareena Verma

test_images:
- ubuntu:latest
test_link: https://github.com/armflorentlebeau/arm-learning-paths/actions/runs/4312122327
test_maintenance: true

### Tags
skilllevels: Introductory
subjects: Libraries
cloud_service_providers:
  - AWS
  - Oracle
armips:
- Neoverse
operatingsystems:
- Linux
tools_software_languages:
- snappy
- Runbook

further_reading:
    - resource:
        title: Lzbench source
        link: https://github.com/inikep/lzbench
        type: documentation
    - resource:
        title: Comparing data compression algorithm performance on Arm servers
        link: https://developer.arm.com/community/arm-community-blogs/b/servers-and-cloud-computing-blog/posts/comparing-data-compression-algorithm-performance-on-aws-graviton2-342166113
        type: blog

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

