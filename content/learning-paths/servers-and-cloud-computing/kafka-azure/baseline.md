---
title: Baseline Testing
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Run a Baseline test with Kafka

After installing Apache Kafka 4.1.0 on your Azure Cobalt 100 Arm64 virtual machine, you can perform a baseline test to verify that Kafka runs correctly and that messages can be produced and consumed end-to-end.
Kafka 4.1.0 introduces KRaft mode (Kafka Raft Metadata mode), which integrates the control and data planes, eliminating the need for ZooKeeper.
This simplifies deployment, reduces latency, and provides a unified, self-managed Kafka cluster architecture.

To perform this baseline test, you will use four terminal sessions:
Terminal 1: Start the Kafka broker (in KRaft mode).
Terminal 2: Create a topic.
Terminal 3: Send messages (Producer).
Terminal 4: Read messages (Consumer).

### Initial Setup: Configure & Format KRaft
KRaft (Kafka Raft) replaces ZooKeeper by embedding metadata management directly into the Kafka broker.
This improves scalability, reduces external dependencies, and speeds up controller failover in distributed clusters.
Before starting Kafka in KRaft mode, configure and initialize the storage directory. These steps are required only once per broker.

1. Edit the Configuration File
Open the Kafka configuration file in an editor:

```console
vi /opt/kafka/config/server.properties
```

2. Add or Modify KRaft Properties
Ensure the following configuration entries are present for a single-node KRaft setup:

```java
process.roles=controller,broker
node.id=1
controller.quorum.voters=1@localhost:9093
listeners=PLAINTEXT://:9092,CONTROLLER://:9093
advertised.listeners=PLAINTEXT://localhost:9092
log.dirs=/tmp/kraft-combined-logs
```
This configuration file sets up a single Kafka server to act as both a controller (managing cluster metadata) and a broker (handling data), running in KRaft mode. It defines the node's unique ID and specifies the local host as the sole participant in the controller quorum.

3. Format the Storage Directory
Format the metadata storage directory using the kafka-storage.sh tool. This initializes KRaft’s internal Raft logs with a unique cluster ID.

```console
bin/kafka-storage.sh format -t $(bin/kafka-storage.sh random-uuid) -c config/server.properties
```
You should see output similar to:

```output
Formatting metadata directory /tmp/kraft-combined-logs with metadata.version 4.1-IV1.
```
This confirms that the Kafka storage directory has been successfully formatted and that the broker is ready to start in KRaft mode.

## Perform the Baseline Test
With Kafka 4.1.0 installed and configured in KRaft mode, you’re now ready to run a baseline test to verify that the Kafka broker starts correctly, topics can be created, and message flow works as expected.

You’ll use multiple terminals for this test:
Terminal 1: Start the Kafka broker.
Terminal 2: Create and verify a topic.
Terminal 3: Send messages (Producer).
Terminal 4: Read messages (Consumer).

### Terminal 1 – Start Kafka Broker
Start the Kafka broker (the main server process responsible for managing topics and handling messages) in KRaft mode:

```console
cd /opt/kafka
bin/kafka-server-start.sh config/server.properties
```
Keep this terminal open and running. The broker process must stay active for all subsequent commands.

### Terminal 2 – Create a Topic
Open a new terminal window. Create a topic named test-topic-kafka, which acts as a logical channel where producers send and consumers receive messages:

```console
cd /opt/kafka
bin/kafka-topics.sh --create --topic test-topic-kafka --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
```
You should see output similar to:

```output
Created topic test-topic-kafka.
```

**Verify Topic Creation**
List available topics to confirm that your new topic was created successfully:

```console
bin/kafka-topics.sh --list --bootstrap-server localhost:9092
```
You should see output similar to:

```output
__consumer_offsets
test-topic-kafka
```
Kafka is now running, and you’ve successfully created and verified a topic.
Next, you’ll use Terminal 3 to produce messages and Terminal 4 to consume messages, completing the baseline functional test on your Arm64 environment.

### Terminal 3 – Console Producer (Write Message)
In this step, you’ll start the Kafka Producer, which publishes messages to the topic test-topic-kafka. The producer acts as the data source, sending messages to the Kafka broker.

```console
cd /opt/kafka
bin/kafka-console-producer.sh --topic test-topic-kafka --bootstrap-server localhost:9092
```
After running the command, you’ll see an empty prompt. This means the producer is ready to send data.
Type the following message and press Enter:

```output
hello from azure arm vm
```
Each line you type is sent as a message to the Kafka topic and stored on disk by the broker.

### Terminal 4 – Console Consumer (Read Message)
Next, open another terminal and start the Kafka Consumer, which subscribes to the same topic (test-topic-kafka) and reads messages from the beginning of the log.

```console
cd /opt/kafka
bin/kafka-console-consumer.sh --topic test-topic-kafka --from-beginning --bootstrap-server localhost:9092
```
If Kafka is working correctly, you should immediately see your message `hello from azure arm vm` displayed:


Now you can proceed to benchmarking Kafka’s performance on the Azure Cobalt 100 Arm virtual machine.
`hello from azure arm vm`
