---
title: "General enablement method of libhugetlbfs"
weight: 2
layout: "learningpathall"
---

##  Introduction of libhugetlbfs
libhugetlbfs is a library that can back application text, data, malloc() and shared memory with hugepages. This is of benefit to applications that use large amounts of address space and suffer a performance hit due to TLB misses. Hence, by enabling libhugetlbfs, workloads with large code/data/heap sections would see significant performance improvement.


## Install necessary packages
On ubuntu 20, install necessary package and create symbolic link:
```
$ sudo apt-get install libhugetlbfs-dev libhugetlbfs-bin
$ sudo ln -s /usr/bin/ld.hugetlbfs /usr/share/libhugetlbfs/ld
```
## Add compile option to enable libhugetlbfs
add the following build option to build script (gcc option), and rebuild workload, from build option we could learn libhugetlbfs would be enabled in linking stage:
```
-B /usr/share/libhugetlbfs -Wl,--hugetlbfs-align -no-pie -Wl,--no-as-needed

```

## Enable system hugepage

enable Linux system hugepage, for example, setting 1000 huge pages, for 2M huge pages, that's 2G:
```
# echo 1000 > /proc/sys/vm/nr_hugepages
# cat /proc/meminfo |grep HugePages_Total
HugePages_Total: 1000

```


## Add HUGETLB_ELFMAP=RW before starting workload
add HUGETLB_ELFMAP=RW prefix before starting the workload, which places both READ (such as code) and WRITE (such as data) in hugepage, such as:
```
$ HUGETLB_ELFMAP=RW [workload]
```


## Check hugepage is used

make sure hugepage is used by checking meminfo:

```
cat /proc/meminfo

HugePages_Total: 1000
HugePages_Free: 994

```

Also check if the process is having huge page mapped:
```
$ cat /proc/<pid>/smaps | less

00200000-00400000 r-xp 00000000 00:25 48337 /dev/hugepages/libhugetlbfs.tmp.0D0D7x (deleted)
Size: 2048 kB
KernelPageSize: 2048 kB
MMUPageSize: 2048 kB
Rss: 0 kB
Pss: 0 kB
Shared_Clean: 0 kB
Shared_Dirty: 0 kB
Private_Clean: 0 kB
Private_Dirty: 0 kB
Referenced: 0 kB
Anonymous: 0 kB
LazyFree: 0 kB
AnonHugePages: 0 kB
ShmemPmdMapped: 0 kB
FilePmdMapped: 0 kB
Shared_Hugetlb: 0 kB
Private_Hugetlb: 2048 kB
Swap: 0 kB
SwapPss: 0 kB
Locked: 0 kB
THPeligible: 0
```








