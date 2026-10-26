---
title: Tune PostgreSQL configuration for performance
description: Learn how to tune PostgreSQL parameters for connections, memory, write-ahead logging, query planning, I/O, and parallel execution.

weight: 4
layout: "learningpathall"
---

## Choose PostgreSQL parameters for tuning

You can set PostgreSQL parameters in `postgresql.conf`, with `ALTER SYSTEM`, or for a database, role, or session when the parameter supports that scope. For persistent tuning, use a configuration method that can be reviewed, version controlled, and applied consistently when PostgreSQL restarts. See the PostgreSQL [configuration settings documentation](https://www.postgresql.org/docs/current/config-setting.html) for details.

{{% notice Note %}}
Leave most PostgreSQL settings at their defaults and change them only when a workload requirement, test result, profile, or observed bottleneck supports the change.
{{% /notice %}}

### Connections

The [`max_connections`](https://www.postgresql.org/docs/current/runtime-config-connection.html#GUC-MAX-CONNECTIONS) parameter sets the maximum number of concurrent connections PostgreSQL accepts. It does not directly improve query performance.

```ini
# Example high connection limit. Size this for your expected peak connection count.
max_connections = 1000
```

Each PostgreSQL connection uses memory and operating system resources. Size this value for expected peak demand, and review the kernel resource limits when you increase it. When an application needs many client connections, use a connection pooler such as [PgBouncer](https://www.pgbouncer.org/) to reuse a smaller number of PostgreSQL server connections. This can reduce memory use and process overhead, but it does not make individual queries faster.

### Memory configuration

#### Shared buffers

The [`shared_buffers`](https://www.postgresql.org/docs/current/runtime-config-resource.html#GUC-SHARED-BUFFERS) parameter controls the shared memory cache that PostgreSQL uses for table and index data.

For a dedicated database server with at least `1 GB` of memory, set `shared_buffers` to `25%` to `40%` of system memory as a starting range. PostgreSQL also relies on the operating system page cache, so values above `40%` are unlikely to help. Larger `shared_buffers` settings often need a corresponding increase in `max_wal_size`.

```ini
# Example for a dedicated server with 128 GiB of memory.
shared_buffers = 32GB
```

#### Query and maintenance memory

The [`work_mem`](https://www.postgresql.org/docs/current/runtime-config-resource.html#GUC-WORK-MEM) parameter is the base memory limit for each sort or hash operation before PostgreSQL writes temporary files. A single complex query can use multiple operations, and many sessions can run them concurrently. Treat increases as a measured change, not a global performance setting.

```ini
# Example values. Test with realistic query concurrency.
work_mem = 32MB
maintenance_work_mem = 2GB
```

The [`maintenance_work_mem`](https://www.postgresql.org/docs/current/runtime-config-resource.html#GUC-MAINTENANCE-WORK-MEM) parameter controls memory for maintenance operations such as `VACUUM` and `CREATE INDEX`. A larger value can improve maintenance performance, especially for databases with frequent updates or deletes, but account for concurrent autovacuum workers. Set [`autovacuum_work_mem`](https://www.postgresql.org/docs/current/runtime-config-resource.html#GUC-AUTOVACUUM-WORK-MEM) separately if you need to limit each worker.

#### Huge pages

The [`huge_pages`](https://www.postgresql.org/docs/current/runtime-config-resource.html#GUC-HUGE-PAGES) setting requests huge pages for PostgreSQL shared memory. The default value, `try`, falls back to regular pages if allocation fails. Set it to `on` when you want PostgreSQL to fail at startup instead of using regular pages.

```ini
huge_pages = on
```

Huge pages must also be configured at the Linux kernel level. For setup instructions and sizing guidance, see the [system, kernel, compiler, and library settings](/learning-paths/servers-and-cloud-computing/postgresql_tune/kernel_comp_lib/) section of this Learning Path.

### Write-ahead log and durability configuration

PostgreSQL uses the write-ahead log (WAL) to protect committed data and support crash recovery. The following settings affect checkpoint behavior and transaction durability.

#### Checkpoint and WAL capacity

The [`max_wal_size`](https://www.postgresql.org/docs/current/runtime-config-wal.html#GUC-MAX-WAL-SIZE) parameter is a soft limit on WAL size during automatic checkpoints. Increasing it can reduce checkpoint frequency and smooth write I/O for write-heavy workloads.

Under sustained high load, WAL can fill quickly enough to trigger frequent checkpoints and checkpoint warnings. Increasing `max_wal_size` gives PostgreSQL more WAL space before a checkpoint is required. The following value is an example, not a universal recommendation:

```ini
# Example for a write-heavy workload. Test against storage capacity and recovery requirements.
min_wal_size = 1GB
max_wal_size = 20GB
```

The [`min_wal_size`](https://www.postgresql.org/docs/current/runtime-config-wal.html#GUC-MIN-WAL-SIZE) parameter keeps a minimum amount of WAL available for recycling. Increasing it can help absorb bursts of WAL activity and reduce the need to create new WAL files during a spike.

Larger WAL settings use more storage and can increase crash recovery time. PostgreSQL logs a checkpoint warning when WAL-triggered checkpoints occur more often than `checkpoint_warning`, which can indicate that `max_wal_size` is too small for the workload.

#### Transaction durability settings

Use the following setting when transaction durability is required. It is the PostgreSQL default:

```ini
# Keep the default when transaction durability is required.
synchronous_commit = on
```

The [`synchronous_commit`](https://www.postgresql.org/docs/current/runtime-config-wal.html#GUC-SYNCHRONOUS-COMMIT) parameter controls whether PostgreSQL waits for WAL records to reach durable storage before reporting commit success to the client.

When `synchronous_commit` is `on`, PostgreSQL prioritizes transaction durability over peak write throughput. Setting `synchronous_commit=off` lets PostgreSQL acknowledge commits before the WAL data is flushed to durable storage. This can improve parallel transaction execution and write throughput, especially for write-heavy workloads, but it increases the time window where acknowledged transactions exist only in memory or operating system cache.

{{% notice Warning %}}
Changing `synchronous_commit` to `off` trades away transaction durability, which is part of ACID compliance. A power failure, operating system crash, or unexpected PostgreSQL exit can lose recently acknowledged transactions, though this setting does not cause database corruption.

Change this setting only when your application and recovery process can tolerate potential transaction loss.
{{% /notice %}}

### Query planner configuration

The PostgreSQL query planner selects an execution plan using table and index statistics, along with cost estimates for operations such as sequential scans and index scans. Use `EXPLAIN` and `EXPLAIN ANALYZE` with representative queries to understand a plan before changing planner-related settings.

#### Effective cache size

The [`effective_cache_size`](https://www.postgresql.org/docs/current/runtime-config-query.html#GUC-EFFECTIVE-CACHE-SIZE) parameter tells the planner how much memory it can expect to be available for caching PostgreSQL data. Set it to an estimate of the total cache available to PostgreSQL, including `shared_buffers` and the operating system page cache. It does not allocate memory or reserve page cache.

For a dedicated PostgreSQL server, `80%` of total memory is a useful starting estimate. Use `free` while PostgreSQL is running to understand page-cache use, then refine the value for the memory available to PostgreSQL and the expected number of concurrent queries.

When the page cache is large, data that misses `shared_buffers` is more likely to be read from memory instead of storage. A larger `effective_cache_size` makes index scans look less expensive to the planner, while a smaller value makes sequential scans more likely. This can help the planner choose an index scan when the index is likely to be cached, rather than assuming the access requires a slow storage read.

#### Random page cost

The [`random_page_cost`](https://www.postgresql.org/docs/current/runtime-config-query.html#GUC-RANDOM-PAGE-COST) parameter estimates the relative cost of a non-sequential page read. The default is `4.0`. Lowering it relative to `seq_page_cost` makes index scans more likely; raising it makes them less likely.

The default can be a better fit for storage with a high random-read penalty, such as hard disks. On SSD-backed systems, or when a large part of the database is likely to be cached, a lower value such as `1.1` can be worth testing. Storage latency, cache behavior, and network latency all affect the right value, so compare the resulting plans and execution times with representative queries instead of applying a fixed value to every system.

`random_page_cost` and `effective_cache_size` both influence how the planner values index scans, but from different directions. `effective_cache_size` estimates how likely the data is to be cached. `random_page_cost` estimates the penalty when PostgreSQL has to access a page that is not already in cache.

### Parallel execution and I/O configuration

PostgreSQL uses worker processes for parallel queries, maintenance, and extensions. The [`max_worker_processes`](https://www.postgresql.org/docs/current/runtime-config-resource.html#GUC-MAX-WORKER-PROCESSES) setting is the overall limit. The [`max_parallel_workers`](https://www.postgresql.org/docs/current/runtime-config-resource.html#GUC-MAX-PARALLEL-WORKERS) setting limits workers available to parallel operations, and must not exceed `max_worker_processes`.

Set `max_worker_processes` and `max_parallel_workers` high enough to allow useful parallel work, but leave CPU capacity for connection handling, background processes, and other applications. A starting point for a dedicated test system is the number of available logical CPUs. PostgreSQL can launch fewer workers than the configured limits when capacity is unavailable.

Use [`max_parallel_workers_per_gather`](https://www.postgresql.org/docs/current/runtime-config-query.html#GUC-MAX-PARALLEL-WORKERS-PER-GATHER) and [`max_parallel_maintenance_workers`](https://www.postgresql.org/docs/current/runtime-config-resource.html#GUC-MAX-PARALLEL-MAINTENANCE-WORKERS) to limit workers used by an individual query or maintenance operation. A value of `4` is a reasonable test starting point for each on a sufficiently large system. Increase the values only when suitable queries or maintenance operations have unused CPU capacity. More workers can increase coordination overhead or reduce performance when CPU, memory bandwidth, or storage is already saturated.

The [`effective_io_concurrency`](https://www.postgresql.org/docs/current/runtime-config-resource.html#GUC-EFFECTIVE-IO-CONCURRENCY) parameter controls how many storage I/O operations a PostgreSQL session expects to issue in parallel. A value in the low hundreds, such as `300`, can be a useful starting point for high-IOPS SSD or cloud storage. Higher values can help high-latency storage with enough I/O capacity, but unnecessarily high values can increase I/O latency. Its default has changed across PostgreSQL versions, so check the value on the version you deploy before overriding it.

## What you've learned

You've explored PostgreSQL parameters that affect connection handling, memory use, WAL behavior, query planning, and parallel execution.

Use the guidance in this Learning Path to design measured tuning experiments for your PostgreSQL workload on Arm.

Next, use the HammerDB TPROC-C workflow to measure the effect of your tuning changes.
