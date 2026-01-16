---
title: RabbitMQ use case 2 - WhatsApp Notification
weight: 11 

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

In this section you'll implement a real-world asynchronous messaging pattern where RabbitMQ processes WhatsApp notifications reliably using a worker-based architecture.

## Why use RabbitMQ for WhatsApp notification

In production systems, sending WhatsApp notifications must be:
- Reliable
- Asynchronous
- Independent of the main application flow

RabbitMQ acts as a message broker to decouple message production from message consumption.

The architecture follows this flow:

- Application publishes a message to RabbitMQ
- RabbitMQ routes the message to a queue
- A Python worker consumes the message
- The worker simulates sending a WhatsApp notification

### Prerequisites

- GCP SUSE Arm64 virtual machine
- RabbitMQ is installed and running
- RabbitMQ Management Plugin enabled
- Python 3.8+
- `pika` Python client library installed

## Install Python dependencies

Install Python and the RabbitMQ Python client needed to build a consumer.

```console
sudo zypper install -y python3 python3-pip
pip3 install pika
```

## Understand the RabbitMQ topology

This use case uses a direct exchange topology for exact-match routing.

**Exchanges:**
- `notifications` (direct): Routes WhatsApp notification messages based on an exact routing key match.

**Queue:**
- `whatsapp.notifications` (durable): Stores WhatsApp messages persistently until they are consumed by a worker.

**Binding:**
- Exchange: `notifications`
- Routing key: `whatsapp` 
- Queue: `whatsapp.notifications`

This ensures only WhatsApp-related messages are routed to the final destination for processing.

## Declare RabbitMQ resources

Create the required exchange, queue, and binding for WhatsApp notifications.
  
```console
./rabbitmqadmin declare exchange \
  name=notifications \
  type=direct \
  durable=true

./rabbitmqadmin declare queue \
  name=whatsapp.notifications \
  durable=true

./rabbitmqadmin declare binding \
  source=notifications \
  destination=whatsapp.notifications \
  routing_key=whatsapp
```

Each command confirms successful creation.

## Validate the setup

Verify that RabbitMQ resources exist and are correctly connected.

```console
./rabbitmqadmin list queues name messages
./rabbitmqadmin list exchanges name type
./rabbitmqadmin list bindings
```

- `list queues` displays all queues along with the number of messages currently stored in each queue.
- `list exchanges` lists all exchanges and their types, allowing verification of correct exchange configuration.
- `list bindings` shows how exchanges, queues, and routing keys are connected.

The output shows you the following:

- `notifications` exchange of type direct
- `whatsapp.notifications` durable queue
- Correct routing key binding (`whatsapp`)
- Zero or more queued messages

This confirms topology correctness before consuming messages.

```output
> ./rabbitmqadmin list queues name messages
+------------------------+----------+
|          name          | messages |
+------------------------+----------+
| jobs                   | 0        |
| order.events           | 1        |
| testqueue              | 1        |
| whatsapp.notifications | 0        |
+------------------------+----------+

> ./rabbitmqadmin list exchanges name type
+--------------------+---------+
|        name        |  type   |
+--------------------+---------+
|                    | direct  |
| amq.direct         | direct  |
| amq.fanout         | fanout  |
| amq.headers        | headers |
| amq.match          | headers |
| amq.rabbitmq.trace | topic   |
| amq.topic          | topic   |
| events             | topic   |
| notifications      | direct  |
+--------------------+---------+

> ./rabbitmqadmin list bindings
+---------------+------------------------+------------------------+
|    source     |      destination       |      routing_key       |
+---------------+------------------------+------------------------+
|               | jobs                   | jobs                   |
|               | order.events           | order.events           |
|               | testqueue              | testqueue              |
|               | whatsapp.notifications | whatsapp.notifications |
| events        | order.events           | order.*                |
| notifications | whatsapp.notifications | whatsapp               |
+---------------+------------------------+------------------------+
```

## Implement the WhatsApp worker

Create a Python consumer (worker) that processes WhatsApp notification messages from the queue.

Create a file named `whatsapp_worker.py` with the following code:

```python
import pika
import json
import time

RABBITMQ_HOST = "localhost"
RABBITMQ_VHOST = "/"
RABBITMQ_USER = "guest"
RABBITMQ_PASS = "guest"
QUEUE_NAME = "whatsapp.notifications"

credentials = pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASS)

parameters = pika.ConnectionParameters(
    host=RABBITMQ_HOST,
    virtual_host=RABBITMQ_VHOST,
    credentials=credentials,
    heartbeat=60
)

print("[DEBUG] Connecting to RabbitMQ...")
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

print("[DEBUG] Declaring queue...")
channel.queue_declare(queue=QUEUE_NAME, durable=True)

print("[DEBUG] Setting QoS...")
channel.basic_qos(prefetch_count=1)

print("WhatsApp Worker started. Waiting for messages...")

def send_whatsapp(ch, method, properties, body):
    data = json.loads(body.decode())
    print(f"[Worker] Sending WhatsApp message to {data['phone']}")
    print(f"[Worker] Message content: {data['message']}")

    # Simulate external WhatsApp API call
    time.sleep(1)

    print("[Worker] Message sent successfully")
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(
    queue=QUEUE_NAME,
    on_message_callback=send_whatsapp,
    auto_ack=False
)

print("[DEBUG] Starting consumer loop (this should block)...")
channel.start_consuming()
```

## Start the worker

Run the worker in a dedicated terminal session:

```console
python3 whatsapp_worker.py
```

The worker runs correctly and waits for messages without exiting.

The output is similar to:

```output
[DEBUG] Connecting to RabbitMQ...
[DEBUG] Declaring queue...
[DEBUG] Setting QoS...
WhatsApp Worker started. Waiting for messages...
[DEBUG] Starting consumer loop (this should block)...
```

The process blocks without returning to the shell prompt.

## Publish a test message

Open another SSH terminal and publish a WhatsApp notification message to RabbitMQ.

```console
./rabbitmqadmin publish \
  exchange=notifications \
  routing_key=whatsapp \
  payload='{"phone":"+911234567890","message":"Hello from RabbitMQ"}'
```

The output appears in the first terminal running `whatsapp_worker.py`:

```output
[Worker] Sending WhatsApp message to +911234567890
[Worker] Message content: Hello from RabbitMQ
[Worker] Message sent successfully
```

## Validate message consumption

The worker terminal displays the complete log:

```output
[DEBUG] Connecting to RabbitMQ...
[DEBUG] Declaring queue...
[DEBUG] Setting QoS...
WhatsApp Worker started. Waiting for messages...
[DEBUG] Starting consumer loop (this should block)...
[Worker] Sending WhatsApp message to +911234567890
[Worker] Message content: Hello from RabbitMQ
[Worker] Message sent successfully
```

This confirms:

- Message routing works correctly
- Queue consumption is successful
- Manual acknowledgments are applied

This validates the end-to-end message flow.

## Verify queue state

```console
./rabbitmqadmin list queues name messages consumers
```

The output is similar to:

```output
+------------------------+----------+-----------+
|          name          | messages | consumers |
+------------------------+----------+-----------+
| jobs                   | 0        | 0         |
| order.events           | 2        | 0         |
| testqueue              | 1        | 0         |
| whatsapp.notifications | 0        | 1         |
+------------------------+----------+-----------+
```

This confirms:

- Messages were consumed successfully
- One active consumer is connected
- No backlog remains in the queue

## What you've accomplished

In this use case, you:
- Configured a direct exchange topology for exact-match routing
- Created durable queues and bindings for WhatsApp notifications
- Implemented a Python worker using the `pika` library
- Published test messages and validated end-to-end message flow
- Confirmed reliable message consumption with manual acknowledgments

This pattern demonstrates how RabbitMQ enables asynchronous, decoupled communication for notification systems on Arm-based cloud platforms.
