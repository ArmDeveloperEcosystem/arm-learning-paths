---
# User change
title: "Creating MongoDB test scenarios"

weight: 3 # (intro is 1), 2 is first, 3 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
## MongoDB test scenarios
To test Mongodb you need two parts. A instance running the testing software([YCSB](/learning-paths/servers-and-cloud-computing/mongodb/benchmark_mongodb-8.0)). one or more instances running MongoDB in some configuration. The recommended MongoDB test setup is a three node relica set. These three nodes are of equal size with one instance being desigated as the primary node( the target for test traffic ) and the others as secondary nodes.

## What is a replica set?

A replica set is a group of instances that maintain the same dataset. A replica set contains many nodes, but three nodes are the most common for testing.

## What node size should I use?

The most common size for testing MongoDB is an 8 vCPU instance. You can test with any sized instance, but if you are looking for ideal testing conditions, 8 vCPUs is enough. Each node should have atleast 32GB of RAM.

To achieve the best results, its recommended to keep the complete data set in memory. If you see disk access when running tests, increase the RAM size of your instances. Additional details about the recommended configuration are provided below.

## Creating replica sets

You can create replica sets of any size(two is the minimum). Three is recemmended but you can add as many as you like.

## Three node replica sets

To creating a three node replica set, start by launching three [Arm based instance](/learning-paths/servers-and-cloud-computing/csp/) of equal size.

[install](/learning-paths/servers-and-cloud-computing/mongodb/run_mongodb) Mongodb on all three instances.

Once all three instances are up and running. Modify the service and configuration file for all instances.

## Modify the MongoDB configuration

Use a text editor to edit the file `/etc/mongodb.conf` and replace the contents of the file with the text below.

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

**Details of what all these mean is below:**

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

Run this command to reload the new configurtion.

```
sudo service mongod restart
```

## Modify the MongoDB service

Use a text editor to edit the file `/etc/systemd/system/mongod.service` and replace the contents of the file with the text below.

```
[Unit]
Description=High-performance, schema-free document-oriented database
After=network.target
Documentation=https://docs.mongodb.org/manual

[Service]
User=mongodb
Group=mongodb
ExecStart=/usr/bin/mongod --quiet --config /etc/mongod.conf

# Recommended limits for for mongod as specified in
# https://docs.mongodb.com/manual/reference/ulimit/#recommended-ulimit-settings
# (file size)
LimitFSIZE=infinity
# (cpu time)
LimitCPU=infinity
# (virtual memory size)
LimitAS=infinity
# (locked-in-memory size)
LimitMEMLOCK=infinity
# (open files)
LimitNOFILE=64000
# (processes/threads)
LimitNPROC=64000

[Install]
WantedBy=multi-user.target
```

details on these can be found here: https://docs.mongodb.com/manual/reference/ulimit/#recommended-ulimit-settings

Run this command to reload the service.

```
sudo ystemctl daemon-reload
```

**Once all three instances are created and have mongodb installed, select one to be your primary node. The remaining instances will be secondary nodes.**

## Initialize the replica set

Connect to the primary node and run the following commands below.

1. Set variables with the IP addresses of each node:

    ```bash
    PRIMARY_NODE_IP="<primary-node-ip>"
    SECONDARY_NODE1_IP="<secondary-node1-ip>"
    SECONDARY_NODE2_IP="<secondary-node2-ip>"
    ```

2. Initialize the replica set with the following command:

    ```
    mongosh --host $PRIMARY_NODE_IP:27017 <<EOF
    rs.initiate({
      _id: "rs0",
      members: [
        { _id: 0, host: "$PRIMARY_NODE_IP:27017", priority: 2, votes: 1 },
        { _id: 1, host: "$SECONDARY_NODE1_IP:27017", priority: 1, votes: 1 },
        { _id: 2, host: "$SECONDARY_NODE2_IP:27017", priority: 1, votes: 1 }
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