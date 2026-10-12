---
title: Understand the staged Ceph topology
description: Review how the example grows from a one-node learning cluster into a three-node replicated cluster.
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Understand the Ceph deployment

In this section, you will learn the role of each VM and how the Ceph cluster grows from one storage node to three. This topology supports the exercises that follow: using Ceph storage as a Linux block device and testing access during an object storage daemon (OSD) outage.

## Review the software versions

This example uses three Ubuntu 26.04 Arm64 virtual machines on an Arm AGI CPU host running Ubuntu 24.04. The VMs run Ceph Squid 19.2.6. The tested guest image uses Ubuntu 26.04.1 with kernel `7.0.0-34-generic`. Cluster commands and RADOS Block Device (RBD) mapping use the pinned Ceph container image, and cluster setup uses standalone cephadm 19.2.6.

## Why start with one node

Ceph is a distributed storage system. A production deployment normally spreads services and data across independent physical hosts. In this example you will start with one virtual machine so that you can learn the main Ceph concepts before adding cluster membership and data replication.

Ceph RBD presents an image stored as objects in Ceph as a block device that a Linux client can format and mount.

The first stage contains these components on `ceph1`:

- A monitor (MON), which maintains the cluster map and membership
- A manager (MGR), which provides management and monitoring functions
- An object storage daemon (OSD), which stores data on an unused disk
- An RBD client, which maps the example image as a Linux block device

The tutorial initially sets only the example pool to one replica. A single replica provides no redundancy, but it lets the pool become usable with one OSD.

## How the cluster expands

You will then add `ceph2` and `ceph3`, including one OSD on each node. The completed topology is:

| Virtual machine | Ceph services | Data disk |
| --- | --- | --- |
| `ceph1` | MON, MGR, OSD, RBD client | `/dev/vdb` |
| `ceph2` | MON, OSD | `/dev/vdb` |
| `ceph3` | MON, OSD | `/dev/vdb` |

After all three OSDs are available, you will increase the RBD pool size to three, so Ceph keeps three copies of the pool's data. Ceph uses Controlled Replication Under Scalable Hashing (CRUSH) to decide which OSDs store those copies.

A CRUSH rule defines how to spread copies across the cluster. Its failure domain identifies the boundary that copies must be separated across, such as a host or a rack. This example uses `host`, so each copy goes to an OSD on a different VM: `ceph1`, `ceph2`, or `ceph3`. If one VM becomes unavailable, the other two still hold copies of the data.

{{% notice Note %}}
All three virtual machines run on one physical AGI CPU host. The completed exercise demonstrates Ceph node membership, replication, and OSD recovery, but it does not tolerate failure of the physical host. Use independent physical hosts, failure domains, networks, and power sources when designing a production cluster.
{{% /notice %}}

## What you've learned and what's next

You've learned how the one-node learning stage maps to the final three-node cluster. Next, you'll create the three Arm64 virtual machines on the AGI CPU host.
