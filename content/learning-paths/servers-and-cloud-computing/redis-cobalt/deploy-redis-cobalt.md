---
title: Deploy Redis on Azure Cobalt 100
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Deploy Redis on Azure Cobalt 100 (Arm)

This section guides you through installing Redis on an Azure Cobalt 100 Arm-based virtual machine and building a real-time messaging and event processing system using Redis Pub/Sub and Streams.

You will implement low-latency messaging and event-driven pipelines optimized for Arm-based infrastructure.

## Update your system

Update your operating system packages to the latest versions:

```console
sudo apt update && sudo apt upgrade -y
```

## Install required dependencies

Install build tools and utilities required to compile and run Redis:

```bash
sudo apt install -y build-essential tcl git curl python3-pip
```

## Download and install Redis

Download the latest Redis source code and compile it:

```bash
cd /tmp
curl -O http://download.redis.io/redis-stable.tar.gz
tar xzf redis-stable.tar.gz
cd redis-stable
make -j$(nproc)
```

(Optional) Run tests to validate the build:

```bash
make test
```

## Start the Redis server

Start the Redis server in a new terminal.

**Terminal 1:**

```bash
cd /tmp/redis-stable
src/redis-server
```

The output shows Redis starting successfully and listening on port 6379.

## Verify Redis is running

Open another terminal and connect using the Redis CLI.

**Terminal 2:**

```bash
cd /tmp/redis-stable
src/redis-cli
PING
```

The output is similar to:
```output
127.0.0.1:6379> ping
PONG
```

This confirms that Redis is running and accepting connections.

## Implement real-time messaging using Pub/Sub

Redis Pub/Sub enables real-time communication between producers and consumers.

**Terminal 2 (Subscriber):**

```bash
SUBSCRIBE chat_channel
```

The output is similar to:

```output
127.0.0.1:6379> SUBSCRIBE chat_channel
1) "subscribe"
2) "chat_channel"
3) (integer) 1
1) "message"
2) "chat_channel"
```

**Terminal 3 (Publisher):**

```bash
cd /tmp/redis-stable
src/redis-cli
PUBLISH chat_channel "Hello from Cobalt Arm!"
```

After publishing the message, switch back to the subscriber terminal.

The output is similar to:

```output
1) "subscribe"
2) "chat_channel"
3) (integer) 1
1) "message"
2) "chat_channel"
3) "Hello from Cobalt Arm!"
```

This demonstrates real-time message delivery.

## Build an event pipeline using Redis Streams

Redis Streams provide persistent messaging with replay capability.

**Terminal 3 (Producer):**

```bash
XADD mystream * user jack action login
XADD mystream * user yan action purchase
```

The output is similar to:
```output
127.0.0.1:6379> XADD mystream * user jack action login
"1774931844279-0"
127.0.0.1:6379> XADD mystream * user yan action purchase
"1774931858864-0"
```

**Terminal 2 (Consumer):**

```bash
XREAD COUNT 2 STREAMS mystream 0
```

The output is similar to:
```output
1) 1) "mystream"
   2) 1) 1) "1774931844279-0"
         2) 1) "user"
            2) "jack"
            3) "action"
            4) "login"
      2) 1) "1774931858864-0"
         2) 1) "user"
            2) "yan"
            3) "action"
            4) "purchase"
```

This confirms that events are stored and can be read reliably.

## Key differences between Pub/Sub and Streams

- Pub/Sub delivers messages in real time but does not store them
- Streams persist messages and allow replay
- Streams support consumer groups for scalability

## What you've learned and what's next
You have successfully:

- Installed Redis on an Arm-based Cobalt 100 VM
- Verified Redis connectivity
- Implemented real-time messaging using Pub/Sub
- Built an event-driven pipeline using Redis Streams

You are now ready to extend this setup with consumer groups, application integration, and performance benchmarking.
