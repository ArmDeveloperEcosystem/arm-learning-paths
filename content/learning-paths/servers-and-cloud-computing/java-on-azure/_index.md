---
title: Deploy Java applications on Azure Cobalt 100 processors 

minutes_to_complete: 30   

description: Deploy Java on Azure Cobalt 100 Arm virtual machines and benchmark application performance with JMH microbenchmarks.
who_is_this_for: This is an introductory topic about Java deployment and benchmarking on Microsoft Azure Cobalt 100 Arm-based virtual machines (VMs). It is designed for developers migrating Java applications from x86_64 to Arm architecture.

learning_objectives: 
    - Provision an Azure Arm-based VM using Azure console, with Ubuntu Pro 24.04 LTS as the base image.
    - Deploy Java on the Azure Arm64 VM.
    - Perform Java baseline testing and benchmarking on the Arm64 VM.

prerequisites:
    - A [Microsoft Azure](https://azure.microsoft.com/) account with access to Cobalt 100-based instances (Dpsv6)

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-09-15T21:18:20Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 762f1a48dc462eaf80807f8247b3970888f01762b4e55e84f0a9f1449b4944f4
  summary_generated_at: '2026-09-15T21:18:20Z'
  summary_source_hash: 762f1a48dc462eaf80807f8247b3970888f01762b4e55e84f0a9f1449b4944f4
  faq_generated_at: '2026-09-15T21:18:20Z'
  faq_source_hash: 762f1a48dc462eaf80807f8247b3970888f01762b4e55e84f0a9f1449b4944f4
  summary: >-
    You'll provision an Arm64 Azure VM powered by Cobalt 100 with Ubuntu Pro 24.04 LTS, install OpenJDK,
    and verify the Java runtime and compiler. First, you'll run a Java baseline to separate Java Virtual Machine (JVM)
    execution from framework overhead. Then, you'll use Java Microbenchmark Harness (JMH) to measure throughput or timing while
    accounting for warmup and just-in-time (JIT) effects. Finally, you'll have benchmark results that provide a
    baseline for further experiments.
  faqs:
  - question: What Azure VM instance type should I use?
    answer: >-
      Use the `D4ps_v6` instance type in the Dpsv6 (D-series v6) family. 
  - question: Which OS image and architecture should I select when creating the VM?
    answer: >-
      Choose Ubuntu Pro 24.04 LTS on Arm64. 
  - question: Does installing default-jdk give me everything I need to run and build Java code?
    answer: >-
      `default-jdk` installs the Java runtime and compiler. For the JMH benchmark, install Maven separately before creating and running the benchmark project.
  - question: How do I verify that Java is installed correctly on Arm64 before running tests?
    answer: >-
      Confirm that the VM reports an Arm64 architecture and that the installed Java versions are present.
      Ensure both the runtime and compiler are available before proceeding.
  - question: What should I look for in JMH output?
    answer: >-
      In JMH, focus on throughput or timing metrics that stabilize after warmup
      to establish a reliable baseline.
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
