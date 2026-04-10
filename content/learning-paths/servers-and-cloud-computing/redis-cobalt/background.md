---
title: Understand Redis on Azure Cobalt 100

weight: 2

layout: "learningpathall"
---

## Why run Redis on Azure Cobalt 100

Redis on Arm-based Azure Cobalt 100 processors delivers high-performance, low-latency data operations for real-time messaging and event processing. Cobalt 100's dedicated physical cores per vCPU provide consistent performance that suits Redis's in-memory architecture and event-driven workloads.

## Azure Cobalt 100 Arm-based processor

Azure’s Cobalt 100 is Microsoft’s first-generation, in-house Arm-based processor. Built on Arm Neoverse N2, Cobalt 100 is a 64-bit CPU that delivers strong performance and energy efficiency for cloud-native, scale-out Linux workloads such as web and application servers, data analytics, open-source databases, and caching systems. Running at 3.4 GHz, Cobalt 100 allocates a dedicated physical core for each vCPU, which helps ensure consistent and predictable performance.

To learn more, see the Microsoft blog [Announcing the preview of new Azure VMs based on the Azure Cobalt 100 processor](https://techcommunity.microsoft.com/blog/azurecompute/announcing-the-preview-of-new-azure-vms-based-on-the-azure-cobalt-100-processor/4146353).

## Redis

Redis is an open-source, in-memory data structure store used as a database, cache, and message broker. It is widely adopted for building high-performance, low-latency applications such as real-time analytics, caching layers, session stores, and event-driven systems.

Redis supports multiple data structures, including strings, hashes, lists, sets, sorted sets, and streams, enabling flexible application design. Its in-memory architecture allows it to deliver sub-millisecond latency and high throughput, making it ideal for modern cloud-native workloads.

To learn more, see the official [Redis documentation](https://redis.io/docs/).

Redis also provides built-in support for real-time messaging and event processing through:

- **Pub/Sub (Publish/Subscribe):** Enables real-time communication between producers and consumers without message persistence. It is commonly used for chat systems, notifications, and live updates.

- **Redis Streams:** A persistent data structure designed for event-driven architectures. Streams allow message storage, replay, and consumer group-based processing for scalable and reliable event pipelines.

- **Consumer Groups:** A feature of Redis Streams that enables distributed processing by multiple consumers, ensuring scalability and fault tolerance in production systems.

Redis is commonly used in:

- Real-time messaging systems  
- Event-driven microservices architectures  
- Data ingestion and streaming pipelines  
- Caching and session management  
- High-performance APIs  

In this Learning Path, you'll deploy Redis on an Azure Cobalt 100 Arm64 virtual machine and build a real-time messaging and event processing system using Pub/Sub and Redis Streams. You will also benchmark Redis performance to validate its efficiency on Arm-based infrastructure.

## What you've learned and what's next

You now have the context for why Azure Cobalt 100 and Redis are a strong combination for high-performance, low-latency workloads. Next, you'll create the virtual machine that will run Redis throughout this Learning Path.
