---
# User change
title: "Install Kafka and Zookeeper"

weight: 2

layout: "learningpathall"


---

## Prerequisites

* 7 Physical machines or 7 cloud nodes with Ubuntu/Debian installed. We need 3 Kafka nodes, 3 Zookeeper nodes, and 1 client node.

*  Download latest Kafka binary from [here](https://dlcdn.apache.org/kafka/).

## What is Kafka and How Does it Work?

Kafka is an event streaming platform. It is a distributed system consisting of servers and clients that communicate via a high-performance TCP network protocol. It can be deployed on bare-metal hardware, virtual machines, and containers in on-premise as well as cloud environments. The [Getting Started Guide](https://kafka.apache.org/documentation/#gettingStarted) is a great resource to learn more about Kafka.

## Setup

In this learning path, we will deploy 3 Kafka nodes, 3 Zookeeper nodes and a client node as shown in the diagram here. For a simpler single node setup, follow the Kafka [quick start guide](https://kafka.apache.org/quickstart).

![KAFKA_image3 (3)](https://user-images.githubusercontent.com/66300308/189855554-51b0c9d2-095b-4196-8a2d-e8a768880d72.png)

## Install Java:

First, install Java on all 7 nodes.

```console

apt install -y default-jdk

```

## Install Zookeeper(3.8.0):

Next, Zookeeper needs to be installed on the 3 Zookeeper nodes as shown below.

```console

mkdir Zookeeper

wget https://dlcdn.apache.org/zookeeper/zookeeper-3.8.0/apache-zookeeper-3.8.0-bin.tar.gz

tar -xzf apache-zookeeper-3.8.0-bin.tar.gz

cd apache-zookeeper-3.8.0-bin

```

Create a Zookeeper directory on each node.

```console

mkdir  /tmp/zookeeper

echo 1 >> /tmp/zookeeper/myid

```

## Install Kafka:

Next, Install Kafka on the 3 nodes as shown below.

```console

mkdir Kafka

wget https://dlcdn.apache.org/kafka/3.2.3/kafka_2.13-3.2.3.tgz

tar -xzf kafka_2.13-3.2.3.tgz

cd kafka_2.13-3.2.3

```
Create a Kafka log directory on each node.

```console

mkdir /tmp/kafka-logs

```


