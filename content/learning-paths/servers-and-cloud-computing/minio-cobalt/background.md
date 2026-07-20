---
title: "Overview of Azure Cobalt 100 and MinIO"

weight: 2

layout: "learningpathall"
---

## Why MinIO on Azure Cobalt 100

MinIO is an open source, Amazon S3 compatible object storage platform you can run on your own infrastructure. Running MinIO on Azure Cobalt 100 Arm-based processors provides high-throughput storage with the performance consistency needed for cloud-native workloads. By the end of this Learning Path, you'll have MinIO running on an Azure Cobalt 100 virtual machine, with measured storage throughput, confirmed S3 API compatibility using Python, and a practical AI/ML workflow for storing and retrieving datasets and model artifacts.

## Azure Cobalt 100 Arm-based processor

Azure Cobalt 100 is Microsoft's first-generation Arm-based processor, built on Arm Neoverse N2. It allocates a dedicated physical core for each vCPU, which provides consistent and predictable performance for cloud-native, scale-out Linux workloads. These characteristics make Cobalt 100 well suited for storage-intensive applications like MinIO, where throughput and latency consistency matter.

To learn more, see the Microsoft blog [Announcing the preview of new Azure VMs based on the Azure Cobalt 100 processor](https://techcommunity.microsoft.com/blog/azurecompute/announcing-the-preview-of-new-azure-vms-based-on-the-azure-cobalt-100-processor/4146353).

## MinIO

MinIO is an open source, Amazon S3 compatible object storage platform you can run on your own infrastructure. It supports the Amazon S3 API, so applications and SDKs written for S3 work with MinIO without modification. MinIO is a practical choice when you want S3-compatible storage without cloud vendor lock-in, or when your compute and storage need to run in the same environment to avoid data transfer costs.

MinIO is optimized for high-throughput workloads and supports both standalone and distributed deployments. It includes erasure coding, encryption, and access control, and has a minimal footprint that works well in containerized and cloud-native environments.

## MinIO deployment architecture

MinIO deployments typically consist of the following components:

- **MinIO Server:** The core storage service that handles object storage operations and exposes S3-compatible APIs.  
- **Object Storage (Buckets):** Logical containers used to store data objects such as files, datasets, and model artifacts.  
- **MinIO Client (mc):** A command-line tool used to interact with MinIO for uploading, downloading, and managing objects.  
- **Web Console:** A browser-based interface for managing buckets, objects, users, and access policies. 

## MinIO use cases

MinIO is widely used as object storage for AI/ML training datasets and model artifacts, and as a backend for data lakes and analytics pipelines with tools like Apache Spark, Presto, and Hadoop. It also serves backup and archival needs and provides object storage for microservices and cloud-native applications.
