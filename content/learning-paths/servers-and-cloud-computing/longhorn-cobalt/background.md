---
title: Understand Longhorn on Azure Cobalt 100
description: Understand how Longhorn provides Kubernetes persistent storage on Azure Cobalt 100 Arm64 virtual machines.

weight: 2

layout: "learningpathall"
---

## Why run Longhorn on Azure Cobalt 100

Longhorn on Arm-based Azure Cobalt 100 processors provides lightweight, Kubernetes-native distributed storage for cloud-native workloads running on Arm64 infrastructure.

Azure Cobalt 100 processors deliver dedicated physical cores per vCPU, providing predictable and consistent performance for Kubernetes storage workloads. This architecture complements Longhorn’s distributed block storage model and delivers stable storage performance for stateful applications running on Kubernetes.

Longhorn enables persistent storage for Kubernetes workloads such as databases, analytics platforms, monitoring stacks, and stateful cloud-native applications running on Azure Cobalt 100 Arm64 virtual machines.

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

To learn more, see the official [Longhorn documentation](https://longhorn.io/docs/).

Longhorn provides several important capabilities for Kubernetes storage management:

- Persistent volumes: Dynamically provisions Kubernetes Persistent Volumes for stateful workloads.
- Distributed storage: Replicates and manages block storage volumes across Kubernetes nodes.
- CSI integration: Integrates natively with Kubernetes using the Container Storage Interface.
- Snapshot and backup support: Supports volume snapshots and backup operations for Kubernetes workloads.
- Stateful workload support: Enables databases, monitoring stacks, and analytics applications to run with persistent storage.

Longhorn is widely used in Kubernetes environments to provide lightweight and reliable storage without requiring external SAN or NAS infrastructure.

In this Learning Path, you'll deploy Longhorn on an Azure Cobalt 100 Arm64 virtual machine using K3s Kubernetes. You'll configure Longhorn for a single-node Kubernetes cluster, create persistent volumes, validate storage persistence, and benchmark storage performance using fio.

## What you've learned and what's next

You now understand why Azure Cobalt 100 and Longhorn are a strong combination for Kubernetes-native persistent storage on Arm64 infrastructure.

Next, you'll create a virtual machine with Azure Cobalt 100.
