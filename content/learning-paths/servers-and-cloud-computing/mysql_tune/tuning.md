---
# User change
title: "Tuning MySQL"

weight: 3 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

Performance tuning refers to the parameters you can change to increase `MySQL` database performance. This topic teaches you the parameters to look for and how to modify them. 


##  Application performance tuning

Application tuning allows you to gain performance without scaling your deployment up (bigger machines) or out (more machines). You have the option to use the gained performance or trade it for cost savings by reducing the total compute resources provisioned. Below is a graph that shows the difference performance tuning on `MySQL` can make.

![Before and after Tuning](BeforeAndAfter.png)

##  About database performance tuning

Keep in mind that deployment configurations and the profile of SQL requests made by clients will be different. This means there is no one size fits all set of tuning parameters for `MySQL`.  Use the information below to learn how to tune `MySQL`.

##  Storage technology and file system format

The underlying storage technology and the file system format can impact performance significantly. In general, locally attached SSD storage will perform best. However, network based storage systems can perform very well also. As always, performance is dependent on the request profile coming from clients. You should spend some time studying and experimenting with different storage technologies and configuration options.

Aside from the storage technology, it is also worth testing different file system formats with `MySQL`. The `xfs` file system is a good starting point. The `ext4` file system is another good alternative. 

##  MySQL storage engines

There are different storage engines available for `MySQL`. The default storage engine is `InnoDB`. `InnoDB` is good for performance testing and tuning.

Information on alternative storage engines can be found in the [MySQL documentation](https://dev.mysql.com/doc/refman/8.0/en/storage-engines.html).

##  Kernel configuration

`MySQL` can benefit from adjustments to kernel parameters. Below is a list of kernel related settings that can have a positive impact on performance.

### Linux-PAM limits

Linux-PAM limits can be changed in the `/etc/security/limits.conf` file, or by using the `ulimit` command. 

If you want more information about how to display and modify parameters look for a tutorial on the `ulimit` command. 

To display all limits:
```bash
ulimit -a
```

To display the `memlock` (Max locked-in-memory address space) limit only:
```bash
ulimit -l
```

`memlock` is the only PAM limit which is useful to adjust for `MySQL`. 

The suggested value for `memlock` is `unlimited` when using huge pages with `MySQL`. 

Enabling huge pages can result in significant performance gains. 

The suggestion to set `memlock` when huge pages are enabled can be found in the [MySQL documentation](https://dev.mysql.com/doc/refman/8.0/en/large-page-support.html).


### Linux virtual memory subsystem

Making changes to the Linux Virtual Memory subsystem can also improve performance. 

These settings can be changed in the `/etc/sysctl.conf` file, or by using the `sysctl` command. 

If you want more information about how to display and modify virtual memory parameters look for a tutorial on the `sysctl` command. 

Documentation on each of these parameters can be found in the [admin-guide for sysctl in the Linux source code](https://github.com/torvalds/linux/blob/master/Documentation/admin-guide/sysctl/vm.rst).

To list all kernel parameters available:

```bash
sudo sysctl -a
```

### Huge memory pages

 `MySQL` benefits from using huge memory pages. Huge pages reduce how often virtual memory pages are mapped to physical memory. 
 
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

The kernel parameter that enables huge pages is shown below:

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

You should set `vm.nr_hugepages` to a value that gives a total huge page space slightly bigger than the `MySQL` shared buffer size (discussed later). 

Make it slightly larger than the shared buffer because `MySQL` will use additional memory for things like connection management.

More information on the different parameters that affect the configuration of huge pages can be found in the [admin-guide for hugetlbpage in the Linux source code](https://github.com/torvalds/linux/blob/master/Documentation/admin-guide/mm/hugetlbpage.rst).

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

Using larger pages helps to reduce how often physical memory has to get mapped to virtual memory. Note that huge pages needs to be turned on at the kernel level for this to work.

`innodb_buffer_pool_size` is one of the most important configuration parameters that can be set. It determines how much memory can be used to store indexes and table data. It's a cache that improves read/write latency and relieves pressure on storage. The [MySQL documentation](https://dev.mysql.com/doc/refman/8.0/en/innodb-buffer-pool.html) suggests this be set to up to 80% of total system memory. Setting this value significantly larger than the default of 128MB is a good idea.

Other memory related configurations that could be worth exploring are the [Buffer Pool Prefetching](https://dev.mysql.com/doc/refman/8.0/en/innodb-performance-read_ahead.html) configurations. 

You may see modest performance gains by decreasing the `innodb_read_ahead_threshold` a little. The default is very conservative and will result in very little to no prefetching. Some workloads may benefit from being less conservative. Turning on random prefetch (`innodb_random_read_ahead`) seems to hurt performance. 

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

`innodb_io_capacity` tells the `InnoDB` storage engine how many IOPS it can issue to storage. The default of 200 is on the smaller side and more appropriate for rotational storage. Modern SSD storage and even cloud based storage can benefit greatly from increasing this value. The [MySQL InnoDB I/O Capacity documentation](https://dev.mysql.com/doc/refman/8.0/en/innodb-configuring-io-capacity.html) suggests this be set to around 1000 for higher performing storage. There are many types of storage technologies available so you should experiment with this setting.

`innodb_io_capacity_max` defaults to 2x of `innodb_io_capacity`. It is worth experimenting with this value in use cases that experience heavy disk usage.

`innodb_read_io_threads` and `innodb_write_io_threads` sets the number of threads used for IO disk operations. Setting this to the number of CPUs in the system provides performance benefits. Experiment with these parameters since a value that is smaller then the total number of CPUs in the system may be sufficient.

### Spin lock configuration

```output
innodb_sync_spin_loops=120    # Default is 30
```

You should experiment with the `innodb_sync_spin_loops` parameter. This sets the number of times a thread checks for an `InnoDB` mutex to be free before yielding execution to another thread. 

Profiling `MySQL` with Linux `perf` shows that `MySQL` spends a lot of time waiting for locks to be freed. Experimenting with tuning parameters around locks might help. Increasing the number of times a lock is checked before the thread yields reduces context switching. This reduction in context switching increases performance. Start with a value of 120 for `innodb_sync_spin_loops`, but you can also try values such as 30, 60, 180, and 240. 

You now have a good understanding of the parameters to investigate to increase performance of `MySQL`.