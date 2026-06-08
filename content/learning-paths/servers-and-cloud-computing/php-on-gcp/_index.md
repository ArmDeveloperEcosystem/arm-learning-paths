---
title:  Deploy PHP on Google Cloud C4A Arm-based Axion VMs

  
minutes_to_complete: 30

who_is_this_for: This is an introductory topic for developers migrating Hypertext Preprocessor (PHP) workloads from x86_64 to Arm-based servers, specifically on Google Cloud C4A virtual machines (VM) built on Axion processors.

learning_objectives:
  - Provision a SUSE Linux Enterprise Server (SLES) virtual machine on a Google Cloud C4A Arm-based Axion virtual machine
  - Install PHP on a SUSE Arm64 C4A instance
  - Validate PHP functionality by running baseline HTTP server tests  
  - Benchmark PHP performance using PHPBench on Arm64 architecture 


prerequisites:
  - A [Google Cloud Platform (GCP)](https://cloud.google.com/free) account with billing enabled
  - Basic familiarity with web servers and PHP scripting

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T01:48:24Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 719ec8966a776cc5ee97782b7ef7cc2b989a8616d14cb36b9847c9cbd2f16446
  summary_generated_at: '2026-06-02T04:47:26Z'
  summary_source_hash: 719ec8966a776cc5ee97782b7ef7cc2b989a8616d14cb36b9847c9cbd2f16446
  faq_generated_at: '2026-06-03T01:48:24Z'
  faq_source_hash: 719ec8966a776cc5ee97782b7ef7cc2b989a8616d14cb36b9847c9cbd2f16446
  summary: >-
    Follow this introductory path to deploy and validate a PHP stack on Arm-based Google Cloud
    C4A virtual machines built on Axion processors. You will provision a SUSE Linux Enterprise
    Server instance (c4a-standard-4), install PHP, Apache, and common PHP extensions, and configure
    PHP-FPM. The path guides you through running baseline HTTP server tests to confirm the setup
    and benchmarking PHP performance with PHPBench on Arm64. It is intended for developers migrating
    PHP workloads from x86_64 to Arm on Google Cloud. Prerequisites include a Google Cloud Platform
    account with billing enabled and basic familiarity with web servers and PHP scripting.
  faqs:
  - question: What do I need before provisioning the instance on Google Cloud?
    answer: >-
      You need a Google Cloud Platform account with billing enabled and basic familiarity with
      web servers and PHP scripting. The path references a separate Learning Path for general
      GCP setup support.
  - question: Which Google Cloud VM configuration does this path use?
    answer: >-
      You will create a Google Cloud C4A Arm-based Axion VM using the c4a-standard-4 machine type
      (four vCPUs, 16 GB memory). Provisioning is performed in the Google Cloud Console.
  - question: Which operating system and architecture are targeted?
    answer: >-
      The path uses SUSE Linux Enterprise Server on an Arm64 Google Cloud C4A instance. Steps
      refer to installing and configuring software on a SUSE Arm-based virtual machine.
  - question: How do I install the PHP stack on the SUSE instance?
    answer: >-
      Update the system with zypper and then install PHP, PHP-FPM, Apache, and commonly used PHP
      extensions. The steps use zypper refresh, zypper update, and zypper install to add the required
      packages.
  - question: How do I validate the setup and what should I look for in benchmarks?
    answer: >-
      Configure a PHP-FPM pool, connect it to Apache, and run baseline HTTP server tests to verify
      FastCGI and dynamic PHP are working. For benchmarking, use PHPBench and review metrics like
      mode time, variance, and throughput on sample operations such as string and array handling.
# END generated_summary_faq

author: Pareena Verma

##### Tags
skilllevels: Introductory
subjects: Web
cloud_service_providers:
  - Google Cloud

armips:
  - Neoverse

tools_software_languages:
  - PHP
  - Apache
  - PHPBench

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
      title: PHP documentation
      link: https://www.php.net/ 
      type: documentation

  - resource:
      title: PHPBench documentation
      link: https://github.com/phpbench/phpbench
      type: documentation

weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---

