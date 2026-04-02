---
title: Get started with Qdrant on Google Axion C4A
weight: 2

layout: "learningpathall"
---

## Explore Axion C4A Arm instances in Google Cloud

Google Axion C4A is a family of Arm-based virtual machines built on Google’s custom Axion CPU, which is based on Arm Neoverse-V2 cores. Designed for high-performance and energy-efficient computing, these virtual machines offer strong performance for data-intensive and analytics workloads such as big data processing, in-memory analytics, columnar data processing, and high-throughput data services.

The C4A series provides a cost-effective alternative to x86 virtual machines while leveraging the scalability, SIMD acceleration, and memory bandwidth advantages of the Arm architecture in Google Cloud.

These characteristics make Axion C4A instances well-suited for modern analytics stacks that rely on columnar data formats and memory-efficient execution engines.

To learn more, see the Google blog [Introducing Google Axion Processors, our new Arm-based CPUs](https://cloud.google.com/blog/products/compute/introducing-googles-new-arm-based-cpu).

## Explore Qdrant Vector Search on Google Axion C4A (Arm Neoverse V2)

Qdrant is an open-source vector database designed for efficient similarity search and high-performance vector indexing. It enables applications to store and retrieve embeddings—numerical representations of data such as text, images, or audio—allowing systems to perform semantic search and AI-powered retrieval.

Vector databases like Qdrant are commonly used in modern AI systems to support applications such as semantic search, recommendation systems, anomaly detection, and Retrieval-Augmented Generation (RAG) pipelines. By storing embeddings and performing nearest-neighbor search, Qdrant allows applications to retrieve the most relevant information based on semantic meaning rather than simple keyword matching.

Running Qdrant on Google Axion C4A Arm-based infrastructure enables efficient execution of AI and vector search workloads. Axion processors, based on the Arm Neoverse V2 architecture, provide high performance and improved energy efficiency for modern cloud-native applications and data services.

Using Qdrant on Axion allows you to achieve:

- High-performance vector similarity search for AI applications
- Efficient embedding, storage, and indexing for semantic retrieval
- Low-latency data access for chatbots and AI assistants
- Scalable infrastructure for Retrieval-Augmented Generation (RAG) pipelines
- Cost-efficient execution of vector database workloads on Arm-based cloud infrastructure

Common use cases include AI chatbots, semantic search engines, recommendation systems, enterprise knowledge assistants, document retrieval systems, and machine learning feature stores.

To learn more, visit the [Qdrant documentation](https://qdrant.tech/documentation/) and explore how vector databases enable modern AI applications.

## What you've learned and what's next

In this section, you learned about:

* Google Axion C4A Arm-based VMs and their performance characteristics
* Qdrant as a vector database for storing and retrieving embeddings
* Semantic similarity search and how it powers AI retrieval systems
* How vector search enables chatbot and RAG-style knowledge retrieval 

Next, you can explore how to extend this setup by integrating large language models (LLMs) to build a full Retrieval-Augmented Generation (RAG) pipeline, enabling AI systems to generate context-aware responses using information retrieved from the Qdrant vector database.
