---
title: Deploy and validate Jenkins on Arm cloud servers

minutes_to_complete: 30   

who_is_this_for: This Learning Path is for software developers deploying and optimizing Jenkins workloads on Arm Linux environments, specifically on Microsoft Azure Cobalt 100 processors and Google Cloud C4A virtual machines powered by Axion processors.

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

author: Pareena Verma

##### Tags
skilllevels: Advanced
subjects: CI-CD

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
