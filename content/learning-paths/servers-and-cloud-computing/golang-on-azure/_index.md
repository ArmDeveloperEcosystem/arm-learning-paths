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

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T01:07:53Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 46a0a3df799ac473f56d3820390af405b3301758cf15685a250a04c4854aba9e
  summary_generated_at: '2026-06-02T04:05:37Z'
  summary_source_hash: 46a0a3df799ac473f56d3820390af405b3301758cf15685a250a04c4854aba9e
  faq_generated_at: '2026-06-03T01:07:53Z'
  faq_source_hash: 46a0a3df799ac473f56d3820390af405b3301758cf15685a250a04c4854aba9e
  summary: >-
    This introductory Learning Path guides you through provisioning an Arm64 Azure Cobalt 100
    (Dpsv6-series) virtual machine using the Azure portal with Ubuntu Pro 24.04 LTS, installing
    the Go toolchain, deploying a simple Go web server for baseline validation, and running performance
    tests with go test -bench (and -benchmem). You will use the official Arm64 Go distribution,
    confirm compilation, networking, and runtime on the VM, and perform basic benchmarking, with
    objectives that include comparing results on both x86_64 and Arm64 virtual machines. Prerequisites
    include an Azure account with access to Cobalt 100 instances, familiarity with Go and cloud
    deployment practices, and understanding of the Linux command line and VM management. After
    completing the path, you can provision, deploy, and benchmark Go workloads on Azure Cobalt
    100.
  faqs:
  - question: What do I need before running this Learning Path?
    answer: >-
      You need a Microsoft Azure account with access to Azure Cobalt 100 Arm-based instances (Dpsv6-series),
      basic familiarity with Go and cloud deployment practices, and an understanding of the Linux
      command line and virtual machine management.
  - question: Which VM series and operating system image should I choose?
    answer: >-
      Use a general-purpose Dpsv6-series virtual machine and select Ubuntu Pro 24.04 LTS (Arm64)
      as the base image in the Azure portal.
  - question: Which Go distribution should I install on the Arm64 VM?
    answer: >-
      Download the official Arm64-optimized Go distribution from the Go website and install it
      on Ubuntu Pro 24.04 LTS. The steps guide you to fetch the tarball directly from go.dev.
  - question: What result should I expect from the baseline Go web server test?
    answer: >-
      You will build and run a simple Go web application that serves an HTML page, confirming
      that compilation, networking, and runtime execution work correctly on the Azure Cobalt 100
      Arm64 VM.
  - question: How do I run and interpret the performance benchmarks, and compare with x86_64?
    answer: >-
      Use go test -bench to run benchmarks and add -benchmem to capture memory usage, which reports
      ns/op, B/op, and allocs/op. To compare architectures, run the same benchmark suite on an
      x86_64 VM and evaluate the reported metrics side by side.
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

