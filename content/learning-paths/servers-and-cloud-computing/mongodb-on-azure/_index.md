---
title: Run MongoDB on the Microsoft Azure Cobalt 100 processors 

draft: true
cascade:
    draft: true

minutes_to_complete: 30   

who_is_this_for: This Learning Path is designed for software developers looking to migrate their MongoDB workloads to Arm-based platforms, specifically on the Microsoft Azure Cobalt 100 processors.

learning_objectives: 
    - Provision an Azure Arm64 Cobalt 100 based virtual machine using Azure console, with Ubuntu Pro 24.04 LTS as the base image.
    - Deploy MongoDB on an Azure Cobalt 100 based virtual machine.
    - Perform MongoDB baseline testing and benchmarking on the Arm64 virtual machine.

prerequisites:
    - A [Microsoft Azure](https://azure.microsoft.com/) account with access to Cobalt 100 based instances (Dpsv6). 
    - Familiarity with the [MongoDB architecture](https://www.mongodb.com/) and deployment practices on Arm64 platforms.

author: Pareena Verma

### Tags
skilllevels: Introductory
subjects: Databases
cloud_service_providers: Microsoft Azure

armips:
    - Neoverse

tools_software_languages:
    - MongoDB
    - mongotop
    - mongostat

operatingsystems:
    - Linux

further_reading:
    - resource:
        title: MongoDB Manual
        link: https://www.mongodb.com/docs/manual/
        type: documentation
    - resource:
        title: MongoDB Performance Tool
        link: https://github.com/idealo/mongodb-performance-test#readme
        type: documentation
    - resource:        
        title: MongoDB on Azure
        link: https://azure.microsoft.com/en-us/solutions/mongodb
        type: documentation


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
