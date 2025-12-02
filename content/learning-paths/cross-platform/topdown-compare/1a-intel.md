---
title: "Understand Intel x86 multilevel hierarchical top-down analysis"
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Configure slot-based accounting with Intel x86 PMU counters

Intel uses a slot-based accounting model, where each CPU cycle provides multiple issue slots.  

A slot is a hardware resource that represents one opportunity for a microoperation (μop) to issue for execution during a single clock cycle.  

Each cycle, the core exposes a fixed number of these issue opportunities, and this is known as the machine width in Intel’s Top-Down Microarchitecture Analysis Methodology (TMAM). You may also see the methodology referred to as TMA. 

The total number of available slots is defined as:

`Total_SLOTS = machine_width × CPU_CLK_UNHALTED.THREAD`

The machine width corresponds to the maximum number of μops that a core can issue to execution pipelines per cycle.

- Intel cores such as Skylake and Cascade Lake are 4-wide.  
- Newer server and client cores such as Sapphire Rapids, Emerald Rapids, Granite Rapids, and Meteor Lake P-cores are 6-wide.  
- Future generations may widen further, but the slot-based framework remains the same.

Tools such as `perf topdown` automatically apply the correct machine width for the detected CPU.

Intel’s methodology uses a multi-level hierarchy that typically extends to three or four levels of detail. Each level provides progressively finer analysis, allowing you to drill down from high-level categories to specific hardware events.

### Level 1: Identify top-level performance categories

At Level 1, all pipeline slots are attributed to one of four categories, giving a high-level view of how the CPU’s issue capacity is being used:

- Retiring = UOPS_RETIRED.RETIRE_SLOTS / SLOTS  
- Frontend Bound = IDQ_UOPS_NOT_DELIVERED.CORE / SLOTS  
- Bad Speculation = derived from speculative flush behavior (branch mispredictions and machine clears) or computed residually  
- Backend Bound = 1 − (Retiring + Frontend Bound + Bad Speculation)

Most workflows compute Backend Bound as the residual after Retiring, Frontend Bound, and Bad Speculation are accounted for.

### Level 2: Analyze broader bottleneck causes

Once the dominant Level 1 category is identified, Level 2 separates each category into groups:

| Category | Level 2 Sub-Categories | Purpose |
|-----------|------------------------|----------|
| Frontend Bound | Frontend Latency vs Frontend Bandwidth | Distinguish instruction-fetch delays from decode or μop cache throughput limits. |
| Backend Bound | Memory Bound vs Core Bound | Separate stalls caused by memory hierarchy latency/bandwidth from those caused by execution-unit contention or scheduler pressure. |
| Bad Speculation | Branch Mispredict vs Machine Clears | Identify speculation waste due to control-flow mispredictions or pipeline clears. |
| Retiring | Base vs Microcode Sequencer | Show the proportion of useful work from regular instructions versus microcoded sequences. |

### Level 3: Target specific microarchitecture bottlenecks

Level 3 provides fine-grained attribution that pinpoints precise hardware limitations.

Examples include:  
- Memory Bound covers L1 Bound, L2 Bound, L3 Bound, DRAM Bound, Store Bound  
- Core Bound covers execution-port pressure, divider utilization, scheduler or ROB occupancy  
- Frontend latency covers instruction-cache misses, ITLB walks, branch-prediction misses  
- Frontend bandwidth covers decode throughput or μop cache saturation  

At this level, you can determine whether workloads are limited by memory latency, cache hierarchy bandwidth, or execution-resource utilization.

### Level 4: Access specific PMU counter events

Level 4 exposes the Performance Monitoring Unit (PMU) events that implement the hierarchy.  

Here you analyze raw event counts to understand detailed pipeline behavior.  
Event names and availability vary by microarchitecture, but you can verify them with `perf list`.

| Event Name | Purpose |
| :---------------------------------------------- | :----------------------------------------------------------------------------------- |
| `UOPS_RETIRED.RETIRE_SLOTS` | Counts retired μops |
| `UOPS_ISSUED.ANY` | Counts all issued μops (used in speculation analysis) |
| `IDQ_UOPS_NOT_DELIVERED.CORE` | Counts μops not delivered from frontend |
| `CPU_CLK_UNHALTED.THREAD` | Core clock cycles (baseline for normalization) |
| `BR_MISP_RETIRED.ALL_BRANCHES` | Branch mispredictions |
| `MACHINE_CLEARS.COUNT` | Pipeline clears due to faults or ordering |
| `CYCLE_ACTIVITY.STALLS_TOTAL` | Total stall cycles |
| `CYCLE_ACTIVITY.STALLS_MEM_ANY` | Stalls from memory hierarchy misses |
| `CYCLE_ACTIVITY.STALLS_L1D_MISS` | Stalls due to L1 data-cache misses |
| `CYCLE_ACTIVITY.STALLS_L2_MISS` | Stalls waiting on L2 cache misses |
| `CYCLE_ACTIVITY.STALLS_L3_MISS` | Stalls waiting on last-level cache misses |
| `MEM_LOAD_RETIRED.L1_HIT / L2_HIT / L3_HIT` | Track where loads are satisfied in the cache hierarchy |
| `MEM_LOAD_RETIRED.L3_MISS` | Loads missing the LLC and going to memory |
| `MEM_LOAD_RETIRED.DRAM_HIT` | Loads serviced by DRAM |
| `OFFCORE_RESPONSE.*` | Detailed classification of off-core responses (L3 vs DRAM, local vs remote socket) |

Some events (for example, CYCLE_ACTIVITY.* and MEM_LOAD_RETIRED.*) vary across microarchitectures so you should confirm them on your CPU.

### Practical guidance

Here are some practical steps to keep in mind:

- Normalize all metrics to total slots: machine_width × CPU_CLK_UNHALTED.THREAD.  
- Start at Level 1 to identify the dominant bottleneck.  
- Drill down progressively through Levels 2 and 3 to isolate the root cause.  
- Use raw events (Level 4) for detailed validation or hardware-tuning analysis.  
- Check event availability before configuring counters on different CPU generations.  

## Summary

Intel's Top-Down methodology provides a structured, slot-based framework for understanding pipeline efficiency. Each slot represents a potential μop issue opportunity.  

By attributing every slot to one of the four categories you can measure how effectively a core executes useful work versus wasting cycles on stalls or speculation.
