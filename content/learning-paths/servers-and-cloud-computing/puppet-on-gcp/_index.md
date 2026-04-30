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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-04-30T18:58:19Z'
  generator: template
  source_hash: aeb6a390b5134af2f851e36db17c5d3578d4697b3c372af86c6bd5176765e087
  summary: >-
    Deploy Puppet on Google Cloud C4A walks you through an end-to-end Arm software workflow. It
    is designed for developers deploying and optimizing Puppet workloads on Arm Linux environments,
    specifically using Google Cloud C4A virtual machines powered by Axion processors. By the end,
    you will be able to provision an Arm-based SUSE SLES (SUSE Linux Enterprise Server) virtual
    machine (VM) on Google Cloud C4A with Axion processors, install Puppet on a SUSE Arm64 C4A
    instance, and verify Puppet by applying a test manifest and confirming successful resource
    creation on Arm64. It focuses on tools and technologies such as Puppet, Ruby, Facter, and
    Hiera, Linux environments, Arm platforms including Neoverse, and cloud platforms such as Google
    Cloud. The main steps cover Get started with Arm-based Google Axion and Puppet, Create a Google
    Axion C4A Arm virtual machine on GCP, Install Puppet on a GCP VM, Perform Puppet baseline
    testing, and Benchmark Puppet.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will provision an Arm-based SUSE SLES (SUSE Linux Enterprise Server) virtual machine
      (VM) on Google Cloud C4A with Axion processors, install Puppet on a SUSE Arm64 C4A instance,
      and verify Puppet by applying a test manifest and confirming successful resource creation
      on Arm64.
  - question: Who is this Learning Path for?
    answer: >-
      This is an introductory topic for developers deploying and optimizing Puppet workloads on
      Arm Linux environments, specifically using Google Cloud C4A virtual machines powered by
      Axion processors.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: A [Google Cloud Platform (GCP)](https://cloud.google.com/free)
      account with billing enabled; Basic familiarity with [Puppet](https://www.puppet.com/).
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including Puppet, Ruby, Facter, and Hiera, Linux environments,
      Arm platforms such as Neoverse, and cloud platforms such as Google Cloud.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Get started with Arm-based Google Axion and Puppet,
      Create a Google Axion C4A Arm virtual machine on GCP, Install Puppet on a GCP VM, Perform
      Puppet baseline testing, and Benchmark Puppet.
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

