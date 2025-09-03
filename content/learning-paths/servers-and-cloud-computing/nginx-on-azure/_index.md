---
title: Run Nginx on the Microsoft Azure Cobalt 100 processors 

minutes_to_complete: 30   

who_is_this_for: This Learning Path introduces Nginx deployment on Microsoft Azure Cobalt 100 (Arm-based) virtual machine. It is intended for system administrators and developers looking to deploy and benchmark Nginx on Arm architecture with minimal adjustments from traditional x86_64 environments.

learning_objectives: 
    - Start an Azure Arm64 virtual machine using Azure console and Ubuntu as the base image.
    - Learn how to create an Azure Linux 3.0 Docker container.
    - Deploy the Nginx web server on an Azure Linux 3.0 Arm64-based Docker container and an Azure Linux 3.0 custom-image-based Azure virtual machine.
    - Test and Benchmark Nginx in both the containerized and virtual machine environments.

prerequisites:
    - A [Microsoft Azure](https://azure.microsoft.com/) account with access to Cobalt 100 based instances (Dpsv6). 
    - A machine with [Docker](/install-guides/docker/) installed.
    - Network settings (firewalls and security groups) should allow inbound communication on ports 22 (SSH) and 80 (HTTP).

author: Jason Andrews

### Tags
skilllevels: Advanced
subjects: Web
cloud_service_providers: Microsoft Azure

armips:
    - Neoverse

tools_software_languages:
    - Nginx
    - Docker
    - Apache Bench

operatingsystems:
    - Linux

further_reading:
  - resource:
      title: Nginx official documentation
      link: https://nginx.org/en/docs/
      type: documentation
  - resource:
      title: Apache Bench official documentation
      link: https://httpd.apache.org/docs/2.4/programs/ab.html
      type: documentation
  - resource:
      title: Docker overview
      link: https://docs.docker.com/get-started/overview/
      type: documentation
  - resource:
      title: Nginx on Azure
      link: https://docs.nginx.com/nginx/deployment-guides/microsoft-azure/virtual-machines-for-nginx/
      type: documentation


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
