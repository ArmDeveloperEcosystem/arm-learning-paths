---
title: Deploy Gerrit on Google Cloud C4A
description: Learn how to install and configure Gerrit on Google Cloud Axion C4A Arm64 instances and benchmark its performance 

    
minutes_to_complete: 30

who_is_this_for: This is an introductory topic for developers deploying Gerrit in Arm Linux environments, specifically using Google Cloud C4A virtual machines (VM) powered by Axion processors. 

learning_objectives:
  - Provision an Arm-based Ubuntu 24.04 LTS virtual machine on Google Cloud (C4A with Axion processors)
  - Install Gerrit Server on the Ubuntu arm64 (C4A) instance
  - Verify Gerrit deployment by accessing the web console
  - Benchmark Gerrit by measuring operations per second (ops/sec), memory utilization, and disk performance on the Arm platform

prerequisites:
  - A [Google Cloud Platform (GCP)](https://cloud.google.com/free) account with billing enabled  
  - Basic familiarity with [Gerrit](https://gerrit-review.googlesource.com/Documentation/intro-gerrit-walkthrough-github.html)

author: Doug Anson

##### Tags
skilllevels: Introductory
subjects: Databases
cloud_service_providers:
  - Google Cloud

armips:
  - Neoverse

tools_software_languages:
  - Gerrit

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
      title: Gerrit documentation
      link: https://gerrit-review.googlesource.com/Documentation/intro-gerrit-walkthrough-github.html
      type: documentation

weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---
