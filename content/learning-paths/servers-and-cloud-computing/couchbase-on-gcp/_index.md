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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-27T18:44:09Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 0a7d76b8c944a50073c7524813acf83948155c7c61d9c92f9202eae1192c9600
  summary_generated_at: '2026-07-27T18:44:09Z'
  summary_source_hash: 0a7d76b8c944a50073c7524813acf83948155c7c61d9c92f9202eae1192c9600
  faq_generated_at: '2026-07-27T18:44:09Z'
  faq_source_hash: 0a7d76b8c944a50073c7524813acf83948155c7c61d9c92f9202eae1192c9600
  summary: >-
    You'll deploy Couchbase Server on an Arm-based Google Cloud C4A virtual machine and validate the
    setup for benchmarking. You'll provision a C4A instance, expose the Couchbase Web Console with a
    firewall rule, install Couchbase on a SUSE-based Arm64 VM, initialize the cluster, and create a
    test bucket. By the end, you'll confirm the node is healthy and the bucket is ready for read and write
    benchmarking with external tools.
  faqs:
  - question: What result should I expect when I open `http://<VM_IP>:8091`?
    answer: >-
      You should see the Couchbase Web Console for initial setup or login. After completing the
      setup, the **Servers** page should show your node as healthy and your test bucket should appear
      in the Buckets view.
  - question: I can’t reach the Couchbase Web Console on port 8091 — what should I check?
    answer: >-
      Create a GCP firewall rule that allows TCP port `8091` and applies to your instance. Confirm
      that the VM is running, note its external IP, and try again.
  - question: Which package manager should I use to follow the installation steps?
    answer: >-
      The steps use zypper for SUSE-based systems. Follow the commands as shown to refresh repositories,
      update the system, and install required tools before adding Couchbase.
  - question: How do I know the environment is ready for benchmarking?
    answer: >-
      Confirm that the web console responds on port `8091`, cluster initialization is complete, the
      node shows healthy status, and a test bucket exists. These checks indicate that the deployment
      is ready for workload testing.
  - question: When should I run YCSB workloads against Couchbase?
    answer: >-
      Run YCSB after you verify console access, complete cluster setup, and create a bucket. The
      specific YCSB commands aren't listed here, so use your verified bucket name and credentials
      when you proceed.
# END generated_summary_faq

author: Pareena Verma

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

##### Tags
skilllevels: Introductory
subjects: Databases
platforms:
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
