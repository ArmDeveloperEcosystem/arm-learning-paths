---
title: "Understand Azure Cobalt 100 and Apache Spark with Gluten and Velox"

weight: 2

layout: "learningpathall"
---

## Azure Cobalt 100 Arm-based processor

Azure’s Cobalt 100 is Microsoft’s first-generation, in-house Arm-based processor. Built on Arm Neoverse N2, Cobalt 100 is a 64-bit CPU that delivers strong performance and energy efficiency for cloud-native, scale-out Linux workloads. These workloads include web and application servers, data analytics, open-source databases, and caching systems. Running at 3.4 GHz, Cobalt 100 allocates a dedicated physical core for each vCPU, which ensures consistent and predictable performance.

To learn more, see the Microsoft blog [Announcing the preview of new Azure VMs based on the Azure Cobalt 100 processor](https://techcommunity.microsoft.com/blog/azurecompute/announcing-the-preview-of-new-azure-vms-based-on-the-azure-cobalt-100-processor/4146353).

## Apache Spark with Gluten and Velox

Apache Spark is an open-source distributed data processing engine designed for large-scale data analytics. It provides high-level APIs for SQL, streaming, machine learning, and graph processing, and is widely used for building data pipelines and analytical workloads. For more information about Apache Spark, see the [Apache Spark Documentation](https://spark.apache.org/docs/latest/).

By default, Spark executes queries using the Java Virtual Machine (JVM), which can introduce overhead in CPU-intensive workloads. To address this, modern acceleration frameworks such as Gluten and Velox enable native execution for improved performance.

Gluten is an open-source Spark plugin that offloads Spark SQL execution from the JVM to native engines. It acts as a bridge between Spark and high-performance backends, enabling efficient query execution while maintaining compatibility with existing Spark workloads. For more information about Gluten, see [Gluten Project](https://github.com/apache/incubator-gluten).

Velox is a high-performance, vectorized execution engine written in C++. It is optimized for modern hardware, including Arm64 architectures such as Azure Cobalt 100. Velox processes data in a columnar format and uses vectorized execution to significantly reduce CPU overhead and improve query performance. For more information about Velox, see [Velox Engine](https://github.com/facebookincubator/velox).

### What you've learned and what's next

You've now learned about Azure Cobalt 100 Arm-based processors and Apache Spark. You've also understood how frameworks such as Gluten and Velox improve Spark SQL performance.  

In the next section, you'll create a Cobalt 100 virtual machine for building a Spark SQL workload.