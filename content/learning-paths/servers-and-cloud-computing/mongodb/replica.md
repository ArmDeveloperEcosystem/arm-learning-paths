---
# User change
title: "Run YCSB using a 3 node replica set"

draft: true

weight: 5 # (intro is 1), 2 is first, 3 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

The recommended MongoDB YCSB test setup is a relica set containing three nodes of equal size. The primary node is the node you send the YCSB traffic to and the others are secondary nodes.

## What is a replica set?

A replica set is a group of instances that maintain the same data set. A replica set contains many nodes, but 3 nodes are used for testing. 

## What node size should I use?

The most common size for testing MongoDB is an 8 vCPU instance. You can test with any sized machine, but if you are looking for ideal testing conditions 8 vCPUs is enough. Each node should have 32GB of RAM.

You should keep the complete data set in memory. Additional details abut the recommended configuration are provided below.

## Create a replica set

Create a 3 node replica set by starting 3 Arm instances with the specifications above. 

Install MongoDB on each node using the previously provided instructions. 

Select 1 instance as the primary node and install YCSB on the instance.

## Initialize the replica set

1. Set variables with the IP addresses of each node:

    ```bash
    PRIMARY_NODE_IP="<primary-node-ip>"
    SECONDARY_NODE1_IP="<secondary-node1-ip>"
    SECONDARY_NODE2_IP="<secondary-node2-ip>"
    ```

2. Connect to the primary node using the MongoDB shell:

    ```bash
    mongosh --host <primary-node-ip>:27017
    ```

3. Initialize the replica set with the following command:

    ```bash
    PRIMARY_NODE_IP="<primary-node-ip>"
    SECONDARY_NODE1_IP="<secondary-node1-ip>"
    SECONDARY_NODE2_IP="<secondary-node2-ip>"

    mongosh --host $PRIMARY_NODE_IP:27017 <<EOF
    rs.initiate({
      _id: "rs0",
      members: [
        { _id: 0, host: "$PRIMARY_NODE_IP:27017" },
        { _id: 1, host: "$SECONDARY_NODE1_IP:27017" },
        { _id: 2, host: "$SECONDARY_NODE2_IP:27017" }
      ]
    })
    EOF
    ```

3. Verify the replica set status:

    ```bash
    mongosh --host $PRIMARY_NODE_IP:27017 <<EOF
    rs.status()
    EOF
    ```

## Modify the MongoDB configuration

Use a text editor to edit the file `/etc/mongodb.conf` file and replace the contents of the file with the text below.

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

**setParameter:** Additional options
- **diagnosticDataCollectionDirectorySizeMB:** 400 is based on the docs.
- **honorSystemUmask:** Sets read and write permissions only to the owner of new files
- **lockCodeSegmentsInMemory:** Locks code into memory and prevents it from being swapped.
- **suppressNoTLSPeerCertificateWarning:** allows clients to connect without a certificate. (Only for testing purposes)
- **tlsWithholdClientCertificate:** Will not send the certification during communication. (Only for testing purposes)

If you want to use encryption you will need to add the security and keyFile to your configuration. As well as change some of the parameters in the `mongod.conf` file.


## Recommended Tests on MongoDB

The most common real world test to run is a 95/5 test, 95% read and 5% update. 100/0 and 90/10 are also popular. 

Run the following commands for about 5 mins before collecting data.

Load the dataset:

```console
./bin/ycsb load mongodb -s  -P workloads/workloadb  -p mongodb.url=mongodb://localhost:27017 -p compressibility=2 -p fieldlengthdistribution=zipfian -p minfieldlength=50 -threads 64 -p recordcount=20000000
```

Run the 95/5 test:

```console
./bin/ycsb run mongodb -s  -P workloads/workloadb  -p mongodb.url=mongodb://localhost:27017 -p minfieldlength=50 -p compressibility=2 -p maxexecutiontime=120 -threads 64 -p operationcount=40000000 -p recordcount=20000000 -p requestdistribution=zipfian -p readproportion=0.95 -p updateproportion=0.05

```

Run the 100/0 test:

```console
./bin/ycsb run mongodb -s  -P workloads/workloadc  -p mongodb.url=mongodb://Localhost:27017 -p minfieldlength=50 -p compressibility=2 -p maxexecutiontime=120 -threads 64 -p operationcount=40000000 -p recordcount=20000000 -p requestdistribution=zipfian -p readproportion=1.0 -p updateproportion=0.0
```

Run the 90/10 test:

```console
./bin/ycsb run mongodb -s  -P workloads/workloadb  -p mongodb.url=mongodb://localhost:27017 -p minfieldlength=50 -p compressibility=2 -p maxexecutiontime=120 -threads 64 -p operationcount=40000000 -p recordcount=20000000  -p requestdistribution=zipfian -p readproportion=0.90 -p updateproportion=0.10
```

## Other tests

For instructions on running any other tests or more details on the metrics reported, refer to the [GitHub project for the YCSB.](https://github.com/brianfrankcooper/YCSB/wiki/).

