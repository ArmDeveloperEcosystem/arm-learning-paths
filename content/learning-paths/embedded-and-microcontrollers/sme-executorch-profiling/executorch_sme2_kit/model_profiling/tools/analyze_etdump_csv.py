#!/usr/bin/env python3
"""
ETDump CSV Analysis Script

Analyzes ETDump timeline CSV files to calculate:
- End-to-end latency (from Method::execute duration)
- Operator category breakdown (GEMM, IGEMM, CONV, ELEMENTWISE, MEMORY, OTHER)
- Operator-specific latency reports
- Handles multiple executions and calculates averages

Validation:
    This script has been validated against ground truth results from
    SAM_SME2_performance_report.md:
    - EdgeTAM Image Encoder: Mac M4 shows 3.86x E2E speedup, 12.33x GEMM speedup
    - Android results show 5.11x E2E speedup, 9.27x GEMM speedup (different device)
    - Both show correct SME2 speedup pattern and operator categorization

Usage:
    # Single analysis
    python model_profiling/scripts/analyze_etdump_csv.py \
        --timeline-csv model_profiling/out_edgetam/android/edgetam_encoder_exec_run0_timeline.csv \
        --output-dir model_profiling/out_edgetam/android/ \
        --verbose

    # Comparison analysis
    python model_profiling/scripts/analyze_etdump_csv.py \
        --timeline-csv model_profiling/out_edgetam/android/edgetam_encoder_exec_run0_timeline.csv \
        --compare model_profiling/out_edgetam/android/edgetam_image_encoder_xnnpack_fp32_sme2_off_exec_run0_timeline.csv \
        --name1 "SME2-On" \
        --name2 "SME2-Off" \
        --output-dir model_profiling/out_edgetam/android/ \
        --verbose
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import pandas as pd


# Framework overhead operators to exclude from operator analysis
FRAMEWORK_OVERHEAD = {
    "Method::execute",
    "DELEGATE_CALL",
    "OPERATOR_CALL",
    "Program::load_method",
    "Method::init",
}


# --- Helpers and patterns -----------------------------------------------------

def _normalize(s: str) -> str:
    # lowercase; turn separators into spaces; collapse whitespace
    return re.sub(r"\s+", " ",
                 re.sub(r"[_:/\-\.]", " ", str(s).lower())
                ).strip()


# Backends/engines frequently visible in ET traces
_ENGINE_PATTERNS = {
    "QNNPACK": [r"\bqnnpack\b"],
    "XNNPACK": [r"\bxnnpack\b"],
    "cuDNN":   [r"\bcudnn\b"],
    "MPS":     [r"\bmps\b"],
    "Vulkan":  [r"\bvulkan\b"],
    "Metal":   [r"\bmetal\b"],
}


# Convolution algorithm identifiers
_ALGO_PATTERNS = {
    "IGEMM":   [r"\bigemm\b", r"\bimplicit[_\s-]?gemm\b"],
    "WINOGRAD":[r"\bwinograd\b"],
    "FFT":     [r"\bfft\b"],
    "DIRECT":  [r"\bdirect\b"],
}


# Ordered categories: most specific first to avoid false matches
_CATEGORY_PATTERNS = [
    # Convolutions and variants
    ("CONV", [
        r"\bconv(?:[123]d)?\b", r"\bconvolution\b",
        r"\bconv[_\s-]?transpose(?:[123]d)?\b", r"\bdeconv\b",
        r"\bdepthwise\b", r"\bdwconv\b", r"\bpointwise\b"
    ]),
    # GEMM & friends (avoid matching IGEMM)
    ("GEMM", [
        r"(?<!i)\bgemm\b", r"\bmatmul\b", r"\bmm\b", r"\bbmm\b",
        r"\baddmm\b", r"\blinear\b", r"\bfully[_\s-]?connected\b", r"\bdense\b",
        r"\beinsum\b"
    ]),
    ("POOL", [r"\b(?:avg|adaptive|max)?pool(?:[123]d)?\b"]),
    ("NORM", [r"\b(?:batch|layer|group|instance|rms)norm\b"]),
    ("ATTENTION", [r"\b(sdpa|flash[_\s-]?attn|multihead[_\s-]?attention|mha|attention)\b"]),
    ("EMBEDDING", [r"\bembedding(?:_bag)?\b"]),
    # Nonlinearities
    ("ACTIVATION", [
        r"\bgelu\b", r"\brelu6?\b", r"\bleaky[_\s-]?relu\b", r"\bprelu\b",
        r"\bsilu\b", r"\bswish\b", r"\bmish\b", r"\btanh\b", r"\bsigmoid\b",
        r"\bsoftplus\b", r"\bsoftsign\b", r"\belu\b", r"\bselu\b",
        r"\bhard[t ]?tanh\b", r"\bhard[_\s-]?sigmoid\b", r"\blog[_\s-]?softmax\b",
        r"\bsoftmax\b"
    ]),
    # Arithmetic & logical elementwise
    ("ELEMENTWISE", [
        r"\b(add|sub|mul|multiply|div|divide)\b",
        r"\b(pow|exp|log|abs|sqrt|rsqrt|sin|cos)\b",
        r"\b(where|max|min|clamp|clip|round|floor|ceil)\b",
        r"\b(and|or|xor|eq|ne|gt|ge|lt|le)\b",
        r"\bvmulcaddc\b"  # often appears in mobile kernels
    ]),
    ("REDUCTION", [r"\b(sum|mean|amax|amin|argmax|argmin|prod)\b"]),
    # Shape-only vs data movement
    ("RESHAPE", [r"\b(reshape|view|flatten|squeeze|unsqueeze)\b"]),
    ("DATA_MOVEMENT", [
        r"\b(transpose|permute|cat|concat|split|stack)\b",
        r"\b(gather|scatter|index[_\s-]?select|take)\b",
        r"\b(copy|clone|expand|tile|repeat|unfold|pad|roll|slice)\b"
    ]),
    ("RESIZE", [r"\b(upsample|interpolate|resize)\b"]),
    ("QUANT", [
        r"\b(quantize|dequantize|requantize|fake[_\s-]?quant)\b",
        r"\b(int8|uint8|q8)\b", r"\bper[_\s-](tensor|channel)\b"
    ]),
    ("RNN", [r"\b(lstm|gru|rnn)\b"]),
]


# Optional conv subtypes
_CONV_SUBTYPES = [
    ("DEPTHWISE", [r"\bdepthwise\b", r"\bdwconv\b"]),
    ("POINTWISE", [r"\bpointwise\b", r"\b1x1\b"]),
    ("TRANSPOSED", [r"\bconv[_\s-]?transpose\b", r"\bdeconv\b"]),
]


def _first_match(name: str, table) -> Optional[str]:
    for label, patterns in table.items() if isinstance(table, dict) else table:
        pats = patterns if isinstance(patterns, list) else patterns
        if any(re.search(p, name) for p in pats):
            return label
    return None


def categorize_operator(name: str) -> str:
    """
    Categorize operator based on name patterns.
    
    Returns the category string (e.g., "GEMM", "CONV", "ELEMENTWISE", etc.)
    Uses comprehensive pattern matching for accurate classification.
    
    Categories:
    - CONV: Convolution operations
    - GEMM: General Matrix Multiply (Fully Connected, Linear, etc.)
    - IGEMM: Implicit GEMM (Convolution with IGEMM algorithm)
    - POOL: Pooling operations
    - NORM: Normalization operations
    - ATTENTION: Attention mechanisms
    - EMBEDDING: Embedding operations
    - ACTIVATION: Activation functions
    - ELEMENTWISE: Element-wise arithmetic/logical operations
    - REDUCTION: Reduction operations
    - RESHAPE: Shape manipulation
    - DATA_MOVEMENT: Data movement operations
    - RESIZE: Resize/interpolation operations
    - QUANT: Quantization operations
    - RNN: RNN/LSTM/GRU operations
    - OTHER: Everything else
    """
    n = _normalize(name)
    
    # Detect backend/engine and algorithm first
    engine = _first_match(n, _ENGINE_PATTERNS)
    algo   = _first_match(n, _ALGO_PATTERNS)
    
    # Determine main category
    category = "OTHER"
    for cat, pats in _CATEGORY_PATTERNS:
        if any(re.search(p, n) for p in pats):
            category = cat
            break
    
    # Conv subtyping
    conv_subtype = None
    if category == "CONV":
        for sub, pats in _CONV_SUBTYPES:
            if any(re.search(p, n) for p in pats):
                conv_subtype = sub
                break
    
    # Heuristic: IGEMM almost always implies a convolutional kernel
    if algo == "IGEMM" and category != "CONV":
        category = "CONV"
    
    # Map some categories to existing ones for backward compatibility
    # ACTIVATION, POOL, NORM, etc. can be grouped as ELEMENTWISE or MEMORY
    # For now, keep them separate but we can aggregate later if needed
    
    return category


def analyze_timeline_csv(
    timeline_csv: Path,
    model_name: Optional[str] = None,
    output_dir: Optional[Path] = None,
    verbose: bool = False,
) -> Dict:
    """Analyze ETDump timeline CSV file.
    
    Args:
        timeline_csv: Path to timeline CSV file
        model_name: Optional model name for output files
        output_dir: Optional directory to save analysis results
        verbose: Print detailed output
        
    Returns:
        Dictionary with analysis results
    """
    if not timeline_csv.exists():
        raise FileNotFoundError(f"Timeline CSV not found: {timeline_csv}")
    
    # Read CSV
    df = pd.read_csv(timeline_csv)
    
    if verbose:
        print(f"📊 Analyzing: {timeline_csv}")
        print(f"   Total events: {len(df)}")
        print(f"   Unique run indices: {df['run_index'].nunique() if 'run_index' in df.columns else 1}")
    
    # Get model name from CSV if not provided
    if model_name is None:
        model_name = df['model_id'].iloc[0] if 'model_id' in df.columns else timeline_csv.stem
    
    # Filter for Method::execute to get E2E latency
    method_exec = df[df['name'] == 'Method::execute'].copy()
    
    if len(method_exec) == 0:
        raise ValueError("No 'Method::execute' event found in timeline CSV")
    
    # Calculate E2E latency per run
    e2e_latency_per_run = method_exec.groupby('run_index')['duration_ms'].sum()
    num_runs = len(e2e_latency_per_run)
    e2e_total_ms = e2e_latency_per_run.sum()
    e2e_avg_ms = e2e_latency_per_run.mean()
    e2e_min_ms = e2e_latency_per_run.min()
    e2e_max_ms = e2e_latency_per_run.max()
    
    if verbose:
        print(f"\n⏱️  End-to-End Latency (Method::execute)")
        print(f"   Runs: {num_runs}")
        print(f"   Total: {e2e_total_ms:.3f} ms")
        print(f"   Average: {e2e_avg_ms:.3f} ms")
        print(f"   Min: {e2e_min_ms:.3f} ms")
        print(f"   Max: {e2e_max_ms:.3f} ms")
    
    # Filter out framework overhead for operator analysis
    ops_df = df[~df['name'].isin(FRAMEWORK_OVERHEAD)].copy()
    
    # Categorize operators
    ops_df['category'] = ops_df['name'].apply(categorize_operator)
    
    # Calculate category-level statistics
    # Get all unique categories from the data
    all_categories = sorted(ops_df['category'].unique())
    
    category_stats = []
    for category in all_categories:
        cat_ops = ops_df[ops_df['category'] == category]
        if len(cat_ops) > 0:
            # Sum duration across all runs
            cat_total_ms = cat_ops['duration_ms'].sum()
            cat_avg_ms = cat_total_ms / num_runs
            cat_count = len(cat_ops['name'].unique())
            cat_pct = (cat_avg_ms / e2e_avg_ms) * 100 if e2e_avg_ms > 0 else 0
            
            category_stats.append({
                'category': category,
                'total_ms': cat_total_ms,
                'avg_ms': cat_avg_ms,
                'pct_of_e2e': cat_pct,
                'operator_count': cat_count,
            })
    
    # Sort by average time (descending)
    category_stats.sort(key=lambda x: x['avg_ms'], reverse=True)
    
    # Operator-level statistics
    operator_stats = []
    for name in ops_df['name'].unique():
        op_events = ops_df[ops_df['name'] == name]
        category = op_events['category'].iloc[0]
        op_total_ms = op_events['duration_ms'].sum()
        op_avg_ms = op_total_ms / num_runs
        op_count = len(op_events)
        op_pct = (op_avg_ms / e2e_avg_ms) * 100 if e2e_avg_ms > 0 else 0
        
        operator_stats.append({
            'operator': name,
            'category': category,
            'total_ms': op_total_ms,
            'avg_ms': op_avg_ms,
            'pct_of_e2e': op_pct,
            'event_count': op_count,
        })
    
    # Sort by average time
    operator_stats.sort(key=lambda x: x['avg_ms'], reverse=True)
    
    results = {
        'model_name': model_name,
        'num_runs': num_runs,
        'e2e_latency': {
            'total_ms': e2e_total_ms,
            'avg_ms': e2e_avg_ms,
            'min_ms': e2e_min_ms,
            'max_ms': e2e_max_ms,
        },
        'category_stats': category_stats,
        'operator_stats': operator_stats,
    }

    # Surface top contributors inside the OTHER bucket for quick diagnostics.
    other_ops = [op for op in operator_stats if op['category'] == 'OTHER']
    top_other_ops = other_ops[:2]
    results['top_other_ops'] = top_other_ops
    
    # Print summary
    if verbose:
        print(f"\n📋 Operator Category Breakdown")
        print(f"{'Category':<20} {'Avg Time (ms)':<15} {'% of E2E':<15} {'Op Count':<10}")
        print("-" * 60)
        for stat in sorted(category_stats, key=lambda x: x['avg_ms'], reverse=True):
            print(f"{stat['category']:<20} {stat['avg_ms']:>12.3f} ms {stat['pct_of_e2e']:>13.2f}% {stat.get('operator_count', 0):>10}")
        
        print(f"\n🔍 Top 10 Operators by Time")
        print(f"{'Operator':<50} {'Category':<15} {'Avg Time (ms)':<15} {'% of E2E':<15}")
        print("-" * 95)
        for op_stat in operator_stats[:10]:
            op_name = op_stat['operator'][:47] + '...' if len(op_stat['operator']) > 50 else op_stat['operator']
            print(f"{op_name:<50} {op_stat['category']:<15} {op_stat['avg_ms']:>12.3f} ms {op_stat['pct_of_e2e']:>13.2f}%")
        if top_other_ops:
            print(f"\n🕵️  Top OTHER operators")
            for idx, op_stat in enumerate(top_other_ops, start=1):
                op_name = op_stat['operator'][:60] + '...' if len(op_stat['operator']) > 63 else op_stat['operator']
                print(
                    f"   {idx}. {op_name} — {op_stat['avg_ms']:.3f} ms avg "
                    f"({op_stat['pct_of_e2e']:.2f}% of E2E across {op_stat['event_count']} events)"
                )
    
    # Save results if output directory provided
    if output_dir:
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
        
        # Save category summary
        category_df = pd.DataFrame(category_stats)
        category_csv = output_dir / f"{model_name}_category_summary.csv"
        category_df.to_csv(category_csv, index=False)
        if verbose:
            print(f"\n💾 Saved category summary: {category_csv}")
        
        # Save operator details
        operator_df = pd.DataFrame(operator_stats)
        operator_csv = output_dir / f"{model_name}_operator_details.csv"
        operator_df.to_csv(operator_csv, index=False)
        if verbose:
            print(f"💾 Saved operator details: {operator_csv}")
        
        # Save E2E latency summary
        e2e_df = pd.DataFrame([{
            'model_name': model_name,
            'num_runs': num_runs,
            'total_ms': e2e_total_ms,
            'avg_ms': e2e_avg_ms,
            'min_ms': e2e_min_ms,
            'max_ms': e2e_max_ms,
        }])
        e2e_csv = output_dir / f"{model_name}_e2e_latency.csv"
        e2e_df.to_csv(e2e_csv, index=False)
        if verbose:
            print(f"💾 Saved E2E latency: {e2e_csv}")

        if top_other_ops:
            other_df = pd.DataFrame(top_other_ops)
            other_csv = output_dir / f"{model_name}_other_top_ops.csv"
            other_df.to_csv(other_csv, index=False)
            if verbose:
                print(f"💾 Saved top OTHER ops: {other_csv}")
    
    return results


def compare_analyses(
    results1: Dict,
    results2: Dict,
    name1: str = "Config 1",
    name2: str = "Config 2",
    verbose: bool = False,
) -> Dict:
    """Compare two analysis results.
    
    Returns:
        Dictionary with comparison results
    """
    e2e1 = results1['e2e_latency']['avg_ms']
    e2e2 = results2['e2e_latency']['avg_ms']
    speedup = e2e2 / e2e1 if e2e1 > 0 else 0
    
    comparison = {
        'e2e_comparison': {
            name1: e2e1,
            name2: e2e2,
            'speedup': speedup,
        },
        'category_comparison': [],
    }
    
    # Compare categories
    cats1 = {s['category']: s for s in results1['category_stats']}
    cats2 = {s['category']: s for s in results2['category_stats']}
    
    all_categories = set(cats1.keys()) | set(cats2.keys())
    
    for category in sorted(all_categories):
        cat1 = cats1.get(category, {'avg_ms': 0})
        cat2 = cats2.get(category, {'avg_ms': 0})
        
        time1 = cat1['avg_ms']
        time2 = cat2['avg_ms']
        cat_speedup = time2 / time1 if time1 > 0 else 0
        
        comparison['category_comparison'].append({
            'category': category,
            f'{name1}_ms': time1,
            f'{name2}_ms': time2,
            'speedup': cat_speedup,
            f'{name1}_pct': cat1.get('pct_of_e2e', 0),
            f'{name2}_pct': cat2.get('pct_of_e2e', 0),
        })
    
    if verbose:
        print(f"\n🔄 Comparison: {name1} vs {name2}")
        print(f"{'Metric':<20} {name1:<20} {name2:<20} {'Speedup':<15}")
        print("-" * 75)
        print(f"{'E2E Latency':<20} {e2e1:>15.3f} ms {e2e2:>15.3f} ms {speedup:>13.3f}x")
        
        print(f"\n📊 Category Comparison")
        print(f"{'Category':<20} {name1:<20} {name2:<20} {'Speedup':<15}")
        print("-" * 75)
        for comp in sorted(comparison['category_comparison'], key=lambda x: x[name1 + '_ms'], reverse=True):
            print(f"{comp['category']:<20} {comp[name1 + '_ms']:>15.3f} ms {comp[name2 + '_ms']:>15.3f} ms {comp['speedup']:>13.3f}x")
    
    return comparison


def main():
    parser = argparse.ArgumentParser(
        description="Analyze ETDump timeline CSV files",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        '--timeline-csv',
        type=Path,
        required=True,
        help='Path to timeline CSV file',
    )
    parser.add_argument(
        '--output-dir',
        type=Path,
        help='Directory to save analysis results',
    )
    parser.add_argument(
        '--model-name',
        type=str,
        help='Model name for output files (default: from CSV model_id)',
    )
    parser.add_argument(
        '--compare',
        type=Path,
        help='Path to second timeline CSV for comparison',
    )
    parser.add_argument(
        '--name1',
        type=str,
        default='Config 1',
        help='Name for first configuration (for comparison)',
    )
    parser.add_argument(
        '--name2',
        type=str,
        default='Config 2',
        help='Name for second configuration (for comparison)',
    )
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Print detailed output',
    )
    
    args = parser.parse_args()
    
    try:
        # Analyze first CSV
        results1 = analyze_timeline_csv(
            args.timeline_csv,
            model_name=args.model_name,
            output_dir=args.output_dir,
            verbose=args.verbose,
        )
        
        # Compare if second CSV provided
        if args.compare:
            results2 = analyze_timeline_csv(
                args.compare,
                model_name=args.model_name,
                output_dir=args.output_dir,
                verbose=args.verbose,
            )
            
            comparison = compare_analyses(
                results1,
                results2,
                name1=args.name1,
                name2=args.name2,
                verbose=args.verbose,
            )
            
            # Save comparison if output directory provided
            if args.output_dir:
                comp_df = pd.DataFrame(comparison['category_comparison'])
                comp_csv = args.output_dir / f"{results1['model_name']}_comparison.csv"
                comp_df.to_csv(comp_csv, index=False)
                if args.verbose:
                    print(f"\n💾 Saved comparison: {comp_csv}")
        
        return 0
        
    except Exception as e:
        print(f"❌ Error: {e}", file=sys.stderr)
        if args.verbose:
            import traceback
            traceback.print_exc()
        return 1


if __name__ == '__main__':
    sys.exit(main())
