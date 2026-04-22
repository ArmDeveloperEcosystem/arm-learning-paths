---
title: Understand Azure Cobalt 100 VMs and MySQL migration strategy

weight: 2

layout: "learningpathall"
---

### Azure Cobalt 100 Arm-based processor

Azure’s Cobalt 100 is Microsoft’s first-generation, in-house Arm-based processor. Built on Arm Neoverse N2, Cobalt 100 is a 64-bit CPU that delivers strong performance and energy efficiency for cloud-native, scale-out Linux workloads such as web and application servers, data analytics, open-source databases, and caching systems. Running at 3.4 GHz, Cobalt 100 allocates a dedicated physical core for each vCPU, which helps ensure consistent and predictable performance.

To learn more, see the Microsoft blog [Announcing the preview of new Azure VMs based on the Azure Cobalt 100 processor](https://techcommunity.microsoft.com/blog/azurecompute/announcing-the-preview-of-new-azure-vms-based-on-the-azure-cobalt-100-processor/4146353).

### MySQL Migrations

MySQL is a cross-platform relational database system whose storage engines and on-disk formats are designed for reliability and portability. When you move between CPU architectures, such as x64 to Arm, MySQL documentation recommends a logical migration instead of copying raw data files.

A practical approach is to use `mysqldump` to export SQL, transfer the dump, and import it on the Arm target with the `mysql` client. The MySQL 8.4 Reference Manual also recommends this approach for cross-architecture transfers.


## What you've learned and what's next

You now have the background on Azure Cobalt 100 and the recommended MySQL migration method for x64-to-Arm moves.

Next, you'll create a simulated on-premises x64 server in Azure and prepare it as the migration source environment.