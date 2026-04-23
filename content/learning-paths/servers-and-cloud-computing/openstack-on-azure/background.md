---
title: "Overview of Azure Cobalt 100 and OpenStack"
weight: 2

layout: "learningpathall"
---

## Azure Cobalt 100 Arm-based processor

Azure’s Cobalt 100 is Microsoft’s first-generation, in-house Arm-based processor. Built on Arm Neoverse N2, Cobalt 100 is a 64-bit CPU that delivers strong performance and energy efficiency for cloud-native, scale-out Linux workloads such as web and application servers, data analytics, open-source databases, and caching systems. Running at 3.4 GHz, Cobalt 100 allocates a dedicated physical core for each vCPU, which helps ensure consistent and predictable performance.

To learn more, see the Microsoft blog [Announcing the preview of new Azure VMs based on the Azure Cobalt 100 processor](https://techcommunity.microsoft.com/blog/azurecompute/announcing-the-preview-of-new-azure-vms-based-on-the-azure-cobalt-100-processor/4146353).

## OpenStack

OpenStack is an open-source cloud computing platform used to build and manage Infrastructure-as-a-Service (IaaS) environments.

It enables users to provision and manage compute, storage, and networking resources via APIs and dashboards, similar to those of public cloud providers.

OpenStack is widely used for:

* Private cloud deployments
* Hybrid cloud environments
* Edge and telecom infrastructure
* Development and testing platforms

OpenStack runs efficiently on Arm-based architectures such as Azure Cobalt 100, enabling cost-effective and scalable cloud environments.

## Key services in OpenStack

OpenStack is composed of modular services that handle different aspects of cloud infrastructure:

* **Keystone (Identity):** Authentication and authorization service
* **Nova (Compute):** Manages virtual machine lifecycle
* **Glance (Image):** Stores and manages VM images
* **Neutron (Networking):** Provides networking and connectivity
* **Cinder (Block Storage):** Persistent block storage for instances
* **Horizon (Dashboard):** Web-based user interface for managing resources


## OpenStack architecture components

A typical OpenStack deployment consists of:

* **Controller Node:** Runs core services such as API, scheduler, and database
* **Compute Node:** Hosts virtual machines using hypervisors
* **Networking (Neutron):** Handles virtual networking, bridges, and routing
* **Storage Services:** Provide block and object storage

In this learning path, OpenStack is deployed using **Kolla-Ansible**, which runs services as containers for easier management.


## Use cases

OpenStack is widely used across industries:

* **Private Cloud Infrastructure:** Build internal cloud platforms
* **Dev/Test Environments:** Rapid provisioning of virtual machines
* **Edge Computing:** Lightweight deployments on Arm-based hardware
* **Telco Cloud:** Network function virtualization (NFV)
* **Research and HPC:** Scalable compute environments

## Learn more about OpenStack

To learn more about OpenStack, see:

- [OpenStack Official Website](https://www.openstack.org/)  
- [OpenStack Documentation](https://docs.openstack.org/)  
- [OpenStack GitHub Repository](https://github.com/openstack)  
- [Kolla-Ansible Documentation](https://docs.openstack.org/kolla-ansible/latest/)  

## What you will learn

In this learning path, you will:

* Deploy OpenStack on an Azure Cobalt 100 Arm64 virtual machine
* Configure core OpenStack services (Keystone, Nova, Neutron, Glance, Cinder)
* Deploy containerized OpenStack using Kolla-Ansible
* Set up networking and storage for OpenStack
* Launch and manage virtual machine instances
* Access and manage resources using CLI and Horizon dashboard
