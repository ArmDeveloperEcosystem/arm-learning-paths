---
# User change
title: "MongoDB test configuration and setup"

draft: true

weight: 30 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

The most popular test setup for real world testing is a replica set. A replica set of three equal sized nodes is created and initiated.

## What is a replica Set?

A replica set is a group of instances that maintain the same data set. A replica set contains many nodes, and in this test it is 3 nodes. Of the 3 nodes, one node is the primary node, while the other nodes are secondary nodes.

## What node size should I use?

The most common size for testing MongoDB is an 8 vCPU instance. You can test with any sized machine, but if you are looking for ideal testing conditions 8 nodes is enough. Each node should have 32GB of RAM.

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

**setParameter:** Additional options
- **diagnosticDataCollectionDirectorySizeMB:** 400 is based on the docs.
- **honorSystemUmask:** Sets read and write permissions only to the owner of new files
- **lockCodeSegmentsInMemory:** Locks code into memory and prevents it from being swapped.
- **suppressNoTLSPeerCertificateWarning:** allows clients to connect without a certificate. (Only for testing purposes)
- **tlsWithholdClientCertificate:** Will not send the certification during communication. (Only for testing purposes)

If you would like to use encryption you will need to add the security and keyFile to your configuration. As well as change some of the parameters in the mongod.conf.