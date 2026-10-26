---
title: Deploy Golang on Azure Cobalt 100 on Arm
description: Learn how to provision Azure Cobalt 100 Arm64 virtual machines and deploy Golang applications with performance benchmarking on Arm architecture.

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for software developers, DevOps engineers, and cloud architects looking to migrate their Golang (Go) applications from x86_64 to high-performance Arm-based Azure Cobalt 100 virtual machines (VMs) for improved cost efficiency and performance.

learning_objectives: 
    - Provision an Azure Arm64-based VM using the Azure portal, with Ubuntu Pro 24.04 LTS as the base image.
    - Deploy Golang on an Arm64-based VM running Ubuntu Pro 24.04 LTS.
    - Perform Golang baseline testing and benchmarking on both x86_64 and Arm64 VMs.

prerequisites:
    - A [Microsoft Azure](https://azure.microsoft.com/) account with access to Azure Cobalt 100 Arm-based instances (Dpsv6-series)
    - Basic familiarity with the [Go programming language](https://go.dev/) and cloud deployment practices
    - Understanding of Linux command line and virtual machine management

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-09-10T22:10:44Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: b29a940e7d899c6bff0e44683011ffd240d2e987aae9ffe1129332a290f32400
  summary_generated_at: '2026-09-10T22:10:44Z'
  summary_source_hash: b29a940e7d899c6bff0e44683011ffd240d2e987aae9ffe1129332a290f32400
  faq_generated_at: '2026-09-10T22:10:44Z'
  faq_source_hash: b29a940e7d899c6bff0e44683011ffd240d2e987aae9ffe1129332a290f32400
  summary: >-
    You'll provision an Azure Cobalt 100-based Arm64 VM, install Go on Ubuntu Pro, and validate the environment with a small web application. First, you'll compile and serve a styled HTML page, then use Go’s built-in benchmarks to measure latency and memory allocation. The workflow gives you baseline metrics for comparing Arm64 and x86_64 systems.
  faqs:
  - question: Which VM sizes are used for the Arm64 and x86-64 comparison?
    answer: >-
      Use `D4ps_v6` from the `Dpsv6` series for the Arm64 benchmark and `D4s_v6` for the x86-64
      comparison, and use Ubuntu Pro 24.04 LTS for both benchmark environments.
  - question: How do I make the Go web server reachable over HTTP?
    answer: >-
      Allow HTTP traffic through Ubuntu's UFW firewall with `sudo ufw allow 80/tcp`, then enable
      UFW with `sudo ufw enable`. Confirm the rule with `sudo ufw status`.
  - question: Which Go distribution should I download for this VM?
    answer: >-
      Download the official Linux Arm64 (AArch64) Go distribution from `go.dev`. This build targets the Arm64 architecture used by Azure Cobalt 100.
  - question: How do I know my Go installation and environment are working before I continue?
    answer: >-
      Build and run the baseline web server in the `goweb` project. If the application starts and
      serves the HTML page that you created, the toolchain and networking are set up correctly.
  - question: Which options should I use to run the benchmarks, and what output should I expect?
    answer: >-
      Use `go test -bench` to run benchmarks and add `-benchmem` to include memory metrics. The output
      reports latency (`ns/op`) and, with `-benchmem`, memory per operation (`B/op`) and allocations
      (`allocs/op`).
# END generated_summary_faq

author: Pareena Verma

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
platforms:
  - Microsoft Azure Cobalt

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
