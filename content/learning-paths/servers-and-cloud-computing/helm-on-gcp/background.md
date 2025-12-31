---
title: Get started with Helm on Google Axion C4A (Arm-based)

weight: 2

layout: "learningpathall"
---

## Explore Google Axion C4A instances in Google Cloud

Google Axion C4A is a family of Arm-based virtual machines built on Google’s custom Axion CPU, which is based on Arm Neoverse-V2 cores. Designed to deliver high performance with improved energy efficiency, these virtual machines offer strong performance for modern cloud workloads such as CI/CD pipelines, microservices, media processing, and general-purpose applications.

The C4A series provides an Arm-based alternative to x86 virtual machines, enabling developers to evaluate cost, performance, and efficiency trade-offs in Google Cloud. For Kubernetes users, Axion C4A instances provide a practical way to run Arm-native clusters and validate tooling such as Helm on modern cloud infrastructure.

To learn more about Google Axion, see the Google blog [Introducing Google Axion Processors, our new Arm-based CPUs](https://cloud.google.com/blog/products/compute/introducing-googles-new-arm-based-cpu).

## Explore Helm

Helm is the package manager for Kubernetes. It simplifies application deployment, upgrades, rollbacks, and lifecycle management by packaging Kubernetes resources into reusable charts.

Helm runs as a lightweight CLI that interacts directly with the Kubernetes API. Because it is architecture-agnostic, it works consistently across x86 and Arm64 clusters, including those running on Google Axion C4A instances.

In this Learning Path, you use Helm to deploy and manage applications on an Arm-based Kubernetes environment and verify common workflows such as install, upgrade, and uninstall operations.

For more information, see the [Helm website](https://helm.sh/).
