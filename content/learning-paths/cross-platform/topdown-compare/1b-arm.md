---
title: "Understand Arm Neoverse top-down analysis"
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Explore Arm's approach to performance analysis

After understanding the Intel x86 multi-level top-down hierarchy, you can look at how Arm Neoverse approaches the same challenge with a two-stage model designed for clarity and cross-architecture consistency.

Arm's methodology follows the same four top-level categories: Retiring, Bad Speculation, Frontend Bound, and Backend Bound, but uses Arm-specific Performance Monitoring Unit (PMU) events and formulas.

Neoverse V3 is used below; the details will be different for other Neoverse processors.

## Pipeline slot model in Arm Neoverse V3

Neoverse V3 uses a slot-based model to measure pipeline bandwidth.

Each cycle provides up to ten micro-operation (μop) slots for issue and execution in the top-down formulas.

This forms the foundation of the Neoverse V3 slot-based top-down accounting.

`Total_SLOTS = CPU_CYCLES × 10`

Just like Intel's issue-slot model, Arm attributes every slot to one of the same four categories.

This allows percentage-based comparisons of pipeline efficiency across different cores, regardless of frontend or backend width.

## Stage 1: Identify top-level performance categories

Stage 1 corresponds to Level 1 in Intel's TMAM and determines where the processor spends its available slots.

The Arm Neoverse V3 Telemetry Specification starts with the `Topdown_L1` metric group, then uses `Topdown_Frontend` and `Topdown_Backend` to split the dominant bound category into more specific causes.

### Topdown Level 1 metric group

`Topdown_L1` classifies total slots into four top-level categories.

All formulas below are defined in the Arm Neoverse V3 Telemetry Specification.

| Metric | Formula | Description |
| :-- | :-- | :-- |
| `retiring` | 100 × ((1 − STALL_SLOT / (CPU_CYCLES × 10)) × (OP_RETIRED / OP_SPEC)) | Slots that retire valid μops (useful work) |
| `bad_speculation` | 100 × ((1 − STALL_SLOT / (CPU_CYCLES × 10)) × (1 − OP_RETIRED / OP_SPEC) + STALL_FRONTEND_FLUSH / CPU_CYCLES) | Slots used by operations that never retire due to mispredictions or pipeline flushes |
| `frontend_bound` | 100 × (STALL_SLOT_FRONTEND / (CPU_CYCLES × 10) − STALL_FRONTEND_FLUSH / CPU_CYCLES) | Slots lost because the frontend cannot supply μops (fetch, decode, or branch delays) |
| `backend_bound` | 100 × (STALL_SLOT_BACKEND / (CPU_CYCLES × 10)) | Percentage of total slots stalled by backend resource constraints |

Each metric is expressed as a percentage of total slots.

All four categories sum to 100%, providing a complete top-level pipeline utilization view.

### Topdown Frontend metric group

`Topdown_Frontend` analyzes workloads where `frontend_bound` dominates and separates frontend memory-bound causes from frontend core-bound causes.

For frontend memory-bound cases, inspect instruction-side cache and translation groups such as `L1I_Cache_Effectiveness`, `L2_Cache_Effectiveness`, `LL_Cache_Effectiveness`, and `ITLB_Effectiveness`. For frontend core-bound cases, inspect branch behavior with `Branch_Effectiveness` and compare stalled cycles with `Cycle_Accounting`.

### Topdown Backend metric group

`Topdown_Backend` analyzes workloads where `backend_bound` dominates and separates backend memory-bound causes from backend core-bound causes.

For backend memory-bound cases, inspect `L1D_Cache_Effectiveness`, `L2_Cache_Effectiveness`, `LL_Cache_Effectiveness`, and `DTLB_Effectiveness`. For backend core-bound cases, use `Operation_Mix`, `FP_Arithmetic_Intensity`, `FP_Precision_Mix`, `SVE_Effectiveness`, and `Cycle_Accounting` to understand execution pressure.

## Stage 2: Microarchitecture exploration and effectiveness groups

Stage 2 expands on Stage 1 hotspots by examining detailed resource groups rather than a strict hierarchy.

The Neoverse V3 Telemetry Specification organizes metrics into effectiveness groups that can be analyzed independently:

| Metric Group | Purpose |
| :-- | :-- |
| `L1D_Cache_Effectiveness` | Measures data cache access, refill, hit, and miss behavior closest to the core. |
| `L1I_Cache_Effectiveness` | Measures instruction cache refill and miss behavior that can limit frontend delivery. |
| `L2_Cache_Effectiveness` | Measures L2 cache hits, misses, and refill behavior for instruction and data traffic. |
| `LL_Cache_Effectiveness` | Measures last-level cache read behavior before traffic leaves the core cluster or cache hierarchy. |
| `DTLB_Effectiveness` | Measures data translation lookaside buffer misses and walks that can affect load and store latency. |
| `ITLB_Effectiveness` | Measures instruction translation misses and walks that can affect fetch latency. |
| `Branch_Effectiveness` | Measures branch prediction accuracy, branch density, and misprediction rate. |
| `Cycle_Accounting` | Compares frontend stalled cycles, backend stalled cycles, and active cycles. |
| `General` | Provides broad normalization metrics such as cycles, instructions, IPC, and elapsed time. |
| `FP_Arithmetic_Intensity` | Relates floating-point work to memory activity to show whether a workload is compute-heavy or memory-heavy. |
| `FP_Precision_Mix` | Shows the floating-point precision mix used by the workload. |
| `SVE_Effectiveness` | Shows SVE instruction use and whether vector-length scalable execution is significant. |
| `Operation_Mix` | Breaks down retired or speculated work by operation type, such as load, store, integer, SIMD, FP, and SVE operations. |
| `MPKI` | Normalizes cache, TLB, and branch misses per thousand retired instructions. |
| `Miss_Ratio` | Reports miss rates relative to relevant access or lookup counts. |

On Neoverse V3 systems where the last-level cache is configured as a system-level cache, last-level cache read metrics can represent SLC behavior. Neoverse V3 does not include write variants for last-level cache events because the SLC is used as an eviction cache.

Unlike Intel's drill-down approach, Arm's groups can be explored in any order to focus on the dominant subsystem.

## Key Arm Neoverse V3 PMU events for top-down analysis

Neoverse V3 exposes PMU events for slot accounting, branch analysis, memory hierarchy behavior, and operation mix analysis.

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
| `STALL_FRONTEND_FLUSH` | Frontend flush stalls used to account for bad speculation and frontend-bound slots |
| `BR_MIS_PRED` | Speculatively executed mispredicted branches – useful for branch analysis |
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

- Normalize all percentages to total slots (CPU_CYCLES × 10)
- Start with `Topdown_L1` to locate the dominant performance category
- If `frontend_bound` dominates, inspect `Topdown_Frontend`, then follow the indicated branch, L1I, L2, LL cache, and ITLB groups
- If `backend_bound` dominates, inspect `Topdown_Backend`, then follow the indicated L1D, L2, LL cache, DTLB, and operation or core-related groups
- Use `Cycle_Accounting` to compare frontend and backend stalled cycles
- Use `MPKI` and `Miss_Ratio` for normalized cache, TLB, and branch analysis
- Use `Operation_Mix`, `FP_Arithmetic_Intensity`, `FP_Precision_Mix`, and `SVE_Effectiveness` when retiring or execution-unit utilization is the focus

## Summary

Arm Neoverse V3 employs a concise, two-level top-down methodology built around slot-based pipeline accounting.

Stage 1 classifies total slots into `retiring`, `bad_speculation`, `frontend_bound`, and `backend_bound`.

Stage 2 uses effectiveness groups to investigate specific subsystems such as branch prediction, cache, and memory.

This model mirrors Intel's top-down philosophy so you can compare the top-level categories.
