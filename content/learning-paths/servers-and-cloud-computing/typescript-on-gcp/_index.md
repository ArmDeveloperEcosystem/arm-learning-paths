---
title: Deploy TypeScript on Google Cloud C4A (Arm-based Axion VMs)

draft: true
cascade:
    draft: true
    
minutes_to_complete: 30

who_is_this_for: This is an introductory topic for software developers deploying and optimizing TypeScript workloads on Arm64 Linux environments, specifically using Google Cloud C4A virtual machines powered by Axion processors.

learning_objectives:
  - Provision an Arm-based SUSE SLES virtual machine on Google Cloud (C4A with Axion processors)
  - Install TypeScript on a SUSE Arm64 (C4A) instance
  - Validate TypeScript functionality by creating, compiling, and running a simple TypeScript script on the Arm64 VM
  - Benchmark TypeScript performance using a JMH-style custom benchmark with perf_hooks on Arm64 architecture

prerequisites:
  - A [Google Cloud Platform (GCP)](https://cloud.google.com/free) account with billing enabled
  - Basic familiarity with [TypeScript](https://www.typescriptlang.org/) and Node.js runtime environment


author: Pareena Verma

##### Tags
skilllevels: Introductory
subjects: Web
cloud_service_providers: Google Cloud

armips:
  - Neoverse

tools_software_languages:
  - TypeScript
  - node.js
  - npm

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
      title: TypeScript documentation
      link:  https://www.typescriptlang.org/docs/
      type: documentation

  - resource:
      title: TypeScript Benchmark documentation
      link: https://tech.spiko.io/posts/benchmarking-typescript-type-checking/
      type: documentation

weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---
