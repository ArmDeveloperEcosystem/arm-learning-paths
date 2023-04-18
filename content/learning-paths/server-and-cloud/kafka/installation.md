---
# User change
title: "Introduction to Kafka and Zookeeper"

weight: 2

layout: "learningpathall"


---

## Before you begin

You will need 7 physical Arm machines or cloud instances with Ubuntu/Debian installed. 
Make sure ports 8080, 2888, 3888, 2181 and 9092 are open in the security group of the IP addresses for these machines.

## Introduction to Kafka

Kafka is an event streaming platform. It is a distributed system consisting of servers and clients that communicate via a high-performance TCP network protocol. It can be deployed on bare-metal hardware, virtual machines, and containers in on-premise as well as cloud environments. The [Getting Started Guide](https://kafka.apache.org/documentation/#gettingStarted) is a great resource to learn more about Kafka.

## Introduction to Zookeeper

Zookeeper is an open sourced project that provides a centralized service for maintainence of configuration information, naming and group services. It is used by a cluster or a group of nodes to share data. Kafka is built to use Zookeeper to coordinate tasks.

## Setup

In this learning path, you will deploy 3 of the Arm machines as Kafka nodes, 3 machines as Zookeeper nodes and one machine as a client node. A diagram of the setup is shown below. For a simpler single node setup, follow the Kafka [quick start guide](https://kafka.apache.org/quickstart).

![KAFKA_image3 (3) center](https://user-images.githubusercontent.com/66300308/189855554-51b0c9d2-095b-4196-8a2d-e8a768880d72.png)

# Install Java:

Install Java on all 7 nodes.

```console
sudo apt install -y default-jdk
```


















