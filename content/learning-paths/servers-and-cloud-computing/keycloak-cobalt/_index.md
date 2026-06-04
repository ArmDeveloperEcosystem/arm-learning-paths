---
title: Deploy Keycloak on Azure Cobalt 100 Arm64 virtual machines for identity and access management

draft: true
cascade:
    draft: true
    
description: Learn how to install and configure Keycloak on an Azure Cobalt 100 Arm64 virtual machine, integrate it with PostgreSQL, configure OAuth2/OpenID Connect authentication, and secure applications using centralized identity management.

minutes_to_complete: 90

who_is_this_for: This is an introductory topic for developers, DevOps engineers, platform engineers, and cloud architects who want to deploy centralized authentication and identity management using Keycloak on Arm-based cloud environments.

learning_objectives:
    - Install and configure Keycloak on Azure Cobalt 100 Arm64 virtual machines
    - Configure PostgreSQL as the backend database for Keycloak
    - Configure realms, users, and OAuth2/OpenID Connect clients
    - Integrate a Flask application with Keycloak authentication
    - Validate OAuth2/OpenID Connect authentication workflows

prerequisites:
  - A [Microsoft Azure account](https://azure.microsoft.com/) with access to Cobalt 100 based instances (Dpsv6)
  - Basic knowledge of Linux command-line operations
  - Familiarity with SSH and remote server access
  - Basic understanding of authentication, OAuth2, and identity management concepts

author: Pareena Verma

### Tags
skilllevels: Introductory
subjects: Containers and Virtualization
cloud_service_providers:
  - Microsoft Azure

armips:
    - Neoverse

tools_software_languages:
    - Keycloak
    - PostgreSQL
    - Flask
    - Python
    - Java

operatingsystems:
    - Linux

further_reading:
  - resource:
      title: Keycloak Official Website
      link: https://www.keycloak.org/
      type: website
  - resource:
      title: Keycloak Documentation
      link: https://www.keycloak.org/documentation
      type: documentation
  - resource:
      title: OAuth 2.0 Framework
      link: https://oauth.net/2/
      type: documentation
  - resource:
      title: OpenID Connect Documentation
      link: https://openid.net/connect/
      type: documentation
  - resource:
      title: Azure Cobalt 100 processors
      link: https://techcommunity.microsoft.com/blog/azurecompute/announcing-the-preview-of-new-azure-vms-based-on-the-azure-cobalt-100-processor/4146353
      type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---
