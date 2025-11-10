---
# User change
title: "Overview"

weight: 2 

# Do not modify these elements
layout: "learningpathall"
---

This Learning Path shows you how to migrate a real microservices application from x86 to Arm on GKE using multi-architecture container images. You'll work with Google's Online Boutique, a sample application built with multiple programming languages that represents real production architectures. The migration requires no major code changes, making it a practical example of moving to Arm-based Google Axion processors.

## Why use Google Axion processors for GKE?

Google Axion processors bring modern Arm-based compute to GKE, delivering strong price-performance and energy efficiency for cloud-native, scale-out services. With multi-architecture images and mixed node pools, you can migrate services from x86 to Arm gradually, with no major code changes.

### What is Google Axion?

[Google Axion](https://cloud.google.com/blog/products/compute/introducing-googles-new-arm-based-cpu) is Google Cloud's Arm-based CPU family built on Arm Neoverse, for general-purpose, cloud-native services and CPU-based AI. Deploy it for workloads like web apps and web servers, containerized microservices, open-source databases, in-memory caches, data analytics, media processing, and CPU-based AI inference and data processing. On GKE, leverage Axion through the C4A and N4A VM families, paired with Google's Titanium offloads to free CPU cycles for application work.

### Why migrate to Arm on GKE?

Consider three factors when evaluating Google Axion processors:

- Price-performance: you can run more workload per unit of cost for scale-out services
- Energy efficiency: you can reduce power usage for always-on microservices
- Compatibility: migrate containerized apps with build and deploy changes only—no code rewrites required

## Learn about the Online Boutique sample application

[Online Boutique](https://github.com/GoogleCloudPlatform/microservices-demo) is a polyglot microservices storefront, complete with shopping cart, checkout, catalog, ads, and recommendations. It's implemented in Go, Java, Python, .NET, and Node.js, with ready-to-use Dockerfiles and Kubernetes manifests. It's a realistic example for demonstrating an x86 to Arm migration with minimal code changes.

## Multi-architecture on GKE (pragmatic path)

This Learning Path demonstrates a practical migration approach using Docker Buildx with a Kubernetes driver. Your builds run natively inside BuildKit pods on GKE node pools—no QEMU emulation needed. You'll add an Arm node pool alongside your existing x86 nodes, then use node selectors and affinity rules to control where services run. This lets you migrate safely, one service at a time.

## How this Learning Path demonstrates migration

You'll migrate the Online Boutique application from x86 to Arm step by step. You'll build multi-architecture container images and use mixed node pools, so you can test each service on Arm before you fully commit to the migration.

The migration process involves these steps:

- Open Google Cloud Shell and set the environment variables.
- Enable required APIs, create an Artifact Registry repository, and authenticate Docker.
- Create a GKE Standard cluster with an amd64 node pool and add an arm64 (Axion-based C4A) node pool.
- Create a Buildx (Kubernetes driver) builder that targets both pools, then build and push multi-architecture images (amd64 and arm64) natively using BuildKit pods.
- Deploy to amd64 first (Kustomize overlay), validate, then migrate to arm64 (overlay) and verify.
- Automate builds and rollouts with Cloud Build and Skaffold.