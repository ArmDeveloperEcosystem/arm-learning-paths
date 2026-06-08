---
title: Run Spark applications on Microsoft Azure Cobalt 100 processors

minutes_to_complete: 60

who_is_this_for: This is an advanced topic that introduces Spark deployment on Microsoft Azure Cobalt 100 (Arm-based) virtual machines. It is designed for developers migrating Spark applications from x86_64 to Arm.

learning_objectives: 
    - Provision an Azure Arm64 virtual machine using Azure console
    - Learn how to create an Azure Linux 3.0 Docker container
    - Deploy a Spark application inside an Azure Linux 3.0 Arm64-based Docker container or an Azure Linux 3.0 custom-image based Azure virtual machine
    - Run a suite of Spark benchmarks to understand and evaluate performance on the Azure Cobalt 100 virtual machine

prerequisites:
    - A [Microsoft Azure](https://azure.microsoft.com/) account with access to Cobalt 100 based instances (Dpsv6)
    - A machine with [Docker](/install-guides/docker/) installed
    - Familiarity with distributed computing concepts and the [Apache Spark architecture](https://spark.apache.org/docs/latest/)

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T02:07:30Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 009f2219f1b949be39b4a1dd43a5e4c1ceb5bb273d9a11c3c155315160d593ac
  summary_generated_at: '2026-06-02T05:12:43Z'
  summary_source_hash: 009f2219f1b949be39b4a1dd43a5e4c1ceb5bb273d9a11c3c155315160d593ac
  faq_generated_at: '2026-06-03T02:07:30Z'
  faq_source_hash: 009f2219f1b949be39b4a1dd43a5e4c1ceb5bb273d9a11c3c155315160d593ac
  summary: >-
    Learn how to deploy and validate Apache Spark on Microsoft Azure Cobalt 100 (Arm-based) virtual
    machines using Azure Linux 3.0. You will provision an Arm64 VM via the Azure portal, choose
    between running Spark in an Azure Linux 3.0 Docker container or on a custom-image VM, and
    install the required components (Java, Python, and Spark). The path includes a simple PySpark
    functional test and guidance to run a suite of Spark benchmarks to understand performance
    on the Cobalt 100 platform. This advanced path targets developers migrating Spark workloads
    from x86_64 to Arm. Prerequisites include an Azure account with access to Cobalt 100 (Dpsv6),
    a machine with Docker installed, and familiarity with distributed computing and the Apache
    Spark architecture.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need a Microsoft Azure account with access to Cobalt 100 instances (Dpsv6), a machine
      with Docker installed, and familiarity with distributed computing concepts and the Apache
      Spark architecture.
  - question: How do I make sure I’m creating the correct Arm64 VM in Azure?
    answer: >-
      Use the Azure portal to create a virtual machine and select a Cobalt 100-based Arm64 size
      such as Dpsv6. Then choose the image appropriate for your deployment as shown in the steps.
  - question: Should I deploy Spark in an Azure Linux 3.0 Docker container or on a custom-image
      VM?
    answer: >-
      This Learning Path supports both options on Arm64. Pick one approach and follow the corresponding
      instructions for an Azure Linux 3.0 container or a VM created from a custom Azure Linux
      3.0 image.
  - question: Which packages do I install before setting up Spark, and how do I verify Java?
    answer: >-
      Install Java 17 (runtime and devel), Python 3, pip, and common tools such as git and maven
      using tdnf as shown. Verify the installation by running java -version; it should report
      OpenJDK 17.
  - question: How do I validate that Spark is working after installation?
    answer: >-
      Create the provided test_spark.py, run it as directed in the steps, and confirm that df.show()
      prints the sample rows. This verifies that Spark can initialize, process a small job, and
      exit on the Arm64 environment.
# END generated_summary_faq

author: Pareena Verma

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
cloud_service_providers:
  - Microsoft Azure

armips:
    - Neoverse

tools_software_languages:
    - Apache Spark
    - Python
    - Docker
 
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
      title: Docker overview
      link: https://docs.docker.com/get-started/overview/
      type: documentation
  - resource:
      title: Spark official website and documentation
      link: https://spark.apache.org/
      type: documentation
  - resource:
      title: Hadoop official website
      link: https://hadoop.apache.org/
      type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

