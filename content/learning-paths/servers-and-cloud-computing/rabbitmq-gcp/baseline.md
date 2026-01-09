---
title: RabbitMQ Baseline Testing on Google Axion C4A Arm Virtual Machine
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## RabbitMQ baseline validation on GCP SUSE Arm64 VM
This document defines a **baseline validation procedure** for RabbitMQ installed on a **Google Cloud SUSE Linux Arm64 virtual machine**.  
The purpose of this baseline is to confirm:

- RabbitMQ service health
- Management plugin availability
- Queue operations (create, publish, consume)
- CLI tooling functionality (`rabbitmqctl` and `rabbitmqadmin`)

### Check RabbitMQ node status
Verify that the RabbitMQ node is operational and healthy.

```console
sudo rabbitmqctl status
```
- Node status reports RabbitMQ is running
- No active alarms
- Listeners are active on ports 5672 and 15672
- Memory and disk space are within safe limits

### Verify enabled plugins
Confirm that the RabbitMQ management plugins are enabled:

```console
sudo rabbitmq-plugins list | grep management
```

The output is similar to:
```output
[  ] rabbitmq_federation_management          4.2.0
[E*] rabbitmq_management                     4.2.0
[e*] rabbitmq_management_agent               4.2.0
[  ] rabbitmq_shovel_management              4.2.0
[  ] rabbitmq_stream_management              4.2.0
```

### Validate RabbitMQ listeners
Ensure RabbitMQ is listening on the required ports:

```console
sudo rabbitmqctl status | grep -A5 Listeners
```

The output is similar to:
```output
Listeners

Interface: [::], port: 15672, protocol: http, purpose: HTTP API
Interface: [::], port: 25672, protocol: clustering, purpose: inter-node and CLI tool communication
Interface: [::], port: 5672, protocol: amqp, purpose: AMQP 0-9-1 and AMQP 1.0
```

### Download RabbitMQ admin CLI tool
Download the rabbitmqadmin CLI tool from the local management endpoint.

```console
curl -u guest:guest http://localhost:15672/cli/rabbitmqadmin -o rabbitmqadmin
```
**Make the tool executable:**

```console
chmod +x rabbitmqadmin
```
### Validate queue creation
Create a test queue to validate write operations:

```console
./rabbitmqadmin declare queue name=testqueue durable=false
```

The output is similar to:
```output
queue declared
```

### Publish a test message
Send a test message to the queue:

```console
./rabbitmqadmin publish exchange=amq.default routing_key=testqueue payload="hello world"
```

The output is similar to:
```output
Message published
```

### Consume message from queue
Retrieve messages from the queue to verify read functionality:

```console
./rabbitmqadmin get queue=testqueue
```

The output is similar to:
```output
+-------------+----------+---------------+-------------+---------------+------------------+------------+-------------+
| routing_key | exchange | message_count |   payload   | payload_bytes | payload_encoding | properties | redelivered |
+-------------+----------+---------------+-------------+---------------+------------------+------------+-------------+
| testqueue   |          | 0             | hello world | 11            | string           |            | False       |
+-------------+----------+---------------+-------------+---------------+------------------+------------+-------------+
```

### Verify queue state
Confirm that the queue is empty after consumption:

```console
./rabbitmqadmin list queues name messages
```

The output is similar to:
```output
+--------------+----------+
|     name     | messages |
+--------------+----------+
| jobs         | 0        |
| order.events | 1        |
| testqueue    | 1        |
```

## What you've accomplished and what's next

You've successfully validated RabbitMQ on your Google Cloud SUSE Arm64 virtual machine. The node is running and healthy, the management plugin is enabled and accessible, and queue operations (creation, publishing, consumption) work correctly. Next, you'll explore practical use cases that demonstrate RabbitMQ's capabilities for event-driven architectures and notification systems.
