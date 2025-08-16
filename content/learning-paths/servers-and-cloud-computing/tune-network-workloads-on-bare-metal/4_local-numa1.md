---
title: Tuning via local NUMA
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Tuning via local NUMA
- Setting local NUMA
- The result after tuning local NUMA

Typically, cross-NUMA data transfers within the CPU incur higher latency than intra-NUMA transfers. Therefore, Tomcat should be deployed on the NUMA node where the network interface resides.

### Setting local NUMA

1. Use the following command to check that the latency for cross-NUMA transfers is greater than the latency for intra-NUMA transfers.
```bash
numactl -H
```

It can be observed that the cross-NUMA latency to intra-NUMA latency ratio is 10:40.
```bash
available: 2 nodes (0-1)
node 0 cpus: 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71
node 0 size: 483129 MB
node 0 free: 462395 MB
node 1 cpus: 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143
node 1 size: 481845 MB
node 1 free: 472013 MB
node distances:
node   0   1
  0:  10  40
  1:  40  10
```

2. Use the following command to check the NUMA node where the ${net} network interface resides.
```bash
cat /sys/class/net/${net}/device/numa_node
```
It can be observed that the NUMA node where the ${net} network interface resides is 1.
```bash
1
```

3. Therefore, allocate the reserved 8 cores to NUMA node 1.
```bash
for no in {72..79}; do sudo bash -c "echo 1 > /sys/devices/system/cpu/cpu${no}/online"; done
for no in {0..71} {80..143}; do sudo bash -c "echo 0 > /sys/devices/system/cpu/cpu${no}/online"; done
```

4. Verify whether the settings have been successfully applied.
```bash
lscpu
```

It can be observed that the only online CPUs are 72-79 on NUMA node 1.
```bash
Architecture:             aarch64
  CPU op-mode(s):         64-bit
  Byte Order:             Little Endian
CPU(s):                   144
  On-line CPU(s) list:    72-79
  Off-line CPU(s) list:   0-71,80-143
Vendor ID:                ARM
  Model name:             Neoverse-V2
...
NUMA:
  NUMA node(s):           2
  NUMA node0 CPU(s):
  NUMA node1 CPU(s):      72-79
...
```

### The result after tuning local NUMA

1. Use the following command on the Grace bare-metal where `Tomcat` is on
```bash
~/apache-tomcat-11.0.9/bin/shutdown.sh 2>/dev/null
ulimit -n 65535 && ~/apache-tomcat-11.0.9/bin/startup.sh
```

2. And use the following command on the `x86_64` bare-metal where `wrk2` is on
```bash
ulimit -n 65535 && wrk -c1280 -t128 -R500000 -d60 http://${tomcat_ip}:8080/examples/servlets/servlet/HelloWorldExample
```

The result after NUMA node tuned:
```bash
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    18.72s     7.76s   33.78s    57.93%
    Req/Sec     1.87k    59.38     2.08k    58.75%
  14111369 requests in 1.00m, 7.32GB read
  Socket errors: connect 0, read 0, write 0, timeout 64
Requests/sec: 235505.32
Transfer/sec:    125.10MB
```
