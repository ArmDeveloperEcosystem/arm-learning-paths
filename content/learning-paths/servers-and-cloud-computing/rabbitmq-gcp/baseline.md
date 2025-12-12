---
title: RabbitMQ Baseline Testing on Google Axion C4A Arm Virtual Machine
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## RabbitMQ Baseline Validation on GCP SUSE Arm64 VM
This document defines a **baseline validation procedure** for RabbitMQ installed on a **Google Cloud SUSE Linux Arm64 virtual machine**.  
The purpose of this baseline is to confirm:

- RabbitMQ service health
- Management plugin availability
- Queue operations (create, publish, consume)
- CLI tooling functionality (`rabbitmqctl` and `rabbitmqadmin`)

### Check RabbitMQ Node Status
Verify that the RabbitMQ node is operational and healthy.

```console
sudo rabbitmqctl status
```
- Node status reports RabbitMQ is running
- No active alarms
- Listeners are active on ports 5672 and 15672
- Memory and disk space are within safe limits

### Verify Enabled Plugins
Confirm that the RabbitMQ management plugins are enabled.

```console
sudo rabbitmq-plugins list | grep management
```

You should see an output similar to:
```output
[  ] rabbitmq_federation_management          4.2.0
[E*] rabbitmq_management                     4.2.0
[e*] rabbitmq_management_agent               4.2.0
[  ] rabbitmq_shovel_management              4.2.0
[  ] rabbitmq_stream_management              4.2.0
```

### Validate RabbitMQ Listeners
Ensure RabbitMQ is listening on the required ports.

```console
sudo rabbitmqctl status | grep -A5 Listeners
```

You should see an output similar to:
```output
Listeners

Interface: [::], port: 15672, protocol: http, purpose: HTTP API
Interface: [::], port: 25672, protocol: clustering, purpose: inter-node and CLI tool communication
Interface: [::], port: 5672, protocol: amqp, purpose: AMQP 0-9-1 and AMQP 1.0
```

### Download RabbitMQ Admin CLI Tool
Download the rabbitmqadmin CLI tool from the local management endpoint.

```console
curl -u guest:guest http://localhost:15672/cli/rabbitmqadmin -o rabbitmqadmin
```
**Make the tool executable:**

```console
chmod +x rabbitmqadmin
```
### Validate Queue Creation
Create a test queue to validate write operations.

```console
./rabbitmqadmin declare queue name=testqueue durable=false
```

You should see an output similar to:
```output
queue declared
```

### Publish a Test Message
Send a test message to the queue.

```console
./rabbitmqadmin publish exchange=amq.default routing_key=testqueue payload="hello world"
```

You should see an output similar to:
```output
Message published
```

### Consume Message From Queue
Retrieve messages from the queue to verify read functionality.

```console
./rabbitmqadmin get queue=testqueue
```

You should see an output similar to:
```output
+-------------+----------+---------------+-------------+---------------+------------------+------------+-------------+
| routing_key | exchange | message_count |   payload   | payload_bytes | payload_encoding | properties | redelivered |
+-------------+----------+---------------+-------------+---------------+------------------+------------+-------------+
| testqueue   |          | 0             | hello world | 11            | string           |            | False       |
+-------------+----------+---------------+-------------+---------------+------------------+------------+-------------+
```

### Verify Queue State
Confirm that the queue is empty after consumption.

```console
./rabbitmqadmin list queues name messages
```

You should see an output similar to:
```output
+--------------+----------+
|     name     | messages |
+--------------+----------+
| jobs         | 0        |
| order.events | 1        |
| testqueue    | 1        |
```

### Baseline validation summary

- RabbitMQ node is running and healthy
- The management plugin is enabled and accessible
- Queue creation is successful
- Message publishing works as expected
- Message consumption functions correctly
- CLI tools operate without error

This confirms a successful baseline validation of RabbitMQ on a GCP SUSE Arm64 virtual machine.
