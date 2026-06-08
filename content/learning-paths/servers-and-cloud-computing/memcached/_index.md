---
title: Run memcached on Arm servers and measure its performance

minutes_to_complete: 10

who_is_this_for: This is an introductory topic for developers who want to use memcached as their in-memory key-value store.

description: Install memcached on Arm cloud servers and benchmark in-memory key-value store performance using open-source tools.

learning_objectives:
- Install and run memcached on your Arm-based cloud server
- Use an open-source benchmark to test memcached performance

prerequisites:
- An Arm based instance from an appropriate cloud service provider.

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T01:26:50Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: b42ca5cc8f4db6ba6019f3720a5ef46119aa403a2baaef5362e874f898ce0419
  summary_generated_at: '2026-06-02T04:20:04Z'
  summary_source_hash: b42ca5cc8f4db6ba6019f3720a5ef46119aa403a2baaef5362e874f898ce0419
  faq_generated_at: '2026-06-03T01:26:50Z'
  faq_source_hash: b42ca5cc8f4db6ba6019f3720a5ef46119aa403a2baaef5362e874f898ce0419
  summary: >-
    This introductory Learning Path shows how to install and run Memcached on an Arm-based Ubuntu
    Linux cloud instance and measure its performance with the open-source memtier_benchmark tool.
    You will provision an Arm server (tested on AWS and Oracle Cloud), install gcc and required
    development libraries such as libevent, and set up the packages needed to build and run the
    benchmark. By the end, you will have Memcached running and will execute a benchmark workload
    to generate performance results for your environment. Prerequisite: access to an Arm-based
    instance from a cloud service provider; no other explicit prerequisites are listed.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need access to an Arm-based instance from a cloud service provider running Ubuntu Linux.
      Install gcc on the instance by following the GNU compiler install guide.
  - question: Which cloud platforms are referenced in this Learning Path?
    answer: >-
      The steps have been tested on AWS and Oracle Cloud. Any appropriate Arm-based cloud instance
      running Ubuntu Linux is suitable.
  - question: Which packages should I install to prepare for memcached and the benchmark?
    answer: >-
      Install libevent-dev for memcached. For memtier_benchmark, install build-essential, autoconf,
      automake, libpcre3-dev, libevent-dev, pkg-config, zlib1g-dev, libssl-dev, wget, and git.
  - question: Which benchmark tool is used to measure memcached performance?
    answer: >-
      The path uses the open-source memtier_benchmark. You install its required build and runtime
      dependencies and then run it against your memcached service.
  - question: How do I know the setup worked?
    answer: >-
      After starting memcached, run memtier_benchmark; a successful connection and benchmark output
      indicate the service is running and being exercised. The benchmark will report performance
      metrics you can review.
# END generated_summary_faq

author: Pareena Verma

test_images:
- ubuntu:latest
test_link: https://github.com/armflorentlebeau/arm-learning-paths/actions/runs/4312122327
test_maintenance: true

### Tags
skilllevels: Introductory
subjects: Web
cloud_service_providers:
  - AWS
  - Oracle
armips:
- Neoverse
operatingsystems:
- Linux
tools_software_languages:
- Runbook
- Memcached

further_reading:
    - resource:
        title: Memcached Wiki
        link: https://github.com/memcached/memcached/wiki
        type: documentation
    - resource:
        title: Benchmarking memcached performance on AWS Graviton2 servers
        link: https://developer.arm.com/community/arm-community-blogs/b/servers-and-cloud-computing-blog/posts/accelerating-deep-packet-inspection-with-neon-on-arm-neoverse
        type: blog


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

