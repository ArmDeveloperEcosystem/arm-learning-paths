---
title: Deploy Puppet on Google Cloud C4A 

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for developers deploying and optimizing Puppet workloads on Arm Linux environments, specifically using Google Cloud C4A virtual machines powered by Axion processors. 

learning_objectives:
  - Provision an Arm-based SUSE SLES (SUSE Linux Enterprise Server) virtual machine (VM) on Google Cloud C4A with Axion processors
  - Install Puppet on a SUSE Arm64 C4A instance
  - Verify Puppet by applying a test manifest and confirming successful resource creation on Arm64  
  - Benchmark Puppet by measuring catalog compile time, apply speed, and resource usage on Arm64

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T01:54:50Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: aeb6a390b5134af2f851e36db17c5d3578d4697b3c372af86c6bd5176765e087
  summary_generated_at: '2026-06-02T04:51:08Z'
  summary_source_hash: aeb6a390b5134af2f851e36db17c5d3578d4697b3c372af86c6bd5176765e087
  faq_generated_at: '2026-06-03T01:54:50Z'
  faq_source_hash: aeb6a390b5134af2f851e36db17c5d3578d4697b3c372af86c6bd5176765e087
  summary: >-
    Learn how to deploy and validate Puppet on Arm-based Google Cloud C4A virtual machines powered
    by Axion processors. You will provision a SUSE Linux Arm64 VM (c4a-standard-4), install Puppet
    by setting up dependencies and building Ruby 3.1.4 from source, then verify the installation
    by checking Puppet and Facter versions, applying a simple manifest, and confirming system
    facts collection. The path concludes with a standalone benchmark of Puppet on Arm64 to measure
    catalog compile time, apply speed, and resource usage—without a Puppet Master. Prerequisites
    include a GCP account with billing enabled and basic familiarity with Puppet. Expected duration
    is about 30 minutes.
  faqs:
  - question: What do I need before provisioning the VM?
    answer: >-
      You need a Google Cloud Platform account with billing enabled and basic familiarity with
      Puppet. No other prerequisites are explicitly listed.
  - question: Which Google Cloud machine type and OS should I select?
    answer: >-
      Use the c4a-standard-4 machine type (4 vCPUs, 16 GB memory) and a SUSE Linux Arm64 (SUSE
      Linux Enterprise Server) image. The VM is created from the Google Cloud Console under Compute
      Engine.
  - question: Do I need to build Ruby, and which version is used?
    answer: >-
      Yes. You will install required development tools and libraries, then build Ruby 3.1.4 from
      source to prepare the environment for Puppet and avoid compatibility issues.
  - question: How do I verify that Puppet installed correctly?
    answer: >-
      Run a version check such as puppet --version (the example output shown is 8.10.0), then
      run basic Puppet commands. Apply a simple manifest and confirm that resources are created
      and Facter reports system facts.
  - question: Does the benchmark require a Puppet Master, and what does it measure?
    answer: >-
      No. The benchmark runs standalone on the SUSE Arm64 VM and measures local execution, including
      catalog compile time, apply speed, and resource usage on Arm64.
# END generated_summary_faq

author: Pareena Verma

prerequisites:
  - A [Google Cloud Platform (GCP)](https://cloud.google.com/free) account with billing enabled  
  - Basic familiarity with [Puppet](https://www.puppet.com/)

##### Tags
skilllevels: Introductory
subjects: Performance and Architecture
cloud_service_providers:
  - Google Cloud

armips:
  - Neoverse

tools_software_languages:
  - Puppet
  - Ruby
  - Facter
  - Hiera

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
      title: Puppet documentation
      link: https://www.puppet.com/docs/index.html
      type: documentation

weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---

