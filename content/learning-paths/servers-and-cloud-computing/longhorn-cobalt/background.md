---
title: Understand Longhorn on Azure Cobalt 100
description: Understand how Longhorn provides Kubernetes persistent storage on Azure Cobalt 100 Arm64 virtual machines.

weight: 2

layout: "learningpathall"
---

## Why run Longhorn on Azure Cobalt 100

Longhorn on Arm-based Azure Cobalt 100 processors provides lightweight, Kubernetes-native, persistent distributed storage for cloud-native workloads running on Arm64 infrastructure.

Azure Cobalt 100 processors deliver dedicated physical cores per vCPU, providing predictable and consistent performance for Kubernetes storage workloads. This architecture complements Longhorn’s distributed block storage model and delivers stable storage performance for stateful applications running on Kubernetes.

You’ll use this architecture in the following sections to install Longhorn on K3s, create a Longhorn-backed PersistentVolume, and validate storage behavior with fio.

## Azure Cobalt 100 Arm-based processor

Azure’s Cobalt 100 is Microsoft’s first-generation, in-house Arm-based processor. Built on Arm Neoverse N2, Cobalt 100 is a 64-bit CPU that delivers strong performance and energy efficiency for cloud-native, scale-out Linux workloads. 

These workloads include:
- Kubernetes platforms
- Containerized applications
- Open-source databases 
- Data analytics systems
- Storage and caching platforms

Running at 3.4 GHz, Cobalt 100 allocates a dedicated physical core for each vCPU, ensuring predictable and consistent workload performance.

To learn more, see the Microsoft blog [Announcing the preview of new Azure VMs based on the Azure Cobalt 100 processor](https://techcommunity.microsoft.com/blog/azurecompute/announcing-the-preview-of-new-azure-vms-based-on-the-azure-cobalt-100-processor/4146353).

## How Longhorn provides Kubernetes storage

Longhorn is an open-source cloud-native distributed block storage platform designed specifically for Kubernetes environments.

It provides persistent storage volumes for Kubernetes workloads and enables applications to retain data independently of container or pod lifecycle events.

Longhorn integrates directly with Kubernetes through the Container Storage Interface (CSI) and provides dynamic volume provisioning, storage management, and persistent storage capabilities for stateful workloads.

Longhorn provides several important capabilities for Kubernetes storage management:

- Persistent volumes: Dynamically provisions Kubernetes persistent volumes for stateful workloads.
- Distributed storage: Replicates and manages block storage volumes across Kubernetes nodes.
- CSI integration: Integrates natively with Kubernetes using CSI.
- Snapshot and backup support: Supports volume snapshots and backup operations.
- Stateful workload support: Enables databases, monitoring stacks, and analytics applications to run with persistent storage.

It is widely used in Kubernetes environments to provide lightweight and reliable storage without requiring external Storage Area Network (SAN) or Network Attached Storage (NAS) infrastructure.

To learn more about Longhorn, see the official [Longhorn documentation](https://longhorn.io/docs/).

## What you've learned and what's next

You now understand why Azure Cobalt 100 and Longhorn are a strong combination for Kubernetes-native persistent storage on Arm64 infrastructure. You also learned about the Kubernetes storage management capabilities that Longhorn provides.

Next, you'll create a virtual machine with Azure Cobalt 100.
