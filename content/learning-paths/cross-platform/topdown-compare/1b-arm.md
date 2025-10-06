---
title: "Understand Arm Neoverse top-down analysis"
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---
## Explore Arm's approach to performance analysis

After understanding Intel's comprehensive 4-level hierarchy, you can explore how Arm approached the same performance analysis challenge with a different philosophy. Arm developed a complementary top-down methodology specifically for Neoverse server cores that prioritizes practical usability while maintaining analysis effectiveness.

The Arm Neoverse architecture uses an 8-slot rename unit for pipeline bandwidth accounting, which differs from Intel's issue-slot model. Unlike Intel's hierarchical model, Arm employs a streamlined two-stage methodology that balances analysis depth with practical usability.

### Execute Stage 1: Calculate top-down performance categories

Stage 1 identifies high-level bottlenecks using the same four categories as Intel, but with Arm-specific PMU events and formulas. This stage uses slot-based accounting similar to Intel's approach while employing Arm event names and calculations tailored to the Neoverse architecture.

#### Configure Arm-specific PMU counter formulas

Arm uses different top-down metrics based on different events, but the concept remains similar to Intel's approach. The key difference lies in the formula calculations and slot accounting methodology:

| Metric | Formula | Purpose |
| :-- | :-- | :-- |
| Backend bound | `100 * (STALL_SLOT_BACKEND / (CPU_CYCLES * 8))` | Backend resource constraints |
| Frontend bound | `100 * ((STALL_SLOT_FRONTEND / (CPU_CYCLES * 8)) - (BR_MIS_PRED / (4 * CPU_CYCLES)))` | Frontend delivery issues |
| Bad speculation | `100 * (1 - (OP_RETIRED/OP_SPEC)) * (1 - (STALL_SLOT/(CPU_CYCLES * 8))) + (BR_MIS_PRED / (4 * CPU_CYCLES))` | Misprediction recovery |
| Retiring | `100 * (OP_RETIRED/OP_SPEC) * (1 - (STALL_SLOT/(CPU_CYCLES * 8)))` | Useful work completed |

### Execute Stage 2: Explore resource effectiveness groups

Stage 2 focuses on resource-specific effectiveness metrics grouped by CPU component. This stage provides industry-standard metrics like MPKI (Misses Per Kilo Instructions) and offers detailed breakdown without the strict hierarchical drilling required by Intel's methodology.

#### Navigate resource groups without hierarchical constraints

Instead of Intel's hierarchical levels, Arm organizes detailed metrics into effectiveness groups that can be explored independently. 

**Branch Effectiveness** provides misprediction rates and MPKI, while **ITLB/DTLB Effectiveness** measures translation lookaside buffer efficiency. **Cache Effectiveness** groups (L1I/L1D/L2/LL) deliver cache hit ratios and MPKI across the memory hierarchy. Additionally, **Operation Mix** breaks down instruction types (SIMD, integer, load/store), and **Cycle Accounting** tracks frontend versus backend stall percentages.

## Apply essential Arm Neoverse PMU counters for analysis

Neoverse cores expose approximately 100 hardware events optimized for server workloads. The core set for top-down analysis includes:

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


