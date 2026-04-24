---
title: Understand Azure Cobalt 100 VMs and Elasticsearch benchmarking with ESRally

weight: 2

layout: "learningpathall"
---

## Azure Cobalt 100 Arm-based processor

Azure’s Cobalt 100 is Microsoft’s first-generation, in-house Arm-based processor. Built on Arm Neoverse N2, Cobalt 100 is a 64-bit CPU that delivers strong performance and energy efficiency for cloud-native, scale-out Linux workloads such as web and application servers, data analytics, open-source databases, and caching systems. Running at 3.4 GHz, Cobalt 100 allocates a dedicated physical core for each vCPU, which helps ensure consistent and predictable performance.

To learn more, see the Microsoft blog [Announcing the preview of new Azure VMs based on the Azure Cobalt 100 processor](https://techcommunity.microsoft.com/blog/azurecompute/announcing-the-preview-of-new-azure-vms-based-on-the-azure-cobalt-100-processor/4146353).

## Elasticsearch

Elasticsearch is a distributed search and analytics engine built on Apache Lucene that is used to index, store, search, and analyze large volumes of structured and unstructured data in near real time. It is commonly used for full-text search, log and event analytics, observability, security workloads, and increasingly as a vector database for AI-powered retrieval use cases.

## ESRally benchmarking tools for Elasticsearch

ESRally is Elastic's benchmarking tool for Elasticsearch, designed to measure indexing, query, and cluster performance under realistic workloads so teams can compare configurations, detect regressions, and evaluate tuning changes. It works by running repeatable benchmark races against Elasticsearch using predefined or custom tracks, making it useful for both local testing and larger-scale performance validation.

## What you've learned and what's next

Next, you'll create a Cobalt 100 Azure VM and prepare it to install the Elasticsearch runtime and ESRally benchmark tool.
