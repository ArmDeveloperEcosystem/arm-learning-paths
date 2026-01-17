#!/usr/bin/env python3
"""Generate profiling report from CSV files."""

import argparse
import csv
import json
import platform
import statistics
import subprocess
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional


def load_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def load_csv(csv_path: Path) -> List[Dict[str, Any]]:
    """Load CSV file and return as list of dictionaries."""
    if not csv_path.exists():
        raise FileNotFoundError(f"CSV file not found: {csv_path}")
    
    rows = []
    with csv_path.open(encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)
    return rows


def extract_latencies_from_timeline_csv(timeline_csv: Path) -> List[float]:
    """Extract per-run latencies from timeline CSV file."""
    rows = load_csv(timeline_csv)
    
    run_totals = defaultdict(float)
    for row in rows:
        name = row.get("name", "")
        if name not in ["Method::init", "Program::load_method"]:
            run_idx = int(row.get("run_index", 0))
            duration_ms = float(row.get("duration_ms", 0) or 0)
            run_totals[run_idx] += duration_ms
    
    if run_totals:
        max_run = max(run_totals.keys())
        return [run_totals[i] for i in range(max_run + 1) if i in run_totals]
    else:
        total = sum(float(row.get("duration_ms", 0) or 0) for row in rows 
                   if row.get("name", "") not in ["Method::init", "Program::load_method"])
        return [total] if total > 0 else []


def categorize_op(op_name: str) -> str:
    """Categorize operator name into category."""
    if not op_name or not isinstance(op_name, str):
        return "Other"
    s = op_name.lower()
    if "conv" in s:
        return "Convolution"
    if "matmul" in s or "linear" in s or "gemm" in s or "igemm" in s:
        return "GEMM"
    if "transpose" in s or "reshape" in s or "copy" in s or "convert" in s or "pad" in s:
        return "Data Movement"
    if any(k in s for k in ["relu", "gelu", "sigmoid", "tanh", "hardtanh", "hardswish", "hard_swish", "clamp", "add", "mul", "sub", "div"]):
        return "Elementwise"
    return "Other"


def extract_category_totals_from_stats_csv(stats_csv: Path) -> Dict[str, float]:
    """Extract total time by operator category from stats CSV file."""
    rows = load_csv(stats_csv)
    category_totals = defaultdict(float)
    
    for row in rows:
        op_type = row.get("type", "")
        total_ms = float(row.get("total_ms", 0) or 0)
        cat = categorize_op(op_type)
        category_totals[cat] += total_ms
    
    return dict(category_totals)


def calculate_statistics(latencies: List[float]) -> Dict[str, float]:
    """Calculate statistical metrics from latency list."""
    if not latencies:
        return {}
    return {
        "mean": statistics.mean(latencies),
        "median": statistics.median(latencies),
        "min": min(latencies),
        "max": max(latencies),
        "stdev": statistics.stdev(latencies) if len(latencies) > 1 else 0.0,
    }


def find_csv_files(run_dir: Path) -> Dict[str, Dict[str, Path]]:
    """Find CSV files in run directory (same directory as ETDump files)."""
    csv_files = {}
    
    # Find CSV files in same directories as ETDump files
    for timeline_csv in run_dir.glob("**/*_run0_timeline.csv"):
        exp_name = timeline_csv.parent.name if timeline_csv.parent != run_dir else timeline_csv.stem.replace("_exec_run0_timeline", "")
        if exp_name not in csv_files:
            csv_files[exp_name] = {}
        csv_files[exp_name]["timeline"] = timeline_csv
    
    for stats_csv in run_dir.glob("**/*_ops_stats.csv"):
        exp_name = stats_csv.parent.name if stats_csv.parent != run_dir else stats_csv.stem.replace("_exec_ops_stats", "")
        if exp_name not in csv_files:
            csv_files[exp_name] = {}
        csv_files[exp_name]["stats"] = stats_csv
    
    return csv_files


def get_device_info() -> Dict[str, str]:
    """Get device/platform information."""
    info = {
        "architecture": platform.machine(),
        "platform": platform.system(),
        "platform_version": platform.version(),
    }
    
    if platform.system() == "Darwin":
        try:
            result = subprocess.run(["sw_vers"], capture_output=True, text=True, timeout=5)
            if result.returncode == 0:
                for line in result.stdout.strip().split("\n"):
                    if "ProductName:" in line:
                        info["os"] = line.split(":", 1)[1].strip()
                    elif "ProductVersion:" in line:
                        info["os_version"] = line.split(":", 1)[1].strip()
        except Exception:
            pass
    
    return info


def generate_report(run_dir: Path, output_path: Optional[Path] = None, title: Optional[str] = None) -> str:
    """Generate markdown report from CSV files."""
    run_dir = run_dir.resolve()
    
    # Find CSV files
    csv_files = find_csv_files(run_dir)
    if not csv_files:
        raise FileNotFoundError(
            f"No CSV files found in {run_dir}. "
            f"Run 'python model_profiling/scripts/analyze_results.py --run-dir {run_dir}' first."
        )
    
    # Load manifest
    manifest_path = run_dir / "manifest.json"
    manifest_data = load_json(manifest_path) if manifest_path.exists() else {}
    
    # Load config
    config_path = None
    config_data = {}
    if manifest_data.get("config"):
        config_path = Path(manifest_data["config"])
        if config_path.exists():
            config_data = load_json(config_path)
    
    # Get model name
    model_path = None
    if manifest_data.get("model"):
        model_path = Path(manifest_data["model"])
        model_name = model_path.stem
    else:
        model_name = "Unknown"
    
    # Process CSV files
    experiments_data = []
    for exp_name, csv_info in csv_files.items():
        timeline_csv = csv_info.get("timeline")
        stats_csv = csv_info.get("stats")
        
        latencies = []
        if timeline_csv:
            try:
                latencies = extract_latencies_from_timeline_csv(timeline_csv)
            except Exception:
                pass
        
        stats = calculate_statistics(latencies) if latencies else {}
        
        category_totals = {}
        if stats_csv:
            try:
                category_totals = extract_category_totals_from_stats_csv(stats_csv)
            except Exception:
                pass
        
        experiments_data.append({
            "name": exp_name,
            "timeline_csv": timeline_csv,
            "stats_csv": stats_csv,
            "latencies": latencies,
            "stats": stats,
            "category_totals": category_totals,
        })
    
    # Build report
    lines = []
    lines.append(f"# {title or f'Profiling Report: {model_name}'}\n")
    lines.append(f"**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    lines.append("")
    
    # Metadata
    lines.append("## Metadata\n")
    if model_path:
        lines.append(f"- **Model**: `{model_path.name}`")
        lines.append(f"- **Model Path**: `{model_path}`")
    lines.append(f"- **Run Directory**: `{run_dir}`")
    
    if config_path:
        lines.append(f"- **Config File**: `{config_path}`")
        
        # Runner paths from config
        experiments_config = config_data.get("experiments", [])
        if experiments_config:
            lines.append("")
            lines.append("### Runner Paths\n")
            for exp_config in experiments_config:
                exp_name = exp_config.get("name", "unknown")
                runner_path = exp_config.get("runner_path", "")
                if runner_path:
                    # Resolve full path - try multiple possible locations
                    runner_full_path = None
                    if Path(runner_path).is_absolute():
                        runner_full_path = Path(runner_path)
                    else:
                        # Try different possible repo root locations
                        possible_roots = [
                            run_dir.parent.parent.parent.parent,  # repo root (out_<model>/runs/mac -> repo)
                            run_dir.parent.parent.parent,  # model_profiling level
                        ]
                        for repo_root in possible_roots:
                            if (repo_root / "executorch" / runner_path).exists():
                                runner_full_path = (repo_root / "executorch" / runner_path).resolve()
                                break
                            elif (repo_root / runner_path).exists():
                                runner_full_path = (repo_root / runner_path).resolve()
                                break
                    
                    lines.append(f"- **{exp_name}**:")
                    lines.append(f"  - Relative path: `{runner_path}`")
                    if runner_full_path and runner_full_path.exists():
                        lines.append(f"  - Full path: `{runner_full_path}`")
                        lines.append(f"  - Status: ✓ Executable")
                        try:
                            size_mb = runner_full_path.stat().st_size / (1024 * 1024)
                            lines.append(f"  - Size: {size_mb:.2f} MB")
                        except Exception:
                            pass
                    elif runner_full_path:
                        lines.append(f"  - Full path: `{runner_full_path}`")
                        lines.append(f"  - Status: ⚠️ Not found")
    
    # Device info
    lines.append("")
    lines.append("### Device Information\n")
    device_info = get_device_info()
    lines.append(f"- **Architecture**: {device_info.get('architecture', 'Unknown')}")
    lines.append(f"- **Platform**: {device_info.get('platform', 'Unknown')}")
    lines.append(f"- **Platform Version**: {device_info.get('platform_version', 'Unknown')}")
    if device_info.get("os"):
        lines.append(f"- **OS**: {device_info['os']}")
    if device_info.get("os_version"):
        lines.append(f"- **OS Version**: {device_info['os_version']}")
    
    # ExecuTorch info
    lines.append("")
    lines.append("### ExecuTorch Information\n")
    if manifest_data.get("executorch", {}).get("sha"):
        et_info = manifest_data["executorch"]
        lines.append(f"- **ExecuTorch SHA**: `{et_info['sha']}`")
        lines.append(f"- **ExecuTorch Status**: {'⚠️ Dirty' if et_info.get('dirty') else '✓ Clean'}")
    
    lines.append("")
    lines.append("### Analysis Information\n")
    lines.append(f"- **CSV Files Analyzed**: {len(experiments_data)}")
    lines.append("")
    
    # Latency Comparison
    lines.append("## Latency Comparison (SME2-On vs SME2-Off)\n")
    lines.append("| Metric | SME2-On | SME2-Off | Improvement |")
    lines.append("|--------|---------|----------|-------------|")
    
    sme2_on_data = None
    sme2_off_data = None
    for exp_data in experiments_data:
        exp_name = exp_data["name"].lower()
        if "sme2_on" in exp_name or "sme2-on" in exp_name:
            sme2_on_data = exp_data
        elif "sme2_off" in exp_name or "sme2-off" in exp_name:
            sme2_off_data = exp_data
    
    if sme2_on_data and sme2_off_data:
        on_stats = sme2_on_data["stats"]
        off_stats = sme2_off_data["stats"]
        
        if on_stats and off_stats:
            for metric_name, metric_key in [("Median", "median"), ("Mean", "mean"), ("Min", "min"), ("Max", "max")]:
                on_val = on_stats.get(metric_key, 0)
                off_val = off_stats.get(metric_key, 0)
                improvement = ((off_val - on_val) / off_val * 100) if off_val > 0 else 0
                improvement_str = f"{improvement:+.2f}%" if improvement != 0 else "0.00%"
                lines.append(f"| **{metric_name} Latency** | {on_val:.3f} ms | {off_val:.3f} ms | {improvement_str} |")
            
            on_stdev = on_stats.get("stdev", 0)
            off_stdev = off_stats.get("stdev", 0)
            lines.append(f"| **Std Dev** | {on_stdev:.3f} ms | {off_stdev:.3f} ms | - |")
    
    lines.append("")
    
    # Category Breakdown
    lines.append("## Operator Category Breakdown\n")
    total_category_totals = defaultdict(float)
    for exp_data in experiments_data:
        for cat, ms in exp_data["category_totals"].items():
            total_category_totals[cat] += ms
    
    if total_category_totals:
        lines.append("### Total Time by Category (across all experiments)\n")
        lines.append("| Category | Time (ms) |")
        lines.append("|----------|-----------|")
        for cat, ms in sorted(total_category_totals.items(), key=lambda x: x[1], reverse=True):
            lines.append(f"| **{cat}** | {ms:.3f} |")
        lines.append("")
    
    # Generated Artifacts
    lines.append("## Generated Artifacts\n")
    lines.append("### CSV Files (Source Data for Report)\n")
    lines.append("| File | Description |")
    lines.append("|------|-------------|")
    
    seen_csv = set()
    for exp_data in experiments_data:
        for csv_type, csv_path in [("timeline", exp_data.get("timeline_csv")), ("stats", exp_data.get("stats_csv"))]:
            if csv_path:
                csv_name = csv_path.name
                if csv_name not in seen_csv:
                    desc = "Timeline CSV (per-run operator timing)" if csv_type == "timeline" else "Stats CSV (aggregated operator statistics)"
                    lines.append(f"| `{csv_name}` | {desc} |")
                    seen_csv.add(csv_name)
    
    lines.append("")
    
    # Summary
    lines.append("## Summary\n")
    if sme2_on_data and sme2_off_data:
        on_stats = sme2_on_data["stats"]
        off_stats = sme2_off_data["stats"]
        if on_stats and off_stats:
            on_median = on_stats.get("median", 0)
            off_median = off_stats.get("median", 0)
            improvement = ((off_median - on_median) / off_median * 100) if off_median > 0 else 0
            
            if improvement > 0:
                lines.append(f"✅ **SME2 acceleration shows {improvement:.2f}% improvement** in median latency.")
            elif improvement < 0:
                lines.append(f"⚠️  **SME2 shows {abs(improvement):.2f}% regression** in median latency.")
            else:
                lines.append("ℹ️  **No significant difference** between SME2-on and SME2-off.")
    
    lines.append("")
    lines.append("---")
    lines.append("*Report generated from CSV files (derived from ETDump)*")
    
    report_content = "\n".join(lines)
    
    if output_path:
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(report_content, encoding="utf-8")
        print(f"Report written to: {output_path}")
    else:
        print(report_content)
    
    return report_content


def main():
    parser = argparse.ArgumentParser(description="Generate profiling report from CSV files")
    parser.add_argument("--run-dir", type=Path, required=True, help="Run output directory")
    parser.add_argument("--out", type=Path, default=None, help="Output markdown file (default: <run-dir>/report.md)")
    parser.add_argument("--title", type=str, default=None, help="Report title")
    args = parser.parse_args()
    
    run_dir = args.run_dir.resolve()
    output_path = args.out or (run_dir / "report.md")
    
    try:
        generate_report(run_dir, output_path, args.title)
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"Error generating report: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
