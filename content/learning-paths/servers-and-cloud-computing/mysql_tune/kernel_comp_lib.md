---
# User change
title: Tune storage, kernel, compiler, and library settings for performance
description: Learn how storage, kernel page size, Linux huge pages, compiler settings, and OpenSSL choices can affect MySQL performance on Arm-based systems.

weight: 3 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## Tune the system around MySQL

MySQL configuration is only one part of performance tuning. Operating system settings, storage behavior, kernel memory management, compiler choices, and library versions can also affect throughput and latency. The following are system-level areas to check before or alongside MySQL-specific tuning.

### Storage technology, file systems, and disk scheduling

Storage technology and file system choices can affect performance. In general, locally attached SSD storage performs best, but network-based storage systems can also perform well. Test the storage technologies and configuration options available in your environment.

The file system used with MySQL can also affect performance. The `xfs` file system is a good starting point, and `ext4` is another good option. For production systems, use storage volumes dedicated to the database instead of sharing them with the operating system or other applications.

When running in the cloud, the disk scheduling algorithm is typically set to `noop` or a similar minimal scheduler. This is usually a good setting for MySQL in cloud environments, so no adjustment is needed. If you run MySQL on an on-premises server, double-check the disk scheduling algorithm and test alternatives. According to the [Optimizing InnoDB Disk I/O documentation](https://dev.mysql.com/doc/refman/en/optimizing-innodb-diskio.html), `noop` or `deadline` might be better options for some systems.

### MySQL storage engines

MySQL supports different storage engines. The default storage engine is `InnoDB`, which performs best across the broadest set of use cases.

Information on alternative storage engines can be found in the [MySQL documentation](https://dev.mysql.com/doc/refman/en/storage-engines.html).

### Kernel configuration

MySQL can benefit from adjustments to kernel parameters. The following kernel-related settings can have a positive impact on performance.

#### Linux virtual memory subsystem

Making changes to the Linux virtual memory subsystem can improve performance.

You can change these settings by using the `sysctl` command or by adding configuration files under `/etc/sysctl.d/`.

Documentation on the virtual memory subsystem parameters can be found in the [admin-guide for sysctl in the Linux source code](https://github.com/torvalds/linux/blob/master/Documentation/admin-guide/sysctl/vm.rst).

To list all sysctl parameters available:

```bash
sudo sysctl -a
```

For more information, see the `sysctl` command documentation.

#### Consider 64 KB kernel pages on Arm

Some Arm Linux distributions provide kernels built with `64 KB` base pages instead of `4 KB` base pages. This is a kernel selection or build-time choice, not a `sysctl` setting you can change on a running system.

A `64 KB` base page can improve some memory-intensive workloads because each base page maps more memory. This can reduce Memory Management Unit (MMU) translation overhead, reduce page-table walk depth, and relieve Translation Lookaside Buffer (TLB) pressure, including instruction-side TLB pressure in the CPU front end.

The tradeoff is memory efficiency. Larger base pages can increase internal fragmentation for workloads with many small or sparsely touched mappings, which can reduce the effective amount of memory available to the application and operating system.

The benefit is workload dependent, so compare a `4 KB` kernel and a `64 KB` kernel with the same MySQL & storage configuration.

Base page size also affects the huge page sizes available on Arm. The common PMD-level huge page sizes are:

| Kernel base page size | PMD-level huge page size |
|-----------------------|--------------------------|
| `4 KB`                | `2 MiB`                  |
| `64 KB`               | `512 MiB`                |

For more information, see the Linux kernel documentation for [Memory Layout on AArch64 Linux](https://docs.kernel.org/next/arm64/memory.html) and [HugeTLBpage on ARM64](https://docs.kernel.org/next/arm64/hugetlbpage.html).

### Huge memory pages

MySQL can benefit from using huge memory pages, especially when the InnoDB buffer pool is large. Huge memory pages have a similar performance goal to `64 KB` base pages: they map more memory per translation entry, which can reduce page-table walks and TLB pressure.

The tradeoff is also similar. Huge pages reserve memory in larger chunks, so over-allocating them can reduce the memory available for other uses. Under-allocating them can prevent MySQL from using huge pages at all. The performance impact depends on your workload and system configuration.

To see the current huge memory page configuration, run the following command on the host:

```bash
grep '^Huge' /proc/meminfo
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

Huge pages are not being used if `HugePages_Total` is `0` (this is typically the default).

The `Hugepagesize` value depends on the kernel base page size and platform configuration. Use the value reported by `/proc/meminfo` when calculating `vm.nr_hugepages`.

The sysctl parameter that enables huge pages is shown below:

```output
vm.nr_hugepages
```

This parameter sets the number of huge pages you want the kernel to make available to applications.

The total amount of memory used for huge pages is this number, which defaults to 0, multiplied by the `Hugepagesize` value.

For example, if you want `1 GiB` of huge page space and `Hugepagesize` is `2 MiB`, set `vm.nr_hugepages` to `512`.

```bash
sudo sysctl -w vm.nr_hugepages=512
```

To make the change permanent:

```bash
echo "vm.nr_hugepages=512" | sudo tee /etc/sysctl.d/99-mysql-hugepages.conf
sudo sysctl --system
```

#### Selecting the number of huge pages to use

If huge pages improve your workload, set `vm.nr_hugepages` to a value that gives a total huge page space equal to or slightly larger than the InnoDB buffer pool size, which is controlled by `innodb_buffer_pool_size`.

{{% notice Important %}}
After restarting MySQL with `large-pages=ON`, check both `/proc/meminfo` and the MySQL error log. If the huge page pool is too small, or MySQL cannot allocate huge pages for another reason, InnoDB can fall back to traditional memory and write `Warning: Using conventional memory pool.` to the MySQL error log. You might also see an allocation warning similar to `large_page_aligned_alloc mmap(... bytes) failed; errno 12`.
{{% /notice %}}

Selecting the buffer pool size is discussed in the [Tuning MySQL](/learning-paths/servers-and-cloud-computing/mysql_tune/tuning/) section.

Typically, only the number of huge pages needs to be configured. However, for more information on the different parameters that affect the configuration of huge pages, review the [admin-guide for hugetlbpage in the Linux source code](https://github.com/torvalds/linux/blob/master/Documentation/admin-guide/mm/hugetlbpage.rst).

### Compiler considerations

If you build MySQL from source, the compiler version and optimization flags can affect performance. Use a recent version of GCC, and consider flags such as `-mcpu` and `-flto` for additional optimization. These flags are explained in the [Migrating C/C++ applications](/learning-paths/servers-and-cloud-computing/migration/c/) section of the [Migrating applications to Arm servers](/learning-paths/servers-and-cloud-computing/migration/) Learning Path.

### OpenSSL considerations

MySQL relies on [OpenSSL](https://www.openssl.org/) for cryptographic operations. The OpenSSL version used with MySQL, and the compiler version and switches used to build it, can affect performance. The default OpenSSL version provided by your Linux distribution is typically sufficient.

If you build MySQL from source, you can also build and install a newer version of OpenSSL before building MySQL. This might improve performance for workloads that spend significant time in cryptographic operations.

## What you've learned and what's next

You've now explored enhancements you can make at the system-level related to storage, memory pages, compiler flags, and OpenSSL to improve MySQL performance on Arm. 

Next, you'll learn about specific MySQL parameters that you can tune for performance. 