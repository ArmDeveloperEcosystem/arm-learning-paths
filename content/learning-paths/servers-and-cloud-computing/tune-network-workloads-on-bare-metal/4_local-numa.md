---
title: NUMA-based tuning
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Tune with local NUMA (Non-Uniform Memory Access)

In this section, you configure local NUMA and assess the performance uplift achieved through tuning. Cross‑NUMA data transfers generally incur higher latency than intra‑NUMA transfers, so Tomcat should be deployed on the NUMA node where the network interface resides to reduce cross‑node memory traffic and improve throughput and latency.

## Configure local NUMA

Check NUMA topology and relative latencies:

```bash
numactl -H
```

You should see that cross‑NUMA latency is higher than intra‑NUMA latency (for example, 10:100):

```output
available: 2 nodes (0-1)
node 0 cpus: 0 1 2 3 4 5 6 7
node 0 size: 193502 MB
node 0 free: 188478 MB
node 1 cpus:
node 1 size: 192625 MB
node 1 free: 192338 MB
node distances:
node   0   1
  0:  10  100
  1:  100  10
```

Identify the NUMA node for your network interface (using the `${net}` variable defined earlier):

```bash
cat /sys/class/net/${net}/device/numa_node
```

Example output (NIC on NUMA node 1):

```output
1
```

Allocate the eight reserved cores to the NIC's NUMA node (the example below keeps CPUs 96–103 online on node 1 and offlines the rest):

```bash
for no in {96..103}; do sudo bash -c "echo 1 > /sys/devices/system/cpu/cpu${no}/online"; done
for no in {0..95} {104..191}; do sudo bash -c "echo 0 > /sys/devices/system/cpu/cpu${no}/online"; done
```

Verify CPU online status and NUMA placement:

```bash
lscpu
```

You should see only CPUs 96–103 online on NUMA node 1:

```output
Architecture:                aarch64
  CPU op-mode(s):            64-bit
  Byte Order:                Little Endian
CPU(s):                      192
  On-line CPU(s) list:       96-103
  Off-line CPU(s) list:      0-95,104-191
Vendor ID:                   ARM
  Model name:                Neoverse-V2
...
NUMA:
  NUMA node(s):              2
  NUMA node0 CPU(s):
  NUMA node1 CPU(s):         96-103
...
```

## Validate performance after NUMA tuning

Restart Tomcat on the Arm Neoverse bare‑metal instance:

```bash
~/apache-tomcat-11.0.10/bin/shutdown.sh 2>/dev/null
ulimit -n 65535 && ~/apache-tomcat-11.0.10/bin/startup.sh
```

Run `wrk2` on the `x86_64` bare‑metal client to measure throughput and latency:

```bash
ulimit -n 65535 && wrk -c1280 -t128 -R500000 -d60 http://${tomcat_ip}:8080/examples/servlets/servlet/HelloWorldExample
```

Sample results after placing Tomcat on the NIC's local NUMA node:

```output
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     9.41s     4.71s   18.02s    61.07%
    Req/Sec     2.84k    76.55     3.06k    72.37%
  21814220 requests in 1.00m, 11.32GB read
Requests/sec: 363744.39
Transfer/sec:    193.22MB
```
