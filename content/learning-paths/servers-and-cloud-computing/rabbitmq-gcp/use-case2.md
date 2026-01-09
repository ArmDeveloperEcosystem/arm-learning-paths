---
title: "RabbitMQ use case 2: WhatsApp Notification"
weight: 8 

### FIXED, DO NOT MODIFY
layout: learningpathall
---
## WhatsApp notification with direct exchange routing

In this use case, you implement an asynchronous notification workflow where RabbitMQ routes WhatsApp notification messages using a **direct exchange** with exact-match routing. A Python worker consumes and processes these messages reliably.

### Use case overview

In many production systems, sending WhatsApp notifications must be reliable, asynchronous, and independent of the main application flow. RabbitMQ acts as a message broker to decouple message production from consumption.

**When to use this pattern:**

Use direct exchanges when you need exact-match routing where `whatsapp` routes only to the WhatsApp queue. This approach provides simple, predictable routing without wildcards, and each message type routes to a specific, dedicated queue.

**Comparison:**

Use Case 1 (Topic Exchange) provides flexible routing with wildcards, ideal for event streams. Use Case 2 (Direct Exchange) provides exact-match routing, ideal for targeted notifications.

### Architecture flow

The application publishes a WhatsApp notification message to the `notifications` exchange. RabbitMQ routes the message to the `whatsapp.notifications` queue using the exact-match routing key `whatsapp`. The Python worker then consumes the message from the queue and simulates sending the WhatsApp notification. In production, this would call an external WhatsApp API.

### RabbitMQ topology

This use case uses a direct exchange topology for exact-match routing. The `notifications` exchange (type: `direct`) routes notification messages based on exact routing key matches. The `whatsapp.notifications` queue is durable, which means it persists messages across broker restarts. The binding connects the exchange to the queue using the `whatsapp` routing key, ensuring only messages published with this exact key are routed to the queue.

### Declare RabbitMQ resources

Create the required exchange, queue, and binding for WhatsApp notifications.

**Declare the exchange:**

```console
./rabbitmqadmin declare exchange \
  name=notifications \
  type=direct \
  durable=true
```

This creates a durable direct exchange named `notifications` that routes messages using exact routing keys.

You should see:
```output
exchange declared
```

**Declare the queue:**

```console
./rabbitmqadmin declare queue \
  name=whatsapp.notifications \
  durable=true
```

This creates a durable queue to persist WhatsApp notification messages until consumed.

The output is similar to:
```output
queue declared
```

**Declare the binding:**

```console
./rabbitmqadmin declare binding \
  source=notifications \
  destination=whatsapp.notifications \
  routing_key=whatsapp
```

This links the exchange to the queue using the `whatsapp` routing key.

Expected output:
```output
binding declared
```

### Validate the setup

Validate that RabbitMQ resources exist and are correctly connected:

```console
./rabbitmqadmin list exchanges name type
./rabbitmqadmin list queues name messages
./rabbitmqadmin list bindings source destination routing_key
```

These commands verify that the `notifications` exchange exists (type: `direct`), the `whatsapp.notifications` queue exists with zero messages, and the binding connects the exchange to the queue with routing key `whatsapp`.

The output is similar to:

```output
+---------------+--------+
| name          | type   |
+---------------+--------+
| notifications | direct |
+---------------+--------+

+------------------------+----------+
| name                   | messages |
+------------------------+----------+
| whatsapp.notifications | 0        |
+------------------------+----------+

+---------------+------------------------+-------------+
| source        | destination            | routing_key |
+---------------+------------------------+-------------+
| notifications | whatsapp.notifications | whatsapp    |
+---------------+------------------------+-------------+
```

### Install Python dependencies

If you haven't already installed Python dependencies in Use Case 1, install them now:

```console
sudo zypper install -y python3-pip
pip3 install pika
```

This installs `pip` (Python package manager) and `pika` (RabbitMQ client library for Python).

### WhatsApp worker implementation

The worker attaches as a blocking consumer to the `whatsapp.notifications` queue and processes incoming messages. This worker uses durable queues for message persistence, `prefetch_count=1` for fair dispatch, and manual acknowledgments for reliable processing.

Using a text editor, create a `whatsapp_worker.py` file with the content below:

```python
import pika
import json
import time

RABBITMQ_HOST = "localhost"
QUEUE_NAME = "whatsapp.notifications"

print("[DEBUG] Connecting to RabbitMQ...")
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=RABBITMQ_HOST)
)
channel = connection.channel()

print("[DEBUG] Declaring queue...")
channel.queue_declare(queue=QUEUE_NAME, durable=True)

print("[DEBUG] Setting QoS...")
channel.basic_qos(prefetch_count=1)

print("WhatsApp Worker started. Waiting for messages...")

def send_whatsapp(ch, method, properties, body):
    data = json.loads(body.decode())
    phone = data.get('phone', 'unknown')
    message = data.get('message', '')
    
    print(f"[Worker] Processing WhatsApp notification")
    print(f"[Worker] Recipient: {phone}")
    print(f"[Worker] Message: {message}")

    # Simulate external WhatsApp API call
    time.sleep(1)

    print("[Worker] WhatsApp notification sent successfully")
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(
    queue=QUEUE_NAME,
    on_message_callback=send_whatsapp,
    auto_ack=False
)

print("[DEBUG] Starting consumer loop (this should block)...")
channel.start_consuming()
```

### Start the worker

Now that you've created the worker script, run it in a dedicated terminal session:

```console
python3 whatsapp_worker.py
```

The worker connects to RabbitMQ and begins listening for WhatsApp notifications. The output is similar to:

```output
[DEBUG] Connecting to RabbitMQ...
[DEBUG] Declaring queue...
[DEBUG] Setting QoS...
WhatsApp Worker started. Waiting for messages...
[DEBUG] Starting consumer loop (this should block)...
```

The worker blocks at this point, waiting for messages without returning to the shell prompt.

### Publish a test message

With the worker running, open another SSH terminal and publish a WhatsApp notification message:

```console
./rabbitmqadmin publish \
  exchange=notifications \
  routing_key=whatsapp \
  payload='{"phone":"+911234567890","message":"Hello from RabbitMQ"}'
```

The message routes through the `notifications` exchange to the `whatsapp.notifications` queue, where the worker consumes it. In the first SSH terminal where the worker is running, you should see:

```output
[Worker] Processing WhatsApp notification
[Worker] Recipient: +911234567890
[Worker] Message: Hello from RabbitMQ
[Worker] WhatsApp notification sent successfully
```

### Message consumption validation

The complete worker output shows the full message flow:

```output
[DEBUG] Connecting to RabbitMQ...
[DEBUG] Declaring queue...
[DEBUG] Setting QoS...
WhatsApp Worker started. Waiting for messages...
[DEBUG] Starting consumer loop (this should block)...
[Worker] Processing WhatsApp notification
[Worker] Recipient: +911234567890
[Worker] Message: Hello from RabbitMQ
[Worker] WhatsApp notification sent successfully
```

This output confirms that message routing works correctly through the direct exchange, the worker successfully consumes from the queue, manual acknowledgments are applied, and the end-to-end message flow is validated.

### Verify queue state

To confirm successful message consumption, check the queue status:

```console
./rabbitmqadmin list queues name messages consumers
```

The output is similar to:

```output
+------------------------+----------+-----------+
| name                   | messages | consumers |
+------------------------+----------+-----------+
| whatsapp.notifications | 0        | 1         |
+------------------------+----------+-----------+
```

The output shows zero messages remaining (all were consumed), one active consumer connected, and no message backlog in the queue.

When you're done testing, press Ctrl+C in the worker terminal to exit the application.

## What you've accomplished

You've implemented an asynchronous notification system using RabbitMQ with direct exchange routing, durable queues, manual acknowledgments, and fair dispatch. The Python worker processes WhatsApp notifications asynchronously, and the exact-match routing ensures messages go only to the intended queue.

This pattern works well for targeted notifications (email, SMS, WhatsApp, push notifications) where routing needs to be simple and predictable. Each notification type routes to a dedicated queue using an exact-match routing key, providing reliable, guaranteed delivery.

The key difference from Use Case 1 is the routing approach: Use Case 1 uses topic exchange with wildcard routing (`order.*`) for flexible event streams, while Use Case 2 uses direct exchange with exact routing (`whatsapp`) for targeted notifications.
