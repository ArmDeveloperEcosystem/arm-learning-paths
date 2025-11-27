---
title: Run CircleCI Arm Native Workflows on a SUSE Arm GCP VM
    
minutes_to_complete: 45

who_is_this_for: This is an introductory topic for developers and DevOps engineers looking to set up and run CircleCI Arm native workflows on SUSE Linux Arm64 virtual machines (VMs), specifically on Google Cloud C4A with Axion processors, using self-hosted runners.

learning_objectives:
  - Provision a SUSE Arm64 virtual machine on Google Cloud (C4A with Axion processors)
  - Install and configure CircleCI self-hosted machine runners on Arm64
  - Create a cloud-native Node.js demo app to run on the self-hosted Arm runner
  - Write and execute a CircleCI workflow using a custom Arm resource class
  - Test CircleCI workflows locally and understand job execution on Arm64 runners

prerequisites:
  - A [Google Cloud Platform (GCP)](https://cloud.google.com/free) account with billing enabled
  - Basic familiarity with Linux command line, Node.js, and npm
  - Basic understanding of CircleCI concepts such as 
    [workflows](https://circleci.com/docs/guides/orchestrate/workflows/), 
    [jobs](https://circleci.com/docs/guides/orchestrate/jobs-steps/),
    [resource classes](https://circleci.com/docs/guides/execution-managed/resource-class-overview/), and 
    [runners](https://circleci.com/docs/guides/execution-runner/runner-overview/)


author: Pareena Verma

##### Tags
skilllevels: Introductory
subjects: CI-CD
cloud_service_providers: Google Cloud

armips:
  - Neoverse

tools_software_languages:
  - CircleCI
  - Node.js
  - npm
  - Docker

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
      title: CircleCI Self-Hosted Runner Documentation
      link:  https://circleci.com/docs/guides/execution-runner/install-machine-runner-3-on-linux/
      type: documentation

  - resource:
      title: CircleCI CLI Documentation
      link: https://circleci.com/docs/guides/toolkit/local-cli/
      type: documentation

  - resource:
      title: Node.js Express Documentation
      link: https://expressjs.com/
      type: documentation

weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---
