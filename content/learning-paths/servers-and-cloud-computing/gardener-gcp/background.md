---
title: Get started with Gardener on Google Axion C4A (Arm Neoverse-V2)

weight: 2

layout: "learningpathall"
---

## Explore Google Axion C4A Arm instances

Google Axion C4A is a family of Arm-based virtual machines built on Google's custom Axion CPU, which uses Arm Neoverse-V2 cores. Designed for high-performance and energy-efficient computing, these virtual machines deliver strong performance for modern cloud workloads such as CI/CD pipelines, microservices, media processing, and general-purpose applications.

The C4A series provides a cost-effective alternative to x86 virtual machines while leveraging the scalability and performance benefits of the Arm architecture in Google Cloud.

To learn more about Google Axion, see the Google blog [Introducing Google Axion Processors, our new Arm-based CPUs](https://cloud.google.com/blog/products/compute/introducing-googles-new-arm-based-cpu).

## Explore Gardener

Gardener is an open-source, Kubernetes-native system for managing and operating Kubernetes clusters at scale. It enables automated creation, updates, healing, and deletion of clusters across multiple cloud providers and on-premises environments.

Gardener uses Kubernetes APIs and Custom Resource Definitions (CRDs) to declaratively manage clusters in a cloud-agnostic way. It follows a Garden–Seed–Shoot architecture to separate control planes from workload clusters:

- Garden is the central management cluster that runs Gardener components.
- Seed clusters are intermediary clusters that host Shoot control planes.
- Shoot clusters are the workload clusters managed by Gardener for end users.

Organizations use Gardener to build and operate Kubernetes clusters at scale, creating reliable internal developer platforms that serve thousands of teams.

To learn more, visit the [Gardener website](https://gardener.cloud/) and explore the [Gardener documentation](https://gardener.cloud/docs/).

## Summary and what's next

You now understand Google Axion C4A's capabilities as a cost-effective Arm-based platform and how Gardener automates Kubernetes cluster management at scale. Together, these technologies provide a powerful foundation for running enterprise Kubernetes workloads on Arm infrastructure.

In the next sections, you'll provision your Arm-based VM on Google Cloud, install Gardener, and deploy your first clusters. You're ready to get started!
