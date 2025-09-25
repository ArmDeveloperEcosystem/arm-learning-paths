---
title: Monitor MongoDB with mongotop
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

This section demonstrates how to monitor MongoDB performance using `mongotop`, which reports how much time the server spends reading and writing per collection in real time. It includes benchmark results collected on Azure Arm64 virtual machines, providing a reference for expected latencies.

## Prerequisites

- `mongod` is running locally and bound to `127.0.0.1` (as started earlier)
- Your **long_system_load.js** script is actively generating traffic in another terminal
- MongoDB Database Tools (which include `mongotop`) are installed

## Run mongotop - terminal 2

```console
mongotop 2
```
This refreshes every 2 seconds and displays per‑collection time spent on reads and writes. Press **Ctrl+C** to stop.

## Example output

The tail end of the output should look like:
```output
                            ns    total    read    write    2025-09-04T04:58:23Z
test.admin_system_version_test      5ms     2ms      3ms
    test.system_sessions_bench      5ms     2ms      3ms
                admin.atlascli      3ms     1ms      1ms
  config.system_sessions_bench      3ms     1ms      1ms
                 test.atlascli      3ms     1ms      1ms
        benchmarkDB.cursorTest      2ms     1ms      1ms
    benchmarkDB.testCollection      2ms     1ms      1ms
     config.transactions_bench      2ms     1ms      1ms
    local.system_replset_bench      2ms     1ms      1ms
          admin.system.version      0ms     0ms      0ms

                            ns    total    read    write    2025-09-04T04:58:25Z
                admin.atlascli      5ms     2ms      3ms
  config.system_sessions_bench      4ms     1ms      3ms
    test.system_sessions_bench      3ms     1ms      1ms
        benchmarkDB.cursorTest      2ms     1ms      1ms
    benchmarkDB.testCollection      2ms     1ms      1ms
     config.transactions_bench      2ms     1ms      1ms
    local.system_replset_bench      2ms     1ms      1ms
test.admin_system_version_test      2ms     1ms      1ms
                 test.atlascli      2ms     1ms      1ms
          admin.system.version      0ms     0ms      0ms

                            ns    total    read    write    2025-09-04T04:58:27Z
test.admin_system_version_test      6ms     2ms      3ms
        benchmarkDB.cursorTest      5ms     2ms      3ms
    benchmarkDB.testCollection      5ms     2ms      3ms
     config.transactions_bench      5ms     2ms      3ms
    local.system_replset_bench      5ms     2ms      3ms
                 test.atlascli      5ms     2ms      3ms
    test.system_sessions_bench      5ms     2ms      3ms
                admin.atlascli      3ms     1ms      1ms
  config.system_sessions_bench      3ms     2ms      1ms
          admin.system.version      0ms     0ms      0ms
```

## Interpret the metrics

Before you dive into individual columns, read each line as a snapshot of *where time was spent* in the last interval. Start with **total** to spot hot namespaces, then compare **read** vs **write** to understand the workload shape. Look across multiple refreshes for trends—steady growth or a single collection dominating is a signal to investigate indexes, query shapes, or storage latency.

- **ns (namespace)** the `database.collection` being measured
- **total** total time the server spent servicing operations for that namespace in the interval
- **read** time spent on read operations such as queries and fetches
- **write** time spent on write operations such as inserts, updates, and deletes
- **timestamp** the time when the snapshot was captured

**Namespaces**

  - **benchmarkDB.testCollection** core benchmark collection with balanced read/write load
  - **admin.atlascli** tracks admin-level client activity
  - **benchmarkDB.cursorTest** measures cursor operations during benchmarking
  - **config.system_sessions_bench** benchmarks session handling in config DB
  - **config.transactions_bench** evaluates transaction performance in config DB
  - **local.system_replset_bench** tests replication set metadata access
  - **test.admin_system_version_test** monitors versioning metadata in test DB
  - **test.atlascli** simulates client-side workload in test DB
  - **test.system_sessions_bench** benchmarks session handling in test DB
  - **admin.system.version** static metadata collection with minimal activity

## Benchmark summary on Arm64

For easier visualization, here is a summary of benchmark results collected on an Arm64 **D4ps_v6 Azure Ubuntu Pro 24.04 LTS** virtual machine.

| Namespace (ns)                  | Total Time Range | Read Time Range | Write Time Range | Notes |
| :------------------------------ | :--------------- | :-------------- | :--------------- | :---- |
| **admin.atlascli**                   | 2–6 ms           | 0–2 ms          | 1–3 ms           | Admin CLI operations |
| **benchmarkDB.cursorTest**           | 2–5 ms           | 0–2 ms          | 1–3 ms           | Cursor benchmark load |
| **benchmarkDB.testCollection**       | 2–5 ms           | 0–2 ms          | 1–3 ms           | Main benchmark workload |
| **config.system_sessions_bench**     | 2–6 ms           | 0–2 ms          | 1–3 ms           | System/benchmark sessions |
| **config.transactions_bench**        | 2–6 ms           | 0–2 ms          | 1–3 ms           | Internal transaction benchmark |
| **local.system_replset_bench**       | 2–5 ms           | 0–2 ms          | 1–3 ms           | Local replica set benchmark |
| **test.admin_system_version_test**   | 2–5 ms           | 0–2 ms          | 1–3 ms           | Version check workload |
| **test.atlascli**                    | 2–5 ms           | 0–2 ms          | 1–3 ms           | CLI/system background operations (test namespace) |
| **test.system_sessions_bench**       | 2–5 ms           | 0–2 ms          | 1–3 ms           | Session benchmark (test namespace) |
| **admin.system.version**             | 0 ms             | 0 ms            | 0 ms             | Appears inactive or instantaneous responses |

With the MongoDB performance summary of the results on your Arm-based Azure Cobalt 100 VM, you will notice:
  - Stable, low-latency behavior across all tested namespaces
  - Read operations are near-instant (sub-2 ms), showing efficient query performance
  - Write operations remain consistently low, supporting reliable data modifications
  - System and transaction overheads are predictable, indicating a well-tuned environment for concurrent or replicated workloads

In conclusion, MongoDB operations on Arm64 are lightweight with predictable, low-latency reads and writes, confirming efficient performance on Azure Ubuntu Pro 24.04 LTS Arm64 virtual machines.
