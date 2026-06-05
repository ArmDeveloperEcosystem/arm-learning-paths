---
title: Understand OpenEBS on Azure Cobalt 100
weight: 2

layout: "learningpathall"
---

## Why run OpenEBS on Azure Cobalt 100

OpenEBS on Arm-based Azure Cobalt 100 processors provides lightweight, Kubernetes-native persistent storage for cloud-native workloads. Azure Cobalt 100 processors deliver dedicated physical cores per vCPU, enabling consistent and predictable performance for Kubernetes storage operations and stateful applications.

OpenEBS integrates directly with Kubernetes and dynamically provisions Persistent Volumes for applications using Container Storage Interface (CSI) drivers and storage engines. Running OpenEBS on Azure Cobalt 100 enables efficient Arm64-native Kubernetes storage deployments optimized for lightweight cloud-native environments.

## Azure Cobalt 100 Arm-based processor

Azure’s Cobalt 100 is Microsoft’s first-generation, in-house Arm-based processor. Built on Arm Neoverse N2, Cobalt 100 is a 64-bit CPU that delivers strong performance and energy efficiency for cloud-native, scale-out Linux workloads. These workloads include web and application servers, data analytics, open-source databases, and caching systems. Running at 3.4 GHz, Cobalt 100 allocates a dedicated physical core for each vCPU, ensuring consistent and predictable performance.

To learn more, see the Microsoft blog [Announcing the preview of new Azure VMs based on the Azure Cobalt 100 processor](https://techcommunity.microsoft.com/blog/azurecompute/announcing-the-preview-of-new-azure-vms-based-on-the-azure-cobalt-100-processor/4146353).

## How OpenEBS improves Kubernetes storage

OpenEBS is an open-source, Kubernetes-native storage platform designed for stateful workloads running inside Kubernetes clusters. Unlike traditional external storage systems, OpenEBS runs completely inside Kubernetes and dynamically provisions storage volumes directly through Kubernetes APIs.

OpenEBS enables applications to retain persistent data even after pods restart, reschedule, or recreate. This makes OpenEBS ideal for databases, analytics platforms, message queues, and other stateful cloud-native applications.

To learn more, see the official [OpenEBS documentation](https://openebs.io/docs).

OpenEBS provides key capabilities for Kubernetes-native storage management:

- Dynamic Provisioning: Automatically creates Persistent Volumes using Kubernetes Persistent Volume Claims (PVCs).
- Kubernetes-native Architecture: Runs entirely inside Kubernetes without requiring external storage appliances.
- Lightweight Local Storage: OpenEBS LocalPV uses node-local storage optimized for lightweight Kubernetes environments.
- CSI Integration: Integrates with Kubernetes Container Storage Interface (CSI) drivers for standard storage management.
- Stateful Workload Support: Enables persistent storage for databases, web applications, and distributed systems.

## Why OpenEBS LocalPV for this learning path

This learning path uses OpenEBS LocalPV because it is optimized for:

- Single-node Kubernetes clusters
- Arm64 environments
- Lightweight Kubernetes deployments
- Development and learning environments
- High-performance local storage provisioning

Advanced replicated storage engines such as Mayastor are designed for multi-node production environments and are intentionally excluded from this setup.

## Learning path overview

In this Learning Path, you'll deploy OpenEBS LocalPV on an Azure Cobalt 100 Arm64 virtual machine using a lightweight K3s Kubernetes cluster.

You'll learn how to:

- Install Kubernetes using K3s
- Deploy OpenEBS LocalPV
- Configure Kubernetes storage classes
- Create Persistent Volume Claims (PVCs)
- Deploy stateful applications
- Validate persistent storage functionality
- Expose Kubernetes applications externally using Azure networking

## What you've learned and what's next

You now understand why Azure Cobalt 100 and OpenEBS are a strong combination for lightweight Kubernetes-native persistent storage on Arm64 infrastructure.

Next, you'll create an Azure Cobalt 100 Arm64 virtual machine to host the Kubernetes cluster.
