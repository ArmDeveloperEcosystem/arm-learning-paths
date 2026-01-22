---
title: Get started with Argo CD on Google Axion C4A (Arm-based)

weight: 2

layout: "learningpathall"
---

## Explore Google Axion C4A instances in Google Cloud

Google Axion C4A is a family of **Arm-based virtual machines** powered by Google’s custom **Axion processors**, built on **Arm Neoverse V2** cores. These instances are designed to deliver high performance with improved energy efficiency for modern cloud workloads, including CI/CD pipelines, microservices, GitOps workflows, and cloud-native applications.

The C4A series provides a production-ready Arm alternative to x86 VMs, enabling teams to evaluate performance, cost, and efficiency trade-offs on Google Cloud. For Kubernetes users, Axion C4A instances are particularly well suited for running **Arm-native GKE clusters** and validating cloud-native tooling such as **Argo CD** on modern infrastructure.

To learn more about Google Axion, see the Google blog:
[Introducing Google Axion Processors, our new Arm-based CPUs](https://cloud.google.com/blog/products/compute/introducing-googles-new-arm-based-cpu).


## Explore Argo CD

Argo CD is a **declarative, GitOps-based continuous delivery tool for Kubernetes**. It continuously monitors application manifests stored in Git repositories and ensures that the live cluster state matches the desired state defined in Git.

Instead of manually applying manifests, Argo CD treats Git as the **single source of truth**. Any change committed to Git is automatically detected, synchronized, and enforced on the cluster. This model provides strong guarantees around consistency, traceability, and repeatability.

Argo CD runs natively on Kubernetes and is **architecture-agnostic**, making it fully compatible with **Arm64-based GKE clusters running on Google Axion C4A**. All core Argo CD components and common application images support `linux/arm64`, enabling fully native GitOps workflows on Arm infrastructure.

In this learning path, you will use Argo CD to:

* Deploy applications declaratively from Git
* Enable automated synchronization and self-healing
* Observe application health and sync status via the UI
* Validate GitOps workflows on an Arm-based Kubernetes platform

For more information, see the official Argo CD documentation:
[https://argo-cd.readthedocs.io](https://argo-cd.readthedocs.io).
