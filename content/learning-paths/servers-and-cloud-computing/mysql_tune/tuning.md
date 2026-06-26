---
# User change
title: Tune MySQL configuration for performance
description: Learn how to tune MySQL server parameters for connections, memory, disk flushing, transaction durability, I/O capacity, and lock polling.

weight: 4 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## Update MySQL parameters

You can set MySQL server configuration parameters in an option file or on the `mysqld` command line.

For persistent tuning, use an option file so the configuration can be reviewed, version controlled, and applied consistently when MySQL restarts. For more information, see  [Specifying Program Options](https://dev.mysql.com/doc/refman/en/program-options.html) in MySQL documentation.

The examples in this section are intended for the `[mysqld]` group in a MySQL option file.

{{% notice Note %}}
In general, leave most MySQL settings at their defaults and change them only when you have a workload requirement, test result, profile, or observed bottleneck that supports the change.
{{% /notice %}}

### Connections and prepared statements

The following example shows intentionally high limits that can be useful in benchmark environments where you want to prevent connection or prepared statement limits from affecting the test result:

```ini
# Intentionally high benchmark limits.
max_connections=100000
max_prepared_stmt_count=4194304
```

The [`max_connections`](https://dev.mysql.com/doc/refman/en/server-system-variables.html#sysvar_max_connections) parameter doesn't directly improve performance. It raises the number of client connections MySQL can accept. Higher values consume more memory and can also depend on operating system limits such as file descriptors, so size this value for your expected peak connection count.

The [`max_prepared_stmt_count`](https://dev.mysql.com/doc/refman/en/server-system-variables.html#sysvar_max_prepared_stmt_count) parameter limits the total number of prepared statements across the server. The default protects the server from excessive memory use. Increase this value only when a benchmark or application needs more prepared statements, and avoid carrying an oversized value into production without measuring memory impact.

### Dedicated server configuration

If the system runs only MySQL, enable the dedicated server setting:

```ini
innodb_dedicated_server=ON
```

The [`innodb_dedicated_server`](https://dev.mysql.com/doc/refman/en/innodb-parameters.html#sysvar_innodb_dedicated_server) parameter automatically sizes selected InnoDB settings for a server dedicated to MySQL. Check the [MySQL dedicated server documentation](https://dev.mysql.com/doc/refman/en/innodb-dedicated-server.html) for the MySQL version you deploy because the behavior can change between releases.

In MySQL 8.4+, `innodb_dedicated_server` automatically configures `innodb_buffer_pool_size` and `innodb_redo_log_capacity`. On systems with more than `4 GiB` of RAM, `innodb_buffer_pool_size` is set to `75%` of detected system memory.

The auto-sized values are a useful starting point, but you can still override individual settings when workload requirements or performance data justify the change.

### Buffer pool size

The [`innodb_buffer_pool_size`](https://dev.mysql.com/doc/refman/en/innodb-parameters.html#sysvar_innodb_buffer_pool_size) parameter is one of the most important MySQL performance settings. It controls how much memory InnoDB can use to cache indexes and table data.

If MySQL runs on a dedicated server, `innodb_dedicated_server=ON` can be enough to size the buffer pool. If you don't use `innodb_dedicated_server`, or you want to test a specific value, set `innodb_buffer_pool_size` based on your workload and available memory:

```ini
# Example value for a dedicated 128 GiB test system.
innodb_buffer_pool_size=96G
```

The [MySQL InnoDB buffer pool documentation](https://dev.mysql.com/doc/refman/en/innodb-buffer-pool.html) suggests setting the buffer pool size to as much as `80%` of system memory on a dedicated database server. Leave memory for the operating system, connections, background MySQL memory use, and any other processes on the system.

Confirm the current buffer pool size:

```sql
SHOW VARIABLES LIKE 'innodb_buffer_pool_size';
```

{{% notice Note %}}
The `innodb_buffer_pool_size` value is shown in bytes. Use the value reported by MySQL when calculating huge page allocation.
{{% /notice %}}

### Buffer pool instances

For large buffer pools, multiple buffer pool instances can improve concurrency by reducing contention as different threads read and write cached pages.

```ini
# Example value for a large buffer pool.
innodb_buffer_pool_instances=8
```

The [`innodb_buffer_pool_instances`](https://dev.mysql.com/doc/refman/en/innodb-parameters.html#sysvar_innodb_buffer_pool_instances) setting takes effect only when `innodb_buffer_pool_size` is at least `1 GiB`. The total buffer pool is divided across the instances, so keep each instance at least `1 GiB`. Test values such as `4`, `8`, or `16` with your workload, and avoid creating so many instances that each one becomes too small.

### Redo log capacity

For write-heavy workloads, you can keep `innodb_dedicated_server=ON` and explicitly set a larger redo log capacity than the value MySQL calculates automatically:

```ini
innodb_dedicated_server=ON
# Example override for write-heavy workloads.
innodb_redo_log_capacity=32G
```

The [`innodb_redo_log_capacity`](https://dev.mysql.com/doc/refman/en/innodb-parameters.html#sysvar_innodb_redo_log_capacity) parameter controls the amount of disk space used for redo log files. It was introduced in MySQL `8.0.30`. In earlier MySQL versions, [`innodb_log_file_size`](https://dev.mysql.com/doc/refman/8.0/en/innodb-parameters.html#sysvar_innodb_log_file_size) and [`innodb_log_files_in_group`](https://dev.mysql.com/doc/refman/8.0/en/innodb-parameters.html#sysvar_innodb_log_files_in_group) control redo log size and behavior.

The auto-sized `innodb_redo_log_capacity` value is a starting point. Increasing it can improve write-heavy workloads by giving InnoDB more redo log space before checkpoints limit write throughput. An explicit `innodb_redo_log_capacity` value overrides the value calculated by `innodb_dedicated_server` for that variable, while still allowing `innodb_dedicated_server` to size other settings such as `innodb_buffer_pool_size`. When you override one of the automatically configured variables, MySQL prints a startup warning such as `Option innodb_dedicated_server is ignored for innodb_redo_log_capacity`. That warning is expected for the overridden variable.

Larger redo logs use more disk space and can increase crash recovery time, so test values against both performance and operational requirements.

### Huge pages

Enable large page support in the MySQL configuration:

```ini
large-pages=ON
```

Turning on [`large-pages`](https://dev.mysql.com/doc/refman/en/server-system-variables.html#sysvar_large_pages) can improve performance when MySQL uses a large InnoDB buffer pool. Larger pages map more memory per translation entry, which can reduce page-table walks and TLB pressure.

Huge pages must also be configured at the Linux kernel level. For huge page setup instructions, see the [system, kernel, compiler, and library settings](/learning-paths/servers-and-cloud-computing/mysql_tune/kernel_comp_lib/) section of this Learning Path.

Divide the buffer pool size by the huge page size to estimate the number of huge pages needed. Use the `Hugepagesize` value from `/proc/meminfo`, and allocate enough huge pages for a total huge page space equal to or slightly larger than the buffer pool.

{{% notice Important %}}
After restarting MySQL with `large-pages=ON`, check `/proc/meminfo` and the MySQL error log. If the huge page pool is too small, or MySQL can't allocate huge pages for another reason, InnoDB can fall back to traditional memory and print `Warning: Using conventional memory pool.` to the MySQL error log. You might also see an allocation warning similar to `large_page_aligned_alloc mmap(... bytes) failed; errno 12`.
{{% /notice %}}

You don't usually need to change other memory parameters unless you observe a specific issue. One optional area to test is [InnoDB buffer pool prefetching](https://dev.mysql.com/doc/refman/en/innodb-performance-read_ahead.html). Lowering [`innodb_read_ahead_threshold`](https://dev.mysql.com/doc/refman/en/innodb-parameters.html#sysvar_innodb_read_ahead_threshold) from the default can help workloads with predictable sequential access patterns, while [`innodb_random_read_ahead`](https://dev.mysql.com/doc/refman/en/innodb-parameters.html#sysvar_innodb_random_read_ahead) can help some workloads and hurt others. Treat these settings as workload-specific experiments.

### Disk flush behavior

For MySQL versions earlier than 8.4, test `innodb_use_fdatasync`:

```ini
innodb_use_fdatasync=ON
```

The [`innodb_use_fdatasync`](https://dev.mysql.com/doc/refman/en/innodb-parameters.html#sysvar_innodb_use_fdatasync) parameter allows InnoDB to use `fdatasync()` instead of `fsync()` for operating systems and flush methods that support it. This can improve write performance because `fdatasync()` flushes file data without forcing unrelated metadata updates, such as timestamps to disk. Metadata required to retrieve the data is still flushed. In MySQL 8.4, this setting defaults to `ON`.

### Transaction durability settings

Use the following settings when transaction durability and consistency are required (these are the default in MySQL 8.4+):

```ini
sync_binlog=1
innodb_flush_log_at_trx_commit=1
```

The [`sync_binlog`](https://dev.mysql.com/doc/refman/en/replication-options-binary-log.html#sysvar_sync_binlog) parameter controls how often MySQL synchronizes the binary log to disk. The [`innodb_flush_log_at_trx_commit`](https://dev.mysql.com/doc/refman/en/innodb-parameters.html#sysvar_innodb_flush_log_at_trx_commit) parameter controls how InnoDB writes and flushes redo log records at transaction commit.

When both settings are `1`, MySQL prioritizes transaction durability over peak write throughput. Relaxing either setting can reduce how often transactions wait for binary log and redo log data to be flushed to durable storage. This can improve parallel transaction execution and write throughput, especially on write-heavy workloads, but it increases the time window where committed transactions exist only in memory or operating system cache.

{{% notice Warning %}}
Changing `sync_binlog` or `innodb_flush_log_at_trx_commit` away from `1` trades away transaction durability, which is part of ACID compliance. Values such as `sync_binlog=0`, `sync_binlog=N` where `N` is greater than `1`, or `innodb_flush_log_at_trx_commit=0` or `2` can lose committed transactions during a power failure, operating system crash, or unexpected MySQL exit. Change these settings only when your application and recovery process can tolerate potential transaction loss.
{{% /notice %}}

### I/O capacity configuration

Increasing parallelism can help InnoDB use available storage resources more efficiently. For older MySQL versions on SSD-backed or cloud storage, test values similar to the MySQL 8.4 defaults:

```ini
innodb_io_capacity=10000
innodb_io_capacity_max=20000
```

The [`innodb_io_capacity`](https://dev.mysql.com/doc/refman/en/innodb-parameters.html#sysvar_innodb_io_capacity) parameter tells InnoDB how many I/O operations per second it can issue to storage for background work. Before MySQL 8.4, the default was `200`, which is often too low for modern SSD and cloud storage. In MySQL 8.4, the default is `10000`.

The [`innodb_io_capacity_max`](https://dev.mysql.com/doc/refman/en/innodb-parameters.html#sysvar_innodb_io_capacity_max) parameter provides a higher limit for bursts of background work. It defaults to `2x` `innodb_io_capacity`. Use that relationship as a starting point, then adjust the values based on storage capability and measured performance.

### Spin lock configuration

Use the following setting as a starting point for testing lock polling behavior:

```ini
innodb_sync_spin_loops=30
```

The [`innodb_sync_spin_loops`](https://dev.mysql.com/doc/refman/en/innodb-parameters.html#sysvar_innodb_sync_spin_loops) parameter controls how many times a thread checks whether an InnoDB mutex is free before yielding execution to another thread.

Profiling MySQL under heavy load on Arm with Linux `perf` can show time spent waiting for locks. Increasing `innodb_sync_spin_loops` can reduce context switching when locks are released quickly, but setting it too high can waste power and delay other useful work. Keep the default value, `30`, unless profiling and measured performance show that a different value helps. For more information, see the MySQL [Configuring Spin Lock Polling documentation](https://dev.mysql.com/doc/refman/en/innodb-performance-spin_lock_polling.html).

## What you've learned

You've now explored various MySQL parameters you can tune for improved performance on Arm. 

You can use the guidance in this Learning Path to optimize the performance of your MySQL databases. 
