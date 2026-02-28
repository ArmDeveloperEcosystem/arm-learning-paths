---
title: Get started with Apache Arrow and Arrow Flight on Google Axion C4A
weight: 2

layout: "learningpathall"
---

## Explore Axion C4A Arm instances in Google Cloud

Google Axion C4A is a family of Arm-based virtual machines built on Google’s custom Axion CPU, which is based on Arm Neoverse-V2 cores. Designed for high-performance and energy-efficient computing, these virtual machines offer strong performance for data-intensive and analytics workloads such as big data processing, in-memory analytics, columnar data processing, and high-throughput data services.

The C4A series provides a cost-effective alternative to x86 virtual machines while leveraging the scalability, SIMD acceleration, and memory bandwidth advantages of the Arm architecture in Google Cloud.

These characteristics make Axion C4A instances well-suited for modern analytics stacks that rely on columnar data formats and memory-efficient execution engines.

To learn more, see the Google blog [Introducing Google Axion Processors, our new Arm-based CPUs](https://cloud.google.com/blog/products/compute/introducing-googles-new-arm-based-cpu).

## Explore Apache Arrow and Arrow Flight on Google Axion C4A (Arm Neoverse V2)

Apache Arrow is an open-source, cross-language platform for in-memory data processing. It defines a standardized columnar memory format that enables zero-copy data sharing between analytics systems, significantly improving performance for modern data workloads.

Arrow is widely used as a foundational layer for analytics engines, data science tools, and big data frameworks, enabling efficient processing of formats such as Parquet and ORC while minimizing serialization overhead.

Arrow Flight is a high-performance RPC framework built on gRPC that enables fast, memory-to-memory data transfer using the Arrow columnar format. It is designed to replace traditional REST- or file-based data exchange with a low-latency, high-throughput alternative optimized for analytics workloads.

Running Apache Arrow and Arrow Flight on Google Axion C4A Arm-based infrastructure allows you to achieve:

- High-throughput columnar data processing  
- Reduced CPU overhead through zero-copy data exchange  
- Improved performance per watt for analytics pipelines  
- Cost-efficient scaling of in-memory data services  

Common use cases include interactive analytics, data lake acceleration, machine learning feature pipelines, distributed query engines, and high-performance data services.

To learn more, visit the [Apache Arrow website](https://arrow.apache.org/) and explore the [Arrow Flight documentation](https://arrow.apache.org/docs/format/Flight.html).

## What you've accomplished and what's next

In this section, you learned about:

* Google Axion C4A Arm-based VMs and their performance characteristics  
* Apache Arrow’s columnar in-memory format and its role in modern analytics  
* Arrow Flight and its use for high-speed, memory-to-memory data transfer  
* How Arm architecture enables cost-effective, high-performance analytics workloads  

Next, you'll configure firewall rules and network access to allow external communication between MinIO object storage, Apache Arrow workloads, and Arrow Flight services running on your Axion C4A virtual machine.
