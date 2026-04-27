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

## Two deployment approaches

This Learning Path covers two ways to deploy OpenStack on an Azure Cobalt 100 Arm64 VM. Each approach has different requirements and suits a different use case.

**DevStack** is a script-based installer designed for development and testing. It runs all OpenStack services directly on the host OS and is the fastest way to get a working OpenStack environment. It is not suitable for production.

**Kolla-Ansible** runs every OpenStack service as a Docker container and is the recommended approach for reproducible, production-grade deployments. It takes longer to set up but is easier to manage, upgrade, and extend.

| Feature | DevStack | Kolla-Ansible |
|---------|----------|---------------|
| Purpose | Development and testing | Production-grade deployment |
| Deployment method | Shell scripts on host OS | Docker containers via Ansible |
| Setup time | ~20 minutes | ~60 minutes |
| Arm64 images required | No | Yes (Debian-based) |
| Networking | Simplified (Neutron disabled) | Full Neutron with OVS |
| Horizon dashboard | Yes | Yes |

Each approach runs on its own dedicated VM. Do not run both on the same virtual machine — they use the same ports and will conflict.

## VM requirements for each deployment

Because the two approaches have different infrastructure requirements, this Learning Path uses two separate Azure VMs.

| | VM 1 — DevStack | VM 2 — Kolla-Ansible |
|-|-----------------|----------------------|
| vCPUs | 4 | 4 (8 recommended) |
| RAM | 8 GB | 16 GB recommended |
| OS disk | 80 GB | 100 GB |
| Data disk | None | 32 GB (for Cinder/Docker) |
| NICs | 1 (`eth0` with IP) | 2 (`eth0` management + `eth1` external) |
| OS | Ubuntu 24.04 | Ubuntu 24.04 |

You'll create VM 1 first, complete the DevStack deployment, then create and configure VM 2 before the Kolla-Ansible deployment.
