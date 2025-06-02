---
layout: learningpathall
title: Run and test Memcached on Arm servers
weight: 2
---

## Prerequisites

Launch an [Arm based instance](/learning-paths/servers-and-cloud-computing/csp/) from a cloud service provider running an Ubuntu Linux distribution.

Install `gcc` on your instance by following the steps in the [GNU compiler install guide](/install-guides/gcc/native/).

This Learning Path has been tested on `AWS` and `Oracle Cloud` platforms.

## Install necessary software and packages

Install [libevent](https://libevent.org/):
```bash
sudo apt-get update
sudo apt install libevent-dev -y
```

Install the necessary packages required by `memtier_benchmark`:
```bash
sudo apt install build-essential autoconf automake libpcre3-dev libevent-dev pkg-config zlib1g-dev libssl-dev wget git -y
```

## Install and start memcached

You can install a pre-built memcached with:
```bash
sudo apt install memcached -y
```
Start the memcached service with:
```bash
sudo systemctl start memcached
```

### Install memcached from source on Arm servers

If you prefer to build from source code, use:
```bash
wget https://memcached.org/files/memcached-1.6.27.tar.gz
tar -zxvf memcached-1.6.27.tar.gz
cd memcached-1.6.27
./configure && make && make test && sudo make install
```
You can verify the latest available version on the [downloads page](https://memcached.org/downloads).

### Run memcached on Arm server
When built, start the `memcached` daemon with:
```console
/usr/local/bin/memcached start -u memcached -d
```
To understand possible options, use the following command:
```bash
/usr/local/bin/memcached -h
```

## Build memtier_benchmark

[memtier_benchmark](https://github.com/RedisLabs/memtier_benchmark) is a command line utility developed by Redis Labs for load generation and bechmarking NoSQL key-value databases. You will use this to benchmark the performance of memcached.

```bash
git clone https://github.com/RedisLabs/memtier_benchmark
cd memtier_benchmark
autoreconf -ivf
./configure
make
sudo make install
```

## Measure memcached performance by running memtier_benchmark

Run the benchmark with a command such as:
```console
memtier_benchmark -s localhost -p 11211 --protocol=memcache_text --clients=100 --threads=5 --ratio=1:1 --key-pattern=R:R --key-minimum=16 --key-maximum=16 --data-size=128 --requests=10000 --run-count=20
```
This will take a few minutes to complete.

To understand what each of the command line options do, see the help output:
```bash { ret_code="2" }
memtier_benchmark --help
```

## View Results

At the end of the benchmark run, the aggregated performance results are printed on the console.

The output will be similar to:
```output
AGGREGATED AVERAGE RESULTS (20 runs)
============================================================================================================================
Type         Ops/sec     Hits/sec   Misses/sec    Avg. Latency     p50 Latency     p99 Latency   p99.9 Latency       KB/sec
----------------------------------------------------------------------------------------------------------------------------
Sets       187514.94          ---          ---         1.33816         1.12700         2.84700         7.42300     29665.45
Gets       187514.94    187514.94         0.00         1.33374         1.12700         2.83100         7.39100     32046.01
Waits           0.00          ---          ---             ---             ---             ---             ---          ---
Totals     375029.89    187514.94         0.00         1.33595         1.12700         2.84700         7.42300     61711.46
```
