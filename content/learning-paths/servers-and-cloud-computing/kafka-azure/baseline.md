---
title: Baseline Testing
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Run a Baseline test with Kafka

After installing Kafka on your Arm64 virtual machine, you can perform a simple baseline test to validate that Kafka runs correctly and produces the expected output. 

Kafka 4.1.0 uses **KRaft**, which integrates the control and data planes, eliminating the need for a separate ZooKeeper instance.

We need 4 terminals to complete this test. The first will start the Kafka server, the second will create a topic, and the final two will send and receive messages, respectively.

### Initial Setup: Configure & Format KRaft
**KRaft** is Kafka's new metadata protocol that integrates the responsibilities of ZooKeeper directly into Kafka, simplifying deployment and improving scalability by making the brokers self-managing.

First, you must configure your `server.properties` file for KRaft and format the storage directory. These steps are done only once.

**1. Edit the Configuration File**: Open your `server.properties` file.

```console
nano /opt/kafka/config/server.properties
```

**2. Add/Modify KRaft Properties:** Ensure the following lines are present and correctly configured for a single-node setup.

This configuration file sets up a single Kafka server to act as both a **controller** (managing cluster metadata) and a broker (handling data), running in **KRaft** mode. It defines the node's unique ID and specifies the local host as the sole participant in the **controller** quorum.

```java
process.roles=controller,broker
node.id=1
controller.quorum.voters=1@localhost:9093
listeners=PLAINTEXT://:9092,CONTROLLER://:9093
advertised.listeners=PLAINTEXT://localhost:9092
log.dirs=/tmp/kraft-combined-logs
```
**3. Format the Storage Directory:** Use the `kafka-storage.sh` tool to format the metadata directory.

```console
bin/kafka-storage.sh format -t $(bin/kafka-storage.sh random-uuid) -c config/server.properties
```
You should see an output similar to:

```output
Formatting metadata directory /tmp/kraft-combined-logs with metadata.version 4.1-IV1.
```

Now, Perform the Baseline Test

### Terminal 1 – Start Kafka Broker
This command starts the Kafka broker (the main server that sends and receives messages) in KRaft mode. Keep this terminal open.

```console
cd /opt/kafka
bin/kafka-server-start.sh config/server.properties
```
### Terminal 2 – Create a Topic
This command creates a new Kafka topic named `test-topic-kafka` (like a channel where messages will be stored and shared) with 1 partition and 1 copy (replica).

```console
cd /opt/kafka
bin/kafka-topics.sh --create --topic test-topic-kafka --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
```
You should see output similar to:

```output
Created topic test-topic-kafka.
```

- **Verify topic**

```console
bin/kafka-topics.sh --list --bootstrap-server localhost:9092
```
You should see output similar to:

```output
__consumer_offsets
test-topic-kafka
```

### Terminal 3 – Console Producer (Write Message)
This command starts the **Kafka Producer**, which lets you type and send messages into the `test-topic-kafka` topic. For example, when you type `hello from azure vm`, this message will be delivered to any Kafka consumer subscribed to that topic.

```console
cd /opt/kafka
bin/kafka-console-producer.sh --topic test-topic-kafka --bootstrap-server localhost:9092
```
You should see an empty prompt where you can start typing. Type `hello from azure arm vm` and press **Enter**.

### Terminal 4 – Console Consumer (Read Message)
This command starts the **Kafka Consumer**, which listens to the `test-topic-kafka` topic and displays all messages from the beginning.

```console
cd /opt/kafka
bin/kafka-console-consumer.sh --topic test-topic-kafka --from-beginning --bootstrap-server localhost:9092
```

You should see your message `hello from azure arm vm` displayed in this terminal, confirming that the producer's message was successfully received.

Now you can proceed to benchmarking Kafka’s performance on the Azure Cobalt 100 Arm virtual machine.
