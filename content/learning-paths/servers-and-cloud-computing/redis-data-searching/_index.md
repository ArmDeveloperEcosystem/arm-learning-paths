---
title: Deploy Redis for data searching on Google Cloud C4A 

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for developers deploying and optimizing Redis-based data searching workloads on Linux/Arm64 environments, specifically using Google Cloud C4A virtual machines (VMs) powered by Axion processors.

learning_objectives:
  - Provision an Arm-based SUSE SLES C4A virtual machine on Google Cloud.
  - Install Redis on a SUSE Arm64 instance.
  - Verify Redis functionality by running the server and performing baseline data insertion and retrieval tests on the Arm64 VM. 
  - Measure Redis SET (write) and GET (read) performance using the official redis-benchmark tool to evaluate throughput and latency on Arm64 (AArch64).

prerequisites:
  - A [Google Cloud Platform (GCP)](https://cloud.google.com/free) account with billing enabled
  - Basic familiarity with [Redis](https://redis.io/)

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-11-19T16:03:54Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 3932c64a3ffa2252da47514025674e19c9f77e6543acb992654d62828e7fe8fd
  summary_generated_at: '2026-11-19T16:03:54Z'
  summary_source_hash: 3932c64a3ffa2252da47514025674e19c9f77e6543acb992654d62828e7fe8fd
  faq_generated_at: '2026-11-19T16:03:54Z'
  faq_source_hash: 3932c64a3ffa2252da47514025674e19c9f77e6543acb992654d62828e7fe8fd
  summary: >-
    You'll install Redis on a Google Axion C4A VM and test data search on SUSE Linux. First, you'll
    provision a `c4a-standard-4` instance, build Redis from source, and verify the server with
    `redis-cli ping`. You'll then insert sample data, retrieve keys, and compare pattern searches
    with `SCAN`. Finally, you'll run SET and GET benchmarks to inspect request rates and latency
    on Arm.
  faqs:
  - question: What virtual machine type and image should I use?
    answer: >-
      Select `c4a-standard-4` and a SUSE arm64 image. 
  - question: What do I install before building Redis?
    answer: >-
      Use `zypper` to install `gcc`, `gcc-c++`, and `make`, as well as `tcl`, `openssl-devel`, and `wget`
      after refreshing repositories.
  - question: Which Redis version do I build?
    answer: >-
      Download and build Redis `8.2.2` from its official GitHub source archive.
  - question: How do I check that Redis is running?
    answer: >-
      Start Redis with `redis-server &`, then run `redis-cli ping`. You should receive `PONG`.
  - question: How do I compare write and read performance?
    answer: >-
      Run `redis-benchmark -t set -n 100000 -c 50` for SET and `redis-benchmark -t get -n
      100000 -c 50` for GET. You can compare their throughput and latency output.
# END generated_summary_faq

author: Pareena Verma

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

##### Tags
skilllevels: Introductory
subjects: Databases
platforms:
  - Google Axion

armips:
  - Neoverse

tools_software_languages:
  - Redis
  - redis-benchmark

operatingsystems:
  - Linux

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
further_reading:
  - resource:
      title: Google Cloud documentation
      link: https://cloud.google.com/docs
      type: documentation

  - resource:
      title: Redis documentation
      link: https://redis.io/docs/
      type: documentation

  - resource:
      title: Redis benchmark documentation
      link: https://redis.io/docs/latest/operate/oss_and_stack/management/optimization/benchmarks/
      type: documentation

weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---

