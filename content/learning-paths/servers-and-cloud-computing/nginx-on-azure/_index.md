---
title: Deploy NGINX on Azure Cobalt 100 Arm-based virtual machines 

minutes_to_complete: 30   

who_is_this_for: This is an introductory topic for system administrators and developers who want to learn how to deploy and benchmark NGINX on Microsoft Azure Cobalt 100 Arm-based instances.

learning_objectives: 
    - Create an Arm64 virtual machine on Azure Cobalt 100 (Dpsv6) using the Azure console with Ubuntu Pro 24.04 LTS as the base image
    - Install and configure the NGINX web server on the Azure Arm64 virtual machine
    - Configure and test a static website with NGINX on the virtual machine
    - Run baseline NGINX performance tests with ApacheBench (ab) on Ubuntu Pro 24.04 LTS Arm64


prerequisites:
    - A [Microsoft Azure](https://azure.microsoft.com/) account with access to Cobalt 100 based instances (Dpsv6)

author: Pareena Verma

### Tags
skilllevels: Introductory
subjects: Web
cloud_service_providers:
  - Microsoft Azure

armips:
    - Neoverse

tools_software_languages:
    - NGINX
    - ApacheBench

operatingsystems:
    - Linux

further_reading:
  - resource:
      title: NGINX official documentation
      link: https://nginx.org/en/docs/
      type: documentation
  - resource:
      title: ApacheBench official documentation
      link: https://httpd.apache.org/docs/2.4/programs/ab.html
      type: documentation
  - resource:
      title: NGINX on Azure virtual machines
      link: https://docs.nginx.com/nginx/deployment-guides/microsoft-azure/virtual-machines-for-nginx/
      type: documentation


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
