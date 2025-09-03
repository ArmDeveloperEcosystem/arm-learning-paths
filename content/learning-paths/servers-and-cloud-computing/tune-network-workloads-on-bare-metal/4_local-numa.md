---
title: NUMA-based Tuning
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Tuning via local (Non-Uniform Memory Access) NUMA
In this section you will learn how to configure local NUMA and assess performance uplift acheieved through tuning.

Typically, cross-NUMA data transfers within the CPU incur higher latency than intra-NUMA transfers. Therefore, Tomcat should be deployed on the NUMA node where the network interface resides.

### Setting local NUMA

1. Use the following command to check that the latency for cross-NUMA transfers is greater than the latency for intra-NUMA transfers:
```bash
numactl -H
```

It can be observed that the cross-NUMA latency to intra-NUMA latency ratio is 10:100.
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

2. Use the following command to check the NUMA node where the ${net} network interface resides.
```bash
cat /sys/class/net/${net}/device/numa_node
```
You will notice that the NUMA node where the ${net} network interface resides is 1.
```output
1
```

3. As a result, allocate the reserved 8 cores to NUMA node 1.
```bash
for no in {96..103}; do sudo bash -c "echo 1 > /sys/devices/system/cpu/cpu${no}/online"; done
for no in {0..95} {104..191}; do sudo bash -c "echo 0 > /sys/devices/system/cpu/cpu${no}/online"; done
```

4. Verify whether the settings have been successfully applied.
```bash
lscpu
```

From the output you will see that the only online CPUs are 72-79 on NUMA node 1.
```bash
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

### The result after tuning local NUMA

1. Shutdown and start Tomcat on the Arm Neoverse bare-metal instance:
```bash
~/apache-tomcat-11.0.10/bin/shutdown.sh 2>/dev/null
ulimit -n 65535 && ~/apache-tomcat-11.0.10/bin/startup.sh
```

2. Run `wrk2` on the `x86_64` bare-metal instance:
```bash
ulimit -n 65535 && wrk -c1280 -t128 -R500000 -d60 http://${tomcat_ip}:8080/examples/servlets/servlet/HelloWorldExample
```

The result after configuring NUMA node should look like:
```output
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     9.41s     4.71s   18.02s    61.07%
    Req/Sec     2.84k    76.55     3.06k    72.37%
  21814220 requests in 1.00m, 11.32GB read
Requests/sec: 363744.39
Transfer/sec:    193.22MB
```
