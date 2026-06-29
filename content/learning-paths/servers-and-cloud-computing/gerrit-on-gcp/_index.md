---
title: Deploy Gerrit on a Google Cloud C4A instance 

description: Deploy Gerrit on an Ubuntu 24.04 arm64 Google Cloud C4A virtual machine powered by Google Axion processors, verify web access, and benchmark baseline performance.
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
subjects: CI-CD
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
      title: Google Cloud documentation for C4A VMs
      link: https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4a_series
      type: documentation

  - resource:
      title: Gerrit documentation
      link: https://gerrit-review.googlesource.com/Documentation/
      type: documentation

  - resource:
      title: Getting started with Google Cloud Platform
      link: /learning-paths/servers-and-cloud-computing/csp/google/
      type: website

  - resource:
      title: Gerrit 3.14 release notes
      link: https://www.gerritcodereview.com/3.14.html
      type: documentation

weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---
