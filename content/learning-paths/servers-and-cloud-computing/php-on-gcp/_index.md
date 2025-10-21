---
title:  Deploy PHP on Google Cloud C4A on Arm-based Axion VMs

  
minutes_to_complete: 30

who_is_this_for: This is an introductory topic for software developers migrating PHP workloads from x86_64 to Arm-based servers, specifically on Google Cloud C4A virtual machines built on Axion processors.


learning_objectives:
  - Provision a SUSE SLES virtual machine on a Google Cloud C4A Arm-based Axion VM
  - Install PHP on a SUSE Arm64 C4A instance
  - Validate PHP functionality with baseline HTTP server tests  
  - Benchmark PHP performance using PHPBench on Arm64 architecture 


prerequisites:
  - A [Google Cloud Platform (GCP)](https://cloud.google.com/free) account with billing enabled
  - Basic familiarity with web servers and PHP scripting
author: Pareena Verma

##### Tags
skilllevels: Introductory
subjects: Web
cloud_service_providers: Google Cloud

armips:
  - Neoverse

tools_software_languages:
  - PHP
  - apache
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
