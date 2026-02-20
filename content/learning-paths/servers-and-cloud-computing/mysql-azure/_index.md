---
title: Deploy MySQL on Microsoft Azure Cobalt 100 processors

   
minutes_to_complete: 30

who_is_this_for: This is an introductory topic for developers migrating MySQL applications from x86_64 to Arm.

learning_objectives:
    - Provision an Azure Arm64 virtual machine using Azure console, with Ubuntu Pro 24.04 LTS as the base image
    - Deploy MySQL on the Ubuntu virtual machine
    - Perform MySQL baseline testing and benchmarking on Arm64 virtual machines

prerequisites:
    - A [Microsoft Azure](https://azure.microsoft.com/) account with access to Cobalt 100 based instances (Dpsv6)
    - Familiarity with relational databases and the basics of [MySQL](https://dev.mysql.com/doc/refman/8.0/en/introduction.html)

author: Pareena Verma

### Tags
skilllevels: Introductory
subjects: Databases
cloud_service_providers:
  - Microsoft Azure

armips:
    - Neoverse

tools_software_languages:
    - MySQL
    - SQL
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
