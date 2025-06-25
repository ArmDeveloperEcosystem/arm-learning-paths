---
title: Go Benchmarks with Sweet and Benchstat

draft: true
cascade:
    draft: true

minutes_to_complete: 60

who_is_this_for: This is an introductory topic for developers who are interested in measuring the performance of Go-based applications on Arm-based servers.

learning_objectives: 
    - Learn how to start up Arm64 and x64 instances of GCP VMs 
    - Install Go, benchmarks, benchstat, and sweet on the two VMs  
    - Use sweet and benchstat to compare the performance of Go applications on the two VMs

prerequisites:
    - A [Google Cloud account](https://console.cloud.google.com/).  This learning path can be run on on-prem or on any cloud provider instance, but specifically documents the process for running on Google Axion.
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
