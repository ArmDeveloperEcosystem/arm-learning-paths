---
title: Deploy Elasticsearch on Azure Cobalt 100 Arm virtual machines

description: Learn how to deploy Elasticsearch on an Azure Cobalt 100 Arm virtual machine, validate the service, and run a baseline ESRally benchmark.

draft: true
cascade:
    draft: true

minutes_to_complete: 30

who_is_this_for: This Learning Path is for developers who want to deploy and benchmark Elasticsearch on Azure Cobalt 100 Arm virtual machines.

learning_objectives: 
    - Provision an Arm-based Azure Cobalt 100 virtual machine via Azure
    - Install and validate Elasticsearch on the Cobalt 100 VM
    - Run a baseline ESRally benchmark and interpret key performance metrics

prerequisites:
    - A [Microsoft Azure](https://azure.microsoft.com/) account with access to Cobalt 100 instances (Dpsv6)
    - Basic familiarity with SSH
    - Familiarity with Elasticsearch and ESRally


author: Doug Anson

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
cloud_service_providers:
  - Microsoft Azure

armips:
    - Neoverse

tools_software_languages:
    - Elasticsearch
    - ESRally
    - Bash

operatingsystems:
    - Linux

further_reading:
  - resource:
      title: Azure Virtual Machines documentation
      link: https://learn.microsoft.com/en-us/azure/virtual-machines/
      type: documentation
  - resource:
      title: Elasticsearch documentation
      link: https://www.elastic.co/docs/reference/elasticsearch
      type: documentation
  - resource:
      title: ESRally documentation
      link: https://esrally.readthedocs.io/en/stable/index.html
      type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

## Learning Path overview

In this Learning Path, you deploy Elasticsearch on an Arm-based Azure Cobalt 100 virtual machine and run a baseline benchmark with ESRally. You then review key latency and throughput metrics so you can assess initial performance on Arm.

## What you will do

You will complete one end-to-end developer task:

1. Create an Azure Cobalt 100 Arm virtual machine.
2. Install Elasticsearch and ESRally.
3. Run the geonames track and review benchmark results.
