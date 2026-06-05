---
title: Understand how OpenEBS provides Kubernetes-native persistent storage on Azure 
weight: 2

layout: "learningpathall"
---

## Why run OpenEBS on Azure Cobalt 100

OpenEBS on Arm-based Azure Cobalt 100 processors provides lightweight, Kubernetes-native persistent storage for cloud-native workloads. Azure Cobalt 100 processors deliver dedicated physical cores per vCPU, enabling consistent and predictable performance for Kubernetes storage operations and stateful applications.

OpenEBS integrates directly with Kubernetes and dynamically provisions persistent volumes for applications using Container Storage Interface (CSI) drivers and storage engines. Running OpenEBS on Azure Cobalt 100 enables efficient Arm64-native Kubernetes storage deployments optimized for lightweight cloud-native environments.

## Azure Cobalt 100 Arm-based processor

Azure’s Cobalt 100 is Microsoft’s first-generation, in-house Arm-based processor. Built on Arm Neoverse N2, Cobalt 100 is a 64-bit CPU that delivers strong performance and energy efficiency for cloud-native, scale-out Linux workloads. 

Running at 3.4 GHz, Cobalt 100 allocates a dedicated physical core for each vCPU, ensuring consistent and predictable performance.

To learn more, see the Microsoft blog [Announcing the preview of new Azure VMs based on the Azure Cobalt 100 processor](https://techcommunity.microsoft.com/blog/azurecompute/announcing-the-preview-of-new-azure-vms-based-on-the-azure-cobalt-100-processor/4146353).

## How OpenEBS provides Kubernetes storage

OpenEBS is an open-source, Kubernetes-native storage platform designed for stateful workloads running inside Kubernetes clusters. Unlike traditional external storage systems, OpenEBS runs completely inside Kubernetes and dynamically provisions storage volumes directly through Kubernetes APIs.

OpenEBS allows applications to retain persistent data on a node even after pods restart, reschedule, or recreate. This makes OpenEBS ideal for databases, analytics platforms, message queues, and other stateful cloud-native applications.

OpenEBS provides key capabilities for Kubernetes-native storage management:

- Dynamic provisioning: Automatically creates persistent volumes using Kubernetes PersistentVolumeClaims (PVCs).
- Kubernetes-native architecture: Runs entirely inside Kubernetes without requiring external storage appliances.
- Lightweight local storage: OpenEBS LocalPV uses node-local storage optimized for lightweight Kubernetes environments.
- CSI integration: Integrates with Kubernetes CSI drivers for standard storage management.
- Stateful workload support: Enables persistent storage for databases, web applications, and distributed systems.

To learn more, see the official [OpenEBS documentation](https://openebs.io/docs).

## Why use OpenEBS LocalPV 

You'll use OpenEBS LocalPV in this Learning Path because it's optimized for:

- Single-node Kubernetes clusters
- Arm64 environments
- Lightweight Kubernetes deployments
- Development and learning environments
- High-performance local storage provisioning

Advanced replicated storage engines such as Mayastor are designed for multi-node production environments and are intentionally excluded from this setup.

## What you've learned and what's next

You now understand why Azure Cobalt 100 and OpenEBS are a strong combination for lightweight Kubernetes-native persistent storage on Arm64 infrastructure. You've also learned how OpenEBS provides persistent storage and why OpenEBS LocalPV is suited for this Learning Path.

Next, you'll create an Azure Cobalt 100 Arm64 virtual machine to host the Kubernetes cluster.
