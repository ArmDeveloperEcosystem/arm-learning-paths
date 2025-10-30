---
title: Redis Baseline Testing on Google Axion C4A Arm Virtual Machine
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Redis Baseline Testing on GCP SUSE VMs
This section performs baseline testing for Redis running on a GCP SUSE Arm64 VM, focusing on data insertion, retrieval, and search performance.

### Prerequisites
This command launches the Redis server process in the background. It allows you to run subsequent commands in the same terminal session while Redis continues running.
Start the Redis service in the background:

```console
redis-server &
```

**Check if Redis is active and responding to commands:**

The redis-cli ping command sends a simple health check request to the Redis server. A PONG response confirms that the server is running correctly and the client can communicate with it.
```console
redis-cli ping
```

output:

```output
PONG
```

### Insert Sample Data
These steps populate the Redis database with a sample dataset to validate insertion performance and data persistence. You will create 10,000 key-value pairs using a simple shell loop and verify that the data has been successfully stored.

Use `redis-cli` to insert **10,000 sample key-value pairs**:
```console
for i in $(seq 1 10000); do
  redis-cli SET key:$i "value-$i" > /dev/null
done
```
- This command iterates through numbers **1 to 10,000**, setting each as a Redis key in the format `key:<number>` with the corresponding value `"value-<number>"`.
- The `> /dev/null` part suppresses command output to make the insertion process cleaner and faster.

**Verify Data Storage Count:**

The `DBSIZE` command returns the total number of keys currently stored in the Redis database.

```console
redis-cli DBSIZE
```

```output
(integer) 10000
```
Seeing `(integer) 10000` confirms that all key-value pairs were inserted successfully.

**Verify Sample Data Retrieval**

Fetch one of the inserted keys to confirm data correctness:

```console
redis-cli GET key:5000
```
- The `GET` command retrieves the value of a given key.  
- If Redis returns `"value-5000"`, it confirms that data insertion worked properly and the database is responding as expected.

You should see an output similar to:

```output
"value-5000"
```

### Perform Basic Data Search Tests
This step verifies Redis’s ability to retrieve specific data efficiently using unique keys. The `GET` command fetches the value associated with a given key from Redis.

You can test this by retrieving a known key-value pair:

```console
redis-cli GET key:1234
```

You should see an output similar to:

```output
"value-1234"
```
This confirms that Redis is storing and retrieving data correctly from memory.

### Search for Multiple Keys Using Pattern Matching
This test demonstrates how Redis can locate multiple keys that match a pattern, useful for exploratory queries or debugging.

Use the `KEYS` command to search for keys matching a pattern:

```console
redis-cli KEYS "key:1*"
```
`KEYS` is fast but **blocks the server** when handling large datasets, so it’s not recommended in production.

You should see an output similar to:

```output
   1) "key:1392"
   2) "key:1076"
   3) "key:1683"
   4) "key:1490"
   5) "key:117"
   6) "key:1293"
   7) "key:1791"
   8) "key:1891"
   9) "key:1543"
..........
```

### Production-Safe Searching with SCAN
This step introduces a production-friendly method for iterating through keys without blocking Redis operations.

Use the `SCAN` command for larger datasets — it is non-blocking and iterates safely.

```console
redis-cli SCAN 0 MATCH "key:1*" COUNT 100
```

You should see an output similar to:

```output
1) "9792"
2) 1) "key:151"
   2) "key:1845"
   3) "key:1397"
   4) "key:1501"
   5) "key:1994"
   6) "key:1475"
   7) "key:1522"
   8) "key:1884"
```
Redis will return a cursor value (for example, `9792`).  
Continue scanning by reusing the cursor until it returns `0`, meaning the iteration is complete.

### Measure Data Retrieval Performance
This step measures how quickly Redis can retrieve a single key from memory, helping to establish a baseline for data access latency on the Arm-based VM.

**Time Single Key Lookup**: Redis operations are extremely fast since data is stored in-memory. To quantify this, the Unix `time` command is used to measure the latency of retrieving a single key using `redis-cli`.

```console
(time redis-cli GET key:9000) 2>&1
```

This command measures three time metrics:

- **real** – Total elapsed time (wall-clock time)  
- **user** – Time spent in user mode  
- **sys** – Time spent in kernel mode

You should see an output similar to:

```output
"value-9000"

real    0m0.002s
user    0m0.002s
sys     0m0.000s
```
These results show that Redis retrieves data almost instantly (in milliseconds or microseconds), confirming that the instance is performing efficiently under baseline conditions.
