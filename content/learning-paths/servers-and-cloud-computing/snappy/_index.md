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

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T02:06:13Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 62edadd9a4163e020b55d33f541a13ceb604c3700ba56787b650563c446a3b0d
  summary_generated_at: '2026-06-02T05:10:41Z'
  summary_source_hash: 62edadd9a4163e020b55d33f541a13ceb604c3700ba56787b650563c446a3b0d
  faq_generated_at: '2026-06-03T02:06:13Z'
  faq_source_hash: 62edadd9a4163e020b55d33f541a13ceb604c3700ba56787b650563c446a3b0d
  summary: >-
    This Learning Path guides you through installing and running lzbench with Snappy and Zstandard
    to measure compression library performance on Arm servers. It targets Linux and has been tested
    on AWS EC2 and Oracle OCI Arm-based instances running Ubuntu 20.04, with Snappy and Zstandard
    also supported on Amazon Linux 2, RHEL/CentOS 8, and Ubuntu 22.04/20.04/18.04. You will install
    required packages (gcc, g++, unzip, make), install lzbench, and run benchmarks to collect
    performance measurements on a 64-bit Arm instance. It is introductory and intended for developers
    using compression libraries on Arm Neoverse-based servers. The only explicit prerequisite
    is access to an Arm-based cloud instance, and it takes about 10 minutes to complete.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need access to an Arm-based instance from an appropriate cloud service provider. The
      steps have been tested on AWS EC2 and Oracle OCI Arm-based servers running Ubuntu 20.04.
  - question: Which Linux distributions are supported for Snappy and Zstandard in this path?
    answer: >-
      Amazon Linux 2, RHEL/CentOS 8, and Ubuntu 18.04, 20.04, and 22.04 are supported. The detailed
      steps were validated on Ubuntu 20.04.
  - question: Which packages should I install on the instance before building or running lzbench?
    answer: >-
      Install GNU gcc and g++ for your Arm Linux distribution, along with unzip and make. On Ubuntu,
      the packages are gcc, g++, unzip, and make.
  - question: Which compression libraries are benchmarked and how are they executed?
    answer: >-
      The path benchmarks Snappy and Zstandard using lzbench. You install lzbench and run it to
      measure these libraries on your Arm-based server.
  - question: What result should I expect after running the benchmarks?
    answer: >-
      You should obtain lzbench performance measurements for Snappy and Zstandard on your instance.
      Use these results to assess compression performance on a 64-bit Arm AWS EC2 environment.
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

