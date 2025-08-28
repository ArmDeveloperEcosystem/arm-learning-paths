---
title: Run MySQL on Microsoft Azure Cobalt 100 processors

minutes_to_complete: 40

who_is_this_for: This is an advanced topic that introduces MySQL deployment on Microsoft Azure Cobalt 100 (Arm-based) virtual machines. It is designed for developers migrating MySQL applications from x86_64 to Arm.

learning_objectives: 
    - Provision an Azure Arm64 virtual machine using Azure console
    - Learn how to create an Azure Linux 3.0 Docker container
    - Deploy a MySQL database inside an Azure Linux 3.0 Arm64-based Docker container or an Azure Linux 3.0 custom-image based Azure virtual machine
    - Run MySQL mysqlslap benchmarks to understand and evaluate performance on the Azure Cobalt 100 virtual machine

prerequisites:
    - A [Microsoft Azure](https://azure.microsoft.com/) account with access to Cobalt 100 based instances (Dpsv6)
    - A machine with [Docker](/install-guides/docker/) installed
    - Familiarity with relational databases and the basics of [MySQL](https://dev.mysql.com/doc/refman/8.0/en/introduction.html)

author: Pareena Verma

### Tags
skilllevels: Advanced
subjects: Databases
cloud_service_providers: Microsoft Azure

armips:
    - Neoverse

tools_software_languages:
    - MySQL
    - mysqlslap
    - Docker
 
operatingsystems:
    - Linux

further_reading:
  - resource:
      title: Azure Virtual Machines documentation
      link: https://learn.microsoft.com/en-us/azure/virtual-machines/
      type: documentation
  - resource:
      title: Azure Container Instances documentation
      link: https://learn.microsoft.com/en-us/azure/container-instances/
      type: documentation
  - resource:
      title: Docker overview
      link: https://docs.docker.com/get-started/overview/
      type: documentation
  - resource:
      title: MySQL Manual
      link: https://dev.mysql.com/doc/refman/8.0/en/installing.html
      type: documentation
  - resource:
      title: mysqlslap official website
      link: https://dev.mysql.com/doc/refman/8.4/en/mysqlslap.html
      type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
