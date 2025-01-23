---
title: "Kernel, compiler, and OpenSSL settings"
weight: 2
layout: "learningpathall"
---

In this section you can get an overview of the linux kernel, compiler and OpenSSL settings that impact the performance of Redis.

##  Kernel configuration

The profile of requests made by clients will differ based on the use case. This means there is no one size fits all set of tuning parameters for Redis. Use the information below as general guidance to tune Redis.

### Memory Management

The memory related kernel parameters can be changed either temporarily through the `/proc` file system or permanently using the `sysctl` command.
To improve memory utilization on your system, use the following commands:

```console
sudo echo 'vm.overcommit_memory = 1' >> /etc/sysctl.conf 
sudo echo 'vm.swappiness=1' >> /etc/sysctl.conf 
```
Understand the parameters:

* `vm.overcommit_memory`:
  * Enabling overcommit_memory to avoid out of memory space issues. If the overcommit memory value is 0 then there is chance that Redis will get an OOM (out of memory) error.  
* `vm.swappiness`:
  * When the Redis server consuming high memory, configuring the swappiness to its lowest value could be helpful. 

### Transparent Huge Page

Redis by default will disable transparent huge page (THP) if it is enabled for Redis process to avoid latency problems. You should disable this parameter in case this config has no effect.

The command to disable this setting is shown below:

```console
sudo echo never > /sys/kernel/mm/transparent_hugepage/enabled  
```

### Linux Network Stack

The Linux Network stack settings can be changed in the `/etc/sysctl.conf` file, or by using the `sysctl` command.

Documentation on each of the parameters discussed below can be found in the [admin-guide](https://github.com/torvalds/linux/blob/master/Documentation/admin-guide/sysctl/net.rst) and [networking](https://github.com/torvalds/linux/blob/master/Documentation/networking/ip-sysctl.rst) documentation within the Linux source.

Run the command below to list all kernel parameters.

```bash
sudo sysctl -a
```

Shown below are the network stack settings used for performance testing.

```console
sudo sysctl -w net.core.somaxconn=65535
sudo sysctl -w net.ipv4.tcp_max_syn_backlog=65535

```

These settings open up the network stack to make sure it is not a bottleneck.

* `net.core.somaxconn`:
  * This setting is used to select the maximum number of connections the kernel will allow.
  * If the Redis server is expected to support a large number of clients, it may be helpful to increase this parameter.
  * A value of 65535 is probably excessively large for production. In practice, this just needs to be large enough to support the peak number of connections that will be made.
* `net.ipv4.tcp_max_syn_backlog`:
  * This setting is used to select the maximum number of connection requests that are pending but not established yet.
  * A value of 65535 is probably excessively large for production. In practice, this just needs to be large enough to support the peak number of connection requests that will be made.


##  Compiler Considerations

The easiest way to gain performance is to use the latest version of GCC. Aside from that, the flag `-mcpu` and `-flto` can be used to potentially gain additional performance. Usage of these flags is explained in the [Migrating C/C++ applications](/learning-paths/servers-and-cloud-computing/migration/c/) section of the [Migrating applications to Arm servers](/learning-paths/servers-and-cloud-computing/migration/) learning path.

If you need to understand how to configure a build of Redis. Please review the [build Redis from source](https://redis.io/docs/getting-started/installation/install-redis-from-source/).

##  OpenSSL Considerations

Redis relies on [OpenSSL](https://www.openssl.org/) for cryptographic operations. Thus, the version of OpenSSL used with Redis (and the GCC version and switches used to compile it) can impact performance. Typically using the Linux distribution default version of OpenSSL is sufficient.

However, it is possible to use newer versions of OpenSSL which could yield performance improvements. This is achieved by using the `--with-openssl` switch when configuring the Redis build. Point this switch to the directory that contains the source code of the version of OpenSSL you'd like to have Redis link to. The Redis build system takes care of the rest. There is also a `--with-openssl-opt` switch which allows you to add options to the build for OpenSSL.

