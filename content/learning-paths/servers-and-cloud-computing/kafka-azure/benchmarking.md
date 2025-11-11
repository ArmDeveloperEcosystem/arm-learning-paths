---
title: Benchmarking with Official Kafka Tools
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Benchmark Kafka on Azure Cobalt 100 Arm-based instances

Apache Kafka includes official performance testing utilities that allow you to measure throughput, latency, and end-to-end efficiency of your messaging system. These tools`kafka-producer-perf-test.sh` and `kafka-consumer-perf-test.sh` are bundled with Kafka’s standard installation and are designed for realistic performance evaluation of producers and consumers.

## Steps for Kafka Benchmarking 

Before running the benchmarks, make sure your Kafka broker is already active in a separate terminal (as configured in the previous section).
Now open two new terminal sessions — one for running the producer benchmark and another for the consumer benchmark.

### Terminal A - Producer Benchmark

The Producer Performance Test measures how quickly Kafka can publish messages to a topic and reports key performance metrics such as throughput, average latency, and percentile latencies.

Run the following command to simulate message production on your Azure Cobalt 100 Arm64 VM:

```console
cd /opt/kafka
bin/kafka-producer-perf-test.sh \
  --topic test-topic-kafka \
  --num-records 1000000 \
  --record-size 100 \
  --throughput -1 \
  --producer-props bootstrap.servers=localhost:9092
```
You should see output similar to:

```output
1000000 records sent, 252589.0 records/sec (24.09 MB/sec), 850.85 ms avg latency, 1219.00 ms max latency, 851 ms 50th, 1184 ms 95th, 1210 ms 99th, 1218 ms 99.9th.
```

| Metric                             | Meaning                                                                                                         |
| ---------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| **Records/sec**                    | Number of messages successfully produced per second. Higher indicates better throughput.                        |
| **MB/sec**                         | Total data throughput in megabytes per second.                                                                  |
| **Avg latency**                    | Average time (in milliseconds) for the producer to send a message and receive acknowledgment from the broker.   |
| **Max latency**                    | The longest single message send time recorded.                                                                  |
| **50th / 95th / 99th percentiles** | Distribution of message send times. For example, 95% of messages completed under 1,184 ms in the sample output. |

### Terminal B - Consumer benchmark

The Consumer Performance Test measures how efficiently Kafka can read and process messages from a topic. It reports metrics such as total messages consumed, data throughput, and fetch rates, helping validate overall consumer-side performance on your Azure Cobalt 100 (Arm64) VM.

Run the following command in a new terminal:
```console
cd /opt/kafka
bin/kafka-consumer-perf-test.sh \
  --topic test-topic-kafka \
  --bootstrap-server localhost:9092 \
  --messages 1000000 \
  --timeout 30000
```
You should see output similar to:

```output
start.time, end.time, data.consumed.in.MB, MB.sec, data.consumed.in.nMsg, nMsg.sec, rebalance.time.ms, fetch.time.ms, fetch.MB.sec, fetch.nMsg.sec
2025-09-03 06:07:13:616, 2025-09-03 06:07:17:545, 95.3674, 24.2727, 1000001, 254517.9435, 3354, 575, 165.8564, 1739132.1739
```
Understanding the Metrics:

| Metric                      | Description                                                                                               |
| --------------------------- | --------------------------------------------------------------------------------------------------------- |
| **`data.consumed.in.MB`**   | Total data consumed during the benchmark.                                                                 |
| **`MB.sec`**                | Consumption throughput in megabytes per second. Higher values indicate better sustained read performance. |
| **`data.consumed.in.nMsg`** | Total number of messages successfully consumed.                                                           |
| **`nMsg.sec`**              | Messages consumed per second (a key measure of consumer-side throughput).                                 |
| **`fetch.time.ms`**         | Time spent retrieving messages from the broker. Lower values mean faster message delivery.                |
| **`fetch.nMsg.sec`**        | Per-fetch message rate, useful for comparing network and I/O efficiency.                                  |
| **`rebalance.time.ms`**     | Time spent coordinating consumer group assignments before actual consumption begins.                      |

## Benchmark summary on Arm64:
The following results summarize Kafka producer and consumer benchmark performance on an Azure Cobalt 100 (Arm64) virtual machine, specifically a D4ps_v6 instance running Ubuntu Pro 24.04 LTS.
These results validate Kafka’s stability and throughput consistency on Arm-based infrastructure.
### Consumer Performance Test
| Metric                     | Value       | Unit          |
|-----------------------------|-------------|---------------|
| Total Time Taken           | 3.875       | Seconds       |
| Data Consumed              | 95.3674     | MB            |
| Throughput (Data)          | 24.6110     | MB/sec        |
| Messages Consumed          | 1,000,001   | Messages      |
| Throughput (Messages)      | 258,064.77  | Messages/sec  |
| Rebalance Time             | 3348        | Milliseconds  |
| Fetch Time                 | 527         | Milliseconds  |
| Fetch Throughput (Data)    | 180.9629    | MB/sec        |
| Fetch Throughput (Messages)| 1,897,535.10| Messages/sec  |

Interpretation:
The consumer achieved over 258,000 messages per second, equivalent to ~24.6 MB/sec, with low fetch latency.
A fetch throughput near 1.9 million messages/sec indicates efficient partition reads and network I/O handling on the Arm64 platform.
Minimal rebalance and fetch times confirm Kafka’s responsiveness under sustained workloads.

### Producer Performance Test
| Metric | Records Sent | Records/sec | Throughput | Average Latency | Maximum Latency | 50th Percentile Latency | 95th Percentile Latency | 99th Percentile Latency | 99.9th Percentile Latency |
|--------|--------------|-------------|------------|-----------------|-----------------|-------------------------|-------------------------|-------------------------|---------------------------|
| Value  | 1,000,000    | 257,532.8   | 24.56      | 816.19          | 1237.00         | 799                     | 1168                    | 1220                    | 1231                      |
| Unit   | Records      | Records/sec | MB/sec     | ms              | ms              | ms                      | ms                      | ms                      | ms                        |
Interpretation:
The producer sustained a throughput of ~257,500 records/sec (~24.5 MB/sec) with an average latency of 816 ms.
The 95th percentile latency (1168 ms) and 99th percentile (1220 ms) show predictable network and I/O performance.
Kafka maintained consistent throughput, even under full-speed production, with no message loss or broker errors reported.

### Benchmark Comparison Insights
When analyzing performance on Azure Cobalt 100 Arm64 virtual machines:
**Producer efficiency**: The producer reached ~23–25 MB/sec throughput with average latencies below 900 ms, demonstrating stable delivery rates for high-volume workloads.
**Consumer scalability**: The consumer maintained ~262K messages/sec throughput with near-linear scaling of fetch performance — exceeding 1.85M messages/sec internally.
**Performance stability**: Both producer and consumer benchmarks showed low jitter and consistent latency distribution across iterations, confirming Kafka’s predictable behavior on Arm-based VMs.
afka on an Azure Cobalt 100 Arm64 virtual machine and compared results with x86_64.
