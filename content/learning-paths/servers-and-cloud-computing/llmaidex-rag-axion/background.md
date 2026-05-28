---
title: Learn about LlamaIndex and Google Axion C4A for RAG applications
weight: 2

layout: "learningpathall"
---

## Google Axion C4A Arm instances for AI and RAG workloads

Google Axion C4A is a family of Arm-based virtual machines built on Google’s custom Axion CPU, which is based on Arm Neoverse V2 cores. Designed for high-performance and energy-efficient computing, these virtual machines offer strong performance for modern cloud workloads such as AI applications, vector databases, Retrieval-Augmented Generation (RAG) pipelines, and scalable inference services.

The C4A series provides a cost-effective alternative to x86 virtual machines while using the scalability and performance benefits of the Arm architecture in Google Cloud.

To learn more, see the Google blog [Introducing Google Axion Processors, our new Arm-based CPUs](https://cloud.google.com/blog/products/compute/introducing-googles-new-arm-based-cpu).

## LlamaIndex for RAG and context-aware AI applications on Arm

LlamaIndex is an open-source framework designed to build context-aware AI applications using Large Language Models (LLMs). It's widely used for Retrieval-Augmented Generation (RAG), document indexing, vector search, semantic retrieval, and integrating custom data sources with LLMs.

LlamaIndex provides a unified framework with components such as:

* Document loaders for ingesting custom data  
* Indexing pipelines for structured retrieval workflows  
* Query engines for context-aware question answering  
* Vector store integrations for scalable embedding search  
* LLM integrations for generating grounded responses  

Running LlamaIndex on Google Axion C4A Arm-based infrastructure enables efficient execution of AI and RAG workloads by using multi-core Arm CPUs and optimized memory performance. This results in improved performance per watt, reduced infrastructure costs, and better scalability for browser-based AI applications and local inference pipelines.

Common use cases include browser-based AI assistants, document search applications, semantic retrieval systems, vector database integrations, enterprise knowledge bases, and context-aware chatbot applications.

To learn more, see the [LlamaIndex documentation](https://docs.llamaindex.ai/en/stable/) and the [LlamaIndex GitHub repository](https://github.com/run-llama/llama_index).

## What you've learned and what's next

You've now learned about Google Axion C4A Arm-based virtual machines and their performance advantages for AI and RAG workloads. You were also introduced to core LlamaIndex components including document ingestion, indexing pipelines, query engines, vector stores, and LLM integrations.

Next, you'll create a firewall rule in Google Cloud Console to enable remote access to the browser-based LlamaIndex RAG application used in this Learning Path.
