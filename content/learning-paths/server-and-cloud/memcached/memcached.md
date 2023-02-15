---
layout: learningpathall
title: Run Memcached on Arm servers
weight: 2
---

## Prerequisites

* An [Arm based instance](/learning-paths/server-and-cloud/csp/) from an appropriate cloud service provider running `Ubuntu Linux 20.04`.

This learning path has been tested on AWS and Oracle platforms.


## Install necessary software and packages

Launch an Arm-based instance running `Ubuntu 20.04`.

Install `gcc` on your instance following the steps [here](/install-tools/gcc/#native).

Install [libevent](https://libevent.org/):
```bash
sudo apt-get update
sudo apt install libevent-dev -y
```

Install the necessary packages required by `memtier_benchmark`:
```bash
sudo apt install build-essential autoconf automake libpcre3-dev libevent-dev pkg-config zlib1g-dev libssl-dev wget git -y
```

## Install memcached from source on Arm servers

```bash
wget http://memcached.org/files/memcached-1.6.17.tar.gz
tar -zxvf memcached-1.6.17.tar.gz
cd memcached-1.6.17
./configure && make && make test && sudo make install
```

## Run memcached on Arm server
```console
/usr/local/bin/memcached
```

To understand possible options, use the following command:
```bash
/usr/local/bin/memcached -h
```

## Install memtier_benchmark

[memtier_benchmark](https://github.com/RedisLabs/memtier_benchmark) is a command line utility developed by Redis Labs for load generation and bechmarking NoSQL key-value databases. We will use this to benchmark the performance of memcached.

```bash
git clone https://github.com/RedisLabs/memtier_benchmark
cd memtier_benchmark
autoreconf -ivf
./configure
make
sudo make install
```

## Measure memcached performance by running memtier_benchmark

```console
memtier_benchmark -s localhost -p 11211 --protocol=memcache_text --clients=100 --threads=5 --ratio=1:1 --key-pattern=R:R --key-minimum=16 --key-maximum=16 --data-size=128 --requests=10000 --run-count=20
```
To understand what each of the command line options do, see the help output:
```bash { ret_code="2" }
memtier_benchmark --help
```

## View Results

At the end of the benchmark run, the aggregated performance results are printed on the console. For example, using the command above, the output will be similar to:
```
AGGREGATED AVERAGE RESULTS (20 runs)
============================================================================================================================
Type         Ops/sec     Hits/sec   Misses/sec    Avg. Latency     p50 Latency     p99 Latency   p99.9 Latency       KB/sec
----------------------------------------------------------------------------------------------------------------------------
Sets       187514.94          ---          ---         1.33816         1.12700         2.84700         7.42300     29665.45
Gets       187514.94    187514.94         0.00         1.33374         1.12700         2.83100         7.39100     32046.01
Waits           0.00          ---          ---             ---             ---             ---             ---          ---
Totals     375029.89    187514.94         0.00         1.33595         1.12700         2.84700         7.42300     61711.46
```