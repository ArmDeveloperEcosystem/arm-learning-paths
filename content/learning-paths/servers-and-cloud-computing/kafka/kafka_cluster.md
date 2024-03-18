---
# User change
title: "Setup a 3 node Kafka Cluster"

weight: 4

layout: "learningpathall"


---

## Setup 3 node Kafka Cluster:

In this section, you will setup a Kafka cluster on 3 Arm machines. Ensure that the [3 Node Zookeeper cluster](/learning-paths/servers-and-cloud-computing/kafka/zookeeper_cluster) is running.

### Node 1:

Run the commands shown to download and setup Kafka on node 1:

```console
mkdir kafka_node1
cd kafka_node1
wget https://dlcdn.apache.org/kafka/3.7.0/kafka_2.13-3.7.0.tgz
tar -xzf kafka_2.13-3.7.0.tgz
cd  kafka_2.13-3.7.0
```
Use a file editor of your choice and replace the contents in `config/server.properties` with the contents below:.
Replace `zk_1_ip`,`zk_2_ip` and `zk_3_ip` with the IP addresses of the 3 Zookeeper nodes you setup.

```console
broker.id=1 

listeners=PLAINTEXT://:9092 

log.dirs=/tmp/kafka-logs 

zookeeper.connect=zk_1_ip:2181,zk_2_ip:2181,zk_3_ip:2181 
```

Create a directory for the log files:

```console
mkdir /tmp/kafka-logs
```

Start Kafka server on node 1:

```console
bin/kafka-server-start.sh config/server.properties
```

### Node 2:

Run the commands shown to download and setup Kafka on node 2:

```console
mkdir kafka_node2
cd kafka_node2
wget https://dlcdn.apache.org/kafka/3.7.0/kafka_2.13-3.7.0.tgz
tar -xzf kafka_2.13-3.7.0.tgz
cd  kafka_2.13-3.7.0
```
Use a file editor of your choice and replace the contents in `config/server.properties` with the contents below:.
Replace `zk_1_ip`,`zk_2_ip` and `zk_3_ip` with the IP addresses of the 3 Zookeeper nodes you setup.

```console
broker.id=2 

listeners=PLAINTEXT://:9092

log.dirs=/tmp/kafka-logs

zookeeper.connect=zk_1_ip:2181,zk_2_ip:2181,zk_3_ip:2181
```

Create a directory for the log files:

```console
mkdir /tmp/kafka-logs
```

Start Kafka server on node 2:

```console
bin/kafka-server-start.sh config/server.properties
```

### Node 3:

Run the commands shown to download and setup Kafka on node 3:

```console
mkdir kafka_node3
cd kafka_node3
wget https://dlcdn.apache.org/kafka/3.7.0/kafka_2.13-3.7.0.tgz
tar -xzf kafka_2.13-3.7.0.tgz
cd  kafka_2.13-3.7.0
```
Use a file editor of your choice and replace the contents in `config/server.properties` with the contents below:.
Replace `zk_1_ip`,`zk_2_ip` and `zk_3_ip` with the IP addresses of the 3 Zookeeper nodes you setup.

```console
broker.id=3 

listeners=PLAINTEXT://:9092 

log.dirs=/tmp/kafka-logs

zookeeper.connect=zk_1_ip:2181,zk_2_ip:2181,zk_3_ip:2181
```

Create a directory for the log files:

```console
mkdir /tmp/kafka-logs
```

Start Kafka server on node 3:

```console
bin/kafka-server-start.sh config/server.properties
```

In the next section, you will verify that the Kafka cluster is working.

