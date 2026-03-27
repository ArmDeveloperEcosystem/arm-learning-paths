---
title: Compare systems and draw conclusions
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Bringing it all together

You now have a complete set of memory subsystem measurements for each of your test systems. This section shows how to collect all results in one pass, compare systems using ASCT's built-in diff tool, and draw meaningful architectural conclusions.

## Collect all memory benchmarks in one command

Throughout the previous sections, you ran individual ASCT benchmarks. To characterize a new system from scratch, run all memory benchmarks at once.

Run all tests and save the results.

```bash
sudo asct run memory loaded-latency --output-dir results_$(hostname)
```

This runs `latency-sweep`, `bandwidth-sweep`, `idle-latency`, `peak-bandwidth`, `c2c-latency`, and `loaded-latency` in a single pass, saving all results and plots to the output directory. The directory name includes the hostname so you can easily identify which system produced the data.

## Compare systems with asct diff

ASCT includes a `diff` command that compares output directories from different runs. It loads the results from each directory, groups fields by benchmark, and reports percentage differences for measurements and raw values for system configuration.

After collecting results on both instances, copy the output directories to the same machine and run:

```bash
asct diff results_graviton2-c6g/ results_graviton4-c8g/
```

ASCT uses the first directory as the baseline. 

To specify a baseline explicitly:

```bash
asct diff results_graviton2-c6g/ --baseline results_graviton4-c8g/
```

### Save diff output

Save the comparison as CSV for further analysis:

```bash
asct diff results_graviton2-c6g/ results_graviton4-c8g/ --format=csv --output-dir comparison/ --benchmarks ^system-info
```

ASCT writes `diff.csv` to the output directory.

### Filter the comparison

You can also focus on specific benchmarks.

To compare only peak bandwidth and latency sweep:

```bash
asct diff results_graviton2-c6g/ results_graviton4-c8g/ --benchmarks peak-bandwidth latency-sweep
```

To compare everything except system-info:

```bash
asct diff results_graviton2-c6g/ results_graviton4-c8g/ --benchmarks ^system-info
```

Output is:

```output
,field,recipe,run,comparator,delta,delta_percent,baseline
0,loaded-latency.data.0.Bandwidth [GB/s],loaded-latency,results_graviton4-c8g,459.65,291.03,172.59%,168.62
1,loaded-latency.data.0.Loaded latency [ns],loaded-latency,results_graviton4-c8g,197.43,-146.73,-42.63%,344.16
2,loaded-latency.data.10.Bandwidth [GB/s],loaded-latency,results_graviton4-c8g,464.27,298.39,179.88%,165.88
3,loaded-latency.data.10.Loaded latency [ns],loaded-latency,results_graviton4-c8g,197.89,-97.42,-32.99%,295.31
4,loaded-latency.data.100.Bandwidth [GB/s],loaded-latency,results_graviton4-c8g,105.01,19.1,22.23%,85.91
5,loaded-latency.data.100.Loaded latency [ns],loaded-latency,results_graviton4-c8g,122.3,10.24,9.14%,112.06
6,loaded-latency.data.180.Bandwidth [GB/s],loaded-latency,results_graviton4-c8g,59.97,13.57,29.24%,46.41
7,loaded-latency.data.180.Loaded latency [ns],loaded-latency,results_graviton4-c8g,119.32,16.95,16.56%,102.37
8,loaded-latency.data.20.Bandwidth [GB/s],loaded-latency,results_graviton4-c8g,442.78,277.23,167.46%,165.55
9,loaded-latency.data.20.Loaded latency [ns],loaded-latency,results_graviton4-c8g,187.41,-106.88,-36.32%,294.3
10,loaded-latency.data.30.Bandwidth [GB/s],loaded-latency,results_graviton4-c8g,337.23,171.6,103.61%,165.63
11,loaded-latency.data.30.Loaded latency [ns],loaded-latency,results_graviton4-c8g,142.05,-143.66,-50.28%,285.7
12,loaded-latency.data.3000.Bandwidth [GB/s],loaded-latency,results_graviton4-c8g,3.7,1.09,41.78%,2.61
13,loaded-latency.data.3000.Loaded latency [ns],loaded-latency,results_graviton4-c8g,115.06,18.38,19.01%,96.67
14,loaded-latency.data.40.Bandwidth [GB/s],loaded-latency,results_graviton4-c8g,254.2,87.78,52.75%,166.42
15,loaded-latency.data.40.Loaded latency [ns],loaded-latency,results_graviton4-c8g,132.74,-144.33,-52.09%,277.06
16,loaded-latency.data.50.Bandwidth [GB/s],loaded-latency,results_graviton4-c8g,206.14,36.71,21.67%,169.43
17,loaded-latency.data.50.Loaded latency [ns],loaded-latency,results_graviton4-c8g,129.36,-136.83,-51.4%,266.19
18,loaded-latency.data.500.Bandwidth [GB/s],loaded-latency,results_graviton4-c8g,21.16,5.97,39.31%,15.19
19,loaded-latency.data.500.Loaded latency [ns],loaded-latency,results_graviton4-c8g,116.88,18.71,19.06%,98.17
20,loaded-latency.data.70.Bandwidth [GB/s],loaded-latency,results_graviton4-c8g,148.73,23.11,18.4%,125.62
21,loaded-latency.data.70.Loaded latency [ns],loaded-latency,results_graviton4-c8g,125.18,-9.19,-6.84%,134.36
22,loaded-latency.data.80.Bandwidth [GB/s],loaded-latency,results_graviton4-c8g,129.29,20.48,18.82%,108.81
23,loaded-latency.data.80.Loaded latency [ns],loaded-latency,results_graviton4-c8g,123.76,0.73,0.59%,123.03
24,loaded-latency.data.900.Bandwidth [GB/s],loaded-latency,results_graviton4-c8g,12.05,3.31,37.84%,8.75
25,loaded-latency.data.900.Loaded latency [ns],loaded-latency,results_graviton4-c8g,116.85,19.42,19.93%,97.42
26,c2c-latency.data.Local.max,c2c-latency,results_graviton4-c8g,25.94,-15.82,-37.88%,41.76
27,c2c-latency.data.Local.mean,c2c-latency,results_graviton4-c8g,25.8,-15.95,-38.2%,41.75
28,c2c-latency.data.Local.median,c2c-latency,results_graviton4-c8g,25.8,-15.95,-38.2%,41.75
29,c2c-latency.data.Local.min,c2c-latency,results_graviton4-c8g,25.66,-16.08,-38.52%,41.74
30,c2c-latency.data.Local.p99,c2c-latency,results_graviton4-c8g,25.94,-15.82,-37.88%,41.76
31,peak-bandwidth.data.1:1 Reads-Writes.Peak BW [GB/s],peak-bandwidth,results_graviton4-c8g,410.07,258.31,170.21%,151.76
32,peak-bandwidth.data.2:1 Rd-Wr (Non-Temporal).Peak BW [GB/s],peak-bandwidth,results_graviton4-c8g,402.26,added,N/A,<missing>
33,peak-bandwidth.data.2:1 Reads-Writes.Peak BW [GB/s],peak-bandwidth,results_graviton4-c8g,430.17,272.94,173.59%,157.23
34,peak-bandwidth.data.3:1 Reads-Writes.Peak BW [GB/s],peak-bandwidth,results_graviton4-c8g,434.75,273.81,170.13%,160.94
35,peak-bandwidth.data.All Reads.Peak BW [GB/s],peak-bandwidth,results_graviton4-c8g,465.55,295.83,174.3%,169.72
36,bandwidth-sweep.data.DRAM.Bandwidth [GB/s],bandwidth-sweep,results_graviton4-c8g,37.0,16.13,77.27%,20.88
37,bandwidth-sweep.data.L1.Bandwidth [GB/s],bandwidth-sweep,results_graviton4-c8g,321.05,161.7,101.47%,159.35
38,bandwidth-sweep.data.L2.Bandwidth [GB/s],bandwidth-sweep,results_graviton4-c8g,94.98,21.56,29.37%,73.41
39,bandwidth-sweep.data.L2.Datasize Used,bandwidth-sweep,results_graviton4-c8g,655360,360448.0,122.22%,294912
40,bandwidth-sweep.data.LLC.Bandwidth [GB/s],bandwidth-sweep,results_graviton4-c8g,79.63,43.86,122.61%,35.77
41,bandwidth-sweep.data.LLC.Datasize Used,bandwidth-sweep,results_graviton4-c8g,6291456,-11010048.0,-63.64%,17301504
42,cross-numa-bandwidth.data.Node 0.Node 0,cross-numa-bandwidth,results_graviton4-c8g,465.59,295.8,174.21%,169.79
43,latency-sweep.data.Latency [ns].DRAM,latency-sweep,results_graviton4-c8g,114.56,19.02,19.91%,95.54
44,latency-sweep.data.Latency [ns].L1,latency-sweep,results_graviton4-c8g,1.43,-0.17,-10.58%,1.61
45,latency-sweep.data.Latency [ns].L2,latency-sweep,results_graviton4-c8g,3.96,-1.46,-26.92%,5.42
46,latency-sweep.data.Latency [ns].LLC,latency-sweep,results_graviton4-c8g,21.84,-6.97,-24.2%,28.8
47,latency-sweep.data.Lower Bound.L2,latency-sweep,results_graviton4-c8g,262144,196608.0,300.0%,65536
48,latency-sweep.data.Lower Bound.LLC,latency-sweep,results_graviton4-c8g,4194304,3145728.0,300.0%,1048576
49,latency-sweep.data.Optimum Datasize.L2,latency-sweep,results_graviton4-c8g,655360,360448.0,122.22%,294912
50,latency-sweep.data.Optimum Datasize.LLC,latency-sweep,results_graviton4-c8g,6291456,-11010048.0,-63.64%,17301504
51,latency-sweep.data.Upper Bound.L2,latency-sweep,results_graviton4-c8g,1048576,524288.0,100.0%,524288
52,latency-sweep.data.Upper Bound.LLC,latency-sweep,results_graviton4-c8g,8388608,-25165824.0,-75.0%,33554432
53,idle-latency.data.Node 0.Node 0,idle-latency,results_graviton4-c8g,115.16,19.52,20.41%,95.64
```

## Organize your results

Collect the key measurements from each system into a comparison table:

| Metric | Graviton2 (Neoverse N1) | Graviton4 (Neoverse V2) | Graviton4 vs Graviton2 |
|--------|------------------------|------------------------|------------------------|
| L1D latency | 1.6 ns | 1.4 ns | 11% faster |
| L2 latency | 5.4 ns | 4.0 ns | 27% faster |
| LLC latency | 28.8 ns | 21.8 ns | 24% faster |
| DRAM latency (unloaded) | 95.5 ns | 114.6 ns | 20% slower |
| Core-to-core latency (local) | 41.8 ns | 25.8 ns | 38% faster |
| Loaded latency at idle (~3000 NOPs) | 96.7 ns | 115.1 ns | 19% slower |
| Loaded latency at saturation (0 NOPs) | 344.2 ns | 197.4 ns | 43% faster |
| L1 bandwidth (1 core) | 159.4 GB/s | 321.1 GB/s | 101% higher |
| L2 bandwidth (1 core) | 73.4 GB/s | 95.0 GB/s | 29% higher |
| LLC bandwidth (1 core) | 35.8 GB/s | 79.6 GB/s | 123% higher |
| DRAM bandwidth (1 core) | 20.9 GB/s | 37.0 GB/s | 77% higher |
| Peak bandwidth (all cores, all reads) | 169.7 GB/s | 465.6 GB/s | 174% higher |

## Analyze the differences

### Latency

The latency measurements from `latency-sweep` reveal how each generation's cache hierarchy performs:

- **L1 latency** is similar across both generations (1.6 ns vs 1.4 ns). L1 caches are designed for very low latency (typically a few cycles), so the small difference reflects clock speed rather than cache microarchitecture.
- **L2 latency** improves by 27% on Graviton4 (4.0 ns vs 5.4 ns). Neoverse V2 has a 2 MB private L2 compared to N1's 1 MB. Despite the larger size, V2's improved cache pipeline delivers lower latency.
- **LLC latency** improves by 24% on Graviton4 (21.8 ns vs 28.8 ns), despite the L3 being only slightly larger (36 MB vs 32 MB). This reflects microarchitectural improvements in the V2 cache interconnect.
- **DRAM latency** is higher on Graviton4 (114.6 ns vs 95.5 ns, +20%). DDR5 trades slightly higher access latency for significantly more bandwidth per channel compared to DDR4.

### Loaded latency

The `loaded-latency` results reveal the latency-bandwidth tradeoff:

- At low load (~3000 NOPs), latency matches the idle DRAM latency from `latency-sweep` (96.7 ns for Graviton2, 115.1 ns for Graviton4), confirming the two benchmarks are consistent.
- The knee on Graviton2 occurs between 70 and 50 NOPs, where latency nearly doubles from 134 ns to 266 ns. Beyond the knee, latency climbs to 344 ns at saturation.
- The knee on Graviton4 occurs between 30 and 20 NOPs, at a much higher bandwidth (~340 GB/s vs ~126 GB/s on Graviton2). Graviton4's latency plateaus around 190-198 ns at saturation rather than continuing to climb, suggesting the DDR5 memory controllers handle queue saturation more gracefully.
- Despite Graviton4's higher idle DRAM latency, its latency at saturation is 43% lower than Graviton2's (197 ns vs 344 ns), making it the better choice for workloads that operate near memory bandwidth limits.

### Bandwidth

Single-core bandwidth from `bandwidth-sweep` shows the throughput capacity at each cache level:

- **L1 bandwidth** doubles on Graviton4 (321 vs 159 GB/s, +101%). This likely reflects a combination of higher clock speed and microarchitectural throughput improvements in Neoverse V2.
- **L2 bandwidth** improves by 29% on Graviton4 (95 vs 73 GB/s), due to the wider L2 fill path and microarchitectural improvements in V2.
- **LLC bandwidth** more than doubles on Graviton4 (80 vs 36 GB/s, +123%), reflecting improvements in the interconnect and shared cache design.
- **DRAM bandwidth (single core)** improves by 77% on Graviton4 (37 vs 21 GB/s). V2 supports more outstanding memory requests than N1, and DDR5 provides more bandwidth per channel than DDR4.

Peak bandwidth from `peak-bandwidth` shows the system-level memory controller capacity:

- Graviton4 delivers 2.7x the peak all-reads bandwidth of Graviton2 (465.6 vs 169.7 GB/s). This is the most dramatic difference between the two generations.
- Compare the "All Reads" figure with the theoretical peak bandwidth from `asct system-info` to see how efficiently each system uses its available bandwidth. Well-configured systems typically achieve 85-95% of theoretical peak.

## Cross-validate your findings

The credibility of this type of analysis comes from cross-validation. Check that:

1. **Latency steps match cache sizes**: the `latency-sweep` boundaries should align with the cache sizes reported by `sysfs` and the TRM.
2. **Bandwidth plateaus match cache sizes**: the `bandwidth-sweep` should show transitions at the same data sizes that `latency-sweep` identified.
3. **Peak bandwidth matches documented limits**: compare the "All Reads" figure from `peak-bandwidth` against the theoretical peak from `asct system-info`. A well-configured system typically achieves 85-95% of theoretical peak.
4. **Idle loaded latency matches unloaded latency**: the lowest-load row from `loaded-latency` should be close to the DRAM latency from `latency-sweep`.
5. **Results are repeatable**: run each benchmark at least twice. If results vary by more than 5%, investigate sources of noise (CPU frequency scaling, background processes).

{{% notice Tip %}}
Disable CPU frequency scaling during benchmarks for more consistent results:
```bash
echo performance | sudo tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor
```
{{% /notice %}}

## Adapting this analysis to any Arm Linux system

The examples here used AWS Graviton instances, but the methodology works on any Arm Linux machine with a NUMA-enabled kernel. To adapt it:

1. **Install ASCT** on the target system following the [install guide](/install-guides/asct/).
2. **Run all memory benchmarks**: `sudo asct run memory loaded-latency --format=csv --output-dir results_$(hostname)`
3. **Compare with previous systems**: `asct diff results_new/ --baseline results_reference/`
4. **Cross-validate**: check that latency boundaries, bandwidth plateaus, and peak numbers are consistent with each other and with the hardware documentation.


## What you've accomplished

In this section you:
- Identified the topology and cache hierarchy of Arm Linux systems using `sysfs` and `asct system-info`
- Measured cache and memory latency with the ASCT `latency-sweep` benchmark
- Measured single-core streaming bandwidth with `bandwidth-sweep`
- Measured peak system bandwidth with `peak-bandwidth` and the latency-bandwidth tradeoff with `loaded-latency`
- Compared Graviton2 and Graviton4 to understand how generational improvements in core microarchitecture and memory technology affect real-world performance
- Developed a portable methodology that works on any Arm Linux system with a single command
