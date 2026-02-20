---
title: Run MongoDB on Arm-based Azure Cobalt 100 instances

minutes_to_complete: 30   

who_is_this_for: This is an introductory topic for software developers who want to migrate MongoDB workloads to Arm-based platforms, with a focus on Microsoft Azure Cobalt 100 Arm64 instances.

learning_objectives: 
    - Provision an Arm64-based Cobalt 100 virtual machine in Azure using Ubuntu Pro 24.04 LTS
    - Deploy MongoDB on the Cobalt 100 instance
    - Run baseline tests and performance benchmarks on MongoDB in the Arm64 environment

prerequisites:
    - A [Microsoft Azure](https://azure.microsoft.com/) account with access to Cobalt 100 (Dpsv6) instances
    - Familiarity with the [MongoDB architecture](https://www.mongodb.com/) and deployment practices on Arm64 platforms

author: Pareena Verma

### Tags
skilllevels: Introductory
subjects: Databases
cloud_service_providers:
  - Microsoft Azure

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
