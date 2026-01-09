---
title: "RabbitMQ use case 1: event processing with Python workers"
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## RabbitMQ use case: event processing with Python workers
This use case demonstrates how RabbitMQ enables event-driven architectures using topic exchanges, durable queues, and Python-based worker consumers. It focuses on reliable, asynchronous event processing, which is a common production pattern.

The use case models an **event-driven system**, where order-related events are published and processed asynchronously by workers.

### Use case overview

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

### Declare a topic exchange
Create a durable topic exchange to route events based on routing keys.

```console
./rabbitmqadmin declare exchange name=events type=topic durable=true
```

- Creates a durable topic exchange named events.
- Routes messages using wildcard-based routing keys (for example, order.*).
- Ensures the exchange survives broker restarts.

### Declare a durable queue
Create a durable queue to store order-related events.

```console
./rabbitmqadmin declare queue name=order.events durable=true
```

This creates a durable queue for order events that guarantees messages are persisted until consumed, ensuring reliability in case of worker or broker restarts.

The output is similar to:
```output
queue declared
```

### Bind queue to exchange
Bind the queue to the exchange using a topic routing pattern.

```console
./rabbitmqadmin declare binding source=events destination=order.events routing_key="order.*"
```

This connects the queue to the exchange and ensures all order-related routing keys match the queue, enabling flexible event expansion without changing consumers.

The output is similar to:
```output
binding declared
```

This binding ensures the queue receives all messages with routing keys such as:
- order.created
- order.updated
- order.completed

### Publish an event message
Publish a sample order event to the exchange.

```console
./rabbitmqadmin publish exchange=events routing_key="order.created" payload='{"order_id":123}'
```

This publishes an event to the `events` exchange using a routing key that matches the binding filter. The payload is structured JSON to simulate real event data.

The output is similar to:
```output
Message published
```

### Install Python dependencies
Install pip and the pika RabbitMQ client library.

```console
sudo zypper install -y python3-pip
pip install pika
```

### Create the worker script

The Python worker processes messages from a RabbitMQ queue (`jobs`) using the `pika` library. The queue is durable, ensuring message persistence. The worker implements fair dispatch (`prefetch_count=1`) and manual acknowledgments to reliably process each job without loss.

Using your favorite editor, create a `worker.py` file:

```console
edit worker.py
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

### Start the worker
Run the worker process:

```console
python3 worker.py
```

The output is similar to:
```output
The worker started. Waiting for jobs...
```

### Publish job messages
From another SSH terminal, publish a job message.

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
Press Ctrl+C to exit the worker application.

## What you've accomplished and what's next

You've successfully implemented an event-driven system using RabbitMQ with topic exchange-based routing, durable queues with acknowledgments, and worker-based consumption for safe and controlled job execution. This setup provides a strong foundation for production-grade, message-driven architectures on Google Cloud SUSE Arm64 virtual machines. In the next section, you'll implement a WhatsApp notification system that demonstrates another common RabbitMQ use case.
