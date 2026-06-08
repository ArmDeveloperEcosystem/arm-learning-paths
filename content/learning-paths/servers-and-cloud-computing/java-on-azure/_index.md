---
title: Deploy Java applications on Azure Cobalt 100 processors 

minutes_to_complete: 30   

description: Deploy Java on Azure Cobalt 100 Arm virtual machines and benchmark application performance with JMH microbenchmarks.
who_is_this_for: This is an introductory topic about Java deployment and benchmarking on Microsoft Azure Cobalt 100 Arm-based virtual machines. It is designed for developers migrating Java applications from x86_64 to Arm architecture.

learning_objectives: 
    - Provision an Azure Arm-based Cobalt 100 virtual machine using Azure console, with Ubuntu Pro 24.04 LTS as the base image
    - Deploy Java on the Azure Arm64 virtual machine
    - Perform Java baseline testing and benchmarking on the Arm64 virtual machines

prerequisites:
    - A [Microsoft Azure](https://azure.microsoft.com/) account with access to Cobalt 100 based instances (Dpsv6)


generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T01:13:27Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 58b0bb9f6e4190029d7edc65bdb04a597c7539de55a5e51ed59e88b174e527c3
  summary_generated_at: '2026-06-02T04:09:50Z'
  summary_source_hash: 58b0bb9f6e4190029d7edc65bdb04a597c7539de55a5e51ed59e88b174e527c3
  faq_generated_at: '2026-06-03T01:13:27Z'
  faq_source_hash: 58b0bb9f6e4190029d7edc65bdb04a597c7539de55a5e51ed59e88b174e527c3
  summary: >-
    Provision an Arm-based Azure Cobalt 100 virtual machine using the Azure portal, install Java
    on Ubuntu Pro 24.04 LTS (Arm64), and measure application performance with JVM-aware microbenchmarks.
    This introductory path is aimed at developers migrating Java workloads to Arm and walks through
    creating a Cobalt 100 (Dpsv6) VM, installing the JRE and JDK via the Ubuntu package manager,
    validating the installation, and running a simple Tomcat-like Java baseline before benchmarking
    with JMH. You will learn how to set up the environment, run baseline tests, and execute JMH
    to assess Java performance on Arm. A Microsoft Azure account with access to Cobalt 100 instances
    is required. Estimated time to complete: 30 minutes.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need a Microsoft Azure account with access to Cobalt 100 based instances (Dpsv6). No
      other explicit prerequisites are listed.
  - question: How should I create the VM and which OS image should I choose?
    answer: >-
      Use the Azure portal to create an Arm64 VM with the Cobalt 100 processor. Select Ubuntu
      Pro 24.04 LTS as the base image, following the VM creation steps in the portal.
  - question: Which Java package should I install on Ubuntu Pro 24.04 LTS (Arm64)?
    answer: >-
      Install OpenJDK using the default-jdk package, which provides both the JRE and JDK. Run:
      sudo apt update and then sudo apt install -y default-jdk.
  - question: Why start with a Tomcat-like baseline instead of deploying a full Tomcat server?
    answer: >-
      A Tomcat-like baseline lets you measure how efficiently raw Java executes simple operations
      before adding server components. Full servers introduce complexity such as request parsing,
      thread management, and I/O handling.
  - question: How will I benchmark the Java code and what results should I look for?
    answer: >-
      You will use JMH (Java Microbenchmark Harness) to run JVM-aware microbenchmarks. JMH accounts
      for JIT and warmup and enables you to measure throughput for small code snippets.
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
    - Java
    - JMH

operatingsystems:
    - Linux

further_reading:
  - resource:
      title: Azure Virtual Machines documentation
      link: https://learn.microsoft.com/en-us/azure/virtual-machines/
      type: documentation
  - resource:
      title: Azure Container Instances documentation
      link: https://learn.microsoft.com/en-us/azure/container-instances/
      type: documentation
  - resource:
      title: Java on Azure
      link: https://learn.microsoft.com/en-us/java/azure/
      type: documentation
  - resource:
      title: JMH (Java Microbenchmark Harness) documentation
      link: https://openjdk.org/projects/code-tools/jmh/
      type: documentation


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

