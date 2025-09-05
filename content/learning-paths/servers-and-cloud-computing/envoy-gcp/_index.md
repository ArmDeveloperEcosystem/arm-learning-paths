---
title: Deploy Envoy on Google Axion processors

draft: true
cascade:
    draft: true
   
minutes_to_complete: 30

who_is_this_for: This introductory topic is for software developers interested in migrating their Envoy workloads from x86_64 platforms to Arm-based platforms, specifically on Google Axion–based C4A virtual machines.  

learning_objectives:
  - Start an Arm virtual machine on Google Cloud Platform (GCP) using the C4A Google Axion instance family with RHEL 9 as the base image
  - Install and configure Envoy on Arm-based GCP C4A instances
  - Validate Envoy functionality through baseline testing
  - Benchmark Envoy performance on Arm

prerequisites:
  - A [Google Cloud Platform (GCP)](https://cloud.google.com/free?utm_source=google&hl=en) account with billing enabled
  - Familiarity with networking concepts and the [Envoy architecture](https://www.envoyproxy.io/docs/envoy/latest/).

author: Pareena Verma

##### Tags
skilllevels: Advanced
subjects: Web
cloud_service_providers: Google Cloud

armips:
  - Neoverse

tools_software_languages:
  - Envoy
  - Siege 

operatingsystems:
  - Linux

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
further_reading:
  - resource:
      title: Google Cloud official documentation
      link: https://cloud.google.com/docs
      type: documentation

  - resource:
      title: Envoy documentation
      link: https://www.envoyproxy.io/docs/envoy/latest/about_docs
      type: documentation

  - resource:
      title: The official documentation for Siege
      link: https://www.joedog.org/siege-manual/
      type: documentation

weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # Indicates this should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
