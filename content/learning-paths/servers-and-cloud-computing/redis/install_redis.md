---
# User change
title: "Install, configure and connect to Redis"

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---


##  Introduction to Redis
Redis, which stands for Remote Dictionary Server, is an open source, in-memory, key-value data store. Redis has a variety of data types, including bitmaps, hyperloglogs, geographic indexes, streams, lists, sets, and sorted sets with range queries.

### Before you begin

In this section you will learn about different options to install, configure and connect to your Redis server. If you already know how to deploy a Redis server, you can skip this learning path, and instead explore the [Learn how to Tune Redis](/learning-paths/servers-and-cloud-computing/redis_tune/) learning path. 

### Arm deployment options

There are numerous ways to deploy Redis on Arm: Bare metal, cloud VMs, or the various Redis services that cloud providers offer. If you already have an Arm system, you can skip over this subsection and continue reading.

* Arm Cloud VMs
  * [Get started with Arm-based cloud instances](/learning-paths/servers-and-cloud-computing/csp) learning path
  * [AWS EC2](https://aws.amazon.com/ec2/)
    * [Deploy Arm Instances on AWS using Terraform](/learning-paths/servers-and-cloud-computing/aws-terraform) learning path
  * [Azure VMs](https://azure.microsoft.com/en-us/products/virtual-machines/)
    * [Deploy Arm virtual machines on Azure with Terraform](/learning-paths/servers-and-cloud-computing/azure-terraform) learning path
  * [GCP Compute Engine](https://cloud.google.com/compute)
    * [Deploy Arm virtual machines on Google Cloud Platform (GCP) using Terraform](/learning-paths/servers-and-cloud-computing/gcp) learning path
  * [Oracle Cloud Infrastructure](https://www.oracle.com/cloud/)
* Redis services
  * [AWS MemoryDB or ElastiCache](https://aws.amazon.com/redis/)
    * Select an Arm based instance for deployment
* Additional options are listed in the [Get started with Servers and Cloud Computing](/learning-paths/servers-and-cloud-computing/intro) learning path

###  Redis documentation

Redis has a variety of use cases in large enterprise applications. You can explore the [Redis documentation](https://redis.io/docs/) for more details.

### Redis installation options

If you are using a cloud service like AWS MemoryDB or ElastiCache, then the installation of Redis is handled by that service. However, if you are working with a bare metal or cloud node, Redis is available to install on [Linux](https://redis.io/docs/latest/operate/oss_and_stack/install/archive/install-redis/install-redis-on-linux//), [macOS](https://redis.io/docs/latest/operate/oss_and_stack/install/archive/install-redis/install-redis-on-mac-os/), and [Windows](https://redis.io/docs/latest/operate/oss_and_stack/install/archive/install-redis/install-redis-on-windows/) through command line or you can download the latest Redis [binary](https://redis.io/docs/latest/operate/oss_and_stack/install/archive/install-redis/) for your target platform and build it from [source](https://redis.io/docs/latest/operate/oss_and_stack/install/archive/install-redis/install-redis-from-source/).
