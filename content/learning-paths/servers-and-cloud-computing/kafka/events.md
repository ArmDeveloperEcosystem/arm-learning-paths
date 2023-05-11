---
# User change
title: "Verify that the Kafka Cluster is working"

weight: 5

layout: "learningpathall"


---

After successfully setting up a 3 node Kafka cluster, verify it works by creating a topic and storing the events. Follow the steps below to create a topic, write some events into the topic, and then read the events.

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

![describe](https://user-images.githubusercontent.com/66300308/199558769-69cb218c-6360-4289-9a7f-cca6893cfbeb.png)

## Run the producer client to write events into the created topic:

Run this command in the same client terminal where the topic was created. Replace `kf_1_ip`, `kf_2_ip` and `kf_3_ip` with the IP addresses of the 3 nodes running the Kafka server.

```console
./bin/kafka-console-producer.sh --topic test-topic --bootstrap-server kf_1_ip:9092,kf_2_ip:9092,kf_3_ip:9092
```
Write a message, example shown below:

![producer](https://user-images.githubusercontent.com/66300308/199559053-3f8b4ea7-88b6-4f90-8cc6-45bf0ca95340.png)

## Run the consumer client to read all the events created:

Open a new terminal on the client machine to run the consumer client. Replace `kf_1_ip`, `kf_2_ip` and `kf_3_ip` with the IP addresses of the 3 nodes running the Kafka server.

```console
./bin/kafka-console-consumer.sh --topic test-topic --bootstrap-server kf_1_ip:9092,kf_2_ip:9092,kf_3_ip:9092
```

The same message you wrote in the producer client terminal should appear on the consumer client. Example shown below:

![consumer](https://user-images.githubusercontent.com/66300308/199558517-4d52e7b9-3952-4d54-b8c5-21d36406bad7.png)

You have now successfully verified that the Kafka cluster is working.
