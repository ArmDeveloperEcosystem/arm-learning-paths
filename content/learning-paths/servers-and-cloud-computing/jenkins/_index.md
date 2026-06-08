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

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T01:14:54Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 525d893a796e8e4eb5cc7a9d5996bd7d55a35f8fe413f87b9a275a214d77626f
  summary_generated_at: '2026-06-02T04:11:14Z'
  summary_source_hash: 525d893a796e8e4eb5cc7a9d5996bd7d55a35f8fe413f87b9a275a214d77626f
  faq_generated_at: '2026-06-03T01:14:54Z'
  faq_source_hash: 525d893a796e8e4eb5cc7a9d5996bd7d55a35f8fe413f87b9a275a214d77626f
  summary: >-
    This Learning Path guides you through deploying Jenkins LTS on Arm-based cloud servers and
    validating Arm-native CI/CD pipelines. You provision an Azure Cobalt 100 (Dpsv6) virtual machine
    using the Azure console with Ubuntu Pro 24.04 LTS, and a Google Cloud C4A instance powered
    by Axion processors on SUSE Linux. You configure cloud firewall rules to expose Jenkins on
    TCP port 8080, install Jenkins with OpenJDK 17 on Arm64, and verify the setup via service
    checks, UI access, and pipeline execution. You then run Arm-native Jenkins pipelines, including
    Docker-based workflows. No additional prerequisites are listed beyond cloud account access,
    basic Linux skills, and familiarity with CI/CD and Jenkins fundamentals.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need an Azure account with access to Cobalt 100-based Dpsv6 instances and a Google Cloud
      account with access to Arm-based VMs. You should be comfortable with the Linux command line
      and basic CI/CD and Jenkins concepts.
  - question: Which VM types and operating systems are used in this path?
    answer: >-
      On Azure, you provision an Arm64 VM from the Dpsv6 (Cobalt 100) series using Ubuntu Pro
      24.04 LTS. On Google Cloud, you provision an Arm-based SUSE Linux VM on the C4A family powered
      by Axion processors.
  - question: How do I expose the Jenkins web UI to my browser?
    answer: >-
      Open TCP port 8080. On Azure, create an NSG rule for the VM’s network interface or subnet;
      on Google Cloud, create a VPC firewall rule allowing inbound TCP 8080 to the instance.
  - question: How do I validate that Jenkins installed correctly on the Azure VM?
    answer: >-
      Confirm the Jenkins service is running, then access the web UI on port 8080. The setup verifies
      Jenkins on Arm64 (aarch64) with Java 17 as part of the installation outcome.
  - question: What should I check if I plan to run Docker-based pipelines?
    answer: >-
      This path includes CI use cases that use Docker-based pipelines on Arm64. Follow the steps
      when they introduce Docker workflows and ensure your environment meets those requirements.
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

