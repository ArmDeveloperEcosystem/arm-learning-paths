---
title: Deploy Django on Google Cloud C4A (Arm-based Axion VMs)

draft: true
cascade:
    draft: true
    
minutes_to_complete: 30

who_is_this_for: This learning path is intended for software developers deploying and optimizing Django-based web applications on Linux/Arm64 environments, specifically using Google Cloud C4A virtual machines powered by Axion processors.

learning_objectives:
  - Provision an Arm-based SUSE SLES virtual machine on Google Cloud (C4A with Axion processors)
  - Install Django on a SUSE Arm64 (C4A) instance
  - Verify Django functionality by running the development server and accessing the default welcome page on the Arm64 VM  
  - Measure Django application performance by benchmarking request handling throughput and latency using the official ApacheBench (ab) tool with Gunicorn on Arm64 (Aarch64)

prerequisites:
  - A [Google Cloud Platform (GCP)](https://cloud.google.com/free) account with billing enabled  
  - Basic familiarity with [Django](https://www.djangoproject.com/)

author: Pareena Verma

##### Tags
skilllevels: Introductory
subjects: Web
cloud_service_providers: Google Cloud

armips:
  - Neoverse

tools_software_languages:
  - Django
  - Python
  - Gunicorn
  - Apache Bench

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
      title: Django documentation
      link: https://docs.djangoproject.com/
      type: documentation

  - resource:
      title: Apache-bench documentation
      link: https://httpd.apache.org/docs/2.4/programs/ab.html 
      type: documentation

weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---
