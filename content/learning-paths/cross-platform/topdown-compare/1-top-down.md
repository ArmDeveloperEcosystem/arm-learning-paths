---
title: Top-down performance analysis
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What are the differences between Arm and x86 PMU counters?

This is a common question from software developers and performance engineers. 

Both Arm and x86 CPUs provide sophisticated Performance Monitoring Units (PMUs) with hundreds of hardware counters. Instead of trying to list all available counters and compare microarchitecture, it makes more sense to focus on the performance methodologies they enable and the calculations used for performance metrics. 

While the specific counter names and formulas differ between architectures, both have converged on top-down performance analysis methodologies that categorize performance bottlenecks into four buckets: Retiring, Bad Speculation, Frontend Bound, and Backend Bound.

This Learning Path provides a comparison of how Arm and x86 processors implement top-down
analysis, highlighting the similarities in approach while explaining the architectural differences in counter events and formulas.

## Introduction to top-down performance analysis

Top-down methodology makes performance analysis easier by shifting focus from individual performance
counters to pipeline slot utilization. Instead of trying to interpret dozens of seemingly unrelated metrics, you can systematically identify bottlenecks by attributing each CPU pipeline slot to one of four categories.

- Retiring: pipeline slots that successfully complete useful work
- Bad Speculation: slots wasted on mispredicted branches
- Frontend Bound: slots stalled due to instruction fetch/decode limitations
- Backend Bound: slots stalled due to execution resource constraints

The methodology uses a hierarchical approach that allows you to drill down only into the dominant bottleneck category, and avoid the complexity of analyzing all possible performance issues at the same time. 

The next sections compare the Intel x86 methodology with the Arm top-down methodology. AMD also has an equivalent top-down methodology which is similar to Intel, but uses different counters and calculations. 

## Intel x86 top-down methodology

Intel uses a slot-based accounting model where each CPU cycle provides multiple issue slots. A slot is a hardware resource needed to process operations. More slots means more work can be done. The number of slots depends on the design but current processor designs have 4, 6, or 8 slots. 

### Hierarchical Structure

Intel uses a multi-level hierarchy that typically extends to 4 levels of detail.

**Level 1 (Top-Level):**

At Level 1, all pipeline slots are attributed to one of four categories, providing a high-level view of whether the CPU is doing useful work or stalling.

- Retiring = `UOPS_RETIRED.RETIRE_SLOTS / SLOTS`
- Bad Speculation = `(UOPS_ISSUED.ANY - UOPS_RETIRED.RETIRE_SLOTS + N * RECOVERY_CYCLES) / SLOTS`
- Frontend Bound = `IDQ_UOPS_NOT_DELIVERED.CORE / SLOTS`
- Backend Bound = `1 - (Frontend + Bad Spec + Retiring)`

Where `SLOTS = 4 * CPU_CLK_UNHALTED.THREAD` on most Intel cores.

**Level 2 breakdown:**

Level 2 drills into each of these to identify broader causes, such as distinguishing between frontend latency and bandwidth limits, or between memory and core execution stalls in the backend.

- Frontend Bound covers frontend latency vs. frontend bandwidth
- Backend Bound covers memory bound vs. core bound
- Bad Speculation covers branch mispredicts vs. machine clears
- Retiring covers base vs. microcode sequencer

**Level 3 breakdown:**

Level 3 provides fine-grained attribution, pinpointing specific bottlenecks like DRAM latency, cache misses, or port contention, which makes it possible to identify the exact root cause and apply targeted optimizations.

- Memory Bound includes L1 Bound, L2 Bound, L3 Bound, DRAM Bound, Store Bound
- Core Bound includes Divider, Ports Utilization
- And many more specific categories

**Level 4 breakdown:**

Level 4 provides the specific microarchitecture events that cause the inefficiencies. 

### Key Performance Events

Intel processors expose hundreds of performance events, but top-down analysis relies on a core set:

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


Using the above levels of metrics you can find out which of the 4 top-level categories are causing bottlenecks.

### Arm top-down methodology

Arm developed a similar top-down methodology for Neoverse server cores. The Arm architecture uses an 8-slot rename unit for pipeline bandwidth accounting.

### Two-Stage Approach

Unlike Intel's hierarchical model, Arm employs a two-stage methodology:

**Stage 1: Topdown analysis**

- Identifies high-level bottlenecks using the same four categories
- Uses Arm-specific PMU events and formulas
- Slot-based accounting similar to Intel but with Arm event names

**Stage 2: Micro-architecture exploration**

- Resource-specific effectiveness metrics grouped by CPU component
- Industry-standard metrics like MPKI (Misses Per Kilo Instructions)
- Detailed breakdown without strict hierarchical drilling

### Stage 1 formulas 

Arm uses different top-down metrics based on different events but the concept is similar.

| Metric | Formula | Purpose |
| :-- | :-- | :-- |
| Backend bound | `100 * (STALL_SLOT_BACKEND / (CPU_CYCLES * 8))` | Backend resource constraints |
| Frontend bound | `100 * ((STALL_SLOT_FRONTEND / (CPU_CYCLES * 8)) - (BR_MIS_PRED / (4 * CPU_CYCLES)))` | Frontend delivery issues |
| Bad speculation | `100 * (1 - (OP_RETIRED/OP_SPEC)) * (1 - (STALL_SLOT/(CPU_CYCLES * 8))) + (BR_MIS_PRED / (4 * CPU_CYCLES))` | Misprediction recovery |
| Retiring | `100 * (OP_RETIRED/OP_SPEC) * (1 - (STALL_SLOT/(CPU_CYCLES * 8)))` | Useful work completed |

### Stage 2 resource groups

Instead of hierarchical levels, Arm organizes detailed metrics into effectiveness groups as shown below:

- Branch Effectiveness: Misprediction rates, MPKI
- ITLB/DTLB Effectiveness: Translation lookaside buffer efficiency
- L1I/L1D/L2/LL Cache Effectiveness: Cache hit ratios and MPKI
- Operation Mix: Breakdown of instruction types (SIMD, integer, load/store)
- Cycle Accounting: Frontend vs. backend stall percentages

### Key performance events 

Neoverse cores expose approximately 100 hardware events optimized for server workloads, including:

| Event Name            | Purpose / Usage                                                                          |
| :-------------------- | :--------------------------------------------------------------------------------------- |
| `CPU_CYCLES`          | Core clock cycles (baseline for normalization).                                          |
| `OP_SPEC`             | Speculatively executed micro-operations (used as slot denominator).                      |
| `OP_RETIRED`          | Retired micro-operations (used to measure useful work).                                  |
| `INST_RETIRED`        | Instructions retired (architectural measure; used for IPC, MPKI normalization).          |
| `INST_SPEC`           | Instructions speculatively executed (needed for operation mix and speculation analysis). |
| `STALL_SLOT`          | Total stall slots (foundation for efficiency metrics).                                   |
| `STALL_SLOT_FRONTEND` | Stall slots due to frontend resource constraints.                                        |
| `STALL_SLOT_BACKEND`  | Stall slots due to backend resource constraints.                                         |
| `BR_RETIRED`          | Branches retired (baseline for branch misprediction ratio).                              |
| `BR_MIS_PRED_RETIRED` | Mispredicted branches retired (branch effectiveness, speculation waste).                 |
| `L1I_CACHE_REFILL`    | Instruction cache refills (frontend stalls due to I-cache misses).                       |
| `ITLB_WALK`           | Instruction TLB walks (frontend stalls due to translation).                              |
| `L1D_CACHE_REFILL`    | Data cache refills (backend stalls due to L1D misses).                                   |
| `L2D_CACHE_REFILL`    | Unified L2 cache refills (backend stalls from L2 misses).                                |
| `LL_CACHE_MISS_RD`    | Last-level/system cache read misses (backend stalls from LLC/memory).                    |
| `DTLB_WALK`           | Data TLB walks (backend stalls due to translation).                                      |
| `MEM_ACCESS`          | Total memory accesses (baseline for cache/TLB effectiveness ratios).                     |


## Arm compared to x86 

### Conceptual similarities

Both architectures adhere to the same fundamental top-down performance analysis philosophy:

1. Four-category classification: Retiring, Bad Speculation, Frontend Bound, Backend Bound
2. Slot-based accounting: Pipeline utilization measured in issue or rename slots
3. Hierarchical analysis: Broad classification followed by drill-down into dominant bottlenecks
4. Resource attribution: Map performance issues to specific CPU micro-architectural components

### Key Differences

| Aspect | x86 Intel | Arm Neoverse |
| :-- | :-- | :-- |
| Hierarchy Model | Multi-level tree (Level 1 → Level 2 → Level 3+) | Two-stage: Topdown Level 1 + Resource Groups |
| Slot Width | 4 issue slots per cycle (typical) | 8 rename slots per cycle (Neoverse V1) |
| Formula Basis | Micro-operation (uop) centric | Operation and cycle centric |
| Event Naming | Intel-specific mnemonics | Arm-specific mnemonics |
| Drill-down Strategy | Strict hierarchical descent | Exploration by resource groups |

### Event Mapping Examples

| Performance Question | x86 Intel Events | Arm Neoverse Events |
| :-- | :-- | :-- |
| Frontend bound? | `IDQ_UOPS_NOT_DELIVERED.*` | `STALL_SLOT_FRONTEND` |
| Bad speculation? | `BR_MISP_RETIRED.*` | `BR_MIS_PRED_RETIRED` |
| Memory bound? | `CYCLE_ACTIVITY.STALLS_L3_MISS` | `L1D_CACHE_REFILL`, `L2D_CACHE_REFILL` |
| Cache effectiveness? | `MEM_LOAD_RETIRED.L3_MISS_PS` | Cache refill metrics / Cache access metrics |

While it doesn't make sense to directly compare PMU counters for the Arm and x86 architectures, it is useful to understand the top-down methodologies for each so you can do effective performance analysis and compare you code running on each architecture. 

Continue to the next step to try a code example.