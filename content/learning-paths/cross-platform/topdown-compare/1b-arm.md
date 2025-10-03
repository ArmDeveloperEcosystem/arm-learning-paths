---
title: "Learn about Arm Neoverse two-stage top-down methodology"
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---
## Arm Neoverse two-stage top-down methodology

Arm developed a complementary top-down methodology specifically for Neoverse server cores. The Arm Neoverse architecture uses an 8-slot rename unit for pipeline bandwidth accounting, differing from Intel's issue-slot model.

Unlike Intel's hierarchical model, Arm employs a two-stage methodology:

### Stage 1: top-down analysis

- Identifies high-level bottlenecks using the same four categories
- Uses Arm-specific PMU events and formulas
- Slot-based accounting similar to Intel but with Arm event names

### Stage 2: Micro-architecture exploration

- Resource-specific effectiveness metrics grouped by CPU component
- Industry-standard metrics like MPKI (Misses Per Kilo Instructions)
- Detailed breakdown without strict hierarchical drilling

### Stage 1: formulas 

Arm uses different top-down metrics based on different events but the concept is similar.

| Metric | Formula | Purpose |
| :-- | :-- | :-- |
| Backend bound | `100 * (STALL_SLOT_BACKEND / (CPU_CYCLES * 8))` | Backend resource constraints |
| Frontend bound | `100 * ((STALL_SLOT_FRONTEND / (CPU_CYCLES * 8)) - (BR_MIS_PRED / (4 * CPU_CYCLES)))` | Frontend delivery issues |
| Bad speculation | `100 * (1 - (OP_RETIRED/OP_SPEC)) * (1 - (STALL_SLOT/(CPU_CYCLES * 8))) + (BR_MIS_PRED / (4 * CPU_CYCLES))` | Misprediction recovery |
| Retiring | `100 * (OP_RETIRED/OP_SPEC) * (1 - (STALL_SLOT/(CPU_CYCLES * 8)))` | Useful work completed |

### Stage 2: resource groups

Instead of hierarchical levels, Arm organizes detailed metrics into effectiveness groups as shown below:

- Branch Effectiveness: Misprediction rates, MPKI
- ITLB/DTLB Effectiveness: Translation lookaside buffer efficiency
- L1I/L1D/L2/LL Cache Effectiveness: Cache hit ratios and MPKI
- Operation Mix: Breakdown of instruction types (SIMD, integer, load/store)
- Cycle Accounting: Frontend vs. backend stall percentages

## Key performance events 

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


