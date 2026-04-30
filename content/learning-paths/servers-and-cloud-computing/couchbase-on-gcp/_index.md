---
title: Deploy Couchbase on Google Cloud C4A
description: Learn how to install and configure Couchbase on Google Cloud Axion C4A Arm64 instances and benchmark read/write performance using YCSB workloads.

    
minutes_to_complete: 30

who_is_this_for: This is an introductory topic for developers deploying Couchbase workloads on Arm Linux environments, specifically using Google Cloud C4A virtual machines (VM) powered by Axion processors. 

learning_objectives:
  - Provision an Arm-based SUSE Linux Enterprise Server (SLES) virtual machine on Google Cloud (C4A with Axion processors)
  - Install Couchbase Server on the SUSE Arm64 (C4A) instance
  - Verify Couchbase deployment by accessing the web console, creating a test bucket, and confirming cluster health 
  - Benchmark Couchbase by measuring operations per second (ops/sec), memory utilization, and disk performance on the Arm platform

prerequisites:
  - A [Google Cloud Platform (GCP)](https://cloud.google.com/free) account with billing enabled  
  - Basic familiarity with [Couchbase](https://www.couchbase.com/)

generate_summary_faq: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-04-30T18:58:17Z'
  generator: template
  source_hash: 0a7d76b8c944a50073c7524813acf83948155c7c61d9c92f9202eae1192c9600
  summary: >-
    Learn how to install and configure Couchbase on Google Cloud Axion C4A Arm64 instances and
    benchmark read/write performance using YCSB workloads. It is designed for developers deploying
    Couchbase workloads on Arm Linux environments, specifically using Google Cloud C4A virtual
    machines (VM) powered by Axion processors. By the end, you will be able to provision an Arm-based
    SUSE Linux Enterprise Server (SLES) virtual machine on Google Cloud (C4A with Axion processors),
    install Couchbase Server on the SUSE Arm64 (C4A) instance, and verify Couchbase deployment
    by accessing the web console, creating a test bucket, and confirming cluster health. It focuses
    on tools and technologies such as Couchbase, Linux environments, Arm platforms including Neoverse,
    and cloud platforms such as Google Cloud. The main steps cover Get started with Couchbase
    on Google Axion C4A, Create a firewall rule on GCP, Create a Google Axion C4A Arm virtual
    machine on GCP, Install Couchbase, and Perform Couchbase baseline testing.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will provision an Arm-based SUSE Linux Enterprise Server (SLES) virtual machine on Google
      Cloud (C4A with Axion processors), install Couchbase Server on the SUSE Arm64 (C4A) instance,
      and verify Couchbase deployment by accessing the web console, creating a test bucket, and
      confirming cluster health. Learn how to install and configure Couchbase on Google Cloud
      Axion C4A Arm64 instances and benchmark read/write performance using YCSB workloads.
  - question: Who is this Learning Path for?
    answer: >-
      This is an introductory topic for developers deploying Couchbase workloads on Arm Linux
      environments, specifically using Google Cloud C4A virtual machines (VM) powered by Axion
      processors.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: A [Google Cloud Platform (GCP)](https://cloud.google.com/free)
      account with billing enabled; Basic familiarity with [Couchbase](https://www.couchbase.com/).
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including Couchbase, Linux environments, Arm platforms such
      as Neoverse, and cloud platforms such as Google Cloud.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Get started with Couchbase on Google Axion C4A, Create
      a firewall rule on GCP, Create a Google Axion C4A Arm virtual machine on GCP, Install Couchbase,
      and Perform Couchbase baseline testing.
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
  - Couchbase

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
      title: Couchbase documentation
      link: https://docs.couchbase.com/home/index.html
      type: documentation

weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---

