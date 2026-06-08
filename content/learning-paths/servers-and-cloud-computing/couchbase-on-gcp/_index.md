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

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T00:36:56Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 0a7d76b8c944a50073c7524813acf83948155c7c61d9c92f9202eae1192c9600
  summary_generated_at: '2026-06-02T03:28:12Z'
  summary_source_hash: 0a7d76b8c944a50073c7524813acf83948155c7c61d9c92f9202eae1192c9600
  faq_generated_at: '2026-06-03T00:36:56Z'
  faq_source_hash: 0a7d76b8c944a50073c7524813acf83948155c7c61d9c92f9202eae1192c9600
  summary: >-
    Follow this introductory path to deploy Couchbase Server on Arm-based Google Cloud Axion C4A
    virtual machines and run basic performance checks. You will provision a SUSE Linux Enterprise
    Server (SLES) VM on the c4a-standard-4 machine type, create a Google Cloud firewall rule to
    open TCP port 8091, install Couchbase on Arm64, and initialize the cluster from the web console
    by creating a test bucket and confirming node health. You then benchmark Couchbase using YCSB
    workloads to record operations per second, memory utilization, and disk behavior on the Arm
    platform. Prerequisites are a GCP account with billing enabled and basic familiarity with
    Couchbase.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need a Google Cloud Platform account with billing enabled and basic familiarity with
      Couchbase. No additional prerequisites are explicitly listed.
  - question: Which Google Cloud VM type and OS should I use?
    answer: >-
      Provision an Arm-based Google Axion C4A VM using the c4a-standard-4 machine type (4 vCPUs,
      16 GB memory). The Learning Path targets SUSE Linux Enterprise Server (Arm64).
  - question: How do I allow and test access to the Couchbase Web Console?
    answer: >-
      Create a VPC firewall rule in Google Cloud Console to allow inbound TCP port 8091. Then
      open http://VM_PUBLIC_IP:8091 in your browser to reach the console.
  - question: How do I know Couchbase installed correctly on the VM?
    answer: >-
      You should be able to access the Couchbase Web Console, complete the initial cluster setup,
      see your node reported as healthy, and create a test bucket. These checks confirm the deployment
      is ready for benchmarking.
  - question: What should I capture when running the YCSB benchmarks?
    answer: >-
      Measure and record operations per second (ops/sec), memory utilization, and disk performance
      for the Couchbase workload on the Arm-based instance. The Learning Path guides you to prepare
      the bucket and run YCSB workloads to collect these results.
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

