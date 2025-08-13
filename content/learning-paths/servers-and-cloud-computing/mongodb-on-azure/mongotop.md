---
title: Monitor MongoDB with mongotop
weight: 8

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Monitoring MongoDB Performance using Mongotop
This guide demonstrates how to monitor MongoDB performance using **mongotop**, showing **read/write** activity across collections in **real time**. It includes benchmark results collected on Azure Arm64 virtual machines, providing a reference for expected latencies.

### Run mongotop — Terminal 2

```console
mongotop 2
```
**mongotop** shows how much time the server spends reading and writing each collection (refreshes every 2 seconds here). It helps you see which collections are busiest and whether reads or writes dominate.

You should see an output similar to:
```output
2025-08-13T08:02:06.613+0000    connected to: mongodb://localhost/
                            ns    total    read    write    2025-08-13T08:02:08Z
                admin.atlascli      4ms     2ms      2ms
        benchmarkDB.cursorTest      4ms     1ms      2ms
    benchmarkDB.testCollection      4ms     1ms      2ms
    local.system_replset_bench      4ms     1ms      2ms
                 test.atlascli      4ms     2ms      2ms
  config.system_sessions_bench      3ms     1ms      1ms
     config.transactions_bench      3ms     1ms      1ms
    test.system_sessions_bench      3ms     1ms      2ms
test.admin_system_version_test      1ms     0ms      1ms
          admin.system.version      0ms     0ms      0ms

                            ns    total    read    write    2025-08-13T08:02:10Z
test.admin_system_version_test      4ms     1ms      2ms
                admin.atlascli      2ms     1ms      1ms
        benchmarkDB.cursorTest      2ms     0ms      1ms
    benchmarkDB.testCollection      2ms     1ms      1ms
     config.transactions_bench      2ms     0ms      1ms
    local.system_replset_bench      2ms     1ms      1ms
                 test.atlascli      2ms     0ms      1ms
    test.system_sessions_bench      2ms     1ms      1ms
  config.system_sessions_bench      1ms     0ms      1ms
          admin.system.version      0ms     0ms      0ms

                            ns    total    read    write    2025-08-13T08:02:12Z
                admin.atlascli      5ms     2ms      2ms
        benchmarkDB.cursorTest      4ms     2ms      2ms
    benchmarkDB.testCollection      4ms     2ms      2ms
  config.system_sessions_bench      4ms     2ms      2ms
     config.transactions_bench      4ms     2ms      2ms
    local.system_replset_bench      4ms     2ms      2ms
test.admin_system_version_test      4ms     2ms      2ms
                 test.atlascli      4ms     2ms      2ms
    test.system_sessions_bench      4ms     2ms      2ms
          admin.system.version      0ms     0ms      0ms

                            ns    total    read    write    2025-08-13T08:02:14Z
                admin.atlascli      2ms     1ms      1ms
        benchmarkDB.cursorTest      2ms     1ms      1ms
    benchmarkDB.testCollection      2ms     1ms      1ms
  config.system_sessions_bench      2ms     1ms      1ms
     config.transactions_bench      2ms     1ms      1ms
    local.system_replset_bench      2ms     1ms      1ms
test.admin_system_version_test      2ms     1ms      1ms
                 test.atlascli      2ms     1ms      1ms
    test.system_sessions_bench      2ms     1ms      1ms
          admin.system.version      0ms     0ms      0ms

                            ns    total    read    write    2025-08-13T08:02:16Z
                admin.atlascli      4ms     1ms      2ms
        benchmarkDB.cursorTest      4ms     2ms      2ms
    benchmarkDB.testCollection      4ms     1ms      2ms
  config.system_sessions_bench      4ms     1ms      2ms
     config.transactions_bench      4ms     2ms      2ms
    local.system_replset_bench      4ms     1ms      2ms
test.admin_system_version_test      4ms     1ms      2ms
                 test.atlascli      4ms     1ms      2ms
    test.system_sessions_bench      4ms     1ms      2ms
          admin.system.version      0ms     0ms      0ms

                            ns    total    read    write    2025-08-13T08:02:18Z
                admin.atlascli      2ms     1ms      1ms
        benchmarkDB.cursorTest      2ms     1ms      1ms
    benchmarkDB.testCollection      2ms     0ms      1ms
  config.system_sessions_bench      2ms     1ms      0ms
     config.transactions_bench      2ms     1ms      0ms
    local.system_replset_bench      2ms     0ms      1ms
test.admin_system_version_test      2ms     1ms      1ms
                 test.atlascli      2ms     0ms      1ms
    test.system_sessions_bench      2ms     0ms      1ms
          admin.system.version      0ms     0ms      0ms

                            ns    total    read    write    2025-08-13T08:02:20Z
                admin.atlascli      4ms     2ms      2ms
        benchmarkDB.cursorTest      4ms     1ms      2ms
    benchmarkDB.testCollection      4ms     2ms      2ms
     config.transactions_bench      4ms     2ms      1ms
    local.system_replset_bench      4ms     1ms      2ms
test.admin_system_version_test      4ms     1ms      2ms
                 test.atlascli      4ms     1ms      2ms
    test.system_sessions_bench      4ms     2ms      2ms
  config.system_sessions_bench      3ms     1ms      1ms
          admin.system.version      0ms     0ms      0ms

                            ns    total    read    write    2025-08-13T08:02:22Z
                admin.atlascli      2ms     1ms      1ms
        benchmarkDB.cursorTest      2ms     1ms      1ms
    benchmarkDB.testCollection      2ms     1ms      1ms
  config.system_sessions_bench      2ms     0ms      1ms
    local.system_replset_bench      2ms     1ms      1ms
test.admin_system_version_test      2ms     1ms      1ms
                 test.atlascli      2ms     1ms      1ms
    test.system_sessions_bench      2ms     1ms      1ms
     config.transactions_bench      1ms     0ms      1ms
          admin.system.version      0ms     0ms      0ms

                            ns    total    read    write    2025-08-13T08:02:24Z
                admin.atlascli      4ms     2ms      2ms
        benchmarkDB.cursorTest      4ms     2ms      2ms
    benchmarkDB.testCollection      4ms     2ms      2ms
  config.system_sessions_bench      4ms     2ms      2ms
     config.transactions_bench      4ms     2ms      2ms
    local.system_replset_bench      4ms     2ms      2ms
test.admin_system_version_test      4ms     2ms      2ms
                 test.atlascli      4ms     2ms      2ms
    test.system_sessions_bench      4ms     2ms      2ms
          admin.system.version      0ms     0ms      0ms

                            ns    total    read    write    2025-08-13T08:02:26Z
                admin.atlascli      2ms     1ms      1ms
        benchmarkDB.cursorTest      2ms     1ms      1ms
    benchmarkDB.testCollection      2ms     1ms      1ms
  config.system_sessions_bench      2ms     1ms      1ms
     config.transactions_bench      2ms     1ms      1ms
    local.system_replset_bench      2ms     1ms      1ms
test.admin_system_version_test      2ms     1ms      1ms
                 test.atlascli      2ms     1ms      1ms
    test.system_sessions_bench      2ms     1ms      1ms
          admin.system.version      0ms     0ms      0ms

                            ns    total    read    write    2025-08-13T08:02:28Z
                admin.atlascli      5ms     2ms      2ms
        benchmarkDB.cursorTest      5ms     2ms      2ms
    benchmarkDB.testCollection      5ms     2ms      2ms
     config.transactions_bench      5ms     3ms      2ms
    local.system_replset_bench      5ms     2ms      2ms
                 test.atlascli      5ms     2ms      2ms
    test.system_sessions_bench      5ms     2ms      2ms
  config.system_sessions_bench      4ms     2ms      2ms
test.admin_system_version_test      2ms     1ms      1ms
          admin.system.version      0ms     0ms      0ms

                            ns    total    read    write    2025-08-13T08:02:30Z
test.admin_system_version_test      4ms     2ms      2ms
                admin.atlascli      2ms     1ms      1ms
        benchmarkDB.cursorTest      2ms     1ms      1ms
    benchmarkDB.testCollection      2ms     1ms      1ms
  config.system_sessions_bench      2ms     1ms      1ms
     config.transactions_bench      2ms     1ms      1ms
    local.system_replset_bench      2ms     1ms      1ms
                 test.atlascli      2ms     1ms      1ms
    test.system_sessions_bench      2ms     1ms      1ms
          admin.system.version      0ms     0ms      0ms

                            ns    total    read    write    2025-08-13T08:02:32Z
    benchmarkDB.testCollection      5ms     2ms      2ms
                admin.atlascli      4ms     2ms      2ms
        benchmarkDB.cursorTest      4ms     1ms      2ms
  config.system_sessions_bench      4ms     2ms      2ms
     config.transactions_bench      4ms     2ms      2ms
    local.system_replset_bench      4ms     2ms      2ms
test.admin_system_version_test      2ms     1ms      1ms
                 test.atlascli      2ms     1ms      1ms
    test.system_sessions_bench      2ms     1ms      1ms
          admin.system.version      0ms     0ms      0ms

                            ns    total    read    write    2025-08-13T08:02:34Z
test.admin_system_version_test      4ms     2ms      2ms
                 test.atlascli      4ms     2ms      2ms
    test.system_sessions_bench      4ms     2ms      2ms
        benchmarkDB.cursorTest      3ms     2ms      1ms
                admin.atlascli      2ms     1ms      1ms
    benchmarkDB.testCollection      2ms     1ms      1ms
  config.system_sessions_bench      2ms     1ms      1ms
     config.transactions_bench      2ms     1ms      1ms
    local.system_replset_bench      2ms     1ms      1ms
          admin.system.version      0ms     0ms      0ms

                            ns    total    read    write    2025-08-13T08:02:36Z
                admin.atlascli      5ms     2ms      2ms
  config.system_sessions_bench      4ms     2ms      2ms
     config.transactions_bench      4ms     2ms      2ms
        benchmarkDB.cursorTest      2ms     1ms      1ms
    benchmarkDB.testCollection      2ms     1ms      1ms
    local.system_replset_bench      2ms     1ms      1ms
test.admin_system_version_test      2ms     1ms      1ms
                 test.atlascli      2ms     1ms      1ms
    test.system_sessions_bench      2ms     1ms      1ms
          admin.system.version      0ms     0ms      0ms

                            ns    total    read    write    2025-08-13T08:02:38Z
        benchmarkDB.cursorTest      5ms     2ms      2ms
    benchmarkDB.testCollection      5ms     2ms      2ms
    local.system_replset_bench      5ms     2ms      2ms
test.admin_system_version_test      5ms     2ms      2ms
                 test.atlascli      5ms     2ms      2ms
    test.system_sessions_bench      5ms     2ms      2ms
                admin.atlascli      2ms     1ms      1ms
  config.system_sessions_bench      2ms     1ms      1ms
     config.transactions_bench      2ms     1ms      1ms
          admin.system.version      0ms     0ms      0ms

                            ns    total    read    write    2025-08-13T08:02:40Z
                admin.atlascli      4ms     2ms      2ms
        benchmarkDB.cursorTest      2ms     1ms      1ms
    benchmarkDB.testCollection      2ms     1ms      1ms
  config.system_sessions_bench      2ms     1ms      1ms
     config.transactions_bench      2ms     1ms      1ms
    local.system_replset_bench      2ms     1ms      1ms
test.admin_system_version_test      2ms     1ms      1ms
                 test.atlascli      2ms     1ms      1ms
    test.system_sessions_bench      2ms     1ms      1ms
          admin.system.version      0ms     0ms      0ms

                            ns    total    read    write    2025-08-13T08:02:42Z
        benchmarkDB.cursorTest      5ms     2ms      2ms
    benchmarkDB.testCollection      5ms     2ms      2ms
    local.system_replset_bench      5ms     2ms      2ms
test.admin_system_version_test      5ms     2ms      2ms
    test.system_sessions_bench      5ms     2ms      2ms
  config.system_sessions_bench      4ms     2ms      2ms
     config.transactions_bench      4ms     2ms      2ms
                 test.atlascli      4ms     2ms      2ms
                admin.atlascli      2ms     1ms      1ms
          admin.system.version      0ms     0ms      0ms

                            ns    total    read    write    2025-08-13T08:02:44Z
                admin.atlascli      2ms     1ms      1ms
        benchmarkDB.cursorTest      2ms     1ms      1ms
    benchmarkDB.testCollection      2ms     1ms      1ms
  config.system_sessions_bench      2ms     1ms      1ms
     config.transactions_bench      2ms     1ms      1ms
    local.system_replset_bench      2ms     1ms      1ms
test.admin_system_version_test      2ms     1ms      1ms
                 test.atlascli      2ms     1ms      1ms
    test.system_sessions_bench      2ms     1ms      1ms
          admin.system.version      0ms     0ms      0ms

                            ns    total    read    write    2025-08-13T08:02:46Z
                admin.atlascli      5ms     2ms      2ms
        benchmarkDB.cursorTest      5ms     2ms      2ms
    benchmarkDB.testCollection      5ms     2ms      3ms
    local.system_replset_bench      5ms     2ms      2ms
test.admin_system_version_test      5ms     2ms      2ms
                 test.atlascli      5ms     2ms      2ms
    test.system_sessions_bench      5ms     2ms      2ms
  config.system_sessions_bench      4ms     2ms      2ms
     config.transactions_bench      4ms     2ms      2ms
          admin.system.version      0ms     0ms      0ms

                            ns    total    read    write    2025-08-13T08:02:48Z
                admin.atlascli      2ms     1ms      1ms
        benchmarkDB.cursorTest      2ms     1ms      1ms
    benchmarkDB.testCollection      2ms     1ms      1ms
  config.system_sessions_bench      2ms     1ms      1ms
     config.transactions_bench      2ms     1ms      1ms
    local.system_replset_bench      2ms     1ms      1ms
test.admin_system_version_test      2ms     1ms      1ms
                 test.atlascli      2ms     1ms      1ms
    test.system_sessions_bench      2ms     1ms      1ms
          admin.system.version      0ms     0ms      0ms

                            ns    total    read    write    2025-08-13T08:02:50Z
                admin.atlascli      5ms     2ms      3ms
        benchmarkDB.cursorTest      5ms     2ms      2ms
    benchmarkDB.testCollection      5ms     2ms      2ms
     config.transactions_bench      5ms     2ms      2ms
    local.system_replset_bench      5ms     2ms      2ms
test.admin_system_version_test      5ms     2ms      2ms
                 test.atlascli      5ms     2ms      3ms
    test.system_sessions_bench      5ms     2ms      2ms
  config.system_sessions_bench      4ms     2ms      2ms
          admin.system.version      0ms     0ms      0ms

                            ns    total    read    write    2025-08-13T08:02:52Z
                admin.atlascli      2ms     1ms      1ms
        benchmarkDB.cursorTest      2ms     1ms      1ms
    benchmarkDB.testCollection      2ms     1ms      1ms
  config.system_sessions_bench      2ms     1ms      1ms
     config.transactions_bench      2ms     1ms      1ms
    local.system_replset_bench      2ms     1ms      1ms
test.admin_system_version_test      2ms     1ms      1ms
                 test.atlascli      2ms     1ms      1ms
    test.system_sessions_bench      2ms     1ms      1ms
          admin.system.version      0ms     0ms      0ms

                            ns    total    read    write    2025-08-13T08:02:54Z
                admin.atlascli      5ms     2ms      3ms
  config.system_sessions_bench      5ms     2ms      2ms
     config.transactions_bench      5ms     2ms      2ms
    local.system_replset_bench      5ms     2ms      3ms
    benchmarkDB.testCollection      4ms     1ms      2ms
        benchmarkDB.cursorTest      2ms     1ms      1ms
test.admin_system_version_test      2ms     1ms      1ms
                 test.atlascli      2ms     1ms      1ms
    test.system_sessions_bench      2ms     1ms      1ms
          admin.system.version      0ms     0ms      0ms

                            ns    total    read    write    2025-08-13T08:02:56Z
                 test.atlascli      6ms     2ms      3ms
        benchmarkDB.cursorTest      5ms     2ms      2ms
test.admin_system_version_test      5ms     2ms      2ms
    test.system_sessions_bench      5ms     2ms      2ms
    benchmarkDB.testCollection      4ms     2ms      1ms
    local.system_replset_bench      3ms     1ms      1ms
                admin.atlascli      2ms     1ms      1ms
  config.system_sessions_bench      2ms     1ms      1ms
     config.transactions_bench      2ms     1ms      1ms
          admin.system.version      0ms     0ms      0ms

                            ns    total    read    write    2025-08-13T08:02:58Z
    test.system_sessions_bench      3ms     1ms      1ms
                admin.atlascli      2ms     1ms      1ms
        benchmarkDB.cursorTest      2ms     1ms      1ms
    benchmarkDB.testCollection      2ms     1ms      1ms
  config.system_sessions_bench      2ms     1ms      1ms
     config.transactions_bench      2ms     1ms      1ms
    local.system_replset_bench      2ms     1ms      1ms
test.admin_system_version_test      2ms     1ms      1ms
                 test.atlascli      2ms     1ms      1ms
          admin.system.version      0ms     0ms      0ms

                            ns    total    read    write    2025-08-13T08:03:00Z
                admin.atlascli      6ms     2ms      3ms
    benchmarkDB.testCollection      6ms     2ms      3ms
        benchmarkDB.cursorTest      5ms     2ms      3ms
  config.system_sessions_bench      5ms     2ms      2ms
     config.transactions_bench      5ms     2ms      2ms
    local.system_replset_bench      5ms     2ms      3ms
test.admin_system_version_test      5ms     2ms      2ms
                 test.atlascli      5ms     2ms      3ms
    test.system_sessions_bench      5ms     2ms      3ms
          admin.system.version      0ms     0ms      0ms

                            ns    total    read    write    2025-08-13T08:03:02Z
                 test.atlascli      3ms     1ms      1ms
                admin.atlascli      2ms     1ms      1ms
        benchmarkDB.cursorTest      2ms     1ms      1ms
    benchmarkDB.testCollection      2ms     1ms      1ms
  config.system_sessions_bench      2ms     1ms      1ms
     config.transactions_bench      2ms     1ms      1ms
    local.system_replset_bench      2ms     1ms      1ms
test.admin_system_version_test      2ms     1ms      1ms
    test.system_sessions_bench      2ms     1ms      1ms
          admin.system.version      0ms     0ms      0ms

                            ns    total    read    write    2025-08-13T08:03:04Z
                admin.atlascli      5ms     2ms      3ms
        benchmarkDB.cursorTest      5ms     2ms      3ms
    benchmarkDB.testCollection      5ms     2ms      2ms
  config.system_sessions_bench      5ms     2ms      2ms
     config.transactions_bench      5ms     2ms      2ms
    local.system_replset_bench      5ms     2ms      3ms
                 test.atlascli      5ms     2ms      3ms
test.admin_system_version_test      2ms     1ms      1ms
    test.system_sessions_bench      2ms     1ms      1ms
          admin.system.version      0ms     0ms      0ms

                            ns    total    read    write    2025-08-13T08:03:06Z
test.admin_system_version_test      5ms     2ms      2ms
    test.system_sessions_bench      5ms     2ms      3ms
    benchmarkDB.testCollection      3ms     1ms      1ms
                 test.atlascli      3ms     1ms      1ms
                admin.atlascli      2ms     1ms      1ms
        benchmarkDB.cursorTest      2ms     1ms      1ms
  config.system_sessions_bench      2ms     1ms      1ms
     config.transactions_bench      2ms     1ms      1ms
    local.system_replset_bench      2ms     1ms      1ms
          admin.system.version      0ms     0ms      0ms

                            ns    total    read    write    2025-08-13T08:03:08Z
                admin.atlascli      2ms     1ms      1ms
        benchmarkDB.cursorTest      2ms     1ms      1ms
    benchmarkDB.testCollection      2ms     1ms      1ms
  config.system_sessions_bench      2ms     1ms      1ms
     config.transactions_bench      2ms     1ms      1ms
    local.system_replset_bench      2ms     1ms      1ms
test.admin_system_version_test      2ms     1ms      1ms
                 test.atlascli      2ms     1ms      1ms
    test.system_sessions_bench      2ms     1ms      1ms
          admin.system.version      0ms     0ms      0ms
```

### Explanation of Metrics and Namespaces

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

{{% notice Note %}}
Benchmarking was performed in both an Azure Linux 3.0 Docker container and an Azure Linux 3.0 virtual machine, with comparable results.
{{% /notice %}}

Accordingly, this Learning path includes benchmark results from virtual machines only, for both x86 and Arm64 platforms.

### Benchmark summary on x86_64:
The following benchmark results are collected on an x86_64 **D4s_v4 Azure virtual machine using the Azure Linux 3.0 image published by Ntegral Inc**.

| Namespace (ns) | Total Time Range | Read Time Range | Write Time Range | Notes |
| :------------------------------- | :--------------- | :-------------- | :--------------- | :------------------------------------------------------------------------------------------------------------------------------- |
| admin.atlascli | 2–7 ms | 0–2 ms | 1–4 ms | Admin CLI operations. |
| benchmarkDB.cursorTest | 2–7 ms | 0–3 ms | 1–4 ms | Secondary benchmark load. |
| benchmarkDB.testCollection | 2–6 ms | 0–2 ms | 1–3 ms | Main benchmark workload. |
| config.system_sessions_bench | 1–5 ms | 0–2 ms | 1–3 ms | System/benchmark sessions. |
| config.transactions_bench | 2–6 ms | 0–2 ms | 1–4 ms | Internal transaction benchmark. |
| local.system_replset_bench | 1–6 ms | 0–2 ms | 1–3 ms | Local replica set benchmark. |
| test.admin_system_version_test | 2–5 ms | 0–2 ms | 1–3 ms | Light version check activity. |
| test.atlascli | 1–6 ms | 0–2 ms | 1–3 ms | CLI/system background operations. |
| test.system_sessions_bench | 2–6 ms | 0–2 ms | 1–3 ms | System/benchmark sessions (test namespace). |
| admin.system.version | 0–0 ms | 0–0 ms | 0–0 ms | Appears to be inactive or have instantaneous responses. |


### Benchmark summary on Arm64:
The following benchmark results were collected on an Arm64 **D4ps_v6 Azure virtual machine created from a custom Azure Linux 3.0 image using the AArch64 ISO**.

| Namespace (ns) | Total Time Range | Read Time Range | Write Time Range | Notes |
| :------------------------------- | :--------------- | :-------------- | :--------------- | :------------------------------------------------------------------------------------------------------------------------------- |
| admin.atlascli | 2–6 ms | 1–2 ms | 1–3 ms | Admin CLI operations. |
| benchmarkDB.cursorTest | 2–5 ms | 0–2 ms | 1–3 ms | Secondary benchmark load. |
| benchmarkDB.testCollection | 2–6 ms | 0–2 ms | 1–3 ms | Main benchmark workload. |
| config.system_sessions_bench | 1–5 ms | 0–2 ms | 1–2 ms | System/benchmark sessions. |
| config.transactions_bench | 1–5 ms | 0–3 ms | 1–2 ms | Internal transaction benchmark. |
| local.system_replset_bench | 2–5 ms | 0–2 ms | 1–3 ms | Local replica set benchmark. |
| test.admin_system_version_test | 1–5 ms | 0–2 ms | 1–2 ms | Light version check activity. |
| test.atlascli | 2–6 ms | 0–2 ms | 1–3 ms | CLI/system background operations. |
| test.system_sessions_bench | 2–5 ms | 0–2 ms | 1–3 ms | System/benchmark sessions (test namespace). |
| admin.system.version | 0–0 ms | 0–0 ms | 0–0 ms | Appears to be inactive or have instantaneous responses. |

### Highlights from Azure Linux Arm64 Benchmarking

- **Most active namespaces:** admin.atlascli, benchmarkDB.testCollection, benchmarkDB.cursorTest, and test.atlascli — total times 2–6ms.
- **Read patterns:** Reads across collections are 0–2ms, showing low-latency performance on Arm64.
- **Write patterns:** Writes are mostly 1–3ms, indicating a balanced workload on Arm64.
- **Less active namespaces:** config.system_sessions_bench, config.transactions_bench, test.system_sessions_bench — total 1–5ms.
- **Idle collections:** admin.system.version remains 0ms, showing minimal activity.
- **Overall observation:** MongoDB operations on Arm64 are lightweight with consistently low-latency reads and writes, confirming efficient Arm64 performance.

Now, let us monitor MongoDB using Mongostat.
