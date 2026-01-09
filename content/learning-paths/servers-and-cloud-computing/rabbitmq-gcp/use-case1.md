---
title: "RabbitMQ use case 1: event processing with Python workers"
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Event processing with topic-based routing

In this use case, you implement an event-driven workflow using RabbitMQ with a topic exchange, a durable queue, and a Python worker consumer. You publish order events (for example, `order.created`, `order.updated`) and process them asynchronously.

This pattern is useful when you need flexible, wildcard-based routing (such as `order.*`) where multiple event types route to the same queue and producers and consumers evolve independently.

### Use case overview

**Scenario:**  
An application publishes order-related events (`order.created`, `order.updated`, etc.) to RabbitMQ. A background worker consumes these events from a queue and processes them independently.

This use case shows how order-related events can be published to RabbitMQ and processed asynchronously by background workers without tightly coupling producers and consumers.

**Typical events include:**

- order.created
- order.updated
- order.completed

This architecture improves scalability, fault tolerance, and system decoupling.

**When to use this pattern:**

Use topic exchanges when you need wildcard routing where `order.*` matches `order.created`, `order.updated`, and `order.completed`. This approach allows multiple related event types to flow to the same consumer and provides flexibility to add new event types without reconfiguring consumers.

**Comparison:**

Use Case 1 (Topic Exchange) provides flexible routing with wildcards, ideal for event streams. Use Case 2 (Direct Exchange) provides exact-match routing, ideal for targeted notifications.

### Declare a topic exchange

Create a durable topic exchange to route events based on routing keys:

```console
./rabbitmqadmin declare exchange name=events type=topic durable=true
```

This creates a durable topic exchange named `events` that routes messages using wildcard-based routing keys (for example, `order.*`) and survives broker restarts.

You should see:
```output
exchange declared
```

### Declare a durable queue

Create a durable queue to store order-related events.

```console
./rabbitmqadmin declare queue name=order.events durable=true
```

This creates a durable queue for order events that guarantees messages are persisted until consumed, ensuring reliability in case of worker or broker restarts.

You should see:
```output
queue declared
```

### Bind queue to exchange

Bind the queue to the exchange using a topic routing pattern:

```console
./rabbitmqadmin declare binding source=events destination=order.events routing_key="order.*"
```

This connects the queue to the exchange so all order-related routing keys match the queue. The wildcard pattern `order.*` matches routing keys such as `order.created`, `order.updated`, and `order.completed`, enabling flexible event expansion without changing consumers.

The output is similar to:
```output
binding declared
```

### Validate the setup

Confirm that the exchange, queue, and binding exist and are correctly connected:

```console
./rabbitmqadmin list exchanges name type
./rabbitmqadmin list queues name messages
./rabbitmqadmin list bindings
```

These commands verify that the `events` exchange exists (type: `topic`), the `order.events` queue exists with zero messages initially, and a binding connects `events` to `order.events` with the `order.*` routing pattern.

The output is similar to:

```output
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
+--------------------+---------+
+--------------+----------+
|     name     | messages |
+--------------+----------+
| order.events | 0        |
| testqueue    | 1        |
+--------------+----------+
+--------+--------------+--------------+
| source | destination  | routing_key  |
+--------+--------------+--------------+
|        | order.events | order.events |
|        | testqueue    | testqueue    |
| events | order.events | order.*      |
+--------+--------------+--------------+
```

### Install Python dependencies

To create the worker, you need Python 3 with the `pika` library, which provides the RabbitMQ client:

```console
sudo zypper install -y python3-pip
pip3 install pika
```

This installs `pip` (Python package manager) and `pika` (RabbitMQ client library for Python).

### Create the worker script

The Python worker consumes order-related events from the `order.events` queue. This worker uses durable queues for message persistence, `prefetch_count=1` for fair dispatch, and manual acknowledgments for reliable processing.

Using a text editor, create a `worker.py` file with the content below: 

```python
import pika
import time
import json

RABBITMQ_HOST = "localhost"
QUEUE_NAME = "order.events"

print("[DEBUG] Connecting to RabbitMQ...")
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=RABBITMQ_HOST)
)
channel = connection.channel()

print("[DEBUG] Declaring queue...")
channel.queue_declare(queue=QUEUE_NAME, durable=True)

print("[DEBUG] Setting QoS...")
channel.basic_qos(prefetch_count=1)

print("Worker started. Waiting for events...")

def process_event(ch, method, properties, body):
    event = json.loads(body.decode())
    print(f"[Worker] Received event: {event}")
    print(f"[Worker] Processing event type: {event.get('event', 'unknown')}")

    # Simulate processing time
    time.sleep(2)
    
    print("[Worker] Event processed successfully")
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(
    queue=QUEUE_NAME,
    on_message_callback=process_event
)

print("[DEBUG] Starting consumer loop...")
channel.start_consuming()
```

### Start the worker

Now that you've created the worker script, run it to start consuming messages:

```console
python3 worker.py
```

The worker connects to RabbitMQ and begins listening for events. The output is similar to:
```output
[DEBUG] Connecting to RabbitMQ...
[DEBUG] Declaring queue...
[DEBUG] Setting QoS...
Worker started. Waiting for events...
[DEBUG] Starting consumer loop...
```

### Publish event messages

With the worker running, open another SSH terminal and publish an order event:

```console
./rabbitmqadmin publish exchange=events routing_key="order.created" payload='{"order_id":123,"event":"order.created"}'
```

The message routes through the `events` exchange to the `order.events` queue, where the worker consumes it. The worker output shows:

```output
[Worker] Received event: {'order_id': 123, 'event': 'order.created'}
[Worker] Processing event type: order.created
[Worker] Event processed successfully
```

Publish a second event to test the wildcard routing:

```console
./rabbitmqadmin publish exchange=events routing_key="order.updated" payload='{"order_id":123,"event":"order.updated"}'
```

The worker processes this event using the same logic. The output shows:

```output
[Worker] Received event: {'order_id': 123, 'event': 'order.updated'}
[Worker] Processing event type: order.updated
[Worker] Event processed successfully
```

The wildcard binding (`order.*`) allows the worker to process any event with a routing key matching this pattern. You can publish additional events such as `order.completed` or `order.cancelled` and the worker processes them all.

When you're done testing, press Ctrl+C in the worker terminal to exit the application.

## What you've accomplished and what's next

You've implemented an event-driven system using RabbitMQ with topic exchange routing, durable queues, manual acknowledgments, and fair dispatch. 

The Python worker processes order events asynchronously, and the wildcard routing pattern (`order.*`) allows multiple related event types to flow to the same consumer.

This pattern works well for event streams where you want flexibility to add new event types without reconfiguring consumers.

Next, you implement a WhatsApp notification pipeline using a direct exchange with exact-match routing, better suited for targeted notifications.
