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
  template_version: summary-faq-v1
  generated_at: '2026-05-06T17:17:58Z'
  generator: template
  source_hash: abbdde22271151fb1485c54bafe463e7797a0b913c7d4c99245d2914a3f9bb82
  summary: >-
    Deploy MongoDB on Google Cloud Axion C4A virtual machines and benchmark database performance
    with Yahoo Cloud Serving Benchmark (YCSB). It is designed for This introductory topic is for
    software developers who want to migrate MongoDB workloads from x86_64 to Arm-based platforms,
    specifically on Google Axion-based C4A virtual machines. By the end, you will be able to create
    an Arm virtual machine on Google Cloud (C4A Axion family), install and run MongoDB on the
    Arm-based C4A instance, and benchmark MongoDB performance with Yahoo Cloud Serving Benchmark
    (YCSB). It focuses on tools and technologies such as MongoDB and YCSB, Linux environments,
    Arm platforms including Neoverse, and cloud platforms such as Google Cloud. The main steps
    cover About Google Axion C4A series and MongoDB, Create Google Axion instance, Install MongoDB,
    Baseline Testing, and MongoDB Benchmarking.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will create an Arm virtual machine on Google Cloud (C4A Axion family), install and run
      MongoDB on the Arm-based C4A instance, and benchmark MongoDB performance with Yahoo Cloud
      Serving Benchmark (YCSB). Deploy MongoDB on Google Cloud Axion C4A virtual machines and
      benchmark database performance with Yahoo Cloud Serving Benchmark (YCSB).
  - question: Who is this Learning Path for?
    answer: >-
      This introductory topic is for software developers who want to migrate MongoDB workloads
      from x86_64 to Arm-based platforms, specifically on Google Axion-based C4A virtual machines.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: A [Google Cloud Platform (GCP)](https://cloud.google.com/free?utm_source=google&hl=en)
      account with billing enabled.
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including MongoDB and YCSB, Linux environments, Arm platforms
      such as Neoverse, and cloud platforms such as Google Cloud.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around About Google Axion C4A series and MongoDB, Create
      Google Axion instance, Install MongoDB, Baseline Testing, and MongoDB Benchmarking.
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

