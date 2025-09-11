---
title: Monitor MongoDB with mongotop
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Monitor MongoDB Performance using Mongotop
This guide demonstrates how to monitor MongoDB performance using **mongotop**, showing read and write activity across collections in real time. It includes benchmark results collected on Azure Arm64 virtual machines, providing a reference for expected latencies.

## Run mongotop — Terminal 2

```console
mongotop 2
```
**mongotop** shows how much time the server spends reading and writing each collection (refreshes every 2 seconds here). It helps you see which collections are busiest and whether reads or writes dominate.

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
## Explanation of Metrics and Namespaces

**Metrics**

  - **ns (Namespace)** – Identifies the specific database and collection being measured.
  - **total** – Total time spent on both read and write operations.
  - **read** – Time taken by read operations like queries or fetches.
  - **write** – Time taken by write operations like inserts, updates, or deletes.
  - **timestamp** – Marks when the metric snapshot was captured.

**Namespaces**

  - **benchmarkDB.testCollection** – Core benchmark collection with balanced read/write load.
  - **admin.atlascli** – Tracks admin-level client activity.
  - **benchmarkDB.cursorTest** – Measures cursor operations during benchmarking.
  - **config.system_sessions_bench** – Benchmarks session handling in config DB.
  - **config.transactions_bench** – Evaluates transaction performance in config DB.
  - **local.system_replset_bench** – Tests replication set metadata access.
  - **test.admin_system_version_test** – Monitors versioning metadata in test DB.
  - **test.atlascli** – Simulates client-side workload in test DB.
  - **test.system_sessions_bench** – Benchmarks session handling in test DB.
  - **admin.system.version** – Static metadata collection with minimal activity.

## Benchmark summary on Arm64
For easier visualization, shown here is a summary of benchmark results collected on an Arm64 **D4ps_v6 Azure Ubuntu Pro 24.04 LTS virtual machine**.

| Namespace (ns)                  | Total Time Range | Read Time Range | Write Time Range | Notes |
| :------------------------------- | :--------------- | :-------------- | :--------------- | :------------------------------------------------------------ |
| **admin.atlascli**                   | 2–6 ms           | 0–2 ms          | 1–3 ms           | Admin CLI operations. |
| **benchmarkDB.cursorTest**           | 2–5 ms           | 0–2 ms          | 1–3 ms           | Cursor benchmark load. |
| **benchmarkDB.testCollection**       | 2–5 ms           | 0–2 ms          | 1–3 ms           | Main benchmark workload. |
| **config.system_sessions_bench**     | 2–6 ms           | 0–2 ms          | 1–3 ms           | System/benchmark sessions. |
| **config.transactions_bench**        | 2–6 ms           | 0–2 ms          | 1–3 ms           | Internal transaction benchmark. |
| **local.system_replset_bench**       | 2–5 ms           | 0–2 ms          | 1–3 ms           | Local replica set benchmark. |
| **test.admin_system_version_test**   | 2–5 ms           | 0–2 ms          | 1–3 ms           | Version check workload. |
| **test.atlascli**                    | 2–5 ms           | 0–2 ms          | 1–3 ms           | CLI/system background operations (test namespace). |
| **test.system_sessions_bench**       | 2–5 ms           | 0–2 ms          | 1–3 ms           | Session benchmark (test namespace). |
| **admin.system.version**             | 0 ms             | 0 ms            | 0 ms             | Appears inactive or instantaneous responses. |



With the MongoDB performance summary of the results on your Arm-based Azure Cobalt 100 VM, you will notice:
  - Stable, low-latency behavior across all tested namespaces.
  - Read operations are near-instant (sub-2 ms), showing efficient query performance.
  - Write operations remain consistently low, supporting reliable data modifications.
  - System and transaction overheads are predictable, indicating a well-tuned environment for concurrent/replicated workloads.

**Overall observation:** MongoDB operations on Arm64 are lightweight with predictable, low-latency reads and writes, confirming efficient performance on Azure Ubuntu Pro 24.04 LTS Arm64 Virtual machines. 
