---
title: "Enable libhugetlbfs on MySQL"
weight: 3
layout: "learningpathall"
---
## Overview
This page illustrates the steps to enable libhugetlbfs on MySQL and test results after enabling it.


## Commands to build
In order to build libhugetlbfs on MySQL, please add the following options to both -DCMAKE_C_FLAGS and -DCMAKE_CXX_FLAGS:
```
-B /usr/share/libhugetlbfs -Wl,--hugetlbfs-align -no-pie -Wl --no-as-needed
```

for example:
```
$ cmake -DCMAKE_C_FLAGS="-g -mcpu=native -B /usr/share/libhugetlbfs -Wl,--hugetlbfs-align -no-pie -Wl,--no-as-needed" -DCMAKE_CXX_FLAGS="-g -mcpu=native -B /usr/share/libhugetlbfs -Wl,--hugetlbfs-align -no-pie -Wl,--no-as-needed" -DCMAKE_INSTALL_PREFIX=/home/mysql/mysql_install/1-install_8.0.33_huge -DWITH_BOOST=/home/mysql/boost_1_77_0/ ..
$ make -j $(nproc)
$ make install
```

after build, check if the program has linked to libhugetlbfs.so, for example:
```
root@bolt-ecs:/data# ldd mysqld |grep huge
libhugetlbfs.so.0 => /lib/aarch64-linux-gnu/libhugetlbfs.so.0 (0x0000ffffac690000)
```

## Commands to run
After rebuilding MySQL with libhugetlbfs, add HUGETLB_ELFMAP=RW at the beginning of the command to start MySQL. for example:
```
$ HUGETLB_ELFMAP=RW /home/mysql/mysql_install/1-install_8.0.33_huge/bin/mysqld ...
```

please note don't export HUGETLB_ELFMAP=RW as an environment varible, it has to be specified right before the mysqld exectuable.


## Test Results

By testing MySQL without/with libhugetlbfs, it shows performance increased by 11.9%～12.9%.

### Without libhugetlbfs
Reboot server and do 2 round tests

#### First round

```
Throughput:

    events/s (eps):                      8604.3221

    time elapsed:                        300.0912s

    total number of events:              2582080

```

#### Second round
TPS is 8524, also get the perf stat during the run:

```
root@bolt-ecs:~# perf stat -e l1d_tlb_refill,l1i_tlb_refill,l2d_tlb_refill -a -- sleep 10



 Performance counter stats for 'system wide':



       815,254,864      l1d_tlb_refill                                              

       490,265,467      l1i_tlb_refill                                              

       422,887,362      l2d_tlb_refill                                              



      10.003289183 seconds time elapsed

Throughput:

    events/s (eps):                      8524.8307

    time elapsed:                        300.0878s

    total number of events:              2558197

```

### With libhugetlbfs

Reboot and do 2 round test, in order to enable hugepage in server, need to do the following things:

```
# chown -R mysql.mysql /dev/hugepages

# echo 40 >  /proc/sys/vm/nr_hugepages

# cat /proc/meminfo

HugePages_Total:      40

HugePages_Free:        4

HugePages_Rsvd:        1

HugePages_Surp:        0

Hugepagesize:       2048 kB

Hugetlb:           81920 kB

```
mysql used 36 huge pages (36*2M=72M) in the case.


#### First round
TPS is 9627, this is 12.9% increased compared to the 1st round without enabling hugepage:
```
Throughput:

    events/s (eps):                      9627.5017

    time elapsed:                        300.0855s

    total number of events:              2889073

```
#### Second round
TPS is 9538, this is 11.9% increased compared to the 2nd round of without enabling hugepage, perf stat shows TLB misses are signifcantly reduced:

```
root@bolt-ecs:~# perf stat -e l1d_tlb_refill,l1i_tlb_refill,l2d_tlb_refill -a -- sleep 10



 Performance counter stats for 'system wide':



       688,157,786      l1d_tlb_refill                                              

        70,741,621      l1i_tlb_refill                                              

       254,054,393      l2d_tlb_refill                                              



      10.002128509 seconds time elapsed

Throughput:

    events/s (eps):                      9538.9346

    time elapsed:                        300.0847s

    total number of events:              2862487

```
