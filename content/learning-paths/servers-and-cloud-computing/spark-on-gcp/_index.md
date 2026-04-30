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

generate_summary_faq: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-04-30T18:58:19Z'
  generator: template
  source_hash: a4ac73af7e8959a546a66ab776c0bca8b60957e6f1729aa00fd78783e6594c0b
  summary: >-
    Deploy Apache Spark on Google Axion processors walks you through an end-to-end Arm software
    workflow. It is designed for This introductory topic is for software developers interested
    in migrating their Apache Spark workloads from x86_64 platforms to Arm-based platforms, specifically
    on Google Axion–based C4A virtual machines. By the end, you will be able to start an Arm virtual
    machine on Google Cloud Platform (GCP) using the C4A Google Axion instance family with RHEL
    9 as the base image, install and configure Apache Spark on Arm-based GCP C4A instances, and
    validate Spark functionality through baseline testing. It focuses on tools and technologies
    such as Apache Spark and Python, Linux environments, Arm platforms including Neoverse, and
    cloud platforms such as Google Cloud. The main steps cover Getting started with Apache Spark
    on Google Axion C4A (Arm Neoverse-V2), How to create a Google Axion C4A Arm virtual machine
    on GCP, How to deploy Apache Spark on Google Axion C4A Arm virtual machines, Apache Spark
    baseline testing on Google Axion C4A Arm VM, and Apache Spark performance benchmarks on Arm64
    and x86_64 in Google Cloud.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will start an Arm virtual machine on Google Cloud Platform (GCP) using the C4A Google
      Axion instance family with RHEL 9 as the base image, install and configure Apache Spark
      on Arm-based GCP C4A instances, and validate Spark functionality through baseline testing.
  - question: Who is this Learning Path for?
    answer: >-
      This introductory topic is for software developers interested in migrating their Apache
      Spark workloads from x86_64 platforms to Arm-based platforms, specifically on Google Axion–based
      C4A virtual machines.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: A [Google Cloud Platform (GCP)](https://cloud.google.com/free?utm_source=google&hl=en)
      account with billing enabled; Familiarity with distributed computing concepts and the [Apache
      Spark architecture](https://spark.apache.org/docs/latest/).
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including Apache Spark and Python, Linux environments, Arm
      platforms such as Neoverse, and cloud platforms such as Google Cloud.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Getting started with Apache Spark on Google Axion
      C4A (Arm Neoverse-V2), How to create a Google Axion C4A Arm virtual machine on GCP, How
      to deploy Apache Spark on Google Axion C4A Arm virtual machines, Apache Spark baseline testing
      on Google Axion C4A Arm VM, and Apache Spark performance benchmarks on Arm64 and x86_64
      in Google Cloud.
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

