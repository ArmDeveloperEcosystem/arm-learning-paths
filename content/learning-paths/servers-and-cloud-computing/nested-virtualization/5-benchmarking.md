---
title: Test nested virtualization overhead
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## How the virtualization layers are pinned

To measure the overhead of nested virtualization, you'll install and run a reference benchmark across the three layers: L0 (bare metal), the L1 guest VM, and the L2 guest VM. To make the test comparable and minimize interaction with other workloads running on the server, pin each system under test to a fixed set of host cores.

The following table shows how each system is pinned:

| System under test | vCPUs | Pinned to |
|-------------------|-------|-----------|
| Host (L0) benchmark | | Host cores 8-15 |
| L1 guest | 0-7 | Host cores 16-23 |
| L1 hypervisor | 0-15 | Host cores 24-39 |
| L2 guest | 0-7 | Hypervisor cores 8-15 (host cores 32-39) |

After the core pinning is in place and `sysbench` is installed on all systems under test, run the test. Verify that the correct cores run at 100% CPU for the duration of the test. Check the results to see how much virtualization passthrough affects performance. Apply this core pinning while the VMs are running by using the `--live` flag for `virsh`.

## Pin cores for the L1 guest and L1 hypervisor

Pin the cores for the L1 guest and L1 hypervisor:

```bash
 # Pin L1 guest to cores 16-23
 for i in $(seq 0 7); do
   sudo virsh vcpupin fedora-l1-guest $i $((i+16)) --config --live
 done
 sudo virsh emulatorpin fedora-l1-guest 16-23 --config --live

 # Pin L1 hypervisor to cores 24-39
 for i in $(seq 0 15); do
   sudo virsh vcpupin fedora-l1-hyper $i $((i+24)) --config --live
 done
 sudo virsh emulatorpin fedora-l1-hyper 24-39 --config --live
```

## Pin cores for the L2 guest

Log in to `fedora-l1-hyper` and pin the cores of `fedora-l2-guest` to cores 8-15:

```bash
 # On host:
 ssh -i ~/.ssh/guest_key fedora@${fedora-l1-hyper IP address}

 # Inside L1 hypervisor: pin L2 guest to vCPUs 8-15 
 for i in $(seq 0 7); do 
   sudo virsh vcpupin fedora-l2-guest $i $((i+8)) --config --live 
 done 
 sudo virsh emulatorpin fedora-l2-guest 8-15 --config --live 
```

## Verify the core pinning

Verify that the pinning is correct, replacing `<domain>` with the domain name for each of the VMs, such as `fedora-l1-guest`:

```bash
sudo virsh vcpuinfo <domain>
sudo virsh emulatorpin <domain>
```

## Install sysbench

Install the `sysbench` benchmarking tool on the host, the L1 guest VM, and the L2 guest VM:

```bash
sudo dnf install -y sysbench 
```

## Run the benchmark

Run the same benchmark test on each system under test. You can run the tests in three different terminals at the same time. The tests shouldn't significantly interfere with each other because they use different cores.

On the bare metal host, use `taskset` to bind the benchmark to physical cores 8 to 15:

```bash
taskset -c 8-15 sysbench cpu --cpu-max-prime=20000 --threads=8 --time=60 run 
```

On the L1 guest and the L2 guest VMs, run the benchmark without `taskset`, because you already pinned their virtual CPUs with `virsh`:

```bash
sysbench cpu --cpu-max-prime=20000 --threads=8 --time=60 run 
```

The following is an example of the output from a single run:

```output
sysbench 1.0.20 (using system LuaJIT 2.1.1761727121)

Running the test with following options:
Number of threads: 8
Initializing random number generator from current time


Prime numbers limit: 20000

Initializing worker threads...

Threads started!

CPU speed:
    events per second:  9693.21

General statistics:
    total time:                          60.0007s
    total number of events:              581607

Latency (ms):
         min:                                    0.82
         avg:                                    0.83
         max:                                    0.98
         95th percentile:                        0.83
         sum:                               479906.25

Threads fairness:
    events (avg/stddev):           72700.8750/20.69
    execution time (avg/stddev):   59.9883/0.00
```

### How to read the output

The following fields matter most for comparing the three layers:

- `events per second` under `CPU speed` is the throughput. Higher is better. This is the primary number to compare across bare metal, L1, and L2.
- The `Latency (ms)` block reports per-request latency. `min`, `avg`, and `95th percentile` describe typical responsiveness, while `max` captures the worst-case spike. Lower is better.
- `events (avg/stddev)` under `Threads fairness` shows how evenly work was spread across threads. The second number is the standard deviation. A smaller value means more even distribution.

### Record your results

Run the benchmark on each layer and record the values from your own output. 

To calculate the overhead for a layer, compare its events per second against the bare metal result:

```text
overhead = (bare_metal_events_per_second - layer_events_per_second) / bare_metal_events_per_second * 100
```

For example, if bare metal reports 9693 events per second and the L2 nested guest reports 9219 events per second, the overhead is `(9693 - 9219) / 9693 * 100`, or less than 5%.

Compare the events per second and latency values across the three layers to see how virtualization and nested virtualization affect your workload. The average and 95th percentile latencies are often close across all three layers, while the maximum latency tends to increase with each level of nesting.

{{% notice Note %}}
Results vary with the Arm server, CPU generation, kernel, and workload. Draw your conclusions from your own measurements rather than from any single reference figure. Nested virtualization support continues to improve, so newer Arm Neoverse generations typically show lower overhead than older ones. Focus on the relative difference between bare metal, L1, and L2 on your own hardware.
{{% /notice %}}

The following is an example set of results:

| Metric | Bare Metal | L1 KVM Guest | L2 Nested Guest |
| ------ | ---------- | ------------ | --------------- |
| Events per second | 2533.02 | 2525.84 | 2306.22 |
| Overhead versus bare metal | N/A | -0.3% | -8.9% |
| Min latency | 3.14ms | 3.15ms | 3.38ms |
| Avg latency | 3.16ms | 3.17ms | 3.47ms |
| Max latency | 9.16ms | 13.02ms | 19.72ms |
| 95th percentile | 3.13ms | 3.19ms | 3.55ms |
| Thread stddev | 52.18 | 41.46 | 73.47 |

## What you've accomplished

You've pinned CPU cores across all three layers and benchmarked them with `sysbench`.

You can now use the techniques described in the Learning Path to run VMs inside VMs on Arm for workload isolation, hypervisor development and testing, or running microVMs in cloud environments.
