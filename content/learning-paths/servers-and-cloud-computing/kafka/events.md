---
# User change
title: "Verify that the Kafka Cluster is working"

weight: 5

layout: "learningpathall"


---

After successfully setting up a 3 node Kafka cluster, verify it works by creating a topic and storing the events. Follow the steps below to create a topic, write some events into the topic, and then read the events.

## Install Kafka

Run the commands shown to download and setup Kafka on client machine:

```console
mkdir kafka_node3
cd kafka_node3
wget https://dlcdn.apache.org/kafka/3.7.0/kafka_2.13-3.7.0.tgz
tar -xzf kafka_2.13-3.7.0.tgz
cd  kafka_2.13-3.7.0
```

## Create a topic

Open a terminal on the client machine and run the command shown below. Replace `kf_1_ip`, `kf_2_ip` and `kf_3_ip` with the IP addresses of the 3 nodes running the Kafka server.

```console
./bin/kafka-topics.sh --create --topic test-topic --bootstrap-server kf_1_ip:9092,kf_2_ip:9092,kf_3_ip:9092 --replication-factor 3 --partitions 64
```

## Describe the topic created:

Run this command in the same client terminal where the topic was created. Replace `kf_1_ip`, `kf_2_ip` and `kf_3_ip` with the IP addresses of the 3 nodes running the Kafka server.

```console
./bin/kafka-topics.sh --topic test-topic --bootstrap-server kf_1_ip:9092,kf_2_ip:9092,kf_3_ip:9092 --describe
```

The output from this command is shown below:

```output
ubuntu@ip-172-31-19-179:~/kafka_node/kafka_2.13-3.2.3$ ./bin/kafka-topics.sh --topic test-topic --bootstrap-server 3.144.181.100:9092,3.15.19.197:9092,18.191.61.20:9092 --describe
Topic: test-topic       TopicId: WMy9lruTQC6uuuuyep-C_Q PartitionCount: 64      ReplicationFactor: 3    Configs: segment.bytes=1073741824
        Topic: test-topic       Partition: 0    Leader: 3       Replicas: 3,1,2 Isr: 3,1,2
        Topic: test-topic       Partition: 1    Leader: 1       Replicas: 1,2,3 Isr: 1,2,3
        Topic: test-topic       Partition: 2    Leader: 2       Replicas: 2,3,1 Isr: 2,3,1
```

## Run the producer client to write events into the created topic:

Run this command in the same client terminal where the topic was created. Replace `kf_1_ip`, `kf_2_ip` and `kf_3_ip` with the IP addresses of the 3 nodes running the Kafka server.

```console
./bin/kafka-console-producer.sh --topic test-topic --bootstrap-server kf_1_ip:9092,kf_2_ip:9092,kf_3_ip:9092
```
Write a message, example shown below:

```output
ubuntu@ip-172-31-19-179:~/kafka_node/kafka_2.13-3.2.3$ ./bin/kafka-console-producer.sh --topic test-topic --bootstrap-server 3.144.181.100:9092,3.15.19.197:9092,18.191.61.20:9092
>This is the first message written on producer
>
```

## Run the consumer client to read all the events created:

Open a new terminal on the client machine to run the consumer client. Replace `kf_1_ip`, `kf_2_ip` and `kf_3_ip` with the IP addresses of the 3 nodes running the Kafka server.

```console
./bin/kafka-console-consumer.sh --topic test-topic --bootstrap-server kf_1_ip:9092,kf_2_ip:9092,kf_3_ip:9092
```

The same message you wrote in the producer client terminal should appear on the consumer client. Example shown below:

```output
ubuntu@ip-172-31-19-179:~/kafka_node/kafka_2.13-3.2.3$ ./bin/kafka-console-consumer.sh --topic test-topic --bootstrap-server 3.144.181.100:9092,3.15.19.197:9092,18.191.61.20:9092
This is the first message written on producer
```

You have now successfully verified that the Kafka cluster is working.
