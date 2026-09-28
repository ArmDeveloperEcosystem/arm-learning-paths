---
title: Run Memcached on Arm servers and measure its performance

minutes_to_complete: 10

who_is_this_for: This is an introductory topic for developers who want to use memcached as their in-memory key-value store.

description: Install memcached on Arm cloud servers and benchmark in-memory key-value store performance using open-source tools.

learning_objectives:
- Install and run memcached on your Arm-based cloud server
- Use an open-source benchmark to test memcached performance

prerequisites:
- An Arm based instance from an appropriate cloud service provider.

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-09-28T19:46:55Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 5320f539f2948752ccb1596fe7c3a8319cc0cb7097ecf2cd698c3e1ca903aaf0
  summary_generated_at: '2026-09-28T19:46:55Z'
  summary_source_hash: 5320f539f2948752ccb1596fe7c3a8319cc0cb7097ecf2cd698c3e1ca903aaf0
  faq_generated_at: '2026-09-28T19:46:55Z'
  faq_source_hash: 5320f539f2948752ccb1596fe7c3a8319cc0cb7097ecf2cd698c3e1ca903aaf0
  summary: >-
    You'll deploy and benchmark Memcached on an Arm-based cloud server. First, you'll provision an Ubuntu instance
    on AWS Graviton or OCI Ampere Compute, then install `libevent`, build tools, and the Memcached
    service. You'll prepare `memtier_benchmark`, verify that the service is available, and run a
    workload to generate performance results. The completed setup gives you a repeatable baseline
    for testing Memcached on Arm infrastructure.
  faqs:
  - question: Which Linux distribution should I use on the cloud instance?
    answer: >-
      Use Ubuntu Linux because the package installation commands use `apt`.
  - question: Do I need a specific cloud provider or instance type?
    answer: >-
      Use an Arm-based Amazon EC2 or OCI Ampere Compute instance.
  - question: Which packages must be installed before running the benchmark tool?
    answer: >-
      Install `libevent` and the packages required by `memtier_benchmark`.
  - question: How do I know if I’m ready to run the benchmark against Memcached?
    answer: >-
      Confirm that Memcached is running on your Ubuntu instance and that the packages required
      by `memtier_benchmark` installed without errors.
  - question: Can I install Memcached without building it from source?
    answer: >-
      Yes. Run `sudo apt install memcached -y`, then start the service with `sudo systemctl start
      memcached`. 
# END generated_summary_faq

author: Pareena Verma

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

test_images:
- ubuntu:latest
test_link: https://github.com/armflorentlebeau/arm-learning-paths/actions/runs/4312122327
test_maintenance: true

### Tags
skilllevels: Introductory
subjects: Web
platforms:
  - AWS Graviton
  - Oracle Cloud Infrastructure (OCI) Ampere Compute
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
