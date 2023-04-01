---
# User change
title: "Tuning PostgreSQL"

weight: 3 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

Performance tuning refers to the parameters you can change to increase `PostgreSQL` database performance. This topic teaches you the parameters to look for and how to modify them. 


##  Application performance tuning

Application tuning allows you to gain performance without scaling your deployment up (bigger machines) or out (more machines). You have the option to either use the gained performance or trade it for cost savings by reducing the total compute resources provisioned. Below is a graph that shows the difference performance tuning on PostgreSQL can make.

![Before and after Tuning](BeforeAndAfter.png)

##  About database performance tuning

Keep in mind that deployment configurations and the profile of SQL requests made by clients will be different. This means there is no one size fits all set of tuning parameters for `PostgreSQL`.  Use the information below to learn how to tune `PostgreSQL`.

##  Storage technology and file system format

The underlying storage technology and the file system format can impact performance significantly. In general, locally attached SSD storage will perform best. However, network based storage systems can perform very well also. As always, performance is dependent on the request profile coming from clients. You should spend some time studying and experimenting with different storage technologies and configuration options.

Aside from the storage technology, it is also worth testing different file system formats with `PostgreSQL`. The `xfs` file system is a good starting point. The `ext4` file system is another good alternative.  

##  Kernel configuration

`PostgreSQL` can benefit from adjustments to kernel parameters. Below is a list of kernel related settings that can have a positive impact on performance.

### Linux-PAM limits

Linux-PAM limits can be changed in the `/etc/security/limits.conf` file, or by using the `ulimit` command. 

If you want more information about how to display and modify parameters look for a tutorial on the `ulimit` command. 

To display all limits:
```bash
ulimit -a
```

An explanation about why these Linux-PAM settings can help performance is found in the [PostgreSQL documentation](https://www.postgresql.org/docs/current/kernel-resources.html).

```output
nofile (ulimit -n):  Max number of open file descriptors
nproc (ulimit -u):   Max number of processes
data (ulimit -d):    Max data segment size
memlock (ulimit -l): Max locked-in-memory address space
```

### Linux virtual memory subsystem

Making changes to the Linux Virtual Memory subsystem can also improve performance. 

These settings can be changed in the `/etc/sysctl.conf` file, or by using the `sysctl` command. 

If you want more information about how to display and modify virtual memory parameters look for a tutorial on the `sysctl` command. 

Documentation on each of these parameters can be found in the [admin-guide for sysctl in the Linux source code](https://github.com/torvalds/linux/blob/master/Documentation/admin-guide/sysctl/vm.rst).

To list all kernel parameters available:

```bash
sudo sysctl -a
```

### Overcommit memory

```output
vm.overcommit_memory
```

The recommended setting for `vm.overcommit_memory` is 2 in the [PostgreSQL documentation](https://www.postgresql.org/docs/15/kernel-resources.html). 

This tells Linux to never over commit memory. Set `vm.overcommit_memory` to 2 is to avoid a situation where the kernel might terminate the `PostgreSQL` postmaster when memory is scarce.

### Huge memory pages

`PostgreSQL` benefits from using huge memory pages. Huge pages reduce how often virtual memory pages are mapped to physical memory.  

To see the current memory page configuration, run the following command on the host:

```bash
cat /proc/meminfo | grep ^Huge
```

The output should be similar to:

```output
HugePages_Total:       0
HugePages_Free:        0
HugePages_Rsvd:        0
HugePages_Surp:        0
Hugepagesize:       2048 kB
Hugetlb:               0 kB
```

Huge pages are not being used if `HugePages_Total` is 0 (this is the default). 

Also note that `Hugepagesize` is 2MB which is the typical default for huge pages on Linux. 

You can modify the huge page values.

The setting that enables huge pages is shown below:

```output
vm.nr_hugepages
```

This parameter sets the number of huge pages you want the kernel to make available to applications. 

The total amount of memory that will be used for huge pages will be this number (defaulted to 0) times the `Hugepagesize`. 

As an example, if you want a total of 1GB of huge page space, then you should set `vm.nr_hugepages` to 500 (500x2MB=1GB).

```bash
sudo sysctl -w vm.nr_hugepages=500
```

To make the change permanent:

```bash
sudo sh -c 'echo "vm.nr_hugepages=500" >> /etc/sysctl.conf'
```

### Set huge memory pages

You should set `vm.nr_hugepages` to a value that gives a total huge page space slightly bigger than the `PostgreSQL` shared buffer size (discussed later). 

Make it slightly larger than the shared buffer because `PostgreSQL` will use additional memory for things like connection management.

More information on the different parameters that affect the configuration of huge pages can be found in the [admin-guide for hugetlbpage in the Linux source code](https://github.com/torvalds/linux/blob/master/Documentation/admin-guide/mm/hugetlbpage.rst).

### Page cache parameters

`PostgreSQL` writes data to files like any Linux process does. The behavior of the page cache can affect performance. These two parameters control how often the kernel flushes the page cache data to disk.

```output
vm.dirty_background_ratio
```

The `vm.dirty_background_ratio` sets the percentage of the page cache that needs to be dirty in order for a flush to disk to start in the background. 

Setting this value to lower than the default (typically 10) helps write heavy workloads. This is because by lowering this threshold, you are spreading writes to storage over time. This reduces the probability of saturating storage.

```output
vm.dirty_ratio
```

The `vm.dirty_ratio` sets the percentage of the page cache that needs to be dirty in order for threads that are writing to storage to be paused to allow flushing to catch up. 

Setting this value higher than default (typically 10-20) helps performance when disk writes are bursty. A higher value gives the background flusher (controlled by `vm.dirty_background_ratio`) more time to catch up. 

Setting this as high as 80 can help performance.

##  PostgreSQL configuration

There are different ways to set configuration parameters for `PostgreSQL`. 

This is discussed in the [Setting Parameters documentation](https://www.postgresql.org/docs/current/config-setting.html). 

The configurations below can be directly pasted into a `PostgreSQL` configuration file.

### Connections and prepared transactions

```output
max_connections = 1000    # Default 100
max_prepared_transactions = 1000   # Default 0
```

`max_connections` doesn't impact performance, but if a high client connection count is expected or required, it's a good idea to raise this in order to not reject request from clients. 

Keep in mind that more client connections means more resources will be consumed (especially memory). Setting this to something higher is completely dependent on use case and requirements.

`max_prepared_transactions` is 0 by default. 

This means that stored procedures and functions cannot be used out of the box. It must be enabled by setting `max_prepared_transactions` to a value greater than 0. 

Using procedures and functions can greatly improve performance. 

### Memory related configuration

```output
huge_pages = on    # default is try
shared_buffers = <25%-40% system memory>    # Default is 128MB
work_mem = 32MB    # default is 4MB
maintenance_work_mem = 2GB    # Default is 64MB
```

Turning on `huge_pages` is not required because the default is `try`. 

However, you can explicitly set it to `on` because errors will be produced if huge pages are not enabled in Linux.

`shared_buffers` is one of the most important configuration parameters that can be set. It determines how much memory can be used to store indexes and table data. It's a cache that improves read/write latency and relieves pressure on storage. The [PostgreSQL documentation](https://www.postgresql.org/docs/15/runtime-config-resource.html) suggests this be set to 25% - 40% of total system memory.

`work_mem` is memory used when queries are being processed. Raising this significantly from the default value can help performance.

`maintenance_work_mem` is memory used for operations like VACUUM. In a scenario where data is removed often, raising this can help performance.

### Processing and process count

```output
deadlock_timeout = 10s    # Default is 1s
max_worker_processes = <num_system_cpus>    # Default is 8
```

`deadlock_timeout` sets a polling interval for checking locks. The [documentation](https://www.postgresql.org/docs/15/runtime-config-locks.html) states that this check is expensive from a CPU cycles standpoint, and that the default of 1s is probably the smallest that should be used. Consider raising this timeout much higher to save some CPU cycles. 

`max_worker_processes` is a key parameter for performance. It's the number of total background processes allowed. Set it to the number of cores present on the PostgreSQL node. A good starting point for thread/process count parameters is to use the number of cores on the system. This is not always true so try some experimentation.

### Write Ahead Log (WAL) configuration

```output
synchronous_commit = off    # Default is on
max_wal_size = 20GB    # Default is 1GB
wal_recycle = off    # Default is on
```

If `synchronous_commit` is on (default), it tells the WAL processor to wait until more of the log is applied before reporting success to clients. Turning this off means that the PostgreSQL instance will report success to clients sooner. This will result in a performance improvement. It is safe to turn this off in most cases, but keep in mind that it will increase the risk of losing transactions if there is a crash. However, it will not increase the risk of data corruption.

In high load scenarios, check pointing can happen very often. In fact, in testing with HammerDB, there may be so much check pointing that PostgreSQL reports warnings. One way to reduce how often check pointing occurs is to increase the `max_wal_size` of the WAL log. Setting it to 20GB can make the excessive check pointing warnings go away. 

`wal_recycle` does not impact performance. However, in scenarios where a large amount of data is being loaded (for example, restoring a database), turning this off will speed up the process and reduce the chances of replication errors to occur if streaming replication is used.

### Planner/Optimizer configuration

The optimizer (also called planner) is responsible for taking statistics about the execution of previous queries, and using that information to figure out what is the fastest way to process new queries. Some of these statistics include shared buffer hit/miss rate, execution time of sequential scans, and execution time of index scans. Below are some parameters that affect the optimizer. 

```output
effective_cache_size = <80% of system memory>    # Default is 4GB
random_page_cost = 1.1    # Default is 4.0
```

One key piece of information that a `PostgreSQL` instance will not have access to is the size of the OS page cache. `effective_cache_size` provides a way to inform `PostgreSQL` of the page cache size. Assuming the host is dedicated to running `PostgreSQL`, a good starting value is to set this to about 80% of total system memory. The value of this parameter should roughly be the shared buffer size and the OS page cache size combined. Use a tool like `free` while `PostgreSQL` is running to understand how much memory is being used for the OS page cache. This can help further refine the value from the suggested 80%. Also note that this parameter does not affect memory allocations.

**How does `effective_cache_size` affect the optimizer and help performance?**

When data is loaded into the PostgreSQL shared buffer, the same data may also be present in the page cache. It is also possible that data that isn't in the shared buffer is present in the page cache. This second case creates a scenario where tuning `effective_cache_size` can help improve performance. 

Sometimes `PostgreSQL` needs to read data that is not in the shared buffer, but it is in the page cache. From the perspective of `PostgreSQL`, there will be a shared buffer miss when it tries to read the data. When this happens, the `PostgreSQL` instance will assume that reading this data will be slow because it will come from disk. It assumes the data will come from disk because `PostgreSQL` has no way to know if the data is in the page cache. However, if it turns out that the data is present in the page cache, the data will be read faster than if it was read from disk.

If the page cache is large, it is far more likely that the data will in fact be in the page cache. `effective_cache_size` gives us a way to tell `PostgreSQL` that there is a lot of system memory used for the page cache, and thus, even if there is a shared buffer miss, it's very possible we will be "saved" by the page cache. The bigger we set `effective_cache_size`, the more likely `PostgreSQL` is to favor doing something like trying to read an index that is not present in the shared buffer, over doing a sequential scan of a table that is in the shared buffer. Even with the overhead of moving the index to the shared buffer from the page cache, the index scan will likely be faster than a sequential scan from the shared buffer. On average, this should improve performance.

`random_page_cost` has a similar effect as `effective_cache_size`.

`random_page_cost` tells the optimizer how much of a relative cost there is to accessing data from storage. The default of 4.0 is fairly conservative and is more appropriate for HDD based storage or when the shared buffer hit rate is below 90%. If the underlying storage technology is SSD, then it's best to reduce this number. Also, if the shared buffer hit rate is very high (90%+), it is also a good idea to reduce this number. The [documentation](https://www.postgresql.org/docs/15/runtime-config-query.html#GUC-RANDOM-PAGE-COST) suggests 1.1 for these cases.

**How does `random_page_cost` affect the optimizer and help performance?**

The effect to the planner/optimizer is similar to that of `effective_cache_size`. Basically, a lower `random_page_cost` tells the optimizer to favor doing something like reading an index from disk over doing a sequential table scan from the shared buffer. Also, keep in mind that when `PostgreSQL` tries to access the disk, it might actually be accessing from the page cache which is faster.

### Concurrency configuration

Increasing parallelism uses available resources more efficiently. It's always a good idea to look at parameters related to parallel execution.

```output
max_parallel_workers = <num_system_cpus>    # Default is 8
max_parallel_workers_per_gather = 4    # Default is 2
max_parallel_maintenance_workers = 4    # Default is 2
effective_io_concurrency = 300    # Default is 1
```

`max_parallel_workers` selects how many parallel operations can occur. A good starting point for this parameter is to set this to match the number of cores in the system.

Doubling `max_parallel_workers_per_gather` and  `max_parallel_maintenance_workers` to 4 seems to provide the most benefit.

`effective_io_concurrency` affects how many parallel IO requests you can send to storage. Modern storage technologies tend to allow a large number of IOPS. Thus, setting this higher is advised. Also note, this parameter only affects bitmap heap scans. A bitmap heap scan is an "in between" method for processing a query. That is, while Index scans (and Index only scans) are typically the fastest way to access data, and sequential scans are typically the slowest way to access data. A bitmap heap scan is in between these extremes.

You now have a good understanding of the parameters to check to increase performance of `PostgreSQL`.
