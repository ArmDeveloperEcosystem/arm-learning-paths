---
title: "Kernel, compiler, and OpenSSL settings"
weight: 2
layout: "learningpathall"
---

This section gives an overview of Linux kernel, compiler, and OpenSSL settings that can impact Redis performance.

## Kernel Configuration

The request profile varies by use case, so there is no one-size-fits-all set of tuning parameters for Redis. Use the information below as a starting point, then measure the impact for your workload.

### Memory Management

Memory-related kernel parameters can be changed temporarily with `sysctl -w` or made persistent by adding them to a file under `/etc/sysctl.d/`.

Use the following commands to apply the settings immediately:

```console
sudo sysctl -w vm.overcommit_memory=1
sudo sysctl -w vm.swappiness=1
```

To make the settings persistent across reboots, create a Redis-specific sysctl file:

```console
printf "vm.overcommit_memory = 1\nvm.swappiness = 1\n" | sudo tee /etc/sysctl.d/99-redis.conf
sudo sysctl --system
```

`vm.overcommit_memory` should be set to `1` so Redis background save and rewrite operations are less likely to fail during `fork()`.

`vm.swappiness` controls how aggressively Linux swaps memory pages. A low value helps reduce Redis latency caused by paging under memory pressure.

### Transparent Huge Page

Transparent Huge Pages (THP) can increase Redis latency and memory use, especially when Redis forks for RDB snapshots or AOF rewrite. Disable THP at the kernel level on systems used for Redis performance tuning.

Check the current THP setting:

```console
cat /sys/kernel/mm/transparent_hugepage/enabled
```

Disable THP until the next reboot:

```console
echo never | sudo tee /sys/kernel/mm/transparent_hugepage/enabled
```

### Linux Network Stack

Linux network stack settings can be changed temporarily with `sysctl -w` or made persistent by adding them to a file under `/etc/sysctl.d/`.

Documentation on each of the parameters discussed below can be found in the [admin-guide](https://github.com/torvalds/linux/blob/master/Documentation/admin-guide/sysctl/net.rst) and [networking](https://github.com/torvalds/linux/blob/master/Documentation/networking/ip-sysctl.rst) documentation within the Linux source.

Run the command below to list all kernel parameters.

```bash
sudo sysctl -a
```

Shown below are network stack settings used for Redis performance tuning.

```console
sudo sysctl -w net.core.somaxconn=65535
sudo sysctl -w net.ipv4.tcp_max_syn_backlog=65535
```

These settings raise connection queue limits so the kernel is less likely to be the bottleneck during high connection churn.

* `net.core.somaxconn`:
  * This setting controls the maximum listen backlog the kernel allows.
  * If the Redis server is expected to support a large number of clients, it may be helpful to increase this parameter.
  * The value should be at least as large as the Redis `tcp-backlog` setting.
  * A value of 65535 is probably too large for production. In practice, this only needs to support the expected peak connection backlog.
* `net.ipv4.tcp_max_syn_backlog`:
  * This setting controls the maximum number of connection requests that are pending but not established.
  * A value of 65535 is probably too large for production. In practice, this only needs to support the expected peak rate of new connection attempts.


## Compiler Considerations

If you build Redis from source, use a recent GCC version from your Linux distribution. Compiler flags such as `-mcpu` and `-flto` can change performance, but they should be tested against your workload before use. Usage of these flags is explained in the [Migrating C/C++ applications](/learning-paths/servers-and-cloud-computing/migration/c/) section of the [Migrating applications to Arm servers](/learning-paths/servers-and-cloud-computing/migration/) learning path.

For Redis build instructions, review the [build Redis from source](https://redis.io/docs/latest/operate/oss_and_stack/install/archive/install-redis/install-redis-from-source/) documentation.

## OpenSSL Considerations

Redis uses [OpenSSL](https://www.openssl.org/) for TLS. TLS adds encryption and integrity-check overhead, so it can reduce the maximum throughput of a Redis instance. Typically, the Linux distribution default OpenSSL version is sufficient.

To build Redis with TLS support, install the OpenSSL development libraries for your distribution and build Redis with:

```console
make BUILD_TLS=yes
```

Only test a newer OpenSSL version if TLS is part of the workload. If clients connect without TLS, OpenSSL does not affect Redis command throughput.
