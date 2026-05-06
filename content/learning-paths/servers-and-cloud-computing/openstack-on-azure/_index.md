---
title: Deploy OpenStack on Azure Cobalt 100 Arm64 Virtual Machine
description: Deploy OpenStack on Azure Cobalt 100 Arm64 virtual machines using DevStack for development and Kolla-Ansible for containerized production deployments.

    
minutes_to_complete: 90

who_is_this_for: This learning path is designed for developers, DevOps engineers, and platform engineers who want to deploy and manage OpenStack on Arm-based cloud environments using Kolla-Ansible and DevStack.

learning_objectives:
   - Deploy OpenStack on Azure Cobalt 100 Arm64 virtual machines
   - Configure core OpenStack services (Keystone, Nova, Neutron, Glance, Cinder)
   - Deploy containerized OpenStack using Kolla-Ansible
   - Set up networking and storage for OpenStack
   - Launch and manage virtual machine instances
   - Access OpenStack using CLI and Horizon dashboard

prerequisites:
  - A [Microsoft Azure account](https://azure.microsoft.com/) with access to Cobalt 100 based instances (Dpsv6)
  - Basic knowledge of Linux command-line operations
  - Familiarity with SSH and remote server access
  - Basic understanding of cloud computing and virtualization concepts

generate_summary_faq: true

# rerun_summary: false
# rerun_faqs: false
# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-05-06T17:17:58Z'
  generator: template
  source_hash: 42628afa923ce6e89693bdfc72469ac0803610c3decb6cd4f36bd1a003874d0d
  summary: >-
    Deploy OpenStack on Azure Cobalt 100 Arm64 virtual machines using DevStack for development
    and Kolla-Ansible for containerized production deployments. It is designed for This learning
    path is designed for developers, DevOps engineers, and platform engineers who want to deploy
    and manage OpenStack on Arm-based cloud environments using Kolla-Ansible and DevStack. By
    the end, you will be able to deploy OpenStack on Azure Cobalt 100 Arm64 virtual machines,
    configure core OpenStack services (Keystone, Nova, Neutron, Glance, Cinder), and deploy containerized
    OpenStack using Kolla-Ansible. It focuses on tools and technologies such as OpenStack, Kolla-Ansible,
    DevStack, Python, and OpenStack CLI, Linux environments, Arm platforms including Neoverse,
    and cloud platforms such as Microsoft Azure. The main steps cover Understand Azure Cobalt
    100 and OpenStack, Create an Azure Cobalt 100 Arm64 virtual machine for DevStack, Deploy OpenStack
    on an Azure Cobalt 100 Arm64 virtual machine using DevStack, Prepare Azure Arm64 virtual machine
    for Kolla-Ansible, and Deploy OpenStack using Kolla-Ansible on an Azure Ubuntu Arm64 virtual
    machine.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will deploy OpenStack on Azure Cobalt 100 Arm64 virtual machines, configure core OpenStack
      services (Keystone, Nova, Neutron, Glance, Cinder), and deploy containerized OpenStack using
      Kolla-Ansible. Deploy OpenStack on Azure Cobalt 100 Arm64 virtual machines using DevStack
      for development and Kolla-Ansible for containerized production deployments.
  - question: Who is this Learning Path for?
    answer: >-
      This learning path is designed for developers, DevOps engineers, and platform engineers
      who want to deploy and manage OpenStack on Arm-based cloud environments using Kolla-Ansible
      and DevStack.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: A [Microsoft Azure account](https://azure.microsoft.com/)
      with access to Cobalt 100 based instances (Dpsv6); Basic knowledge of Linux command-line
      operations; Familiarity with SSH and remote server access; Basic understanding of cloud
      computing and virtualization concepts.
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including OpenStack, Kolla-Ansible, DevStack, Python, and
      OpenStack CLI, Linux environments, Arm platforms such as Neoverse, and cloud platforms such
      as Microsoft Azure.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Understand Azure Cobalt 100 and OpenStack, Create
      an Azure Cobalt 100 Arm64 virtual machine for DevStack, Deploy OpenStack on an Azure Cobalt
      100 Arm64 virtual machine using DevStack, Prepare Azure Arm64 virtual machine for Kolla-Ansible,
      and Deploy OpenStack using Kolla-Ansible on an Azure Ubuntu Arm64 virtual machine.
# END generated_summary_faq

author: Pareena Verma

### Tags
skilllevels: Introductory
subjects: Containers and Virtualization
cloud_service_providers:
  - Microsoft Azure

armips:
    - Neoverse

tools_software_languages:
    - OpenStack
    - Kolla-Ansible
    - DevStack
    - Python 
    - OpenStack CLI

operatingsystems:
    - Linux

further_reading:
  - resource:
        title: OpenStack Official Website
        link: https://www.openstack.org/
        type: website
  - resource:
      title: OpenStack Documentation
      link: https://docs.openstack.org/
      type: documentation
  - resource:
      title: Kolla-Ansible Documentation
      link: https://docs.openstack.org/kolla-ansible/latest/
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

