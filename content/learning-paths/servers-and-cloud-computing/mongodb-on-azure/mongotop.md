---
title: Monitor MongoDB with mongotop
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Monitoring MongoDB Performance using Mongotop
This guide demonstrates how to monitor MongoDB performance using **mongotop**, showing **read/write** activity across collections in **real time**. It includes benchmark results collected on Azure Arm64 virtual machines, providing a reference for expected latencies.

## Run mongotop — Terminal 2

```console
mongotop 2
```
**mongotop** shows how much time the server spends reading and writing each collection (refreshes every 2 seconds here). It helps you see which collections are busiest and whether reads or writes dominate.

You should see an output similar to:
```output
                         ns    total    read    write    2025-09-04T04:57:21Z
      benchmarkDB.cursorTest      7ms     1ms      6ms
              admin.atlascli      4ms     1ms      2ms
config.system_sessions_bench      3ms     1ms      2ms
  benchmarkDB.testCollection      2ms     0ms      1ms
   config.transactions_bench      2ms     0ms      1ms
  local.system_replset_bench      2ms     0ms      1ms
        admin.system.version      0ms     0ms      0ms
             baselineDB.perf      0ms     0ms      0ms
   baselineDB.testCollection      0ms     0ms      0ms
      config.system.sessions      0ms     0ms      0ms

                            ns    total    read    write    2025-09-04T04:57:23Z
        benchmarkDB.cursorTest      4ms     1ms      2ms
    benchmarkDB.testCollection      4ms     1ms      2ms
     config.transactions_bench      4ms     1ms      2ms
test.admin_system_version_test      4ms     1ms      2ms
                 test.atlascli      4ms     1ms      2ms
    test.system_sessions_bench      4ms     1ms      2ms
    local.system_replset_bench      3ms     1ms      2ms
                admin.atlascli      2ms     0ms      1ms
  config.system_sessions_bench      2ms     1ms      1ms
          admin.system.version      0ms     0ms      0ms

                            ns    total    read    write    2025-09-04T04:57:25Z
                admin.atlascli      4ms     1ms      2ms
  config.system_sessions_bench      4ms     1ms      2ms
     config.transactions_bench      4ms     1ms      2ms
    local.system_replset_bench      4ms     1ms      2ms
        benchmarkDB.cursorTest      2ms     0ms      1ms
    benchmarkDB.testCollection      2ms     0ms      1ms
test.admin_system_version_test      2ms     0ms      1ms
                 test.atlascli      2ms     0ms      1ms
    test.system_sessions_bench      2ms     0ms      1ms
          admin.system.version      0ms     0ms      0ms

                            ns    total    read    write    2025-09-04T04:57:27Z
        benchmarkDB.cursorTest      4ms     1ms      2ms
    benchmarkDB.testCollection      4ms     1ms      2ms
test.admin_system_version_test      4ms     1ms      2ms
                 test.atlascli      4ms     1ms      2ms
    test.system_sessions_bench      4ms     1ms      2ms
                admin.atlascli      2ms     0ms      1ms
  config.system_sessions_bench      2ms     0ms      1ms
     config.transactions_bench      2ms     1ms      1ms
    local.system_replset_bench      2ms     0ms      1ms
          admin.system.version      0ms     0ms      0ms

                            ns    total    read    write    2025-09-04T04:57:29Z
                admin.atlascli      4ms     1ms      2ms
    benchmarkDB.testCollection      4ms     1ms      2ms
  config.system_sessions_bench      4ms     1ms      2ms
     config.transactions_bench      4ms     1ms      2ms
    local.system_replset_bench      4ms     1ms      2ms
        benchmarkDB.cursorTest      3ms     1ms      2ms
test.admin_system_version_test      2ms     0ms      1ms
                 test.atlascli      2ms     1ms      1ms
    test.system_sessions_bench      2ms     0ms      1ms
          admin.system.version      0ms     0ms      0ms

                            ns    total    read    write    2025-09-04T04:57:31Z
test.admin_system_version_test      4ms     2ms      2ms
                 test.atlascli      4ms     2ms      2ms
    test.system_sessions_bench      4ms     2ms      2ms
        benchmarkDB.cursorTest      3ms     1ms      1ms
                admin.atlascli      2ms     1ms      1ms
    benchmarkDB.testCollection      2ms     0ms      1ms
  config.system_sessions_bench      2ms     1ms      1ms
     config.transactions_bench      2ms     0ms      1ms
    local.system_replset_bench      2ms     0ms      1ms
          admin.system.version      0ms     0ms      0ms

                            ns    total    read    write    2025-09-04T04:57:33Z
                admin.atlascli      4ms     2ms      2ms
    benchmarkDB.testCollection      4ms     1ms      2ms
  config.system_sessions_bench      4ms     1ms      2ms
     config.transactions_bench      4ms     1ms      2ms
    local.system_replset_bench      4ms     1ms      2ms
        benchmarkDB.cursorTest      2ms     1ms      1ms
test.admin_system_version_test      2ms     1ms      1ms
                 test.atlascli      2ms     0ms      1ms
    test.system_sessions_bench      2ms     1ms      1ms
          admin.system.version      0ms     0ms      0ms

                            ns    total    read    write    2025-09-04T04:57:35Z
        benchmarkDB.cursorTest      4ms     1ms      2ms
test.admin_system_version_test      4ms     1ms      2ms
                 test.atlascli      4ms     1ms      2ms
    test.system_sessions_bench      4ms     1ms      2ms
                admin.atlascli      2ms     0ms      1ms
    benchmarkDB.testCollection      2ms     1ms      1ms
  config.system_sessions_bench      2ms     0ms      1ms
     config.transactions_bench      2ms     0ms      1ms
    local.system_replset_bench      2ms     0ms      1ms
          admin.system.version      0ms     0ms      0ms

                            ns    total    read    write    2025-09-04T04:57:37Z
                admin.atlascli      4ms     1ms      2ms
    benchmarkDB.testCollection      4ms     1ms      2ms
  config.system_sessions_bench      4ms     1ms      2ms
     config.transactions_bench      4ms     1ms      2ms
    local.system_replset_bench      4ms     1ms      2ms
        benchmarkDB.cursorTest      2ms     0ms      1ms
test.admin_system_version_test      2ms     0ms      1ms
                 test.atlascli      2ms     0ms      1ms
    test.system_sessions_bench      2ms     0ms      1ms
          admin.system.version      0ms     0ms      0ms

                            ns    total    read    write    2025-09-04T04:57:39Z
        benchmarkDB.cursorTest      4ms     2ms      2ms
test.admin_system_version_test      4ms     1ms      2ms
                 test.atlascli      4ms     1ms      2ms
    test.system_sessions_bench      4ms     1ms      2ms
                admin.atlascli      2ms     0ms      1ms
    benchmarkDB.testCollection      2ms     1ms      1ms
  config.system_sessions_bench      2ms     0ms      1ms
     config.transactions_bench      2ms     0ms      1ms
    local.system_replset_bench      2ms     1ms      1ms
          admin.system.version      0ms     0ms      0ms

                            ns    total    read    write    2025-09-04T04:57:41Z
                admin.atlascli      4ms     1ms      2ms
    benchmarkDB.testCollection      4ms     1ms      2ms
  config.system_sessions_bench      4ms     2ms      2ms
     config.transactions_bench      4ms     2ms      2ms
    local.system_replset_bench      4ms     1ms      2ms
        benchmarkDB.cursorTest      2ms     1ms      1ms
test.admin_system_version_test      2ms     1ms      1ms
                 test.atlascli      2ms     0ms      1ms
    test.system_sessions_bench      2ms     1ms      1ms
          admin.system.version      0ms     0ms      0ms

                            ns    total    read    write    2025-09-04T04:57:43Z
        benchmarkDB.cursorTest      5ms     2ms      2ms
    test.system_sessions_bench      5ms     2ms      2ms
test.admin_system_version_test      4ms     2ms      2ms
                 test.atlascli      4ms     1ms      2ms
    benchmarkDB.testCollection      3ms     2ms      1ms
                admin.atlascli      2ms     1ms      1ms
  config.system_sessions_bench      2ms     0ms      1ms
     config.transactions_bench      2ms     1ms      1ms
    local.system_replset_bench      2ms     0ms      1ms
          admin.system.version      0ms     0ms      0ms

                            ns    total    read    write    2025-09-04T04:57:45Z
                admin.atlascli      5ms     2ms      3ms
  config.system_sessions_bench      5ms     2ms      3ms
     config.transactions_bench      5ms     2ms      2ms
        benchmarkDB.cursorTest      2ms     1ms      1ms
    benchmarkDB.testCollection      2ms     1ms      1ms
    local.system_replset_bench      2ms     1ms      1ms
test.admin_system_version_test      2ms     1ms      1ms
                 test.atlascli      2ms     0ms      1ms
    test.system_sessions_bench      2ms     1ms      1ms
          admin.system.version      0ms     0ms      0ms

                            ns    total    read    write    2025-09-04T04:57:47Z
        benchmarkDB.cursorTest      5ms     2ms      2ms
    benchmarkDB.testCollection      5ms     2ms      2ms
    local.system_replset_bench      5ms     2ms      2ms
test.admin_system_version_test      5ms     2ms      3ms
                 test.atlascli      5ms     2ms      2ms
    test.system_sessions_bench      4ms     2ms      2ms
                admin.atlascli      2ms     1ms      1ms
  config.system_sessions_bench      2ms     0ms      1ms
     config.transactions_bench      2ms     0ms      1ms
          admin.system.version      0ms     0ms      0ms

                            ns    total    read    write    2025-09-04T04:57:49Z
                admin.atlascli      5ms     1ms      3ms
  config.system_sessions_bench      4ms     1ms      2ms
        benchmarkDB.cursorTest      2ms     0ms      1ms
    benchmarkDB.testCollection      2ms     0ms      1ms
     config.transactions_bench      2ms     0ms      1ms
    local.system_replset_bench      2ms     0ms      1ms
test.admin_system_version_test      2ms     0ms      1ms
                 test.atlascli      2ms     0ms      1ms
    test.system_sessions_bench      2ms     0ms      1ms
          admin.system.version      0ms     0ms      0ms

                            ns    total    read    write    2025-09-04T04:57:51Z
        benchmarkDB.cursorTest      4ms     1ms      2ms
    benchmarkDB.testCollection      4ms     1ms      2ms
     config.transactions_bench      4ms     1ms      3ms
    local.system_replset_bench      4ms     1ms      2ms
test.admin_system_version_test      4ms     1ms      2ms
                 test.atlascli      4ms     1ms      2ms
    test.system_sessions_bench      4ms     1ms      2ms
                admin.atlascli      2ms     0ms      1ms
  config.system_sessions_bench      2ms     1ms      1ms
          admin.system.version      0ms     0ms      0ms

                            ns    total    read    write    2025-09-04T04:57:53Z
                admin.atlascli      2ms     0ms      1ms
        benchmarkDB.cursorTest      2ms     1ms      1ms
    benchmarkDB.testCollection      2ms     1ms      1ms
  config.system_sessions_bench      2ms     0ms      1ms
     config.transactions_bench      2ms     0ms      1ms
    local.system_replset_bench      2ms     0ms      1ms
test.admin_system_version_test      2ms     1ms      1ms
                 test.atlascli      2ms     1ms      1ms
    test.system_sessions_bench      2ms     1ms      1ms
          admin.system.version      0ms     0ms      0ms

                            ns    total    read    write    2025-09-04T04:57:55Z
                admin.atlascli      5ms     2ms      2ms
     config.transactions_bench      5ms     2ms      2ms
    test.system_sessions_bench      5ms     2ms      2ms
        benchmarkDB.cursorTest      4ms     1ms      2ms
    benchmarkDB.testCollection      4ms     1ms      2ms
  config.system_sessions_bench      4ms     2ms      2ms
    local.system_replset_bench      4ms     1ms      2ms
test.admin_system_version_test      4ms     2ms      2ms
                 test.atlascli      4ms     2ms      2ms
          admin.system.version      0ms     0ms      0ms

                            ns    total    read    write    2025-09-04T04:57:57Z
                admin.atlascli      2ms     1ms      1ms
        benchmarkDB.cursorTest      2ms     0ms      1ms
    benchmarkDB.testCollection      2ms     1ms      1ms
  config.system_sessions_bench      2ms     1ms      1ms
     config.transactions_bench      2ms     0ms      1ms
    local.system_replset_bench      2ms     1ms      1ms
test.admin_system_version_test      2ms     1ms      1ms
                 test.atlascli      2ms     0ms      1ms
    test.system_sessions_bench      2ms     1ms      1ms
          admin.system.version      0ms     0ms      0ms

                            ns    total    read    write    2025-09-04T04:57:59Z
                admin.atlascli      5ms     2ms      3ms
        benchmarkDB.cursorTest      5ms     2ms      3ms
    benchmarkDB.testCollection      5ms     2ms      3ms
  config.system_sessions_bench      5ms     2ms      3ms
     config.transactions_bench      5ms     2ms      3ms
    local.system_replset_bench      5ms     2ms      2ms
test.admin_system_version_test      5ms     2ms      3ms
                 test.atlascli      5ms     2ms      3ms
    test.system_sessions_bench      5ms     2ms      3ms
          admin.system.version      0ms     0ms      0ms

                            ns    total    read    write    2025-09-04T04:58:01Z
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

                            ns    total    read    write    2025-09-04T04:58:03Z
                admin.atlascli      5ms     2ms      3ms
        benchmarkDB.cursorTest      5ms     2ms      3ms
    benchmarkDB.testCollection      5ms     2ms      3ms
  config.system_sessions_bench      5ms     2ms      3ms
     config.transactions_bench      5ms     2ms      3ms
    local.system_replset_bench      5ms     2ms      3ms
test.admin_system_version_test      5ms     2ms      3ms
                 test.atlascli      5ms     2ms      3ms
    test.system_sessions_bench      5ms     2ms      3ms
          admin.system.version      0ms     0ms      0ms

                            ns    total    read    write    2025-09-04T04:58:05Z
     config.transactions_bench      3ms     1ms      1ms
                admin.atlascli      2ms     1ms      1ms
        benchmarkDB.cursorTest      2ms     1ms      1ms
    benchmarkDB.testCollection      2ms     1ms      1ms
  config.system_sessions_bench      2ms     1ms      1ms
    local.system_replset_bench      2ms     1ms      1ms
test.admin_system_version_test      2ms     1ms      1ms
                 test.atlascli      2ms     1ms      1ms
    test.system_sessions_bench      2ms     1ms      1ms
          admin.system.version      0ms     0ms      0ms

                            ns    total    read    write    2025-09-04T04:58:07Z
                admin.atlascli      5ms     2ms      3ms
        benchmarkDB.cursorTest      5ms     2ms      3ms
    benchmarkDB.testCollection      5ms     2ms      3ms
  config.system_sessions_bench      5ms     2ms      3ms
     config.transactions_bench      5ms     2ms      3ms
    local.system_replset_bench      5ms     2ms      3ms
                 test.atlascli      5ms     1ms      3ms
test.admin_system_version_test      2ms     1ms      1ms
    test.system_sessions_bench      2ms     1ms      1ms
          admin.system.version      0ms     0ms      0ms

                            ns    total    read    write    2025-09-04T04:58:09Z
test.admin_system_version_test      5ms     2ms      3ms
    test.system_sessions_bench      5ms     2ms      3ms
                admin.atlascli      2ms     1ms      1ms
        benchmarkDB.cursorTest      2ms     1ms      1ms
    benchmarkDB.testCollection      2ms     1ms      1ms
  config.system_sessions_bench      2ms     1ms      1ms
     config.transactions_bench      2ms     1ms      1ms
    local.system_replset_bench      2ms     1ms      1ms
                 test.atlascli      2ms     1ms      1ms
          admin.system.version      0ms     0ms      0ms

                            ns    total    read    write    2025-09-04T04:58:11Z
                admin.atlascli      5ms     2ms      3ms
  config.system_sessions_bench      5ms     2ms      3ms
     config.transactions_bench      5ms     2ms      3ms
        benchmarkDB.cursorTest      2ms     1ms      1ms
    benchmarkDB.testCollection      2ms     1ms      1ms
    local.system_replset_bench      2ms     1ms      1ms
test.admin_system_version_test      2ms     1ms      1ms
                 test.atlascli      2ms     1ms      1ms
    test.system_sessions_bench      2ms     1ms      1ms
          admin.system.version      0ms     0ms      0ms

                            ns    total    read    write    2025-09-04T04:58:13Z
        benchmarkDB.cursorTest      5ms     2ms      3ms
    benchmarkDB.testCollection      5ms     2ms      3ms
    local.system_replset_bench      5ms     2ms      3ms
test.admin_system_version_test      5ms     2ms      3ms
                 test.atlascli      5ms     2ms      3ms
    test.system_sessions_bench      5ms     2ms      3ms
     config.transactions_bench      3ms     1ms      1ms
                admin.atlascli      2ms     1ms      1ms
  config.system_sessions_bench      2ms     1ms      1ms
          admin.system.version      0ms     0ms      0ms

                            ns    total    read    write    2025-09-04T04:58:15Z
                admin.atlascli      3ms     1ms      1ms
     config.transactions_bench      3ms     1ms      1ms
test.admin_system_version_test      3ms     1ms      1ms
        benchmarkDB.cursorTest      2ms     1ms      1ms
    benchmarkDB.testCollection      2ms     1ms      1ms
  config.system_sessions_bench      2ms     1ms      1ms
    local.system_replset_bench      2ms     1ms      1ms
                 test.atlascli      2ms     1ms      1ms
    test.system_sessions_bench      2ms     1ms      1ms
          admin.system.version      0ms     0ms      0ms

                            ns    total    read    write    2025-09-04T04:58:17Z
                admin.atlascli      6ms     2ms      3ms
  config.system_sessions_bench      6ms     2ms      3ms
     config.transactions_bench      6ms     2ms      3ms
        benchmarkDB.cursorTest      5ms     2ms      3ms
    benchmarkDB.testCollection      5ms     2ms      3ms
    local.system_replset_bench      5ms     2ms      3ms
test.admin_system_version_test      5ms     2ms      3ms
                 test.atlascli      5ms     2ms      3ms
    test.system_sessions_bench      5ms     2ms      3ms
          admin.system.version      0ms     0ms      0ms

                            ns    total    read    write    2025-09-04T04:58:19Z
                admin.atlascli      3ms     1ms      1ms
        benchmarkDB.cursorTest      3ms     1ms      1ms
    benchmarkDB.testCollection      3ms     1ms      1ms
  config.system_sessions_bench      3ms     1ms      1ms
     config.transactions_bench      3ms     1ms      1ms
    local.system_replset_bench      3ms     1ms      1ms
test.admin_system_version_test      3ms     1ms      1ms
                 test.atlascli      3ms     1ms      1ms
    test.system_sessions_bench      2ms     1ms      1ms
          admin.system.version      0ms     0ms      0ms

                            ns    total    read    write    2025-09-04T04:58:21Z
                admin.atlascli      5ms     2ms      3ms
        benchmarkDB.cursorTest      5ms     2ms      3ms
    benchmarkDB.testCollection      5ms     2ms      3ms
  config.system_sessions_bench      5ms     2ms      3ms
     config.transactions_bench      5ms     2ms      3ms
    local.system_replset_bench      5ms     2ms      3ms
                 test.atlascli      5ms     1ms      3ms
    test.system_sessions_bench      3ms     1ms      1ms
test.admin_system_version_test      2ms     1ms      1ms
          admin.system.version      0ms     0ms      0ms

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
For easier comparison, shown here is a summary of benchmark results collected on an Arm64 **D4ps_v6 Azure Ubuntu Pro 24.04 LTS virtual machine**.

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

### Benchmark summary on x86_64:
Here is a summary of the benchmark results collected on x86_64 **D4s_v6 Ubuntu Pro 24.04 LTS virtual machine**.

| Namespace (ns)                    | Total Time Range | Read Time Range | Write Time Range | Notes |
| :-------------------------------- | :--------------- | :-------------- | :--------------- | :--------------------------------------------------------------- |
| **admin.atlascli**                | 1–5 ms           | 0–3 ms          | 0–2 ms           | Admin CLI activity. |
| **benchmarkDB.cursorTest**        | 1–3 ms           | 0–1 ms          | 0–1 ms           | Cursor iteration benchmark workload. |
| **benchmarkDB.testCollection**    | 1–4 ms           | 0–2 ms          | 0–2 ms           | Main insert/query benchmark activity. |
| **config.system_sessions_bench**  | 1–5 ms           | 0–2 ms          | 0–2 ms           | Session handling benchmark. |
| **config.transactions_bench**     | 1–4 ms           | 0–2 ms          | 0–2 ms           | Transaction handling benchmark. |
| **local.system_replset_bench**    | 1–4 ms           | 0–2 ms          | 0–2 ms           | Local replica set performance test. |
| **test.admin_system_version_test**| 1–4 ms           | 0–1 ms          | 0–1 ms           | Versioning metadata check. |
| **test.atlascli**                 | 1–4 ms           | 0–1 ms          | 0–2 ms           | CLI/system background workload in test DB. |
| **test.system_sessions_bench**    | 1–3 ms           | 0–1 ms          | 0–2 ms           | Session simulation in test namespace. |
| **admin.system.version**          | 0 ms             | 0 ms            | 0 ms             | Always inactive/instantaneous response. |


### Highlights from Azure ubuntu Arm64 Benchmarking

When comparing the results on Arm64 vs x86_64 virtual machines:

- **Most active namespaces:** `admin.atlascli`, `benchmarkDB.testCollection`, `benchmarkDB.cursorTest`, and `test.atlascli` — total times **2–6 ms**.  
- **Read patterns:** Reads across collections remain **0–2 ms**, showing consistently low-latency performance on Arm64.  
- **Write patterns:** Writes are mostly **1–3 ms**, indicating stable and balanced write performance.  
- **System-related namespaces:** `config.system_sessions_bench` and `config.transactions_bench` — total times **2–6 ms**, showing manageable system and transaction activity.  
- **Idle collections:** `admin.system.version` remains at **0 ms**, confirming minimal or no activity.  
- **Overall observation:** MongoDB operations on Arm64 are lightweight with **predictable, low-latency reads and writes**, confirming efficient performance on Azure Ubuntu Pro 24.04 LTS Arm64 Virtual machines. 
