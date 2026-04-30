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
