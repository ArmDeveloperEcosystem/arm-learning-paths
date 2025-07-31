---
title: Deploy NGINX on the Microsoft Azure Cobalt 100 processors 

minutes_to_complete: 30   

who_is_this_for: This Learning Path introduces NGINX deployment on Microsoft Azure Cobalt 100 (Arm-based) virtual machine. It is intended for system administrators and developers looking to deploy and benchmark NGINX on Arm architecture with minimal adjustments from traditional x86_64 environments.

learning_objectives: 
    - Start an Azure Arm64 virtual machine using the Azure console and Ubuntu Pro 24.04 LTS as the base image.
    - Deploy the NGINX web server on the Azure Arm64 virtual machine running Ubuntu Pro 24.04 LTS.
    - Configure and test a static website using NGINX on the virtual machine.
    - Perform baseline testing and benchmarking of NGINX in the Ubuntu Pro 24.04 LTS Arm64 virtual machine environment.


prerequisites:
    - A [Microsoft Azure](https://azure.microsoft.com/) account with access to Cobalt 100 based instances (Dpsv6).
    - Familiarity with the [NGINX architecture](https://www.nginx.com/) and deployment practices on Arm64 platforms.
    - Network settings (firewalls and security groups) should allow inbound communication on ports 22 (SSH) and 80 (HTTP).

author: Jason Andrews

### Tags
skilllevels: Advanced
subjects: Web
cloud_service_providers: Microsoft Azure

armips:
    - Neoverse

tools_software_languages:
    - NGINX
    - Apache Bench

operatingsystems:
    - Linux

further_reading:
  - resource:
      title: NGINX official documentation
      link: https://nginx.org/en/docs/
      type: documentation
  - resource:
      title: Apache Bench official documentation
      link: https://httpd.apache.org/docs/2.4/programs/ab.html
      type: documentation
  - resource:
      title: NGINX on Azure
      link: https://docs.nginx.com/nginx/deployment-guides/microsoft-azure/virtual-machines-for-nginx/
      type: documentation


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
