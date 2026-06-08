---
title: Deploy Apache Spark on Google Axion processors
   
minutes_to_complete: 60

who_is_this_for: This introductory topic is for software developers interested in migrating their Apache Spark workloads from x86_64 platforms to Arm-based platforms, specifically on Google Axion–based C4A virtual machines.  

learning_objectives:
  - Start an Arm virtual machine on Google Cloud Platform (GCP) using the C4A Google Axion instance family with RHEL 9 as the base image
  - Install and configure Apache Spark on Arm-based GCP C4A instances
  - Validate Spark functionality through baseline testing
  - Benchmark Apache Spark performance on Arm

prerequisites:
  - A [Google Cloud Platform (GCP)](https://cloud.google.com/free?utm_source=google&hl=en) account with billing enabled
  - Familiarity with distributed computing concepts and the [Apache Spark architecture](https://spark.apache.org/docs/latest/)

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T02:07:54Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: a4ac73af7e8959a546a66ab776c0bca8b60957e6f1729aa00fd78783e6594c0b
  summary_generated_at: '2026-06-02T05:13:16Z'
  summary_source_hash: a4ac73af7e8959a546a66ab776c0bca8b60957e6f1729aa00fd78783e6594c0b
  faq_generated_at: '2026-06-03T02:07:54Z'
  faq_source_hash: a4ac73af7e8959a546a66ab776c0bca8b60957e6f1729aa00fd78783e6594c0b
  summary: >-
    Learn how to deploy Apache Spark on Arm-based Google Axion C4A virtual machines in Google
    Cloud. You will provision a c4a-standard-4 instance with RHEL 9, install Java, Scala, Maven,
    and Spark, then validate the setup by running a simple Scala Spark job. The path concludes
    with running Spark’s built-in SQL micro-benchmarks using the SBT-based framework to produce
    results you can use to compare Arm64 C4A performance with x86_64 platforms. This path targets
    developers evaluating migration of Spark workloads to Arm Neoverse-V2–based systems. Prerequisites
    include a GCP account with billing enabled and familiarity with distributed computing and
    the Apache Spark architecture.
  faqs:
  - question: What do I need before creating the VM?
    answer: >-
      You need a Google Cloud Platform account with billing enabled. Familiarity with distributed
      computing concepts and the Apache Spark architecture is expected.
  - question: Which VM configuration and OS image should I use on GCP?
    answer: >-
      Use a Google Axion C4A Arm VM with the c4a-standard-4 machine type (4 vCPUs, 16 GB memory).
      The Learning Path uses Red Hat Enterprise Linux 9 as the base image.
  - question: How do I access the instance to install Spark and its dependencies?
    answer: >-
      SSH into the C4A VM you created in the Google Cloud Console. From there, install Java, Scala,
      Maven, and Apache Spark on the RHEL 9 system.
  - question: How do I confirm that my Spark installation works on the C4A VM?
    answer: >-
      Create and run a simple Scala Spark job that parallelizes a small dataset and performs a
      basic transformation and action. Successful execution with the expected output indicates
      the installation is correct.
  - question: How are the performance benchmarks run and what do they measure?
    answer: >-
      Clone the Apache Spark source and use the SBT-based framework to run the built-in SQL micro-benchmarks.
      These cover areas such as SQL execution, aggregations, joins, and data source reads and
      can be used to compare Arm64 results with x86_64 runs.
# END generated_summary_faq

author: Pareena Verma

##### Tags
skilllevels: Advanced
subjects: Performance and Architecture
cloud_service_providers:
  - Google Cloud

armips:
  - Neoverse

tools_software_languages:
  - Apache Spark
  - Python

operatingsystems:
  - Linux

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
further_reading:
  - resource:
      title: Google Cloud official documentation
      link: https://cloud.google.com/docs
      type: documentation

  - resource:
      title: Apache Spark documentation
      link: https://spark.apache.org/
      type: documentation

  - resource:
      title: Scala programming language official website
      link: https://scala-lang.org
      type: website

weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # Indicates this should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

