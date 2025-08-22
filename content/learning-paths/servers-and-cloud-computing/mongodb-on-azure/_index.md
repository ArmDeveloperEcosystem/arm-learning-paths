---
title: Run MongoDB on the Microsoft Azure Cobalt 100 processors 

minutes_to_complete: 30   

who_is_this_for: This Learning Path is designed for software developers looking to migrate their MongoDB workloads from x86_64 to Arm-based platforms, specifically on the Microsoft Azure Cobalt 100 processors.

learning_objectives: 
    - Provision an Azure Arm64 virtual machine using Azure console, with Ubuntu as the base image.
    - Learn how to create an Azure Linux 3.0 Docker container.
    - Deploy the MongoDB on an Azure Linux 3.0 Arm64-based Docker container and an Azure Linux 3.0 custom-image-based Azure virtual machine.
    - Perform MongoDB baseline testing and benchmarking in both the containerized and virtual machine environments.

prerequisites:
    - A [Microsoft Azure](https://azure.microsoft.com/) account with access to Cobalt 100 based instances (Dpsv6). 
    - A machine with [Docker](/install-guides/docker/) installed.
    - Basic understanding of Linux command line.
    - Familiarity with the [MongoDB architecture](https://www.mongodb.com/) and deployment practices on Arm64 platforms.

author: Jason Andrews

### Tags
skilllevels: Advanced
subjects: Databases
cloud_service_providers: Microsoft Azure

armips:
    - Neoverse

tools_software_languages:
    - MongoDB
    - Docker
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
      title: MongoDB on Azure
      link: https://azure.microsoft.com/en-us/solutions/mongodb
      type: documentation


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
