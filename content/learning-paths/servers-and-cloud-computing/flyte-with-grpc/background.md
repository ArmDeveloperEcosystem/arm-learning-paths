---
title: Get started with Flyte ML Workflow Pipelines with gRPC on Google Axion C4A
weight: 2

layout: "learningpathall"
---

## Explore Axion C4A Arm instances in Google Cloud

Google Axion C4A is a family of Arm-based virtual machines built on Google’s custom Axion CPU, which is based on Arm Neoverse-V2 cores. Designed for high-performance and energy-efficient computing, these virtual machines offer strong performance for data-intensive and analytics workloads such as big data processing, in-memory analytics, columnar data processing, and high-throughput data services.

The C4A series provides a cost-effective alternative to x86 virtual machines while leveraging the scalability, SIMD acceleration, and memory bandwidth advantages of the Arm architecture in Google Cloud.

These characteristics make Axion C4A instances well-suited for modern analytics stacks that rely on columnar data formats and memory-efficient execution engines.

To learn more, see the Google blog [Introducing Google Axion Processors, our new Arm-based CPUs](https://cloud.google.com/blog/products/compute/introducing-googles-new-arm-based-cpu).

## Explore Flyte ML Workflow Pipelines with gRPC on Google Axion C4A (Arm Neoverse V2)

Flyte is an open-source workflow orchestration platform used to build scalable and reproducible data and machine learning pipelines. It allows developers to define workflows as Python tasks, simplifying the management of complex ML processes such as data preparation, feature engineering, and model training. 

gRPC enables fast communication between distributed services within these pipelines. Running Flyte with gRPC on Google Axion C4A Arm-based processors provides efficient, scalable infrastructure for executing modern ML workflows and distributed data processing tasks.

To learn more, visit the [Flyte documentation](https://docs.flyte.org/) and explore the [gRPC documentation](https://grpc.io/docs/) to understand how distributed service communication enables scalable machine learning workflows.

## What you've learned and what's next

In this section, you learned about:

* Google Axion C4A Arm-based VMs and their performance characteristics
* Flyte as a workflow orchestration platform for machine learning pipelines
* gRPC as a communication layer for distributed services
* How Flyte and gRPC can be used together to build scalable ML training pipelines

Next, You will deploy Flyte tools, create a gRPC-based feature engineering service, and build a distributed ML workflow pipeline that orchestrates data processing and model training tasks on Axion infrastructure.
