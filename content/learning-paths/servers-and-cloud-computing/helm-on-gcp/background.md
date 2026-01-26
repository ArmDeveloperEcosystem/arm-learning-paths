---
title: Get started with Helm on Google Axion C4A (Arm-based)

weight: 2

layout: "learningpathall"
---

## Explore Google Axion C4A instances in Google Cloud

Google Axion C4A is a family of Arm-based VMs built on Google's custom Axion processors, which use Arm Neoverse-V2 cores. These VMs deliver high performance with improved energy efficiency for modern cloud workloads such as CI/CD pipelines, microservices, media processing, and general-purpose applications.

The C4A series provides an Arm-based alternative to x86 VMs, enabling developers to evaluate cost, performance, and efficiency trade-offs in Google Cloud. For Kubernetes users, C4A instances provide a practical way to run Arm-native clusters and validate tooling such as Helm on modern cloud infrastructure.

To learn more about Google Axion, see the Google blog [Introducing Google Axion Processors, our new Arm-based CPUs](https://cloud.google.com/blog/products/compute/introducing-googles-new-arm-based-cpu).

## Explore Helm

Helm is the package manager for Kubernetes. It simplifies application deployment, upgrades, rollbacks, and lifecycle management by packaging Kubernetes resources into reusable charts.

As a lightweight CLI, Helm interacts directly with the Kubernetes API. Its architecture-agnostic design ensures consistent behavior across x86 and Arm64 clusters, including those running on Google Axion C4A instances.

In this Learning Path you'll use Helm to deploy and manage applications on an Arm-based Kubernetes environment, verifying common workflows such as install, upgrade, and uninstall operations.

For more information, see the [Helm website](https://helm.sh/).
