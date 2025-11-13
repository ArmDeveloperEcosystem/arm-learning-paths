---
title: Deploy Couchbase on Google Cloud C4A (Arm-based Axion VMs)

minutes_to_complete: 30

who_is_this_for: This learning path is intended for software developers deploying and optimizing Couchbase  workloads on Linux/Arm64 environments, specifically using Google Cloud C4A virtual machines powered by Axion processors. 

learning_objectives:
  - Provision an Arm-based SUSE SLES virtual machine on Google Cloud (C4A with Axion processors)
  - Install Couchbase Server on the SUSE Arm64 (C4A) instance
  - Verify Couchbase deployment by accessing the Web Console, creating a test bucket, and confirming cluster health on Arm64  
  - Benchmark Couchbase by measuring operations per second (Ops/sec), memory utilization, and disk performance on the Arm64 platform

prerequisites:
  - A [Google Cloud Platform (GCP)](https://cloud.google.com/free) account with billing enabled  
  - Basic familiarity with [Couchbase](https://www.couchbase.com/)

author: Pareena Verma

##### Tags
skilllevels: Introductory
subjects: Databases
cloud_service_providers: Google Cloud

armips:
  - Neoverse

tools_software_languages:
  - Couchbase
  - cbc-pillowfight
  - curl

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
      title: Couchbase documentation
      link: https://docs.couchbase.com/home/index.html
      type: documentation

weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---
