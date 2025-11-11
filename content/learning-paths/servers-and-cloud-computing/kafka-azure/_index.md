---
title: Deploy Kafka on the Microsoft Azure Cobalt 100 processors 

draft: true
cascade:
    draft: true

minutes_to_complete: 30   

who_is_this_for: This is an advanced topic designed for software developers looking to migrate their Kafka workloads from x86_64 to Arm-based platforms, specifically on the Microsoft Azure Cobalt 100 processors.

learning_objectives: 
    - Provision an Azure Arm64 virtual machine using Azure console, with Ubuntu Pro 24.04 LTS as the base image.
    - Deploy Kafka on the Ubuntu virtual machine.
    - Perform Kafka baseline testing and benchmarking on Arm64 virtual machines.

prerequisites:
    - A [Microsoft Azure](https://azure.microsoft.com/) account with access to Cobalt 100 based instances (Dpsv6). 
    - Basic understanding of Linux command line.
    - Familiarity with the [Apache Kafka architecture](https://kafka.apache.org/) and deployment practices on Arm64 platforms.

author: Pareena Verma

### Tags
skilllevels: Advanced
subjects: Storage
cloud_service_providers: Microsoft Azure

armips:
    - Neoverse

tools_software_languages:
    - Kafka

operatingsystems:
    - Linux

further_reading:
    - resource:
        title: Kafka Manual
        link: https://kafka.apache.org/documentation/
        type: documentation
    - resource:
        title: Kafka Performance Tool
        link: https://codemia.io/knowledge-hub/path/use_kafka-producer-perf-testsh_how_to_set_producer_config_at_kafka_210-0820
        type: documentation
    - resource:        
        title: Kafka on Azure
        link: https://learn.microsoft.com/en-us/samples/azure/azure-quickstart-templates/kafka-ubuntu-multidisks/
        type: documentation


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
