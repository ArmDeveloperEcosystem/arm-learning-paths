---
title: Deploy PHP on Arm-based C4A virtual machines on Google Cloud 

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for developers migrating Hypertext Preprocessor (PHP) workloads from x86_64 to Arm-based servers, specifically on Google Cloud C4A virtual machines (VM) built on Axion processors.

learning_objectives:
  - Provision a SUSE Linux Enterprise Server (SLES) virtual machine on a Google Cloud C4A Arm-based VM.
  - Install PHP on a SUSE Arm64 C4A instance.
  - Validate PHP functionality by running baseline HTTP server tests. 
  - Benchmark PHP performance using PHPBench on Arm64 architecture. 

prerequisites:
  - A [Google Cloud Platform (GCP)](https://cloud.google.com/free) account with billing enabled
  - Basic familiarity with web servers and PHP scripting

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-11-18T20:23:40Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 71763ea67e42bb6ea6ce580db0bbdb155735f0e9d4202ad1f21fbe758013f27a
  summary_generated_at: '2026-11-18T20:23:40Z'
  summary_source_hash: 71763ea67e42bb6ea6ce580db0bbdb155735f0e9d4202ad1f21fbe758013f27a
  faq_generated_at: '2026-11-18T20:23:40Z'
  faq_source_hash: 71763ea67e42bb6ea6ce580db0bbdb155735f0e9d4202ad1f21fbe758013f27a
  summary: >-
    You'll set up a PHP web stack on a Google Axion C4A virtual machine. First, you'll provision a
    SUSE Linux VM and install PHP and Apache. Then, you configure PHP-FPM through FastCGI and
    check that Apache renders a PHP test page. Finally, you run PHPBench on the VM and record
    its timing and throughput results as a baseline.
  faqs:
  - question: Which C4A machine type and OS image should I use?
    answer: >-
      Use the `c4a-standard-4` machine type and a SUSE Linux image. 
  - question: What result should I expect after configuring PHP-FPM and connecting it to Apache?
    answer: >-
      Request a test PHP page through Apache. You should see rendered output rather than PHP
      source code when Apache passes the request to PHP-FPM through FastCGI.
  - question: How do I know that the baseline HTTP server tests passed?
    answer: >-
      Check for an HTTP `200` response and the expected PHP-generated content. If you see source
      code or a downloaded file, revisit your PHP, Apache, and PHP-FPM configuration.
  - question: Where should I run PHPBench, and what outputs should I review?
    answer: >-
      Run PHPBench on the provisioned C4A VM after completing PHP installation and baseline
      validation. Review the report for mode time, variance, and throughput. Record these
      values as your baseline.
  - question: What should I check if PHPBench fails to run or reports missing components?
    answer: >-
      Confirm that PHP and PHPBench are installed on the VM. Run PHPBench in the same
      environment where you validated the PHP stack.
# END generated_summary_faq

author: Pareena Verma

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

##### Tags
skilllevels: Introductory
subjects: Web
platforms:
  - Google Axion

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

