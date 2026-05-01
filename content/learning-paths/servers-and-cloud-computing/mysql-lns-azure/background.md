---
title: Understand Azure Cobalt 100 VMs and MySQL migration strategy

weight: 2

layout: "learningpathall"
---

## Azure Cobalt 100 Arm-based processor

Azure Cobalt 100 is Microsoft's first-generation Arm-based processor, built on Arm Neoverse N2. It allocates a dedicated physical core for each vCPU, which provides consistent and predictable performance for cloud-native, scale-out Linux workloads. These characteristics make Cobalt 100 well suited for open-source databases such as MySQL, where consistent I/O throughput and low-latency query execution are critical for production workloads.

To learn more, see the Microsoft blog [Announcing the preview of new Azure VMs based on the Azure Cobalt 100 processor](https://techcommunity.microsoft.com/blog/azurecompute/announcing-the-preview-of-new-azure-vms-based-on-the-azure-cobalt-100-processor/4146353).

## MySQL migrations

MySQL is a cross-platform relational database system whose storage engines and on-disk formats are designed for reliability and portability. When you move between CPU architectures, such as x64 to Arm, MySQL documentation recommends a logical migration instead of copying raw data files.

A practical approach is to use `mysqldump` to export SQL, transfer the dump, and import it on the Arm target with the `mysql` client. The MySQL 8.4 Reference Manual recommends this approach for cross-architecture transfers.


## What you've learned and what's next

You've now learned about Azure Cobalt 100 and the recommended MySQL migration method for x64-to-Arm moves.

Next, you'll create a simulated on-premises x64 server in Azure and prepare it as the migration source environment.