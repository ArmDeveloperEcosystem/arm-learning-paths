---
title: RabbitMQ Use Case 1 – Event Processing with Python Workers
weight: 6 

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## RabbitMQ Use Case – Event Processing with Python Workers
This use case demonstrates how RabbitMQ enables event-driven architectures using topic exchanges, durable queues, and Python-based worker consumers. It focuses on reliable, asynchronous event processing, which is a common production pattern.

- Topic exchange–based routing
- Durable queues and bindings
- A Python-based worker using the `pika` client
- Message publishing and consumption validation

The use case models an **event-driven system**, where order-related events are published and processed asynchronously by workers.

### Use Case Overview

**Scenario:**  
An application publishes order-related events (`order.created`, `order.updated`, etc.) to RabbitMQ. A background worker consumes these events from a queue and processes them independently.

The goal of this use case is to showcase how order-related events can be published to RabbitMQ and processed asynchronously by background workers without tightly coupling producers and consumers.

**Typical events include:**

- order.created
- order.updated
- order.completed

This architecture improves scalability, fault tolerance, and system decoupling.

### Prerequisites

- RabbitMQ installed and running
- RabbitMQ management plugin enabled
- Python 3 installed
- Network access to RabbitMQ broker

### Declare a Topic Exchange
Create a durable topic exchange to route events based on routing keys.

```console
./rabbitmqadmin declare exchange name=events type=topic durable=true
```

- Creates a durable topic exchange named events.
- Routes messages using wildcard-based routing keys (e.g., order.*).
- Ensures the exchange survives broker restarts.

### Declare a Durable Queue
Create a durable queue to store order-related events.

```console
./rabbitmqadmin declare queue name=order.events durable=true
```

- Create a durable queue for order events.
- Guarantee that messages are persisted until consumed.
- Ensure reliability in case of worker or broker restarts.

You should see an output similar to:
```output
queue declared
```

### Bind Queue to Exchange
Bind the queue to the exchange using a topic routing pattern.

```console
./rabbitmqadmin declare binding source=events destination=order.events routing_key="order.*"
```

- Connects the queue to the exchange.
- Ensures all order-related routing keys match the queue.
- Enables flexible event expansion without changing consumers.

You should see an output similar to:
```output
binding declared
```

This binding ensures the queue receives all messages with routing keys such as:
- order.created
- order.updated
- order.completed

### Publish an Event Message
Publish a sample order event to the exchange.

```console
./rabbitmqadmin publish exchange=events routing_key="order.created" payload='{"order_id":123}
```

- Publishes an event to the events exchange.
- Uses a routing key that matches the binding filter.
- Payload is structured JSON to simulate real event data.

You should see an output similar to:
```output
Message published
```

### Install Python Dependencies
Install pip and the pika RabbitMQ client library.

```console
sudo zypper install -y python3-pip
pip install pika
```

### Create the Worker Script
Create a Python worker file to process messages from a queue.

A **Python worker** was created to process messages from a RabbitMQ queue (jobs) using the pika library. The queue is durable, ensuring message persistence. The worker implements fair dispatch (prefetch_count=1) and manual acknowledgments to reliably process each job without loss. Messages were successfully published to the queue using rabbitmqadmin, and the worker consumed them as expected.

```console
vi worker.py
```

**worker.py:**

```python
import pika
import time
import json

# RabbitMQ broker address
RABBITMQ_IP = "localhost"

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=RABBITMQ_IP)
)
channel = connection.channel()

# Ensure queue exists
channel.queue_declare(queue='jobs', durable=True)

print("Worker started. Waiting for jobs...")

def process_job(ch, method, properties, body):
    job = json.loads(body.decode())
    print(f"[Worker] Received job: {job}")

    # Simulate processing
    time.sleep(2)

    # Acknowledge message
    ch.basic_ack(delivery_tag=method.delivery_tag)

# Fair dispatch configuration
channel.basic_qos(prefetch_count=1)

channel.basic_consume(
    queue='jobs',
    on_message_callback=process_job
)

channel.start_consuming()
```

### Start the Worker
Run the worker process.

```console
python3 worker.py
```

You should see an output similar to:
```output
The worker started. Waiting for jobs...
```

### Publish Job Messages
From another terminal, publish a job message.

```console
./rabbitmqadmin publish routing_key=jobs payload='{"job":"test1"}'
```

**Worker output:**

```output
Worker started. Waiting for jobs...
[Worker] Received job: {'job': 'test1'}
```

Publish another job:

```console
./rabbitmqadmin publish routing_key=jobs payload='{"job":"hello1"}'
```

**Worker output:**

```output
Worker started. Waiting for jobs...
[Worker] Received job: {'job': 'hello1'}
```

## Use Case Validation

- Event routing via topic exchanges functions correctly  
- Durable queues and acknowledgments ensure reliable message processing  
- Worker-based consumption supports safe and controlled job execution


This use case demonstrates how RabbitMQ enables reliable, decoupled, and scalable event processing using topic-based routing and Python workers.
The setup provides a strong foundation for production-grade, message-driven architectures on GCP SUSE Arm64 virtual machines.
