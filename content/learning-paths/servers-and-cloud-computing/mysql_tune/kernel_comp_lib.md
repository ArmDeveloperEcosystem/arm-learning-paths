---
# User change
title: "System, Kernel, Compiler, and Libraries"

weight: 3 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

##   Storage technology, file system format, and disk scheduling

The underlying storage technology and the file system format can impact performance. In general, locally attached SSD storage will perform best. However, network based storage systems can perform well. You should spend some time studying and experimenting with different storage technologies and configuration options.

Aside from the storage technology, the file system format used with `MySQL` can impact performance. The `xfs` file system is a good starting point. The `ext4` file system is another good alternative. Last, it is recommended to use storage drives that are dedicated to the database (i.e. not shared with the OS or other applications).

When running in the cloud, the disk scheduling algorithm is typically set to `noop` or a similar "dumb" algorithm. This is typically optimal for `MySQL` in the cloud, so no adjustment is needed. However, if running `MySQL` on an on-prem server, it's a good idea to double check what the disk scheduling algorithm is, and possibly change it. According to the [Optimizing InnoDB Disk I/O documentation](https://dev.mysql.com/doc/refman/en/optimizing-innodb-diskio.html), `noop` or `deadline` might be better options. It's worth testing this with on-prem systems.

##  MySQL storage engines

There are different storage engines available for `MySQL`. The default storage engine is `InnoDB`. `InnoDB` is the default storage engine because it performs the best in the broadest set of use cases.

Information on alternative storage engines can be found in the [MySQL documentation](https://dev.mysql.com/doc/refman/en/storage-engines.html).

##  Kernel configuration

`MySQL` can benefit from adjustments to kernel parameters. Below is a list of kernel related settings that can have a positive impact on performance.

### Linux virtual memory subsystem

Making changes to the Linux Virtual Memory subsystem can improve performance. 

These settings can be changed in the `/etc/sysctl.conf` file, or by using the `sysctl` command. 

Documentation on the virtual memory subsystem parameters can be found in the [admin-guide for sysctl in the Linux source code](https://github.com/torvalds/linux/blob/master/Documentation/admin-guide/sysctl/vm.rst).

To list all sysctl parameters available:

```bash
sudo sysctl -a
```

See the `sysctl` command documentation for more.

### Huge memory pages

 `MySQL` benefits from using huge memory pages. Huge pages reduce how often virtual memory pages are mapped to physical memory. 
 
To see the current huge memory page configuration, run the following command on the host:

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

Huge pages are not being used if `HugePages_Total` is 0 (this is typically the default). 

Also note that `Hugepagesize` is 2MiB which is the typical default for huge pages on Linux. 

The sysctl parameter that enables huge pages is shown below:

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

You should set `vm.nr_hugepages` to a value that gives a total huge page space equal to or slightly larger than the `MySQL` buffer pool size. Selecting the buffer pool size is discussed in the [Tuning MySQL](/learning-paths/servers-and-cloud-computing/mysql_tune/tuning) section.

Typically, only the number of huge pages needs to be configured. However, for more information on the different parameters that affect the configuration of huge pages, review the [admin-guide for hugetlbpage in the Linux source code](https://github.com/torvalds/linux/blob/master/Documentation/admin-guide/mm/hugetlbpage.rst).

##  Compiler Considerations

The easiest way to gain performance is to use the latest version of GCC. Aside from that, the flags `-mcpu` and `-flto` can be used to potentially gain additional performance. Usage of these flags is explained in the [Migrating C/C++ applications](/learning-paths/servers-and-cloud-computing/migration/c/) section of the [Migrating applications to Arm servers](/learning-paths/servers-and-cloud-computing/migration/) learning path.

##  OpenSSL Considerations

MySQL relies on [OpenSSL](https://www.openssl.org/) for cryptographic operations. Thus, the version of OpenSSL used with MySQL (and the GCC version and switches used to compile it) can impact performance. Typically using the Linux distribution default version of OpenSSL is sufficient.

However, it is possible to use newer versions of OpenSSL which could yield performance improvements. This is achieved by building and installing OpenSSL before building MySQL.