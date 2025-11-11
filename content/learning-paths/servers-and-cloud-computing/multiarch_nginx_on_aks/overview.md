---
title: Start your journey with Arm and x86 nginx workloads on a single Kubernetes cluster
weight: 2
### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Project overview

Arm processors are transforming cloud infrastructure, offering improved performance per watt and cost efficiency for web server workloads. In this Learning Path, you'll deploy [nginx](https://nginx.org/) on both Arm and x86 architectures within a single Kubernetes cluster on Azure AKS.

You'll create a cluster with both Arm-based and x86 nodes, which lets you deploy the same nginx workload on different architectures. This setup allows you to compare how nginx performs on each architecture and understand the practical aspects of running mixed workloads in Kubernetes.

## Why deploy nginx on both Arm and x86 nodes in Kubernetes?

Many developers start their Arm journey by adding Arm-based nodes to existing x86 Kubernetes clusters. 

This approach offers several advantages:

- Gradual migration: you can leverage your existing Kubernetes expertise to add Arm nodes without disrupting current x86 workloads.
- Container compatibility: multi-architecture container images allow the same nginx deployment to run on both architectures with minimal configuration changes.
- Performance comparison: running both architectures in the same cluster provides an ideal environment for benchmarking Arm versus x86 performance under identical conditions.

This Learning Path walks you through how to create an initial AKS environment and install nginx on x86.  From there, you'll add Arm-based nodes running the same exact workload.  You'll see how to run simple tests to verify functionality, and then run performance testing to better understand the performance characteristics of each architecture.