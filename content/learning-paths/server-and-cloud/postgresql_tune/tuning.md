---
# User change
title: "Tuning PostgreSQL"

weight: 3 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

In this section we will discuss PostgreSQL tuning parameters.

##  Why Application Performance Tuning is Important

Application tuning allows us to gain performance without scaling our deployment up or out. This also gives us the option to either use the gained performance, or to trade it for cost savings by reducing the total amount of compute resources provisioned. Below is a graph that shows how big of a difference performance tuning on PostgreSQL can make.

![Before and after Tuning](BeforeAndAfter.png)

##  A Note on Tuning

Keep in mind that deployment configurations and the profile of SQL requests that are made by clients will be different. This means there is not a one size fits all set of tuning parameters for PostgreSQL.  Use the below to get some ideas around how PostgreSQL can be tuned.

##  Storage Technology & File System Format

The underlying storage technology and the file system format can impact performance significantly. In general, locally attached SSD storage will perform best. However, network based storage systems can perform very well too. As always, performance is dependent on the request profile coming from clients. We suggest that the reader spends some time studying and experimenting with different storage technologies and configuration options.

Aside from the storage technology, it is also worth testing different file system formats with PostgreSQL. We've found that xfs is a good starting point (ext4 is probably fine too).

##  Kernel Configurations

PostgreSQL can benefit from adjustments to kernel parameters. Below is a list of some kernel related settings that can have a positive impact on performance.

### Linux-PAM Limits

Linux-PAM limits can be changed in the ```/etc/security/limits.conf``` file, or by using the `ulimit` command. We leave it up to the reader to learn how to edit the `limits.conf` file or use the `ulimit` command. An explanation on why these Linux-PAM settings can help performance is found in the [PostgreSQL documentation](https://www.postgresql.org/docs/current/kernel-resources.html).

```

nofile (ulimit -n):  Max number of open file descriptors
nproc (ulimit -u):   Max number of processes
data (ulimit -d):    Max data segment size
memlock (ulimit -l): Max locked-in-memory address space
```

### Linux Virtual Memory Subsystem

Making changes to the Linux Virtual Memory subsystem can also help performance. These settings can be changed in the `/etc/sysctl.conf` file, or by using the `sysctl` command. We leave it up to the reader to learn how to edit the `sysctl.conf` file or use the `sysctl` command. Documentation on each of these parameters can be found in the [admin-guide for sysctl in the Linux source](https://github.com/torvalds/linux/blob/master/Documentation/admin-guide/sysctl/vm.rst).

### vm.overcommit_memory

```

vm.overcommit_memory
```

This setting is recommended to be set to 2 in the [PostgreSQL documentation](https://www.postgresql.org/docs/15/kernel-resources.html). This tells Linux to never over commit memory (see admin-guide linked above). The reason we set this to 2 is to avoid a situation where the kernel might terminate the PostgreSQL postmaster when memory is scarce.

### vm.nr_hugepages

PostgreSQL benefits from using huge memory pages. This is because huge pages reduces how often virtual memory pages are mapped to physical memory. Before we look at this parameter, we'd like to show the reader how the current huge page configuration can be checked on any host. Run the following command on the host:

```

cat /proc/meminfo | grep ^Huge
```

The output should look something like the below:

```

HugePages_Total:       0
HugePages_Free:        0
HugePages_Rsvd:        0
HugePages_Surp:        0
Hugepagesize:       2048 kB
Hugetlb:               0 kB
```

This tells us we are not using huge pages because `HugePages_Total` is set to 0 (this is the default). Also take note of what `Hugepagesize` is set to; in our case it's set to 2MB which is the typical default for huge pages on Linux. This huge page size can be adjusted along with other parameters not discuss here. We leave learning about those other parameters up to the reader.

The setting that enables huge pages is shown below:

```

vm.nr_hugepages
```

This parameter sets the number of huge pages we want the kernel to make available to applications. The total amount of memory that will be used for huge pages will be this number (defaulted to 0) times the `Hugepagesize` we saw earlier (2MiB in our case). As an example, if we want a total of 1GB of huge page space, then we should set `vm.nr_hugepages` to 500 (500x2MB=1GB).

*What should we set `vm.nr_hugepages` to for PostgreSQL?*

We should set `vm.nr_hugepages` to a value that gives us a total huge page space of slightly bigger than the PostgreSQL shared buffer size (discussed later). The reason we need to make it slightly larger than the shared buffer is because PostgreSQL will use additional memory for other things like connection management.

More information on the different parameters that affect the configuration of huge pages can be found in the [admin-guide for hugetlbpage in the Linux source](https://github.com/torvalds/linux/blob/master/Documentation/admin-guide/mm/hugetlbpage.rst).

### vm.dirty_ratio & vm.dirty_background_ratio

PostgreSQL writes data to files like the usual Linux process does. Thus, the behavior of the page cache can affect performance. These two parameters control how often the kernel flushes the page cache data to disk.

```

vm.dirty_background_ratio
```

```vm.dirty_background_ratio``` sets the percentage of the page cache that needs to be dirty in order for a flush to disk to start in the background. In our testing, we found that setting this value to lower than the default (typically 10) seems to help write heavy workloads. This is because by lowering this threshold, we are spreading writes to storage over time. This reduces the probability of saturating storage.

```

vm.dirty_ratio
```

```vm.dirty_ratio``` sets the percentage of the page cache that needs to be dirty in order for threads that are writing to storage to be paused to allow flushing to catch up. In our testing, we found that setting this value higher than default (typically 10-20) can help flush performance when disk writes are bursty. A higher value gives the background flusher (controlled by `vm.dirty_background_ratio`) more time to catch up. We've seen that setting this as high as 80 can help.

##  PostgreSQL Configuration

There are different ways to set configuration parameters for PostgreSQL. This is discussed in the [Setting Parameters documentation](https://www.postgresql.org/docs/current/config-setting.html). The configurations we show below can be directly copied and pasted into a PostgreSQL configuration file.

### Connections and Prepared Transactions

```

max_connections = 1000    # Default 100
max_prepared_transactions = 1000   # Default 0
```

`max_connections` doesn't impact performance, but if a high client connection count is expected/required, it's a good idea to raise this in order to not reject request from clients. Keep in mind that more client connections means more resources will be consumed (especially memory). Setting this to something higher is completely dependent on use case and requirements.

`max_prepared_transactions` is 0 by default. This means that stored procedures and functions cannot be used out of the box. It must be enabled by setting `max_prepared_transactions` to a value greater than 0. Using procedures and functions can greatly improve performance. We leave learning how to use stored procedures and functions with PostgreSQL as an exercise for the reader (there is plenty of information on this subject on the internet).

### Memory Related Configuration

```

huge_pages = on    # default is try
shared_buffers = <25%-40% system memory>    # Default is 128MB
work_mem = 32MB    # default is 4MB
maintenance_work_mem = 2GB    # Default is 64MB
```

Turning on `huge_pages` is not required because the default is `try`. However, we like to explicitly set it to `on` because errors will be produced if huge pages are not enabled in Linux for whatever reason (e.g. Maybe there is a bug in configuration automation that doesn't setup huge pages).

`shared_buffers` is one of the most important configuration parameters that can be set. It determines how much memory can be used to store indexes and table data. It's a cache that improves read/write latency and relieves pressure on storage. The [PostgreSQL documentation](https://www.postgresql.org/docs/15/runtime-config-resource.html) suggests this be set to 25% - 40% of total system memory. Our testing is in agreement with this recommendation.

`work_mem` is memory used when queries are being processed. We found that raising this significantly from default can help performance.

`maintenance_work_mem` is memory used for operations like VACUUM. In a scenario where data is removed often, raising this can help performance.

### Processing and Process Count

```

deadlock_timeout = 10s    # Default is 1s
max_worker_processes = <num_system_cpus>    # Default is 8
```

`deadlock_timeout` sets a polling interval for checking locks. The [documentation](https://www.postgresql.org/docs/15/runtime-config-locks.html) states that this check is expensive from a CPU cycles standpoint, and that the default of 1s is probably the smallest that should be used. Consider raising this timeout much higher to save some CPU cycles. 

`max_worker_processes` is a key parameter for performance. It's the number of total background processes allowed. We suggest setting it to the number of cores present on the PostgreSQL node. Generally speaking, a good starting point for thread/process count parameters is to use the number of cores on the system. That said, that is not always true, and thus, it's important to try some experimentation.

### Write Ahead Log (WAL) Configuration

```

synchronous_commit = off    # Default is on
max_wal_size = 20GB    # Default is 1GB
wal_recycle = off    # Default is on
```

If `synchronous_commit` is on (default), it tells the WAL processor to wait until more of the log is applied before reporting success to clients. Turning this off means that the PostgreSQL instance will report success to clients sooner. This will result in a performance improvement. It is safe to turn this off in most cases, but keep in mind that it will increase the risk of losing transactions if there is a crash. However, it will not increase the risk of data corruption.

In high load scenarios, check pointing can happen very often. In fact, in our testing with HammerDB, we saw so much check pointing that PostgreSQL reported warnings. One way to reduce how often check pointing occurs is to increase the `max_wal_size` of the WAL log. In our case, setting it to 20GB made the excessive check pointing warnings go away. 

`wal_recycle` didn't appear to affect performance for us. However, in scenarios where a large amount of data is being loaded (for example, restoring a database), turning this off will speed up the process and reduce the chances of replication errors to occur if streaming replication is used.

### Planner/Optimizer Configuration

The optimizer (A.K.A. planner) is responsible for taking statistics about the execution of previous queries, and using that information to figure out what is the fastest way to process new queries. Some of these statistics include shared buffer hit/miss rate, execution time of sequential scans, execution time of index scans, etc. Below are some parameters that affect the optimizer. 

```

effective_cache_size = <80% of system memory>    # Default is 4GB
random_page_cost = 1.1    # Default is 4.0
```
Let's discuss `effective_cache_size` first.

One key piece of information that a PostgreSQL instance will not have access to is the size of the OS page cache. `effective_cache_size` gives us a way to inform PostgreSQL of the page cache size. Assuming the host is dedicated to running PostgreSQL only, a good starting value is to set this to about 80% of total system memory. The value of this parameter should roughly be the shared buffer size and the OS page cache size combined. Use a tool like `free` while PostgreSQL is running to understand how much memory is being used for the OS page cache. This can help further refine the value from the suggested 80%. Also note that this parameter does not affect memory allocations.

How does `effective_cache_size` affect the optimizer and help performance?

When data is loaded into the PostgreSQL shared buffer, the same data may also be present in the page cache. It is also possible that data that isn't in the shared buffer is present in the page cache. This second case creates a scenario where tuning `effective_cache_size` can help improve performance. Let's use an example to explain this.

Let's say PostgreSQL needs to read some data that is not in the shared buffer, but it is in the page cache. From the perspective of PostgreSQL, there will be a shared buffer miss when it tries to read the data. When this happens, the PostgreSQL instance will assume that reading this data will be slow because it will come from disk. It assumes the data will come from disk because PostgreSQL has no way to know if the data is in the page cache. However, if it turns out that the data is present in the page cache, the data will be read faster than if it was read from disk.

If the page cache is large, it is far more likely that the data will in fact be in the page cache. `effective_cache_size` gives us a way to tell PostgreSQL that there is a lot of system memory used for the page cache, and thus, even if there is a shared buffer miss, it's very possible we will be "saved" by the page cache. The bigger we set `effective_cache_size`, the more likely PostgreSQL is to favor doing something like trying to read an index that is not present in the shared buffer, over doing a sequential scan of a table that is in the shared buffer. Even with the overhead of moving the index to the shared buffer from the page cache, the index scan will likely be faster than a sequential scan from the shared buffer. On average, this should improve performance.

Next, let's discuss `random_page_cost`. This has a similar effect as `effective_cache_size`.

`random_page_cost` tells the optimizer how much of a relative cost there is to accessing data from storage. The default of 4.0 is fairly conservative and is more appropriate for HDD based storage or when the shared buffer hit rate is below 90%. If the underlying storage technology is SSD, then it's best to reduce this number. Also, if the shared buffer hit rate is very high (90%+), it is also a good idea to reduce this number. The [documentation](https://www.postgresql.org/docs/15/runtime-config-query.html#GUC-RANDOM-PAGE-COST) suggests 1.1 for these cases.

How does `random_page_cost` affect the optimizer and help performance?

The effect to the planner/optimizer is similar to that of `effective_cache_size`. Basically, a lower `random_page_cost` tells the optimizer to favor doing something like reading an index from disk over say, doing a sequential table scan from the shared buffer. Also, keep in mind that when PostgreSQL tries to access the disk, it might actually be accessing from the page cache which is faster (see `effective_cache_size` above).

### Concurrency Configuration

Increasing parallelism allow us to use our available resources more efficiently. It's always a good idea to look at parameters related to parallel execution.

```

max_parallel_workers = <num_system_cpus>    # Default is 8
max_parallel_workers_per_gather = 4    # Default is 2
max_parallel_maintenance_workers = 4    # Default is 2
effective_io_concurrency = 300    # Default is 1
```

`max_parallel_workers` selects how many parallel operations can occur. As mentioned above, a good starting point for this parameter is to select this to match the number of cores on the system.

For `max_parallel_workers_per_gather = 4`, we found that setting this to the number of cores on the system didn't help. In fact, just doubling it to 4 provided the most benefit.

For `max_parallel_maintenance_workers`, we had a similar result to `max_parallel_workers_per_gather`. Doubling it to 4 seemed to provide most of the benefit.

`effective_io_concurrency` affects how many parallel IO requests we can send to storage. Modern storage technologies tend to allow a large number of IOPS. Thus, setting this higher is advised. Also note, this parameter only affects bitmap heap scans. A bitmap heap scan is a "in between" method for processing a query. That is, while Index scans (and Index only scans) are typically the fastest way to access data, and sequential scans are typically the slowest way to access data. A bitmap heap scan is in between these extremes.
