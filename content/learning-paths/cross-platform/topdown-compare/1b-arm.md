---
title: "Understand Arm Neoverse top-down analysis"
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Explore Arm's approach to performance analysis

After understanding the Intel x86 multi-level top-down hierarchy, you can look at how Arm Neoverse approaches the same challenge with a two-stage model designed for clarity and cross-architecture consistency.

Arm's methodology follows the same four top-level categories: Retiring, Bad Speculation, Frontend Bound, and Backend Bound, but uses Arm-specific Performance Monitoring Unit (PMU) events and formulas.

Neoverse V2 is used below; the details will be different for other Neoverse processors.

## Pipeline slot model in Arm Neoverse V2

Neoverse V2 uses an 8-slot rename unit to measure pipeline bandwidth.

Each cycle provides up to eight micro-operation (μop) slots for issue and execution.

This forms the foundation of the Neoverse V2 slot-based top-down accounting.

`Total_SLOTS = CPU_CYCLES × 8`

Just like Intel's issue-slot model, Arm attributes every slot to one of the same four categories.

This allows percentage-based comparisons of pipeline efficiency across different cores, regardless of frontend or backend width.

## Stage 1: Identify top-level performance categories

Stage 1 corresponds to Level 1 in Intel's TMAM and determines where the processor spends its available slots.

All formulas below are defined in the Arm Neoverse V2 Telemetry Specification.

| Metric | Formula | Description |
| :-- | :-- | :-- |
| Backend Bound | 100 × (STALL_SLOT_BACKEND / (CPU_CYCLES × 8) − (BR_MIS_PRED × 3 / CPU_CYCLES)) | Percentage of total slots stalled by backend resource constraints |
| Frontend Bound | 100 × (STALL_SLOT_FRONTEND / (CPU_CYCLES × 8) − (BR_MIS_PRED / CPU_CYCLES)) | Slots lost because the frontend cannot supply μops (fetch, decode, or branch delays) |
| Bad Speculation | 100 × ((1 − OP_RETIRED / OP_SPEC) × (1 − STALL_SLOT / (CPU_CYCLES × 8)) + (BR_MIS_PRED × 4 / CPU_CYCLES)) | Slots used by operations that never retire due to mispredictions or pipeline flushes |
| Retiring | 100 × (OP_RETIRED / OP_SPEC × (1 − STALL_SLOT / (CPU_CYCLES × 8))) | Slots that retire valid μops (useful work) |

Each metric is expressed as a percentage of total slots.

All four categories sum to 100%, providing a complete top-level pipeline utilization view.

## Stage 2: Microarchitecture exploration and effectiveness groups

Stage 2 expands on Stage 1 hotspots by examining detailed resource groups rather than a strict hierarchy.

The Neoverse V2 Telemetry Specification organizes metrics into effectiveness groups that can be analyzed independently:

| Metric Group | Example Metrics | Purpose |
| :-- | :-- | :-- |
| Cycle Accounting | frontend_stalled_cycles, backend_stalled_cycles | Percentage of cycles stalled in frontend vs. backend |
| Branch Effectiveness | branch_misprediction_ratio, branch_mpki | Branch prediction accuracy and misprediction rate |
| ITLB/DTLB Effectiveness | itlb_walk_ratio, dtlb_mpki | TLB efficiency and translation latency impact |
| Cache Effectiveness | l1i_cache_mpki, l1d_cache_miss_ratio, l2_cache_mpki, ll_cache_read_hit_ratio | Cache performance across all hierarchy levels |
| Operation Mix | integer_dp_percentage, load_percentage, simd_percentage, store_percentage, sve_all_percentage | Workload instruction composition and vector utilization |
| MPKI / Miss Ratio | Derived from cache and TLB refill events | Normalized misses per kilo instructions for cross-core comparisons |

Unlike Intel's drill-down approach, Arm's groups can be explored in any order to focus on the dominant subsystem.

## Key Arm Neoverse V2 PMU events for top-down analysis

Neoverse V2 implements the Arm PMUv3.5 architecture and exposes about 155 events.

The following subset is essential for top-down and resource-effectiveness analysis:

| Event Name | Purpose / Usage |
| :-- | :-- |
| `CPU_CYCLES` | Core clock cycles – used as baseline for normalization |
| `OP_SPEC` | Speculatively executed μops – denominator for slot accounting |
| `OP_RETIRED` | Retired μops – measures useful work |
| `INST_RETIRED` | Retired instructions – used for IPC and MPKI metrics |
| `INST_SPEC` | Speculative instructions – required for Operation Mix |
| `STALL_SLOT` | All stalled slots (frontend + backend) |
| `STALL_SLOT_FRONTEND` | Stalled slots caused by frontend fetch/decode limitations |
| `STALL_SLOT_BACKEND` | Stalled slots caused by backend resource constraints |
| `BR_MIS_PRED` | Speculatively executed mispredicted branches (used in top-down formulas) |
| `BR_MIS_PRED_RETIRED` | Mispredicted branches retired – used in Branch Effectiveness |
| `BR_RETIRED` | Total branches retired – misprediction ratio denominator |
| `L1I_CACHE_REFILL` | Instruction cache refills – frontend latency indicator |
| `ITLB_WALK` | Instruction TLB walks – frontend translation stall indicator |
| `L1D_CACHE_REFILL` | Data cache refills – backend memory latency indicator |
| `L2D_CACHE_REFILL` | L2 cache refills – backend stall from L2 misses |
| `LL_CACHE_MISS_RD` | Last-level cache read misses – backend stalls from SLC or memory accesses |
| `DTLB_WALK` | Data TLB walks – backend stall due to address translation |
| `MEM_ACCESS` | All memory accesses – baseline for cache/TLB ratios |

## Understanding MPKI metrics

MPKI (Misses Per Kilo Instructions) is a normalized metric that measures cache or TLB misses per 1,000 retired instructions.

The formula is: `MPKI = (Miss_Events / INST_RETIRED) × 1000`

For example:
- L1D Cache MPKI = `(L1D_CACHE_REFILL / INST_RETIRED) × 1000`
- DTLB MPKI = `(DTLB_WALK / INST_RETIRED) × 1000`

MPKI provides several advantages:
- Workload comparison: Compare cache efficiency across different applications regardless of execution time
- Architecture comparison: Evaluate cache performance between different processor designs
- Optimization tracking: Measure improvement from code changes or compiler optimizations

## Practical guidance

Here are some practical steps to keep in mind:

- Normalize all percentages to total slots (CPU_CYCLES × 8)
- Use Stage 1 to locate the dominant performance category
- Apply Stage 2 metric groups to isolate microarchitectural causes
- Compare frontend vs. backend stalls
- Evaluate branch predictor accuracy
- Use MPKI metrics (cache or TLB) = (refills / INST_RETIRED) × 1000 for workload comparisons
- For vectorized workloads, examine Operation Mix metrics (integer, SIMD, SVE percentages)

## Summary

Arm Neoverse V2 employs a concise, two-stage top-down methodology built around an 8-slot rename unit.

Stage 1 classifies total slots into Retiring, Bad Speculation, Frontend Bound, and Backend Bound.

Stage 2 uses effectiveness groups to investigate specific subsystems such as branch prediction, cache, and memory.

This model mirrors Intel's top-down philosophy so you can compare the top-level categories.
