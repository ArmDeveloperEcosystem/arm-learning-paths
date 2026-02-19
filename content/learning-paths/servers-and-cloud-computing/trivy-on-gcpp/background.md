---
title: Learn Azure Cobalt 100 Arm64 and Use Trivy for Security Scanning
weight: 2

### FIXED, DO NOT MODIFY
layout: "learningpathall"
---

## Key features and benefits of Azure Cobalt 100

Azure Cobalt 100 is Microsoft's first-generation Arm-based processor, designed for cloud-native Linux workloads. Based on Arm's Neoverse-N2 architecture, it delivers improved performance-per-watt and cost efficiency compared to comparable x86 instances. This makes it ideal for containerized workloads and CI/CD runners that run continuously.

Each vCPU is backed by a dedicated physical core, ensuring consistent, predictable performance. Running at 3.4 GHz, Cobalt 100 handles typical cloud workloads including web servers, data analytics, databases, and container platforms efficiently.

Learn more from the [Microsoft Azure Cobalt 100 blog post](https://techcommunity.microsoft.com/blog/azurecompute/announcing-the-preview-of-new-azure-vms-based-on-the-azure-cobalt-100-processor/4146353).

## Why Trivy matters in DevSecOps workflows
 
Trivy is an open-source vulnerability scanner designed to detect security issues in container images, filesystems, and infrastructure configurations. It's a core component in modern DevSecOps workflows, which shift security scanning left in the development pipeline to catch vulnerabilities before they reach production.

DevSecOps (Development, Security, and Operations) integrates security practices throughout the entire development lifecycle rather than as an afterthought. Trivy enables this by providing fast, reliable vulnerability detection on Arm64 and other architectures.

You can use Trivy to perform comprehensive security scans on container images built for multiple architectures, including Arm64. Detecting vulnerabilities early saves time and reduces risk downstream.

See the [Trivy documentation](https://trivy.dev/docs/) for comprehensive information.

## What you've accomplished and what's next

You now understand the core technologies in this Learning Path:

- Azure Cobalt 100, Microsoft's Arm-based processor designed for cloud efficiency
- Trivy, a security scanner that detects vulnerabilities in container images
- DevSecOps, the practice of integrating security throughout your development workflow

Next, you'll create an Azure Cobalt 100 virtual machine to begin building and scanning container images.
