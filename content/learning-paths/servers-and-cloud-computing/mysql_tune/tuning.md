---
# User change
title: "Tuning MySQL"

weight: 4 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

##  MySQL configuration

There are different ways to set configuration parameters for `MySQL`. 

This is discussed in the [MySQL Programs documentation](https://dev.mysql.com/doc/refman/8.0/en/programs.html). 

The configurations below can be directly pasted into a `MySQL` configuration file under the group `mysqld`. 

It's also possible to specify these configurations on the `mysqld` command line (typically within a linux service file). 

To display configuration settings:
```bash { pre_cmd="sudo apt install -y mysql-server" }
mysqld --verbose --help
```

### Connections and prepared transactions

```output
max_connections=100000    # Default 151
max_prepared_stmt_count=4194304   # Default 16382
```

`max_connections` doesn't impact performance, but if a high client connection count is expected or required, it's a good idea to raise this in order to not reject request from clients. 

Keep in mind that more client connections means more resources will be consumed (especially memory). Setting this to something higher is completely dependent on use case and requirements.

`max_prepared_stmt_count` is 16382 by default. It's a good idea to set this as small as possible in order to help prevent denial of service attacks. You can make it very large in a test environment that uses many prepared statements.

### Memory related configuration

```output
large_pages=ON    # default is OFF
innodb_buffer_pool_size=<up to 80% of system memory>    # Default is 128MB
```

Turning on `large_pages` can result in significant performance gains. 

Using larger pages helps to reduce how often physical memory has to get mapped to virtual memory. Note that huge pages needs to be [turned on at the kernel level](/learning-paths/servers-and-cloud-computing/mysql_tune/kernel_comp_lib) for this to work.

`innodb_buffer_pool_size` is one of the most important configuration parameters that can be set. It determines how much memory can be used to store indexes and table data. It's a cache that improves read/write latency and relieves pressure on storage. The [MySQL documentation](https://dev.mysql.com/doc/refman/8.0/en/innodb-buffer-pool.html) suggests this be set to up to 80% of total system memory. Setting this value significantly larger than the default of 128MB is a good idea.

Other memory related configurations that could be worth exploring are the [Buffer Pool Prefetching](https://dev.mysql.com/doc/refman/8.0/en/innodb-performance-read_ahead.html) configurations. You may see modest performance gains by decreasing the `innodb_read_ahead_threshold` from the default. The default is very conservative and will result in very little to no prefetching. Some workloads may benefit from being less conservative with prefetching. Turning on random prefetch (`innodb_random_read_ahead`) seems to hurt performance but could benefit some user cases.

### Logging and disk flush behavior

```output
innodb_use_fdatasync=ON    # Default is OFF
innodb_log_file_size=20GB    # Default is 48MB
```

Setting `innodb_use_fdatasync` to ON helps reduce the number of system calls that occur when flushing data to disk. Using `fdatasync` reduces flushing by not updating the meta data associated with files when those files are written to. For most use cases, this is acceptable.

Setting `innodb_log_file_size` to much larger than the default (48MB) helps reduce how much flushing and check pointing occurs. See the [MySQL documentation](https://dev.mysql.com/doc/refman/8.0/en/innodb-parameters.html#sysvar_innodb_log_file_size) for more information. Also note, there is another parameter called `innodb_log_buffer_size` that may be worth experimenting with as well. [Documentation](https://dev.mysql.com/doc/refman/8.0/en/innodb-parameters.html#sysvar_innodb_log_buffer_size) on this parameter is also available. 

### Concurrency configuration

Increasing parallelism uses available resources more efficiently. It's always a good idea to look at parameters related to parallel execution.

```output
innodb_io_capacity=1000    # Default is 200
innodb_io_capacity_max=2000    # Default is 2x innodb_io_capacity
innodb_read_io_threads=<system CPU count>    # Default is 4
innodb_write_io_threads=<system CPU count>    # Default is 4
```

`innodb_io_capacity` tells the `InnoDB` storage engine how many IOPS it can issue to storage. The default of 200 is quite low and more appropriate for rotational storage. Modern SSD storage and even cloud based storage can benefit greatly from increasing this value. The [MySQL InnoDB I/O Capacity documentation](https://dev.mysql.com/doc/refman/8.1/en/innodb-configuring-io-capacity.html) suggests this be set to around 1000 for higher performing storage. In some cases, it might be worth setting this higher than 1000.

`innodb_io_capacity_max` defaults to 2x of `innodb_io_capacity`. It is worth experimenting with this value in use cases that experience heavy disk usage.

`innodb_read_io_threads` and `innodb_write_io_threads` sets the number of threads used for IO disk operations. Setting this to the number of CPUs in the system can provide performance benefits. Experiment with these parameters since a value that is smaller then the total number of CPUs in the system may be sufficient.

### Spin lock configuration

```output
innodb_sync_spin_loops=120    # Default is 30
```

You should experiment with the `innodb_sync_spin_loops` parameter. This sets the number of times a thread checks for an `InnoDB` lock to be free before yielding execution to another thread. 

Profiling `MySQL` under heavy load with Linux `perf` shows that `MySQL` spends a lot of time waiting for locks to be freed. Experimenting with tuning parameters around locks might help. Increasing the number of times a lock is checked before the thread yields can reduce context switching. This reduction in context switching tends to increase performance. Start with a value of 120 for `innodb_sync_spin_loops`, but you can also try values such as 30, 60, 180, and 240.