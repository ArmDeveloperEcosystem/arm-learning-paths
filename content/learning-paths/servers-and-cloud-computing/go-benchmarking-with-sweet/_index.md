---
title: Benchmark Go performance with Sweet and Benchstat

minutes_to_complete: 60

who_is_this_for: This introductory topic is for developers who want to measure and compare the performance of Go applications on Arm-based servers.

learning_objectives: 
    - Launch Arm64 and x86_64 instances of GCP VMs 
    - Install Go, Sweet, and Benchstat on each VM
    - Use Sweet and Benchstat to compare the performance of Go applications on the two VMs

prerequisites:
    - A [Google Cloud account](https://console.cloud.google.com/). This Learning Path can be run on any cloud provider or on-premises, but it focuses on Google Cloud’s Axion Arm64-based instances.
    - A local machine with [Google Cloud CLI](/install-guides/gcloud/) installed.

author: Geremy Cohen

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
armips:
    - Neoverse
cloud_service_providers: Google Cloud
tools_software_languages:
    - Go
operatingsystems:
    - Linux



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
