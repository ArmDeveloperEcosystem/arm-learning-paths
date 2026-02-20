---
title: Deploy Couchbase on Google Cloud C4A

    
minutes_to_complete: 30

who_is_this_for: This is an introductory topic for developers deploying Couchbase workloads on Arm Linux environments, specifically using Google Cloud C4A virtual machines (VM) powered by Axion processors. 

learning_objectives:
  - Provision an Arm-based SUSE Linux Enterprise Server (SLES) virtual machine on Google Cloud (C4A with Axion processors)
  - Install Couchbase Server on the SUSE Arm64 (C4A) instance
  - Verify Couchbase deployment by accessing the web console, creating a test bucket, and confirming cluster health 
  - Benchmark Couchbase by measuring operations per second (ops/sec), memory utilization, and disk performance on the Arm platform

prerequisites:
  - A [Google Cloud Platform (GCP)](https://cloud.google.com/free) account with billing enabled  
  - Basic familiarity with [Couchbase](https://www.couchbase.com/)

author: Pareena Verma

##### Tags
skilllevels: Introductory
subjects: Databases
cloud_service_providers:
  - Google Cloud

armips:
  - Neoverse

tools_software_languages:
  - Couchbase

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
