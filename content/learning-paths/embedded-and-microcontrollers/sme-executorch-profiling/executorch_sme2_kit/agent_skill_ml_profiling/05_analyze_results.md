---
name: analyze_results
description: Generate operator-category breakdown from ETDump traces using ExecuTorch Inspector. Categorizes operators (CONV, GEMM, Data Movement, etc.) and compares SME2-on vs SME2-off performance. Use when interpreting profiling results, identifying bottlenecks, or analyzing operator-level performance.
---

# Skill: Analyze Results

**Purpose**: Generate operator-category breakdown from ETDump traces

**When to use**: 
- After `run_profiling` completes successfully
- When interpreting profiling results
- When identifying performance bottlenecks
- When comparing SME2-on vs SME2-off performance

## Overview

This skill analyzes ETDump traces to produce an operator-category breakdown. It uses ExecuTorch Inspector to parse ETDump files and categorize operators into groups (Convolution, GEMM, Data Movement, Elementwise, Other).

**Key insight**: After SME2 accelerates CONV/GEMM operations, bottlenecks often shift to **Data Movement** (transpose, layout changes, memory copies). This analysis makes that shift visible.

**Prerequisites**:
- `.venv/` activated
- ETDump files exist in `out_<model>/runs/<platform>/`
- `manifest.json` exists in run directory (for model path lookup)
- Optionally: `.etrecord` file next to `.pte` (for better operator attribution)

## Steps

### 1. Activate Virtual Environment

```bash
source .venv/bin/activate
```

### 2. Run Analysis

```bash
python3 model_profiling/scripts/analyze_results.py \
  --run-dir model_profiling/out_<model>/runs/mac
```

**Note**: The pipeline **automatically runs analysis** after profiling (generates CSV files from ETDump). You only need to run this script manually if:
- You want to re-analyze existing ETDump files
- Analysis failed during pipeline execution
- You're working with ETDump files from a previous pipeline run

**Note**: 
- No PTE file required - script reads config from `manifest.json`
- CSV files are generated in the **same directory as ETDump files** (e.g., `runs/mac/mac_sme2_on/`)
- ETRecord is automatically found from model path in manifest (if available)

### 3. Review Summary

```bash
# Pretty-print JSON summary
cat model_profiling/out_<model>/runs/mac/analysis_summary.json | python -m json.tool

# Or view specific categories
python -c "
import json
with open('model_profiling/out_<model>/runs/mac/analysis_summary.json') as f:
    data = json.load(f)
    print('Category Totals (ms):')
    for cat, ms in data.get('category_totals_ms', {}).items():
        print(f'  {cat}: {ms:.2f}ms')
"
```

**Verification**:

```bash
# Check analysis output exists
test -f model_profiling/out_<model>/runs/mac/analysis_summary.json && echo "✓ Analysis summary exists"

# Check CSV files were generated (in same directory as ETDump files)
test -f model_profiling/out_<model>/runs/mac/mac_sme2_on/*_timeline.csv && echo "✓ Timeline CSV files exist"
test -f model_profiling/out_<model>/runs/mac/mac_sme2_on/*_ops_stats.csv && echo "✓ Stats CSV files exist"

# Check summary is valid JSON and has required fields
python -c "
import json
with open('model_profiling/out_<model>/runs/mac/analysis_summary.json') as f:
    data = json.load(f)
    assert 'category_totals_ms' in data, 'Missing category_totals_ms'
    assert 'per_etdump' in data, 'Missing per_etdump'
    print('✓ Summary structure valid')
"

# Check summary has non-zero timing data
python -c "
import json
with open('model_profiling/out_<model>/runs/mac/analysis_summary.json') as f:
    data = json.load(f)
    totals = data.get('category_totals_ms', {})
    assert any(v > 0 for v in totals.values()), 'No timing data'
    print('✓ Summary has timing data')
"
```

**Expected outputs**:
- `model_profiling/out_<model>/runs/mac/analysis_summary.json` - Operator-level breakdown summary
- **CSV files generated from ETDump** (in same directory as ETDump files):
  - `<model_stem>_<experiment>_t<threads>_exec_all_runs_timeline.csv` - Timeline with all runs (used for latency statistics)
  - `<model_stem>_<experiment>_t<threads>_exec_run0_timeline.csv` - Timeline for run 0 (operator-level analysis)
  - `<model_stem>_<experiment>_t<threads>_exec_ops_stats.csv` - Aggregated operator statistics
  
The CSV files are **intermediate artifacts** that enable:
- **Verification**: You can inspect CSV files to verify the analysis
- **Reproducibility**: CSV files can be re-analyzed with different tools
- **Transparency**: Raw data is available for manual inspection

The `analysis_summary.json` contains:
  - `category_totals_ms`: Operator category timing breakdown (CONV, GEMM, Data Movement, etc.)
  - `per_etdump`: Per-experiment summaries (SME2-on, SME2-off) with CSV file paths
  - `csv_files`: List of generated CSV files
  - `csv_dir`: Directory containing CSV files

## Interpreting Results

### Category Breakdown

| Category | Typical Operations | What to Look For |
|----------|-------------------|------------------|
| **Convolution** | Conv2d, DepthwiseConv | Should decrease with SME2 (if accelerated) |
| **GEMM** | Linear, MatMul | Should decrease with SME2 (if accelerated) |
| **Data Movement** | Transpose, Permute, Copy | Often increases after SME2 (bottleneck shift) |
| **Elementwise** | Add, Mul, ReLU, etc. | Usually small, may increase slightly |
| **Other** | Everything else | Check for unexpected operations |

### Bottleneck Analysis

**Before SME2**: CONV/GEMM dominate timing
**After SME2**: Data Movement often becomes the bottleneck

This is **expected** - SME2 accelerates math, revealing data movement as the next bottleneck.

### SME2 Impact

Compare `category_totals_ms` between SME2-on and SME2-off experiments:
- **CONV/GEMM time decreases** → SME2 is working
- **Data Movement time increases (as %)** → Bottleneck shift (expected)
- **Overall latency decreases** → Successful optimization

## Failure Handling

| Issue | Symptom | Fix |
|-------|---------|-----|
| **Missing .etrecord** | Generic operator names | Analysis still works, but operator names may be generic. Re-export with .etrecord if needed. |
| **ETDump parsing errors** | Inspector errors | Check ETDump files are valid, re-run profiling if corrupted |
| **Import errors** | `Inspector not found` | Ensure ExecuTorch Inspector available: `python -c "from executorch.devtools.inspector import Inspector"` |
| **Empty results** | No timing data | Verify ETDump files contain events, check runner was built with event tracer enabled |
| **File not found** | Model .pte missing | Verify model path is correct, file exists |

## Kernel-Level Insights (Advanced)

If you ran trace-enabled profiling runs, the analysis may include kernel hints:
- `__neonsme2` → SME2 kernel used
- `sme2` → SME2-related operation
- `neon` → Standard NEON kernel

These hints are best-effort and depend on ExecuTorch build configuration.

## Best Practices

- **Compare SME2-on vs SME2-off** - Always analyze both to see the delta
- **Look for bottleneck shifts** - Data Movement increase after SME2 is expected
- **Check category percentages** - Not just absolute times, but relative shares
- **Validate ETDump first** - Ensure files are non-empty before analysis

## Implementation Checklist

- [ ] Virtual environment activated
- [ ] ETDump files exist in run directory
- [ ] Model .pte path correct
- [ ] Analysis script executed successfully
- [ ] Summary JSON exists and is valid
- [ ] Category totals have non-zero values
- [ ] Compared SME2-on vs SME2-off results

**References**:
- Analysis script: `model_profiling/scripts/analyze_results.py`
- ExecuTorch Inspector: [ExecuTorch documentation](https://docs.pytorch.org/executorch/stable/inspector.html)
- Learning path: `03-pipeline-and-analysis.md` (analysis section)

**Assets**:
- `model_profiling/scripts/analyze_results.py` - ETDump analysis script

**Next skill**: `06_validate_workflow.md` (optional, for end-to-end validation)
