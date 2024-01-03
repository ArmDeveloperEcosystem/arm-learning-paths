---
title: "Enable libhugetlbfs on MySQL"
weight: 3
layout: "learningpathall"
---

You can enable libhugetlbfs on more complex workloads such as MySQL and test results after enabling it.

Before proceeding, you should be familiar with building and running MySQL. Refer to [Benchmarking MySQL with Sysbench](/learning-paths/servers-and-cloud-computing/mysql_benchmark/) for more information. The steps below explain how to modify the build and run of MySQL server to enable libhugtlbfs. The full instructions are not provided.

## Commands to build

In order to build MySQL with libhugetlbfs support, you can add the following options to both -DCMAKE_C_FLAGS and -DCMAKE_CXX_FLAGS:

```console
-B /usr/share/libhugetlbfs -Wl,--hugetlbfs-align -no-pie -Wl --no-as-needed
```

If you look at the `cmake` command in the [Build and install MySQL server](/learning-paths/servers-and-cloud-computing/mysql_benchmark/setup_mysql_server/) section you will see the `cmake` command to modify.

The new `cmake` command is:

```console
 cmake -DCMAKE_C_FLAGS="-g -mcpu=native -B /usr/share/libhugetlbfs -Wl,--hugetlbfs-align -no-pie -Wl,--no-as-needed" -DCMAKE_CXX_FLAGS="-g -mcpu=native -B /usr/share/libhugetlbfs -Wl,--hugetlbfs-align -no-pie -Wl,--no-as-needed" -DCMAKE_INSTALL_PREFIX=/home/mysql/mysql_install/1-install_8.0.33_huge -DWITH_BOOST=/home/mysql/boost_1_77_0/ ..
```

The 2 `make` commands are the same:

```console
make -j $(nproc)
make -j $(nproc) install
```

After the build completes, check if the program has linked with libhugetlbfs.so, for example:

```console
ldd mysqld | grep huge
```

The output should show libhugetlbfs is used.

```output
libhugetlbfs.so.0 => /lib/aarch64-linux-gnu/libhugetlbfs.so.0 (0x0000ffffac690000)
```

## Commands to run

After rebuilding MySQL with libhugetlbfs, add HUGETLB_ELFMAP=RW at the beginning of the commands that start MySQL. 

This is an addition to the information in the [Start the MySQL server](/learning-paths/servers-and-cloud-computing/mysql_benchmark/setup_mysql_server/) section. Add the variable before each invocation of `mysql`.

For example:

```console
HUGETLB_ELFMAP=RW /home/mysql/mysql_install/1-install_8.0.33_huge/bin/mysqld ...
```

{{% notice Note %}}
Do not export HUGETLB_ELFMAP=RW as an environment variable, it has to be specified right before the mysqld executable.
{{% /notice %}}

## Test Results

Testing MySQL without and with libhugetlbfs shows performance increases by approximately 12%.

### Without libhugetlbfs

Reboot your server and run the test twice.

#### First round

```output
Throughput:

    events/s (eps):                      8604.3221

    time elapsed:                        300.0912s

    total number of events:              2582080

```

#### Second round

TPS is 8524 events/sec. You can also use `perf stat` during the run to look at the TLB refill counts. 

```console
perf stat -e l1d_tlb_refill,l1i_tlb_refill,l2d_tlb_refill -a -- sleep 10
```

The output will be similar to:

```output



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

Reboot your server and run 2 more tests with libhugetlbfs enabled. 

To enable hugepages, you need to run the following commands:

```console
chown -R mysql.mysql /dev/hugepages
echo 40 >  /proc/sys/vm/nr_hugepages
```

The first command gives permission to the `mysql` user to access hugepages (default is only root). The second command allocates 40 hugepages.


When the test is run you can check that hugepages are used:

```console
cat /proc/meminfo
``````

The output will show the number of free hugepages has decreased.

```output
HugePages_Total:      40

HugePages_Free:        4

HugePages_Rsvd:        1

HugePages_Surp:        0

Hugepagesize:       2048 kB

Hugetlb:           81920 kB

```

In this case, MySQL used 36 huge pages (36*2M=72M).


#### First round

TPS is 9627 events/sec, a 12.9% increase compared to the first round without hugepages.

```output
Throughput:

    events/s (eps):                      9627.5017

    time elapsed:                        300.0855s

    total number of events:              2889073

```

#### Second round

TPS is 9538 events/sec, a 11.9% increase compared to the second round without enabling hugepages. 

The `perf stat` output shows TLB misses are significantly reduced:

```console
perf stat -e l1d_tlb_refill,l1i_tlb_refill,l2d_tlb_refill -a -- sleep 10
```

The output will be similar to:

```output


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

Building and running MySQL with libhugetlbfs provides increased performance.
