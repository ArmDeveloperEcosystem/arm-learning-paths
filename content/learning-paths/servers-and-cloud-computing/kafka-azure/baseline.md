---
title: Run baseline testing with Kafka on Azure Arm VM
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Run a baseline test with Kafka

After installing Apache Kafka 4.1.0 on your Azure Cobalt 100 Arm64 virtual machine, you can perform a baseline test to verify that Kafka runs correctly and that messages can be produced and consumed end-to-end.
Kafka 4.1.0 introduces KRaft mode (Kafka Raft Metadata mode), which integrates the control and data planes, eliminating the need for ZooKeeper.

This simplifies deployment, reduces latency, and provides a unified, self-managed Kafka cluster architecture.

To run this baseline test, open four terminal sessions:

- **Terminal 1:** Start the Kafka broker in KRaft mode.
- **Terminal 2:** Create a topic.
- **Terminal 3:** Send messages as the producer.
- **Terminal 4:** Read messages as the consumer.

Each terminal has a specific role, helping you verify that Kafka works end-to-end on your Arm64 VM.

## Configure and format KRaft

KRaft (Kafka Raft) mode replaces ZooKeeper by managing metadata directly within the Kafka broker. This change improves scalability, reduces external dependencies, and speeds up controller failover in distributed clusters.

Before you start Kafka in KRaft mode, you need to configure the broker and initialize the storage directory. You only need to do this once for each broker.

## Edit the configuration file to update KRaft properties

Use an editor to open the Kafka configuration file at `/opt/kafka/config/server.properties`. Use `sudo` so that you can save the file. 

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

## Format the storage directory

Format the metadata storage directory using the kafka-storage.sh tool. This initializes KRaft's internal Raft logs with a unique cluster ID.

```console
bin/kafka-storage.sh format -t $(bin/kafka-storage.sh random-uuid) -c config/server.properties
```

You should see output similar to:

```output
Formatting metadata directory /tmp/kraft-combined-logs with metadata.version 4.1-IV1.
```

This confirms that the Kafka storage directory has been successfully formatted and that the broker is ready to start in KRaft mode.

## Perform the baseline test

With Kafka 4.1.0 installed and configured in KRaft mode, you’re now ready to run a baseline test to verify that the Kafka broker starts correctly, topics can be created, and message flow works as expected.

You’ll use multiple terminals for this test:
Terminal 1: start the Kafka broker
Terminal 2: create and verify a topic
Terminal 3: send messages (Producer)
Terminal 4: read messages (Consumer)

## Terminal 1 - start Kafka broker

Start the Kafka broker (the main server process responsible for managing topics and handling messages) in KRaft mode:

```console
cd /opt/kafka
bin/kafka-server-start.sh config/server.properties
```

Keep this terminal open and running. The broker process must stay active for all subsequent commands.

## Terminal 2 - create a topic

Open a new terminal window. Create a topic named test-topic-kafka, which acts as a logical channel where producers send and consumers receive messages:

```console
cd /opt/kafka
bin/kafka-topics.sh --create --topic test-topic-kafka --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
```

You should see output similar to:

```output
Created topic test-topic-kafka.
```

## Verify topic creation

List available topics to confirm that your new topic was created successfully. Run the following command:

```console
bin/kafka-topics.sh --list --bootstrap-server localhost:9092
```

The expected output is:

```output
__consumer_offsets
test-topic-kafka
```

If you see `test-topic-kafka` in the list, your topic was created and is ready for use.

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

## Terminal 3 - console producer (write message)

In this step, you’ll start the Kafka Producer, which publishes messages to the topic test-topic-kafka. The producer acts as the data source, sending messages to the Kafka broker.

```console
cd /opt/kafka
bin/kafka-console-producer.sh --topic test-topic-kafka --bootstrap-server localhost:9092
```

After running the command, you'll see an empty prompt. This means the producer is ready to send data. Type the following message and press Enter:

```output
hello from azure arm vm
```

Each line you type is sent as a message to the Kafka topic and stored on disk by the broker.

## Terminal 4 - console consumer (read message)

Next, open another terminal and start the Kafka Consumer, which subscribes to the same topic (test-topic-kafka) and reads messages from the beginning of the log:

```console
cd /opt/kafka
bin/kafka-console-consumer.sh --topic test-topic-kafka --from-beginning --bootstrap-server localhost:9092
```

If Kafka is working correctly, you should immediately see your message `hello from azure arm vm` displayed.

You've now completed a full end-to-end Kafka validation test on your Azure Cobalt 100 Arm64 VM, verifying producer, broker, and consumer communication.

Now you can proceed to benchmarking Kafka's performance on the Azure Cobalt 100 Arm virtual machine.
