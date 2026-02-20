---
title:  Deploy Envoy Proxy on Google Cloud C4A (Arm-based Axion VMs)

minutes_to_complete: 30

who_is_this_for: This introductory topic for software developers migrating Envoy Proxy workloads from x86_64 to Arm-based servers, specifically on Google Cloud C4A virtual machines built on Axion processors.


learning_objectives:
  - Provision an Arm-based C4A VM on Google Cloud Platform (GCP) 
  - Install and configure Envoy Proxy on a C4A instance
  - Validate Envoy functionality with baseline tests
  - Benchmark Envoy performance on both Arm64 (AArch64) and x86_64 architectures

prerequisites:
  - A [Google Cloud Platform (GCP)](https://cloud.google.com/free?utm_source=google&hl=en) account with billing enabled
  - Familiarity with networking concepts and the [Envoy architecture](https://www.envoyproxy.io/docs/envoy/latest/)

author: Pareena Verma

##### Tags
skilllevels: Introductory
subjects: Web
cloud_service_providers:
  - Google Cloud

armips:
  - Neoverse

tools_software_languages:
  - Envoy
  - Siege
  - Networking
  - Service Mesh

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
      title: Envoy documentation
      link: https://www.envoyproxy.io/docs/envoy/latest/about_docs
      type: documentation

  - resource:
      title: Siege documentation
      link: https://www.joedog.org/siege/manual/
      type: documentation

weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---
