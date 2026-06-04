---
title: Deploy Redis for data searching on Google Cloud C4A 

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for developers deploying and optimizing Redis-based data searching workloads on Linux/Arm64 environments, specifically using Google Cloud C4A virtual machines powered by Axion processors.

learning_objectives:
  - Provision an Arm-based SUSE SLES virtual machine on Google Cloud (C4A with Axion processors)
  - Install Redis on a SUSE Arm64 (C4A) instance
  - Verify Redis functionality by running the server and performing baseline data insertion and retrieval tests on the Arm64 VM  
  - Measure Redis SET (write) and GET (read) performance using the official redis-benchmark tool to evaluate throughput and latency on Arm64 (AArch64)

prerequisites:
  - A [Google Cloud Platform (GCP)](https://cloud.google.com/free) account with billing enabled
  - Basic familiarity with [Redis](https://redis.io/) 

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T01:59:24Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: eb008543ea4248b231be5e6345546164533edf2bc149613693095812bbbba3d9
  summary_generated_at: '2026-06-02T04:58:42Z'
  summary_source_hash: eb008543ea4248b231be5e6345546164533edf2bc149613693095812bbbba3d9
  faq_generated_at: '2026-06-03T01:59:24Z'
  faq_source_hash: eb008543ea4248b231be5e6345546164533edf2bc149613693095812bbbba3d9
  summary: >-
    This Learning Path guides you through deploying Redis for data searching on Google Cloud C4A
    virtual machines powered by Axion processors (Arm Neoverse-V2 cores). You will provision a
    SUSE Linux (SLES) Arm64 instance in Compute Engine, build and install Redis from source with
    TLS support, verify the server using redis-cli, and run baseline data insertion and retrieval
    tests. You will then measure Redis SET and GET throughput and latency using the official redis-benchmark
    tool on Arm64. It is introductory in scope and intended for developers working with Redis-based
    data searching on Linux/Arm64. Prerequisites are a Google Cloud account with billing enabled
    and basic familiarity with Redis.
  faqs:
  - question: What do I need before running this Learning Path?
    answer: >-
      You need a Google Cloud Platform account with billing enabled and basic familiarity with
      Redis. No other explicit prerequisites are listed.
  - question: Which Google Cloud instance and OS should I use?
    answer: >-
      Use the C4A family with the c4a-standard-4 machine type (4 vCPUs, 16 GB memory). Provision
      a SUSE SLES Arm64 virtual machine from the Google Cloud Console.
  - question: How is Redis installed on the SUSE Arm64 VM?
    answer: >-
      You install build prerequisites using zypper, then download Redis 8.2.2 from the official
      GitHub repository and build from source. Building from source ensures compatibility on Arm
      and enables TLS support.
  - question: How do I start Redis and confirm it is running?
    answer: >-
      Start the server in the background with redis-server & and verify responsiveness with redis-cli
      ping, which should return PONG. The steps then insert and retrieve sample data to validate
      baseline functionality.
  - question: How do I benchmark Redis and what results should I look for?
    answer: >-
      Use the official redis-benchmark tool; the path demonstrates SET testing with redis-benchmark
      -t set -n 100000 -c 50 and also measures GET. Review requests per second and latency metrics
      reported by the tool.
# END generated_summary_faq

author: Pareena Verma

##### Tags
skilllevels: Introductory
subjects: Databases
cloud_service_providers:
  - Google Cloud

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

