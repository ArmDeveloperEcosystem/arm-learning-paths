---
title: Deploy Golang on Azure Cobalt 100 on Arm
description: Learn how to provision Azure Cobalt 100 Arm64 virtual machines and deploy Golang applications with performance benchmarking on Arm architecture.

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

generate_summary_faq: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-04-30T18:58:18Z'
  generator: template
  source_hash: 46a0a3df799ac473f56d3820390af405b3301758cf15685a250a04c4854aba9e
  summary: >-
    Learn how to provision Azure Cobalt 100 Arm64 virtual machines and deploy Golang applications
    with performance benchmarking on Arm architecture. It is designed for software developers,
    DevOps engineers, and cloud architects looking to migrate their Golang (Go) applications from
    x86_64 to high-performance Arm-based Azure Cobalt 100 virtual machines for improved cost efficiency
    and performance. By the end, you will be able to provision an Azure Arm64 virtual machine
    using the Azure portal, with Ubuntu Pro 24.04 LTS as the base image, deploy Golang on an Arm64-based
    virtual machine running Ubuntu Pro 24.04 LTS, and perform Golang baseline testing and benchmarking
    on both x86_64 and Arm64 virtual machines. It focuses on tools and technologies such as Golang,
    Linux environments, Arm platforms including Neoverse, and cloud platforms such as Microsoft
    Azure. The main steps cover Overview, Create an Azure Cobalt 100 Arm64 virtual machine for
    Golang deployment, Install and configure Golang on Azure Cobalt 100 Arm64, Perform Golang
    baseline testing and web server deployment on Azure Cobalt 100, and Run performance tests
    using go test -bench.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will provision an Azure Arm64 virtual machine using the Azure portal, with Ubuntu Pro
      24.04 LTS as the base image, deploy Golang on an Arm64-based virtual machine running Ubuntu
      Pro 24.04 LTS, and perform Golang baseline testing and benchmarking on both x86_64 and Arm64
      virtual machines. Learn how to provision Azure Cobalt 100 Arm64 virtual machines and deploy
      Golang applications with performance benchmarking on Arm architecture.
  - question: Who is this Learning Path for?
    answer: >-
      This is an introductory topic for software developers, DevOps engineers, and cloud architects
      looking to migrate their Golang (Go) applications from x86_64 to high-performance Arm-based
      Azure Cobalt 100 virtual machines for improved cost efficiency and performance.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: A [Microsoft Azure](https://azure.microsoft.com/)
      account with access to Azure Cobalt 100 Arm-based instances (Dpsv6-series); Basic familiarity
      with the [Go programming language](https://go.dev/) and cloud deployment practices; Understanding
      of Linux command line and virtual machine management.
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including Golang, Linux environments, Arm platforms such as
      Neoverse, and cloud platforms such as Microsoft Azure.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Overview, Create an Azure Cobalt 100 Arm64 virtual
      machine for Golang deployment, Install and configure Golang on Azure Cobalt 100 Arm64, Perform
      Golang baseline testing and web server deployment on Azure Cobalt 100, and Run performance
      tests using go test -bench.
# END generated_summary_faq

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

