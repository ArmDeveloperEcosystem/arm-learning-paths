---
title: Deploy Golang on Azure Cobalt 100 on Arm

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for software developers, DevOps engineers, and cloud architects looking to migrate their Golang (Go) applications from x86_64 to high-performance Arm-based Azure Cobalt 100 virtual machines for improved cost efficiency and performance.

learning_objectives: 
    - Provision an Azure Arm64 virtual machine using the Azure portal, with Ubuntu Pro 24.04 LTS as the base image
    - Deploy Golang on an Arm64-based virtual machine running Ubuntu Pro 24.04 LTS
    - Perform Golang baseline testing and benchmarking on both x86_64 and Arm64 virtual machines

prerequisites:
    - A [Microsoft Azure](https://azure.microsoft.com/) account with access to Azure Cobalt 100 Arm-based instances (Dpsv6-series)
    - Basic familiarity with the [Go programming language](https://go.dev/) and cloud deployment practices
    - Understanding of Linux command line and virtual machine management

author: Pareena Verma

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
cloud_service_providers:
  - Microsoft Azure

armips:
  - Neoverse

tools_software_languages:
    - Golang

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
        type: Documentation
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
