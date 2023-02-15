---
# User change
title: "Setup a 3 node Kafka Cluster"

weight: 4

layout: "learningpathall"


---

## Prerequisites
* Ensure the 3 Node Zookeeper cluster is running.

## Setup 3 node Kafka Cluster:

### Node 1:

```console

mkdir kafka_node1

cd kafka_node1

wget https://dlcdn.apache.org/kafka/3.2.3/kafka_2.13-3.2.3.tgz

tar -xzf kafka_2.13-3.2.3.tgz

cd  kafka_2.13-3.2.3

```
We need to setup the file **config/server.properties** as shown below on each of the 3 nodes of the Kafka cluster. Below is the node 1 **config/server.properties** file.

```console

broker.id=1 

listeners=PLAINTEXT://:9092 

log.dirs=/tmp/kafka-logs 

zookeeper.connect=zk_1_ip:2181,zk_2_ip:2181,zk_3_ip:2181 

```

### Node 2:

  Run the following on Kafka node 2.

```console

mkdir kafka_node2

cd kafka_node2

wget https://dlcdn.apache.org/kafka/3.2.3/kafka_2.13-3.2.3.tgz

tar -xzf kafka_2.13-3.2.3.tgz

cd  kafka_2.13-3.2.3

```
Below is the node 2 **config/server.properties** file.

```console

broker.id=2 

listeners=PLAINTEXT://:9092

log.dirs=/tmp/kafka-logs

zookeeper.connect=zk_1_ip:2181,zk_2_ip:2181,zk_3_ip:2181

```

### Node 3:

  Run the following on Kafka node 3.

```console

mkdir kafka_node3

cd kafka_node3

wget https://dlcdn.apache.org/kafka/3.2.3/kafka_2.13-3.2.3.tgz

tar -xzf kafka_2.13-3.2.3.tgz

cd  kafka_2.13-3.2.3

```
Below is the node 3 **config/server.properties** file.

```console

broker.id=3 

listeners=PLAINTEXT://:9092 

log.dirs=/tmp/kafka-logs

zookeeper.connect=zk_1_ip:2181,zk_2_ip:2181,zk_3_ip:2181

```

### Run the following command on each of the 3 nodes:

```console

mkdir /tmp/kafka-logs

```

### Start Kafka server on each node:

```console

bin/kafka-server-start.sh config/server.properties

```
In the next section, we will verify that the Kafka cluster is working.

