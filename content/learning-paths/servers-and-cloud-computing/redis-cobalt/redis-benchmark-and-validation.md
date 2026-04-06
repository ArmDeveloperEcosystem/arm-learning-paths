---
title: Benchmark and validate Redis on Azure Cobalt 100
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Benchmark and validate Redis performance

This section demonstrates how to implement production-grade event processing using Redis Streams consumer groups, simulate real workloads using Python, and benchmark Redis performance on an Azure Cobalt 100 Arm-based virtual machine.

You will validate Redis for high-throughput, low-latency workloads on Arm infrastructure.


## Create a consumer group

Consumer groups enable scalable and reliable message processing by distributing work across multiple consumers.

```bash
XGROUP CREATE mystream mygroup 0 MKSTREAM
```

The output is similar to:

```output
OK
```

## Consume messages using a consumer group

Read messages from the stream as part of the consumer group:

```bash
XREADGROUP GROUP mygroup consumer1 COUNT 1 STREAMS mystream >
```

The output is similar to:

```output
1) 1) "mystream"
   2) 1) 1) "1774931844279-0"
         2) 1) "user"
            2) "jack"
            3) "action"
            4) "login"
```

## Acknowledge processed messages

Acknowledge messages after processing to prevent re-delivery:

```bash
XACK mystream mygroup <message-id>
```

Replace `<message-id>` with the ID returned from the previous command.

## Install Python Redis client

Install the Redis Python library to simulate real-world producer and consumer applications:

```bash
pip3 install redis
```

## Create a Python producer

Create a producer script to send events to the Redis stream:

```python
import redis

r = redis.Redis(host='localhost', port=6379)

for i in range(10):
    r.xadd("mystream", {"event": f"msg-{i}"})
    print(f"Produced msg-{i}")
```

Run the producer:

```bash
python3 producer.py
```

The output is similar to:

```output
Produced msg-0
Produced msg-1
...
Produced msg-9
```

## Create a Python consumer

Create a consumer script to read and process messages:

```python
import redis

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

while True:
    messages = r.xreadgroup("mygroup", "consumer1", {"mystream": ">"}, count=1, block=5000)
    
    for stream, msgs in messages:
        for msg_id, data in msgs:
            print(f"Consumed {msg_id}: {data}")
            r.xack("mystream", "mygroup", msg_id)
```


**Run the consumer:**

```bash
python3 consumer.py
```

The output is similar to:

```output
Consumed 1774931858864-0: {'user': 'yan', 'action': 'purchase'}
Consumed 1774935598721-0: {'event': 'msg-0'}
Consumed 1774935598721-1: {'event': 'msg-1'}
Consumed 1774935598721-2: {'event': 'msg-2'}
Consumed 1774935598721-3: {'event': 'msg-3'}
Consumed 1774935598722-0: {'event': 'msg-4'}
Consumed 1774935598722-1: {'event': 'msg-5'}
Consumed 1774935598722-2: {'event': 'msg-6'}
Consumed 1774935598722-3: {'event': 'msg-7'}
Consumed 1774935598722-4: {'event': 'msg-8'}
Consumed 1774935598722-5: {'event': 'msg-9'}
```

## Benchmark Redis performance

Run the Redis benchmark tool to measure throughput and latency:

```bash
cd /tmp/redis-stable
src/redis-benchmark -q -n 100000 -c 50
```

The output is similar to:

```output
PING_INLINE: 132978.73 requests per second, p50=0.191 msec
PING_MBULK: 131752.31 requests per second, p50=0.191 msec
SET: 132802.12 requests per second, p50=0.191 msec
GET: 133689.83 requests per second, p50=0.191 msec
INCR: 131926.12 requests per second, p50=0.191 msec
LPUSH: 131406.05 requests per second, p50=0.191 msec
RPUSH: 130548.30 requests per second, p50=0.199 msec
LPOP: 131061.59 requests per second, p50=0.191 msec
RPOP: 135685.22 requests per second, p50=0.191 msec
SADD: 135869.56 requests per second, p50=0.191 msec
HSET: 136612.02 requests per second, p50=0.191 msec
SPOP: 134952.77 requests per second, p50=0.191 msec
ZADD: 136798.91 requests per second, p50=0.191 msec
ZPOPMIN: 134952.77 requests per second, p50=0.191 msec
LPUSH (needed to benchmark LRANGE): 136425.66 requests per second, p50=0.191 msec
LRANGE_100 (first 100 elements): 75357.95 requests per second, p50=0.335 msec
LRANGE_300 (first 300 elements): 31645.57 requests per second, p50=0.791 msec
LRANGE_500 (first 500 elements): 22036.14 requests per second, p50=1.127 msec
LRANGE_600 (first 600 elements): 19109.50 requests per second, p50=1.295 msec
MSET (10 keys): 137931.03 requests per second, p50=0.215 msec
XADD: 136425.66 requests per second, p50=0.191 msec
```

These results demonstrate high throughput and efficient performance on the Arm architecture.

### Arm64 performance analysis

The benchmark results highlight the strong performance characteristics of Redis on Azure Cobalt 100 Arm64 infrastructure:

- **High throughput:** Redis consistently achieves **130K–136K** operations per second across multiple commands.
- **Low latency:** Median latency remains around **~0.19 ms**, ensuring near real-time responsiveness.
- **Efficient stream ingestion:** XADD operations reach **~136K ops/sec**, making Redis Streams suitable for high-ingestion event pipelines.
- **Stable performance across workloads:** Consistent performance across **SET, GET, HASH, and STREAM operations** demonstrates efficient CPU and memory utilization on Arm.

These results validate that Arm-based infrastructure can handle high-performance, low-latency data workloads effectively.

## Benchmark Pub/Sub performance

Run a publish benchmark to evaluate messaging throughput:

```bash
src/redis-benchmark -t publish -n 100000
```

{{% notice Note %}}
The Redis benchmark tool does not display detailed output for Pub/Sub operations. To validate Pub/Sub behavior, use a subscriber or monitor Redis metrics using the INFO command.
{{% /notice %}}

## Monitor Redis metrics

Use the Redis INFO command to inspect runtime statistics:

```bash
src/redis-cli info stats
```

The output is similar to:

```output
# Stats
total_connections_received:1058
total_commands_processed:2300074
instantaneous_ops_per_sec:0
total_net_input_bytes:129526426
total_net_output_bytes:1373991650
total_net_repl_input_bytes:0
total_net_repl_output_bytes:0
instantaneous_input_kbps:0.00
instantaneous_output_kbps:0.00
instantaneous_input_repl_kbps:0.00
instantaneous_output_repl_kbps:0.00
rejected_connections:0
sync_full:0
sync_partial_ok:0
sync_partial_err:0
expired_subkeys:0
expired_subkeys_active:0
expired_keys:0
expired_keys_active:0
expired_stale_perc:0.00
expired_time_cap_reached_count:0
expire_cycle_cpu_milliseconds:65
evicted_keys:0
evicted_clients:0
evicted_scripts:0
total_eviction_exceeded_time:0
current_eviction_exceeded_time:0
keyspace_hits:800087
keyspace_misses:0
pubsub_channels:0
pubsub_patterns:0
pubsubshard_channels:0
latest_fork_usec:430
total_forks:3
migrate_cached_sockets:0
slave_expires_tracked_keys:0
active_defrag_hits:0
active_defrag_misses:0
active_defrag_key_hits:0
active_defrag_key_misses:0
total_active_defrag_time:0
current_active_defrag_time:0
tracking_total_keys:0
tracking_total_items:0
tracking_total_prefixes:0
unexpected_error_replies:0
total_error_replies:0
dump_payload_sanitizations:0
total_reads_processed:2301131
total_writes_processed:2300077
io_threaded_reads_processed:0
io_threaded_writes_processed:0
io_threaded_total_prefetch_batches:0
io_threaded_total_prefetch_entries:0
client_query_buffer_limit_disconnections:0
client_output_buffer_limit_disconnections:0
reply_buffer_shrinks:167
reply_buffer_expands:0
eventloop_cycles:1973082
eventloop_duration_sum:24187445
eventloop_duration_cmd_sum:4769476
instantaneous_eventloop_cycles_per_sec:9
instantaneous_eventloop_duration_usec:142
acl_access_denied_auth:0
acl_access_denied_cmd:0
acl_access_denied_key:0
acl_access_denied_channel:0
```

### Key observations

- Redis achieves **~130K+ ops/sec** on Arm64
- Latency remains under **1 millisecond**
- No rejected connections during load
- Streams provide reliable and scalable messaging
- System remains stable under high throughput

## What you've learned 

You have successfully:

- Implemented consumer groups for scalable processing
- Built Python-based producer and consumer applications
- Benchmarked Redis performance on Cobalt 100
- Validated Redis for high-throughput workloads

