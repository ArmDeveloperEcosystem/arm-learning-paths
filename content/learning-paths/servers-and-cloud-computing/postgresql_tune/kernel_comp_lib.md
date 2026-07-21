---
title: Tune storage, kernel, compiler, and library settings for performance
description: Learn how storage, kernel page size, Linux huge pages, compiler settings, and OpenSSL choices can affect PostgreSQL performance on Arm-based systems.

weight: 3
layout: "learningpathall"
---

## Tune the system around PostgreSQL

PostgreSQL configuration is only one part of performance tuning. Operating system settings, storage behavior, kernel memory management, compiler choices, and library versions can also affect throughput and latency. Check these system-level areas before or alongside PostgreSQL-specific tuning.

### Storage technology and file systems

Storage technology and file system choices can affect performance. Locally attached SSD storage often provides the lowest latency, but network-based storage can also perform well. Test the storage technologies and configuration options available in your environment.

The file system used with PostgreSQL can also affect performance. The `xfs` file system is a useful starting point, and `ext4` is another common option. For production systems, use storage volumes dedicated to the database instead of sharing them with the operating system or other applications.

### Kernel resource limits

PostgreSQL uses operating system resources such as file descriptors, processes, and locked memory. Review the limits for the account that runs PostgreSQL, especially when you increase connection count or shared memory use.

The limits most likely to affect a PostgreSQL deployment are:

- Maximum number of open file descriptors (`ulimit -n`)
- Maximum number of processes (`ulimit -u`)
- Maximum data segment size (`ulimit -d`)
- Maximum locked-in-memory address space (`ulimit -l`)

To display the current limits, run:

```bash
ulimit -a
```

For more information, see the PostgreSQL documentation about [kernel resource limits](https://www.postgresql.org/docs/current/kernel-resources.html).

### Kernel memory configuration

You can change Linux virtual memory settings by using the `sysctl` command or by adding configuration files under `/etc/sysctl.d/`.

To list the available sysctl parameters, run:

```bash
sudo sysctl -a
```

For details about virtual memory parameters, see the Linux [sysctl documentation](https://docs.kernel.org/admin-guide/sysctl/vm.html).

#### Overcommit memory

The `vm.overcommit_memory` setting controls Linux memory-overcommit behavior. PostgreSQL recommends a value of [`2`](https://www.postgresql.org/docs/current/kernel-resources.html) to reduce the risk that the kernel terminates the PostgreSQL server when memory is scarce. With a value of `2`, Linux uses strict overcommit accounting and denies memory allocations that would exceed its commit limit.

To set the value temporarily, run:

```bash
sudo sysctl -w vm.overcommit_memory=2
```

To make the setting persistent, create a file under `/etc/sysctl.d/` and reload the settings:

```bash
echo "vm.overcommit_memory=2" | sudo tee /etc/sysctl.d/99-postgresql-memory.conf
sudo sysctl --system
```

#### Consider 64 KB kernel pages on Arm

Some Arm Linux distributions provide kernels built with `64 KB` base pages instead of `4 KB` base pages. This is a kernel selection or build-time choice, not a `sysctl` setting that you can change on a running system.

A `64 KB` base page can improve some memory-intensive workloads because each base page maps more memory. This can reduce Memory Management Unit (MMU) translation overhead, reduce page-table walk depth, and relieve Translation Lookaside Buffer (TLB) pressure, including instruction-side TLB pressure in the CPU front end.

The tradeoff is memory efficiency. Larger base pages can increase internal fragmentation for workloads with many small or sparsely touched mappings, which can reduce the effective memory available to PostgreSQL and the operating system.

The benefit is workload dependent, so compare a `4 KB` kernel and a `64 KB` kernel with the same PostgreSQL and storage configuration.

Linux uses several page-table levels. A Page Middle Directory (PMD) entry can map one contiguous block of memory directly, without individual page-table entries for the base pages inside that block. The amount of memory mapped by a PMD entry depends on the base page size and page-table geometry.

On Arm, this means a PMD-level huge page commonly maps `2 MiB` with `4 KB` base pages, or `512 MiB` with `64 KB` base pages:

| Kernel base page size | PMD-level huge page size |
|-----------------------|--------------------------|
| `4 KB`                | `2 MiB`                  |
| `64 KB`               | `512 MiB`                |

Other huge page sizes can be available, but use the value reported by `/proc/meminfo` when configuring `vm.nr_hugepages`.

For more information, see the Linux kernel documentation for [Memory Layout on AArch64 Linux](https://docs.kernel.org/next/arm64/memory.html) and [HugeTLBpage on ARM64](https://docs.kernel.org/next/arm64/hugetlbpage.html).

### Huge memory pages

PostgreSQL can benefit from explicit huge memory pages because they use smaller page tables and can reduce CPU time spent on memory management. They have a similar performance goal to `64 KB` base pages: map more memory per translation entry and reduce page-table walks and TLB pressure.

The tradeoff is also similar. Huge pages reserve memory in larger chunks, so over-allocating them can reduce memory available for other uses. The performance impact depends on your workload and system configuration.

To see the current huge page configuration, run:

```bash
grep '^Huge' /proc/meminfo
```

The output is similar to:

```output
HugePages_Total:       0
HugePages_Free:        0
HugePages_Rsvd:        0
HugePages_Surp:        0
Hugepagesize:       2048 kB
Hugetlb:               0 kB
```

The `Hugepagesize` value depends on the kernel base page size and platform configuration. Use the value reported by `/proc/meminfo` when calculating `vm.nr_hugepages`.

The `vm.nr_hugepages` parameter sets the number of huge pages that the kernel makes available to applications. The total memory reserved for huge pages is `vm.nr_hugepages` multiplied by `Hugepagesize`.

For example, if you want `1 GiB` of huge page space and `Hugepagesize` is `2 MiB`, set `vm.nr_hugepages` to `512`:

```bash
sudo sysctl -w vm.nr_hugepages=512
```

To make the setting persistent:

```bash
echo "vm.nr_hugepages=512" | sudo tee /etc/sysctl.d/99-postgresql-hugepages.conf
sudo sysctl --system
```

#### Configure PostgreSQL to use huge pages

The PostgreSQL [`huge_pages`](https://www.postgresql.org/docs/current/runtime-config-resource.html#GUC-HUGE-PAGES) setting controls whether PostgreSQL requests huge pages for its main shared memory area. The default, `try`, attempts to use them and falls back to regular pages if allocation fails.

Set `huge_pages=on` when you want PostgreSQL to fail at startup instead of silently using regular pages:

```ini
huge_pages = on
```

Start with `shared_buffers`, which is usually the largest part of PostgreSQL shared memory. Allocate enough huge pages to cover that value plus a small margin for other shared-memory allocations. The next section explains how to select a `shared_buffers` value.

{{% notice Important %}}
After restarting PostgreSQL, confirm the result with `SHOW huge_pages_status;` and check the PostgreSQL server log. With `huge_pages=try`, PostgreSQL can fall back to regular pages when the huge page pool is too small. With `huge_pages=on`, it does not start until enough huge pages are available.
{{% /notice %}}

PostgreSQL explicitly configured huge pages are different from Transparent Huge Pages (THP). PostgreSQL documentation discourages THP because it has caused performance degradation on some Linux versions.

For more information about Linux huge page configuration, see the [Linux HugeTLBpage documentation](https://docs.kernel.org/admin-guide/mm/hugetlbpage.html).

### Page-cache writeback settings

The Linux page cache affects PostgreSQL write behavior. The `vm.dirty_background_ratio` and `vm.dirty_ratio` settings control when the kernel begins background writeback and when application writes can be delayed while flushing catches up.

The following values are a useful starting point for a write-heavy workload. They are not required for every PostgreSQL deployment:

```ini
vm.dirty_background_ratio = 5
vm.dirty_ratio = 20
```

`vm.dirty_background_ratio` controls the percentage of page cache that must be dirty before the kernel starts background writeback. Lowering it can spread storage writes over time and reduce long write stalls for some write-heavy workloads.

`vm.dirty_ratio` controls the threshold at which processes that generate writes can be delayed while the kernel catches up. Keep it higher than `vm.dirty_background_ratio`. A higher value gives background writeback more time to catch up with bursty writes, but it also allows more dirty data to accumulate and can create longer stalls when the kernel finally needs to flush it.

These settings depend on memory capacity, storage latency, and write behavior, so change them only when measurement shows that writeback is a bottleneck.

### Compiler considerations

If you build PostgreSQL from source, the compiler version and optimization flags can affect performance. Use a recent version of GCC, and consider flags such as `-mcpu` and `-flto` for additional optimization. These flags are explained in the [Migrating C/C++ applications](/learning-paths/servers-and-cloud-computing/migration/c/) section of the [Migrating applications to Arm servers](/learning-paths/servers-and-cloud-computing/migration/) Learning Path.

### OpenSSL considerations

PostgreSQL relies on [OpenSSL](https://www.openssl.org/) for cryptographic operations. The OpenSSL version used with PostgreSQL, and the compiler version and switches used to build it, can affect performance. The default OpenSSL version provided by your Linux distribution is typically sufficient.

If you build PostgreSQL from source, testing a newer OpenSSL release might help workloads that spend significant time in cryptographic operations.

## What you've learned and what's next

You've explored system-level choices related to storage, memory pages, kernel settings, compiler flags, and OpenSSL that can affect PostgreSQL performance on Arm.

Next, you'll learn about PostgreSQL parameters that you can tune for performance.
