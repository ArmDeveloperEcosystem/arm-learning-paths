---
title: "Enable libhugetlbfs on Redis"
weight: 4
layout: "learningpathall"
---

## Overview
This page illustrates the steps to enable libhugetlbfs on Redis and test results after enabling it.

## Commands to build
In order to build libhugetlbfs on Redis, please modify the Makefile like this:
```
# diff -uNr redis/src/Makefile redis-huge/src/Makefile
--- redis/src/Makefile 2023-07-25 15:56:03.247327640 +0800
+++ redis-huge/src/Makefile 2023-08-02 15:12:56.392576822 +0800
@@ -168,6 +168,9 @@
# Include paths to dependencies
FINAL_CFLAGS+= -I../deps/hiredis -I../deps/linenoise -I../deps/lua/src

+
+FINAL_LDFLAGS+= -B /usr/share/libhugetlbfs -Wl,--hugetlbfs-align --no-pie -Wl,--no-as-needed
+
# Determine systemd support and/or build preference (defaulting to auto-detection)
BUILD_WITH_SYSTEMD=no
# If 'USE_SYSTEMD' in the environment is neither "no" nor "yes", try to
```
and build Redis with make.


after build, check if the program has linked to libhugetlbfs.so, for example:

```
root@bolt-ecs:/data# ldd /data/redis-huge/src/redis-server |grep huge
libhugetlbfs.so.0 => /lib/aarch64-linux-gnu/libhugetlbfs.so.0 (0x0000ffffac690000)
```


## Commands to run
After rebuilding Redis with libhugetlbfs, add HUGETLB_ELFMAP=RW at the beginning of the command to start Redis. for example:
```
$ HUGETLB_ELFMAP=RW [path-to-redis]/src/redis-server redis.conf
```

please note don't export HUGETLB_ELFMAP=RW as an environment varible, it has to be specified right before the mysqld exectuable.

## Test results
the test shows enabling libhugetlbfs on redis-server, performance improves 2.69%.

### Without libhugetlbfs
this is the default build.  run memtier test 3 rounds, average TPS is 251940:

```
Avg: (254914+248692+252216)/3=251940
```

#### Round 1
```
ALL STATS

============================================================================================================================

Type         Ops/sec     Hits/sec   Misses/sec    Avg. Latency     p50 Latency     p99 Latency   p99.9 Latency       KB/sec

----------------------------------------------------------------------------------------------------------------------------

Sets       127458.17          ---          ---         0.31439         0.30300         0.49500         0.56700      9570.45

Gets       127456.77     26634.24    100822.53         0.31348         0.30300         0.49500         0.56700      5600.19

Waits           0.00          ---          ---             ---             ---             ---             ---          ---

Totals     254914.94     26634.24    100822.53         0.31394         0.30300         0.49500         0.56700     15170.64

```

#### Round 2
```
ALL STATS

============================================================================================================================

Type         Ops/sec     Hits/sec   Misses/sec    Avg. Latency     p50 Latency     p99 Latency   p99.9 Latency       KB/sec

----------------------------------------------------------------------------------------------------------------------------

Sets       124347.19          ---          ---         0.32206         0.30300         0.51900         0.59100      9336.82

Gets       124345.76     47587.36     76758.40         0.32151         0.30300         0.51900         0.58300      6180.83

Waits           0.00          ---          ---             ---             ---             ---             ---          ---

Totals     248692.95     47587.36     76758.40         0.32179         0.30300         0.51900         0.59100     15517.65

```
#### Round 3
round 3, also captured the perf stat for tlb misses:

```
root@bolt-ecs:~# perf stat -e l1d_tlb_refill,l1i_tlb_refill,l2d_tlb_refill -a -- sleep 10



 Performance counter stats for 'system wide':



       542,736,109      l1d_tlb_refill

        99,163,242      l1i_tlb_refill

        17,063,682      l2d_tlb_refill



       9.987657624 seconds time elapsed



ALL STATS

============================================================================================================================

Type         Ops/sec     Hits/sec   Misses/sec    Avg. Latency     p50 Latency     p99 Latency   p99.9 Latency       KB/sec 

----------------------------------------------------------------------------------------------------------------------------

Sets       126108.74          ---          ---         0.31765         0.31100         0.50300         0.57500      9469.10 

Gets       126107.34     48260.06     77847.28         0.31692         0.30300         0.50300         0.57500      6268.31 

Waits           0.00          ---          ---             ---             ---             ---             ---          --- 

Totals     252216.08     48260.06     77847.28         0.31729         0.31100         0.50300         0.57500     15737.41 

```

### With libhugetlbfs
after enabling the hugepage, the average TPS is 258733 after 3 rounds, it shows performance improves 2.69%.

```
(258733-251940)/251940*100=2.69%
```

the improvement is trivial, probably because only 6 hugepages are used:
```
HugePages_Total:      40

HugePages_Free:       34

HugePages_Rsvd:        0

HugePages_Surp:        0
```

#### Round 1
```
ALL STATS

============================================================================================================================

Type         Ops/sec     Hits/sec   Misses/sec    Avg. Latency     p50 Latency     p99 Latency   p99.9 Latency       KB/sec 

----------------------------------------------------------------------------------------------------------------------------

Sets       129378.74          ---          ---         0.30975         0.29500         0.49500         0.56700      9714.64 

Gets       129377.17     27401.31    101975.87         0.30881         0.29500         0.49500         0.56700      5696.70 

Waits           0.00          ---          ---             ---             ---             ---             ---          --- 

Totals     258755.92     27401.31    101975.87         0.30928         0.29500         0.49500         0.56700     15411.34 

```
#### Round 2
```
ALL STATS

============================================================================================================================

Type         Ops/sec     Hits/sec   Misses/sec    Avg. Latency     p50 Latency     p99 Latency   p99.9 Latency       KB/sec 

----------------------------------------------------------------------------------------------------------------------------

Sets       127865.55          ---          ---         0.31327         0.30300         0.49500         0.56700      9601.04 

Gets       127864.25     49489.27     78374.98         0.31262         0.29500         0.49500         0.56700      6374.12 

Waits           0.00          ---          ---             ---             ---             ---             ---          --- 

Totals     255729.80     49489.27     78374.98         0.31294         0.29500         0.49500         0.56700     15975.16 

```
#### Round 3
round 3, it shows the tlb misses dropped:
```
root@bolt-ecs:~# perf stat -e l1d_tlb_refill,l1i_tlb_refill,l2d_tlb_refill -a -- sleep 10



 Performance counter stats for 'system wide':



       521,870,717      l1d_tlb_refill                                              

         1,090,292      l1i_tlb_refill                                              

        14,138,677      l2d_tlb_refill                                              



       9.987569318 seconds time elapsed



ALL STATS

============================================================================================================================

Type         Ops/sec     Hits/sec   Misses/sec    Avg. Latency     p50 Latency     p99 Latency   p99.9 Latency       KB/sec 

----------------------------------------------------------------------------------------------------------------------------

Sets       130859.79          ---          ---         0.30621         0.30300         0.47900         0.55100      9825.81 

Gets       130858.19     50660.77     80197.42         0.30536         0.30300         0.47900         0.55100      6523.79 

Waits           0.00          ---          ---             ---             ---             ---             ---          --- 

Totals     261717.97     50660.77     80197.42         0.30579         0.30300         0.47900         0.55100     16349.60 

```




