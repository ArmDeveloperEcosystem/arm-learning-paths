---
title: Deploy Golang on the Microsoft Azure Cobalt 100 processors 

minutes_to_complete: 40   

who_is_this_for: This Learning Path is designed for software developers looking to migrate their Golang workloads from x86_64 to Arm-based platforms, specifically on the Microsoft Azure Cobalt 100 processors.

learning_objectives: 
    - Provision an Azure Arm64 virtual machine using Azure console, with Ubuntu Pro 24.04 LTS as the base image.
    - Deploy Golang on an Arm64-based virtual machine running Ubuntu Pro 24.04 LTS.
    - Perform Golang baseline testing and benchmarking on both x86_64 and Arm64 virtual machine.

prerequisites:
    - A [Microsoft Azure](https://azure.microsoft.com/) account with access to Cobalt 100 based instances (Dpsv6)
    - Basic understanding of Linux command line.
    - Familiarity with the [Golang](https://go.dev/) and deployment practices on Arm64 platforms.

author: Jason Andrews

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
cloud_service_providers: Microsoft Azure

armips:
    - Neoverse

tools_software_languages:
    - Golang
    - go test -bench

operatingsystems:
    - Linux

further_reading:
    - resource: 
        title: Effective Go Benchmarking
        link: https://go.dev/doc/effective_go#testing
        type: Guide
    - resource:
        title: Testing and Benchmarking in Go
        link: https://pkg.go.dev/testing
        type: Official Documentation
    - resource:        
        title: Using go test -bench for Benchmarking
        link: https://pkg.go.dev/cmd/go#hdr-Testing_flags
        type: Reference


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
