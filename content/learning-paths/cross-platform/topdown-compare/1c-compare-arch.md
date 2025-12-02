---
title: "Evaluate cross-platform PMU counter differences"
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Contrast Intel and Arm Neoverse implementation approaches

After examining each architecture individually, it's clear that Intel x86 and Arm Neoverse V2 share the same top-down philosophy but differ in their implementation, scope, and event model.

Both use slot-based accounting to represent potential pipeline issue opportunities per cycle. However, Intel defines four issue slots per cycle (machine width = 4 to 6 µops per cycle, depending on microarchitecture), while Neoverse V2 defines eight rename slots per cycle for its top-down accounting.

### Key shared principles

Here are some concepts that are shared between Intel x86 and Arm:

- Slot-based utilization to measure pipeline efficiency in terms of µop issue or rename slots per cycle
- Four common categories at the top level: Retiring, Bad Speculation, Frontend Bound, Backend Bound
- Quantitative normalization for metrics that are expressed as a percentage of total available slots (width × cycles)
- Resource attribution to map inefficiencies to architectural subsystems such as frontend, backend, or memory

### Philosophical differences

Intel x86 favors a hierarchical multi-level drill-down, while Arm emphasizes two-stage flexibility.

Intel's TMAM expands from high-level slots to detailed microarchitectural causes, and Arm's model classifies slot usage first, then groups detailed metrics into resource effectiveness groups including cache, TLB, branch, and operation mix that can be examined independently.

## Compare hierarchical versus grouped methodologies

| Aspect | Intel x86 | Arm Neoverse V2 |
| :-- | :-- | :-- |
| Analysis Model | Multi-level hierarchy (Levels 1 → 2 → 3 → 4) | Two-stage model: Stage 1 Top-Down L1 + Stage 2 Resource Groups |
| Machine / Slot Width | 4–6 issue slots per cycle (typically 4 for Skylake/Ice Lake, 6 for Sapphire Rapids and later) | 8 rename slots per cycle for Neoverse V2 |
| Measurement Basis | µops issued and retired per slot | µops speculatively executed and retired per slot |
| Formula Structure | Uses `UOPS_RETIRED.*`, `IDQ_UOPS_NOT_DELIVERED.*`, and derived ratios | Uses `STALL_SLOT_*`, `OP_SPEC`, `OP_RETIRED`, `BR_MIS_PRED` events |
| Hierarchy Depth | Four levels with formal sub-categories (Latency/Bandwidth, Memory/Core etc.) | Stage 1 Top-down L1 + Stage 2 effectiveness groups (Cycle, Branch, Cache) |
| Drill-Down Approach | Sequential hierarchical descent | Parallel exploration by resource group |
| Output Units | Percent of slots utilized per category | Percent of slots utilized per category (normalized to 8 slots/cycle) |

## Map equivalent PMU counters across architectures

The table below shows PMU events used to answer the analysis questions.

| Performance Question | Intel x86 PMU Events | Arm Neoverse V2 PMU Events | Description |
| :-- | :-- | :-- | :-- |
| Is the frontend limiting µop delivery? | `IDQ_UOPS_NOT_DELIVERED.CORE` | `STALL_SLOT_FRONTEND` | Stalls due to instruction-fetch or decode limits |
| Is speculation causing waste? | `BR_MISP_RETIRED.*`, `MACHINE_CLEARS.*` | `BR_MIS_PRED`, `BR_MIS_PRED_RETIRED` | Lost slots/cycles from mispredicted or squashed µops |
| Is memory the bottleneck? | `CYCLE_ACTIVITY.STALLS_L3_MISS`, `CYCLE_ACTIVITY.STALLS_MEM_ANY` | `STALL_SLOT_BACKEND`, `L1D_CACHE_REFILL`, `L2D_CACHE_REFILL`, `LL_CACHE_MISS_RD` | Backend stalls waiting for cache/memory refills |
| How efficient is the cache hierarchy? | `MEM_LOAD_RETIRED.L1_HIT/L2_HIT/L3_HIT`, `MEM_LOAD_RETIRED.L3_MISS` | `L1D_CACHE_REFILL`, `L2D_CACHE_REFILL`, `LL_CACHE_MISS_RD` | Indicates cache locality and hierarchy effectiveness |
| Branch predictor accuracy? | `BR_MISP_RETIRED.ALL_BRANCHES / BR_INST_RETIRED.ALL_BRANCHES` | `BR_MIS_PRED_RETIRED / BR_RETIRED` | Fraction of mispredicted branches affecting control-flow stalls |

On Intel, `MACHINE_CLEARS.*` represent pipeline flushes caused by memory ordering violations, self-modifying code, or other speculation faults.

On Arm Neoverse V2, equivalent lost work appears under Bad Speculation through `BR_MIS_PRED` and `STALL_SLOT` accounting, which include misprediction recovery and pipeline refill overhead.

## Interpretation and cross-platform analysis

| Focus | Intel x86 Approach | Arm Neoverse V2 Approach |
| :-- | :-- | :-- |
| Frontend vs Backend Balance | Measured by slot distribution from `IDQ_UOPS_NOT_DELIVERED` and `CYCLE_ACTIVITY` counters | Measured using `STALL_SLOT_FRONTEND` and `STALL_SLOT_BACKEND` |
| Speculative Execution Impact | Explicit "Bad Speculation" slot fraction + `MACHINE_CLEARS.*` | Derived from `BR_MIS_PRED`, `BR_MIS_PRED_RETIRED`, and `OP_SPEC/OP_RETIRED` ratios |
| Cache and Memory Hierarchy | Layered: L1 → L2 → L3 → DRAM via `CYCLE_ACTIVITY` events | Effectiveness groups: L1I/L1D/L2/LL with MPKI and hit/miss ratios |
| Stall Accounting Granularity | Strict hierarchical attribution (single bottleneck per slot) | Flexible overlap across groups—multiple concurrent stall sources possible |
| Metric Normalization | All metrics normalized to total slots = machine_width × CPU cycles | All metrics normalized to total slots = CPU cycles × 8 (rename width) |

## Practical cross-platform guidance

- Normalize correctly: Intel uses width × CPU cycles (where width could be 4 or 6) and Arm Neoverse V2 uses 8 × CPU cycles
- Interpret "slots" consistently: both represent theoretical µop issue capacity per cycle
- Compare memory and cache behavior using MPKI and refill events rather than identical counter names
- Speculation loss differs as Intel isolates machine clears and Arm includes misprediction recovery directly in Bad Speculation

## Summary

Intel's TMAM and Arm Neoverse V2 top-down analysis both translate raw PMU data into actionable insights about how efficiently each core issues, executes, and retires µops.

Intel x86 uses a deep, multi-level hierarchy emphasizing structured drill-down from slots to hardware events.

Arm Neoverse V2 uses a simplified, two-stage model with explicit slot-based formulas and resource-group flexibility.

By understanding these conceptual and measurement differences, you can interpret performance data consistently across architectures, enabling direct comparison of Retiring %, Frontend/Backend Bound %, and Bad Speculation % to optimize workloads for both x86 and Arm servers.
