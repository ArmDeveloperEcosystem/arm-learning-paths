---
# User change
title: "System, Kernel, compiler, and Libraries"

weight: 3 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

##  Storage technology and file system format

The underlying storage technology and the file system format can impact performance significantly. In general, locally attached SSD storage will perform best. However, network based storage systems can perform well. As always, performance is dependent on the request profile coming from clients. You should spend some time studying and experimenting with different storage technologies and configuration options.

Aside from the storage technology, it is also worth testing different file system formats with `PostgreSQL`. The `xfs` file system is a good starting point. The `ext4` file system is another good alternative.  

##  Kernel configuration

`PostgreSQL` can benefit from adjustments to kernel parameters. Below is a list of kernel related settings that can have a positive impact on performance.

### Linux-PAM limits

Linux-PAM limits can be changed in the `/etc/security/limits.conf` file, or by using the `ulimit` command. 

If you want more information about how to display and modify parameters check the documentation of the `ulimit` command.

To display all limits:
```bash
ulimit -a
```

An explanation about why these Linux-PAM settings can help performance is found in the [PostgreSQL documentation](https://www.postgresql.org/docs/current/kernel-resources.html).

Some of the key settings that can affect performance are:

- Maximum number of open file descriptors (`ulimit -n`)
- Maximum number of processes (`ulimit -u`)
- Maximum data segment size (`ulimit -d`)
- Maximum locked-in-memory address space (`ulimit -l`)


### Linux virtual memory subsystem

Making changes to the Linux Virtual Memory subsystem can also improve performance. 

These settings can be changed in the `/etc/sysctl.conf` file, or by using the `sysctl` command. 

If you want more information about how to display and modify virtual memory parameters check the documentation of the `sysctl` command.

Documentation on each of these parameters can be found in the [admin-guide for sysctl in the Linux source code](https://github.com/torvalds/linux/blob/master/Documentation/admin-guide/sysctl/vm.rst).

To list all kernel parameters available:

```bash
sudo sysctl -a
```

### Overcommit memory

The overcommit policy is set via the sysctl `vm.overcommit_memory' setting. 

The recommended setting for `vm.overcommit_memory` is 2 according to the [PostgreSQL documentation](https://www.postgresql.org/docs/15/kernel-resources.html). 

To set the overcommit_memory parameter to 2 temporarily, run the following command:

```console
sudo sysctl -w vm.overcommit_memory=2
```
To make the change permanent:

```bash
sudo sh -c 'echo "vm.overcommit_memory=2" >> /etc/sysctl.conf'
```
This tells Linux to never over commit memory. Setting `vm.overcommit_memory` to 2 is to avoid a situation where the kernel might terminate the `PostgreSQL` postmaster when memory is scarce.

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

### Selecting the number of huge pages to use

You should set `vm.nr_hugepages` to a value that gives a total huge page space slightly bigger than the `PostgreSQL` shared buffer size (discussed later). 

Make it slightly larger than the shared buffer because `PostgreSQL` will use additional memory for things like connection management.

More information on the different parameters that affect the configuration of huge pages can be found in the [admin-guide for hugetlbpage in the Linux source code](https://github.com/torvalds/linux/blob/master/Documentation/admin-guide/mm/hugetlbpage.rst).

### Page cache parameters

`PostgreSQL` writes data to files like any Linux process does. The behavior of the page cache can affect performance. There are two sysctl that parameters control how often the kernel flushes the page cache data to disk.

- `vm.dirty_background_ratio=5`
- `vm.dirty_ratio=80`

The `vm.dirty_background_ratio` sets the percentage of the page cache that needs to be dirty in order for a flush to disk to start in the background. 

Setting this value to lower than the default (typically 10) helps write heavy workloads. This is because by lowering this threshold, you are spreading writes to storage over time. This reduces the probability of saturating storage.

Setting this value to 5 can improve performance.

The `vm.dirty_ratio` sets the percentage of the page cache that needs to be dirty in order for threads that are writing to storage to be paused to allow flushing to catch up. 

Setting this value higher than default (typically 10-20) helps performance when disk writes are bursty. A higher value gives the background flusher (controlled by `vm.dirty_background_ratio`) more time to catch up. 

Setting this as high as 80 can improve performance.

##  Compiler Considerations

The easiest way to gain performance is to use the latest version of GCC. Aside from that, the flags `-mcpu` and `-flto` can be used to potentially gain additional performance. Usage of these flags is explained in the [Migrating C/C++ applications](/learning-paths/servers-and-cloud-computing/migration/c/) section of the [Migrating applications to Arm servers](/learning-paths/servers-and-cloud-computing/migration/) learning path.

##  OpenSSL Considerations

PostgreSQL relies on [OpenSSL](https://www.openssl.org/) for cryptographic operations. Thus, the version of OpenSSL used with PostgreSQL (and the GCC version and switches used to compile it) can impact performance. Typically using the Linux distribution default version of OpenSSL is sufficient so long as the Linux distribution used isn't very old. That said, it is possible to use newer versions of OpenSSL which could yield performance improvements. We leave this as an exercise to the reader.
