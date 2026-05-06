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

# rerun_summary: false
# rerun_faqs: false
# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-05-06T17:17:59Z'
  generator: template
  source_hash: eb008543ea4248b231be5e6345546164533edf2bc149613693095812bbbba3d9
  summary: >-
    Deploy Redis for data searching on Google Cloud C4A walks you through an end-to-end Arm software
    workflow. It is designed for developers deploying and optimizing Redis-based data searching
    workloads on Linux/Arm64 environments, specifically using Google Cloud C4A virtual machines
    powered by Axion processors. By the end, you will be able to provision an Arm-based SUSE SLES
    virtual machine on Google Cloud (C4A with Axion processors), install Redis on a SUSE Arm64
    (C4A) instance, and verify Redis functionality by running the server and performing baseline
    data insertion and retrieval tests on the Arm64 VM. It focuses on tools and technologies such
    as Redis and redis-benchmark, Linux environments, Arm platforms including Neoverse, and cloud
    platforms such as Google Cloud. The main steps cover Get started with Redis on Google Axion
    C4A, Create a Compute Engine instance, Install Redis, Test Redis, and Benchmark Redis.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will provision an Arm-based SUSE SLES virtual machine on Google Cloud (C4A with Axion
      processors), install Redis on a SUSE Arm64 (C4A) instance, and verify Redis functionality
      by running the server and performing baseline data insertion and retrieval tests on the
      Arm64 VM.
  - question: Who is this Learning Path for?
    answer: >-
      This is an introductory topic for developers deploying and optimizing Redis-based data searching
      workloads on Linux/Arm64 environments, specifically using Google Cloud C4A virtual machines
      powered by Axion processors.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: A [Google Cloud Platform (GCP)](https://cloud.google.com/free)
      account with billing enabled; Basic familiarity with [Redis](https://redis.io/).
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including Redis and redis-benchmark, Linux environments, Arm
      platforms such as Neoverse, and cloud platforms such as Google Cloud.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Get started with Redis on Google Axion C4A, Create
      a Compute Engine instance, Install Redis, Test Redis, and Benchmark Redis.
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

