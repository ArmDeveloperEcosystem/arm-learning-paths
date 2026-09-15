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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-09-15T21:19:31Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 5d5baa4d8c9a24cac97280c7a9316eaa3194ef6a6791ec0594d7daa04f1e45a7
  summary_generated_at: '2026-09-15T21:19:31Z'
  summary_source_hash: 5d5baa4d8c9a24cac97280c7a9316eaa3194ef6a6791ec0594d7daa04f1e45a7
  faq_generated_at: '2026-09-15T21:19:31Z'
  faq_source_hash: 5d5baa4d8c9a24cac97280c7a9316eaa3194ef6a6791ec0594d7daa04f1e45a7
  summary: >-
    You deploy Jenkins on Arm-based cloud servers and validate an Arm-native CI/CD setup.
    You provision an Azure Cobalt 100 VM, open port 8080, install Jenkins LTS with OpenJDK
    17, and verify the aarch64 runtime. You can then run Arm-native pipelines, including
    Docker-based jobs when needed, and configure a Google Cloud firewall rule for Axion C4A
    access.
  faqs:
  - question: Which Azure VM series should I choose for a Cobalt 100 deployment?
    answer: >-
      Use the Dpsv6 size series and create the instance from the Azure portal as shown in the
      steps. Other creation methods are possible but are not covered here.
  - question: How do I know Jenkins installed correctly on the Azure Ubuntu Arm64 VM?
    answer: >-
      Jenkins runs as a system service and is accessible on port 8080. You should be able to load
      the Jenkins UI and confirm it uses Java 17 on an Arm64 (aarch64) host.
  - question: What should I check if I can’t reach the Jenkins UI on port 8080?
    answer: >-
      Verify that the Jenkins service is running and that an inbound TCP rule for port 8080 exists
      in the Azure NSG attached to the VM’s network interface or subnet. Also confirm you are
      using the correct public IP and port.
  - question: Where do I configure the cloud network access for Jenkins in this workflow?
    answer: >-
      Create the Azure NSG inbound TCP rule for port 8080 in the Azure portal. For an Axion C4A
      instance on Google Cloud, create the inbound firewall rule in the Google Cloud Console.
  - question: How do I confirm the environment is Arm-native before running pipelines or Docker-based
      jobs?
    answer: >-
      Check that the system reports Arm64 (aarch64) and that Jenkins runs with OpenJDK 17. Ensure
      port 8080 is open so the controller is reachable before you start pipelines.
# END generated_summary_faq

author: Pareena Verma

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

##### Tags
skilllevels: Advanced
subjects: CI-CD
platforms:
  - Microsoft Azure Cobalt
  - Google Axion

armips:
    - Neoverse

tools_software_languages:
  - Jenkins
  - OpenJDK 17
  - Docker
  - Groovy

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
