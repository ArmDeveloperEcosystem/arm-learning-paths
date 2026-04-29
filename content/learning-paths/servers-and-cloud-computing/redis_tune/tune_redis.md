---
title: "Tune Redis"
weight: 3
layout: "learningpathall"
---

## Redis Deployment Tuning

Optimizing Redis can improve performance without scaling your deployment up to larger machines or out to more nodes. The gained performance can be used directly, or traded for cost savings by reducing provisioned compute resources.

The profile of requests made by clients varies by use case, so there is no one-size-fits-all Redis configuration. Start with a small, explicit `redis.conf`, measure throughput, latency, memory use, and CPU use, then change one setting at a time.

If you do not already have a Redis server running, review [Learn how to deploy Redis on Arm](/learning-paths/servers-and-cloud-computing/redis/) and the [Configure Redis single-node](/learning-paths/servers-and-cloud-computing/redis/single-node_deployment/) section before applying these tuning settings.

For the complete list of Redis configuration directives, see the [Redis configuration documentation](https://redis.io/docs/latest/operate/oss_and_stack/management/config/) and the self-documented `redis.conf` file shipped with your Redis release.

## Baseline redis.conf

The following configuration is a good starting point for performance tuning on a dedicated Redis server. It includes performance-related settings and a small number of operational settings that make results easier to compare. Replace the placeholder values before applying the configuration.

Add these settings to the Redis configuration file used by your server, commonly `/etc/redis/redis.conf`. If Redis is managed by `systemd`, restart the service after editing the file:

```bash
sudo systemctl restart redis-server
```

If you start Redis manually, pass the configuration file path to `redis-server`:

```bash
redis-server /etc/redis/redis.conf
```

```console
################################## NETWORK #####################################

bind <server-private-ip>
protected-mode yes
port 6379
tcp-backlog 511
tcp-keepalive 300
timeout 0

################################## GENERAL #####################################

daemonize no
supervised no
databases 16

################################### CLIENTS ####################################

maxclients 10000

################################ SNAPSHOTTING ##################################

save ""
stop-writes-on-bgsave-error yes

################################ APPEND ONLY MODE ##############################

appendonly no
appendfsync everysec
no-appendfsync-on-rewrite no

############################### MEMORY MANAGEMENT ##############################

maxmemory <bytes>
maxmemory-policy noeviction
maxmemory-samples 5
lazyfree-lazy-eviction no
lazyfree-lazy-expire no
lazyfree-lazy-server-del no
replica-lazy-flush no
activedefrag no

################################ THREADED I/O ##################################

io-threads 1

################################### LATENCY ####################################

hz 10
dynamic-hz yes
```

## Configuration options

| Setting | Starting value | Why it matters and when to change it |
| --- | --- | --- |
| `bind` | Private server IP | Bind to the private or VPN interface used by benchmark clients. Use `0.0.0.0` only in isolated benchmark environments where clients may connect through multiple private interfaces and access to port `6379` is already restricted by network controls. |
| `protected-mode` | `yes` | Keep enabled by default. Set to `no` only for isolated benchmark networks where Redis access is already restricted by VPN, firewall rules, cloud security groups, or equivalent controls. |
| `port` | `6379` | Change only to avoid a port conflict or to run multiple Redis instances on the same host. |
| `tcp-backlog` | `511` | Increase for high connection churn. The Linux `net.core.somaxconn` value must be at least as large. |
| `tcp-keepalive` | `300` | Reduce when you need faster detection of dead TCP peers. Increase if idle connections are long lived and stable. |
| `timeout` | `0` | Keep `0` for benchmarks so idle clients are not disconnected. Set a finite value for production connection cleanup. |
| `supervised` | `no` | Use `systemd` when Redis is managed as a system service. Use `no` for manual foreground testing. |
| `databases` | `16` | Use the default unless the application requires fewer logical databases. Redis Cluster only uses database `0`. |
| `maxclients` | `10000` | Increase only if the workload needs more concurrent connections and the OS file descriptor limit has been raised. Lower it to fail early on small test systems. |
| `save` | `""` | Disables RDB snapshots. Use this for pure cache or throughput tests. Add snapshot intervals when restart recovery from disk is required. |
| `stop-writes-on-bgsave-error` | `yes` | Keep `yes` when RDB persistence is required and failed snapshots must stop writes. Use `no` only when monitoring catches persistence failures. |
| `appendonly` | `no` | Keep disabled for cache-style or maximum throughput tests. Enable AOF when durability is required. |
| `appendfsync` | `everysec` | Relevant only when `appendonly yes` is set. Use `always` for stronger durability with higher latency. Use `no` only when OS-managed flushing is acceptable. |
| `no-appendfsync-on-rewrite` | `no` | Relevant only with AOF. Use `yes` to reduce latency spikes during AOF rewrite at the cost of more data-loss exposure during the rewrite window. |
| `maxmemory` | Host-specific | Set this explicitly. Start at 70-80% of RAM on a dedicated Redis server, leaving memory for the OS, replicas, forked persistence, and client buffers. |
| `maxmemory-policy` | `noeviction` | Use `noeviction` for correctness testing because writes fail instead of silently evicting keys. Use `allkeys-lru` or `allkeys-lfu` for cache workloads. Use `volatile-*` policies only when the application reliably sets TTLs. |
| `maxmemory-samples` | `5` | Increase to improve LRU/LFU eviction accuracy with more CPU cost. Leave unchanged for a first test. |
| `lazyfree-lazy-eviction` | `no` | Enable when eviction of large values causes latency spikes. Background freeing can increase memory pressure temporarily. |
| `lazyfree-lazy-expire` | `no` | Enable when expiration of large values causes latency spikes. |
| `lazyfree-lazy-server-del` | `no` | Enable when commands that replace or delete large values, such as `DEL`, `RENAME`, or writes over existing keys, cause latency spikes. |
| `replica-lazy-flush` | `no` | Enable on replicas when full resynchronization or flush operations create latency spikes. |
| `activedefrag` | `no` | Enable for long-running write-heavy workloads with high memory fragmentation. Keep disabled for first-pass throughput tests because it consumes CPU. |
| `io-threads` | `1` | `1` uses the main thread only, which is the standard starting point. Increase only when Redis is CPU-bound on network I/O, the server has at least four cores, and the workload benefits in measurement. Redis 8 uses I/O threads for reads and writes when this is enabled. |
| `hz` | `10` | Increase only when background maintenance, key expiration, or client timeout responsiveness is too slow. Higher values use more CPU. |
| `dynamic-hz` | `yes` | Keep enabled so Redis can adjust background task frequency as client count changes. |

## Client-side pipelining

Test client-side pipelining separately from Redis I/O threads. Pipelining reduces round-trip and socket syscall overhead, and is often the simplest way to increase throughput from benchmark clients such as [memtier_benchmark](https://github.com/RedisLabs/memtier_benchmark). I/O threads are a server-side option for workloads limited by Redis network I/O.

Start with pipeline depth `1`, then test values such as `4`, `8`, `16`, and `32`. Larger pipeline depths can increase throughput, but they also increase tail latency and client-side memory use.
