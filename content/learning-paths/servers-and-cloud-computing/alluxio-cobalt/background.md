---
title: Understand Alluxio on Azure Cobalt 100

weight: 2

layout: "learningpathall"
---

## Why run Alluxio on Azure Cobalt 100

Alluxio on Arm-based Azure Cobalt 100 processors delivers high-performance data access for analytics and AI workloads. Cobalt 100's dedicated physical cores per vCPU provide consistent and predictable performance, which complements Alluxio’s in-memory caching and data orchestration capabilities. 

Alluxio's memory-centric architecture on Arm-based compute can reduce data latency and help accelerate frameworks such as Apache Spark.

## Azure Cobalt 100 Arm-based processor

Azure’s Cobalt 100 is Microsoft’s first-generation, in-house Arm-based processor. Built on Arm Neoverse N2, Cobalt 100 is a 64-bit CPU that delivers strong performance and energy efficiency for cloud-native, scale-out Linux workloads. These workloads include web and application servers, data analytics, open-source databases, and caching systems. Running at 3.4 GHz, Cobalt 100 allocates a dedicated physical core for each vCPU, ensuring consistent and predictable performance.

To learn more, see the Microsoft blog [Announcing the preview of new Azure VMs based on the Azure Cobalt 100 processor](https://techcommunity.microsoft.com/blog/azurecompute/announcing-the-preview-of-new-azure-vms-based-on-the-azure-cobalt-100-processor/4146353).

## How Alluxio improves data access

Alluxio is an open-source data orchestration platform that enables fast and reliable access to data across distributed storage systems. It acts as a unified layer between compute frameworks and storage systems, improving performance for data-intensive applications.

Alluxio is widely used in modern data platforms to accelerate analytics workloads by caching frequently accessed data in memory. The caching reduces latency and minimizes repeated reads from slower storage systems such as local disks or cloud storage.

Alluxio integrates with popular analytics frameworks such as Apache Spark, Presto, and Hadoop. The integration makes it ideal for building high-performance data pipelines and AI/ML workloads.

To learn more, see the official [Alluxio documentation](https://docs.alluxio.io/).

Alluxio provides key capabilities for data orchestration and performance optimization:

- Data Caching: Stores frequently accessed data in memory, significantly reducing access time compared to disk-based reads.
- Unified Namespace: Presents a single logical view of data across multiple storage systems, simplifying data access.
- Tiered Storage: Supports multiple storage layers (memory, SSD, HDD), enabling efficient data management based on access patterns.
- Compute Integration: Works with analytics engines such as Apache Spark to accelerate data processing without modifying application logic.

In this Learning Path, you'll deploy Alluxio on an Azure Cobalt 100 Arm64 virtual machine and build a data orchestration and caching layer for analytics workloads. You'll integrate Alluxio with Apache Spark and benchmark performance to understand how caching improves data access speed.

## What you've learned and what's next

You now know why Azure Cobalt 100 and Alluxio are a strong combination for high-performance data orchestration and analytics workloads. Next, you'll create the virtual machine that will run Alluxio throughout this Learning Path.
