---
title: Decode the traces and reveal operator-level bottlenecks
weight: 7
layout: "learningpathall"
---

<p>
  <img
    src="/learning-paths/embedded-and-microcontrollers/sme-executorch-profiling/images/step06_analyze.svg"
    alt="Outcome: analysis summary produced"
    class="content-uploaded-image centered"
  />
  <span class="content-image-caption centered">
    Outcome: analysis_summary.json with operator-level breakdown and kernel hints.
  </span>
</p>

## Goal of this step

Turn the `.etdump` traces into a readable summary you can act on:
- which operator categories dominate (Convolution / GEMM / Data Movement / Other), and
- which specific operators are responsible (names + totals), including kernel hints when available.

**Time:** ~10 seconds to run analysis

<details>
  <summary><strong>What is an ETDump?</strong></summary>
  <p>ETDump is ExecuTorch's profiling trace format. It captures nested events emitted during execution and allows you to aggregate timings by operator.</p>
</details>

## Do this now
```bash
python scripts/analyze_results.py \
  --run-dir runs/mac --quiet
```

**Outputs:**
- **`runs/mac/analysis_summary.json`**: Full results with operator-level details + category totals + kernel hints
- **Terminal output**: Summary table (category view) for quick review

To see operator-level details:
```bash
# Pretty-print the full analysis
python -m json.tool runs/mac/analysis_summary.json | less

# Or just the operator details section
python -c "import json; print(json.dumps(json.load(open('runs/mac/analysis_summary.json'))['operator_details'], indent=2))"
```

## What ETDump gives you (and a common pitfall)

ETDump is a profiling trace that captures **nested events**. Practically:
- Use **`Method::execute`** for **end-to-end latency** (E2E).
- Do **not** sum all child operator durations to compute E2E — that double-counts nested spans.

If you build a category report, compute:

\[
OTHER = E2E - (CONV + GEMM + ELEMENTWISE + DATA\_MOVEMENT)
\]

This avoids double counting from nested framework events.

## You should see (blog-derived pattern)
- **End-to-end (1 core):**
  - INT8 SME2 off → on: 556 → 304 ms (≈1.8×)
  - FP16 SME2 off → on: 1,163 → 298 ms (≈3.9×)
- **Operator categories (SME2 on, FP16 example):**
  - Convolution: drops from ~881 ms to ~98 ms
  - GEMM: drops from ~31.6 ms to ~7.6 ms
  - Data Movement: ~120 ms (≈40% share, mostly transpose)

![Operator-category breakdown showing Convolution and GEMM shrink while Data Movement grows](images/combined_operator_breakdown_stacked.png "Figure. Operator breakdown (1 CPU core): SME2 accelerates Convolution/iGEMM and GEMM; Data Movement becomes a dominant share.")

## Essential code idea (categorize operators)

You don’t need a big framework to start. The key is: **map operator names to categories** so humans can reason about bottlenecks.

```python
def categorize(op: str) -> str:
    s = op.lower()
    if "conv" in s:
        return "Convolution"
    if "matmul" in s or "linear" in s or "gemm" in s:
        return "GEMM"
    if any(k in s for k in ["transpose", "reshape", "copy", "convert", "pad"]):
        return "Data Movement"
    if any(k in s for k in ["relu", "gelu", "add", "mul", "sub", "div", "sigmoid", "tanh"]):
        return "Elementwise"
    return "Other"
```

## Understanding the two-level view: operators → categories

The analysis script produces two complementary views:

1. **Operator-level view**: Individual operators with their timings (e.g., `aten::conv2d`, `aten::transpose`, `aten::linear`)
2. **Category-level view**: Operators grouped by function (Convolution, Data Movement, GEMM, etc.)

Both views are essential: operator-level shows you **exactly what's slow**, category-level shows you **which architectural pattern dominates**.

## Example output (what "good" looks like)

### Category-level summary (high-level bottleneck view)

```output
Category totals (ms, SME2-on, FP16):
  - Convolution:    98.100  (32.7%)
  - Data Movement: 119.100  (39.7%)  ← new bottleneck after SME2
  - Other:          71.700  (23.9%)
  - GEMM:            7.600   (2.5%)
  - Elementwise:     1.700   (0.6%)
---
Total (category sum): 298.200 ms
E2E (Method::execute): 298.200 ms
```

### Operator-level details (example excerpt from `analysis_summary.json`)

```json
{
  "operator_details": [
    {
      "name": "aten::_native_batch_norm_legit",
      "category": "Data Movement",
      "avg_ms": 45.2,
      "count": 24,
      "total_ms": 108.5,
      "kernel_hint": "xnn_f16_vlrelu_ukernel__neonfp16arith_u16"
    },
    {
      "name": "aten::convolution",
      "category": "Convolution",
      "avg_ms": 8.1,
      "count": 12,
      "total_ms": 97.2,
      "kernel_hint": "xnn_pf16_igemm_minmax_ukernel_4x8__neonsme2"
    },
    {
      "name": "aten::transpose",
      "category": "Data Movement",
      "avg_ms": 0.45,
      "count": 18,
      "total_ms": 8.1
    },
    {
      "name": "aten::linear",
      "category": "GEMM",
      "avg_ms": 2.5,
      "count": 3,
      "total_ms": 7.5,
      "kernel_hint": "xnn_pf16_gemm_minmax_ukernel_6x8__neonsme2"
    }
  ]
}
```

**Key insights from this example:**
- Batch norms (`_native_batch_norm_legit`) dominate Data Movement with **108.5 ms total** (45.2 ms avg × 24 calls)
- Convolutions use SME2 kernels (`__neonsme2`) and contribute **97.2 ms**
- Many small transposes (0.45 ms each, 18 calls) add up to **8.1 ms**
- Linear layers (GEMM) are fast with SME2: **7.5 ms total**

Wrote: runs/mac/analysis_summary.json
```

## How to interpret operator-level results

### Start with categories (high-level view)
- If **Convolution/GEMM did not shrink**: Check runner flags and SME2 support (kernel hints should show `__neonsme2`)
- If **Data Movement dominates (~40%)**: Likely layout churn (NCHW ↔ NHWC transposes, batch norms, reshape/pad)
- If **Other is large**: Framework overhead or non-delegated ops (inspect `operator_details` for specifics)

### Drill down to operators (when you need specifics)
1. **Find the slowest individual operators** in `operator_details` (sort by `total_ms` or `avg_ms`)
2. **Check kernel hints**: Names like `xnn_pf16_*__neonsme2` confirm SME2 delegation; NEON-only names suggest fallback
3. **Look for repetition**: Many fast calls can add up (e.g., 18 transposes × 0.45 ms = 8.1 ms)
4. **Map back to model architecture**: 
   - High batch norm time → normalization layers between conv blocks
   - Many transposes → layout mismatches (e.g., channels-last vs channels-first)
   - Slow specific conv → check that layer's channel counts, kernel size, delegation

**Example drill-down:**
- Category view: "Data Movement: 119 ms (40%)" ← high-level signal
- Operator view: `aten::_native_batch_norm_legit` accounts for 108.5 ms of that ← specific culprit
- Action: Consider fusing batch norms into conv layers or switching to layer norm if applicable

## A practical mindset: what to optimize next

Use the SME2-on vs SME2-off comparison to decide *where engineering time buys the most latency*:

- **Step 1 — confirm the stack is wired correctly**: SME2-on should reduce Convolution/iGEMM and GEMM time. If it doesn’t, fix build/delegation first (don’t “optimize the model” yet).
- **Step 2 — read the new bottleneck**: once matrix math is fast, **Data Movement** often becomes the biggest slice. In the SqueezeSAM case study, it rises to ~40% and is dominated by transpose/layout conversions.
- **Step 3 — map bottlenecks back to architecture**: repeated layout churn typically appears where operators disagree on layout expectations (e.g., norms in NCHW vs conv kernels preferring NHWC). That’s the bridge from “profile” → “model change”.

## Validation
- Analysis output should include: E2E summary (median/mean/p50/p90), operator-category table, optional kernel list.
- SME2-on should reduce Convolution/GEMM time. If not, revisit build and config.
- If `analyze_results.py` cannot find a `.etrecord`, re-export the model and keep `<model>.etrecord` beside `<model>.pte`.
- To sanity-check against the known-good fixture schema: `python scripts/compare_run_to_known_good.py --run-dir runs/mac`
