#!/usr/bin/env python3
import os
from .visualization import parse_benchstat, plot_metric_group, generate_html

class BenchstatReport:
    """
    Encapsulate benchstat report generation logic.
    """
    def generate_report(self, benchstat_file: str, out_dir: str):
        """Generate HTML report from benchstat results file."""
        if not os.path.exists(benchstat_file):
            print(f"Error: Benchstat file {benchstat_file} not found")
            return
            
        groups = parse_benchstat(benchstat_file)
        images = []
        for idx, (inst_a, inst_b, metric_name, df) in enumerate(groups):
            img_path = plot_metric_group(inst_a, inst_b, metric_name, df, out_dir, idx)
            images.append((img_path, metric_name, inst_a, inst_b))
        generate_html(images, out_dir)