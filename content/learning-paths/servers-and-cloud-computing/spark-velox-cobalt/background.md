---
title: "Overview of Azure Cobalt 100 and Apache Spark with Gluten and Velox"

weight: 2

layout: "learningpathall"
---

## Azure Cobalt 100 Arm-based processor

Azure’s Cobalt 100 is Microsoft’s first-generation, in-house Arm-based processor. Built on Arm Neoverse N2, Cobalt 100 is a 64-bit CPU that delivers strong performance and energy efficiency for cloud-native, scale-out Linux workloads such as web and application servers, data analytics, open-source databases, and caching systems. Running at 3.4 GHz, Cobalt 100 allocates a dedicated physical core for each vCPU, which helps ensure consistent and predictable performance.

To learn more, see the Microsoft blog [Announcing the preview of new Azure VMs based on the Azure Cobalt 100 processor](https://techcommunity.microsoft.com/blog/azurecompute/announcing-the-preview-of-new-azure-vms-based-on-the-azure-cobalt-100-processor/4146353).

## Apache Spark with Gluten and Velox

Apache Spark is an open-source distributed data processing engine designed for large-scale data analytics. It provides high-level APIs for SQL, streaming, machine learning, and graph processing, and is widely used for building data pipelines and analytical workloads.

By default, Spark executes queries using the JVM (Java Virtual Machine), which can introduce overhead in CPU-intensive workloads. To address this, modern acceleration frameworks like **Gluten** and **Velox** enable native execution for improved performance.

**Gluten** is an open-source Spark plugin that offloads Spark SQL execution from the JVM to native engines. It acts as a bridge between Spark and high-performance backends, enabling efficient query execution while maintaining compatibility with existing Spark workloads.

**Velox** is a high-performance, vectorized execution engine written in C++. It is optimized for modern hardware, including Arm64 architectures such as Azure Cobalt 100. Velox processes data in a columnar format and uses vectorized execution to significantly reduce CPU overhead and improve query performance.

Together, **Gluten + Velox** provide:

- Native (off-JVM) execution of Spark SQL queries  
- Vectorized processing for faster computation  
- Reduced memory and CPU overhead  
- Improved performance on Arm-based infrastructure  

To learn more, see:
- [Apache Spark Documentation](https://spark.apache.org/docs/latest/)
- [Gluten Project](https://github.com/apache/incubator-gluten)
- [Velox Engine](https://github.com/facebookincubator/velox)


### Key Capabilities

- **Native Query Execution:**  
  Spark SQL queries are executed using Velox instead of JVM-based execution.

- **Columnar Processing:**  
  Data is processed in columnar batches, improving cache efficiency and throughput.

- **Vectorized Execution:**  
  Multiple data values are processed in a single CPU instruction, accelerating computation.

- **Hardware Optimization:**  
  Velox is optimized for modern CPUs, including Arm64 (Azure Cobalt 100), delivering better performance per core.

### In This Learning Path

In this Learning Path, you will:

- Deploy Apache Spark on an Azure Cobalt 100 Arm64 virtual machine  
- Build and integrate Gluten with the Velox backend  
- Configure Spark to use native execution  
- Run Spark SQL workloads using Gluten + Velox  
- Generate and load TPC-DS benchmark datasets  
- Execute analytical queries and measure performance  
- Compare accelerated workloads against vanilla Spark  

