#!/usr/bin/env python3
"""Generate combined profiling report from multiple platforms (macOS + Android)."""

import argparse
import sys
from pathlib import Path
from typing import Dict, List, Optional

# Add parent directory to path
ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from model_profiling.scripts.generate_report import (
    find_csv_files,
    extract_latencies_from_timeline_csv,
    extract_category_totals_from_stats_csv,
    calculate_statistics,
    load_json,
)


def generate_combined_report(
    mac_dir: Path,
    android_dir: Path,
    output_path: Path,
    model_name: str = "edgetam_image_encoder_xnnpack_fp32",
) -> None:
    """Generate combined report from macOS and Android data."""
    from datetime import datetime

    platforms_data = {}

    # Process macOS
    if mac_dir.exists():
        csv_files = find_csv_files(mac_dir)
        if csv_files:
            metrics_path = mac_dir / "metrics.json"
            metrics_data = load_json(metrics_path) if metrics_path.exists() else {}

            experiments = {}
            for exp_name, csv_info in csv_files.items():
                all_runs_csv = csv_info.get("all_runs_timeline") or csv_info.get("timeline")
                stats_csv = csv_info.get("stats")

                latencies = []
                if all_runs_csv:
                    try:
                        latencies = extract_latencies_from_timeline_csv(all_runs_csv)
                    except Exception:
                        pass

                if not latencies and metrics_data.get("results"):
                    for result in metrics_data["results"]:
                        if result.get("experiment") == exp_name:
                            metrics = result.get("metrics", {})
                            latencies = metrics.get("latency_ms") or metrics.get("avg_latency_ms", [])
                            break

                stats = calculate_statistics(latencies) if latencies else {}
                category_totals = {}
                if stats_csv:
                    try:
                        category_totals = extract_category_totals_from_stats_csv(stats_csv)
                    except Exception:
                        pass

                experiments[exp_name] = {
                    "latencies": latencies,
                    "stats": stats,
                    "category_totals": category_totals,
                }

            platforms_data["macOS"] = experiments

    # Process Android
    if android_dir.exists():
        csv_files = find_csv_files(android_dir)
        if csv_files:
            metrics_path = android_dir / "metrics.json"
            metrics_data = load_json(metrics_path) if metrics_path.exists() else {}

            experiments = {}
            for exp_name, csv_info in csv_files.items():
                all_runs_csv = csv_info.get("all_runs_timeline") or csv_info.get("timeline")
                stats_csv = csv_info.get("stats")

                latencies = []
                if all_runs_csv:
                    try:
                        latencies = extract_latencies_from_timeline_csv(all_runs_csv)
                    except Exception:
                        pass

                if not latencies and metrics_data.get("results"):
                    for result in metrics_data["results"]:
                        if result.get("experiment") == exp_name:
                            metrics = result.get("metrics", {})
                            latencies = metrics.get("latency_ms") or metrics.get("avg_latency_ms", [])
                            break

                stats = calculate_statistics(latencies) if latencies else {}
                category_totals = {}
                if stats_csv:
                    try:
                        category_totals = extract_category_totals_from_stats_csv(stats_csv)
                    except Exception:
                        pass

                experiments[exp_name] = {
                    "latencies": latencies,
                    "stats": stats,
                    "category_totals": category_totals,
                }

            platforms_data["Android"] = experiments

    if not platforms_data:
        raise FileNotFoundError("No data found in either macOS or Android directories")

    # Generate report
    lines = []
    lines.append(f"# Profiling Report: {model_name} (macOS + Android)\n")
    lines.append(f"**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    lines.append("")

    # Metadata
    lines.append("## Metadata\n")
    lines.append(f"- **Model**: `{model_name}.pte`")
    lines.append(f"- **Platforms**: macOS, Android")
    lines.append("")

    # Cross-platform latency comparison
    lines.append("## Cross-Platform Latency Comparison\n")
    lines.append("| Platform | Experiment | Median (ms) | Mean (ms) | Min (ms) | Max (ms) | Std Dev (ms) |")
    lines.append("|----------|-----------|-------------|-----------|----------|----------|--------------|")

    for platform_name in ["macOS", "Android"]:
        if platform_name not in platforms_data:
            continue
        for exp_name, data in sorted(platforms_data[platform_name].items()):
            stats = data["stats"]
            if stats:
                lines.append(
                    f"| {platform_name} | {exp_name} | {stats.get('median', 0):.2f} | "
                    f"{stats.get('mean', 0):.2f} | {stats.get('min', 0):.2f} | "
                    f"{stats.get('max', 0):.2f} | {stats.get('stdev', 0):.2f} |"
                )

    lines.append("")

    # SME2 speedup comparison
    lines.append("## SME2 Speedup Comparison (SME2-On vs SME2-Off)\n")
    lines.append("| Platform | Speedup |")
    lines.append("|----------|---------|")

    for platform_name in ["macOS", "Android"]:
        if platform_name not in platforms_data:
            continue
        on_exp = None
        off_exp = None
        for exp_name, data in platforms_data[platform_name].items():
            if "sme2_on" in exp_name.lower():
                on_exp = data
            elif "sme2_off" in exp_name.lower():
                off_exp = data

        if on_exp and off_exp:
            on_median = on_exp["stats"].get("median", 0)
            off_median = off_exp["stats"].get("median", 0)
            if on_median > 0 and off_median > 0:
                speedup = off_median / on_median
                lines.append(f"| {platform_name} | {speedup:.2f}x |")

    lines.append("")

    # Operator category breakdown
    lines.append("## Operator Category Breakdown (Cross-Platform)\n")

    for platform_name in ["macOS", "Android"]:
        if platform_name not in platforms_data:
            continue

        lines.append(f"### {platform_name}\n")
        lines.append("| Category | SME2-On (ms) | SME2-Off (ms) |")
        lines.append("|----------|--------------|---------------|")

        # Find SME2-on and SME2-off experiments
        on_exp = None
        off_exp = None
        for exp_name, data in platforms_data[platform_name].items():
            if "sme2_on" in exp_name.lower():
                on_exp = data
            elif "sme2_off" in exp_name.lower():
                off_exp = data

        if on_exp and off_exp:
            on_cats = on_exp.get("category_totals", {})
            off_cats = off_exp.get("category_totals", {})
            all_cats = sorted(set(list(on_cats.keys()) + list(off_cats.keys())))
            for cat in all_cats:
                on_ms = on_cats.get(cat, 0)
                off_ms = off_cats.get(cat, 0)
                lines.append(f"| **{cat}** | {on_ms:.3f} | {off_ms:.3f} |")

        lines.append("")

    lines.append("---")
    lines.append("*Report generated from CSV files (derived from ETDump)*")

    report_content = "\n".join(lines)
    output_path.write_text(report_content, encoding="utf-8")
    print(f"Combined report written to: {output_path}")


def main():
    parser = argparse.ArgumentParser(description="Generate combined report from macOS and Android data")
    parser.add_argument("--mac-dir", type=Path, required=True, help="macOS run directory")
    parser.add_argument("--android-dir", type=Path, required=True, help="Android run directory")
    parser.add_argument("--out", type=Path, default=None, help="Output markdown file")
    parser.add_argument("--model-name", type=str, default="edgetam_image_encoder_xnnpack_fp32", help="Model name")
    args = parser.parse_args()

    mac_dir = args.mac_dir.resolve()
    android_dir = args.android_dir.resolve()

    if not mac_dir.exists() and not android_dir.exists():
        print(f"Error: Neither {mac_dir} nor {android_dir} exists", file=sys.stderr)
        return 1

    if args.out:
        output_path = args.out.resolve()
    else:
        # Default to parent of mac_dir or android_dir
        output_path = (mac_dir.parent if mac_dir.exists() else android_dir.parent) / "combined_report.md"

    try:
        generate_combined_report(mac_dir, android_dir, output_path, args.model_name)
    except Exception as e:
        print(f"Error generating combined report: {e}", file=sys.stderr)
        import traceback

        traceback.print_exc()
        return 1

    return 0


if __name__ == "__main__":
    exit(main())
