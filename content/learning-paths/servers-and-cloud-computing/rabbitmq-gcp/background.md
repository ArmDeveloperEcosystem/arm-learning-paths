---
title: Technology Stack Overview

weight: 2

layout: "learningpathall"
---

## Cobalt 100 Arm-based processor

Azure’s Cobalt 100 is built on Microsoft's first-generation, in-house Arm-based processor: the Cobalt 100. Designed entirely by Microsoft and based on Arm’s Neoverse N2 architecture, this 64-bit CPU delivers improved performance and energy efficiency across a broad spectrum of cloud-native, scale-out Linux workloads. These include web and application servers, data analytics, open-source databases, caching systems, and other related technologies. Running at 3.4 GHz, the Cobalt 100 processor allocates a dedicated physical core for each vCPU, ensuring consistent and predictable performance. 

To learn more about Cobalt 100, refer to the blog [Announcing the preview of new Azure virtual machine based on the Azure Cobalt 100 processor](https://techcommunity.microsoft.com/blog/azurecompute/announcing-the-preview-of-new-azure-vms-based-on-the-azure-cobalt-100-processor/4146353).

## Google Axion C4A Arm instances in Google Cloud

Google Axion C4A is a family of Arm-based virtual machines built on Google’s custom Axion CPU, which is based on Arm Neoverse-V2 cores. Designed for high-performance and energy-efficient computing, these virtual machines offer strong performance for modern cloud workloads such as CI/CD pipelines, microservices, media processing, and general-purpose applications.

The C4A series provides a cost-effective alternative to x86 virtual machines while leveraging the scalability and performance benefits of the Arm architecture in Google Cloud.

To learn more about Google Axion, see the [Introducing Google Axion Processors, Arm-based CPUs](https://cloud.google.com/blog/products/compute/introducing-googles-new-arm-based-cpu) blog.

## RabbitMQ

RabbitMQ is an open-source **message broker** that enables applications to communicate asynchronously using messaging patterns such as queues, publish/subscribe, and routing. It acts as an intermediary that reliably receives, stores, and forwards messages between producers and consumers.

RabbitMQ helps decouple application components, improve scalability, and increase fault tolerance by ensuring messages are not lost and can be processed independently. It supports multiple messaging protocols, including AMQP, and provides features such as message durability, acknowledgments, routing via exchanges, and flexible delivery guarantees.

RabbitMQ is widely used for **event-driven architectures**, **background job processing**, **microservices communication**, and **notification systems**. It integrates easily with many programming languages and platforms.

Learn more from the [RabbitMQ official website](https://www.rabbitmq.com/) and the [official documentation](https://www.rabbitmq.com/documentation.html).
