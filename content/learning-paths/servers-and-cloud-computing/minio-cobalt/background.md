---
title: "Overview of Azure Cobalt 100 and MinIO"

weight: 2

layout: "learningpathall"
---

## Azure Cobalt 100 Arm-based processor

Azure’s Cobalt 100 is Microsoft’s first-generation, in-house Arm-based processor. Built on Arm Neoverse N2, Cobalt 100 is a 64-bit CPU that delivers strong performance and energy efficiency for cloud-native, scale-out Linux workloads such as web and application servers, data analytics, open-source databases, and caching systems. Running at 3.4 GHz, Cobalt 100 allocates a dedicated physical core for each vCPU, which helps ensure consistent and predictable performance.

To learn more, see the Microsoft blog [Announcing the preview of new Azure VMs based on the Azure Cobalt 100 processor](https://techcommunity.microsoft.com/blog/azurecompute/announcing-the-preview-of-new-azure-vms-based-on-the-azure-cobalt-100-processor/4146353).

## MinIO

MinIO is a high-performance, S3-compatible object storage platform designed for cloud-native applications, AI/ML workloads, and modern data infrastructure. It is lightweight, scalable, and optimized for high-throughput and low-latency object storage operations.

MinIO is commonly used as a storage backend for data lakes, machine learning pipelines, backup systems, and analytics platforms. It supports the Amazon S3 API, allowing seamless integration with existing tools and SDKs that are built for AWS S3.

MinIO is designed to run efficiently on Arm-based architectures such as Azure Cobalt 100, enabling cost-effective and energy-efficient storage solutions for large-scale workloads.



## Key features of MinIO

- **S3 Compatibility:** Fully compatible with the Amazon S3 API, enabling easy integration with existing applications and tools.  
- **High Performance:** Optimized for high-throughput workloads such as AI/ML datasets and analytics pipelines.  
- **Scalability:** Supports both standalone and distributed deployments for scaling storage capacity and performance.  
- **Lightweight and Cloud-Native:** Minimal resource footprint and designed for containerized and cloud environments.  
- **Data Protection:** Supports erasure coding, encryption, and access control for secure and reliable storage.  


## MinIO architecture components

MinIO deployments typically consist of the following components:

- **MinIO Server:** The core storage service that handles object storage operations and exposes S3-compatible APIs.  
- **Object Storage (Buckets):** Logical containers used to store data objects such as files, datasets, and model artifacts.  
- **MinIO Client (mc):** A command-line tool used to interact with MinIO for uploading, downloading, and managing objects.  
- **Web Console:** A browser-based interface for managing buckets, objects, users, and access policies. 

## Use cases

MinIO is widely used in modern cloud and data environments:

- **AI/ML Workloads:** Store training datasets, model artifacts, and inference data  
- **Data Lakes:** Serve as a scalable backend for structured and unstructured data  
- **Backup and Archival:** Store backups and snapshots with high durability  
- **Cloud-Native Applications:** Provide object storage for microservices and distributed systems  
- **Analytics Pipelines:** Integrate with tools like Apache Spark, Presto, and Hadoop

To learn more about MinIO, see:

- [MinIO Official Website](https://min.io/)  
- [MinIO Documentation](https://min.io/docs/minio/linux/index.html)  
- [MinIO GitHub Repository](https://github.com/minio/minio)  

## What you will learn

In this learning path, you will:

- Deploy MinIO on an Azure Cobalt ARM virtual machine  
- Configure and manage object storage using MinIO  
- Benchmark storage performance for high-throughput workloads  
- Validate S3 compatibility using standard SDKs  
- Implement a real-world AI/ML dataset and model storage workflow  
