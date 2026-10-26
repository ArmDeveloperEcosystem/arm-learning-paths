---
title: Deploy Keycloak on Azure Cobalt 100-based Arm64 virtual machines for identity and access management

description: Learn how to install and configure Keycloak on an Azure Cobalt 100 Arm64 virtual machine, integrate it with PostgreSQL, configure OAuth2/OpenID Connect authentication, and secure applications using centralized identity management.

minutes_to_complete: 90

who_is_this_for: This is an introductory topic for developers, DevOps engineers, platform engineers, and cloud architects who want to deploy centralized authentication and identity management using Keycloak on Arm-based cloud environments.

learning_objectives:
    - Install and configure Keycloak on Azure Cobalt 100-based Arm64 virtual machines (VMs).
    - Configure PostgreSQL as the backend database for Keycloak.
    - Configure realms, users, and OAuth2/OpenID Connect clients.
    - Integrate a Flask application with Keycloak authentication.
    - Validate OAuth2/OpenID Connect authentication workflows.

prerequisites:
  - A [Microsoft Azure account](https://azure.microsoft.com/) with access to Cobalt 100-based instances (Dpsv6)
  - Basic knowledge of Linux command-line operations
  - Familiarity with SSH and remote server access
  - Basic understanding of authentication, OAuth2, and identity management concepts

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-09-15T21:23:00Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 9f5a5aa286f27fc31143675bf3658434b56dc80be9dfcf3dfa32292a6d55ab1b
  summary_generated_at: '2026-09-15T21:23:00Z'
  summary_source_hash: 9f5a5aa286f27fc31143675bf3658434b56dc80be9dfcf3dfa32292a6d55ab1b
  faq_generated_at: '2026-09-15T21:23:00Z'
  faq_source_hash: 9f5a5aa286f27fc31143675bf3658434b56dc80be9dfcf3dfa32292a6d55ab1b
  summary: >-
    You'll deploy Keycloak on an Azure Cobalt 100 Arm64 VM with PostgreSQL and a Flask OAuth2
    demo. First, you'll create a Dpsv6 VM, restrict network access to required services, and install the
    needed packages. You'll configure a realm, users, and an OpenID Connect client. Then, you'll
    test the admin console and Flask login flow to verify redirects and the authenticated
    session.
  faqs:
  - question: How do I know that the Azure VM is ready before installing Keycloak?
    answer: >-
      Verify that you can connect to the instance over SSH and update the system packages. 
  - question: Which inbound firewall rules should I add in Azure?
    answer: >-
      Add inbound rules for ports `8080`, `9000`, and `5000`. Test from a browser using the VM’s
      public IP and the configured ports to confirm access.
  - question: What should I check if Keycloak fails to start with database errors?
    answer: >-
      Ensure that PostgreSQL is installed, running, and reachable on the VM. Check that the Keycloak
      database settings match the PostgreSQL database, user, and connection details that you configured.
  - question: How do I confirm my realm, user, and client configuration is correct?
    answer: >-
      Open the Flask application and start the login flow. You should be redirected to the Keycloak
      login page and, after authenticating, returned to the Flask app with an authenticated session.
  - question: Can I run Keycloak and the Flask demo on the same VM?
    answer: >-
      Yes. You'll install both on the Azure Cobalt 100-based VM and expose them through separate
      inbound rules in the network security group.
# END generated_summary_faq

author: Pareena Verma

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Web
platforms:
  - Microsoft Azure Cobalt

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
