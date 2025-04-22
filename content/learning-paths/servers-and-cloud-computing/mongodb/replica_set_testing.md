---
# User change
title: "Three node replica set testing with YCSB"


weight: 5 # (intro is 1), 2 is first, 3 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

talk about which one to get on and how to run tests and see output

## Recommended Tests on MongoDB

The most common three tests are **95/5** (95% read and 5% update), **100/0** (100% read and 0% update) and **90/10** (90% read and 10% update). In real world testing its recommended to run a **95/5** test.

Once you have loaded the dataset, run the selected test for approximately **five** minutes. This will allow the system to warm up before you start collecting performance data. The goal is to reach a high cpu utilization( 90+% ). Adjusting the number of threads, operationscount and recordscount can help you achieve this. Examples below maybe need to be adjusted based on the instance type you selected.

## Load dataset

```console
./bin/ycsb load mongodb -s  -P workloads/workloadb  -p mongodb.url=mongodb://localhost:27017 -p compressibility=2 -p fieldlengthdistribution=zipfian -p minfieldlength=50 -threads 64 -p recordcount=20000000
```

## Run 95/5 test:

```console
./bin/ycsb run mongodb -s  -P workloads/workloadb  -p mongodb.url=mongodb://localhost:27017 -p minfieldlength=50 -p compressibility=2 -p maxexecutiontime=120 -threads 64 -p operationcount=40000000 -p recordcount=20000000 -p requestdistribution=zipfian -p readproportion=0.95 -p updateproportion=0.05
```

## Run 100/0 test:

```console
./bin/ycsb run mongodb -s  -P workloads/workloadc  -p mongodb.url=mongodb://Localhost:27017 -p minfieldlength=50 -p compressibility=2 -p maxexecutiontime=120 -threads 64 -p operationcount=40000000 -p recordcount=20000000 -p requestdistribution=zipfian -p readproportion=1.0 -p updateproportion=0.0
```

## Run 90/10 test:

```console
./bin/ycsb run mongodb -s  -P workloads/workloadb  -p mongodb.url=mongodb://localhost:27017 -p minfieldlength=50 -p compressibility=2 -p maxexecutiontime=120 -threads 64 -p operationcount=40000000 -p recordcount=20000000  -p requestdistribution=zipfian -p readproportion=0.90 -p updateproportion=0.10
```

For more detailed information on all the parameters for running a workload refer to [Running a Workload.](https://github.com/brianfrankcooper/YCSB/wiki/Running-a-Workload)

## Other tests

For instructions on running any other tests or more details on the metrics reported, refer to the [GitHub project for the YCSB.](https://github.com/brianfrankcooper/YCSB/wiki/).

