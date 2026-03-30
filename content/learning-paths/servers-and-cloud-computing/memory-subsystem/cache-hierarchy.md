---
title: Understand the cache hierarchy
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Cache levels and performance clifs

Each memory access is satisfied by the closest level of the hierarchy that contains the requested data. If the data is not found in the private caches, the request falls through to the next cache level and eventually to DRAM. Each level trades capacity for speed: L1 is tiny but fast, L2 is larger but slower, and L3 (or a system-level cache) is the largest on-chip cache but has the highest latency. Understanding this hierarchy for your specific system tells you where performance "cliffs" will occur as your working set grows.

## Cache levels on Arm systems

Both Graviton systems use 4-way L1 caches with 64-byte lines and 8-way L2 caches, also with 64-byte lines. The key architectural differences are in L2 size and the last level cache size. If you investigate a variety of Arm Linux systems you will see many different cache sizes and configurations.

Graviton2 (Neoverse N1) has a 1 MB private L2 per core and a 32 MB shared L3 across all 64 cores. Graviton4 (Neoverse V2) doubles the L2 to 2 MB and has a 36 MB shared L3. The larger L2 on Neoverse V2 reduces traffic to the shared L3 and lowers contention in multi-threaded workloads, which is especially beneficial for workloads with per-thread working sets between 1 MB and 2 MB.

## Read cache properties from the kernel

You already saw the `sysfs` approach in the previous section. You can also create a structured summary across all cache levels.

Save the following script as `cache2.sh`:

```bash
for cpu in 0; do
  echo "=== CPU $cpu ==="
  for idx in /sys/devices/system/cpu/cpu${cpu}/cache/index*; do
    level=$(cat $idx/level)
    type=$(cat $idx/type)
    size=$(cat $idx/size)
    ways=$(cat $idx/ways_of_associativity)
    line=$(cat $idx/coherency_line_size)
    shared=$(cat $idx/shared_cpu_list)
    echo "  L${level} ${type}: ${size}, ${ways}-way, ${line}B line, shared with CPUs: ${shared}"
  done
done
```

Run the script on each instance.

```bash
bash ./cache2.sh
```

On Graviton2 the output is:

```output
=== CPU 0 ===
  L1 Data: 64K, 4-way, 64B line, shared with CPUs: 0
  L1 Instruction: 64K, 4-way, 64B line, shared with CPUs: 0
  L2 Unified: 1024K, 8-way, 64B line, shared with CPUs: 0
  L3 Unified: 32768K, 16-way, 64B line, shared with CPUs: 0-63
```

On Graviton4 the output is:

```output
=== CPU 0 ===
  L1 Data: 64K, 4-way, 64B line, shared with CPUs: 0
  L1 Instruction: 64K, 4-way, 64B line, shared with CPUs: 0
  L2 Unified: 2048K, 8-way, 64B line, shared with CPUs: 0
  L3 Unified: 36864K, 12-way, 64B line, shared with CPUs: 0-63
```

Pay attention to:
- **Associativity**: higher associativity reduces conflict misses but can increase access latency.
- **Line size**: almost universally 64 bytes on modern Arm server cores, which matters for stride-based benchmarks.
- **Shared CPU list**: tells you exactly which cores share each cache level.

## Key concepts to carry forward

The following concepts explain why latency plots have the shape they do, and are worth keeping in mind as you work through the benchmarks.

### Cache line and spatial locality

When you access a single byte, the hardware fetches an entire 64-byte cache line. Sequential access patterns benefit from this because nearby data is already cached. Random access patterns do not, because each access potentially fetches a new line.

### Associativity and conflict misses

A 4-way set associative cache can hold 4 lines that map to the same set. If your access pattern happens to map many addresses to the same set, lines get evicted even though the cache isn't full. This is less likely with randomized pointer-chase patterns, but can still occur depending on address distribution and cache indexing but worth understanding.

### Prefetching

Modern Arm cores have hardware prefetchers that detect sequential and strided access patterns. They pull data into the cache before the CPU requests it, which can mask latency for predictable patterns. The pointer-chase benchmark in the next section defeats prefetching by design, giving you the true hardware latency rather than the prefetcher-assisted latency.

### Why nanoseconds matter more than cycles

When comparing systems with different clock speeds, cycles are misleading. A 3 GHz core with 12-cycle L2 latency has 4 ns L2 access time, but a 2.8 GHz core with the same 12-cycle latency has 4.3 ns. When the goal is comparing systems, nanoseconds normalize the comparison.

## Cross-check with documentation

For Arm Neoverse cores, the Technical Reference Manuals (TRMs) list:
- Default and configurable cache sizes
- Associativity
- Prefetcher behavior
- Expected cycle-count latencies

Compare your `sysfs` findings with the TRM. If the sizes differ, the SoC vendor may have chosen a different configuration. Many Arm CPUs have multiple options for cache size. For example, Neoverse V2 allows L2 sizes of 1 MB or 2 MB, and the TRM documents both options.

{{% notice Tip %}}
Arm publishes TRMs on the [Arm Developer documentation portal](https://developer.arm.com/documentation/). Search for the specific core name (for example, "Neoverse N1 TRM" or "Neoverse V2 TRM") to find the detailed cache specifications.
{{% /notice %}}

## What you've accomplished and what's next

In this section you:
- Reviewed the cache hierarchy for Neoverse N1 (Graviton2) and Neoverse V2 (Graviton4)
- Learned the key concepts of cache lines, associativity, prefetching, and ns-vs-cycles that explain benchmark results
- Cross-checked kernel-reported values against Arm documentation

The next section uses the ASCT `latency-sweep` benchmark to measure the actual access latency at each level of the memory hierarchy.
