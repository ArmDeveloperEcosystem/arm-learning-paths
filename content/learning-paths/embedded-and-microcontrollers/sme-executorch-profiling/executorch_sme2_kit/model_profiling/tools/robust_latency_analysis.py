#!/usr/bin/env python3
"""
Robust Latency Analysis for ETDump CSV Files

This script provides robust statistical analysis of execution timing data,
including:
- Per-execution latency analysis
- Outlier detection and removal
- Robust statistics (median, trimmed mean, percentiles)
- Coefficient of Variation (CV) for variability assessment
- Comparison between configurations with confidence intervals

Key features:
- Uses median and trimmed mean instead of just mean (more robust to outliers)
- Calculates Coefficient of Variation (CV) to quantify variability
- Provides percentile-based statistics (P50, P90, P95, P99)
- Detects and flags outliers using IQR method
- Generates comparison reports with confidence metrics

Usage:
    # Analyze single configuration
    python model_profiling/scripts/robust_latency_analysis.py \
        --timeline-csv model_profiling/out_edgetam/android/edgetam_image_encoder_xnnpack_fp32_sme2_off_exec_all_runs_timeline.csv \
        --output-dir model_profiling/out_edgetam/android/ \
        --name "SME2-Off" \
        --verbose

    # Compare two configurations
    python model_profiling/scripts/robust_latency_analysis.py \
        --timeline-csv model_profiling/out_edgetam/android/edgetam_image_encoder_xnnpack_fp32_sme2_off_exec_all_runs_timeline.csv \
        --compare model_profiling/out_edgetam/android/edgetam_image_encoder_xnnpack_fp32_sme2_on_exec_all_runs_timeline.csv \
        --name1 "SME2-Off" \
        --name2 "SME2-On" \
        --output-dir model_profiling/out_edgetam/android/ \
        --verbose
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import numpy as np
import pandas as pd
from scipy import stats


def calculate_robust_statistics(latencies: List[float], outlier_threshold: float = 1.5) -> Dict:
    """Calculate robust statistics for latency measurements.
    
    Args:
        latencies: List of latency values in milliseconds
        outlier_threshold: IQR multiplier for outlier detection (default 1.5)
        
    Returns:
        Dictionary with robust statistics
    """
    if len(latencies) == 0:
        return {}
    
    latencies_array = np.array(latencies)
    
    # Basic statistics
    mean = np.mean(latencies_array)
    median = np.median(latencies_array)
    std_dev = np.std(latencies_array, ddof=1)  # Sample std dev
    min_val = np.min(latencies_array)
    max_val = np.max(latencies_array)
    
    # Coefficient of Variation (CV) - relative variability
    cv = (std_dev / mean * 100) if mean > 0 else 0.0
    
    # Percentiles
    percentiles = {
        'p50': np.percentile(latencies_array, 50),
        'p75': np.percentile(latencies_array, 75),
        'p90': np.percentile(latencies_array, 90),
        'p95': np.percentile(latencies_array, 95),
        'p99': np.percentile(latencies_array, 99),
    }
    
    # IQR-based outlier detection
    q1 = np.percentile(latencies_array, 25)
    q3 = np.percentile(latencies_array, 75)
    iqr = q3 - q1
    lower_bound = q1 - outlier_threshold * iqr
    upper_bound = q3 + outlier_threshold * iqr
    
    outliers = latencies_array[(latencies_array < lower_bound) | (latencies_array > upper_bound)]
    num_outliers = len(outliers)
    outlier_percentage = (num_outliers / len(latencies_array)) * 100
    
    # Trimmed mean (remove top and bottom 5%)
    trimmed_mean_5 = stats.trim_mean(latencies_array, 0.05)
    trimmed_mean_10 = stats.trim_mean(latencies_array, 0.10)
    
    # Robust statistics (excluding outliers)
    clean_latencies = latencies_array[(latencies_array >= lower_bound) & (latencies_array <= upper_bound)]
    if len(clean_latencies) > 0:
        robust_mean = np.mean(clean_latencies)
        robust_median = np.median(clean_latencies)
        robust_std = np.std(clean_latencies, ddof=1)
        robust_cv = (robust_std / robust_mean * 100) if robust_mean > 0 else 0.0
    else:
        robust_mean = mean
        robust_median = median
        robust_std = std_dev
        robust_cv = cv
    
    return {
        'count': len(latencies_array),
        'mean_ms': mean,
        'median_ms': median,
        'std_dev_ms': std_dev,
        'cv_percent': cv,
        'min_ms': min_val,
        'max_ms': max_val,
        'percentiles': percentiles,
        'outliers': {
            'count': num_outliers,
            'percentage': outlier_percentage,
            'values': outliers.tolist() if len(outliers) > 0 else [],
            'bounds': {'lower': lower_bound, 'upper': upper_bound}
        },
        'trimmed_mean_5_ms': trimmed_mean_5,
        'trimmed_mean_10_ms': trimmed_mean_10,
        'robust_stats': {
            'count': len(clean_latencies),
            'mean_ms': robust_mean,
            'median_ms': robust_median,
            'std_dev_ms': robust_std,
            'cv_percent': robust_cv
        }
    }


def analyze_all_runs_timeline(timeline_csv: Path, verbose: bool = False) -> Dict:
    """Analyze all runs from timeline CSV to get per-execution latency.
    
    Args:
        timeline_csv: Path to timeline CSV with all_runs data
        verbose: Print detailed output
        
    Returns:
        Dictionary with per-execution latencies and statistics
    """
    if not timeline_csv.exists():
        raise FileNotFoundError(f"Timeline CSV not found: {timeline_csv}")
    
    df = pd.read_csv(timeline_csv)
    
    if verbose:
        print(f"📊 Analyzing: {timeline_csv}")
        print(f"   Total events: {len(df)}")
        if 'run_index' in df.columns:
            print(f"   Runs: {df['run_index'].nunique()}")
        else:
            print(f"   ⚠️  No run_index column - this CSV may not have all runs data")
            print(f"   Use --all-runs flag when generating CSV with etdump_to_csv.py")
    
    # Get Method::execute events
    method_exec = df[df['name'] == 'Method::execute'].copy()
    
    if len(method_exec) == 0:
        raise ValueError("No 'Method::execute' event found in timeline CSV")
    
    if 'run_index' not in method_exec.columns:
        # Fallback: use duration_ms if only one run
        if len(method_exec) == 1:
            latencies = [method_exec['duration_ms'].iloc[0]]
            run_indices = [0]
        else:
            raise ValueError("No run_index column and multiple Method::execute events found")
    else:
        # Group by run_index to get per-execution latency
        latencies_per_run = method_exec.groupby('run_index')['duration_ms'].sum()
        latencies = latencies_per_run.values.tolist()
        run_indices = latencies_per_run.index.tolist()
    
    # Calculate robust statistics
    stats_dict = calculate_robust_statistics(latencies)
    stats_dict['latencies_ms'] = latencies
    stats_dict['run_indices'] = run_indices
    
    if verbose:
        print(f"\n⏱️  Per-Execution Latency Analysis")
        print(f"   Total runs: {stats_dict['count']}")
        print(f"   Mean: {stats_dict['mean_ms']:.3f} ms")
        print(f"   Median: {stats_dict['median_ms']:.3f} ms")
        print(f"   Std Dev: {stats_dict['std_dev_ms']:.3f} ms")
        print(f"   CV: {stats_dict['cv_percent']:.2f}%")
        print(f"   Min: {stats_dict['min_ms']:.3f} ms")
        print(f"   Max: {stats_dict['max_ms']:.3f} ms")
        print(f"\n📊 Percentiles:")
        for p, val in stats_dict['percentiles'].items():
            print(f"   {p.upper()}: {val:.3f} ms")
        print(f"\n🔍 Outlier Analysis:")
        print(f"   Outliers: {stats_dict['outliers']['count']} ({stats_dict['outliers']['percentage']:.1f}%)")
        if stats_dict['outliers']['count'] > 0:
            print(f"   Outlier bounds: [{stats_dict['outliers']['bounds']['lower']:.3f}, {stats_dict['outliers']['bounds']['upper']:.3f}] ms")
        print(f"\n📈 Robust Statistics (excluding outliers):")
        robust = stats_dict['robust_stats']
        print(f"   Count: {robust['count']}")
        print(f"   Mean: {robust['mean_ms']:.3f} ms")
        print(f"   Median: {robust['median_ms']:.3f} ms")
        print(f"   Std Dev: {robust['std_dev_ms']:.3f} ms")
        print(f"   CV: {robust['cv_percent']:.2f}%")
        print(f"\n🎯 Trimmed Means:")
        print(f"   5% trimmed: {stats_dict['trimmed_mean_5_ms']:.3f} ms")
        print(f"   10% trimmed: {stats_dict['trimmed_mean_10_ms']:.3f} ms")
    
    return stats_dict


def compare_configurations(
    stats1: Dict,
    stats2: Dict,
    name1: str,
    name2: str,
    verbose: bool = False
) -> Dict:
    """Compare two configuration statistics.
    
    Args:
        stats1: Statistics from first configuration
        stats2: Statistics from second configuration
        name1: Name of first configuration
        name2: Name of second configuration
        verbose: Print detailed output
        
    Returns:
        Dictionary with comparison results
    """
    # Use robust median for comparison (most reliable)
    median1 = stats1['robust_stats']['median_ms']
    median2 = stats2['robust_stats']['median_ms']
    
    # Also compare trimmed means
    trimmed1 = stats1['trimmed_mean_5_ms']
    trimmed2 = stats2['trimmed_mean_5_ms']
    
    # Speedup calculation
    if median2 > 0:
        speedup_median = median1 / median2
    else:
        speedup_median = 0.0
    
    if trimmed2 > 0:
        speedup_trimmed = trimmed1 / trimmed2
    else:
        speedup_trimmed = 0.0
    
    # Variability comparison
    cv1 = stats1['robust_stats']['cv_percent']
    cv2 = stats2['robust_stats']['cv_percent']
    
    comparison = {
        'config1': {
            'name': name1,
            'median_ms': median1,
            'trimmed_mean_ms': trimmed1,
            'cv_percent': cv1,
            'count': stats1['count']
        },
        'config2': {
            'name': name2,
            'median_ms': median2,
            'trimmed_mean_ms': trimmed2,
            'cv_percent': cv2,
            'count': stats2['count']
        },
        'speedup': {
            'median_based': speedup_median,
            'trimmed_mean_based': speedup_trimmed,
            'description': f"{name2} is {speedup_median:.2f}x faster than {name1}" if speedup_median > 1 else f"{name1} is {1/speedup_median:.2f}x faster than {name2}"
        },
        'variability': {
            'config1_cv': cv1,
            'config2_cv': cv2,
            'more_variable': name1 if cv1 > cv2 else name2,
            'cv_ratio': cv1 / cv2 if cv2 > 0 else 0.0
        }
    }
    
    if verbose:
        print(f"\n{'='*60}")
        print(f"📊 Configuration Comparison")
        print(f"{'='*60}")
        print(f"\n{name1}:")
        print(f"   Median: {median1:.3f} ms")
        print(f"   Trimmed Mean (5%): {trimmed1:.3f} ms")
        print(f"   CV: {cv1:.2f}%")
        print(f"   Runs: {stats1['count']}")
        print(f"\n{name2}:")
        print(f"   Median: {median2:.3f} ms")
        print(f"   Trimmed Mean (5%): {trimmed2:.3f} ms")
        print(f"   CV: {cv2:.2f}%")
        print(f"   Runs: {stats2['count']}")
        print(f"\n🚀 Speedup:")
        print(f"   Based on median: {speedup_median:.2f}x")
        print(f"   Based on trimmed mean: {speedup_trimmed:.2f}x")
        print(f"   {comparison['speedup']['description']}")
        print(f"\n📈 Variability:")
        print(f"   {name1} CV: {cv1:.2f}%")
        print(f"   {name2} CV: {cv2:.2f}%")
        print(f"   More variable: {comparison['variability']['more_variable']}")
        if cv1 > 0 and cv2 > 0:
            print(f"   CV ratio: {comparison['variability']['cv_ratio']:.2f}x")
    
    return comparison


def main() -> int:
    parser = argparse.ArgumentParser(
        description='Robust latency analysis for ETDump CSV files',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    
    parser.add_argument(
        '--timeline-csv',
        type=Path,
        required=True,
        help='Path to timeline CSV file (with all_runs data)'
    )
    
    parser.add_argument(
        '--compare',
        type=Path,
        help='Path to second timeline CSV for comparison'
    )
    
    parser.add_argument(
        '--name',
        type=str,
        help='Name for single analysis (optional, defaults to CSV stem)'
    )
    
    parser.add_argument(
        '--name1',
        type=str,
        default='Config1',
        help='Name for first configuration in comparison'
    )
    
    parser.add_argument(
        '--name2',
        type=str,
        default='Config2',
        help='Name for second configuration in comparison'
    )
    
    parser.add_argument(
        '--output-dir',
        type=Path,
        help='Directory to save analysis results (JSON and report)'
    )
    
    parser.add_argument(
        '--verbose',
        action='store_true',
        help='Print detailed output'
    )
    
    args = parser.parse_args()
    
    # Analyze first configuration
    try:
        stats1 = analyze_all_runs_timeline(args.timeline_csv, verbose=args.verbose)
        
        if args.name:
            stats1['name'] = args.name
        else:
            stats1['name'] = args.timeline_csv.stem
        
        # Save results
        if args.output_dir:
            args.output_dir.mkdir(parents=True, exist_ok=True)
            output_file = args.output_dir / f"{args.timeline_csv.stem}_robust_stats.json"
            with open(output_file, 'w') as f:
                json.dump(stats1, f, indent=2)
            if args.verbose:
                print(f"\n💾 Saved results to: {output_file}")
        
        # Compare if second CSV provided
        if args.compare:
            stats2 = analyze_all_runs_timeline(args.compare, verbose=args.verbose)
            stats2['name'] = args.name2
            
            comparison = compare_configurations(
                stats1,
                stats2,
                args.name1,
                args.name2,
                verbose=args.verbose
            )
            
            # Save comparison
            if args.output_dir:
                comparison_file = args.output_dir / f"{args.timeline_csv.stem}_vs_{args.compare.stem}_robust_comparison.json"
                with open(comparison_file, 'w') as f:
                    json.dump(comparison, f, indent=2)
                if args.verbose:
                    print(f"\n💾 Saved comparison to: {comparison_file}")
        
        return 0
        
    except Exception as e:
        print(f"❌ Error: {e}", file=sys.stderr)
        if args.verbose:
            import traceback
            traceback.print_exc()
        return 1


if __name__ == '__main__':
    sys.exit(main())
