---
# User change
title: "Tuning MySQL"

weight: 4 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

##  MySQL configuration

There are different ways to set configuration parameters for `MySQL`. 

This is discussed in the [Specifying Program Options](https://dev.mysql.com/doc/refman/en/program-options.html) section of the MySQL documentation. 

The configurations below can be directly pasted into a `MySQL` configuration file under the group `mysqld`. 

It's also possible to specify these configurations on the `mysqld` command line. However, it's better to use configuration files since these can be version controlled more easily.

Last, keep in mind, that in general, it's usually best to leave most configs at default, and only change them if there is a suspected/known issue.

### Connections and prepared transactions

```
max_connections=100000    # Default 151
max_prepared_stmt_count=4194304   # Default 16382
```

`max_connections` doesn't impact performance, but if a high connection count is expected or required, this should be raised in order to not reject requests from clients. 

Keep in mind that more connections means more resources will be consumed, especially memory. Setting this to something higher is completely dependent on use case and requirements.

`max_prepared_stmt_count` is 16382 by default. It's a good idea to set this as small as possible in order to help prevent denial of service attacks. You can make it very large in a test environment that uses many prepared statements.

### Dedicated Server Configuration
```
innodb_dedicated_server=ON
```
If the node will only run `MySQL` and no other application. One of the easiest ways to gain performance is by setting `innodb_dedicated_server=ON`. This setting does different things depending on the version of `MySQL`, so it's important to check the [documentation](https://dev.mysql.com/doc/refman/en/innodb-dedicated-server.html) for the specific version of `MySQL` being deployed. As of version 8.4, this setting will automatically set both `innodb_buffer_pool_size` and `innodb_redo_log_capacity`. Two configurations that impact performance.

On systems with a large amount of RAM (greater than 4GB), the `innodb_buffer_pool_size` will be set to 75% total system memory. `innodb_buffer_pool_size` is one of the most important configuration parameters that can be set. It determines how much memory can be used to store indexes and table data. It's a cache that improves read/write latency by relieving pressure on storage. If `innodb_dedicated_server` is not used, then this parameter should be set. The [MySQL documentation](https://dev.mysql.com/doc/refman/en/innodb-buffer-pool.html) suggests this be set to up to 80% of total system memory. The default of 128MiB is probably going to be far less than 80% of total system memory.

`innodb_redo_log_capacity` was introduced in MySQL 8.0.30. It controls the amount of disk space used for redo log files. In earlier versions of `MySQL`, the parameters `innodb_log_file_size` and `innodb_log_files_in_group` influence redo log size and behavior. `innodb_redo_log_capacity` simplifies things. When `innodb_dedicated_server` is enabled, `innodb_redo_log_capacity` is set to (number of available logical processors / 2)GB with a max of 16GB. If `innodb_dedicated_server` is not used, then `innodb_redo_log_capacity` should be set. If the redo log is too small, the status variable [`Innodb_log_waits`](https://dev.mysql.com/doc/refman/en/server-status-variables.html#statvar_Innodb_log_waits) will be large. This indicates that the redo log buffer is waiting for the log to be flushed to storage before continuing. Ideally, this status variable is 0 at all times.

### Huge Pages

```
large_pages=ON    # default is OFF
```

Turning on `large_pages` can result in significant performance gains. 

Using larger pages helps to reduce how often physical memory has to get mapped to virtual memory. Note that huge pages needs to be [turned on at the kernel level](/learning-paths/servers-and-cloud-computing/mysql_tune/kernel_comp_lib) for this to work.

If `innodb_dedicated_server` is set to `ON`, then `innodb_buffer_pool_size` will automatically be set. The value of `innodb_buffer_pool_size` is needed to calculate how many huge pages will need to be allocated. The value of `innodb_buffer_pool_size` can be confirmed by checking the variable in the `mysql` cli.

```sql
SHOW VARIABLES LIKE 'innodb_buffer_pool_size';
```

> NOTE: The innodb_buffer_pool_size unit is bytes.
> There is no need to confirm the value of `innodb_buffer_pool_size` if it is set manually (i.e. you are not using `innodb_dedicated_server=ON`).
> Alternatively, you can estimate the value of `innodb_buffer_pool_size` since the calculation when `innodb_dedicated_server=ON` is in the documentation. Use the command "`free --bytes`" to get the total system memory in bytes.

Divide this number by the huge page size (convert to bytes first) to get the number of huge pages that should be allocated. Instructions on how to get the huge page size and to set the number of pages is in the [System, Kernel, Compiler, and Libraries](/learning-paths/servers-and-cloud-computing/mysql_tune/kernel_comp_lib) section.

In general, there's no need to adjust other memory parameters unless an issue is suspected/found. That said, other memory related configurations that could be worth exploring are the [Buffer Pool Prefetching](https://dev.mysql.com/doc/refman/en/innodb-performance-read_ahead.html) configurations (take this as an FYI). You may see modest performance gains by decreasing the `innodb_read_ahead_threshold` from the default. The default is very conservative and will result in very little to no prefetching. Some workloads may benefit from being less conservative with prefetching. Turning on random prefetch (`innodb_random_read_ahead`) seems to hurt performance but could benefit some user cases. The affects of these settings will be use case dependent.

### Disk flush behavior

```
innodb_use_fdatasync=ON    # Default is OFF prior to MySQL 8.4
```

Setting `innodb_use_fdatasync` to ON helps reduce the number of system calls that occur when flushing data to disk. Using `fdatasync` reduces flushing by not updating the meta data associated with files when those files are written to. For most use cases, this is acceptable. As of MySQL 8.4, this is now set to `ON` by default. If running an older version of `MySQL`, it is generally recommended to set this to `ON`. In fact, this is why it has been defaulted to `ON` in newer version of `MySQL`.

### Concurrency configuration

Increasing parallelism uses available resources more efficiently. It's always a good idea to look at parameters related to parallel execution.

```
innodb_io_capacity=10000    # Default is 200 prior to MySQL 8.4 and 10000 from 8.4
innodb_io_capacity_max=20000    # Default is 2x innodb_io_capacity
```

`innodb_io_capacity` tells the `InnoDB` storage engine how many IOPS it can issue to storage. Prior to `MySQL` 8.4, the default was 200 which is very low and more appropriate for rotational storage. Modern SSD storage and even cloud based storage can benefit greatly from increasing this value. As of `MySQL` 8.4, the default value has been increased to 10000. If you are using an older version of `MySQL` where this is defaulted to 200, it might benefit you to set this to 10000. See the [MySQL InnoDB I/O Capacity documentation](https://dev.mysql.com/doc/refman/en/innodb-configuring-io-capacity.html) for more.

`innodb_io_capacity_max` defaults to 2x of `innodb_io_capacity`. This should be ok for most use cases.

### Spin lock configuration

```
innodb_sync_spin_loops=120    # Default is 30
```

You should experiment with the `innodb_sync_spin_loops` parameter. This sets the number of times a thread checks for an `InnoDB` lock to be free before yielding execution to another thread. 

Profiling `MySQL` under heavy load on Arm with Linux `perf` shows that `MySQL` spends a lot of time waiting for locks to be freed. Experimenting with tuning parameters around locks might help. Increasing the number of times a lock is checked before the thread yields can reduce context switching. This reduction in context switching tends to increase performance. Start with a value of 120 for `innodb_sync_spin_loops`, but you can also try values such as 30, 60, 180, and 240. See the [Configuring Spin Lock Polling](https://dev.mysql.com/doc/refman/en/innodb-performance-spin_lock_polling.html) for more.