---
title: Deploy and validate Jenkins on Arm cloud servers

minutes_to_complete: 30   

who_is_this_for: This Learning Path is for software developers deploying and optimizing Jenkins workloads on Arm Linux environments, specifically on Microsoft Azure Cobalt 100 processors and Google Cloud C4A virtual machines powered by Axion processors.

description: Deploy Jenkins on Azure Cobalt 100 and Google Axion virtual machines, validate installation, and execute Arm-native CI/CD pipelines including Docker workflows.

learning_objectives: 
    - Provision an Azure Arm64 virtual machine using the Azure console with Ubuntu Pro 24.04 LTS
    - Provision an Arm-based SUSE Linux virtual machine on Google Cloud (C4A with Axion processors)
    - Install Jenkins LTS with OpenJDK 17 on an Arm64 virtual machine
    - Validate Jenkins installation through service checks, UI access, and Arm-native pipeline execution
    - Execute Arm-native Jenkins pipelines to verify correct runtime behavior
    - Implement CI use cases on Arm64, including Docker-based pipelines

prerequisites:
    - A [Microsoft Azure](https://azure.microsoft.com/) account with access to Cobalt 100-based instances (Dpsv6)
    - A [Google Cloud Platform](https://cloud.google.com/) account with access to Arm-based virtual machine instances
    - Basic understanding of Linux command line
    - Familiarity with CI/CD concepts and [Jenkins fundamentals](https://www.jenkins.io/doc/book/pipeline/)

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false
# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-05-06T17:17:57Z'
  generator: template
  source_hash: 525d893a796e8e4eb5cc7a9d5996bd7d55a35f8fe413f87b9a275a214d77626f
  summary: >-
    Deploy Jenkins on Azure Cobalt 100 and Google Axion virtual machines, validate installation,
    and execute Arm-native CI/CD pipelines including Docker workflows. It is designed for software
    developers deploying and optimizing Jenkins workloads on Arm Linux environments, specifically
    on Microsoft Azure Cobalt 100 processors and Google Cloud C4A virtual machines powered by
    Axion processors. By the end, you will be able to provision an Azure Arm64 virtual machine
    using the Azure console with Ubuntu Pro 24.04 LTS, provision an Arm-based SUSE Linux virtual
    machine on Google Cloud (C4A with Axion processors), and install Jenkins LTS with OpenJDK
    17 on an Arm64 virtual machine. It focuses on tools and technologies such as Jenkins, OpenJDK
    17, Docker, and Groovy (Jenkins Pipeline), Linux environments, Arm platforms including Neoverse,
    and cloud platforms such as Microsoft Azure and Google Cloud. The main steps cover Technology
    stack overview, Create an Arm-based virtual machine using Microsoft Cobalt 100, Create a firewall
    rule on Azure, Install Jenkins on Azure Ubuntu Arm64 virtual machine, and Create a firewall
    rule on GCP.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will provision an Azure Arm64 virtual machine using the Azure console with Ubuntu Pro
      24.04 LTS, provision an Arm-based SUSE Linux virtual machine on Google Cloud (C4A with Axion
      processors), and install Jenkins LTS with OpenJDK 17 on an Arm64 virtual machine. Deploy
      Jenkins on Azure Cobalt 100 and Google Axion virtual machines, validate installation, and
      execute Arm-native CI/CD pipelines including Docker workflows.
  - question: Who is this Learning Path for?
    answer: >-
      This Learning Path is for software developers deploying and optimizing Jenkins workloads
      on Arm Linux environments, specifically on Microsoft Azure Cobalt 100 processors and Google
      Cloud C4A virtual machines powered by Axion processors.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: A [Microsoft Azure](https://azure.microsoft.com/)
      account with access to Cobalt 100-based instances (Dpsv6); A [Google Cloud Platform](https://cloud.google.com/)
      account with access to Arm-based virtual machine instances; Basic understanding of Linux
      command line; Familiarity with CI/CD concepts and [Jenkins fundamentals](https://www.jenkins.io/doc/book/pipeline/).
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including Jenkins, OpenJDK 17, Docker, and Groovy (Jenkins
      Pipeline), Linux environments, Arm platforms such as Neoverse, and cloud platforms such
      as Microsoft Azure and Google Cloud.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Technology stack overview, Create an Arm-based virtual
      machine using Microsoft Cobalt 100, Create a firewall rule on Azure, Install Jenkins on
      Azure Ubuntu Arm64 virtual machine, and Create a firewall rule on GCP.
# END generated_summary_faq

author: Pareena Verma

##### Tags
skilllevels: Advanced
subjects: CI-CD
cloud_service_providers:
  - Microsoft Azure
  - Google Cloud

armips:
    - Neoverse

tools_software_languages:
  - Jenkins
  - OpenJDK 17
  - Docker
  - Groovy (Jenkins Pipeline)

operatingsystems:
    - Linux

further_reading:
    - resource:
        title: Jenkins Official Documentation
        link: https://www.jenkins.io/doc/
        type: documentation
    - resource:
        title: Jenkins Pipeline Syntax
        link: https://www.jenkins.io/doc/book/pipeline/syntax/
        type: documentation
    - resource:        
        title: Jenkins on Azure
        link: https://learn.microsoft.com/en-us/azure/developer/jenkins/
        type: documentation
    - resource:        
        title: Jenkins on Google Cloud
        link: https://cloud.google.com/jenkins
        type: documentation

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---

