---
# User change
title: "Run YCSB using a 3 node replica set"

weight: 5 # (intro is 1), 2 is first, 3 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

The recommended MongoDB YCSB test setup is a relica set containing three nodes of equal size. The primary node is the node you send the YCSB traffic to and the others are secondary nodes.

## What is a replica Set?

A replica set is a group of instances that maintain the same data set. A replica set contains many nodes, but 3 nodes are used for testing. 

## What node size should I use?

The most common size for testing MongoDB is an 8 vCPU instance. You can test with any sized machine, but if you are looking for ideal testing conditions 8 vCPUs is enough. Each node should have 32GB of RAM.

## How should I run this test?

You should keep the complete data set in memory. Additional details abut the recommended configuration are provided below.

## Mongod.conf

```console
# Configuration Options: https://docs.mongodb.org/manual/reference/configuration-options/
# Log Messages/Components: https://docs.mongodb.com/manual/reference/log-messages/index.html

systemLog:
  destination: file
  logAppend: true
  path: /var/log/mongodb/mongodb.log

storage:
  dbPath: /mnt/mongodb # Mounting point selected
  engine: wiredTiger
  wiredTiger:
    engineConfig:
      configString: "cache_size=16484MB" # 50% of your ram is recommened. Adding more helps depending on dataset.

replication:
  replSetName: "rs0" # Name of your replicaset
  oplogSizeMB: 5000

# network interfaces
net:
  port: 27017
  bindIp: 0.0.0.0
  maxIncomingConnections: 16000
setParameter:
  diagnosticDataCollectionDirectorySizeMB: 400
  honorSystemUmask: false
  lockCodeSegmentsInMemory: true
  reportOpWriteConcernCountersInServerStatus: true
  suppressNoTLSPeerCertificateWarning: true
  tlsWithholdClientCertificate: true
```
**systemLog:** Contains locations and details of where logging should be contained.
- **path:** Location for logging

**storage:** Its recommended to run test within memory to get achieve the best performance. This contains details on the engine used and location of storage.
- **engine:** Wiredtiger is used in this case. Using a disk will add latency.
- **cache_size:** The minimum if using the recommend instance size is 50% of 32(16gb). But in testing using 18gb produced better results.

**replication:** This is used for replica set setup.
- **replSetName:** This is the name of the replica set.
- **oplogSizeMB:** 5% of the disk size is recommended.

**net:** Contains details of networking on the node.
- **port:** 27017 is the port used for replica sets
- **maxIncomingConnections:** The maximum number of incoming connections supported by MongoDB

**setParameter:** Addtional options
- **diagnosticDataCollectionDirectorySizeMB:** 400 is based on the docs.
- **honorSystemUmask:** Sets read and write permissions only to the owner of new files
- **lockCodeSegmentsInMemory:** Locks code into memory and prevents it from being swapped.
- **suppressNoTLSPeerCertificateWarning:** allows clients to connect without a certificate. (Only for testing purposes)
- **tlsWithholdClientCertificate:** Will not send the certification during communication. (Only for testing purposes)

If you would like to use encryption you will need to add the security and keyFile to your configuration. As well as change some of the parameters in the mongod.conf.

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

