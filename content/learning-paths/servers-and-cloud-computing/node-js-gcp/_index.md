---
title:  Deploy Node.js on Google Cloud C4A (Arm-based Axion VMs)

draft: true
cascade:
    draft: true

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for software developers migrating Node.js workloads from x86_64 to Arm-based servers, specifically on Google Cloud C4A virtual machines built on Axion processors.


learning_objectives:
  - Provision an Arm-based SUSE SLES virtual machine on Google Cloud (C4A with Axion processors)
  - Install and configure Node.js on a SUSE Arm64 (C4A) instance
  - Validate Node.js functionality with baseline HTTP server tests  
  - Benchmark Node.js performance using Autocannon on Arm64 (AArch64) architecture 


prerequisites:
  - A [Google Cloud Platform (GCP)](https://cloud.google.com/free) account with billing enabled
  - Familiarity with networking concepts and [Node.js event-driven architecture](https://nodejs.org/en/docs/guides/event-loop-timers-and-nexttick)

author: Pareena Verma

##### Tags
skilllevels: Introductory
subjects: Web
cloud_service_providers: Google Cloud

armips:
  - Neoverse

tools_software_languages:
  - Node.js
  - npm
  - Autocannon

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
      title: Node.js documentation
      link: https://nodejs.org/en
      type: documentation

  - resource:
      title: Autocannon documentation
      link: https://www.npmjs.com/package/autocannon/v/5.0.0
      type: documentation

weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---
