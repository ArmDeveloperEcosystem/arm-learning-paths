---
title: Deploy MongoDB on an Arm-based Google Axion C4A VM

minutes_to_complete: 15

who_is_this_for: This introductory topic is for software developers who want to migrate MongoDB workloads from x86_64 to Arm-based platforms, specifically on Google Axion-based C4A virtual machines.

description: Deploy MongoDB on Google Cloud Axion C4A virtual machines and benchmark database performance with Yahoo Cloud Serving Benchmark (YCSB).

learning_objectives:
  - Create an Arm virtual machine on Google Cloud (C4A Axion family)
  - Install and run MongoDB on the Arm-based C4A instance
  - Benchmark MongoDB performance with Yahoo Cloud Serving Benchmark (YCSB)

prerequisites:
     - A [Google Cloud Platform (GCP)](https://cloud.google.com/free?utm_source=google&hl=en) account with billing enabled

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T01:33:34Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: abbdde22271151fb1485c54bafe463e7797a0b913c7d4c99245d2914a3f9bb82
  summary_generated_at: '2026-06-02T04:28:40Z'
  summary_source_hash: abbdde22271151fb1485c54bafe463e7797a0b913c7d4c99245d2914a3f9bb82
  faq_generated_at: '2026-06-03T01:33:34Z'
  faq_source_hash: abbdde22271151fb1485c54bafe463e7797a0b913c7d4c99245d2914a3f9bb82
  summary: >-
    Learn how to deploy MongoDB on Arm-based Google Axion C4A virtual machines and benchmark it
    with the Yahoo Cloud Serving Benchmark (YCSB). You will create a c4a-standard-4 VM in Google
    Cloud using the Console, install MongoDB and mongosh on Red Hat Enterprise Linux with Arm64
    (aarch64) binaries for RHEL 9, and verify the server locally. Then you will build YCSB’s MongoDB
    binding from source (Maven/Java 11), load a starter dataset, and run workloads to capture
    a quick baseline and benchmark results. The C4A family uses Google’s Axion CPU based on Arm
    Neoverse‑V2 cores. Prerequisite: a Google Cloud Platform account with billing enabled.
  faqs:
  - question: What do I need before creating the VM on Google Cloud?
    answer: >-
      You need a Google Cloud Platform (GCP) account with billing enabled. All setup and deployment
      takes place in your GCP project.
  - question: Which VM configuration does this path use for Axion C4A?
    answer: >-
      The steps create an Arm-based C4A VM using the c4a-standard-4 machine type (4 vCPUs, 16
      GB memory). You create it in the Google Cloud Console under Compute Engine by selecting
      the C4A series.
  - question: Which operating system and MongoDB package are assumed?
    answer: >-
      The installation targets Red Hat Enterprise Linux on Arm. The steps fetch the Arm64 (aarch64)
      MongoDB binaries for RHEL 9.3.
  - question: How do I verify that MongoDB is running correctly?
    answer: >-
      Connect locally with mongosh using mongodb://127.0.0.1:27017. Create a test database and
      collection, perform basic CRUD operations, and record a quick insert-time baseline.
  - question: How do I install and run YCSB for MongoDB, and what data size is loaded initially?
    answer: >-
      Install git, Maven, and Java 11, clone the YCSB repository, and build the MongoDB binding
      with Maven. Use YCSB to load the starter dataset, which defaults to 1,000 records, and then
      run the workloads to benchmark MongoDB.
# END generated_summary_faq

author: Annie Tallund

##### Tags
skilllevels: Introductory
subjects: Databases
cloud_service_providers:
  - Google Cloud

armips:
    - Neoverse

tools_software_languages:
  - MongoDB
  - YCSB

operatingsystems:
    - Linux

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
further_reading:
    - resource:
        title: MongoDB Manual
        link: https://www.mongodb.com/docs/manual/
        type: documentation
    - resource:
        title: MongoDB Performance Tool
        link: https://github.com/idealo/mongodb-performance-test#readme
        type: documentation
    - resource:
        title: YCSB
        link: https://github.com/brianfrankcooper/YCSB/wiki/
        type: documentation


weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # Indicates this should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

