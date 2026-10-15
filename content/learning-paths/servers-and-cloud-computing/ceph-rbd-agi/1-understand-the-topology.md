---
title: Understand the staged Ceph topology
description: Review how the example grows from a one-node learning cluster into a three-node replicated cluster.
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Understand the Ceph deployment

Ceph is a distributed storage system that keeps multiple copies of your data across independent nodes. You'll build a Ceph cluster on an Arm AGI CPU host, use it as a Linux block device, and watch it protect your data when a node's storage daemon goes down. You'll begin with one node to learn the core concepts, then expand to a three-node replicated cluster.

## What is Ceph RBD?

RADOS Block Device (RBD) exposes Ceph storage as a virtual block device, a volume that behaves like a local disk. Ceph splits the volume into objects and spreads them across the cluster, but to Linux it looks like an ordinary device at a path such as `/dev/rbd0`. You can format it with a filesystem, mount it, and read and write files normally, while Ceph handles replication and distribution across the nodes.

## Review the software versions

The example uses three Ubuntu 26.04 virtual machines on an Arm AGI CPU host running Ubuntu 24.04. The VMs run Ceph Squid 19.2.6. The tested guest image uses Ubuntu 26.04.1 with kernel `7.0.0-34-generic`. Cluster commands and RBD mapping use the pinned Ceph container image, and cluster setup uses standalone cephadm 19.2.6.

## Start with one node

A production deployment normally spreads services and data across independent physical hosts. In this example you will start with one virtual machine so that you can learn the main Ceph concepts before adding cluster membership and data replication.

The first stage configures these components on a virtual machine named `ceph1`:

- A monitor (MON), which maintains the cluster map and membership
- A manager (MGR), which provides management and monitoring functions
- An object storage daemon (OSD), which stores data on an unused disk
- An RBD client, which maps the example image as a Linux block device

The initial configuration sets the example pool to one replica. A single replica provides no redundancy, but it lets the pool become usable with one OSD.

## Expanding the cluster

You will then add virtual machines named `ceph2` and `ceph3`, including one OSD on each node. The completed topology is:

| Virtual machine | Ceph services | Data disk |
| --- | --- | --- |
| `ceph1` | MON, MGR, OSD, RBD client | `/dev/vdb` |
| `ceph2` | MON, OSD | `/dev/vdb` |
| `ceph3` | MON, OSD | `/dev/vdb` |

After all three OSDs are available, you will increase the RBD pool size to three, so Ceph keeps three copies of the pool's data. Ceph uses Controlled Replication Under Scalable Hashing (CRUSH) to decide which OSDs store those copies.

A CRUSH rule defines how to spread copies across the cluster. Its failure domain identifies the boundary that copies must be separated across, such as a host or a rack. This example uses `host`, so each copy goes to an OSD on a different VM: `ceph1`, `ceph2`, or `ceph3`. If one VM becomes unavailable, the other two still hold copies of the data.

{{% notice Note %}}
All three virtual machines run on one physical AGI CPU host. This demonstrates Ceph node membership, replication, and OSD recovery, but it does not tolerate failure of the physical host. Use independent physical hosts, failure domains, networks, and power sources when designing a production cluster.
{{% /notice %}}

## What you've learned and what's next

You now understand the services each node runs to build a distributed storage system across multiple nodes. Next, you'll create the three virtual machines on the AGI CPU host.
