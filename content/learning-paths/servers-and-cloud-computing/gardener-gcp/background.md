---
title: Getting started with Gardener on Google Axion C4A (Arm Neoverse-V2)

weight: 2

layout: "learningpathall"
---

## Google Axion C4A Arm instances in Google Cloud

Google Axion C4A is a family of Arm-based virtual machines built on Google’s custom Axion CPU, which is based on Arm Neoverse-V2 cores. Designed for high-performance and energy-efficient computing, these virtual machines offer strong performance for modern cloud workloads such as CI/CD pipelines, microservices, media processing, and general-purpose applications.

The C4A series provides a cost-effective alternative to x86 virtual machines while leveraging the scalability and performance benefits of the Arm architecture in Google Cloud.

To learn more about Google Axion, refer to the [Introducing Google Axion Processors, our new Arm-based CPUs](https://cloud.google.com/blog/products/compute/introducing-googles-new-arm-based-cpu) blog.

## Gardener

Gardener is an open-source, Kubernetes-native system for managing and operating Kubernetes clusters at scale. It enables automated creation, update, healing, and deletion of clusters across multiple cloud and on-prem providers.  

Gardener uses Kubernetes APIs and CRDs to declaratively manage clusters in a cloud-agnostic way. It follows a **Garden–Seed–Shoot** architecture to separate control planes from workload clusters.  

Gardener is widely used to build reliable internal developer platforms and operate thousands of Kubernetes clusters.

To learn more, visit the Gardener [official website](https://gardener.cloud/) and explore the [documentation](https://gardener.cloud/docs/).
