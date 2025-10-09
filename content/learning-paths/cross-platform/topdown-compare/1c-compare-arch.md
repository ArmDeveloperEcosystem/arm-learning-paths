---
title: "Evaluate cross-platform PMU counter differences"
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---
## Contrast Intel and Arm Neoverse implementation approaches

After understanding each architecture's methodology individually, you can now examine how they differ in implementation while achieving equivalent analysis capabilities. Both architectures implement the same fundamental approach with architecture-specific adaptations:

- Slot-based accounting: pipeline utilization measured in issue or rename slots
- Hierarchical analysis: broad classification followed by drill-down into dominant bottlenecks
- Resource attribution: map performance issues to specific CPU micro-architectural components

## Compare multi-level hierarchical and resource groups methodologies  

| Aspect | Intel x86 | Arm Neoverse |
| :-- | :-- | :-- |
| Hierarchy Model | Multi-level tree (Level 1 → Level 2 → Level 3+) | Two-stage: Topdown Level 1 + Resource Groups |
| Slot Width | 4 issue slots per cycle (typical) | 8 rename slots per cycle (Neoverse V1) |
| Formula Basis | Micro-operation (uop) centric | Operation and cycle centric |
| Event Naming | Intel-specific mnemonics | Arm-specific mnemonics |
| Drill-down Strategy | Strict hierarchical descent | Exploration by resource groups |

## Map equivalent PMU counters across architectures

| Performance Question | x86 Intel Events | Arm Neoverse Events |
| :-- | :-- | :-- |
| Frontend bound? | `IDQ_UOPS_NOT_DELIVERED.*` | `STALL_SLOT_FRONTEND` |
| Bad speculation? | `BR_MISP_RETIRED.*` | `BR_MIS_PRED_RETIRED` |
| Memory bound? | `CYCLE_ACTIVITY.STALLS_L3_MISS` | `L1D_CACHE_REFILL`, `L2D_CACHE_REFILL` |
| Cache effectiveness? | `MEM_LOAD_RETIRED.L3_MISS_PS` | Cache refill metrics / Cache access metrics |

While PMU counter names and calculation formulas differ significantly between Intel x86 and Arm Neoverse architectures, both provide equivalent top-down analysis capabilities. Understanding these methodological differences enables effective cross-platform performance optimization:

- **Intel x86**: Use `perf stat --topdown` for Level 1 analysis, then drill down through hierarchical levels
- **Arm Neoverse**: Use `topdown-tool -m Cycle_Accounting` for Stage 1, then explore resource effectiveness groups
- **Cross-platform strategy**: Focus on the four common categories while adapting tools and counter interpretations to each architecture

Continue to the next step to see practical examples comparing both methodologies.