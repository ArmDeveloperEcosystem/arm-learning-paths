---
title: Deploy Puppet on Google Cloud C4A 

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for developers deploying and optimizing Puppet workloads on Arm Linux environments, specifically using Google Cloud C4A virtual machines powered by Axion processors. 

learning_objectives:
  - Provision an Arm-based SUSE SLES (SUSE Linux Enterprise Server) virtual machine (VM) on Google Cloud C4A with Axion processors
  - Install Puppet on a SUSE Arm64 C4A instance
  - Verify Puppet by applying a test manifest and confirming successful resource creation on Arm64  
  - Benchmark Puppet by measuring catalog compile time, apply speed, and resource usage on Arm64
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
