---
title: "About Google Axion C4A series and GitHub Actions"

weight: 2

layout: "learningpathall"
---

## Google Axion C4A series

The Google Axion C4A series is a family of Arm-based virtual machines built on Google’s custom Axion CPU, which is based on Arm Neoverse-V2 cores. Designed for high-performance and energy-efficient computing, these virtual machines offer strong performance ideal for modern cloud workloads such as CI/CD pipelines, microservices, media processing, and general-purpose applications.

The C4A series provides a cost-effective alternative to x86 virtual machine while leveraging the scalability and performance benefits of the Arm architecture in Google Cloud.

To learn more about Google Axion, refer to the blog [Introducing Google Axion Processors, our new Arm-based CPUs](https://cloud.google.com/blog/products/compute/introducing-googles-new-arm-based-cpu).

## GitHub Actions and CI/CD

GitHub Actions is a powerful CI/CD (Continuous Integration and Continuous Delivery) platform built into GitHub. It allows developers to automate tasks such as building, testing, and deploying code in response to events like code pushes, pull requests, or scheduled jobs—directly from their GitHub repositories. This helps improve development speed, reliability, and collaboration.

A key feature of GitHub Actions is [self-hosted runners](https://docs.github.com/en/actions/concepts/runners/about-self-hosted-runners), which let you run workflows on your own infrastructure instead of GitHub’s hosted servers. This is especially useful for:

- Running on custom hardware, including Arm64-based systems (e.g., Google Axion virtual machine), to optimize performance and ensure architecture-specific compatibility.
- Private network access, allowing secure interaction with internal services or databases.
- Faster execution, especially for resource-intensive workflows, by using dedicated or high-performance machines.

Self-hosted runners provide more control, flexibility, and cost-efficiency—making them ideal for advanced CI/CD pipelines and platform-specific testing.
