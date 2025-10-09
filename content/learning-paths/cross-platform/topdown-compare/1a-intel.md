---
title: "Understand Intel x86 multi-level hierarchical top-down analysis"
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Configure slot-based accounting with Intel x86 PMU counters

Intel uses a slot-based accounting model where each CPU cycle provides multiple issue slots. A slot is a hardware resource needed to process micro-operations (uops). More slots means more work can be done per cycle. The number of slots depends on the microarchitecture design, but current Intel processor designs typically have four issue slots per cycle.

Intel's methodology uses a multi-level hierarchy that typically extends to 3-4 levels of detail. Each level provides progressively more granular analysis, allowing you to drill down from high-level categories to specific microarchitecture events.

## Level 1: Identify top-level performance categories

At Level 1, all pipeline slots are attributed to one of four categories, providing a high-level view of whether the CPU is doing useful work or stalling.

- Retiring = `UOPS_RETIRED.RETIRE_SLOTS / SLOTS`
- Bad Speculation = `(UOPS_ISSUED.ANY - UOPS_RETIRED.RETIRE_SLOTS + N * RECOVERY_CYCLES) / SLOTS`
- Frontend Bound = `IDQ_UOPS_NOT_DELIVERED.CORE / SLOTS`
- Backend Bound = `1 - (Frontend + Bad Spec + Retiring)`

Where `SLOTS = 4 * CPU_CLK_UNHALTED.THREAD` on most Intel cores.

## Level 2: Analyze broader bottleneck causes

Once you've identified the dominant Level 1 category, Level 2 drills into each area to identify broader causes. This level distinguishes between frontend latency and bandwidth limits, or between memory and core execution stalls in the backend.

- Frontend Bound covers frontend latency compared with frontend bandwidth
- Backend Bound covers memory bound compared with core bound
- Bad Speculation covers branch mispredicts compared with machine clears
- Retiring covers base compared with microcode sequencer

## Level 3: Target specific microarchitecture bottlenecks

After identifying broader cause categories in Level 2, Level 3 provides fine-grained attribution that pinpoints specific bottlenecks like DRAM latency, cache misses, or port contention. This precision makes it possible to identify the exact root cause and apply targeted optimizations. 

Memory Bound expands into detailed cache hierarchy analysis including L1 Bound, L2 Bound, L3 Bound, DRAM Bound, and Store Bound categories. Core Bound breaks down into execution unit constraints such as Divider and Ports Utilization, along with many other specific microarchitecture-level categories that enable precise performance tuning.

## Level 4: Access specific PMU counter events

Level 4 provides direct access to the specific microarchitecture events that cause the inefficiencies. At this level, you work directly with raw PMU counter values to understand the underlying hardware behavior causing performance bottlenecks. This enables precise tuning by identifying exactly which execution units, cache levels, or pipeline stages are limiting performance, allowing you to apply targeted code optimizations or hardware configuration changes. 

## Apply essential Intel x86 PMU counters for analysis

Intel processors expose hundreds of performance events, but top-down analysis relies on a core set of counters that map directly to the four-level hierarchy:

| Event Name                                      | Purpose                                                                              |
| :---------------------------------------------- | :----------------------------------------------------------------------------------- |
| `UOPS_RETIRED.RETIRE_SLOTS`                     | Count retired micro-operations (Retiring)                                            |
| `UOPS_ISSUED.ANY`                               | Count issued micro-operations (helps quantify Bad Speculation)                       |
| `IDQ_UOPS_NOT_DELIVERED.CORE`                   | Frontend delivery failures (Frontend Bound)                                          |
| `CPU_CLK_UNHALTED.THREAD`                       | Core clock cycles (baseline for normalization)                                       |
| `BR_MISP_RETIRED.ALL_BRANCHES`                  | Branch mispredictions (Bad Speculation detail)                                       |
| `MACHINE_CLEARS.COUNT`                          | Pipeline clears due to memory ordering or faults (Bad Speculation detail)            |
| `CYCLE_ACTIVITY.STALLS_TOTAL`                   | Total stall cycles (baseline for backend breakdown)                                  |
| `CYCLE_ACTIVITY.STALLS_MEM_ANY`                 | Aggregate stalls from memory hierarchy misses (Backend → Memory Bound)               |
| `CYCLE_ACTIVITY.STALLS_L1D_MISS`                | Stalls due to L1 data cache misses                                                   |
| `CYCLE_ACTIVITY.STALLS_L2_MISS`                 | Stalls waiting on L2 cache misses                                                    |
| `CYCLE_ACTIVITY.STALLS_L3_MISS`                 | Stalls waiting on last-level cache misses                                            |
| `MEM_LOAD_RETIRED.L1_HIT` / `L2_HIT` / `L3_HIT` | Track where loads are satisfied in the cache hierarchy                               |
| `MEM_LOAD_RETIRED.L3_MISS`                      | Loads missing LLC and going to memory                                                |
| `MEM_LOAD_RETIRED.DRAM_HIT`                     | Loads serviced by DRAM (DRAM Bound detail)                                           |
| `OFFCORE_RESPONSE.*`                            | Detailed classification of off-core responses (L3 vs. DRAM, local vs. remote socket) |


Using the above levels of metrics, you can determine which of the four top-level categories are causing bottlenecks.

