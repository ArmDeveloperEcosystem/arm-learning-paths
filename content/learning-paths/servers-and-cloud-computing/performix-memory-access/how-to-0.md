---
title: Background
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Review of the CPU memory hierarchy

This Learning Path assumes you already understand memory hierarchy fundamentals. It is a recap, not an exhaustive explanation, and focuses on concepts used in the worked example.

Modern Arm server CPUs use a hierarchy of memories to reduce the cost of loading and storing data. The fastest storage sits close to each CPU core, while larger memories sit farther away and take more cycles to access.

You typically see:

- L1 data cache (`L1d`) and L1 instruction cache (`L1i`) close to each core with each access usually taking up to 10 cycles.
- L2 cache, often private to each core, with each access usually taking 10-20 cycles.
- Last-level cache, often shared across multiple cores, and usually taking 20+ cycles.
- DRAM, which is much larger but much slower than on-chip cache.

You can inspect cache topology on a Linux system with Arm's [sysreport](https://learn.arm.com/learning-paths/servers-and-cloud-computing/sysreport/) tool or the `lscpu` command. Unlike `lscpu`, Sysreport also reports the set associativity for each cache level. For example, you can run the following command on a system with `git` and `python` installed:

```output
git clone https://github.com/ArmDeveloperEcosystem/sysreport.git
python3 src/sysreport.py | grep -i cache -A 4

  cache info:          size, associativity, sharing
  cache line size:     64
  Caches:
    64 x L1D 64K 4-way 64b-line
    64 x L1I 64K 4-way 64b-line
    64 x L2U 1M 8-way 64b-line
    1 x L3U 32M 16-way 64b-line
```

For a more visual view, install `hwloc` and generate a topology image:

```bash
sudo apt update
sudo apt install -y hwloc
hwloc-ls --of png > topology.png
```

![Hardware locality topology for an Arm server showing per-core L1 and L2 caches and a shared L3 cache across all cores, which helps you verify cache hierarchy before profiling.#center](./topology.png "Example hardware locality topology")

The graphic above illustrates cache tiers on an AWS Graviton3 metal instance based on Neoverse V1. Each of the 64 cores has private `L1d`, `L1i`, and `L2` caches, and all cores share one `L3` cache, sometimes referred to as last-level cache (LLC). Cache sizes, especially at later levels, are not fixed by the Neoverse architecture; implementers such as AWS or Google can configure larger or smaller caches based on design goals.

NUMA, or non-uniform memory access, means memory latency can depend on which processor or socket owns the memory being accessed. On this AWS Graviton3 instance, there is only one NUMA node.

If you would like a comprehensive system-level understanding of the memory subsystem, review our learning path on the [Arm system characterisation tool](https://learn.arm.com/learning-paths/servers-and-cloud-computing/memory-subsystem/).

## Definition of terms used in this learning path

Applications use virtual addresses, which are the addresses a program sees instead of physical DRAM locations. Virtual addressing lets the operating system isolate processes, protect memory, and map each program's address space to available physical memory. The processor translates virtual addresses to physical addresses before it accesses memory.

### Translation lookaside buffer (TLB)

The translation lookaside buffer (TLB) caches recent virtual-to-physical translations at page granularity to avoid page table walks. A TLB miss occurs when the needed translation is not cached, so the processor performs a page table walk to find the mapping. Page walks add latency before a load or store can complete. Large working sets and irregular access patterns, such as strides larger than the typical 4KB page size, can increase TLB pressure because the program touches many pages with little reuse.

### Page Faults

A minor page fault is usually harmless: the data is already in RAM, and the kernel only creates the mapping. This commonly happens during anonymous paging when Linux lazily backs newly allocated heap or stack memory on first touch. A major page fault is more expensive because the kernel must fetch the page from disk, such as from a file or swap, so repeated major faults are usually a real performance concern.

### Working set size

The working set is the data your program actively touches during a period of execution. It differs from resident set size (RSS), which is the amount of physical memory currently resident for a process. A process can have a large RSS while the hot loop actively uses only a smaller working set.

### Memory access from a programmers perspective

From a programmer's perspective, much of the cache and memory subsystem is a black box defined by processor architecture and implementation. Features such as cache associativity, prefetching, and translation caching are designed to hide latency across many workloads. Your main software levers are data structure layout, allocation patterns, and choices such as page size. The layout of your C++ data structures can determine whether the memory hierarchy helps or hurts runtime. The compiler generally cannot reorder structure fields or split objects automatically because that would change program semantics.

