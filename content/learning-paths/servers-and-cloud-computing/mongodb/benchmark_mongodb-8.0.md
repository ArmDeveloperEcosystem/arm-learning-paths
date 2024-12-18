---
# User change
title: "Benchmark MongoDB 8.0 on Arm with Yahoo Cloud Serving Benchmark (YCSB)"

weight: 4 # (intro is 1), 2 is first, 3 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
To further measure the performance of MongoDB, you will run the [Yahoo Cloud Serving Benchmark](http://github.com/brianfrankcooper/YCSB).

YCSB is an open sourced project which provides the framework and common set of workloads to evaluate the performance of different "key-value" and "cloud" serving stores. Here are the steps to run YCSB to evaluate the performance of MongoDB running on 64-bit Arm machine.

## Additional software packages

To run YCSB, additional software packages are required: default-jdk, default-jre, maven, make and Python.


Install all other packages:

{{< tabpane code=true >}}
  {{< tab header="Ubuntu" >}}
sudo apt-get update
sudo apt install -y default-jre default-jdk maven make gcc
{{< /tab >}}
{{< /tabpane >}}
{{% notice  Python Note%}}

For Ubuntu 22.04 and 24.04 the `python` package may not be found. You can install Python 2.7 using:
```console
wget https://www.python.org/ftp/python/2.7.18/Python-2.7.18.tgz
cd Python-2.7.18
sudo ./configure --enable-optimizations
make altinstall
ln -s /usr/local/bin/python2.7 /usr/bin/python
```
{{% /notice %}}

## Setup YCSB

Download the latest released YCSB zip file and uncompress it.

```bash
mkdir ycsb && cd ycsb
curl -O --location https://github.com/brianfrankcooper/YCSB/releases/download/0.17.0/ycsb-0.17.0.tar.gz
tar xfvz ycsb-0.17.0.tar.gz

```
Now `cd` into project folder and run the executable to print a description of how to use the benchmark.

```bash
cd ycsb-0.17.0
./bin/ycsb
```

## Most Common MongoDB Test Setup

The recommended test setup is a relica set. Which contains three nodes each of equal size. A primary will be the node you send the YCSB traffic to.

## Recommended Tests on MongoDB

The most common real world test to run is a 95/5 test, 95% read and 5% update. 100/0 and 90/10 are also popular. Run the following commands for about 5 mins before collecting data.

Load the dataset
```console
./bin/ycsb load mongodb -s  -P workloads/workloadb  -p mongodb.url=mongodb://localhost:27017 -p compressibility=2 -p fieldlengthdistribution=zipfian -p minfieldlength=50 -threads 64 -p recordcount=20000000
```

95/5
```console
./bin/ycsb run mongodb -s  -P workloads/workloadb  -p mongodb.url=mongodb://localhost:27017 -p minfieldlength=50 -p compressibility=2 -p maxexecutiontime=120 -threads 64 -p operationcount=40000000 -p recordcount=20000000 -p requestdistribution=zipfian -p readproportion=0.95 -p updateproportion=0.05

```

100/0
```console
./bin/ycsb run mongodb -s  -P workloads/workloadc  -p mongodb.url=mongodb://Localhost:27017 -p minfieldlength=50 -p compressibility=2 -p maxexecutiontime=120 -threads 64 -p operationcount=40000000 -p recordcount=20000000 -p requestdistribution=zipfian -p readproportion=1.0 -p updateproportion=0.0

```

90/10
```console
./bin/ycsb run mongodb -s  -P workloads/workloadb  -p mongodb.url=mongodb://localhost:27017 -p minfieldlength=50 -p compressibility=2 -p maxexecutiontime=120 -threads 64 -p operationcount=40000000 -p recordcount=20000000  -p requestdistribution=zipfian -p readproportion=0.90 -p updateproportion=0.10

```

For more detailed information on all the parameters for running a workload refer to [this section](https://github.com/brianfrankcooper/YCSB/wiki/Running-a-Workload).

## View the results

At the end of each test, statistics are printed to the console. Shown below is the output from the end of Load/Insert test

```output
2022-07-06 15:50:18:917 1 sec: 1000 operations; 542.01 current ops/sec; [CLEANUP: Count=10, Max=12951, Min=0, Avg=1295.2, 90=4, 99=12951, 99.9=12951, 99.99=12951] [INSERT: Count=1000, Max=134655, Min=561, Avg=8506.37, 90=10287, 99=39903, 99.9=134015, 99.99=134655]
[OVERALL], RunTime(ms), 1849
[OVERALL], Throughput(ops/sec), 540.8328826392644
[TOTAL_GCS_Copy], Count, 5
[TOTAL_GC_TIME_Copy], Time(ms), 23
[TOTAL_GC_TIME_%_Copy], Time(%), 1.2439156300703083
[TOTAL_GCS_MarkSweepCompact], Count, 0
[TOTAL_GC_TIME_MarkSweepCompact], Time(ms), 0
[TOTAL_GC_TIME_%_MarkSweepCompact], Time(%), 0.0
[TOTAL_GCs], Count, 5
[TOTAL_GC_TIME], Time(ms), 23
[TOTAL_GC_TIME_%], Time(%), 1.2439156300703083
[CLEANUP], Operations, 10
[CLEANUP], AverageLatency(us), 1295.2
[CLEANUP], MinLatency(us), 0
[CLEANUP], MaxLatency(us), 12951
[CLEANUP], 95thPercentileLatency(us), 12951
[CLEANUP], 99thPercentileLatency(us), 12951
[INSERT], Operations, 1000
[INSERT], AverageLatency(us), 8506.367
[INSERT], MinLatency(us), 561
[INSERT], MaxLatency(us), 134655
[INSERT], 95thPercentileLatency(us), 11871
[INSERT], 99thPercentileLatency(us), 39903
[INSERT], Return=OK, 1000
...
```
## Other tests

For instructions on running any other tests or more details on the metrics reported, refer to the [GitHub project for the YCSB](https://github.com/brianfrankcooper/YCSB/wiki/).

